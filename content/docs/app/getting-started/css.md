---
title: "How to use CSS in your application"
path: "App / Getting Started / Css"
source_url: https://nextjs.org/docs/app/getting-started/css
content_length: 4040
---

# How to use CSS in your application
Next.js provides several ways to use CSS in your application, including:
  * CSS Modules
  * Global CSS
  * External Stylesheets
  * Tailwind CSS
  * Sass
  * CSS-in-JS


## CSS Modules
CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.
To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `app` directory:
app/blog/blog.module.css
```
.blog {
padding:24px;
}
```

app/blog/page.tsx
```
import styles from'./blog.module.css'
exportdefaultfunctionPage() {
return <mainclassName={styles.blog}></main>
}
```

## Global CSS
You can use global CSS to apply styles across your application.
Create a `app/global.css` file and import it in the root layout to apply the styles to **every route** in your application:
app/global.css
```
body {
padding:20px 20px 60px;
max-width:680px;
margin:0 auto;
}
```

app/layout.tsx
```
// These styles apply to every route in the application
import'./global.css'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <body>{children}</body>
  </html>
 )
}
```

> **Good to know:** Global styles can be imported into any layout, page, or component inside the `app` directory. However, since Next.js uses React's built-in support for stylesheets to integrate with Suspense, this currently does not remove stylesheets as you navigate between routes which can lead to conflicts. We recommend using global styles for _truly_ global CSS, and CSS Modules for scoped CSS.
## External stylesheets
Stylesheets published by external packages can be imported anywhere in the `app` directory, including colocated components:
app/layout.tsx
```
import'bootstrap/dist/css/bootstrap.css'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <bodyclassName="container">{children}</body>
  </html>
 )
}
```

> **Good to know:** In React 19, `<link rel="stylesheet" href="..." />` can also be used. See the for more information.
## Ordering and Merging
Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.
For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:
page.ts
```
import { BaseButton } from'./base-button'
import styles from'./page.module.css'
exportdefaultfunctionPage() {
return <BaseButtonclassName={styles.primary} />
}
```

base-button.tsx
```
import styles from'./base-button.module.css'
exportfunctionBaseButton() {
return <buttonclassName={styles.primary} />
}
```

### Recommendations
To keep CSS ordering predictable:
  * Try to contain CSS imports to a single JavaScript or TypeScript entry file
  * Import global styles and Tailwind stylesheets in the root of your application.
  * Use CSS Modules instead of global styles for nested components.
  * Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
  * Extract shared styles into shared components to avoid duplicate imports.
  * Turn off linters or formatters that auto-sort imports like ESLint’s .
  * You can use the `cssChunking` option in `next.config.js` to control how CSS is chunked.


## Development vs Production
  * In development (`next dev`), CSS updates apply instantly with Fast Refresh.
  * In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
  * CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
  * CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.
