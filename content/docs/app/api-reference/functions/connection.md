---
title: Connection
path: "App / Api Reference / Functions / Connection"
source_url: https://nextjs.org/docs/app/api-reference/functions/connection
content_length: 1231
---

# connection
The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.
It's useful when a component doesn’t use Dynamic APIs, but you want it to be dynamically rendered at runtime and not statically rendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.
app/page.tsx
```
import { connection } from'next/server'
exportdefaultasyncfunctionPage() {
awaitconnection()
// Everything below will be excluded from prerendering
constrand=Math.random()
return <span>{rand}</span>
}
```

## Reference
### Type
```
functionconnection():Promise<void>
```

### Parameters
  * The function does not accept any parameters.


### Returns
  * The function returns a `void` Promise. It is not meant to be consumed.


## Good to know
  * `connection` replaces `unstable_noStore` to better align with the future of Next.js.
  * The function is only necessary when dynamic rendering is required and common Dynamic APIs are not used.


### Version History
Version| Changes  
---|---  
`v15.0.0`| `connection` stabilized.  
`v15.0.0-RC`| `connection` introduced.
