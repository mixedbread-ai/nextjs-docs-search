---
title: GenerateViewport
path: "App / Api Reference / Functions / Generate Viewport"
source_url: https://nextjs.org/docs/app/api-reference/functions/generate-viewport
content_length: 3967
---

# generateViewport
You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.
> **Good to know** :
>   * The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
>   * You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
>   * If you're coming from migrating `metadata` exports, you can use metadata-to-viewport-export codemod to update your changes.
> 

## The `viewport` object
To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.
layout.tsx | page.tsx
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 themeColor:'black',
}
exportdefaultfunctionPage() {}
```

## `generateViewport` function
`generateViewport` should return a `Viewport` object containing one or more viewport fields.
layout.tsx | page.tsx
```
exportfunctiongenerateViewport({ params }) {
return {
  themeColor:'...',
 }
}
```

> **Good to know** :
>   * If the viewport doesn't depend on runtime information, it should be defined using the static `viewport` object rather than `generateViewport`.
> 

## Viewport Fields
### `themeColor`
Learn more about .
**Simple theme color**
layout.tsx | page.tsx
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 themeColor:'black',
}
```

<head> output
```
<metaname="theme-color"content="black" />
```

**With media attribute**
layout.tsx | page.tsx
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 themeColor: [
  { media:'(prefers-color-scheme: light)', color:'cyan' },
  { media:'(prefers-color-scheme: dark)', color:'black' },
 ],
}
```

<head> output
```
<metaname="theme-color"media="(prefers-color-scheme: light)"content="cyan" />
<metaname="theme-color"media="(prefers-color-scheme: dark)"content="black" />
```

### `width`, `initialScale`, `maximumScale` and `userScalable`
> **Good to know** : The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.
layout.tsx | page.tsx
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 width:'device-width',
 initialScale:1,
 maximumScale:1,
 userScalable:false,
// Also supported but less commonly used
// interactiveWidget: 'resizes-visual',
}
```

<head> output
```
<meta
name="viewport"
content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

### `colorScheme`
Learn more about .
layout.tsx | page.tsx
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 colorScheme:'dark',
}
```

<head> output
```
<metaname="color-scheme"content="dark" />
```

## Types
You can add type safety to your viewport object by using the `Viewport` type. If you are using the built-in TypeScript plugin in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.
### `viewport` object
```
importtype { Viewport } from'next'
exportconstviewport:Viewport= {
 themeColor:'black',
}
```

### `generateViewport` function
#### Regular function
```
importtype { Viewport } from'next'
exportfunctiongenerateViewport():Viewport {
return {
  themeColor:'black',
 }
}
```

#### With segment props
```
importtype { Viewport } from'next'
typeProps= {
 params:Promise<{ id:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}
exportfunctiongenerateViewport({ params, searchParams }:Props):Viewport {
return {
  themeColor:'black',
 }
}
exportdefaultfunctionPage({ params, searchParams }:Props) {}
```

#### JavaScript Projects
For JavaScript projects, you can use JSDoc to add type safety.
```
/** @type{import("next").Viewport} */
exportconstviewport= {
 themeColor:'black',
}
```

## Version History
Version| Changes  
---|---  
`v14.0.0`| `viewport` and `generateViewport` introduced.
