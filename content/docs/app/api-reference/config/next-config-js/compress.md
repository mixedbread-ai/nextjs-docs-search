---
title: Compress
path: "App / Api Reference / Config / Next Config Js / Compress"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/compress
content_length: 971
---

# compress
By default, Next.js uses `gzip` to compress rendered content and static files when using `next start` or a custom server. This is an optimization for applications that do not have compression configured. If compression is _already_ configured in your application via a custom server, Next.js will not add compression.
You can check if compression is enabled and which algorithm is used by looking at the (browser accepted options) and (currently used) headers in the response.
## Disabling compression
To disable **compression** , set the `compress` config option to `false`:
next.config.js
```
module.exports= {
 compress:false,
}
```

We **do not recommend disabling compression** unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using and want to switch to `brotli`, set the `compress` option to `false` to allow nginx to handle compression.
