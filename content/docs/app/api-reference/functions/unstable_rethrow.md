---
title: Unstable_rethrow
path: "App / Api Reference / Functions / Unstable_Rethrow"
source_url: https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow
content_length: 2300
---

# unstable_rethrow
This feature is currently unstable and subject to change, it's not recommended for production. Try it out and share your feedback on .
`unstable_rethrow` can be used to avoid catching internal errors thrown by Next.js when attempting to handle errors thrown in your application code.
For example, calling the `notFound` function will throw an internal Next.js error and render the `not-found.js` component. However, if used inside a `try/catch` block, the error will be caught, preventing `not-found.js` from rendering:
@/app/ui/component.tsx
```
import { notFound } from'next/navigation'
exportdefaultasyncfunctionPage() {
try {
constpost=awaitfetch(' => {
if (res.status ===404) notFound()
if (!res.ok) thrownewError(res.statusText)
returnres.json()
  })
 } catch (err) {
console.error(err)
 }
}
```

You can use `unstable_rethrow` API to re-throw the internal error and continue with the expected behavior:
@/app/ui/component.tsx
```
import { notFound, unstable_rethrow } from'next/navigation'
exportdefaultasyncfunctionPage() {
try {
constpost=awaitfetch(' => {
if (res.status ===404) notFound()
if (!res.ok) thrownewError(res.statusText)
returnres.json()
  })
 } catch (err) {
unstable_rethrow(err)
console.error(err)
 }
}
```

The following Next.js APIs rely on throwing an error which should be rethrown and handled by Next.js itself:
  * `notFound()`
  * `redirect()`
  * `permanentRedirect()`


If a route segment is marked to throw an error unless it's static, a Dynamic API call will also throw an error that should similarly not be caught by the developer. Note that Partial Prerendering (PPR) affects this behavior as well. These APIs are:
  * `cookies`
  * `headers`
  * `searchParams`
  * `fetch(..., { cache: 'no-store' })`
  * `fetch(..., { next: { revalidate: 0 } })`


> **Good to know** :
>   * This method should be called at the top of the catch block, passing the error object as its only argument. It can also be used within a `.catch` handler of a promise.
>   * If you ensure that your calls to APIs that throw are not wrapped in a try/catch then you don't need to use `unstable_rethrow`
>   * Any resource cleanup (like clearing intervals, timers, etc) would have to either happen prior to the call to `unstable_rethrow` or within a `finally` block.
>
