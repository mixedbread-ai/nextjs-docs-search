---
title: Loading.js
path: "App / Api Reference / File Conventions / Loading"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/loading
content_length: 611
---

# loading.js
A **loading** file can create instant loading states built on Suspense.
By default, this file is a Server Component - but can also be used as a Client Component through the `"use client"` directive.
app/feed/loading.tsx
```
exportdefaultfunctionLoading() {
// Or a custom loading skeleton component
return <p>Loading...</p>
}
```

Loading UI components do not accept any parameters.
> **Good to know** :
>   * While designing loading UI, you may find it helpful to use the to manually toggle Suspense boundaries.
> 

## Version History
Version| Changes  
---|---  
`v13.0.0`| `loading` introduced.
