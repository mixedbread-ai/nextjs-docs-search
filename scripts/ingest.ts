import * as fs from 'fs';
import * as path from 'path';
import { glob } from 'glob';
import dotenv from 'dotenv';
import { mxbai } from '../lib/mxbai';

dotenv.config();

interface FrontmatterData {
  title?: string;
  path?: string;
  source_url?: string;
  content_length?: number;
  [key: string]: string | number | undefined;
}

interface FileMetadata extends FrontmatterData {
  file_path: string;
  file_name: string;
  text: string;
}

function parseFrontmatter(fileContent: string): { frontmatter: FrontmatterData; content: string } {
  if (!fileContent.startsWith('---')) {
    return { frontmatter: {}, content: fileContent };
  }

  const parts = fileContent.split('---');
  if (parts.length < 3) {
    return { frontmatter: {}, content: fileContent };
  }

  const frontmatterText = parts[1].trim();
  const content = parts.slice(2).join('---').trim();
  
  const frontmatter: FrontmatterData = {};
  const lines = frontmatterText.split('\n');
  
  for (const line of lines) {
    const colonIndex = line.indexOf(':');
    if (colonIndex > 0) {
      const key = line.substring(0, colonIndex).trim();
      let value = line.substring(colonIndex + 1).trim();
      
      if (value.startsWith('"') && value.endsWith('"')) {
        value = value.slice(1, -1);
      }
      
      if (key === 'content_length' && !isNaN(Number(value))) {
        frontmatter[key] = Number(value);
      } else {
        frontmatter[key] = value;
      }
    }
  }

  return { frontmatter, content };
}

async function uploadFiles(): Promise<void> {
  console.log('Starting NextJS Documentation Ingestion');
  
  const VECTOR_STORE_ID = process.env.VECTOR_STORE_ID;
  if (!VECTOR_STORE_ID) {
    throw new Error('Missing vector store ID');
  }

  const mdFiles = await glob('content/**/*.md', { ignore: ['**/node_modules/**'] });
  console.log(`Found ${mdFiles.length} markdown files to upload`);

  for (let i = 0; i < mdFiles.length; i++) {
    const filePath = mdFiles[i];
    
    try {
      console.log(`[${i + 1}/${mdFiles.length}] Processing: ${filePath}`);

      const fileContent = fs.readFileSync(filePath, 'utf-8');
      const { frontmatter } = parseFrontmatter(fileContent);
      const fileName = path.basename(filePath);

      const metadata: FileMetadata = {
        ...frontmatter,
        file_path: filePath,
        file_name: fileName,
        // Save the actual text for potential reranking after search
        text: fileContent,
      };

      const fileBuffer = fs.readFileSync(filePath);
      const file = new File([fileBuffer], fileName, { type: 'text/plain' });

      const response = await mxbai.vectorStores.files.upload(
        VECTOR_STORE_ID,
        file,
        { metadata: metadata }
      );

      console.log(`Uploaded: ${fileName} - ID: ${response.id}`);

    } catch (error) {
      console.error(`Failed to process ${filePath}:`, error);
    }
  }

  console.log('\n' + '='.repeat(60));
  console.log('Ingestion Complete!');
}

async function main(): Promise<void> {
  if (!process.env.MXBAI_API_KEY) {
    console.error('Error: MXBAI_API_KEY environment variable not set');
    console.error('Please add your mixedbread API key to your .env file');
    process.exit(1);
  }

  if (!process.env.VECTOR_STORE_ID) {
    console.error('Error: VECTOR_STORE_ID environment variable not set');
    console.error('Please add your vector store ID to your .env file');
    process.exit(1);
  }

  if (!fs.existsSync('content')) {
    console.error('Error: content directory not found');
    console.error('Please ensure the content directory exists with markdown files');
    process.exit(1);
  }

  await uploadFiles();
}

if (require.main === module) {
  main().catch(console.error);
}
