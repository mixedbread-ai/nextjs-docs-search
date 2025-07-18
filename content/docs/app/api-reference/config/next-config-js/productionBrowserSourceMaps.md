---
title: ProductionBrowserSourceMaps
path: "App / Api Reference / Config / Next Config Js / Productionbrowsersourcemaps"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps
content_length: 737
---

# productionBrowserSourceMaps
Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.
Next.js provides a configuration flag you can use to enable browser source map generation during the production build:
next.config.js
```
module.exports= {
 productionBrowserSourceMaps:true,
}
```

When the `productionBrowserSourceMaps` option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.
  * Adding source maps can increase `next build` time
  * Increases memory usage during `next build`
