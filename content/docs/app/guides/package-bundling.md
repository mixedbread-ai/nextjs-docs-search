---
title: "How to optimize package bundling"
path: "App / Guides / Package Bundling"
source_url: https://nextjs.org/docs/app/guides/package-bundling
content_length: 2746
---

# How to optimize package bundling
Bundling external packages can significantly improve the performance of your application. By default, packages imported inside Server Components and Route Handlers are automatically bundled by Next.js. This page will guide you through how to analyze and further optimize package bundling. 
## Analyzing JavaScript bundles
is a plugin for Next.js that helps you manage the size of your application bundles. It generates a visual report of the size of each package and their dependencies. You can use the information to remove large dependencies, split, or lazy-load your code.
### Installation
Install the plugin by running the following command:
```
npmi@next/bundle-analyzer
# or
yarnadd@next/bundle-analyzer
# or
pnpmadd@next/bundle-analyzer
```

Then, add the bundle analyzer's settings to your `next.config.js`.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {}
constwithBundleAnalyzer=require('@next/bundle-analyzer')({
 enabled:process.env.ANALYZE==='true',
})
module.exports=withBundleAnalyzer(nextConfig)
```

### Generating a report
Run the following command to analyze your bundles:
```
ANALYZE=truenpmrunbuild
# or
ANALYZE=trueyarnbuild
# or
ANALYZE=truepnpmbuild
```

The report will open three new tabs in your browser, which you can inspect. Periodically evaluating your application's bundles can help you maintain application performance over time.
## Optimizing package imports
Some packages, such as icon libraries, can export hundreds of modules, which can cause performance issues in development and production.
You can optimize how these packages are imported by adding the `optimizePackageImports` option to your `next.config.js`. This option will only load the modules you _actually_ use, while still giving you the convenience of writing import statements with many named exports.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 experimental: {
  optimizePackageImports: ['icon-library'],
 },
}
module.exports= nextConfig
```

Next.js also optimizes some libraries automatically, thus they do not need to be included in the optimizePackageImports list. See the full list.
## Opting specific packages out of bundling
Since packages imported inside Server Components and Route Handlers are automatically bundled by Next.js, you can opt specific packages out of bundling using the `serverExternalPackages` option in your `next.config.js`.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 serverExternalPackages: ['package-name'],
}
module.exports= nextConfig
```

Next.js includes a list of popular packages that currently are working on compatibility and automatically opt-ed out. See the full list.
