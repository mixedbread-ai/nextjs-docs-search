---
title: Mdx-components.js
path: "App / Api Reference / File Conventions / Mdx Components"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components
content_length: 1323
---

# mdx-components.js
The `mdx-components.js|tsx` file is **required** to use `@next/mdx` with App Router and will not work without it. Additionally, you can use it to customize styles.
Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.
mdx-components.tsx
```
importtype { MDXComponents } from'mdx/types'
exportfunctionuseMDXComponents(components:MDXComponents):MDXComponents {
return {
...components,
 }
}
```

## Exports
### `useMDXComponents` function
The file must export a single function, either as a default export or named `useMDXComponents`.
mdx-components.tsx
```
importtype { MDXComponents } from'mdx/types'
exportfunctionuseMDXComponents(components:MDXComponents):MDXComponents {
return {
...components,
 }
}
```

## Params
### `components`
When defining MDX Components, the export function accepts a single parameter, `components`. This parameter is an instance of `MDXComponents`.
  * The key is the name of the HTML element to override.
  * The value is the component to render instead.


> **Good to know** : Remember to pass all other components (i.e. `...components`) that do not have overrides.
## Version History
Version| Changes  
---|---  
`v13.1.2`| MDX Components added
