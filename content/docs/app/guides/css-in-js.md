---
title: "How to use CSS-in-JS libraries"
path: "App / Guides / Css In Js"
source_url: https://nextjs.org/docs/app/guides/css-in-js
content_length: 4641
---

# How to use CSS-in-JS libraries
> **Warning:** Using CSS-in-JS with newer React features like Server Components and Streaming requires library authors to support the latest version of React, including .
The following libraries are supported in Client Components in the `app` directory (alphabetical):
  * `styled-jsx`
  * `styled-components`


The following are currently working on support:
> **Good to know** : We're testing out different CSS-in-JS libraries and we'll be adding more examples for libraries that support React 18 features and/or the `app` directory.
## Configuring CSS-in-JS in `app`
Configuring CSS-in-JS is a three-step opt-in process that involves:
  1. A **style registry** to collect all CSS rules in a render.
  2. The new `useServerInsertedHTML` hook to inject rules before any content that might use them.
  3. A Client Component that wraps your app with the style registry during initial server-side rendering.


### `styled-jsx`
Using `styled-jsx` in Client Components requires using `v5.1.0`. First, create a new registry:
app/registry.tsx
```
'use client'
import React, { useState } from'react'
import { useServerInsertedHTML } from'next/navigation'
import { StyleRegistry, createStyleRegistry } from'styled-jsx'
exportdefaultfunctionStyledJsxRegistry({
 children,
}: {
 children:React.ReactNode
}) {
// Only create stylesheet once with lazy initial state
// x-ref: 
const [jsxStyleRegistry] =useState(() =>createStyleRegistry())
useServerInsertedHTML(() => {
conststyles=jsxStyleRegistry.styles()
jsxStyleRegistry.flush()
return <>{styles}</>
 })
return <StyleRegistryregistry={jsxStyleRegistry}>{children}</StyleRegistry>
}
```

Then, wrap your root layout with the registry:
app/layout.tsx
```
import StyledJsxRegistry from'./registry'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <html>
   <body>
    <StyledJsxRegistry>{children}</StyledJsxRegistry>
   </body>
  </html>
 )
}
```

.
### Styled Components
Below is an example of how to configure `styled-components@6` or newer:
First, enable styled-components in `next.config.js`.
next.config.js
```
module.exports= {
 compiler: {
  styledComponents:true,
 },
}
```

Then, use the `styled-components` API to create a global registry component to collect all CSS style rules generated during a render, and a function to return those rules. Then use the `useServerInsertedHTML` hook to inject the styles collected in the registry into the `<head>` HTML tag in the root layout.
lib/registry.tsx
```
'use client'
import React, { useState } from'react'
import { useServerInsertedHTML } from'next/navigation'
import { ServerStyleSheet, StyleSheetManager } from'styled-components'
exportdefaultfunctionStyledComponentsRegistry({
 children,
}: {
 children:React.ReactNode
}) {
// Only create stylesheet once with lazy initial state
// x-ref: 
const [styledComponentsStyleSheet] =useState(() =>newServerStyleSheet())
useServerInsertedHTML(() => {
conststyles=styledComponentsStyleSheet.getStyleElement()
styledComponentsStyleSheet.instance.clearTag()
return <>{styles}</>
 })
if (typeof window !=='undefined') return <>{children}</>
return (
  <StyleSheetManagersheet={styledComponentsStyleSheet.instance}>
   {children}
  </StyleSheetManager>
 )
}
```

Wrap the `children` of the root layout with the style registry component:
app/layout.tsx
```
import StyledComponentsRegistry from'./lib/registry'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <html>
   <body>
    <StyledComponentsRegistry>{children}</StyledComponentsRegistry>
   </body>
  </html>
 )
}
```

.
> **Good to know** :
>   * During server rendering, styles will be extracted to a global registry and flushed to the `<head>` of your HTML. This ensures the style rules are placed before any content that might use them. In the future, we may use an upcoming React feature to determine where to inject the styles.
>   * During streaming, styles from each chunk will be collected and appended to existing styles. After client-side hydration is complete, `styled-components` will take over as usual and inject any further dynamic styles.
>   * We specifically use a Client Component at the top level of the tree for the style registry because it's more efficient to extract CSS rules this way. It avoids re-generating styles on subsequent server renders, and prevents them from being sent in the Server Component payload.
>   * For advanced use cases where you need to configure individual properties of styled-components compilation, you can read our Next.js styled-components API reference to learn more.
>
