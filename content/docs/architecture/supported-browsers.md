---
title: "Supported Browsers"
path: "Architecture / Supported Browsers"
source_url: https://nextjs.org/docs/architecture/supported-browsers
content_length: 1715
---

# Supported Browsers
Next.js supports **modern browsers** with zero configuration.
  * Chrome 64+
  * Edge 79+
  * Firefox 67+
  * Opera 51+
  * Safari 12+


## Browserslist
If you would like to target specific browsers or features, Next.js supports configuration in your `package.json` file. Next.js uses the following Browserslist configuration by default:
package.json
```
{
"browserslist": [
"chrome 64",
"edge 79",
"firefox 67",
"opera 51",
"safari 12"
 ]
}
```

## Polyfills
We inject , including:
  * — Replacing: `whatwg-fetch` and `unfetch`.
  * — Replacing: the .
  * — Replacing: `object-assign`, `object.assign`, and `core-js/object/assign`.


If any of your dependencies include these polyfills, they’ll be eliminated automatically from the production build to avoid duplication.
In addition, to reduce bundle size, Next.js will only load these polyfills for browsers that require them. The majority of the web traffic globally will not download these polyfills.
### Custom Polyfills
If your own code or any external npm dependencies require features not supported by your target browsers (such as IE 11), you need to add polyfills yourself.
In this case, you should add a top-level import for the **specific polyfill** you need in your Custom `<App>` or the individual component.
## JavaScript Language Features
Next.js allows you to use the latest JavaScript features out of the box. In addition to , Next.js also supports:
  * (ES2017)
  * (ES2018)
  * (ES2020)
  * (ES2020)
  * (ES2020)
  * and (ES2022)
  * and more!


### TypeScript Features
Next.js has built-in TypeScript support. Learn more here.
### Customizing Babel Config (Advanced)
You can customize babel configuration. Learn more here.
