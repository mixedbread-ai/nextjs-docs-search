---
title: "How to use Sass"
path: "App / Guides / Sass"
source_url: https://nextjs.org/docs/app/guides/sass
content_length: 1671
---

# How to use Sass
Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.
First, install :
Terminal
```
npminstall--save-devsass
```

> **Good to know** :
> Sass supports , each with their own extension. The `.scss` extension requires you use the , while the `.sass` extension requires you use the .
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").
### Customizing Sass Options
If you want to configure your Sass options, use `sassOptions` in `next.config`.
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 sassOptions: {
  additionalData:`$var: red;`,
 },
}
exportdefault nextConfig
```

#### Implementation
You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the package.
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 sassOptions: {
  implementation:'sass-embedded',
 },
}
exportdefault nextConfig
```

### Sass Variables
Next.js supports Sass variables exported from CSS Module files.
For example, using the exported `primaryColor` Sass variable:
app/variables.module.scss
```
$primary-color: #64ff00;
:export {
primaryColor:$primary-color;
}
```

app/page.js
```
// maps to root `/` URL
import variables from'./variables.module.scss'
exportdefaultfunctionPage() {
return <h1style={{ color:variables.primaryColor }}>Hello, Next.js!</h1>
}
```
