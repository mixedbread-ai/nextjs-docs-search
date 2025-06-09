---
title: UsePathname
path: "App / Api Reference / Functions / Use Pathname"
source_url: https://nextjs.org/docs/app/api-reference/functions/use-pathname
content_length: 2286
---

# usePathname
`usePathname` is a **Client Component** hook that lets you read the current URL's **pathname**.
app/example-client-component.tsx
```
'use client'
import { usePathname } from'next/navigation'
exportdefaultfunctionExampleClientComponent() {
constpathname=usePathname()
return <p>Current pathname: {pathname}</p>
}
```

`usePathname` intentionally requires using a Client Component. It's important to note Client Components are not a de-optimization. They are an integral part of the Server Components architecture.
For example, a Client Component with `usePathname` will be rendered into HTML on the initial page load. When navigating to a new route, this component does not need to be re-fetched. Instead, the component is downloaded once (in the client JavaScript bundle), and re-renders based on the current state.
> **Good to know** :
>   * Reading the current URL from a Server Component is not supported. This design is intentional to support layout state being preserved across page navigations.
>   * Compatibility mode: 
>     * `usePathname` can return `null` when a fallback route is being rendered or when a `pages` directory page has been automatically statically optimized by Next.js and the router is not ready.
>     * When using `usePathname` with rewrites in `next.config` or `Middleware`, `useState` and `useEffect` must also be used in order to avoid hydration mismatch errors.
>     * Next.js will automatically update your types if it detects both an `app` and `pages` directory in your project.
> 

## Parameters
```
constpathname=usePathname()
```

`usePathname` does not take any parameters.
## Returns
`usePathname` returns a string of the current URL's pathname. For example:
URL| Returned value  
---|---  
`/`| `'/'`  
`/dashboard`| `'/dashboard'`  
`/dashboard?v=2`| `'/dashboard'`  
`/blog/hello-world`| `'/blog/hello-world'`  
## Examples
### Do something in response to a route change
app/example-client-component.tsx
```
'use client'
import { usePathname, useSearchParams } from'next/navigation'
functionExampleClientComponent() {
constpathname=usePathname()
constsearchParams=useSearchParams()
useEffect(() => {
// Do something here...
 }, [pathname, searchParams])
}
```

Version| Changes  
---|---  
`v13.0.0`| `usePathname` introduced.
