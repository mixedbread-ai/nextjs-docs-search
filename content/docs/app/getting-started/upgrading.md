---
title: "How to upgrade your Next.js app"
path: "App / Getting Started / Upgrading"
source_url: https://nextjs.org/docs/app/getting-started/upgrading
content_length: 853
---

# How to upgrade your Next.js app
## Latest version
To update to the latest version of Next.js, you can use the `upgrade` codemod:
Terminal
```
npx@next/codemod@canaryupgradelatest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:
Terminal
```
npminext@latestreact@latestreact-dom@latesteslint-config-next@latest
```

## Canary version
To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:
Terminal
```
npminext@canary
```

### Features available in canary
The following features are currently available in canary:
**Caching** :
  * `"use cache"`
  * `cacheLife`
  * `cacheTag`
  * `dynamicIO`


**Authentication** :
  * `forbidden`
  * `unauthorized`
  * `forbidden.js`
  * `unauthorized.js`
  * `authInterrupts`
