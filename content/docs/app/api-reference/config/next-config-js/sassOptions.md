---
title: SassOptions
path: "App / Api Reference / Config / Next Config Js / Sassoptions"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions
content_length: 456
---

# sassOptions
`sassOptions` allow you to configure the Sass compiler.
next.config.ts
```
importtype { NextConfig } from'next'
constsassOptions= {
 additionalData:`
  $var: red;
 `,
}
constnextConfig:NextConfig= {
 sassOptions: {
...sassOptions,
  implementation:'sass-embedded',
 },
}
exportdefault nextConfig
```

> **Good to know:** `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
