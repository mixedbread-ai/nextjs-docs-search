---
title: Typescript
path: "App / Api Reference / Config / Next Config Js / Typescript"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript
content_length: 711
---

# typescript
Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.
If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.
If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.
Open `next.config.js` and enable the `ignoreBuildErrors` option in the `typescript` config:
next.config.js
```
module.exports= {
 typescript: {
// !! WARN !!
// Dangerously allow production builds to successfully complete even if
// your project has type errors.
// !! WARN !!
  ignoreBuildErrors:true,
 },
}
```
