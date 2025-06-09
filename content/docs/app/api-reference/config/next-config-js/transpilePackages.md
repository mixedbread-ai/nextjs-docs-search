---
title: TranspilePackages
path: "App / Api Reference / Config / Next Config Js / Transpilepackages"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages
content_length: 453
---

# transpilePackages
Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 transpilePackages: ['package-name'],
}
module.exports= nextConfig
```

## Version History
Version| Changes  
---|---  
`v13.0.0`| `transpilePackages` added.
