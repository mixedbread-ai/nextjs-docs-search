---
title: CssChunking
path: "App / Api Reference / Config / Next Config Js / Csschunking"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking
content_length: 1793
---

# cssChunking
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
CSS Chunking is a strategy used to improve the performance of your web application by splitting and re-ordering CSS files into chunks. This allows you to load only the CSS that is needed for a specific route, instead of loading all the application's CSS at once.
You can control how CSS files are chunked using the `experimental.cssChunking` option in your `next.config.js` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig= {
 experimental: {
  cssChunking:true,// default
 },
} satisfiesNextConfig
exportdefault nextConfig
```

## Options
  * **`true`(default)** : Next.js will try to merge CSS files whenever possible, determining explicit and implicit dependencies between files from import order to reduce the number of chunks and therefore the number of requests.
  * **`false`**: Next.js will not attempt to merge or re-order your CSS files.
  * **`'strict'`**: Next.js will load CSS files in the correct order they are imported into your files, which can lead to more chunks and requests.


You may consider using `'strict'` if you run into unexpected CSS behavior. For example, if you import `a.css` and `b.css` in different files using a different `import` order (`a` before `b`, or `b` before `a`), `true` will merge the files in any order and assume there are no dependencies between them. However, if `b.css` depends on `a.css`, you may want to use `'strict'` to prevent the files from being merged, and instead, load them in the order they are imported - which can result in more chunks and requests.
For most applications, we recommend `true` as it leads to fewer requests and better performance.
