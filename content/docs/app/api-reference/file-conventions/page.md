---
title: Page.js
path: "App / Api Reference / File Conventions / Page"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/page
content_length: 4149
---

# page.js
The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:
app/blog/[slug]/page.tsx
```
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
return <h1>My Page</h1>
}
```

## Good to know
  * The `.js`, `.jsx`, or `.tsx` file extensions can be used for `page`.
  * A `page` is always the **leaf** of the route subtree.
  * A `page` file is required to make a route segment **publicly accessible**.
  * Pages are by default, but can be set to a .


## Reference
### Props
#### `params` (optional)
A promise that resolves to an object containing the dynamic route parameters from the root segment down to that page.
app/shop/[slug]/page.tsx
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
}
```

Example Route| URL| `params`  
---|---|---  
`app/shop/[slug]/page.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[category]/[item]/page.js`| `/shop/1/2`| `Promise<{ category: '1', item: '2' }>`  
`app/shop/[...slug]/page.js`| `/shop/1/2`| `Promise<{ slug: ['1', '2'] }>`  
  * Since the `params` prop is a promise. You must use `async/await` or React's function to access the values. 
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


#### `searchParams` (optional)
A promise that resolves to an object containing the of the current URL. For example:
app/shop/page.tsx
```
exportdefaultasyncfunctionPage({
 searchParams,
}: {
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
constfilters= (await searchParams).filters
}
```

Example URL| `searchParams`  
---|---  
`/shop?a=1`| `Promise<{ a: '1' }>`  
`/shop?a=1&b=2`| `Promise<{ a: '1', b: '2' }>`  
`/shop?a=1&a=2`| `Promise<{ a: ['1', '2'] }>`  
  * Since the `searchParams` prop is a promise. You must use `async/await` or React's function to access the values. 
    * In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `searchParams` is a **Dynamic API** whose values cannot be known ahead of time. Using it will opt the page into **dynamic rendering** at request time.
  * `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.


## Examples
### Displaying content based on `params`
Using dynamic route segments, you can display or fetch specific content for the page based on the `params` prop.
app/blog/[slug]/page.tsx
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
return <h1>Blog Post: {slug}</h1>
}
```

### Handling filtering with `searchParams`
You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.
app/shop/page.tsx
```
exportdefaultasyncfunctionPage({
 searchParams,
}: {
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
const { page='1',sort='asc',query='' } =await searchParams
return (
  <div>
   <h1>Product Listing</h1>
   <p>Search query: {query}</p>
   <p>Current page: {page}</p>
   <p>Sort order: {sort}</p>
  </div>
 )
}
```

### Reading `searchParams` and `params` in Client Components
To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's function to read the promise:
app/page.tsx
```
'use client'
import { use } from'react'
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
const { slug } =use(params)
const { query } =use(searchParams)
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0-RC`| `params` and `searchParams` are now promises. A codemod is available.  
`v13.0.0`| `page` introduced.
