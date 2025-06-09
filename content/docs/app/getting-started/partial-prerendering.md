---
title: "How to use Partial Prerendering"
path: "App / Getting Started / Partial Prerendering"
source_url: https://nextjs.org/docs/app/getting-started/partial-prerendering
content_length: 6976
---

# How to use Partial Prerendering
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
Partial Prerendering (PPR) is a rendering strategy that allows you to combine static and dynamic content in the same route. This improves the initial page performance while still supporting personalized, dynamic data.
!Partially Prerendered Product Page showing static nav and product information, and dynamic cart and recommended products!Partially Prerendered Product Page showing static nav and product information, and dynamic cart and recommended products
When a user visits a route:
  * The server sends a **shell** containing the static content, ensuring a fast initial load.
  * The shell leaves **holes** for the dynamic content that will load in asynchronously.
  * The dynamic holes are **streamed in parallel** , reducing the overall load time of the page.


> **🎥 Watch:** Why PPR and how it works → .
## How does Partial Prerendering work?
To understand Partial Prerendering, it helps to be familiar with the rendering strategies available in Next.js.
### Static Rendering
With Static Rendering, HTML is generated ahead of time—either at build time or through revalidation. The result is cached and shared across users and requests.
In Partial Prerendering, Next.js prerenders a **static shell** for a route. This can include the layout and any other components that don't depend on request-time data.
### Dynamic Rendering
With Dynamic Rendering, HTML is generated at **request time**. This allows you to serve personalized content based on request-time data.
A component becomes dynamic if it uses the following APIs:
  * `cookies`
  * `headers`
  * `connection`
  * `draftMode`
  * `searchParams` prop
  * `unstable_noStore`
  * `fetch` with `{ cache: 'no-store' }`


In Partial Prerendering, using these APIs throws a special React error that informs Next.js the component cannot be statically rendered, causing a build error. You can use a Suspense boundary to wrap your component to defer rendering until runtime.
### Suspense
React is used to defer rendering parts of your application until some condition is met.
In Partial Prerendering, Suspense is used to mark **dynamic boundaries** in your component tree.
At build time, Next.js prerenders the static content and the `fallback` UI. The dynamic content is **postponed** until the user requests the route.
Wrapping a component in Suspense doesn't make the component itself dynamic (your API usage does), but rather Suspense is used as a boundary that encapsulates dynamic content and enable streaming
app/page.js
```
import { Suspense } from'react'
import StaticComponent from'./StaticComponent'
import DynamicComponent from'./DynamicComponent'
import Fallback from'./Fallback'
exportconstexperimental_ppr=true
exportdefaultfunctionPage() {
return (
  <>
   <StaticComponent />
   <Suspensefallback={<Fallback />}>
    <DynamicComponent />
   </Suspense>
  </>
 )
}
```

### Streaming
Streaming splits the route into chunks and progressively streams them to the client as they become ready. This allows the user to see parts of the page immediately, before the entire content has finished rendering.
!Diagram showing partially rendered page on the client, with loading UI for chunks that are being streamed.!Diagram showing partially rendered page on the client, with loading UI for chunks that are being streamed.
In Partial Prerendering, dynamic components wrapped in Suspense start streaming from the server in parallel.
!Diagram showing parallelization of route segments during streaming, showing data fetching, rendering, and hydration of individual chunks.!Diagram showing parallelization of route segments during streaming, showing data fetching, rendering, and hydration of individual chunks.
To reduce network overhead, the full response—including static HTML and streamed dynamic parts—is sent in a **single HTTP request**. This avoids extra roundtrips and improves both initial load and overall performance.
## Enabling Partial Prerendering
You can enable PPR by adding the `ppr` option to your `next.config.ts` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  ppr:'incremental',
 },
}
exportdefault nextConfig
```

The `'incremental'` value allows you to adopt PPR for specific routes:
/app/dashboard/layout.tsx
```
exportconstexperimental_ppr=true
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
// ...
}
```

/app/dashboard/layout.js
```
exportconstexperimental_ppr=true
exportdefaultfunctionLayout({ children }) {
// ...
}
```

Routes that don't have `experimental_ppr` will default to `false` and will not be prerendered using PPR. You need to explicitly opt-in to PPR for each route.
> **Good to know** :
>   * `experimental_ppr` will apply to all children of the route segment, including nested layouts and pages. You don't have to add it to every file, only the top segment of a route.
>   * To disable PPR for children segments, you can set `experimental_ppr` to `false` in the child segment.
> 

## Examples
### Dynamic APIs
When using Dynamic APIs that require looking at the incoming request, Next.js will opt into dynamic rendering for the route. To continue using PPR, wrap the component with Suspense. For example, the `<User />` component is dynamic because it uses the `cookies` API:
app/user.tsx
```
import { cookies } from'next/headers'
exportasyncfunctionUser() {
constsession= (awaitcookies()).get('session')?.value
return'...'
}
```

The `<User />` component will be streamed while any other content inside `<Page />` will be prerendered and become part of the static shell.
app/page.tsx
```
import { Suspense } from'react'
import { User, AvatarSkeleton } from'./user'
exportconstexperimental_ppr=true
exportdefaultfunctionPage() {
return (
  <section>
   <h1>This will be prerendered</h1>
   <Suspensefallback={<AvatarSkeleton />}>
    <User />
   </Suspense>
  </section>
 )
}
```

### Passing dynamic props
Components only opt into dynamic rendering when the value is accessed. For example, if you are reading `searchParams` from a `<Page />` component, you can forward this value to another component as a prop:
app/page.tsx
```
import { Table, TableSkeleton } from'./table'
import { Suspense } from'react'
exportdefaultfunctionPage({
 searchParams,
}: {
 searchParams:Promise<{ sort:string }>
}) {
return (
  <section>
   <h1>This will be prerendered</h1>
   <Suspensefallback={<TableSkeleton />}>
    <TablesearchParams={searchParams} />
   </Suspense>
  </section>
 )
}
```

Inside of the table component, accessing the value from `searchParams` will make the component dynamic while the rest of the page will be prerendered.
app/table.tsx
```
exportasyncfunctionTable({
 searchParams,
}: {
 searchParams:Promise<{ sort:string }>
}) {
constsort= (await searchParams).sort ==='true'
return'...'
}
```
