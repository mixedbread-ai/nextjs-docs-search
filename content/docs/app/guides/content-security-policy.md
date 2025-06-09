---
title: "How to set a Content Security Policy (CSP) for your Next.js application"
path: "App / Guides / Content Security Policy"
source_url: https://nextjs.org/docs/app/guides/content-security-policy
content_length: 3893
---

# How to set a Content Security Policy (CSP) for your Next.js application
is important to guard your Next.js application against various security threats such as cross-site scripting (XSS), clickjacking, and other code injection attacks.
By using CSP, developers can specify which origins are permissible for content sources, scripts, stylesheets, images, fonts, objects, media (audio, video), iframes, and more.
Examples
## Nonces
A is a unique, random string of characters created for a one-time use. It is used in conjunction with CSP to selectively allow certain inline scripts or styles to execute, bypassing strict CSP directives.
### Why use a nonce?
Even though CSPs are designed to block malicious scripts, there are legitimate scenarios where inline scripts are necessary. In such cases, nonces offer a way to allow these scripts to execute if they have the correct nonce.
### Adding a nonce with Middleware
Middleware enables you to add headers and generate nonces before the page renders.
Every time a page is viewed, a fresh nonce should be generated. This means that you **must use dynamic rendering to add nonces**.
For example:
middleware.ts
```
import { NextRequest, NextResponse } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
constnonce=Buffer.from(crypto.randomUUID()).toString('base64')
constcspHeader=`
  default-src 'self';
  script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
  style-src 'self' 'nonce-${nonce}';
  img-src 'self' blob: data:;
  font-src 'self';
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  frame-ancestors 'none';
  upgrade-insecure-requests;
`
// Replace newline characters and spaces
constcontentSecurityPolicyHeaderValue= cspHeader
.replace(/\s{2,}/g,' ')
.trim()
constrequestHeaders=newHeaders(request.headers)
requestHeaders.set('x-nonce', nonce)
requestHeaders.set(
'Content-Security-Policy',
  contentSecurityPolicyHeaderValue
 )
constresponse=NextResponse.next({
  request: {
   headers: requestHeaders,
  },
 })
response.headers.set(
'Content-Security-Policy',
  contentSecurityPolicyHeaderValue
 )
return response
}
```

By default, Middleware runs on all requests. You can filter Middleware to run on specific paths using a `matcher`.
We recommend ignoring matching prefetches (from `next/link`) and static assets that don't need the CSP header.
middleware.ts
```
exportconstconfig= {
 matcher: [
/*
   * Match all request paths except for the ones starting with:
   * - api (API routes)
   * - _next/static (static files)
   * - _next/image (image optimization files)
   * - favicon.ico (favicon file)
   */
  {
   source:'/((?!api|_next/static|_next/image|favicon.ico).*)',
   missing: [
    { type:'header', key:'next-router-prefetch' },
    { type:'header', key:'purpose', value:'prefetch' },
   ],
  },
 ],
}
```

### Reading the nonce
You can read the nonce from a Server Component using `headers`:
app/page.tsx
```
import { headers } from'next/headers'
import Script from'next/script'
exportdefaultasyncfunctionPage() {
constnonce= (awaitheaders()).get('x-nonce')
return (
  <Script
src=""
strategy="afterInteractive"
nonce={nonce}
  />
 )
}
```

## Without Nonces
For applications that do not require nonces, you can set the CSP header directly in your `next.config.js` file:
next.config.js
```
constcspHeader=`
  default-src 'self';
  script-src 'self' 'unsafe-eval' 'unsafe-inline';
  style-src 'self' 'unsafe-inline';
  img-src 'self' blob: data:;
  font-src 'self';
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  frame-ancestors 'none';
  upgrade-insecure-requests;
`
module.exports= {
asyncheaders() {
return [
   {
    source:'/(.*)',
    headers: [
     {
      key:'Content-Security-Policy',
      value:cspHeader.replace(/\n/g,''),
     },
    ],
   },
  ]
 },
}
```

## Version History
We recommend using `v13.4.20+` of Next.js to properly handle and apply nonces.
