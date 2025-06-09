---
title: "How to use fonts"
path: "App / Getting Started / Fonts"
source_url: https://nextjs.org/docs/app/getting-started/fonts
content_length: 2858
---

# How to use fonts
The `next/font` module automatically optimizes your fonts and removes external network requests for improved privacy and performance.
It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.
To start using `next/font`, import it from `next/font/local` or `next/font/google`, call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:
app/layout.tsx
```
import { Geist } from'next/font/google'
constgeist=Geist({
 subsets: ['latin'],
})
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return (
  <htmllang="en"className={geist.className}>
   <body>{children}</body>
  </html>
 )
}
```

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the Root Layout.
## Google fonts
You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.
To start using a Google Font, import your chosen font from `next/font/google`:
app/layout.tsx
```
import { Geist } from'next/font/google'
constgeist=Geist({
 subsets: ['latin'],
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={geist.className}>
   <body>{children}</body>
  </html>
 )
}
```

We recommend using for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:
app/layout.tsx
```
import { Roboto } from'next/font/google'
constroboto=Roboto({
 weight:'400',
 subsets: ['latin'],
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={roboto.className}>
   <body>{children}</body>
  </html>
 )
}
```

## Local fonts
To use a local font, import your font from `next/font/local` and specify the `src` of your local font file. Fonts can be stored in the `public` folder. For example:
app/layout.tsx
```
import localFont from'next/font/local'
constmyFont=localFont({
 src:'./my-font.woff2',
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={myFont.className}>
   <body>{children}</body>
  </html>
 )
}
```

If you want to use multiple files for a single font family, `src` can be an array:
```
constroboto=localFont({
 src: [
  {
   path:'./Roboto-Regular.woff2',
   weight:'400',
   style:'normal',
  },
  {
   path:'./Roboto-Italic.woff2',
   weight:'400',
   style:'italic',
  },
  {
   path:'./Roboto-Bold.woff2',
   weight:'700',
   style:'normal',
  },
  {
   path:'./Roboto-BoldItalic.woff2',
   weight:'700',
   style:'italic',
  },
 ],
})
```
