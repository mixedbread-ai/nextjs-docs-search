---
title: "How to upgrade to version 14"
path: "App / Guides / Upgrading / Version 14"
source_url: https://nextjs.org/docs/app/guides/upgrading/version-14
content_length: 1273
---

# How to upgrade to version 14
## Upgrading from 13 to 14
To update to Next.js version 14, run the following command using your preferred package manager:
Terminal
```
npminext@next-14react@18react-dom@18&&npmieslint-config-next@next-14-D
```

Terminal
```
yarnaddnext@next-14react@18react-dom@18&&yarnaddeslint-config-next@next-14-D
```

Terminal
```
pnpminext@next-14react@18react-dom@18&&pnpmieslint-config-next@next-14-D
```

Terminal
```
bunaddnext@next-14react@18react-dom@18&&bunaddeslint-config-next@next-14-D
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.
### v14 Summary
  * The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life.
  * The `next export` command has been removed in favor of `output: 'export'` config. Please see the docs for more information.
  * The `next/server` import for `ImageResponse` was renamed to `next/og`. A codemod is available to safely and automatically rename your imports.
  * The `@next/font` package has been fully removed in favor of the built-in `next/font`. A codemod is available to safely and automatically rename your imports.
  * The WASM target for `next-swc` has been removed.
