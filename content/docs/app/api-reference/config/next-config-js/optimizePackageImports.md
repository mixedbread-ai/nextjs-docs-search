---
title: OptimizePackageImports
path: "App / Api Reference / Config / Next Config Js / Optimizepackageimports"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports
content_length: 1032
---

# optimizePackageImports
Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.
Adding a package to `experimental.optimizePackageImports` will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.
next.config.js
```
module.exports= {
 experimental: {
  optimizePackageImports: ['package-name'],
 },
}
```

The following libraries are optimized by default:
  * `lucide-react`
  * `date-fns`
  * `lodash-es`
  * `ramda`
  * `antd`
  * `react-bootstrap`
  * `ahooks`
  * `@ant-design/icons`
  * `@headlessui/react`
  * `@headlessui-float/react`
  * `@heroicons/react/20/solid`
  * `@heroicons/react/24/solid`
  * `@heroicons/react/24/outline`
  * `@visx/visx`
  * `@tremor/react`
  * `rxjs`
  * `@mui/material`
  * `@mui/icons-material`
  * `recharts`
  * `react-use`
  * `@material-ui/core`
  * `@material-ui/icons`
  * `@tabler/icons-react`
  * `mui-core`
  * `react-icons/*`
