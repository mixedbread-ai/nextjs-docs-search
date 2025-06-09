---
title: Codemods
path: "App / Guides / Upgrading / Codemods"
source_url: https://nextjs.org/docs/app/guides/upgrading/codemods
content_length: 11253
---

# Codemods
Codemods are transformations that run on your codebase programmatically. This allows a large number of changes to be programmatically applied without having to manually go through every file.
Next.js provides Codemod transformations to help upgrade your Next.js codebase when an API is updated or deprecated.
## Usage
In your terminal, navigate (`cd`) into your project's folder, then run:
Terminal
```
npx@next/codemod<transform><path>
```

Replacing `<transform>` and `<path>` with appropriate values.
  * `transform` - name of transform
  * `path` - files or directory to transform
  * `--dry` Do a dry-run, no code will be edited
  * `--print` Prints the changed output for comparison


## Codemods
### 15.0
#### Transform App Router Route Segment Config `runtime` value from `experimental-edge` to `edge`
##### `app-dir-runtime-config-experimental-edge`
> **Note** : This codemod is App Router specific.
Terminal
```
npx@next/codemod@latestapp-dir-runtime-config-experimental-edge.
```

This codemod transforms Route Segment Config `runtime` value `experimental-edge` to `edge`.
For example:
```
exportconstruntime='experimental-edge'
```

Transforms into:
```
exportconstruntime='edge'
```

#### Migrate to async Dynamic APIs
APIs that opted into dynamic rendering that previously supported synchronous access are now asynchronous. You can read more about this breaking change in the upgrade guide.
##### `next-async-request-api`
Terminal
```
npx@next/codemod@latestnext-async-request-api.
```

This codemod will transform dynamic APIs (`cookies()`, `headers()` and `draftMode()` from `next/headers`) that are now asynchronous to be properly awaited or wrapped with `React.use()` if applicable. When an automatic migration isn't possible, the codemod will either add a typecast (if a TypeScript file) or a comment to inform the user that it needs to be manually reviewed & updated.
For example:
```
import { cookies, headers } from'next/headers'
consttoken=cookies().get('token')
functionuseToken() {
consttoken=cookies().get('token')
return token
}
exportdefaultfunctionPage() {
constname=cookies().get('name')
}
functiongetHeader() {
returnheaders().get('x-foo')
}
```

Transforms into:
```
import { use } from'react'
import {
 cookies,
 headers,
type UnsafeUnwrappedCookies,
type UnsafeUnwrappedHeaders,
} from'next/headers'
consttoken= (cookies() asunknownasUnsafeUnwrappedCookies).get('token')
functionuseToken() {
consttoken=use(cookies()).get('token')
return token
}
exportdefaultasyncfunctionPage() {
constname= (awaitcookies()).get('name')
}
functiongetHeader() {
return (headers() asunknownasUnsafeUnwrappedHeaders).get('x-foo')
}
```

When we detect property access on the `params` or `searchParams` props in the page / route entries (`page.js`, `layout.js`, `route.js`, or `default.js`) or the `generateMetadata` / `generateViewport` APIs, it will attempt to transform the callsite from a sync to an async function, and await the property access. If it can't be made async (such as with a Client Component), it will use `React.use` to unwrap the promise .
For example:
```
// page.tsx
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params: { slug:string }
 searchParams: { [key:string]:string|string[] |undefined }
}) {
const { value } = searchParams
if (value ==='foo') {
// ...
 }
}
exportfunctiongenerateMetadata({ params }: { params: { slug:string } }) {
const { slug } = params
return {
  title:`My Page - ${slug}`,
 }
}
```

Transforms into:
```
// page.tsx
exportdefaultasyncfunctionPage(props: {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
constsearchParams=awaitprops.searchParams
const { value } = searchParams
if (value ==='foo') {
// ...
 }
}
exportasyncfunctiongenerateMetadata(props: {
 params:Promise<{ slug:string }>
}) {
constparams=awaitprops.params
const { slug } = params
return {
  title:`My Page - ${slug}`,
 }
}
```

> **Good to know:** When this codemod identifies a spot that might require manual intervention, but we aren't able to determine the exact fix, it will add a comment or typecast to the code to inform the user that it needs to be manually updated. These comments are prefixed with **@next/codemod** , and typecasts are prefixed with `UnsafeUnwrapped`. Your build will error until these comments are explicitly removed. Read more.
#### Replace `geo` and `ip` properties of `NextRequest` with `@vercel/functions`
##### `next-request-geo-ip`
Terminal
```
npx@next/codemod@latestnext-request-geo-ip.
```

This codemod installs `@vercel/functions` and transforms `geo` and `ip` properties of `NextRequest` with corresponding `@vercel/functions` features.
For example:
```
importtype { NextRequest } from'next/server'
exportfunctionGET(req:NextRequest) {
const { geo,ip } = req
}
```

Transforms into:
```
importtype { NextRequest } from'next/server'
import { geolocation, ipAddress } from'@vercel/functions'
exportfunctionGET(req:NextRequest) {
constgeo=geolocation(req)
constip=ipAddress(req)
}
```

### 14.0
#### Migrate `ImageResponse` imports
##### `next-og-import`
Terminal
```
npx@next/codemod@latestnext-og-import.
```

This codemod moves transforms imports from `next/server` to `next/og` for usage of Dynamic OG Image Generation.
For example:
```
import { ImageResponse } from'next/server'
```

Transforms into:
```
import { ImageResponse } from'next/og'
```

#### Use `viewport` export
##### `metadata-to-viewport-export`
Terminal
```
npx@next/codemod@latestmetadata-to-viewport-export.
```

This codemod migrates certain viewport metadata to `viewport` export.
For example:
```
exportconstmetadata= {
 title:'My App',
 themeColor:'dark',
 viewport: {
  width:1,
 },
}
```

Transforms into:
```
exportconstmetadata= {
 title:'My App',
}
exportconstviewport= {
 width:1,
 themeColor:'dark',
}
```

### 13.2
#### Use Built-in Font
##### `built-in-next-font`
Terminal
```
npx@next/codemod@latestbuilt-in-next-font.
```

This codemod uninstalls the `@next/font` package and transforms `@next/font` imports into the built-in `next/font`.
For example:
```
import { Inter } from'@next/font/google'
```

Transforms into:
```
import { Inter } from'next/font/google'
```

### 13.0
#### Rename Next Image Imports
##### `next-image-to-legacy-image`
Terminal
```
npx@next/codemod@latestnext-image-to-legacy-image.
```

Safely renames `next/image` imports in existing Next.js 10, 11, or 12 applications to `next/legacy/image` in Next.js 13. Also renames `next/future/image` to `next/image`.
For example:
pages/index.js
```
import Image1 from'next/image'
import Image2 from'next/future/image'
exportdefaultfunctionHome() {
return (
  <div>
   <Image1src="/test.jpg"width="200"height="300" />
   <Image2src="/test.png"width="500"height="400" />
  </div>
 )
}
```

Transforms into:
pages/index.js
```
// 'next/image' becomes 'next/legacy/image'
import Image1 from'next/legacy/image'
// 'next/future/image' becomes 'next/image'
import Image2 from'next/image'
exportdefaultfunctionHome() {
return (
  <div>
   <Image1src="/test.jpg"width="200"height="300" />
   <Image2src="/test.png"width="500"height="400" />
  </div>
 )
}
```

#### Migrate to the New Image Component
##### `next-image-experimental`
Terminal
```
npx@next/codemod@latestnext-image-experimental.
```

Dangerously migrates from `next/legacy/image` to the new `next/image` by adding inline styles and removing unused props.
  * Removes `layout` prop and adds `style`.
  * Removes `objectFit` prop and adds `style`.
  * Removes `objectPosition` prop and adds `style`.
  * Removes `lazyBoundary` prop.
  * Removes `lazyRoot` prop.


#### Remove `<a>` Tags From Link Components
##### `new-link`
Terminal
```
npx@next/codemod@latestnew-link.
```

Remove `<a>` tags inside Link Components, or add a `legacyBehavior` prop to Links that cannot be auto-fixed.
For example:
```
<Linkhref="/about">
 <a>About</a>
</Link>
// transforms into
<Linkhref="/about">
 About
</Link>
<Linkhref="/about">
 <aonClick={() =>console.log('clicked')}>About</a>
</Link>
// transforms into
<Linkhref="/about"onClick={() =>console.log('clicked')}>
 About
</Link>
```

In cases where auto-fixing can't be applied, the `legacyBehavior` prop is added. This allows your app to keep functioning using the old behavior for that particular link.
```
constComponent= () => <a>About</a>
<Linkhref="/about">
 <Component />
</Link>
// becomes
<Linkhref="/about"legacyBehavior>
 <Component />
</Link>
```

### 11
#### Migrate from CRA
##### `cra-to-next`
Terminal
```
npx@next/codemodcra-to-next
```

Migrates a Create React App project to Next.js; creating a Pages Router and necessary config to match behavior. Client-side only rendering is leveraged initially to prevent breaking compatibility due to `window` usage during SSR and can be enabled seamlessly to allow the gradual adoption of Next.js specific features.
Please share any feedback related to this transform .
### 10
#### Add React imports
##### `add-missing-react-import`
Terminal
```
npx@next/codemodadd-missing-react-import
```

Transforms files that do not import `React` to include the import in order for the new to work.
For example:
my-component.js
```
exportdefaultclassHomeextendsReact.Component {
render() {
return <div>Hello World</div>
 }
}
```

Transforms into:
my-component.js
```
import React from'react'
exportdefaultclassHomeextendsReact.Component {
render() {
return <div>Hello World</div>
 }
}
```

### 9
#### Transform Anonymous Components into Named Components
##### `name-default-component`
Terminal
```
npx@next/codemodname-default-component
```

**Versions 9 and above.**
Transforms anonymous components into named components to make sure they work with Fast Refresh.
For example:
my-component.js
```
exportdefaultfunction () {
return <div>Hello World</div>
}
```

Transforms into:
my-component.js
```
exportdefaultfunctionMyComponent() {
return <div>Hello World</div>
}
```

The component will have a camel-cased name based on the name of the file, and it also works with arrow functions.
### 8
#### Transform AMP HOC into page config
##### `withamp-to-config`
Terminal
```
npx@next/codemodwithamp-to-config
```

Transforms the `withAmp` HOC into Next.js 9 page configuration.
For example:
```
// Before
import { withAmp } from'next/amp'
functionHome() {
return <h1>My AMP Page</h1>
}
exportdefaultwithAmp(Home)
```

```
// After
exportdefaultfunctionHome() {
return <h1>My AMP Page</h1>
}
exportconstconfig= {
 amp:true,
}
```

### 6
#### Use `withRouter`
##### `url-to-withrouter`
Terminal
```
npx@next/codemodurl-to-withrouter
```

Transforms the deprecated automatically injected `url` property on top level pages to using `withRouter` and the `router` property it injects. Read more here: 
For example:
From
```
import React from'react'
exportdefaultclassextendsReact.Component {
render() {
const { pathname } =this.props.url
return <div>Current pathname: {pathname}</div>
 }
}
```

To
```
import React from'react'
import { withRouter } from'next/router'
exportdefaultwithRouter(
classextendsReact.Component {
render() {
const { pathname } =this.props.router
return <div>Current pathname: {pathname}</div>
  }
 }
)
```

This is one case. All the cases that are transformed (and tested) can be found in the .
