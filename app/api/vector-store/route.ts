import { NextRequest, NextResponse } from "next/server";
import { mxbai } from "@/lib/mxbai";
import type { StoreSearchResponse } from "@mixedbread/sdk/resources/stores";

interface SearchMetadata {
  title?: string;
  path?: string;
  source_url?: string;
  [key: string]: any;
}

export async function GET(request: NextRequest) {
  if (!process.env.MXBAI_API_KEY || !process.env.STORE_ID) {
    return NextResponse.json(
      { error: "Environment setup failed" },
      { status: 500 }
    );
  }

  const { searchParams } = new URL(request.url);
  const query = searchParams.get("query");

  if (!query) {
    return NextResponse.json({ error: "Query is required" }, { status: 400 });
  }

  const res = await mxbai.stores.search({
    query,
    store_identifiers: [process.env.STORE_ID],
    top_k: 10,
    search_options: {
      return_metadata: true,
    },
  });

  // Deduplicate results based on file_id
  const uniqueResults = res.data.reduce((acc, item) => {
    if (!acc.some((existing) => existing.file_id === item.file_id)) {
      acc.push(item);
    }
    return acc;
  }, [] as StoreSearchResponse.Data[]);

  const fumaStructuredResponse = uniqueResults.flatMap((item, index) => {
    const metadata = item.generated_metadata as SearchMetadata;
    const url = metadata?.source_url || "";
    const description = metadata?.path || "";
    const title = metadata?.title || "Untitled";

    return [
      {
        id: `result-${index}-page`,
        url: url,
        type: "page",
        content: title,
      },
      {
        id: `result-${index}-text`,
        url: url,
        type: "text",
        content: description,
      },
    ];
  });

  return NextResponse.json(fumaStructuredResponse);
}
