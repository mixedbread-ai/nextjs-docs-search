---
title: "Font Module"
path: "App / Api Reference / Components / Font"
source_url: https://nextjs.org/docs/app/api-reference/components/font
content_length: 17361
---

# Font Module
`next/font` automatically optimizes your fonts (including custom fonts) and removes external network requests for improved privacy and performance.
It includes **built-in automatic self-hosting** for any font file. This means you can optimally load web fonts with no .
You can also conveniently use all . CSS and font files are downloaded at build time and self-hosted with the rest of your static assets. **No requests are sent to Google by the browser.**
app/layout.tsx
```
import { Inter } from'next/font/google'
// If loading a variable font, you don't need to specify the font weight
constinter=Inter({
 subsets: ['latin'],
 display:'swap',
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={inter.className}>
   <body>{children}</body>
  </html>
 )
}
```

> **🎥 Watch:** Learn more about using `next/font` → .
## Reference
Key| `font/google`| `font/local`| Type| Required  
---|---|---|---|---  
`src`| | | String or Array of Objects| Yes  
`weight`| | | String or Array| Required/Optional  
`style`| | | String or Array| -  
`subsets`| | | Array of Strings| -  
`axes`| | | Array of Strings| -  
`display`| | | String| -  
`preload`| | | Boolean| -  
`fallback`| | | Array of Strings| -  
`adjustFontFallback`| | | Boolean or String| -  
`variable`| | | String| -  
`declarations`| | | Array of Objects| -  
### `src`
The path of the font file as a string or an array of objects (with type `Array<{path: string, weight?: string, style?: string}>`) relative to the directory where the font loader function is called.
Used in `next/font/local`
  * Required


Examples:
  * `src:'./fonts/my-font.woff2'` where `my-font.woff2` is placed in a directory named `fonts` inside the `app` directory
  * `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
  * if the font loader function is called in `app/page.tsx` using `src:'../styles/fonts/my-font.ttf'`, then `my-font.ttf` is placed in `styles/fonts` at the root of the project


### `weight`
The font with the following possibilities:
  * A string with possible values of the weights available for the specific font or a range of values if it's a font
  * An array of weight values if the font is not a . It applies to `next/font/google` only.


Used in `next/font/google` and `next/font/local`
  * Required if the font being used is **not**


Examples:
  * `weight: '400'`: A string for a single weight value - for the font , the possible values are `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'` or `'variable'` where `'variable'` is the default)
  * `weight: '100 900'`: A string for the range between `100` and `900` for a variable font
  * `weight: ['100','400','900']`: An array of 3 possible values for a non variable font


### `style`
The font with the following possibilities:
  * A string with default value of `'normal'`
  * An array of style values if the font is not a . It applies to `next/font/google` only.


Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `style: 'italic'`: A string - it can be `normal` or `italic` for `next/font/google`
  * `style: 'oblique'`: A string - it can take any value for `next/font/local` but is expected to come from 
  * `style: ['italic','normal']`: An array of 2 values for `next/font/google` - the values are from `normal` and `italic`


### `subsets`
The font defined by an array of string values with the names of each subset you would like to be preloaded. Fonts specified via `subsets` will have a link preload tag injected into the head when the `preload` option is true, which is the default.
Used in `next/font/google`
  * Optional


Examples:
  * `subsets: ['latin']`: An array with the subset `latin`


You can find a list of all subsets on the Google Fonts page for your font.
### `axes`
Some variable fonts have extra `axes` that can be included. By default, only the font weight is included to keep the file size down. The possible values of `axes` depend on the specific font.
Used in `next/font/google`
  * Optional


Examples:
  * `axes: ['slnt']`: An array with value `slnt` for the `Inter` variable font which has `slnt` as additional `axes` as shown . You can find the possible `axes` values for your font by using the filter on the and looking for axes other than `wght`


### `display`
The font with possible string of `'auto'`, `'block'`, `'swap'`, `'fallback'` or `'optional'` with default value of `'swap'`.
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `display: 'optional'`: A string assigned to the `optional` value


### `preload`
A boolean value that specifies whether the font should be preloaded or not. The default is `true`.
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `preload: false`


### `fallback`
The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.
  * Optional


Used in `next/font/google` and `next/font/local`
Examples:
  * `fallback: ['system-ui', 'arial']`: An array setting the fallback fonts to `system-ui` or `arial`


### `adjustFontFallback`
  * For `next/font/google`: A boolean value that sets whether an automatic fallback font should be used to reduce . The default is `true`.
  * For `next/font/local`: A string or boolean `false` value that sets whether an automatic fallback font should be used to reduce . The possible values are `'Arial'`, `'Times New Roman'` or `false`. The default is `'Arial'`.


Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `adjustFontFallback: false`: for `next/font/google`
  * `adjustFontFallback: 'Times New Roman'`: for `next/font/local`


### `variable`
A string value to define the CSS variable name to be used if the style is applied with the CSS variable method.
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `variable: '--my-font'`: The CSS variable `--my-font` is declared


### `declarations`
An array of font face key-value pairs that define the generated `@font-face` further.
Used in `next/font/local`
  * Optional


Examples:
  * `declarations: [{ prop: 'ascent-override', value: '90%' }]`


## Examples
## Google Fonts
To use a Google font, import it from `next/font/google` as a function. We recommend using for the best performance and flexibility.
app/layout.tsx
```
import { Inter } from'next/font/google'
// If loading a variable font, you don't need to specify the font weight
constinter=Inter({
 subsets: ['latin'],
 display:'swap',
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={inter.className}>
   <body>{children}</body>
  </html>
 )
}
```

If you can't use a variable font, you will **need to specify a weight** :
app/layout.tsx
```
import { Roboto } from'next/font/google'
constroboto=Roboto({
 weight:'400',
 subsets: ['latin'],
 display:'swap',
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

You can specify multiple weights and/or styles by using an array:
app/layout.js
```
constroboto=Roboto({
 weight: ['400','700'],
 style: ['normal','italic'],
 subsets: ['latin'],
 display:'swap',
})
```

> **Good to know** : Use an underscore (_) for font names with multiple words. E.g. `Roboto Mono` should be imported as `Roboto_Mono`.
### Specifying a subset
Google Fonts are automatically . This reduces the size of the font file and improves performance. You'll need to define which of these subsets you want to preload. Failing to specify any subsets while `preload` is `true` will result in a warning.
This can be done by adding it to the function call:
app/layout.tsx
```
constinter=Inter({ subsets: ['latin'] })
```

View the Font API Reference for more information.
## Using Multiple Fonts
You can import and use multiple fonts in your application. There are two approaches you can take.
The first approach is to create a utility function that exports a font, imports it, and applies its `className` where needed. This ensures the font is preloaded only when it's rendered:
app/fonts.ts
```
import { Inter, Roboto_Mono } from'next/font/google'
exportconstinter=Inter({
 subsets: ['latin'],
 display:'swap',
})
exportconstroboto_mono=Roboto_Mono({
 subsets: ['latin'],
 display:'swap',
})
```

app/layout.tsx
```
import { inter } from'./fonts'
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return (
  <htmllang="en"className={inter.className}>
   <body>
    <div>{children}</div>
   </body>
  </html>
 )
}
```

app/page.tsx
```
import { roboto_mono } from'./fonts'
exportdefaultfunctionPage() {
return (
  <>
   <h1className={roboto_mono.className}>My page</h1>
  </>
 )
}
```

In the example above, `Inter` will be applied globally, and `Roboto Mono` can be imported and applied as needed.
Alternatively, you can create a CSS variable and use it with your preferred CSS solution:
app/layout.tsx
```
import { Inter, Roboto_Mono } from'next/font/google'
import styles from'./global.css'
constinter=Inter({
 subsets: ['latin'],
 variable:'--font-inter',
 display:'swap',
})
constroboto_mono=Roboto_Mono({
 subsets: ['latin'],
 variable:'--font-roboto-mono',
 display:'swap',
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en"className={`${inter.variable}${roboto_mono.variable}`}>
   <body>
    <h1>My App</h1>
    <div>{children}</div>
   </body>
  </html>
 )
}
```

app/global.css
```
html {
font-family:var(--font-inter);
}
h1 {
font-family:var(--font-roboto-mono);
}
```

In the example above, `Inter` will be applied globally, and any `<h1>` tags will be styled with `Roboto Mono`.
> **Recommendation** : Use multiple fonts conservatively since each new font is an additional resource the client has to download.
### Local Fonts
Import `next/font/local` and specify the `src` of your local font file. We recommend using for the best performance and flexibility.
app/layout.tsx
```
import localFont from'next/font/local'
// Font files can be colocated inside of `app`
constmyFont=localFont({
 src:'./my-font.woff2',
 display:'swap',
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

View the Font API Reference for more information.
### With Tailwind CSS
`next/font` integrates seamlessly with using CSS variables.
In the example below, we use the `Inter` and `Roboto_Mono` fonts from `next/font/google` (you can use any Google Font or Local Font). Use the `variable` option to define a CSS variable name, such as `inter` and `roboto_mono` for these fonts, respectively. Then, apply `inter.variable` and `roboto_mono.variable` to include the CSS variables in your HTML document.
> **Good to know** : You can add these variables to the `<html>` or `<body>` tag, depending on your preference, styling needs or project requirements.
app/layout.tsx
```
import { Inter, Roboto_Mono } from'next/font/google'
constinter=Inter({
 subsets: ['latin'],
 display:'swap',
 variable:'--font-inter',
})
constroboto_mono=Roboto_Mono({
 subsets: ['latin'],
 display:'swap',
 variable:'--font-roboto-mono',
})
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <html
lang="en"
className={`${inter.variable}${roboto_mono.variable} antialiased`}
  >
   <body>{children}</body>
  </html>
 )
}
```

Finally, add the CSS variable to your Tailwind CSS config:
### Tailwind CSS v4
As of , there is zero configuration required by default. If you do need to configure Tailwind, you can follow the for configuring the global CSS file.
global.css
```
@import "tailwindcss";
@theme inline {
--font-sans:var(--font-inter);
--font-mono:var(--font-roboto-mono);
}
```

### Tailwind CSS v3
tailwind.config.js
```
/** @type{import('tailwindcss').Config} */
module.exports= {
 content: [
'./pages/**/*.{js,ts,jsx,tsx}',
'./components/**/*.{js,ts,jsx,tsx}',
'./app/**/*.{js,ts,jsx,tsx}',
 ],
 theme: {
  extend: {
   fontFamily: {
    sans: ['var(--font-inter)'],
    mono: ['var(--font-roboto-mono)'],
   },
  },
 },
 plugins: [],
}
```

You can now use the `font-sans` and `font-mono` utility classes to apply the font to your elements.
```
<p class="font-sans ...">The quick brown fox ...</p>
<p class="font-mono ...">The quick brown fox ...</p>

```

### Applying Styles
You can apply the font styles in three ways:
  * `className`
  * `style`
  * CSS Variables


#### `className`
Returns a read-only CSS `className` for the loaded font to be passed to an HTML element.
```
<pclassName={inter.className}>Hello, Next.js!</p>
```

#### `style`
Returns a read-only CSS `style` object for the loaded font to be passed to an HTML element, including `style.fontFamily` to access the font family name and fallback fonts.
```
<pstyle={inter.style}>Hello World</p>
```

#### CSS Variables
If you would like to set your styles in an external style sheet and specify additional options there, use the CSS variable method.
In addition to importing the font, also import the CSS file where the CSS variable is defined and set the variable option of the font loader object as follows:
app/page.tsx
```
import { Inter } from'next/font/google'
import styles from'../styles/component.module.css'
constinter=Inter({
 variable:'--font-inter',
})
```

To use the font, set the `className` of the parent container of the text you would like to style to the font loader's `variable` value and the `className` of the text to the `styles` property from the external CSS file.
app/page.tsx
```
<mainclassName={inter.variable}>
 <pclassName={styles.text}>Hello World</p>
</main>
```

Define the `text` selector class in the `component.module.css` CSS file as follows:
styles/component.module.css
```
.text {
font-family:var(--font-inter);
font-weight:200;
font-style:italic;
}
```

In the example above, the text `Hello World` is styled using the `Inter` font and the generated font fallback with `font-weight: 200` and `font-style: italic`.
### Using a font definitions file
Every time you call the `localFont` or Google font function, that font will be hosted as one instance in your application. Therefore, if you need to use the same font in multiple places, you should load it in one place and import the related font object where you need it. This is done using a font definitions file.
For example, create a `fonts.ts` file in a `styles` folder at the root of your app directory.
Then, specify your font definitions as follows:
styles/fonts.ts
```
import { Inter, Lora, Source_Sans_3 } from'next/font/google'
import localFont from'next/font/local'
// define your variable fonts
constinter=Inter()
constlora=Lora()
// define 2 weights of a non-variable font
constsourceCodePro400=Source_Sans_3({ weight:'400' })
constsourceCodePro700=Source_Sans_3({ weight:'700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
constgreatVibes=localFont({ src:'./GreatVibes-Regular.ttf' })
export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

You can now use these definitions in your code as follows:
app/page.tsx
```
import { inter, lora, sourceCodePro700, greatVibes } from'../styles/fonts'
exportdefaultfunctionPage() {
return (
  <div>
   <pclassName={inter.className}>Hello world using Inter font</p>
   <pstyle={lora.style}>Hello world using Lora font</p>
   <pclassName={sourceCodePro700.className}>
    Hello world using Source_Sans_3 font with weight 700
   </p>
   <pclassName={greatVibes.className}>My title in Great Vibes font</p>
  </div>
 )
}
```

To make it easier to access the font definitions in your code, you can define a path alias in your `tsconfig.json` or `jsconfig.json` files as follows:
tsconfig.json
```
{
"compilerOptions": {
"paths": {
"@/fonts": ["./styles/fonts"]
  }
 }
}
```

You can now import any font definition as follows:
app/about/page.tsx
```
import { greatVibes, sourceCodePro400 } from'@/fonts'
```

### Preloading
When a font function is called on a page of your site, it is not globally available and preloaded on all routes. Rather, the font is only preloaded on the related routes based on the type of file where it is used:
  * If it's a unique page, it is preloaded on the unique route for that page.
  * If it's a layout, it is preloaded on all the routes wrapped by the layout.
  * If it's the root layout, it is preloaded on all routes.


## Version Changes
Version| Changes  
---|---  
`v13.2.0`| `@next/font` renamed to `next/font`. Installation no longer required.  
`v13.0.0`| `@next/font` was added.
