---
title: MdxRs
path: "App / Api Reference / Config / Next Config Js / Mdxrs"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs
content_length: 323
---

# mdxRs
For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.
next.config.js
```
constwithMDX=require('@next/mdx')()
/** @type{import('next').NextConfig} */
constnextConfig= {
 pageExtensions: ['ts','tsx','mdx'],
 experimental: {
  mdxRs:true,
 },
}
module.exports=withMDX(nextConfig)
```
