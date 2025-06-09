---
title: Middleware
path: "App / Building Your Application / Routing / Middleware"
source_url: https://nextjs.org/docs/app/building-your-application/routing/middleware
content_length: 15157
---

# Middleware
Middleware allows you to run code before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.
Middleware runs before cached content and routes are matched. See Matching Paths for more details.
## Use Cases
Some common scenarios where Middleware is effective include:
  * Quick redirects after reading parts of the incoming request
  * Rewriting to different pages based on A/B tests or experiments
  * Modifying headers for all pages or a subset of pages


Middleware is _not_ a good fit for:
  * Slow data fetching
  * Session management


## Convention
Use the file `middleware.ts` (or `.js`) in the root of your project to define Middleware. For example, at the same level as `pages` or `app`, or inside `src` if applicable.
> **Note** : While only one `middleware.ts` file is supported per project, you can still organize your middleware logic modularly. Break out middleware functionalities into separate `.ts` or `.js` files and import them into your main `middleware.ts` file. This allows for cleaner management of route-specific middleware, aggregated in the `middleware.ts` for centralized control. By enforcing a single middleware file, it simplifies configuration, prevents potential conflicts, and optimizes performance by avoiding multiple middleware layers.
## Example
middleware.ts
```
import { NextResponse } from'next/server'
importtype { NextRequest } from'next/server'
// This function can be marked `async` if using `await` inside
exportfunctionmiddleware(request:NextRequest) {
returnNextResponse.redirect(newURL('/home',request.url))
}
// See "Matching Paths" below to learn more
exportconstconfig= {
 matcher:'/about/:path*',
}
```

## Matching Paths
Middleware will be invoked for **every route in your project**. Given this, it's crucial to use matchers to precisely target or exclude specific routes. The following is the execution order:
  1. `headers` from `next.config.js`
  2. `redirects` from `next.config.js`
  3. Middleware (`rewrites`, `redirects`, etc.)
  4. `beforeFiles` (`rewrites`) from `next.config.js`
  5. Filesystem routes (`public/`, `_next/static/`, `pages/`, `app/`, etc.)
  6. `afterFiles` (`rewrites`) from `next.config.js`
  7. Dynamic Routes (`/blog/[slug]`)
  8. `fallback` (`rewrites`) from `next.config.js`


There are two ways to define which paths Middleware will run on:
  1. Custom matcher config
  2. Conditional statements


### Matcher
`matcher` allows you to filter Middleware to run on specific paths.
middleware.js
```
exportconstconfig= {
 matcher:'/about/:path*',
}
```

You can match a single path or multiple paths with an array syntax:
middleware.js
```
exportconstconfig= {
 matcher: ['/about/:path*','/dashboard/:path*'],
}
```

The `matcher` config allows full regex so matching like negative lookaheads or character matching is supported. An example of a negative lookahead to match all except specific paths can be seen here:
middleware.js
```
exportconstconfig= {
 matcher: [
/*
   * Match all request paths except for the ones starting with:
   * - api (API routes)
   * - _next/static (static files)
   * - _next/image (image optimization files)
   * - favicon.ico, sitemap.xml, robots.txt (metadata files)
   */
'/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
 ],
}
```

You can also bypass Middleware for certain requests by using the `missing` or `has` arrays, or a combination of both:
middleware.js
```
exportconstconfig= {
 matcher: [
/*
   * Match all request paths except for the ones starting with:
   * - api (API routes)
   * - _next/static (static files)
   * - _next/image (image optimization files)
   * - favicon.ico, sitemap.xml, robots.txt (metadata files)
   */
  {
   source:
'/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
   missing: [
    { type:'header', key:'next-router-prefetch' },
    { type:'header', key:'purpose', value:'prefetch' },
   ],
  },
  {
   source:
'/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
   has: [
    { type:'header', key:'next-router-prefetch' },
    { type:'header', key:'purpose', value:'prefetch' },
   ],
  },
  {
   source:
'/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
   has: [{ type:'header', key:'x-present' }],
   missing: [{ type:'header', key:'x-missing', value:'prefetch' }],
  },
 ],
}
```

> **Good to know** : The `matcher` values need to be constants so they can be statically analyzed at build-time. Dynamic values such as variables will be ignored.
Configured matchers:
  1. MUST start with `/`
  2. Can include named parameters: `/about/:path` matches `/about/a` and `/about/b` but not `/about/a/c`
  3. Can have modifiers on named parameters (starting with `:`): `/about/:path*` matches `/about/a/b/c` because `*` is _zero or more_. `?` is _zero or one_ and `+` _one or more_
  4. Can use regular expression enclosed in parenthesis: `/about/(.*)` is the same as `/about/:path*`


Read more details on documentation.
> **Good to know** : For backward compatibility, Next.js always considers `/public` as `/public/index`. Therefore, a matcher of `/public/:path` will match.
### Conditional Statements
middleware.ts
```
import { NextResponse } from'next/server'
importtype { NextRequest } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
if (request.nextUrl.pathname.startsWith('/about')) {
returnNextResponse.rewrite(newURL('/about-2',request.url))
 }
if (request.nextUrl.pathname.startsWith('/dashboard')) {
returnNextResponse.rewrite(newURL('/dashboard/user',request.url))
 }
}
```

## NextResponse
The `NextResponse` API allows you to:
  * `redirect` the incoming request to a different URL
  * `rewrite` the response by displaying a given URL
  * Set request headers for API Routes, `getServerSideProps`, and `rewrite` destinations
  * Set response cookies
  * Set response headers


To produce a response from Middleware, you can:
  1. `rewrite` to a route (Page or Route Handler) that produces a response
  2. return a `NextResponse` directly. See Producing a Response


## Using Cookies
Cookies are regular headers. On a `Request`, they are stored in the `Cookie` header. On a `Response` they are in the `Set-Cookie` header. Next.js provides a convenient way to access and manipulate these cookies through the `cookies` extension on `NextRequest` and `NextResponse`.
  1. For incoming requests, `cookies` comes with the following methods: `get`, `getAll`, `set`, and `delete` cookies. You can check for the existence of a cookie with `has` or remove all cookies with `clear`.
  2. For outgoing responses, `cookies` have the following methods `get`, `getAll`, `set`, and `delete`.


middleware.ts
```
import { NextResponse } from'next/server'
importtype { NextRequest } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
// Assume a "Cookie:nextjs=fast" header to be present on the incoming request
// Getting cookies from the request using the `RequestCookies` API
let cookie =request.cookies.get('nextjs')
console.log(cookie) // => { name: 'nextjs', value: 'fast', Path: '/' }
constallCookies=request.cookies.getAll()
console.log(allCookies) // => [{ name: 'nextjs', value: 'fast' }]
request.cookies.has('nextjs') // => true
request.cookies.delete('nextjs')
request.cookies.has('nextjs') // => false
// Setting cookies on the response using the `ResponseCookies` API
constresponse=NextResponse.next()
response.cookies.set('vercel','fast')
response.cookies.set({
  name:'vercel',
  value:'fast',
  path:'/',
 })
 cookie =response.cookies.get('vercel')
console.log(cookie) // => { name: 'vercel', value: 'fast', Path: '/' }
// The outgoing response will have a `Set-Cookie:vercel=fast;path=/` header.
return response
}
```

## Setting Headers
You can set request and response headers using the `NextResponse` API (setting _request_ headers is available since Next.js v13.0.0).
middleware.ts
```
import { NextResponse } from'next/server'
importtype { NextRequest } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
// Clone the request headers and set a new header `x-hello-from-middleware1`
constrequestHeaders=newHeaders(request.headers)
requestHeaders.set('x-hello-from-middleware1','hello')
// You can also set request headers in NextResponse.next
constresponse=NextResponse.next({
  request: {
// New request headers
   headers: requestHeaders,
  },
 })
// Set a new response header `x-hello-from-middleware2`
response.headers.set('x-hello-from-middleware2','hello')
return response
}
```

> **Good to know** : Avoid setting large headers as it might cause error depending on your backend web server configuration.
### CORS
You can set CORS headers in Middleware to allow cross-origin requests, including and requests.
middleware.ts
```
import { NextRequest, NextResponse } from'next/server'
constallowedOrigins= [']
constcorsOptions= {
'Access-Control-Allow-Methods':'GET, POST, PUT, DELETE, OPTIONS',
'Access-Control-Allow-Headers':'Content-Type, Authorization',
}
exportfunctionmiddleware(request:NextRequest) {
// Check the origin from the request
constorigin=request.headers.get('origin') ??''
constisAllowedOrigin=allowedOrigins.includes(origin)
// Handle preflighted requests
constisPreflight=request.method ==='OPTIONS'
if (isPreflight) {
constpreflightHeaders= {
...(isAllowedOrigin && { 'Access-Control-Allow-Origin': origin }),
...corsOptions,
  }
returnNextResponse.json({}, { headers: preflightHeaders })
 }
// Handle simple requests
constresponse=NextResponse.next()
if (isAllowedOrigin) {
response.headers.set('Access-Control-Allow-Origin', origin)
 }
Object.entries(corsOptions).forEach(([key, value]) => {
response.headers.set(key, value)
 })
return response
}
exportconstconfig= {
 matcher:'/api/:path*',
}
```

> **Good to know:** You can configure CORS headers for individual routes in Route Handlers.
## Producing a Response
You can respond from Middleware directly by returning a `Response` or `NextResponse` instance. (This is available since Next.js v13.1.0)
middleware.ts
```
importtype { NextRequest } from'next/server'
import { isAuthenticated } from'@lib/auth'
// Limit the middleware to paths starting with `/api/`
exportconstconfig= {
 matcher:'/api/:function*',
}
exportfunctionmiddleware(request:NextRequest) {
// Call our authentication function to check the request
if (!isAuthenticated(request)) {
// Respond with JSON indicating an error message
returnResponse.json(
   { success:false, message:'authentication failed' },
   { status:401 }
  )
 }
}
```

### `waitUntil` and `NextFetchEvent`
The `NextFetchEvent` object extends the native object, and includes the method.
The `waitUntil()` method takes a promise as an argument, and extends the lifetime of the Middleware until the promise settles. This is useful for performing work in the background.
middleware.ts
```
import { NextResponse } from'next/server'
importtype { NextFetchEvent, NextRequest } from'next/server'
exportfunctionmiddleware(req:NextRequest, event:NextFetchEvent) {
event.waitUntil(
fetch(' {
   method:'POST',
   body:JSON.stringify({ pathname:req.nextUrl.pathname }),
  })
 )
returnNextResponse.next()
}
```

## Advanced Middleware Flags
In `v13.1` of Next.js two additional flags were introduced for middleware, `skipMiddlewareUrlNormalize` and `skipTrailingSlashRedirect` to handle advanced use cases.
`skipTrailingSlashRedirect` disables Next.js redirects for adding or removing trailing slashes. This allows custom handling inside middleware to maintain the trailing slash for some paths but not others, which can make incremental migrations easier.
next.config.js
```
module.exports= {
 skipTrailingSlashRedirect:true,
}
```

middleware.js
```
constlegacyPrefixes= ['/docs','/blog']
exportdefaultasyncfunctionmiddleware(req) {
const { pathname } =req.nextUrl
if (legacyPrefixes.some((prefix) =>pathname.startsWith(prefix))) {
returnNextResponse.next()
 }
// apply trailing slash handling
if (
!pathname.endsWith('/') &&
!pathname.match(/((?!\.well-known(?:\/.*)?)(?:[^/]+\/)*[^/]+\.\w+)/)
 ) {
returnNextResponse.redirect(
newURL(`${req.nextUrl.pathname}/`,req.nextUrl)
  )
 }
}
```

`skipMiddlewareUrlNormalize` allows for disabling the URL normalization in Next.js to make handling direct visits and client-transitions the same. In some advanced cases, this option provides full control by using the original URL.
next.config.js
```
module.exports= {
 skipMiddlewareUrlNormalize:true,
}
```

middleware.js
```
exportdefaultasyncfunctionmiddleware(req) {
const { pathname } =req.nextUrl
// GET /_next/data/build-id/hello.json
console.log(pathname)
// with the flag this now /_next/data/build-id/hello.json
// without the flag this would be normalized to /hello
}
```

## Unit Testing (experimental)
Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test middleware files. Unit testing middleware can help ensure that it's only run on desired paths and that custom routing logic works as intended before code reaches production.
The `unstable_doesMiddlewareMatch` function can be used to assert whether middleware will run for the provided URL, headers, and cookies.
```
import { unstable_doesMiddlewareMatch } from'next/experimental/testing/server'
expect(
unstable_doesMiddlewareMatch({
  config,
  nextConfig,
  url:'/test',
 })
).toEqual(false)
```

The entire middleware function can also be tested.
```
import { isRewrite, getRewrittenUrl } from'next/experimental/testing/server'
constrequest=newNextRequest('
constresponse=awaitmiddleware(request)
expect(isRewrite(response)).toEqual(true)
expect(getRewrittenUrl(response)).toEqual('
// getRedirectUrl could also be used if the response were a redirect
```

## Runtime
Middleware defaults to using the Edge runtime. As of v15.2 (canary), we have experimental support for using the Node.js runtime. To enable, add the flag to your `next.config` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  nodeMiddleware:true,
 },
}
exportdefault nextConfig
```

Then in your middleware file, set the runtime to `nodejs` in the `config` object:
middleware.ts
```
exportconstconfig= {
 runtime:'nodejs',
}
```

> **Note** : This feature is not yet recommended for production use. Therefore, Next.js will throw an error unless you are using the next@canary release instead of the stable release.
## Platform Support
Deployment Option| Supported  
---|---  
Node.js server| Yes  
Docker container| Yes  
Static export| No  
Adapters| Platform-specific  
Learn how to configure Middleware when self-hosting Next.js.
## Version History
Version| Changes  
---|---  
`v15.2.0`| Middleware can now use the Node.js runtime (experimental)  
`v13.1.0`| Advanced Middleware flags added  
`v13.0.0`| Middleware can modify request headers, response headers, and send responses  
`v12.2.0`| Middleware is stable, please see the upgrade guide  
`v12.0.9`| Enforce absolute URLs in Edge Runtime ()  
`v12.0.0`| Middleware (Beta) added
