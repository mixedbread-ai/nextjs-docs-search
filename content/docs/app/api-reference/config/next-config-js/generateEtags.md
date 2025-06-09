---
title: GenerateEtags
path: "App / Api Reference / Config / Next Config Js / Generateetags"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags
content_length: 282
---

# generateEtags
Next.js will generate for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.
Open `next.config.js` and disable the `generateEtags` option:
next.config.js
```
module.exports= {
 generateEtags:false,
}
```
