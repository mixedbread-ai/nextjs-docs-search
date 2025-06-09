---
title: UseSelectedLayoutSegment
path: "App / Api Reference / Functions / Use Selected Layout Segment"
source_url: https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment
content_length: 3223
---

# useSelectedLayoutSegment
`useSelectedLayoutSegment` is a **Client Component** hook that lets you read the active route segment **one level below** the Layout it is called from.
It is useful for navigation UI, such as tabs inside a parent layout that change style depending on the active child segment.
app/example-client-component.tsx
```
'use client'
import { useSelectedLayoutSegment } from'next/navigation'
exportdefaultfunctionExampleClientComponent() {
constsegment=useSelectedLayoutSegment()
return <p>Active segment: {segment}</p>
}
```

> **Good to know** :
>   * Since `useSelectedLayoutSegment` is a Client Component hook, and Layouts are Server Components by default, `useSelectedLayoutSegment` is usually called via a Client Component that is imported into a Layout.
>   * `useSelectedLayoutSegment` only returns the segment one level down. To return all active segments, see `useSelectedLayoutSegments`
> 

## Parameters
```
constsegment=useSelectedLayoutSegment(parallelRoutesKey?: string)
```

`useSelectedLayoutSegment` _optionally_ accepts a `parallelRoutesKey`, which allows you to read the active route segment within that slot.
## Returns
`useSelectedLayoutSegment` returns a string of the active segment or `null` if one doesn't exist.
For example, given the Layouts and URLs below, the returned segment would be:
Layout| Visited URL| Returned Segment  
---|---|---  
`app/layout.js`| `/`| `null`  
`app/layout.js`| `/dashboard`| `'dashboard'`  
`app/dashboard/layout.js`| `/dashboard`| `null`  
`app/dashboard/layout.js`| `/dashboard/settings`| `'settings'`  
`app/dashboard/layout.js`| `/dashboard/analytics`| `'analytics'`  
`app/dashboard/layout.js`| `/dashboard/analytics/monthly`| `'analytics'`  
## Examples
### Creating an active link component
You can use `useSelectedLayoutSegment` to create an active link component that changes style depending on the active segment. For example, a featured posts list in the sidebar of a blog:
app/blog/blog-nav-link.tsx
```
'use client'
import Link from'next/link'
import { useSelectedLayoutSegment } from'next/navigation'
// This *client* component will be imported into a blog layout
exportdefaultfunctionBlogNavLink({
 slug,
 children,
}: {
 slug:string
 children:React.ReactNode
}) {
// Navigating to `/blog/hello-world` will return 'hello-world'
// for the selected layout segment
constsegment=useSelectedLayoutSegment()
constisActive= slug === segment
return (
  <Link
href={`/blog/${slug}`}
// Change style depending on whether the link is active
style={{ fontWeight: isActive ?'bold':'normal' }}
  >
   {children}
  </Link>
 )
}
```

app/blog/layout.tsx
```
// Import the Client Component into a parent Layout (Server Component)
import { BlogNavLink } from'./blog-nav-link'
import getFeaturedPosts from'./get-featured-posts'
exportdefaultasyncfunctionLayout({
 children,
}: {
 children:React.ReactNode
}) {
constfeaturedPosts=awaitgetFeaturedPosts()
return (
  <div>
   {featuredPosts.map((post) => (
    <divkey={post.id}>
     <BlogNavLinkslug={post.slug}>{post.title}</BlogNavLink>
    </div>
   ))}
   <div>{children}</div>
  </div>
 )
}
```

## Version History
Version| Changes  
---|---  
`v13.0.0`| `useSelectedLayoutSegment` introduced.
