---
title: HttpAgentOptions
path: "App / Api Reference / Config / Next Config Js / Httpagentoptions"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions
content_length: 350
---

# httpAgentOptions
In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with undici and enables by default.
To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:
next.config.js
```
module.exports= {
 httpAgentOptions: {
  keepAlive:false,
 },
}
```
