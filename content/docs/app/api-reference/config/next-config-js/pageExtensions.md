---
title: PageExtensions
path: "App / Api Reference / Config / Next Config Js / Pageextensions"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions
content_length: 399
---

# pageExtensions
By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).
next.config.js
```
constwithMDX=require('@next/mdx')()
/** @type{import('next').NextConfig} */
constnextConfig= {
 pageExtensions: ['js','jsx','ts','tsx','md','mdx'],
}
module.exports=withMDX(nextConfig)
```
