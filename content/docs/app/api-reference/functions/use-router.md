---
title: UseRouter
path: "App / Api Reference / Functions / Use Router"
source_url: https://nextjs.org/docs/app/api-reference/functions/use-router
content_length: 4071
---

# useRouter
The `useRouter` hook allows you to programmatically change routes inside Client Components.
> **Recommendation:** Use the `<Link>` component for navigation unless you have a specific requirement for using `useRouter`.
app/example-client-component.tsx
```
'use client'
import { useRouter } from'next/navigation'
exportdefaultfunctionPage() {
constrouter=useRouter()
return (
  <buttontype="button"onClick={() =>router.push('/dashboard')}>
   Dashboard
  </button>
 )
}
```

## `useRouter()`
  * `router.push(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route. Adds a new entry into the stack.
  * `router.replace(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route without adding a new entry into the .
  * `router.refresh()`: Refresh the current route. Making a new request to the server, re-fetching data requests, and re-rendering Server Components. The client will merge the updated React Server Component payload without losing unaffected client-side React (e.g. `useState`) or browser state (e.g. scroll position).
  * `router.prefetch(href: string)`: Prefetch the provided route for faster client-side transitions.
  * `router.back()`: Navigate back to the previous route in the browser’s history stack.
  * `router.forward()`: Navigate forwards to the next page in the browser’s history stack.


> **Good to know** :
>   * You must not send untrusted or unsanitized URLs to `router.push` or `router.replace`, as this can open your site to cross-site scripting (XSS) vulnerabilities. For example, `javascript:` URLs sent to `router.push` or `router.replace` will be executed in the context of your page.
>   * The `<Link>` component automatically prefetch routes as they become visible in the viewport.
>   * `refresh()` could re-produce the same result if fetch requests are cached. Other Dynamic APIs like `cookies` and `headers` could also change the response.
> 

### Migrating from `next/router`
  * The `useRouter` hook should be imported from `next/navigation` and not `next/router` when using the App Router
  * The `pathname` string has been removed and is replaced by `usePathname()`
  * The `query` object has been removed and is replaced by `useSearchParams()`
  * `router.events` has been replaced. See below.


View the full migration guide.
## Examples
### Router events
You can listen for page changes by composing other Client Component hooks like `usePathname` and `useSearchParams`.
app/components/navigation-events.js
```
'use client'
import { useEffect } from'react'
import { usePathname, useSearchParams } from'next/navigation'
exportfunctionNavigationEvents() {
constpathname=usePathname()
constsearchParams=useSearchParams()
useEffect(() => {
consturl=`${pathname}?${searchParams}`
console.log(url)
// You can now use the current URL
// ...
 }, [pathname, searchParams])
return'...'
}
```

Which can be imported into a layout.
app/layout.js
```
import { Suspense } from'react'
import { NavigationEvents } from'./components/navigation-events'
exportdefaultfunctionLayout({ children }) {
return (
  <htmllang="en">
   <body>
    {children}
    <Suspensefallback={null}>
     <NavigationEvents />
    </Suspense>
   </body>
  </html>
 )
}
```

> **Good to know** : `<NavigationEvents>` is wrapped in a `Suspense` boundary because`useSearchParams()` causes client-side rendering up to the closest `Suspense` boundary during static rendering. Learn more.
### Disabling scroll to top
By default, Next.js will scroll to the top of the page when navigating to a new route. You can disable this behavior by passing `scroll: false` to `router.push()` or `router.replace()`.
app/example-client-component.tsx
```
'use client'
import { useRouter } from'next/navigation'
exportdefaultfunctionPage() {
constrouter=useRouter()
return (
  <button
type="button"
onClick={() =>router.push('/dashboard', { scroll:false })}
  >
   Dashboard
  </button>
 )
}
```

## Version History
Version| Changes  
---|---  
`v13.0.0`| `useRouter` from `next/navigation` introduced.
