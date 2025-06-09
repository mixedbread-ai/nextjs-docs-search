---
title: "Use cache"
path: "App / Api Reference / Directives / Use Cache"
source_url: https://nextjs.org/docs/app/api-reference/directives/use-cache
content_length: 7241
---

# use cache
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on .
The `use cache` directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all exports in the file should be cached, or inline at the top of function or component to cache the return value.
## Usage
`use cache` is currently an experimental feature. To enable it, add the `useCache` option to your `next.config.ts` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  useCache:true,
 },
}
exportdefault nextConfig
```

> **Good to know:** `use cache` can also be enabled with the `dynamicIO` option.
Then, add `use cache` at the file, component, or function level:
```
// File level
'use cache'
exportdefaultasyncfunctionPage() {
// ...
}
// Component level
exportasyncfunctionMyComponent() {
'use cache'
return <></>
}
// Function level
exportasyncfunctiongetData() {
'use cache'
constdata=awaitfetch('/api/data')
return data
}
```

## How `use cache` works
### Cache keys
A cache entry's key is generated using a serialized version of its inputs, which includes:
  * Build ID (generated for each build)
  * Function ID (a secure identifier unique to the function)
  * The function arguments (or props).


The arguments passed to the cached function, as well as any values it reads from the parent scope automatically become a part of the key. This means, the same cache entry will be reused as long as its inputs are the same.
## Non-serializable arguments
Any non-serializable arguments, props, or closed-over values will turn into references inside the cached function, and can be only passed through and not inspected nor modified. These non-serializable values will be filled in at the request time and won't become a part of the cache key.
For example, a cached function can take in JSX as a `children` prop and return `<div>{children}</div>`, but it won't be able to introspect the actual `children` object. This allows you to nest uncached content inside a cached component.
app/ui/cached-component.tsx
```
functionCachedComponent({ children }: { children:ReactNode }) {
'use cache'
return <div>{children}</div>
}
```

## Return values
The return value of the cacheable function must be serializable. This ensures that the cached data can be stored and retrieved correctly.
## `use cache` at build time
When used at the top of a layout or page, the route segment will be prerendered, allowing it to later be revalidated.
This means `use cache` cannot be used with request-time APIs like `cookies` or `headers`.
## `use cache` at runtime
On the **server** , the cache entries of individual components or functions will be cached in-memory.
Then, on the **client** , any content returned from the server cache will be stored in the browser's memory for the duration of the session or until revalidated.
## During revalidation
By default, `use cache` has server-side revalidation period of **15 minutes**. While this period may be useful for content that doesn't require frequent updates, you can use the `cacheLife` and `cacheTag` APIs to configure when the individual cache entries should be revalidated.
  * `cacheLife`: Configure the cache entry lifetime.
  * `cacheTag`: Create tags for on-demand revalidation.


Both of these APIs integrate across the client and server caching layers, meaning you can configure your caching semantics in one place and have them apply everywhere.
See the `cacheLife` and `cacheTag` API docs for more information.
## Examples
### Caching an entire route with `use cache`
To prerender an entire route, add `use cache` to the top of **both** the `layout` and `page` files. Each of these segments are treated as separate entry points in your application, and will be cached independently.
app/layout.tsx
```
'use cache'
exportdefaultfunctionLayout({ children }: { children:ReactNode }) {
return <div>{children}</div>
}
```

Any components imported and nested in `page` file will inherit the cache behavior of `page`.
app/page.tsx
```
'use cache'
asyncfunctionUsers() {
constusers=awaitfetch('/api/users')
// loop through users
}
exportdefaultfunctionPage() {
return (
  <main>
   <Users />
  </main>
 )
}
```

> **Good to know** :
>   * If `use cache` is added only to the `layout` or the `page`, only that route segment and any components imported into it will be cached.
>   * If any of the nested children in the route use Dynamic APIs, then the route will opt out of prerendering.
> 

### Caching a component's output with `use cache`
You can use `use cache` at the component level to cache any fetches or computations performed within that component. The cache entry will be reused as long as the serialized props produce the same value in each instance.
app/components/bookings.tsx
```
exportasyncfunctionBookings({ type ='haircut' }:BookingsProps) {
'use cache'
asyncfunctiongetBookingsData() {
constdata=awaitfetch(`/api/bookings?type=${encodeURIComponent(type)}`)
return data
 }
return//...
}
interfaceBookingsProps {
 type:string
}
```

### Caching function output with `use cache`
Since you can add `use cache` to any asynchronous function, you aren't limited to caching components or routes only. You might want to cache a network request, a database query, or a slow computation.
app/actions.ts
```
exportasyncfunctiongetData() {
'use cache'
constdata=awaitfetch('/api/data')
return data
}
```

### Interleaving
If you need to pass non-serializable arguments to a cacheable function, you can pass them as `children`. This means the `children` reference can change without affecting the cache entry.
app/page.tsx
```
exportdefaultasyncfunctionPage() {
constuncachedData=awaitgetData()
return (
  <CacheComponent>
   <DynamicComponentdata={uncachedData} />
  </CacheComponent>
 )
}
asyncfunctionCacheComponent({ children }: { children:ReactNode }) {
'use cache'
constcachedData=awaitfetch('/api/cached-data')
return (
  <div>
   <PrerenderedComponentdata={cachedData} />
   {children}
  </div>
 )
}
```

You can also pass Server Actions through cached components to Client Components without invoking them inside the cacheable function.
app/page.tsx
```
import ClientComponent from'./ClientComponent'
exportdefaultasyncfunctionPage() {
constperformUpdate=async () => {
'use server'
// Perform some server-side update
awaitdb.update(...)
 }
return <CacheComponentperformUpdate={performUpdate} />
}
asyncfunctionCachedComponent({
 performUpdate,
}: {
performUpdate: () =>Promise<void>
}) {
'use cache'
// Do not call performUpdate here
return <ClientComponentaction={performUpdate} />
}
```

app/ClientComponent.tsx
```
'use client'
exportdefaultfunctionClientComponent({
 action,
}: {
action: () =>Promise<void>
}) {
return <buttononClick={action}>Update</button>
}
```

## Platform Support
Deployment Option| Supported  
---|---  
Node.js server| Yes  
Docker container| Yes  
Static export| No  
Adapters| Platform-specific  
Learn how to configure caching when self-hosting Next.js.
## Version History
Version| Changes  
---|---  
`v15.0.0`| `"use cache"` is introduced as an experimental feature.
