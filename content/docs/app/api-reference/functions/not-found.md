---
title: NotFound
path: "App / Api Reference / Functions / Not Found"
source_url: https://nextjs.org/docs/app/api-reference/functions/not-found
content_length: 969
---

# notFound
The `notFound` function allows you to render the `not-found file` within a route segment as well as inject a `<meta name="robots" content="noindex" />` tag.
## `notFound()`
Invoking the `notFound()` function throws a `NEXT_HTTP_ERROR_FALLBACK;404` error and terminates rendering of the route segment in which it was thrown. Specifying a **not-found** file allows you to gracefully handle such errors by rendering a Not Found UI within the segment.
app/user/[id]/page.js
```
import { notFound } from'next/navigation'
asyncfunctionfetchUser(id) {
constres=awaitfetch('
if (!res.ok) returnundefined
returnres.json()
}
exportdefaultasyncfunctionProfile({ params }) {
const { id } =await params
constuser=awaitfetchUser(id)
if (!user) {
notFound()
 }
// ...
}
```

> **Good to know** : `notFound()` does not require you to use `return notFound()` due to using the TypeScript type.
## Version History
Version| Changes  
---|---  
`v13.0.0`| `notFound` introduced.
