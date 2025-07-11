---
title: Layout.js
path: "App / Api Reference / File Conventions / Layout"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/layout
content_length: 9604
---

# layout.js
The `layout` file is used to define a layout in your Next.js application.
app/dashboard/layout.tsx
```
exportdefaultfunctionDashboardLayout({
 children,
}: {
 children:React.ReactNode
}) {
return <section>{children}</section>
}
```

A **root layout** is the top-most layout in the root `app` directory. It is used to define the `<html>` and `<body>` tags and other globally shared UI.
app/layout.tsx
```
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

## Reference
### Props
#### `children` (required)
Layout components should accept and use a `children` prop. During rendering, `children` will be populated with the route segments the layout is wrapping. These will primarily be the component of a child Layout (if it exists) or Page, but could also be other special files like Loading or Error when applicable.
#### `params` (optional)
A promise that resolves to an object containing the dynamic route parameters object from the root segment down to that layout.
app/dashboard/[team]/layout.tsx
```
exportdefaultasyncfunctionLayout({
 params,
}: {
 params:Promise<{ team:string }>
}) {
const { team } =await params
}
```

Example Route| URL| `params`  
---|---|---  
`app/dashboard/[team]/layout.js`| `/dashboard/1`| `Promise<{ team: '1' }>`  
`app/shop/[tag]/[item]/layout.js`| `/shop/1/2`| `Promise<{ tag: '1', item: '2' }>`  
`app/blog/[...slug]/layout.js`| `/blog/1/2`| `Promise<{ slug: ['1', '2'] }>`  
  * Since the `params` prop is a promise. You must use `async/await` or React's function to access the values. 
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


### Root Layout
The `app` directory **must** include a root `app/layout.js`.
app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <html>
   <body>{children}</body>
  </html>
 )
}
```

  * The root layout **must** define `<html>` and `<body>` tags. 
    * You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, you should use the Metadata API which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
  * You can use route groups to create multiple root layouts. 
    * Navigating **across multiple root layouts** will cause a **full page load** (as opposed to a client-side navigation). For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js` will cause a full page load. This **only** applies to multiple root layouts.


## Caveats
### Request Object
Layouts are cached in the client during navigation to avoid unnecessary server requests.
Layouts do not rerender. They can be cached and reused to avoid unnecessary computation when navigating between pages. By restricting layouts from accessing the raw request, Next.js can prevent the execution of potentially slow or expensive user code within the layout, which could negatively impact performance.
To access the request object, you can use `headers` and `cookies` APIs in Server Components and Functions.
app/shop/layout.tsx
```
import { cookies } from'next/headers'
exportdefaultasyncfunctionLayout({ children }) {
constcookieStore=awaitcookies()
consttheme=cookieStore.get('theme')
return'...'
}
```

### Query params
Layouts do not rerender on navigation, so they cannot access search params which would otherwise become stale.
To access updated query parameters, you can use the Page `searchParams` prop, or read them inside a Client Component using the `useSearchParams` hook. Since Client Components re-render on navigation, they have access to the latest query parameters.
app/ui/search.tsx
```
'use client'
import { useSearchParams } from'next/navigation'
exportdefaultfunctionSearch() {
constsearchParams=useSearchParams()
constsearch=searchParams.get('search')
return'...'
}
```

app/shop/layout.tsx
```
import Search from'@/app/ui/search'
exportdefaultfunctionLayout({ children }) {
return (
  <>
   <Search />
   {children}
  </>
 )
}
```

### Pathname
Layouts do not re-render on navigation, so they do not access pathname which would otherwise become stale.
To access the current pathname, you can read it inside a Client Component using the `usePathname` hook. Since Client Components re-render during navigation, they have access to the latest pathname.
app/ui/breadcrumbs.tsx
```
'use client'
import { usePathname } from'next/navigation'
// Simplified breadcrumbs logic
exportdefaultfunctionBreadcrumbs() {
constpathname=usePathname()
constsegments=pathname.split('/')
return (
  <nav>
   {segments.map((segment, index) => (
    <spankey={index}>
     {' > '}
     {segment}
    </span>
   ))}
  </nav>
 )
}
```

app/docs/layout.tsx
```
import { Breadcrumbs } from'@/app/ui/Breadcrumbs'
exportdefaultfunctionLayout({ children }) {
return (
  <>
   <Breadcrumbs />
   <main>{children}</main>
  </>
 )
}
```

### Fetching Data
Layouts cannot pass data to their `children`. However, you can fetch the same data in a route more than once, and use React to dedupe the requests without affecting performance.
Alternatively, when using `fetch`in Next.js, requests are automatically deduped.
app/lib/data.ts
```
exportasyncfunctiongetUser(id:string) {
constres=awaitfetch(`{id}`)
returnres.json()
}
```

app/dashboard/layout.tsx
```
import { getUser } from'@/app/lib/data'
import { UserName } from'@/app/ui/user-name'
exportdefaultasyncfunctionLayout({ children }) {
constuser=awaitgetUser('1')
return (
  <>
   <nav>
    {/* ... */}
    <UserNameuser={user.name} />
   </nav>
   {children}
  </>
 )
}
```

app/dashboard/page.tsx
```
import { getUser } from'@/app/lib/data'
import { UserName } from'@/app/ui/user-name'
exportdefaultasyncfunctionPage() {
constuser=awaitgetUser('1')
return (
  <div>
   <h1>Welcome {user.name}</h1>
  </div>
 )
}
```

### Accessing child segments
Layouts do not have access to the route segments below itself. To access all route segments, you can use `useSelectedLayoutSegment` or `useSelectedLayoutSegments` in a Client Component.
app/ui/nav-link.tsx
```
'use client'
import Link from'next/link'
import { useSelectedLayoutSegment } from'next/navigation'
exportdefaultfunctionNavLink({
 slug,
 children,
}: {
 slug:string
 children:React.ReactNode
}) {
constsegment=useSelectedLayoutSegment()
constisActive= slug === segment
return (
  <Link
href={`/blog/${slug}`}
// Change style depending on whether the link is active
style={{ fontWeight: isActive ?'bold':'normal' }}
  >
   {children}
  </Link>
 )
}
```

app/blog/layout.tsx
```
import { NavLink } from'./nav-link'
import getPosts from'./get-posts'
exportdefaultasyncfunctionLayout({
 children,
}: {
 children:React.ReactNode
}) {
constfeaturedPosts=awaitgetPosts()
return (
  <div>
   {featuredPosts.map((post) => (
    <divkey={post.id}>
     <NavLinkslug={post.slug}>{post.title}</NavLink>
    </div>
   ))}
   <div>{children}</div>
  </div>
 )
}
```

## Examples
### Metadata
You can modify the `<head>` HTML elements such as `title` and `meta` using the `metadata` object or `generateMetadata` function.
app/layout.tsx
```
importtype { Metadata } from'next'
exportconstmetadata:Metadata= {
 title:'Next.js',
}
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return'...'
}
```

> **Good to know** : You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, use the Metadata APIs which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
### Active Nav Links
You can use the `usePathname` hook to determine if a nav link is active.
Since `usePathname` is a client hook, you need to extract the nav links into a Client Component, which can be imported into your layout:
app/ui/nav-links.tsx
```
'use client'
import { usePathname } from'next/navigation'
import Link from'next/link'
exportfunctionNavLinks() {
constpathname=usePathname()
return (
  <nav>
   <LinkclassName={`link ${pathname ==='/'?'active':''}`} href="/">
    Home
   </Link>
   <Link
className={`link ${pathname ==='/about'?'active':''}`}
href="/about"
   >
    About
   </Link>
  </nav>
 )
}
```

app/layout.tsx
```
import { NavLinks } from'@/app/ui/nav-links'
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return (
  <htmllang="en">
   <body>
    <NavLinks />
    <main>{children}</main>
   </body>
  </html>
 )
}
```

### Displaying content based on `params`
Using dynamic route segments, you can display or fetch specific content based on the `params` prop.
app/dashboard/layout.tsx
```
exportdefaultasyncfunctionDashboardLayout({
 children,
 params,
}: {
 children:React.ReactNode
 params:Promise<{ team:string }>
}) {
const { team } =await params
return (
  <section>
   <header>
    <h1>Welcome to {team}'s Dashboard</h1>
   </header>
   <main>{children}</main>
  </section>
 )
}
```

### Reading `params` in Client Components
To use `params` in a Client Component (which cannot be `async`), you can use React's function to read the promise:
app/page.tsx
```
'use client'
import { use } from'react'
exportdefaultfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =use(params)
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0-RC`| `params` is now a promise. A codemod is available.  
`v13.0.0`| `layout` introduced.
