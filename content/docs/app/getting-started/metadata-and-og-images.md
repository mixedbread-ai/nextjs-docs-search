---
title: "How to add metadata and create OG images"
path: "App / Getting Started / Metadata And Og Images"
source_url: https://nextjs.org/docs/app/getting-started/metadata-and-og-images
content_length: 6469
---

# How to add metadata and create OG images
The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:
  1. The static `metadata` object
  2. The dynamic `generateMetadata` function
  3. Special file conventions that can be used to add static or dynamically generated favicons and OG images.


With all the options above, Next.js will automatically generate the relevant `<head>` tags for your page, which can be inspected in the browser's developer tools.
## Default fields
There are two default `meta` tags that are always added even if a route doesn't define metadata:
  * The sets the character encoding for the website.
  * The sets the viewport width and scale for the website to adjust for different devices.


```
<metacharset="utf-8" />
<metaname="viewport"content="width=device-width, initial-scale=1" />
```

The other metadata fields can be defined with the `Metadata` object (for static metadata) or the `generateMetadata` function (for generated metadata).
## Static metadata
To define static metadata, export a `Metadata` object from a static `layout.js` or `page.js` file. For example, to add a title and description to the blog route:
app/blog/layout.tsx
```
importtype { Metadata } from'next'
exportconstmetadata:Metadata= {
 title:'My Blog',
 description:'...',
}
exportdefaultfunctionPage() {}
```

You can view a full list of available options, in the `generateMetadata` documentation.
## Generated metadata
You can use `generateMetadata` function to `fetch` metadata that depends on data. For example, to fetch the title and description for a specific blog post:
app/blog/[slug]/page.tsx
```
importtype { Metadata, ResolvingMetadata } from'next'
typeProps= {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}
exportasyncfunctiongenerateMetadata(
 { params, searchParams }:Props,
 parent:ResolvingMetadata
):Promise<Metadata> {
constslug= (await params).slug
// fetch post information
constpost=awaitfetch(`{slug}`).then((res) =>
res.json()
 )
return {
  title:post.title,
  description:post.description,
 }
}
exportdefaultfunctionPage({ params, searchParams }:Props) {}
```

Behind-the-scenes, Next.js will stream metadata separately from the UI and inject the metadata into the HTML as soon as it's resolved.
### Memoizing data requests
There may be cases where you need to fetch the **same** data for metadata and the page itself. To avoid duplicate requests, you can use React's to memoize the return value and only fetch the data once. For example, to fetch the blog post information for both the metadata and the page:
app/lib/data.ts
```
import { cache } from'react'
import { db } from'@/app/lib/db'
// getPost will be used twice, but execute only once
exportconstgetPost=cache(async (slug:string) => {
constres=awaitdb.query.posts.findFirst({ where:eq(posts.slug, slug) })
return res
})
```

app/blog/[slug]/page.tsx
```
import { getPost } from'@/app/lib/data'
exportasyncfunctiongenerateMetadata({
 params,
}: {
 params: { slug:string }
}) {
constpost=awaitgetPost(params.slug)
return {
  title:post.title,
  description:post.description,
 }
}
exportdefaultasyncfunctionPage({ params }: { params: { slug:string } }) {
constpost=awaitgetPost(params.slug)
return <div>{post.title}</div>
}
```

## File-based metadata
The following special files are available for metadata:
  * favicon.ico, apple-icon.jpg, and icon.jpg
  * opengraph-image.jpg and twitter-image.jpg
  * robots.txt
  * sitemap.xml


You can use these for static metadata, or you can programmatically generate these files with code.
## Favicons
Favicons are small icons that represent your site in bookmarks and search results. To add a favicon to your application, create a `favicon.ico` and add to the root of the app folder.
!Favicon Special File inside the App Folder with sibling layout and page files!Favicon Special File inside the App Folder with sibling layout and page files
> You can also programmatically generate favicons using code. See the favicon docs for more information.
## Static Open Graph images
Open Graph (OG) images are images that represent your site in social media. To add a static OG image to your application, create a `opengraph-image.png` file in the root of the app folder.
!OG image special file inside the App folder with sibling layout and page files!OG image special file inside the App folder with sibling layout and page files
You can also add OG images for specific routes by creating a `opengraph-image.png` deeper down the folder structure. For example, to create an OG image specific to the `/blog` route, add a `opengraph-image.jpg` file inside the `blog` folder.
!OG image special file inside the blog folder!OG image special file inside the blog folder
The more specific image will take precedence over any OG images above it in the folder structure.
> Other image formats such as `jpeg`, `png`, and `webp` are also supported. See the Open Graph Image docs for more information.
## Generated Open Graph images
The `ImageResponse` constructor allows you to generate dynamic images using JSX and CSS. This is useful for OG images that depend on data.
For example, to generate a unique OG image for each blog post, add a `opengraph-image.ts` file inside the `blog` folder, and import the `ImageResponse` constructor from `next/og`:
app/blog/[slug]/opengraph-image.ts
```
import { ImageResponse } from'next/og'
import { getPost } from'@/app/lib/data'
// Image metadata
exportconstsize= {
 width:1200,
 height:630,
}
exportconstcontentType='image/png'
// Image generation
exportdefaultasyncfunctionImage({ params }: { params: { slug:string } }) {
constpost=awaitgetPost(params.slug)
returnnewImageResponse(
  (
// ImageResponse JSX element
   <div
style={{
     fontSize:128,
     background:'white',
     width:'100%',
     height:'100%',
     display:'flex',
     alignItems:'center',
     justifyContent:'center',
    }}
   >
    {post.title}
   </div>
  )
 )
}
```

`ImageResponse` supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images. See the full list of supported CSS properties.
> **Good to know** :
>   * Examples are available in the .
>   * `ImageResponse` uses , , and `resvg` to convert HTML and CSS into PNG.
>   * Only flexbox and a subset of CSS properties are supported. Advanced layouts (e.g. `display: grid`) will not work.
>
