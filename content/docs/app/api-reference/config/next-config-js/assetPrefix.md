---
title: AssetPrefix
path: "App / Api Reference / Config / Next Config Js / Assetprefix"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix
content_length: 1869
---

# assetPrefix
> **Attention** : Deploying to Vercel automatically configures a global CDN for your Next.js project. You do not need to manually setup an Asset Prefix.
> **Good to know** : Next.js 9.5+ added support for a customizable Base Path, which is better suited for hosting your application on a sub-path like `/docs`. We do not suggest you use a custom Asset Prefix for this use case.
## Set up a CDN
To set up a , you can set up an asset prefix and configure your CDN's origin to resolve to the domain that Next.js is hosted on.
Open `next.config.mjs` and add the `assetPrefix` config based on the phase:
next.config.mjs
```
// @ts-check
import { PHASE_DEVELOPMENT_SERVER } from'next/constants'
exportdefault (phase) => {
constisDev= phase ===PHASE_DEVELOPMENT_SERVER
/**
  * @type{import('next').NextConfig}
  */
constnextConfig= {
  assetPrefix: isDev ?undefined:'
 }
return nextConfig
}
```

Next.js will automatically use your asset prefix for the JavaScript and CSS files it loads from the `/_next/` path (`.next/static/` folder). For example, with the above configuration, the following request for a JS chunk:
```
/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js

```

Would instead become:
```


```

The exact configuration for uploading your files to a given CDN will depend on your CDN of choice. The only folder you need to host on your CDN is the contents of `.next/static/`, which should be uploaded as `_next/static/` as the above URL request indicates. **Do not upload the rest of your`.next/` folder**, as you should not expose your server code and other configuration to the public.
While `assetPrefix` covers requests to `_next/static`, it does not influence the following paths:
  * Files in the public folder; if you want to serve those assets over a CDN, you'll have to introduce the prefix yourself
