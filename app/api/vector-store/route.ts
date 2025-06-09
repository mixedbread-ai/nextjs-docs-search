import { NextRequest, NextResponse } from "next/server";
import { mxbai } from "@/lib/mxbai";
import { ScoredVectorStoreFile } from "@mixedbread/sdk/resources/vector-stores/files";

interface SearchMetadata {
  title?: string;
  path?: string;
  source_url?: string;
  content_length?: string;
  scraped_date?: string;
  file_path?: string;
  file_name?: string;
  [key: string]: string | number | undefined;
}

export async function GET(request: NextRequest) {
  if (!process.env.MXBAI_API_KEY || !process.env.VECTOR_STORE_ID) {
    return NextResponse.json({ error: "Environment setup failed" }, { status: 500 });
  }

  const { searchParams } = new URL(request.url);
  const query = searchParams.get("query");

  if (!query) {
    return NextResponse.json({ error: "Query is required" }, { status: 400 });
  }

  const res = await mxbai.vectorStores.files.search({
    query,
    vector_store_ids: [process.env.VECTOR_STORE_ID],
    top_k: 5,
    search_options: {
      return_metadata: true,
      return_chunks: true,
      chunks_per_file: 2,
    },
  });


  const fumaStructuredResponse = res.data.flatMap((item: ScoredVectorStoreFile) => [
    {
      id: item.id,
      url: (item.metadata as SearchMetadata)?.source_url || '#',
      type: "page",
      content: (item.metadata as SearchMetadata)?.title || 'Untitled',
    },
    {
      id: `${item.id}-text`,
      url: (item.metadata as SearchMetadata)?.source_url || '#',
      type: "text", 
      content: (item.metadata as SearchMetadata)?.path || 'No path available',
    },
  ]);
  
  return NextResponse.json(fumaStructuredResponse);
}