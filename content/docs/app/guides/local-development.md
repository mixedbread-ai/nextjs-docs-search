---
title: "How to optimize your local development environment"
path: "App / Guides / Local Development"
source_url: https://nextjs.org/docs/app/guides/local-development
content_length: 6356
---

# How to optimize your local development environment
Next.js is designed to provide a great developer experience. As your application grows, you might notice slower compilation times during local development. This guide will help you identify and fix common compile-time performance issues.
## Local dev vs. production
The development process with `next dev` is different than `next build` and `next start`.
`next dev` compiles routes in your application as you open or navigate to them. This enables you to start the dev server without waiting for every route in your application to compile, which is both faster and uses less memory. Running a production build applies other optimizations, like minifying files and creating content hashes, which are not needed for local development.
## Improving local dev performance
### 1. Check your computer's antivirus
Antivirus software can slow down file access.
Try adding your project folder to the antivirus exclusion list. While this is more common on Windows machines, we recommend this for any system with an antivirus tool installed.
### 2. Update Next.js and enable Turbopack
Make sure you're using the latest version of Next.js. Each new version often includes performance improvements.
Turbopack is a new bundler integrated into Next.js that can improve local performance.
```
npminstallnext@latest
npmrundev--turbopack
```

Learn more about Turbopack. See our upgrade guides and codemods for more information.
### 3. Check your imports
The way you import code can greatly affect compilation and bundling time. Learn more about optimizing package bundling and explore tools like or .
### Icon libraries
Libraries like `@material-ui/icons` or `react-icons` can import thousands of icons, even if you only use a few. Try to import only the icons you need:
```
// Instead of this:
import { Icon1, Icon2 } from'react-icons/md'
// Do this:
import Icon1 from'react-icons/md/Icon1'
import Icon2 from'react-icons/md/Icon2'
```

Libraries like `react-icons` includes many different icon sets. Choose one set and stick with that set.
For example, if your application uses `react-icons` and imports all of these:
  * `pi` (Phosphor Icons)
  * `md` (Material Design Icons)
  * `tb` (tabler-icons)
  * `cg` (cssgg)


Combined they will be tens of thousands of modules that the compiler has to handle, even if you only use a single import from each.
### Barrel files
"Barrel files" are files that export many items from other files. They can slow down builds because the compiler has to parse them to find if there are side-effects in the module scope by using the import.
Try to import directly from specific files when possible. and the built-in optimizations in Next.js.
### Optimize package imports
Next.js can automatically optimize imports for certain packages. If you are using packages that utilize barrel files, add them to your `next.config.js`:
```
module.exports= {
 experimental: {
  optimizePackageImports: ['package-name'],
 },
}
```

Turbopack automatically analyzes imports and optimizes them. It does not require this configuration.
### 4. Check your Tailwind CSS setup
If you're using Tailwind CSS, make sure it's set up correctly.
A common mistake is configuring your `content` array in a way which includes `node_modules` or other large directories of files that should not be scanned.
Tailwind CSS version 3.4.8 or newer will warn you about settings that might slow down your build.
  1. In your `tailwind.config.js`, be specific about which files to scan:
```
module.exports= {
 content: [
'./src/**/*.{js,ts,jsx,tsx}',// Good
// This might be too broad
// It will match `packages/**/node_modules` too
// '../../packages/**/*.{js,ts,jsx,tsx}',
 ],
}
```

  2. Avoid scanning unnecessary files:
```
module.exports= {
 content: [
// Better - only scans the 'src' folder
'../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
 ],
}
```



### 5. Check custom webpack settings
If you've added custom webpack settings, they might be slowing down compilation.
Consider if you really need them for local development. You can optionally only include certain tools for production builds, or explore moving to Turbopack and using loaders.
### 6. Optimize memory usage
If your app is very large, it might need more memory.
Learn more about optimizing memory usage.
### 7. Server Components and data fetching
Changes to Server Components cause the entire page to re-render locally in order to show the new changes, which includes fetching new data for the component.
The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.
Learn more about the experimental option.
## Tools for finding problems
### Detailed fetch logging
Use the `logging.fetches` option in your `next.config.js` file, to see more detailed information about what's happening during development:
```
module.exports= {
 logging: {
  fetches: {
   fullUrl:true,
  },
 },
}
```

Learn more about fetch logging.
## Turbopack tracing
Turbopack tracing is a tool that helps you understand the performance of your application during local development. It provides detailed information about the time taken for each module to compile and how they are related.
  1. Make sure you have the latest version of Next.js installed.
  2. Generate a Turbopack trace file:
```
NEXT_TURBOPACK_TRACING=1npmrundev
```

  3. Navigate around your application or make edits to files to reproduce the problem.
  4. Stop the Next.js development server.
  5. A file called `trace-turbopack` will be available in the `.next` folder.
  6. You can interpret the file using `next internal trace [path-to-file]`:
```
nextinternaltrace.next/trace-turbopack
```

On versions where `trace` is not available, the command was named `turbo-trace-server`:
```
nextinternalturbo-trace-server.next/trace-turbopack
```

  7. Once the trace server is running you can view the trace at <>.
  8. By default the trace viewer will aggregate timings, in order to see each individual time you can switch from "Aggregated in order" to "Spans in order" at the top right of the viewer.


## Still having problems?
Share the trace file generated in the Turbopack Tracing section and share it on or Discord.
