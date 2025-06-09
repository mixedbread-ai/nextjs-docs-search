---
title: ServerComponentsHmrCache
path: "App / Api Reference / Config / Next Config Js / Servercomponentshmrcache"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache
content_length: 1147
---

# serverComponentsHmrCache
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.
By default, the HMR cache applies to all `fetch` requests, including those with the `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.
You can disable the HMR cache by setting `serverComponentsHmrCache` to `false` in your `next.config.js` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  serverComponentsHmrCache:false,// defaults to true
 },
}
exportdefault nextConfig
```

> **Good to know:** For better observability, we recommend using the `logging.fetches` option which logs fetch cache hits and misses in the console during development.
