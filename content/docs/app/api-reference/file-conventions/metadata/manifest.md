---
title: Manifest.json
path: "App / Api Reference / File Conventions / Metadata / Manifest"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest
content_length: 1312
---

# manifest.json
Add or generate a `manifest.(json|webmanifest)` file that matches the in the **root** of `app` directory to provide information about your web application for the browser.
## Static Manifest file
app/manifest.json | app/manifest.webmanifest
```
{
"name":"My Next.js Application",
"short_name":"Next.js App",
"description":"An application built with Next.js",
"start_url":"/"
// ...
}
```

## Generate a Manifest file
Add a `manifest.js` or `manifest.ts` file that returns a `Manifest` object.
> Good to know: `manifest.js` is special Route Handlers that is cached by default unless it uses a Dynamic API or dynamic config option.
app/manifest.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionmanifest():MetadataRoute.Manifest {
return {
  name:'Next.js App',
  short_name:'Next.js App',
  description:'Next.js App',
  start_url:'/',
  display:'standalone',
  background_color:'#fff',
  theme_color:'#fff',
  icons: [
   {
    src:'/favicon.ico',
    sizes:'any',
    type:'image/x-icon',
   },
  ],
 }
}
```

### Manifest Object
The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using TypeScript or see the docs.
