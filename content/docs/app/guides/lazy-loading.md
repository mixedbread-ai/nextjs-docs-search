---
title: "How to lazy load Client Components and libraries"
path: "App / Guides / Lazy Loading"
source_url: https://nextjs.org/docs/app/guides/lazy-loading
content_length: 4518
---

# How to lazy load Client Components and libraries
in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.
It allows you to defer loading of **Client Components** and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.
There are two ways you can implement lazy loading in Next.js:
  1. Using Dynamic Imports with `next/dynamic`
  2. Using with 


By default, Server Components are automatically , and you can use streaming to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.
## `next/dynamic`
`next/dynamic` is a composite of and . It behaves the same way in the `app` and `pages` directories to allow for incremental migration.
## Examples
### Importing Client Components
app/page.js
```
'use client'
import { useState } from'react'
import dynamic from'next/dynamic'
// Client Components:
constComponentA=dynamic(() =>import('../components/A'))
constComponentB=dynamic(() =>import('../components/B'))
constComponentC=dynamic(() =>import('../components/C'), { ssr:false })
exportdefaultfunctionClientComponentExample() {
const [showMore,setShowMore] =useState(false)
return (
  <div>
   {/* Load immediately, but in a separate client bundle */}
   <ComponentA />
   {/* Load on demand, only when/if the condition is met */}
   {showMore && <ComponentB />}
   <buttononClick={() =>setShowMore(!showMore)}>Toggle</button>
   {/* Load only on the client side */}
   <ComponentC />
  </div>
 )
}
```

> **Note:** When a Server Component dynamically imports a Client Component, automatic is currently **not** supported.
### Skipping SSR
When using `React.lazy()` and Suspense, Client Components will be (SSR) by default.
> **Note:** `ssr: false` option will only work for Client Components, move it into Client Components ensure the client code-splitting working properly.
If you want to disable pre-rendering for a Client Component, you can use the `ssr` option set to `false`:
```
constComponentC=dynamic(() =>import('../components/C'), { ssr:false })
```

### Importing Server Components
If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself. It will also help preload the static assets such as CSS when you're using it in Server Components.
app/page.js
```
import dynamic from'next/dynamic'
// Server Component:
constServerComponent=dynamic(() =>import('../components/ServerComponent'))
exportdefaultfunctionServerComponentExample() {
return (
  <div>
   <ServerComponent />
  </div>
 )
}
```

> **Note:** `ssr: false` option is not supported in Server Components. You will see an error if you try to use it in Server Components. `ssr: false` is not allowed with `next/dynamic` in Server Components. Please move it into a Client Component.
### Loading External Libraries
External libraries can be loaded on demand using the function. This example uses the external library `fuse.js` for fuzzy search. The module is only loaded on the client after the user types in the search input.
app/page.js
```
'use client'
import { useState } from'react'
constnames= ['Tim','Joe','Bel','Lee']
exportdefaultfunctionPage() {
const [results,setResults] =useState()
return (
  <div>
   <input
type="text"
placeholder="Search"
onChange={async (e) => {
const { value } =e.currentTarget
// Dynamically load fuse.js
constFuse= (awaitimport('fuse.js')).default
constfuse=newFuse(names)
setResults(fuse.search(value))
    }}
   />
   <pre>Results: {JSON.stringify(results,null,2)}</pre>
  </div>
 )
}
```

### Adding a custom loading component
app/page.js
```
'use client'
import dynamic from'next/dynamic'
constWithCustomLoading=dynamic(
 () =>import('../components/WithCustomLoading'),
 {
loading: () => <p>Loading...</p>,
 }
)
exportdefaultfunctionPage() {
return (
  <div>
   {/* The loading component will be rendered while <WithCustomLoading/> is loading */}
   <WithCustomLoading />
  </div>
 )
}
```

### Importing Named Exports
To dynamically import a named export, you can return it from the Promise returned by function:
components/hello.js
```
'use client'
exportfunctionHello() {
return <p>Hello!</p>
}
```

app/page.js
```
import dynamic from'next/dynamic'
constClientComponent=dynamic(() =>
import('../components/hello').then((mod) =>mod.Hello)
)
```
