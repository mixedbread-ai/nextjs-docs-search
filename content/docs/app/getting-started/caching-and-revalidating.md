---
title: "How to cache and revalidate data"
path: "App / Getting Started / Caching And Revalidating"
source_url: https://nextjs.org/docs/app/getting-started/caching-and-revalidating
content_length: 3834
---

# How to cache and revalidate data
Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster, without doing the work again. While revalidation allows you to update cache entries without having to rebuild your entire application.
Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through when and how to use them.
  * `fetch`
  * `unstable_cache`
  * `revalidatePath`
  * `revalidateTag`


## `fetch`
By default, `fetch` requests are not cached. You can cache individual requests by setting the `cache` option to `'force-cache'`.
app/page.tsx
```
exportdefaultasyncfunctionPage() {
constdata=awaitfetch(' { cache:'force-cache' })
}
```

> **Good to know** : Although `fetch` requests are not cached by default, Next.js will prerender routes that have `fetch` requests and cache the HTML. If you want to guarantee a route is dynamic, use the `connection` API.
To revalidate the data returned by a `fetch` request, you can use the `next.revalidate` option.
app/page.tsx
```
exportdefaultasyncfunctionPage() {
constdata=awaitfetch(' { next: { revalidate:3600 } })
}
```

This will revalidate the data after a specified amount of seconds.
See the `fetch` API reference to learn more.
## `unstable_cache`
`unstable_cache` allows you to cache the result of database queries and other async functions. To use it, wrap `unstable_cache` around the function. For example:
```
import { db } from'@/lib/db'
exportasyncfunctiongetUserById(id:string) {
return db
.select()
.from(users)
.where(eq(users.id, id))
.then((res) => res[0])
}
```

app/page.tsx
```
import { unstable_cache } from'next/cache'
import { getUserById } from'@/app/lib/data'
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ userId:string }>
}) {
const { userId } =await params
constgetCachedUser=unstable_cache(
async () => {
returngetUserById(userId)
  },
  [userId] // add the user ID to the cache key
 )
}
```

The function accepts a third optional object to define how the cache should be revalidated. It accepts:
  * `tags`: an array of tags used by Next.js to revalidate the cache.
  * `revalidate`: the number of seconds after cache should be revalidated.


app/page.tsx
```
constgetCachedUser=unstable_cache(
async () => {
returngetUserById(userId)
 },
 [userId],
 {
  tags: ['user'],
  revalidate:3600,
 }
)
```

See the `unstable_cache` API reference to learn more.
## `revalidateTag`
`revalidateTag` is used to revalidate a cache entries based on a tag and following an event. To use it with `fetch`, start by tagging the function with the `next.tags` option:
app/lib/data.ts
```
exportasyncfunctiongetUserById(id:string) {
constdata=awaitfetch(``, {
  next: {
   tags: ['user'],
  },
 })
}
```

Alternatively, you can mark an `unstable_cache` function with the `tags` option:
app/lib/data.ts
```
exportconstgetUserById=unstable_cache(
async (id:string) => {
returndb.query.users.findFirst({ where:eq(users.id, id) })
 },
 ['user'],// Needed if variables are not passed as parameters
 {
  tags: ['user'],
 }
)
```

Then, call `revalidateTag` in a Route Handler or Server Action:
app/lib/actions.ts
```
import { revalidateTag } from'next/cache'
exportasyncfunctionupdateUser(id:string) {
// Mutate data
revalidateTag('user')
}
```

You can reuse the same tag in multiple functions to revalidate them all at once.
See the `revalidateTag` API reference to learn more.
## `revalidatePath`
`revalidatePath` is used to revalidate a route and following an event. To use it, call it in a Route Handler or Server Action:
app/lib/actions.ts
```
import { revalidatePath } from'next/cache'
exportasyncfunctionupdateUser(id:string) {
// Mutate data
revalidatePath('/profile')
```

See the `revalidatePath` API reference to learn more.
