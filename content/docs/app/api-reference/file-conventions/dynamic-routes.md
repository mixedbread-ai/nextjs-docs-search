---
title: "Dynamic Route Segments"
path: "App / Api Reference / File Conventions / Dynamic Routes"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes
content_length: 3658
---

# Dynamic Route Segments
When you don't know the exact route segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time.
## Convention
A Dynamic Segment can be created by wrapping a folder's name in square brackets: `[folderName]`. For example, a blog could include the following route `app/blog/[slug]/page.js` where `[slug]` is the Dynamic Segment for blog posts.
app/blog/[slug]/page.tsx
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
return <div>My Post: {slug}</div>
}
```

Dynamic Segments are passed as the `params` prop to `layout`, `page`, `route`, and `generateMetadata` functions.
Route| Example URL| `params`  
---|---|---  
`app/blog/[slug]/page.js`| `/blog/a`| `{ slug: 'a' }`  
`app/blog/[slug]/page.js`| `/blog/b`| `{ slug: 'b' }`  
`app/blog/[slug]/page.js`| `/blog/c`| `{ slug: 'c' }`  
### Catch-all Segments
Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...folderName]`.
For example, `app/shop/[...slug]/page.js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.
Route| Example URL| `params`  
---|---|---  
`app/shop/[...slug]/page.js`| `/shop/a`| `{ slug: ['a'] }`  
`app/shop/[...slug]/page.js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`app/shop/[...slug]/page.js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
### Optional Catch-all Segments
Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...folderName]]`.
For example, `app/shop/[[...slug]]/page.js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.
The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).
Route| Example URL| `params`  
---|---|---  
`app/shop/[[...slug]]/page.js`| `/shop`| `{ slug: undefined }`  
`app/shop/[[...slug]]/page.js`| `/shop/a`| `{ slug: ['a'] }`  
`app/shop/[[...slug]]/page.js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`app/shop/[[...slug]]/page.js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
### TypeScript
When using TypeScript, you can add types for `params` depending on your configured route segment.
Route| `params` Type Definition  
---|---  
`app/blog/[slug]/page.js`| `{ slug: string }`  
`app/shop/[...slug]/page.js`| `{ slug: string[] }`  
`app/shop/[[...slug]]/page.js`| `{ slug?: string[] }`  
`app/[categoryId]/[itemId]/page.js`| `{ categoryId: string, itemId: string }`  
## Behavior
  * Since the `params` prop is a promise. You must use `async`/`await` or React's use function to access the values. 
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


## Examples
### With `generateStaticParams`
The `generateStaticParams` function can be used to statically generate routes at build time instead of on-demand at request time.
app/blog/[slug]/page.tsx
```
exportasyncfunctiongenerateStaticParams() {
constposts=awaitfetch(' =>res.json())
returnposts.map((post) => ({
  slug:post.slug,
 }))
}
```

When using `fetch` inside the `generateStaticParams` function, the requests are automatically deduplicated. This avoids multiple network calls for the same data Layouts, Pages, and other `generateStaticParams` functions, speeding up build time.
