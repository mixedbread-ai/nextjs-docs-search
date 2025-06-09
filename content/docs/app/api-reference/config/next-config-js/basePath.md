---
title: BasePath
path: "App / Api Reference / Config / Next Config Js / Basepath"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath
content_length: 1474
---

# basePath
To deploy a Next.js application under a sub-path of a domain you can use the `basePath` config option.
`basePath` allows you to set a path prefix for the application. For example, to use `/docs` instead of `''` (an empty string, the default), open `next.config.js` and add the `basePath` config:
next.config.js
```
module.exports= {
 basePath:'/docs',
}
```

> **Good to know** : This value must be set at build time and cannot be changed without re-building as the value is inlined in the client-side bundles.
### Links
When linking to other pages using `next/link` and `next/router` the `basePath` will be automatically applied.
For example, using `/about` will automatically become `/docs/about` when `basePath` is set to `/docs`.
```
exportdefaultfunctionHomePage() {
return (
  <>
   <Linkhref="/about">About Page</Link>
  </>
 )
}
```

Output html:
```
<ahref="/docs/about">About Page</a>
```

This makes sure that you don't have to change all links in your application when changing the `basePath` value.
### Images
When using the `next/image` component, you will need to add the `basePath` in front of `src`.
For example, using `/docs/me.png` will properly serve your image when `basePath` is set to `/docs`.
```
import Image from'next/image'
functionHome() {
return (
  <>
   <h1>My Homepage</h1>
   <Image
src="/docs/me.png"
alt="Picture of the author"
width={500}
height={500}
   />
   <p>Welcome to my homepage!</p>
  </>
 )
}
exportdefault Home
```
