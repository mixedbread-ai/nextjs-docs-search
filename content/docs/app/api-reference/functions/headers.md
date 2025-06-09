---
title: Headers
path: "App / Api Reference / Functions / Headers"
source_url: https://nextjs.org/docs/app/api-reference/functions/headers
content_length: 2093
---

# headers
`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a Server Component.
app/page.tsx
```
import { headers } from'next/headers'
exportdefaultasyncfunctionPage() {
constheadersList=awaitheaders()
constuserAgent=headersList.get('user-agent')
}
```

## Reference
### Parameters
`headers` does not take any parameters.
### Returns
`headers` returns a **read-only** object.
  * : Returns an allowing to go through all key/value pairs contained in this object.
  * : Executes a provided function once for each key/value pair in this `Headers` object.
  * : Returns a sequence of all the values of a header within a `Headers` object with a given name.
  * : Returns a boolean stating whether a `Headers` object contains a certain header.
  * : Returns an allowing you to go through all keys of the key/value pairs contained in this object.
  * : Returns an allowing you to go through all values of the key/value pairs contained in this object.


## Good to know
  * `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's function. 
    * In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * Since `headers` is read-only, you cannot `set` or `delete` the outgoing request headers.
  * `headers` is a Dynamic API whose returned values cannot be known ahead of time. Using it in will opt a route into **dynamic rendering**.


## Examples
### Using the Authorization header
app/page.js
```
import { headers } from'next/headers'
exportdefaultasyncfunctionPage() {
constauthorization= (awaitheaders()).get('authorization')
constres=awaitfetch('...', {
  headers: { authorization },// Forward the authorization header
 })
constuser=awaitres.json()
return <h1>{user.name}</h1>
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0-RC`| `headers` is now an async function. A codemod is available.  
`v13.0.0`| `headers` introduced.
