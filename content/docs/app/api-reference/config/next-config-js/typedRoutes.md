---
title: TypedRoutes
path: "App / Api Reference / Config / Next Config Js / Typedroutes"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes
content_length: 437
---

# typedRoutes
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
Experimental support for statically typed links. This feature requires using the App Router as well as TypeScript in your project.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 experimental: {
  typedRoutes:true,
 },
}
module.exports= nextConfig
```
