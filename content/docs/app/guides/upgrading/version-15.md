---
title: "How to upgrade to version 15"
path: "App / Guides / Upgrading / Version 15"
source_url: https://nextjs.org/docs/app/guides/upgrading/version-15
content_length: 11185
---

# How to upgrade to version 15
## Upgrading from 14 to 15
To update to Next.js version 15, you can use the `upgrade` codemod:
Terminal
```
npx@next/codemod@canaryupgradelatest
```

If you prefer to do it manually, ensure that you're installing the latest Next & React versions:
Terminal
```
npminext@latestreact@latestreact-dom@latesteslint-config-next@latest
```

> **Good to know:**
>   * If you see a peer dependencies warning, you may need to update `react` and `react-dom` to the suggested versions, or you use the `--force` or `--legacy-peer-deps` flag to ignore the warning. This won't be necessary once both Next.js 15 and React 19 are stable.
> 

## React 19
  * The minimum versions of `react` and `react-dom` is now 19.
  * `useFormState` has been replaced by `useActionState`. The `useFormState` hook is still available in React 19, but it is deprecated and will be removed in a future release. `useActionState` is recommended and includes additional properties like reading the `pending` state directly. .
  * `useFormStatus` now includes additional keys like `data`, `method`, and `action`. If you are not using React 19, only the `pending` key is available. .
  * Read more in the .


> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.
## Async Request APIs (Breaking change)
Previously synchronous Dynamic APIs that rely on runtime information are now **asynchronous** :
  * `cookies`
  * `headers`
  * `draftMode`
  * `params` in `layout.js`, `page.js`, `route.js`, `default.js`, `opengraph-image`, `twitter-image`, `icon`, and `apple-icon`.
  * `searchParams` in `page.js`


To ease the burden of migration, a codemod is available to automate the process and the APIs can temporarily be accessed synchronously.
### `cookies`
#### Recommended Async Usage
```
import { cookies } from'next/headers'
// Before
constcookieStore=cookies()
consttoken=cookieStore.get('token')
// After
constcookieStore=awaitcookies()
consttoken=cookieStore.get('token')
```

#### Temporary Synchronous Usage
app/page.tsx
```
import { cookies,type UnsafeUnwrappedCookies } from'next/headers'
// Before
constcookieStore=cookies()
consttoken=cookieStore.get('token')
// After
constcookieStore=cookies() asunknownasUnsafeUnwrappedCookies
// will log a warning in dev
consttoken=cookieStore.get('token')
```

### `headers`
#### Recommended Async Usage
```
import { headers } from'next/headers'
// Before
constheadersList=headers()
constuserAgent=headersList.get('user-agent')
// After
constheadersList=awaitheaders()
constuserAgent=headersList.get('user-agent')
```

#### Temporary Synchronous Usage
app/page.tsx
```
import { headers,type UnsafeUnwrappedHeaders } from'next/headers'
// Before
constheadersList=headers()
constuserAgent=headersList.get('user-agent')
// After
constheadersList=headers() asunknownasUnsafeUnwrappedHeaders
// will log a warning in dev
constuserAgent=headersList.get('user-agent')
```

### `draftMode`
#### Recommended Async Usage
```
import { draftMode } from'next/headers'
// Before
const { isEnabled } =draftMode()
// After
const { isEnabled } =awaitdraftMode()
```

#### Temporary Synchronous Usage
app/page.tsx
```
import { draftMode,type UnsafeUnwrappedDraftMode } from'next/headers'
// Before
const { isEnabled } =draftMode()
// After
// will log a warning in dev
const { isEnabled } =draftMode() asunknownasUnsafeUnwrappedDraftMode
```

### `params` & `searchParams`
#### Asynchronous Layout
app/layout.tsx
```
// Before
typeParams= { slug:string }
exportfunctiongenerateMetadata({ params }: { params:Params }) {
const { slug } = params
}
exportdefaultasyncfunctionLayout({
 children,
 params,
}: {
 children:React.ReactNode
 params:Params
}) {
const { slug } = params
}
// After
typeParams=Promise<{ slug:string }>
exportasyncfunctiongenerateMetadata({ params }: { params:Params }) {
const { slug } =await params
}
exportdefaultasyncfunctionLayout({
 children,
 params,
}: {
 children:React.ReactNode
 params:Params
}) {
const { slug } =await params
}
```

#### Synchronous Layout
app/layout.tsx
```
// Before
typeParams= { slug:string }
exportdefaultfunctionLayout({
 children,
 params,
}: {
 children:React.ReactNode
 params:Params
}) {
const { slug } = params
}
// After
import { use } from'react'
typeParams=Promise<{ slug:string }>
exportdefaultfunctionLayout(props: {
 children:React.ReactNode
 params:Params
}) {
constparams=use(props.params)
constslug=params.slug
}
```

#### Asynchronous Page
app/page.tsx
```
// Before
typeParams= { slug:string }
typeSearchParams= { [key:string]:string|string[] |undefined }
exportfunctiongenerateMetadata({
 params,
 searchParams,
}: {
 params:Params
 searchParams:SearchParams
}) {
const { slug } = params
const { query } = searchParams
}
exportdefaultasyncfunctionPage({
 params,
 searchParams,
}: {
 params:Params
 searchParams:SearchParams
}) {
const { slug } = params
const { query } = searchParams
}
// After
typeParams=Promise<{ slug:string }>
typeSearchParams=Promise<{ [key:string]:string|string[] |undefined }>
exportasyncfunctiongenerateMetadata(props: {
 params:Params
 searchParams:SearchParams
}) {
constparams=awaitprops.params
constsearchParams=awaitprops.searchParams
constslug=params.slug
constquery=searchParams.query
}
exportdefaultasyncfunctionPage(props: {
 params:Params
 searchParams:SearchParams
}) {
constparams=awaitprops.params
constsearchParams=awaitprops.searchParams
constslug=params.slug
constquery=searchParams.query
}
```

#### Synchronous Page
```
'use client'
// Before
typeParams= { slug:string }
typeSearchParams= { [key:string]:string|string[] |undefined }
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params:Params
 searchParams:SearchParams
}) {
const { slug } = params
const { query } = searchParams
}
// After
import { use } from'react'
typeParams=Promise<{ slug:string }>
typeSearchParams=Promise<{ [key:string]:string|string[] |undefined }>
exportdefaultfunctionPage(props: {
 params:Params
 searchParams:SearchParams
}) {
constparams=use(props.params)
constsearchParams=use(props.searchParams)
constslug=params.slug
constquery=searchParams.query
}
```

```
// Before
exportdefaultfunctionPage({ params, searchParams }) {
const { slug } = params
const { query } = searchParams
}
// After
import { use } from"react"
exportdefaultfunctionPage(props) {
constparams=use(props.params)
constsearchParams=use(props.searchParams)
constslug=params.slug
constquery=searchParams.query
}

```

#### Route Handlers
app/api/route.ts
```
// Before
typeParams= { slug:string }
exportasyncfunctionGET(request:Request, segmentData: { params:Params }) {
constparams=segmentData.params
constslug=params.slug
}
// After
typeParams=Promise<{ slug:string }>
exportasyncfunctionGET(request:Request, segmentData: { params:Params }) {
constparams=awaitsegmentData.params
constslug=params.slug
}
```

app/api/route.js
```
// Before
exportasyncfunctionGET(request, segmentData) {
constparams=segmentData.params
constslug=params.slug
}
// After
exportasyncfunctionGET(request, segmentData) {
constparams=awaitsegmentData.params
constslug=params.slug
}
```

## `runtime` configuration (Breaking change)
The `runtime` segment configuration previously supported a value of `experimental-edge` in addition to `edge`. Both configurations refer to the same thing, and to simplify the options, we will now error if `experimental-edge` is used. To fix this, update your `runtime` configuration to `edge`. A codemod is available to automatically do this.
## `fetch` requests
`fetch` requests are no longer cached by default.
To opt specific `fetch` requests into caching, you can pass the `cache: 'force-cache'` option.
app/layout.js
```
exportdefaultasyncfunctionRootLayout() {
consta=awaitfetch(' // Not Cached
constb=awaitfetch(' { cache:'force-cache' }) // Cached
// ...
}
```

To opt all `fetch` requests in a layout or page into caching, you can use the `export const fetchCache = 'default-cache'` segment config option. If individual `fetch` requests specify a `cache` option, that will be used instead.
app/layout.js
```
// Since this is the root layout, all fetch requests in the app
// that don't set their own cache option will be cached.
exportconstfetchCache='default-cache'
exportdefaultasyncfunctionRootLayout() {
consta=awaitfetch(' // Cached
constb=awaitfetch(' { cache:'no-store' }) // Not cached
// ...
}
```

## Route Handlers
`GET` functions in Route Handlers are no longer cached by default. To opt `GET` methods into caching, you can use a route config option such as `export const dynamic = 'force-static'` in your Route Handler file.
app/api/route.js
```
exportconstdynamic='force-static'
exportasyncfunctionGET() {}
```

## Client-side Router Cache
When navigating between pages via `<Link>` or `useRouter`, page segments are no longer reused from the client-side router cache. However, they are still reused during browser backward and forward navigation and for shared layouts.
To opt page segments into caching, you can use the `staleTimes` config option:
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 experimental: {
  staleTimes: {
   dynamic:30,
   static:180,
  },
 },
}
module.exports= nextConfig
```

Layouts and loading states are still cached and reused on navigation.
## `next/font`
The `@next/font` package has been removed in favor of the built-in `next/font`. A codemod is available to safely and automatically rename your imports.
app/layout.js
```
// Before
import { Inter } from'@next/font/google'
// After
import { Inter } from'next/font/google'
```

## bundlePagesRouterDependencies
`experimental.bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
// Before
 experimental: {
  bundlePagesExternals:true,
 },
// After
 bundlePagesRouterDependencies:true,
}
module.exports= nextConfig
```

## serverExternalPackages
`experimental.serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
// Before
 experimental: {
  serverComponentsExternalPackages: ['package-name'],
 },
// After
 serverExternalPackages: ['package-name'],
}
module.exports= nextConfig
```

## Speed Insights
Auto instrumentation for Speed Insights was removed in Next.js 15.
To continue using Speed Insights, follow the guide.
## `NextRequest` Geolocation
The `geo` and `ip` properties on `NextRequest` have been removed as these values are provided by your hosting provider. A codemod is available to automate this migration.
If you are using Vercel, you can alternatively use the `geolocation` and `ipAddress` functions from instead:
middleware.ts
```
import { geolocation } from'@vercel/functions'
importtype { NextRequest } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
const { city } =geolocation(request)
// ...
}
```

middleware.ts
```
import { ipAddress } from'@vercel/functions'
importtype { NextRequest } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
constip=ipAddress(request)
// ...
}
```
