from mixedbread import Mixedbread
import os
from dotenv import load_dotenv
import glob
from pathlib import Path

load_dotenv()

# Initialize mixedbread client
mxbai = Mixedbread(
    api_key=os.getenv("MXBAI_API_KEY"),
)

# Vector store ID for NextJS documentation
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")
DOCS_DIR = "docs"


def upload_text_files():
    """Upload all text files from the docs directory to the vector store"""

    print("🚀 Starting NextJS Documentation Ingestion")
    print(f"📁 Source directory: {DOCS_DIR}")
    print(f"🔗 Vector store ID: {VECTOR_STORE_ID}")
    print("=" * 60)

    # Find all text files
    txt_files = glob.glob(f"{DOCS_DIR}/**/*.txt", recursive=True)

    # Filter out progress files
    txt_files = [f for f in txt_files if not f.endswith("_crawl_progress.json")]

    print(f"📄 Found {len(txt_files)} text files to upload")

    if not txt_files:
        print("❌ No text files found in the docs directory")
        return

    uploaded_count = 0
    failed_count = 0

    for i, file_path in enumerate(txt_files, 1):
        try:
            print(f"\n📤 [{i}/{len(txt_files)}] Uploading: {file_path}")

            # Read the file content to extract metadata from frontmatter
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract metadata from frontmatter if present
            metadata = {}

            if content.startswith("---"):
                try:
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1].strip()

                        for line in frontmatter.split("\n"):
                            if ":" in line:
                                key, value = line.split(":", 1)
                                key = key.strip()
                                value = value.strip().strip('"')
                                metadata[key] = value
                except:
                    pass

            # Add file path and full text content to metadata
            metadata["file_path"] = file_path
            metadata["file_name"] = Path(file_path).name
            metadata["text"] = content

            # Upload file directly to vector store using tuple format
            with open(file_path, "rb") as f:
                file_content = f.read()

            # Use tuple format: (filename, file_content, content_type)
            file_tuple = (Path(file_path).name, file_content, "text/plain")

            response = mxbai.vector_stores.files.upload(
                vector_store_id=VECTOR_STORE_ID,
                file=file_tuple,
                metadata=metadata,
            )

            print(response)
            uploaded_count += 1

        except Exception as e:
            print(f"❌ Failed to upload {file_path}: {str(e)}")
            failed_count += 1

    # Final summary
    print("\n" + "=" * 60)
    print("🎉 Ingestion Complete!")
    print(f"✅ Successfully uploaded: {uploaded_count} files")
    print(f"❌ Failed uploads: {failed_count} files")
    print(f"📊 Success rate: {(uploaded_count / len(txt_files) * 100):.1f}%")

    if uploaded_count > 0:
        print(f"\n🔍 You can now search the vector store with ID: {VECTOR_STORE_ID}")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("MXBAI_API_KEY"):
        print("❌ Error: MXBAI_API_KEY environment variable not set")
        print("Please add your mixedbread API key to your .env file")
        exit(1)

    # Check if vector store ID is set
    if not VECTOR_STORE_ID:
        print("❌ Error: VECTOR_STORE_ID environment variable not set")
        print("Please add your vector store ID to your .env file")
        exit(1)

    # Check if docs directory exists
    if not os.path.exists(DOCS_DIR):
        print(f"❌ Error: {DOCS_DIR} directory not found")
        print("Please run the scraper first to generate documentation files")
        exit(1)

    # Upload files
    upload_text_files()
