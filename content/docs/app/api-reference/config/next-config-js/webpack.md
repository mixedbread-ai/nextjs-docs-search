---
title: "Custom Webpack Config"
path: "App / Api Reference / Config / Next Config Js / Webpack"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack
content_length: 2235
---

# Custom Webpack Config
> **Good to know** : changes to webpack config are not covered by semver so proceed at your own risk
Before continuing to add custom webpack configuration to your application make sure Next.js doesn't already support your use-case:
  * CSS imports
  * CSS modules
  * Sass/SCSS imports
  * Sass/SCSS modules


Some commonly asked for features are available as plugins:
In order to extend our usage of `webpack`, you can define a function that extends its config inside `next.config.js`, like so:
next.config.js
```
module.exports= {
webpack: (
  config,
  { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
 ) => {
// Important: return the modified config
return config
 },
}
```

> The `webpack` function is executed three times, twice for the server (nodejs / edge runtime) and once for the client. This allows you to distinguish between client and server configuration using the `isServer` property.
The second argument to the `webpack` function is an object with the following properties:
  * `buildId`: `String` - The build id, used as a unique identifier between builds.
  * `dev`: `Boolean` - Indicates if the compilation will be done in development.
  * `isServer`: `Boolean` - It's `true` for server-side compilation, and `false` for client-side compilation.
  * `nextRuntime`: `String | undefined` - The target runtime for server-side compilation; either `"edge"` or `"nodejs"`, it's `undefined` for client-side compilation.
  * `defaultLoaders`: `Object` - Default loaders used internally by Next.js: 
    * `babel`: `Object` - Default `babel-loader` configuration.


Example usage of `defaultLoaders.babel`:
```
// Example config for adding a loader that depends on babel-loader
// This source was taken from the @next/mdx plugin source:
// 
module.exports= {
webpack: (config, options) => {
config.module.rules.push({
   test: /\.mdx/,
   use: [
options.defaultLoaders.babel,
    {
     loader:'@mdx-js/loader',
     options:pluginOptions.options,
    },
   ],
  })
return config
 },
}
```

#### `nextRuntime`
Notice that `isServer` is `true` when `nextRuntime` is `"edge"` or `"nodejs"`, `nextRuntime` `"edge"` is currently for middleware and Server Components in edge runtime only.
