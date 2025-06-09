---
title: ReactCompiler
path: "App / Api Reference / Config / Next Config Js / Reactcompiler"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler
content_length: 2039
---

# reactCompiler
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
Next.js includes support for the , a tool designed to improve performance by automatically optimizing component rendering. This reduces the need for manual memoization using `useMemo` and `useCallback`.
Next.js includes a custom performance optimization written in SWC that makes the React Compiler more efficient. Instead of running the compiler on every file, Next.js analyzes your project and only applies the React Compiler to relevant files. This avoids unnecessary work and leads to faster builds compared to using the Babel plugin on its own.
## How It Works
The React Compiler runs through a Babel plugin. To keep builds fast, Next.js uses a custom SWC optimization that only applies the React Compiler to relevant files—like those with JSX or React Hooks.
This avoids compiling everything and keeps the performance cost minimal. You may still see slightly slower builds compared to the default Rust-based compiler, but the impact is small and localized.
To use it, install the `babel-plugin-react-compiler`:
Terminal
```
npminstallbabel-plugin-react-compiler
```

Then, add `experimental.reactCompiler` option in `next.config.js`:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  reactCompiler:true,
 },
}
exportdefault nextConfig
```

## Annotations
You can configure the compiler to run in "opt-in" mode as follows:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  reactCompiler: {
   compilationMode:'annotation',
  },
 },
}
exportdefault nextConfig
```

Then, you can annotate specific components or hooks with the `"use memo"` directive from React to opt-in:
app/page.tsx
```
exportdefaultfunctionPage() {
'use memo'
// ...
}
```

> **Note:** You can also use the `"use no memo"` directive from React for the opposite effect, to opt-out a component or hook.
