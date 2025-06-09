---
title: "Route Handlers"
path: "App / Building Your Application / Routing / Route Handlers"
source_url: https://nextjs.org/docs/app/building-your-application/routing/route-handlers
content_length: 9711
---

# Route Handlers
Route Handlers allow you to create custom request handlers for a given route using the Web and APIs.
!Route.js Special File!Route.js Special File
> **Good to know** : Route Handlers are only available inside the `app` directory. They are the equivalent of API Routes inside the `pages` directory meaning you **do not** need to use API Routes and Route Handlers together.
## Convention
Route Handlers are defined in a `route.js|ts` file inside the `app` directory:
app/api/route.ts
```
exportasyncfunctionGET(request:Request) {}
```

Route Handlers can be nested anywhere inside the `app` directory, similar to `page.js` and `layout.js`. But there **cannot** be a `route.js` file at the same route segment level as `page.js`.
### Supported HTTP Methods
The following are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`. If an unsupported method is called, Next.js will return a `405 Method Not Allowed` response.
### Extended `NextRequest` and `NextResponse` APIs
In addition to supporting the native and APIs, Next.js extends them with `NextRequest` and `NextResponse` to provide convenient helpers for advanced use cases.
## Behavior
### Caching
Route Handlers are not cached by default. You can, however, opt into caching for `GET` methods. Other supported HTTP methods are **not** cached. To cache a `GET` method, use a route config option such as `export const dynamic = 'force-static'` in your Route Handler file.
app/items/route.ts
```
exportconstdynamic='force-static'
exportasyncfunctionGET() {
constres=awaitfetch(' {
  headers: {
'Content-Type':'application/json',
'API-Key':process.env.DATA_API_KEY,
  },
 })
constdata=awaitres.json()
returnResponse.json({ data })
}
```

> **Good to know** : Other supported HTTP methods are **not** cached, even if they are placed alongside a `GET` method that is cached, in the same file.
### Special Route Handlers
Special Route Handlers like `sitemap.ts`, `opengraph-image.tsx`, and `icon.tsx`, and other metadata files remain static by default unless they use Dynamic APIs or dynamic config options.
### Route Resolution
You can consider a `route` the lowest level routing primitive.
  * They **do not** participate in layouts or client-side navigations like `page`.
  * There **cannot** be a `route.js` file at the same route as `page.js`.


Page| Route| Result  
---|---|---  
`app/page.js`| `app/route.js`|  Conflict  
`app/page.js`| `app/api/route.js`|  Valid  
`app/[user]/page.js`| `app/api/route.js`|  Valid  
Each `route.js` or `page.js` file takes over all HTTP verbs for that route.
app/page.ts
```
exportdefaultfunctionPage() {
return <h1>Hello,Next.js!</h1>
}
// ❌ Conflict
// `app/route.ts`
exportasyncfunctionPOST(request:Request) {}
```

## Examples
The following examples show how to combine Route Handlers with other Next.js APIs and features.
### Revalidating Cached Data
You can revalidate cached data using Incremental Static Regeneration (ISR):
app/posts/route.ts
```
exportconstrevalidate=60
exportasyncfunctionGET() {
constdata=awaitfetch('
constposts=awaitdata.json()
returnResponse.json(posts)
}
```

### Cookies
You can read or set cookies with `cookies` from `next/headers`. This server function can be called directly in a Route Handler, or nested inside of another function.
Alternatively, you can return a new `Response` using the header.
app/api/route.ts
```
import { cookies } from'next/headers'
exportasyncfunctionGET(request:Request) {
constcookieStore=awaitcookies()
consttoken=cookieStore.get('token')
returnnewResponse('Hello, Next.js!', {
  status:200,
  headers: { 'Set-Cookie':`token=${token.value}` },
 })
}
```

You can also use the underlying Web APIs to read cookies from the request (`NextRequest`):
app/api/route.ts
```
import { type NextRequest } from'next/server'
exportasyncfunctionGET(request:NextRequest) {
consttoken=request.cookies.get('token')
}
```

### Headers
You can read headers with `headers` from `next/headers`. This server function can be called directly in a Route Handler, or nested inside of another function.
This `headers` instance is read-only. To set headers, you need to return a new `Response` with new `headers`.
app/api/route.ts
```
import { headers } from'next/headers'
exportasyncfunctionGET(request:Request) {
constheadersList=awaitheaders()
constreferer=headersList.get('referer')
returnnewResponse('Hello, Next.js!', {
  status:200,
  headers: { referer: referer },
 })
}
```

You can also use the underlying Web APIs to read headers from the request (`NextRequest`):
app/api/route.ts
```
import { type NextRequest } from'next/server'
exportasyncfunctionGET(request:NextRequest) {
constrequestHeaders=newHeaders(request.headers)
}
```

### Redirects
app/api/route.ts
```
import { redirect } from'next/navigation'
exportasyncfunctionGET(request:Request) {
redirect('
}
```

### Dynamic Route Segments
Route Handlers can use Dynamic Segments to create request handlers from dynamic data.
app/items/[slug]/route.ts
```
exportasyncfunctionGET(
 request:Request,
 { params }: { params:Promise<{ slug:string }> }
) {
const { slug } =await params // 'a', 'b', or 'c'
}
```

Route| Example URL| `params`  
---|---|---  
`app/items/[slug]/route.js`| `/items/a`| `Promise<{ slug: 'a' }>`  
`app/items/[slug]/route.js`| `/items/b`| `Promise<{ slug: 'b' }>`  
`app/items/[slug]/route.js`| `/items/c`| `Promise<{ slug: 'c' }>`  
### URL Query Parameters
The request object passed to the Route Handler is a `NextRequest` instance, which includes some additional convenience methods, such as those for more easily handling query parameters.
app/api/search/route.ts
```
import { type NextRequest } from'next/server'
exportfunctionGET(request:NextRequest) {
constsearchParams=request.nextUrl.searchParams
constquery=searchParams.get('query')
// query is "hello" for /api/search?query=hello
}
```

### Streaming
Streaming is commonly used in combination with Large Language Models (LLMs), such as OpenAI, for AI-generated content. Learn more about the .
app/api/chat/route.ts
```
import { openai } from'@ai-sdk/openai'
import { StreamingTextResponse, streamText } from'ai'
exportasyncfunctionPOST(req:Request) {
const { messages } =awaitreq.json()
constresult=awaitstreamText({
  model:openai('gpt-4-turbo'),
  messages,
 })
returnnewStreamingTextResponse(result.toAIStream())
}
```

These abstractions use the Web APIs to create a stream. You can also use the underlying Web APIs directly.
app/api/route.ts
```
// 
functioniteratorToStream(iterator:any) {
returnnewReadableStream({
asyncpull(controller) {
const { value,done } =awaititerator.next()
if (done) {
controller.close()
   } else {
controller.enqueue(value)
   }
  },
 })
}
functionsleep(time:number) {
returnnewPromise((resolve) => {
setTimeout(resolve, time)
 })
}
constencoder=newTextEncoder()
asyncfunction*makeIterator() {
yieldencoder.encode('<p>One</p>')
awaitsleep(200)
yieldencoder.encode('<p>Two</p>')
awaitsleep(200)
yieldencoder.encode('<p>Three</p>')
}
exportasyncfunctionGET() {
constiterator=makeIterator()
conststream=iteratorToStream(iterator)
returnnewResponse(stream)
}
```

### Request Body
You can read the `Request` body using the standard Web API methods:
app/items/route.ts
```
exportasyncfunctionPOST(request:Request) {
constres=awaitrequest.json()
returnResponse.json({ res })
}
```

### Request Body FormData
You can read the `FormData` using the `request.formData()` function:
app/items/route.ts
```
exportasyncfunctionPOST(request:Request) {
constformData=awaitrequest.formData()
constname=formData.get('name')
constemail=formData.get('email')
returnResponse.json({ name, email })
}
```

Since `formData` data are all strings, you may want to use to validate the request and retrieve data in the format you prefer (e.g. `number`).
### CORS
You can set CORS headers for a specific Route Handler using the standard Web API methods:
app/api/route.ts
```
exportasyncfunctionGET(request:Request) {
returnnewResponse('Hello, Next.js!', {
  status:200,
  headers: {
'Access-Control-Allow-Origin':'*',
'Access-Control-Allow-Methods':'GET, POST, PUT, DELETE, OPTIONS',
'Access-Control-Allow-Headers':'Content-Type, Authorization',
  },
 })
}
```

> **Good to know** :
>   * To add CORS headers to multiple Route Handlers, you can use Middleware or the `next.config.js` file.
>   * Alternatively, see our package.
> 

### Webhooks
You can use a Route Handler to receive webhooks from third-party services:
app/api/route.ts
```
exportasyncfunctionPOST(request:Request) {
try {
consttext=awaitrequest.text()
// Process the webhook payload
 } catch (error) {
returnnewResponse(`Webhook error: ${error.message}`, {
   status:400,
  })
 }
returnnewResponse('Success!', {
  status:200,
 })
}
```

Notably, unlike API Routes with the Pages Router, you do not need to use `bodyParser` to use any additional configuration.
### Non-UI Responses
You can use Route Handlers to return non-UI content. Note that `sitemap.xml`, `robots.txt`, `app icons`, and open graph images all have built-in support.
app/rss.xml/route.ts
```
exportasyncfunctionGET() {
returnnewResponse(
`<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>Next.js Documentation</title>
 <link></link>
 <description>The React Framework for the Web</description>
</channel>
</rss>`,
  {
   headers: {
'Content-Type':'text/xml',
   },
  }
 )
}
```

### Segment Config Options
Route Handlers use the same route segment configuration as pages and layouts.
app/items/route.ts
```
exportconstdynamic='auto'
exportconstdynamicParams=true
exportconstrevalidate=false
exportconstfetchCache='auto'
exportconstruntime='nodejs'
exportconstpreferredRegion='auto'
```

See the API reference for more details.
