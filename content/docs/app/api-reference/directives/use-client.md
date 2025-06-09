---
title: "Use client"
path: "App / Api Reference / Directives / Use Client"
source_url: https://nextjs.org/docs/app/api-reference/directives/use-client
content_length: 2474
---

# use client
The `'use client'` directive declares an entry point for the components to be rendered on the **client side** and should be used when creating interactive user interfaces (UI) that require client-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.
> **Good to know:**
> You do not need to add the `'use client'` directive to every file that contains Client Components. You only need to add it to the files whose components you want to render directly within Server Components. The `'use client'` directive defines the client-server boundary, and the components exported from such a file serve as entry points to the client.
## Usage
To declare an entry point for the Client Components, add the `'use client'` directive **at the top of the file** , before any imports:
app/components/counter.tsx
```
'use client'
import { useState } from'react'
exportdefaultfunctionCounter() {
const [count,setCount] =useState(0)
return (
  <div>
   <p>Count: {count}</p>
   <buttononClick={() =>setCount(count +1)}>Increment</button>
  </div>
 )
}
```

When using the `'use client'` directive, the props of the Client Components must be . This means the props need to be in a format that React can serialize when sending data from the server to the client.
app/components/counter.tsx
```
'use client'
exportdefaultfunctionCounter({
 onClick /* ❌ Function is not serializable */,
}) {
return (
  <div>
   <buttononClick={onClick}>Increment</button>
  </div>
 )
}
```

## Nesting Client Components within Server Components
Combining Server and Client Components allows you to build applications that are both performant and interactive:
  1. **Server Components** : Use for static content, data fetching, and SEO-friendly elements.
  2. **Client Components** : Use for interactive elements that require state, effects, or browser APIs.
  3. **Component composition** : Nest Client Components within Server Components as needed for a clear separation of server and client logic.


In the following example:
  * `Header` is a Server Component handling static content.
  * `Counter` is a Client Component enabling interactivity within the page.


app/page.tsx
```
import Header from'./header'
import Counter from'./counter'// This is a Client Component
exportdefaultfunctionPage() {
return (
  <div>
   <Header />
   <Counter />
  </div>
 )
}
```

## Reference
See the for more information on `'use client'`.
