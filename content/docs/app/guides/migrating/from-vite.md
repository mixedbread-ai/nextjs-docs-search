---
title: "How to migrate from Vite to Next.js"
path: "App / Guides / Migrating / From Vite"
source_url: https://nextjs.org/docs/app/guides/migrating/from-vite
content_length: 16406
---

# How to migrate from Vite to Next.js
This guide will help you migrate an existing Vite application to Next.js.
## Why Switch?
There are several reasons why you might want to switch from Vite to Next.js:
### Slow initial page loading time
If you have built your application with the , your application is a purely client-side application. Client-side only applications, also known as single-page applications (SPAs), often experience slow initial page loading time. This happens due to a couple of reasons:
  1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load some data.
  2. Your application code grows with every new feature and extra dependency you add.


### No automatic code splitting
The previous issue of slow loading times can be somewhat managed with code splitting. However, if you try to do code splitting manually, you'll often make performance worse. It's easy to inadvertently introduce network waterfalls when code-splitting manually. Next.js provides automatic code splitting built into its router.
### Network waterfalls
A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One common pattern for data fetching in an SPA is to initially render a placeholder, and then fetch data after the component has mounted. Unfortunately, this means that a child component that fetches data can't start fetching until the parent component has finished loading its own data.
While fetching data on the client is supported with Next.js, it also gives you the option to shift data fetching to the server, which can eliminate client-server waterfalls.
### Fast and intentional loading states
With built-in support for streaming through React Suspense, you can be more intentional about which parts of your UI you want to load first and in what order without introducing network waterfalls.
This enables you to build pages that are faster to load and eliminate .
### Choose the data fetching strategy
Depending on your needs, Next.js allows you to choose your data fetching strategy on a page and component basis. You can decide to fetch at build time, at request time on the server, or on the client. For example, you can fetch data from your CMS and render your blog posts at build time, which can then be efficiently cached on a CDN.
### Middleware
Next.js Middleware allows you to run code on the server before a request is completed. This is especially useful to avoid having a flash of unauthenticated content when the user visits an authenticated-only page by redirecting the user to a login page. The middleware is also useful for experimentation and internationalization.
### Built-in Optimizations
Images, fonts, and third-party scripts often have significant impact on an application's performance. Next.js comes with built-in components that automatically optimize those for you.
## Migration Steps
Our goal with this migration is to get a working Next.js application as quickly as possible, so that you can then adopt Next.js features incrementally. To begin with, we'll keep it as a purely client-side application (SPA) without migrating your existing router. This helps minimize the chances of encountering issues during the migration process and reduces merge conflicts.
### Step 1: Install the Next.js Dependency
The first thing you need to do is to install `next` as a dependency:
Terminal
```
npminstallnext@latest
```

### Step 2: Create the Next.js Configuration File
Create a `next.config.mjs` at the root of your project. This file will hold your Next.js configuration options.
next.config.mjs
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 output:'export',// Outputs a Single-Page Application (SPA).
 distDir:'./dist',// Changes the build output directory to `./dist/`.
}
exportdefault nextConfig
```

> **Good to know:** You can use either `.js` or `.mjs` for your Next.js configuration file.
### Step 3: Update TypeScript Configuration
If you're using TypeScript, you need to update your `tsconfig.json` file with the following changes to make it compatible with Next.js. If you're not using TypeScript, you can skip this step.
  1. Remove the to `tsconfig.node.json`
  2. Add `./dist/types/**/*.ts` and `./next-env.d.ts` to the 
  3. Add `./node_modules` to the 
  4. Add `{ "name": "next" }` to the : `"plugins": [{ "name": "next" }]`
  5. Set to `true`: `"esModuleInterop": true`
  6. Set to `preserve`: `"jsx": "preserve"`
  7. Set to `true`: `"allowJs": true`
  8. Set to `true`: `"forceConsistentCasingInFileNames": true`
  9. Set to `true`: `"incremental": true`


Here's an example of a working `tsconfig.json` with those changes:
tsconfig.json
```
{
"compilerOptions": {
"target":"ES2020",
"useDefineForClassFields":true,
"lib": ["ES2020","DOM","DOM.Iterable"],
"module":"ESNext",
"esModuleInterop":true,
"skipLibCheck":true,
"moduleResolution":"bundler",
"allowImportingTsExtensions":true,
"resolveJsonModule":true,
"isolatedModules":true,
"noEmit":true,
"jsx":"preserve",
"strict":true,
"noUnusedLocals":true,
"noUnusedParameters":true,
"noFallthroughCasesInSwitch":true,
"allowJs":true,
"forceConsistentCasingInFileNames":true,
"incremental":true,
"plugins": [{ "name":"next" }]
 },
"include": ["./src","./dist/types/**/*.ts","./next-env.d.ts"],
"exclude": ["./node_modules"]
}
```

You can find more information about configuring TypeScript on the Next.js docs.
### Step 4: Create the Root Layout
A Next.js App Router application must include a root layout file, which is a React Server Component that will wrap all pages in your application. This file is defined at the top level of the `app` directory.
The closest equivalent to the root layout file in a Vite application is the , which contains your `<html>`, `<head>`, and `<body>` tags.
In this step, you'll convert your `index.html` file into a root layout file:
  1. Create a new `app` directory in your `src` folder.
  2. Create a new `layout.tsx` file inside that `app` directory:


app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return'...'
}
```

> **Good to know** : `.js`, `.jsx`, or `.tsx` extensions can be used for Layout files.
  1. Copy the content of your `index.html` file into the previously created `<RootLayout>` component while replacing the `body.div#root` and `body.script` tags with `<div id="root">{children}</div>`:


app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <head>
    <metacharset="UTF-8" />
    <linkrel="icon"type="image/svg+xml"href="/icon.svg" />
    <metaname="viewport"content="width=device-width, initial-scale=1.0" />
    <title>My App</title>
    <metaname="description"content="My App is a..." />
   </head>
   <body>
    <divid="root">{children}</div>
   </body>
  </html>
 )
}
```

  1. Next.js already includes by default the and tags, so you can safely remove those from your `<head>`:


app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <head>
    <linkrel="icon"type="image/svg+xml"href="/icon.svg" />
    <title>My App</title>
    <metaname="description"content="My App is a..." />
   </head>
   <body>
    <divid="root">{children}</div>
   </body>
  </html>
 )
}
```

  1. Any metadata files such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application `<head>` tag as long as you have them placed into the top level of the `app` directory. After moving all supported files into the `app` directory you can safely delete their `<link>` tags:


app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <head>
    <title>My App</title>
    <metaname="description"content="My App is a..." />
   </head>
   <body>
    <divid="root">{children}</div>
   </body>
  </html>
 )
}
```

  1. Finally, Next.js can manage your last `<head>` tags with the Metadata API. Move your final metadata info into an exported `metadata` object:


app/layout.tsx
```
importtype { Metadata } from'next'
exportconstmetadata:Metadata= {
 title:'My App',
 description:'My App is a...',
}
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <body>
    <divid="root">{children}</div>
   </body>
  </html>
 )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js' convention-based approach built into the framework (Metadata API). This approach enables you to more easily improve your SEO and web shareability of your pages.
### Step 5: Create the Entrypoint Page
On Next.js you declare an entrypoint for your application by creating a `page.tsx` file. The closest equivalent of this file on Vite is your `main.tsx` file. In this step, you’ll set up the entrypoint of your application.
  1. **Create a`[[...slug]]` directory in your `app` directory.**


Since in this guide we're aiming first to set up our Next.js as an SPA (Single Page Application), you need your page entrypoint to catch all possible routes of your application. For that, create a new `[[...slug]]` directory in your `app` directory.
This directory is what is called an optional catch-all route segment. Next.js uses a file-system based router where folders are used to define routes. This special directory will make sure that all routes of your application will be directed to its containing `page.tsx` file.
  1. **Create a new`page.tsx` file inside the `app/[[...slug]]` directory with the following content:**


app/[[...slug]]/page.tsx
```
import'../../index.css'
exportfunctiongenerateStaticParams() {
return [{ slug: [''] }]
}
exportdefaultfunctionPage() {
return'...'// We'll update this
}
```

> **Good to know** : `.js`, `.jsx`, or `.tsx` extensions can be used for Page files.
This file is a Server Component. When you run `next build`, the file is prerendered into a static asset. It does _not_ require any dynamic code.
This file imports our global CSS and tells `generateStaticParams` we are only going to generate one route, the index route at `/`.
Now, let's move the rest of our Vite application which will run client-only.
app/[[...slug]]/client.tsx
```
'use client'
import React from'react'
import dynamic from'next/dynamic'
constApp=dynamic(() =>import('../../App'), { ssr:false })
exportfunctionClientOnly() {
return <App />
}
```

This file is a Client Component, defined by the `'use client'` directive. Client Components are still prerendered to HTML on the server before being sent to the client.
Since we want a client-only application to start, we can configure Next.js to disable prerendering from the `App` component down.
```
constApp=dynamic(() =>import('../../App'), { ssr:false })
```

Now, update your entrypoint page to use the new component:
app/[[...slug]]/page.tsx
```
import'../../index.css'
import { ClientOnly } from'./client'
exportfunctiongenerateStaticParams() {
return [{ slug: [''] }]
}
exportdefaultfunctionPage() {
return <ClientOnly />
}
```

### Step 6: Update Static Image Imports
Next.js handles static image imports slightly different from Vite. With Vite, importing an image file will return its public URL as a string:
App.tsx
```
import image from'./img.png'// `image` will be '/assets/img.2d8efhg.png' in production
exportdefaultfunctionApp() {
return <imgsrc={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the Next.js `<Image>` component, or you can use the object's `src` property with your existing `<img>` tag.
The `<Image>` component has the added benefits of automatic image optimization. The `<Image>` component automatically sets the `width` and `height` attributes of the resulting `<img>` based on the image's dimensions. This prevents layout shifts when the image loads. However, this can cause issues if your app contains images with only one of their dimensions being styled without the other styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension attribute's value, which can cause the image to appear distorted.
Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by configuring a loader, or moving to the default Next.js server which has automatic image optimization.
  1. **Convert absolute import paths for images imported from`/public` into relative imports:**


```
// Before
import logo from'/logo.png'
// After
import logo from'../public/logo.png'
```

  1. **Pass the image`src` property instead of the whole image object to your `<img>` tag:**


```
// Before
<imgsrc={logo} />
// After
<imgsrc={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.
> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src` property. You can safely ignore those for now. They will be fixed by the end of this guide.
### Step 7: Migrate the Environment Variables
Next.js has support for `.env` environment variables similar to Vite. The main difference is the prefix used to expose environment variables on the client-side.
  * Change all environment variables with the `VITE_` prefix to `NEXT_PUBLIC_`.


Vite exposes a few built-in environment variables on the special `import.meta.env` object which aren’t supported by Next.js. You need to update their usage as follows:
  * `import.meta.env.MODE` ⇒ `process.env.NODE_ENV`
  * `import.meta.env.PROD` ⇒ `process.env.NODE_ENV === 'production'`
  * `import.meta.env.DEV` ⇒ `process.env.NODE_ENV !== 'production'`
  * `import.meta.env.SSR` ⇒ `typeof window !== 'undefined'`


Next.js also doesn't provide a built-in `BASE_URL` environment variable. However, you can still configure one, if you need it:
  1. **Add the following to your`.env` file:**


.env
```
# ...
NEXT_PUBLIC_BASE_PATH="/some-base-path"
```

  1. **Set`basePath` to `process.env.NEXT_PUBLIC_BASE_PATH` in your `next.config.mjs` file:**


next.config.mjs
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 output:'export',// Outputs a Single-Page Application (SPA).
 distDir:'./dist',// Changes the build output directory to `./dist/`.
 basePath:process.env.NEXT_PUBLIC_BASE_PATH,// Sets the base path to `/some-base-path`.
}
exportdefault nextConfig
```

  1. **Update`import.meta.env.BASE_URL` usages to `process.env.NEXT_PUBLIC_BASE_PATH`**


### Step 8: Update Scripts in `package.json`
You should now be able to run your application to test if you successfully migrated to Next.js. But before that, you need to update your `scripts` in your `package.json` with Next.js related commands, and add `.next` and `next-env.d.ts` to your `.gitignore`:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start"
 }
}
```

.gitignore
```
# ...
.next
next-env.d.ts
dist
```

Now run `npm run dev`, and open . You should see your application now running on Next.js.
> **Example:** Check out for a working example of a Vite application migrated to Next.js.
### Step 9: Clean Up
You can now clean up your codebase from Vite related artifacts:
  * Delete `main.tsx`
  * Delete `index.html`
  * Delete `vite-env.d.ts`
  * Delete `tsconfig.node.json`
  * Delete `vite.config.ts`
  * Uninstall Vite dependencies


## Next Steps
If everything went according to plan, you now have a functioning Next.js application running as a single-page application. However, you aren't yet taking advantage of most of Next.js' benefits, but you can now start making incremental changes to reap all the benefits. Here's what you might want to do next:
  * Migrate from React Router to the Next.js App Router to get: 
    * Automatic code splitting
    * Streaming Server-Rendering
    * React Server Components
  * Optimize images with the `<Image>` component
  * Optimize fonts with `next/font`
  * Optimize third-party scripts with the `<Script>` component
  * Update your ESLint configuration to support Next.js rules
