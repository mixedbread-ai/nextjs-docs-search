---
title: NextResponse
path: "App / Api Reference / Functions / Next Response"
source_url: https://nextjs.org/docs/app/api-reference/functions/next-response
content_length: 3337
---

# NextResponse
NextResponse extends the with additional convenience methods.
## `cookies`
Read or mutate the header of the response.
### `set(name, value)`
Given a name, set a cookie with the given value on the response.
```
// Given incoming request /home
let response =NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner','false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

### `get(name)`
Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.
```
// Given incoming request /home
let response =NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

### `getAll()`
Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.
```
// Given incoming request /home
let response =NextResponse.next()
// [
//  { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//  { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

### `delete(name)`
Given a cookie name, delete the cookie from the response.
```
// Given incoming request /home
let response =NextResponse.next()
// Returns true for deleted, false is nothing is deleted
response.cookies.delete('experiments')
```

## `json()`
Produce a response with the given JSON body.
app/api/route.ts
```
import { NextResponse } from'next/server'
exportasyncfunctionGET(request:Request) {
returnNextResponse.json({ error:'Internal Server Error' }, { status:500 })
}
```

## `redirect()`
Produce a response that redirects to a .
```
import { NextResponse } from'next/server'
returnNextResponse.redirect(newURL('/new',request.url))
```

The can be created and modified before being used in the `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.
```
import { NextResponse } from'next/server'
// Given an incoming request...
constloginUrl=newURL('/login',request.url)
// Add ?from=/incoming-url to the /login URL
loginUrl.searchParams.set('from',request.nextUrl.pathname)
// And redirect to the new URL
returnNextResponse.redirect(loginUrl)
```

## `rewrite()`
Produce a response that rewrites (proxies) the given while preserving the original URL.
```
import { NextResponse } from'next/server'
// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
returnNextResponse.rewrite(newURL('/proxy',request.url))
```

## `next()`
The `next()` method is useful for Middleware, as it allows you to return early and continue routing.
```
import { NextResponse } from'next/server'
returnNextResponse.next()
```

You can also forward `headers` when producing the response:
```
import { NextResponse } from'next/server'
// Given an incoming request...
constnewHeaders=newHeaders(request.headers)
// Add a new header
newHeaders.set('x-version','123')
// And produce a response with the new headers
returnNextResponse.next({
 request: {
// New request headers
  headers: newHeaders,
 },
})
```
