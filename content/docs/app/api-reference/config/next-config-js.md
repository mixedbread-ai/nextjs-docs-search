---
title: Next.config.js
path: "App / Api Reference / Config / Next Config Js"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js
content_length: 3592
---

# next.config.js
Next.js can be configured through a `next.config.js` file in the root of your project directory (for example, by `package.json`) with a default export.
next.config.js
```
// @ts-check
/** @type{import('next').NextConfig} */
constnextConfig= {
/* config options here */
}
module.exports= nextConfig
```

## ECMAScript Modules
`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.
If you need , you can use `next.config.mjs`:
next.config.mjs
```
// @ts-check
/**
 * @type{import('next').NextConfig}
 */
constnextConfig= {
/* config options here */
}
exportdefault nextConfig
```

> **Good to know** : `next.config` with the `.cjs`, `.cts`, or `.mts` extensions are currently **not** supported.
## Configuration as a Function
You can also use a function:
next.config.mjs
```
// @ts-check
exportdefault (phase, { defaultConfig }) => {
/**
  * @type{import('next').NextConfig}
  */
constnextConfig= {
/* config options here */
 }
return nextConfig
}
```

### Async Configuration
Since Next.js 12.1.0, you can use an async function:
next.config.js
```
// @ts-check
module.exports=async (phase, { defaultConfig }) => {
/**
  * @type{import('next').NextConfig}
  */
constnextConfig= {
/* config options here */
 }
return nextConfig
}
```

### Phase
`phase` is the current context in which the configuration is loaded. You can see the . Phases can be imported from `next/constants`:
next.config.js
```
// @ts-check
const { PHASE_DEVELOPMENT_SERVER } =require('next/constants')
module.exports= (phase, { defaultConfig }) => {
if (phase ===PHASE_DEVELOPMENT_SERVER) {
return {
/* development only config options here */
  }
 }
return {
/* config options for all phases except development here */
 }
}
```

## TypeScript
If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
/* config options here */
}
exportdefault nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are .
However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.
> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.
This page documents all the available configuration options:
## Unit Testing (experimental)
Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test `next.config.js` files.
The `unstable_getResponseFromNextConfig` function runs the `headers`, `redirects`, and `rewrites` functions from `next.config.js` with the provided request information and returns `NextResponse` with the results of the routing.
> The response from `unstable_getResponseFromNextConfig` only considers `next.config.js` fields and does not consider middleware or filesystem routes, so the result in production may be different than the unit test.
```
import {
 getRedirectUrl,
 unstable_getResponseFromNextConfig,
} from'next/experimental/testing/server'
constresponse=awaitunstable_getResponseFromNextConfig({
 url:'
 nextConfig: {
asyncredirects() {
return [{ source:'/test', destination:'/test2', permanent:false }]
  },
 },
})
expect(response.status).toEqual(307)
expect(getRedirectUrl(response)).toEqual('
```
