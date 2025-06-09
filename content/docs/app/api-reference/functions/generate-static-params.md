---
title: GenerateStaticParams
path: "App / Api Reference / Functions / Generate Static Params"
source_url: https://nextjs.org/docs/app/api-reference/functions/generate-static-params
content_length: 8486
---

# generateStaticParams
The `generateStaticParams` function can be used in combination with dynamic route segments to **statically generate** routes at build time instead of on-demand at request time.
app/blog/[slug]/page.tsx
```
// Return a list of `params` to populate the [slug] dynamic segment
exportasyncfunctiongenerateStaticParams() {
constposts=awaitfetch(' =>res.json())
returnposts.map((post) => ({
  slug:post.slug,
 }))
}
// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
// ...
}
```

> **Good to know** :
>   * You can use the `dynamicParams` segment config option to control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
>   * You must return an empty array from `generateStaticParams` or utilize `export const dynamic = 'force-static'` in order to revalidate (ISR) paths at runtime.
>   * During `next dev`, `generateStaticParams` will be called when you navigate to a route.
>   * During `next build`, `generateStaticParams` runs before the corresponding Layouts or Pages are generated.
>   * During revalidation (ISR), `generateStaticParams` will not be called again.
>   * `generateStaticParams` replaces the `getStaticPaths` function in the Pages Router.
> 

## Parameters
`options.params` (optional)
If multiple dynamic segments in a route use `generateStaticParams`, the child `generateStaticParams` function is executed once for each set of `params` the parent generates.
The `params` object contains the populated `params` from the parent `generateStaticParams`, which can be used to generate the `params` in a child segment.
## Returns
`generateStaticParams` should return an array of objects where each object represents the populated dynamic segments of a single route.
  * Each property in the object is a dynamic segment to be filled in for the route.
  * The properties name is the segment's name, and the properties value is what that segment should be filled in with.


Example Route| `generateStaticParams` Return Type  
---|---  
`/product/[id]`| `{ id: string }[]`  
`/products/[category]/[product]`| `{ category: string, product: string }[]`  
`/products/[...slug]`| `{ slug: string[] }[]`  
## Single Dynamic Segment
app/product/[id]/page.tsx
```
exportfunctiongenerateStaticParams() {
return [{ id:'1' }, { id:'2' }, { id:'3' }]
}
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/1
// - /product/2
// - /product/3
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
// ...
}
```

## Multiple Dynamic Segments
app/products/[category]/[product]/page.tsx
```
exportfunctiongenerateStaticParams() {
return [
  { category:'a', product:'1' },
  { category:'b', product:'2' },
  { category:'c', product:'3' },
 ]
}
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ category:string; product:string }>
}) {
const { category,product } =await params
// ...
}
```

## Catch-all Dynamic Segment
app/product/[...slug]/page.tsx
```
exportfunctiongenerateStaticParams() {
return [{ slug: ['a','1'] }, { slug: ['b','2'] }, { slug: ['c','3'] }]
}
// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/a/1
// - /product/b/2
// - /product/c/3
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string[] }>
}) {
const { slug } =await params
// ...
}
```

## Examples
### Static Rendering
#### All paths at build time
To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:
app/blog/[slug]/page.tsx
```
exportasyncfunctiongenerateStaticParams() {
constposts=awaitfetch(' =>res.json())
returnposts.map((post) => ({
  slug:post.slug,
 }))
}
```

#### Subset of paths at build time
To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:
app/blog/[slug]/page.tsx
```
exportasyncfunctiongenerateStaticParams() {
constposts=awaitfetch(' =>res.json())
// Render the first 10 posts at build time
returnposts.slice(0,10).map((post) => ({
  slug:post.slug,
 }))
}
```

Then, by using the `dynamicParams` segment config option, you can control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
app/blog/[slug]/page.tsx
```
// All posts besides the top 10 will be a 404
exportconstdynamicParams=false
exportasyncfunctiongenerateStaticParams() {
constposts=awaitfetch(' =>res.json())
consttopPosts=posts.slice(0,10)
returntopPosts.map((post) => ({
  slug:post.slug,
 }))
}
```

#### All paths at runtime
To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize `export const dynamic = 'force-static'`:
app/blog/[slug]/page.js
```
exportasyncfunctiongenerateStaticParams() {
return []
}
```

> **Good to know:** You must always return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.
app/changelog/[slug]/page.js
```
exportconstdynamic='force-static'
```

### Disable rendering for unspecified paths
To prevent unspecified paths from being statically rendered at runtime, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and unspecified routes will 404 or match (in the case of catch-all routes).
### Multiple Dynamic Segments in a Route
You can generate params for dynamic segments above the current layout or page, but **not below**. For example, given the `app/products/[category]/[product]` route:
  * `app/products/[category]/[product]/page.js` can generate params for **both** `[category]` and `[product]`.
  * `app/products/[category]/layout.js` can **only** generate params for `[category]`.


There are two approaches to generating params for a route with multiple dynamic segments:
#### Generate params from the bottom up
Generate multiple dynamic segments from the child route segment.
app/products/[category]/[product]/page.tsx
```
// Generate segments for both [category] and [product]
exportasyncfunctiongenerateStaticParams() {
constproducts=awaitfetch(' =>res.json())
returnproducts.map((product) => ({
  category:product.category.slug,
  product:product.id,
 }))
}
exportdefaultfunctionPage({
 params,
}: {
 params:Promise<{ category:string; product:string }>
}) {
// ...
}
```

#### Generate params from the top down
Generate the parent segments first and use the result to generate the child segments.
app/products/[category]/layout.tsx
```
// Generate segments for [category]
exportasyncfunctiongenerateStaticParams() {
constproducts=awaitfetch(' =>res.json())
returnproducts.map((product) => ({
  category:product.category.slug,
 }))
}
exportdefaultfunctionLayout({
 params,
}: {
 params:Promise<{ category:string }>
}) {
// ...
}
```

A child route segment's `generateStaticParams` function is executed once for each segment a parent `generateStaticParams` generates.
The child `generateStaticParams` function can use the `params` returned from the parent `generateStaticParams` function to dynamically generate its own segments.
app/products/[category]/[product]/page.tsx
```
// Generate segments for [product] using the `params` passed from
// the parent segment's `generateStaticParams` function
exportasyncfunctiongenerateStaticParams({
 params: { category },
}: {
 params: { category:string }
}) {
constproducts=awaitfetch(
`{category}`
 ).then((res) =>res.json())
returnproducts.map((product) => ({
  product:product.id,
 }))
}
exportdefaultfunctionPage({
 params,
}: {
 params:Promise<{ category:string; product:string }>
}) {
// ...
}
```

> **Good to know** : `fetch` requests are automatically memoized for the same data across all `generate`-prefixed functions, Layouts, Pages, and Server Components. React `cache` can be used if `fetch` is unavailable.
## Version History
Version| Changes  
---|---  
`v13.0.0`| `generateStaticParams` introduced.
