---
title: "How to implement Incremental Static Regeneration (ISR)"
path: "App / Guides / Incremental Static Regeneration"
source_url: https://nextjs.org/docs/app/guides/incremental-static-regeneration
content_length: 7335
---

# How to implement Incremental Static Regeneration (ISR)
Examples
Incremental Static Regeneration (ISR) enables you to:
  * Update static content without rebuilding the entire site
  * Reduce server load by serving prerendered, static pages for most requests
  * Ensure proper `cache-control` headers are automatically added to pages
  * Handle large amounts of content pages without long `next build` times


Here's a minimal example:
app/blog/[id]/page.tsx
```
interfacePost {
 id:string
 title:string
 content:string
}
// Next.js will invalidate the cache when a
// request comes in, at most once every 60 seconds.
exportconstrevalidate=60
// We'll prerender only the params from `generateStaticParams` at build time.
// If a request comes in for a path that hasn't been generated,
// Next.js will server-render the page on-demand.
exportconstdynamicParams=true// or false, to 404 on unknown paths
exportasyncfunctiongenerateStaticParams() {
constposts:Post[] =awaitfetch(' =>
res.json()
 )
returnposts.map((post) => ({
  id:String(post.id),
 }))
}
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
constpost:Post=awaitfetch(`{id}`).then(
  (res) =>res.json()
 )
return (
  <main>
   <h1>{post.title}</h1>
   <p>{post.content}</p>
  </main>
 )
}
```

Here's how this example works:
  1. During `next build`, all known blog posts are generated (there are 25 in this example)
  2. All requests made to these pages (e.g. `/blog/1`) are cached and instantaneous
  3. After 60 seconds has passed, the next request will still show the cached (stale) page
  4. The cache is invalidated and a new version of the page begins generating in the background
  5. Once generated successfully, Next.js will display and cache the updated page
  6. If `/blog/26` is requested, Next.js will generate and cache this page on-demand


## Reference
### Route segment config
  * `revalidate`
  * `dynamicParams`


### Functions
  * `revalidatePath`
  * `revalidateTag`


## Examples
### Time-based revalidation
This fetches and displays a list of blog posts on `/blog`. After an hour, the cache for this page is invalidated on the next visit to the page. Then, in the background, a new version of the page is generated with the latest blog posts.
app/blog/page.tsx
```
interfacePost {
 id:string
 title:string
 content:string
}
exportconstrevalidate=3600// invalidate every hour
exportdefaultasyncfunctionPage() {
constdata=awaitfetch('
constposts:Post[] =awaitdata.json()
return (
  <main>
   <h1>Blog Posts</h1>
   <ul>
    {posts.map((post) => (
     <likey={post.id}>{post.title}</li>
    ))}
   </ul>
  </main>
 )
}
```

We recommend setting a high revalidation time. For instance, 1 hour instead of 1 second. If you need more precision, consider using on-demand revalidation. If you need real-time data, consider switching to dynamic rendering.
### On-demand revalidation with `revalidatePath`
For a more precise method of revalidation, invalidate pages on-demand with the `revalidatePath` function.
For example, this Server Action would get called after adding a new post. Regardless of how you retrieve your data in your Server Component, either using `fetch` or connecting to a database, this will clear the cache for the entire route and allow the Server Component to fetch fresh data.
app/actions.ts
```
'use server'
import { revalidatePath } from'next/cache'
exportasyncfunctioncreatePost() {
// Invalidate the /posts route in the cache
revalidatePath('/posts')
}
```

and .
### On-demand revalidation with `revalidateTag`
For most use cases, prefer revalidating entire paths. If you need more granular control, you can use the `revalidateTag` function. For example, you can tag individual `fetch` calls:
app/blog/page.tsx
```
exportdefaultasyncfunctionPage() {
constdata=awaitfetch(' {
  next: { tags: ['posts'] },
 })
constposts=awaitdata.json()
// ...
}
```

If you are using an ORM or connecting to a database, you can use `unstable_cache`:
app/blog/page.tsx
```
import { unstable_cache } from'next/cache'
import { db, posts } from'@/lib/db'
constgetCachedPosts=unstable_cache(
async () => {
returnawaitdb.select().from(posts)
 },
 ['posts'],
 { revalidate:3600, tags: ['posts'] }
)
exportdefaultasyncfunctionPage() {
constposts=getCachedPosts()
// ...
}
```

You can then use `revalidateTag` in a Server Actions or Route Handler:
app/actions.ts
```
'use server'
import { revalidateTag } from'next/cache'
exportasyncfunctioncreatePost() {
// Invalidate all data tagged with 'posts' in the cache
revalidateTag('posts')
}
```

### Handling uncaught exceptions
If an error is thrown while attempting to revalidate data, the last successfully generated data will continue to be served from the cache. On the next subsequent request, Next.js will retry revalidating the data. Learn more about error handling.
### Customizing the cache location
You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application. Learn more.
## Troubleshooting
### Debugging cached data in local development
If you are using the `fetch` API, you can add additional logging to understand which requests are cached or uncached. Learn more about the `logging` option.
next.config.js
```
module.exports= {
 logging: {
  fetches: {
   fullUrl:true,
  },
 },
}
```

### Verifying correct production behavior
To verify your pages are cached and revalidated correctly in production, you can test locally by running `next build` and then `next start` to run the production Next.js server.
This will allow you to test ISR behavior as it would work in a production environment. For further debugging, add the following environment variable to your `.env` file:
.env
```
NEXT_PRIVATE_DEBUG_CACHE=1
```

This will make the Next.js server console log ISR cache hits and misses. You can inspect the output to see which pages are generated during `next build`, as well as how pages are updated as paths are accessed on-demand.
## Caveats
  * ISR is only supported when using the Node.js runtime (default).
  * ISR is not supported when creating a Static Export.
  * If you have multiple `fetch` requests in a statically rendered route, and each has a different `revalidate` frequency, the lowest time will be used for ISR. However, those revalidate frequencies will still be respected by the Data Cache.
  * If any of the `fetch` requests used on a route have a `revalidate` time of `0`, or an explicit `no-store`, the route will be dynamically rendered.
  * Middleware won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Middleware will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.


## Platform Support
Deployment Option| Supported  
---|---  
Node.js server| Yes  
Docker container| Yes  
Static export| No  
Adapters| Platform-specific  
Learn how to configure ISR when self-hosting Next.js.
## Version history
Version| Changes  
---|---  
`v14.1.0`| Custom `cacheHandler` is stable.  
`v13.0.0`| App Router is introduced.  
`v12.2.0`| Pages Router: On-Demand ISR is stable  
`v12.0.0`| Pages Router: Bot-aware ISR fallback added.  
`v9.5.0`| Pages Router: Stable ISR introduced.
