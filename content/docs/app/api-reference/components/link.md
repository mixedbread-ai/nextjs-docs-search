---
title: Link
path: "App / Api Reference / Components / Link"
source_url: https://nextjs.org/docs/app/api-reference/components/link
content_length: 15252
---

# Link
`<Link>` is a React component that extends the HTML `<a>` element to provide prefetching and client-side navigation between routes. It is the primary way to navigate between routes in Next.js.
Basic usage:
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return <Linkhref="/dashboard">Dashboard</Link>
}
```

## Reference
The following props can be passed to the `<Link>` component:
Prop| Example| Type| Required  
---|---|---|---  
`href`| `href="/dashboard"`| String or Object| Yes  
`replace`| `replace={false}`| Boolean| -  
`scroll`| `scroll={false}`| Boolean| -  
`prefetch`| `prefetch={false}`| Boolean or null| -  
`onNavigate`| `onNavigate={(e) => {}}`| Function| -  
> **Good to know** : `<a>` tag attributes such as `className` or `target="_blank"` can be added to `<Link>` as props and will be passed to the underlying `<a>` element.
### `href` (required)
The path or URL to navigate to.
app/page.tsx
```
import Link from'next/link'
// Navigate to /about?name=test
exportdefaultfunctionPage() {
return (
  <Link
href={{
    pathname:'/about',
    query: { name:'test' },
   }}
  >
   About
  </Link>
 )
}
```

### `replace`
**Defaults to`false`.** When `true`, `next/link` will replace the current history state instead of adding a new URL into the stack.
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Linkhref="/dashboard"replace>
   Dashboard
  </Link>
 )
}
```

### `scroll`
**Defaults to`true`.** The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position** , similar to how browsers handle back and forwards navigation. When you navigate to a new Page, scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.
When `scroll = {false}`, Next.js will not attempt to scroll to the first Page element.
> **Good to know** : Next.js checks if `scroll: false` before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top-level element. All non-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non-visible elements such as those calculated with `getBoundingClientRect`. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Linkhref="/dashboard"scroll={false}>
   Dashboard
  </Link>
 )
}
```

### `prefetch`
Prefetching happens when a `<Link />` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and its data in the background to improve the performance of client-side navigations. If the prefetched data has expired by the time the user hovers over a `<Link />`, Next.js will attempt to prefetch it again. **Prefetching is only enabled in production**.
The following values can be passed to the `prefetch` prop:
  * **`null`(default)** : Prefetch behavior depends on whether the route is static or dynamic. For static routes, the full route will be prefetched (including all its data). For dynamic routes, the partial route down to the nearest segment with a `loading.js` boundary will be prefetched.
  * `true`: The full route will be prefetched for both static and dynamic routes.
  * `false`: Prefetching will never happen both on entering the viewport and on hover.


app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Linkhref="/dashboard"prefetch={false}>
   Dashboard
  </Link>
 )
}
```

### `onNavigate`
An event handler called during client-side navigation. The handler receives an event object that includes a `preventDefault()` method, allowing you to cancel the navigation if needed.
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Link
href="/dashboard"
onNavigate={(e) => {
// Only executes during SPA navigation
console.log('Navigating...')
// Optionally prevent navigation
// e.preventDefault()
   }}
  >
   Dashboard
  </Link>
 )
}
```

> **Good to know** : While `onClick` and `onNavigate` may seem similar, they serve different purposes. `onClick` executes for all click events, while `onNavigate` only runs during client-side navigation. Some key differences:
>   * When using modifier keys (`Ctrl`/`Cmd` + Click), `onClick` executes but `onNavigate` doesn't since Next.js prevents default navigation for new tabs.
>   * External URLs won't trigger `onNavigate` since it's only for client-side and same-origin navigations.
>   * Links with the `download` attribute will work with `onClick` but not `onNavigate` since the browser will treat the linked URL as a download.
> 

## Examples
The following examples demonstrate how to use the `<Link>` component in different scenarios.
### Linking to dynamic segments
When linking to dynamic segments, you can use to generate a list of links. For example, to generate a list of blog posts:
app/blog/post-list.tsx
```
import Link from'next/link'
interfacePost {
 id:number
 title:string
 slug:string
}
exportdefaultfunctionPostList({ posts }: { posts:Post[] }) {
return (
  <ul>
   {posts.map((post) => (
    <likey={post.id}>
     <Linkhref={`/blog/${post.slug}`}>{post.title}</Link>
    </li>
   ))}
  </ul>
 )
}
```

### Checking active links
You can use `usePathname()` to determine if a link is active. For example, to add a class to the active link, you can check if the current `pathname` matches the `href` of the link:
app/ui/nav-links.tsx
```
'use client'
import { usePathname } from'next/navigation'
import Link from'next/link'
exportfunctionLinks() {
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

### Scrolling to an `id`
If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `<Link>` renders to an `<a>` element.
```
<Linkhref="/dashboard#settings">Settings</Link>
// Output
<ahref="/dashboard#settings">Settings</a>
```

> **Good to know** :
>   * Next.js will scroll to the Page if it is not visible in the viewport upon navigation.
> 

### Linking to dynamic route segments
For dynamic route segments, it can be handy to use template literals to create the link's path.
For example, you can generate a list of links to the dynamic route `app/blog/[slug]/page.js`:
app/blog/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage({ posts }) {
return (
  <ul>
   {posts.map((post) => (
    <likey={post.id}>
     <Linkhref={`/blog/${post.slug}`}>{post.title}</Link>
    </li>
   ))}
  </ul>
 )
}
```

### If the child is a custom component that wraps an `<a>` tag
If the child of `Link` is a custom component that wraps an `<a>` tag, you must add `passHref` to `Link`. This is necessary if you’re using libraries like . Without this, the `<a>` tag will not have the `href` attribute, which hurts your site's accessibility and might affect SEO. If you're using ESLint, there is a built-in rule `next/link-passhref` to ensure correct usage of `passHref`.
components/nav-link.tsx
```
import Link from'next/link'
import styled from'styled-components'
// This creates a custom component that wraps an <a> tag
constRedLink=styled.a`
 color: red;
`
functionNavLink({ href, name }) {
return (
  <Linkhref={href} passHreflegacyBehavior>
   <RedLink>{name}</RedLink>
  </Link>
 )
}
exportdefault NavLink
```

  * If you’re using ’s JSX pragma feature (`@jsx jsx`), you must use `passHref` even if you use an `<a>` tag directly.
  * The component should support `onClick` property to trigger navigation correctly.


### Nesting a functional component
If the child of `Link` is a functional component, in addition to using `passHref` and `legacyBehavior`, you must wrap the component in :
app/page.tsx
```
import Link from'next/link'
import React from'react'
// Define the props type for MyButton
interfaceMyButtonProps {
 onClick?:React.MouseEventHandler<HTMLAnchorElement>
 href?:string
}
// Use React.ForwardRefRenderFunction to properly type the forwarded ref
constMyButton:React.ForwardRefRenderFunction<
HTMLAnchorElement,
MyButtonProps
> = ({ onClick, href }, ref) => {
return (
  <ahref={href} onClick={onClick} ref={ref}>
   Click Me
  </a>
 )
}
// Use React.forwardRef to wrap the component
constForwardedMyButton=React.forwardRef(MyButton)
exportdefaultfunctionPage() {
return (
  <Linkhref="/about"passHreflegacyBehavior>
   <ForwardedMyButton />
  </Link>
 )
}
```

### Replace the URL instead of push
The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:
app/page.js
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Linkhref="/about"replace>
   About us
  </Link>
 )
}
```

### Disable scrolling to the top of the page
The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position** , similar to how browsers handle back and forwards navigation. When you navigate to a new Page, scroll position will stay the same as long as the Page is visible in the viewport.
However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element. If you'd like to disable this behavior, you can pass `scroll={false}` to the `<Link>` component, or `scroll: false` to `router.push()` or `router.replace()`.
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <Linkhref="/#hashid"scroll={false}>
   Disables scrolling to the top
  </Link>
 )
}
```

Using `router.push()` or `router.replace()`:
```
// useRouter
import { useRouter } from'next/navigation'
constrouter=useRouter()
router.push('/dashboard', { scroll:false })
```

### Prefetching links in Middleware
It's common to use Middleware for authentication or other purposes that involve rewriting the user to a different page. In order for the `<Link />` component to properly prefetch links with rewrites via Middleware, you need to tell Next.js both the URL to display and the URL to prefetch. This is required to avoid un-necessary fetches to middleware to know the correct route to prefetch.
For example, if you want to serve a `/dashboard` route that has authenticated and visitor views, you can add the following in your Middleware to redirect the user to the correct page:
middleware.ts
```
import { NextResponse } from'next/server'
exportfunctionmiddleware(request:Request) {
constnextUrl=request.nextUrl
if (nextUrl.pathname ==='/dashboard') {
if (request.cookies.authToken) {
returnNextResponse.rewrite(newURL('/auth/dashboard',request.url))
  } else {
returnNextResponse.rewrite(newURL('/public/dashboard',request.url))
  }
 }
}
```

In this case, you would want to use the following code in your `<Link />` component:
app/page.tsx
```
'use client'
import Link from'next/link'
import useIsAuthed from'./hooks/useIsAuthed'// Your auth hook
exportdefaultfunctionPage() {
constisAuthed=useIsAuthed()
constpath= isAuthed ?'/auth/dashboard':'/public/dashboard'
return (
  <Linkas="/dashboard"href={path}>
   Dashboard
  </Link>
 )
}
```

### Blocking navigation
You can use the `onNavigate` prop to block navigation when certain conditions are met, such as when a form has unsaved changes. When you need to block navigation across multiple components in your app (like preventing navigation from any link while a form is being edited), React Context provides a clean way to share this blocking state. First, create a context to track the navigation blocking state:
app/contexts/navigation-blocker.tsx
```
'use client'
import { createContext, useState, useContext } from'react'
interfaceNavigationBlockerContextType {
 isBlocked:boolean
setIsBlocked: (isBlocked:boolean) =>void
}
exportconstNavigationBlockerContext=
createContext<NavigationBlockerContextType>({
  isBlocked:false,
setIsBlocked: () => {},
 })
exportfunctionNavigationBlockerProvider({
 children,
}: {
 children:React.ReactNode
}) {
const [isBlocked,setIsBlocked] =useState(false)
return (
  <NavigationBlockerContext.Providervalue={{ isBlocked, setIsBlocked }}>
   {children}
  </NavigationBlockerContext.Provider>
 )
}
exportfunctionuseNavigationBlocker() {
returnuseContext(NavigationBlockerContext)
}
```

Create a form component that uses the context:
app/components/form.tsx
```
'use client'
import { useNavigationBlocker } from'../contexts/navigation-blocker'
exportdefaultfunctionForm() {
const { setIsBlocked } =useNavigationBlocker()
return (
  <form
onSubmit={(e) => {
e.preventDefault()
setIsBlocked(false)
   }}
onChange={() =>setIsBlocked(true)}
  >
   <inputtype="text"name="name" />
   <buttontype="submit">Save</button>
  </form>
 )
}
```

Create a custom Link component that blocks navigation:
app/components/custom-link.tsx
```
'use client'
import Link from'next/link'
import { useNavigationBlocker } from'../contexts/navigation-blocker'
interfaceCustomLinkPropsextendsReact.ComponentProps<typeof Link> {
 children:React.ReactNode
}
exportfunctionCustomLink({ children,...props }:CustomLinkProps) {
const { isBlocked } =useNavigationBlocker()
return (
  <Link
onNavigate={(e) => {
if (
     isBlocked &&
!window.confirm('You have unsaved changes. Leave anyway?')
    ) {
e.preventDefault()
    }
   }}
   {...props}
  >
   {children}
  </Link>
 )
}
```

Create a navigation component:
app/components/nav.tsx
```
'use client'
import { CustomLink as Link } from'./custom-link'
exportdefaultfunctionNav() {
return (
  <nav>
   <Linkhref="/">Home</Link>
   <Linkhref="/about">About</Link>
  </nav>
 )
}
```

Finally, wrap your app with the `NavigationBlockerProvider` in the root layout and use the components in your page:
app/layout.tsx
```
import { NavigationBlockerProvider } from'./contexts/navigation-blocker'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <body>
    <NavigationBlockerProvider>{children}</NavigationBlockerProvider>
   </body>
  </html>
 )
}
```

Then, use the `Nav` and `Form` components in your page:
app/page.tsx
```
import Nav from'./components/nav'
import Form from'./components/form'
exportdefaultfunctionPage() {
return (
  <div>
   <Nav />
   <main>
    <h1>Welcome to the Dashboard</h1>
    <Form />
   </main>
  </div>
 )
}
```

When a user tries to navigate away using `CustomLink` while the form has unsaved changes, they'll be prompted to confirm before leaving.
## Version history
Version| Changes  
---|---  
`v15.3.0`| Add `onNavigate` API  
`v13.0.0`| No longer requires a child `<a>` tag. A codemod is provided to automatically update your codebase.  
`v10.0.0`| `href` props pointing to a dynamic route are automatically resolved and no longer require an `as` prop.  
`v8.0.0`| Improved prefetching performance.  
`v1.0.0`| `next/link` introduced.
