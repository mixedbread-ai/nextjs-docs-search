---
title: AuthInterrupts
path: "App / Api Reference / Config / Next Config Js / Authinterrupts"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts
content_length: 566
---

# authInterrupts
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on .
The `authInterrupts` configuration option allows you to use `forbidden` and `unauthorized` APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  authInterrupts:true,
 },
}
exportdefault nextConfig
```
