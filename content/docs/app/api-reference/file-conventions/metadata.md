---
title: "Metadata Files API Reference"
path: "App / Api Reference / File Conventions / Metadata"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/metadata
content_length: 832
---

# Metadata Files API Reference
This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.
Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).
Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.
> **Good to know** :
>   * Special Route Handlers like `sitemap.ts`, `opengraph-image.tsx`, and `icon.tsx`, and other metadata files are cached by default.
>   * If using along with `middleware.ts`, configure the matcher to exclude the metadata files.
>
