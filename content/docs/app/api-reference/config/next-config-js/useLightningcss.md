---
title: UseLightningcss
path: "App / Api Reference / Config / Next Config Js / Uselightningcss"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss
content_length: 403
---

# useLightningcss
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
Experimental support for using , a fast CSS bundler and minifier, written in Rust.
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  useLightningcss:true,
 },
}
exportdefault nextConfig
```
