---
title: AllowedDevOrigins
path: "App / Api Reference / Config / Next Config Js / Alloweddevorigins"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins
content_length: 796
---

# allowedDevOrigins
Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.
To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default) you can use the `allowedDevOrigins` config option.
`allowedDevOrigins` allows you to set additional origins that can be used in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:
next.config.js
```
module.exports= {
 allowedDevOrigins: ['local-origin.dev','*.local-origin.dev'],
}
```
