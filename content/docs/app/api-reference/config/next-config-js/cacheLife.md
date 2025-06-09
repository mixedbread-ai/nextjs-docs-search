---
title: CacheLife
path: "App / Api Reference / Config / Next Config Js / Cachelife"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife
content_length: 1631
---

# cacheLife
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on .
The `cacheLife` option allows you to define **custom cache profiles** when using the `cacheLife` function inside components or functions, and within the scope of the `use cache` directive.
## Usage
To define a profile, enable the `dynamicIO` flag and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  dynamicIO:true,
  cacheLife: {
   blog: {
    stale:3600,// 1 hour
    revalidate:900,// 15 minutes
    expire:86400,// 1 day
   },
  },
 },
}
exportdefault nextConfig
```

You can now use this custom `blog` configuration in your component or function as follows:
app/actions.ts
```
import { unstable_cacheLife as cacheLife } from'next/cache'
exportasyncfunctiongetCachedData() {
'use cache'
cacheLife('blog')
constdata=awaitfetch('/api/data')
return data
}
```

## Reference
The configuration object has key values with the following format:
**Property**| **Value**| **Description**| **Requirement**  
---|---|---|---  
`stale`| `number`|  Duration the client should cache a value without checking the server.| Optional  
`revalidate`| `number`| Frequency at which the cache should refresh on the server; stale values may be served while revalidating.| Optional  
`expire`| `number`| Maximum duration for which a value can remain stale before switching to dynamic.| Optional - Must be longer than `revalidate`
