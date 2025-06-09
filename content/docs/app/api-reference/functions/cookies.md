---
title: Cookies
path: "App / Api Reference / Functions / Cookies"
source_url: https://nextjs.org/docs/app/api-reference/functions/cookies
content_length: 6521
---

# cookies
`cookies` is an **async** function that allows you to read the HTTP incoming request cookies in Server Components, and read/write outgoing request cookies in Server Actions or Route Handlers.
app/page.tsx
```
import { cookies } from'next/headers'
exportdefaultasyncfunctionPage() {
constcookieStore=awaitcookies()
consttheme=cookieStore.get('theme')
return'...'
}
```

## Reference
### Methods
The following methods are available:
Method| Return Type| Description  
---|---|---  
`get('name')`| Object| Accepts a cookie name and returns an object with the name and value.  
`getAll()`| Array of objects| Returns a list of all the cookies with a matching name.  
`has('name')`| Boolean| Accepts a cookie name and returns a boolean based on if the cookie exists.  
`set(name, value, options)`| -| Accepts a cookie name, value, and options and sets the outgoing request cookie.  
`delete(name)`| -| Accepts a cookie name and deletes the cookie.  
`clear()`| -| Deletes all cookies.  
`toString()`| String| Returns a string representation of the cookies.  
### Options
When setting a cookie, the following properties from the `options` object are supported:
Option| Type| Description  
---|---|---  
`name`| String| Specifies the name of the cookie.  
`value`| String| Specifies the value to be stored in the cookie.  
`expires`| Date| Defines the exact date when the cookie will expire.  
`maxAge`| Number| Sets the cookie’s lifespan in seconds.  
`domain`| String| Specifies the domain where the cookie is available.  
`path`| String, default: `'/'`| Limits the cookie's scope to a specific path within the domain.  
`secure`| Boolean| Ensures the cookie is sent only over HTTPS connections for added security.  
`httpOnly`| Boolean| Restricts the cookie to HTTP requests, preventing client-side access.  
`sameSite`| Boolean, `'lax'`, `'strict'`, `'none'`| Controls the cookie's cross-site request behavior.  
`priority`| String (`"low"`, `"medium"`, `"high"`)| Specifies the cookie's priority  
`encode('value')`| Function| Specifies a function that will be used to encode a cookie's value.  
`partitioned`| Boolean| Indicates whether the cookie is .  
The only option with a default value is `path`.
To learn more about these options, see the .
## Good to know
  * `cookies` is an **asynchronous** function that returns a promise. You must use `async/await` or React's function to access cookies. 
    * In version 14 and earlier, `cookies` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `cookies` is a Dynamic API whose returned values cannot be known ahead of time. Using it in a layout or page will opt a route into dynamic rendering.
  * The `.delete` method can only be called: 
    * In a Server Action or Route Handler.
    * If it belongs to the same domain from which `.set` is called. For wildcard domains, the specific subdomain must be an exact match. Additionally, the code must be executed on the same protocol (HTTP or HTTPS) as the cookie you want to delete.
  * HTTP does not allow setting cookies after streaming starts, so you must use `.set` in a Server Action or Route Handler.


## Understanding Cookie Behavior in Server Components
When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client-side storage mechanism:
  * **Reading cookies** works in Server Components because you're accessing the cookie data that the client's browser sends to the server in the HTTP request headers.
  * **Setting cookies** cannot be done directly in a Server Component, even when using a Route Handler or Server Action. This is because cookies are actually stored by the browser, not the server.


The server can only send instructions (via `Set-Cookie` headers) to tell the browser to store cookies - the actual storage happens on the client side. This is why cookie operations that modify state (`.set`, `.delete`, `.clear`) must be performed in a Route Handler or Server Action where the response headers can be properly set.
## Examples
### Getting a cookie
You can use the `(await cookies()).get('name')` method to get a single cookie:
app/page.tsx
```
import { cookies } from'next/headers'
exportdefaultasyncfunctionPage() {
constcookieStore=awaitcookies()
consttheme=cookieStore.get('theme')
return'...'
}
```

### Getting all cookies
You can use the `(await cookies()).getAll()` method to get all cookies with a matching name. If `name` is unspecified, it returns all the available cookies.
app/page.tsx
```
import { cookies } from'next/headers'
exportdefaultasyncfunctionPage() {
constcookieStore=awaitcookies()
returncookieStore.getAll().map((cookie) => (
  <divkey={cookie.name}>
   <p>Name: {cookie.name}</p>
   <p>Value: {cookie.value}</p>
  </div>
 ))
}
```

### Setting a cookie
You can use the `(await cookies()).set(name, value, options)` method in a Server Action or Route Handler to set a cookie. The `options` object is optional.
app/actions.ts
```
'use server'
import { cookies } from'next/headers'
exportasyncfunctioncreate(data) {
constcookieStore=awaitcookies()
cookieStore.set('name','lee')
// or
cookieStore.set('name','lee', { secure:true })
// or
cookieStore.set({
  name:'name',
  value:'lee',
  httpOnly:true,
  path:'/',
 })
}
```

### Checking if a cookie exists
You can use the `(await cookies()).has(name)` method to check if a cookie exists:
app/page.ts
```
import { cookies } from'next/headers'
exportdefaultasyncfunctionPage() {
constcookieStore=awaitcookies()
consthasCookie=cookieStore.has('theme')
return'...'
}
```

### Deleting cookies
There are three ways you can delete a cookie.
Using the `delete()` method:
app/actions.ts
```
'use server'
import { cookies } from'next/headers'
exportasyncfunctiondelete(data) {
 (awaitcookies()).delete('name')
}
```

Setting a new cookie with the same name and an empty value:
app/actions.ts
```
'use server'
import { cookies } from'next/headers'
exportasyncfunctiondelete(data) {
 (awaitcookies()).set('name','')
}
```

Setting the `maxAge` to 0 will immediately expire a cookie. `maxAge` accepts a value in seconds.
app/actions.ts
```
'use server'
import { cookies } from'next/headers'
exportasyncfunctiondelete(data) {
 (awaitcookies()).set('name','value', { maxAge:0 })
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0-RC`| `cookies` is now an async function. A codemod is available.  
`v13.0.0`| `cookies` introduced.
