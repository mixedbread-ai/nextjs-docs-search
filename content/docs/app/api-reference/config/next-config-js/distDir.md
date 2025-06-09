---
title: DistDir
path: "App / Api Reference / Config / Next Config Js / Distdir"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir
content_length: 412
---

# distDir
You can specify a name to use for a custom build directory to use instead of `.next`.
Open `next.config.js` and add the `distDir` config:
next.config.js
```
module.exports= {
 distDir:'build',
}
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.
> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.
