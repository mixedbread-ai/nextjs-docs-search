---
title: OnDemandEntries
path: "App / Api Reference / Config / Next Config Js / Ondemandentries"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries
content_length: 496
---

# onDemandEntries
Next.js exposes some options that give you some control over how the server will dispose or keep in memory built pages in development.
To change the defaults, open `next.config.js` and add the `onDemandEntries` config:
next.config.js
```
module.exports= {
 onDemandEntries: {
// period (in ms) where the server will keep pages in the buffer
  maxInactiveAge:25*1000,
// number of pages that should be kept simultaneously without being disposed
  pagesBufferLength:2,
 },
}
```
