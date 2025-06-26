import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center text-center bg-fd-background px-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="mb-6 text-4xl font-bold">Next.js Docs Demo</h1>
        <p className="text-xl text-muted-foreground">
          Powered by{" "}
          <a
            href="https://www.mixedbread.com/docs/vector-stores/overview"
            target="_blank"
            rel="noopener noreferrer"
            className="underline"
          >
            Mixedbread Vector Stores
          </a>
        </p>
        <p className="text-xl text-muted-foreground">
          Automated CI/CD with the{" "}
          <a
            href="https://www.mixedbread.com/cli"
            target="_blank"
            rel="noopener noreferrer"
            className="underline"
          >
            Mixedbread CLI
          </a>
        </p>
      </div>
    </main>
  );
}
