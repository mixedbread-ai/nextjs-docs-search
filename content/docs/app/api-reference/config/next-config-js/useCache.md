---
title: UseCache
path: "App / Api Reference / Config / Next Config Js / Usecache"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/useCache
content_length: 855
---

# useCache
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on .
The `useCache` flag is an experimental feature in Next.js that enables the `use cache` directive to be used independently of `dynamicIO`. When enabled, you can use `use cache` in your application even if `dynamicIO` is turned off.
## Usage
To enable the `useCache` flag, set it to `true` in the `experimental` section of your `next.config.ts` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  useCache:true,
 },
}
exportdefault nextConfig
```

When `useCache` is enabled, you can use the following cache functions and configurations:
  * The `use cache` directive
  * The `cacheLife` function with `use cache`
  * The `cacheTag` function
