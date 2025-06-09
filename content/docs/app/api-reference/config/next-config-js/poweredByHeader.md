---
title: PoweredByHeader
path: "App / Api Reference / Config / Next Config Js / Poweredbyheader"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader
content_length: 223
---

# poweredByHeader
By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:
next.config.js
```
module.exports= {
 poweredByHeader:false,
}
```
