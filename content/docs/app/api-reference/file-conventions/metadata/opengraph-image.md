---
title: "Opengraph-image and twitter-image"
path: "App / Api Reference / File Conventions / Metadata / Opengraph Image"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image
content_length: 8394
---

# opengraph-image and twitter-image
The `opengraph-image` and `twitter-image` file conventions allow you to set Open Graph and Twitter images for a route segment.
They are useful for setting the images that appear on social networks and messaging apps when a user shares a link to your site.
There are two ways to set Open Graph and Twitter images:
  * Using image files (.jpg, .png, .gif)
  * Using code to generate images (.js, .ts, .tsx)


## Image files (.jpg, .png, .gif)
Use an image file to set a route segment's shared image by placing an `opengraph-image` or `twitter-image` image file in the segment.
Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.
File convention| Supported file types  
---|---  
`opengraph-image`| `.jpg`, `.jpeg`, `.png`, `.gif`  
`twitter-image`| `.jpg`, `.jpeg`, `.png`, `.gif`  
`opengraph-image.alt`| `.txt`  
`twitter-image.alt`| `.txt`  
> **Good to know** :
> The `twitter-image` file size must not exceed , and the `opengraph-image` file size must not exceed . If the image file size exceeds these limits, the build will fail.
### `opengraph-image`
Add an `opengraph-image.(jpg|jpeg|png|gif)` image file to any route segment.
<head> output
```
<metaproperty="og:image"content="<generated>" />
<metaproperty="og:image:type"content="<generated>" />
<metaproperty="og:image:width"content="<generated>" />
<metaproperty="og:image:height"content="<generated>" />
```

### `twitter-image`
Add a `twitter-image.(jpg|jpeg|png|gif)` image file to any route segment.
<head> output
```
<metaname="twitter:image"content="<generated>" />
<metaname="twitter:image:type"content="<generated>" />
<metaname="twitter:image:width"content="<generated>" />
<metaname="twitter:image:height"content="<generated>" />
```

### `opengraph-image.alt.txt`
Add an accompanying `opengraph-image.alt.txt` file in the same route segment as the `opengraph-image.(jpg|jpeg|png|gif)` image it's alt text.
opengraph-image.alt.txt
```
About Acme
```

<head> output
```
<metaproperty="og:image:alt"content="About Acme" />
```

### `twitter-image.alt.txt`
Add an accompanying `twitter-image.alt.txt` file in the same route segment as the `twitter-image.(jpg|jpeg|png|gif)` image it's alt text.
twitter-image.alt.txt
```
About Acme
```

<head> output
```
<metaproperty="twitter:image:alt"content="About Acme" />
```

## Generate images using code (.js, .ts, .tsx)
In addition to using literal image files, you can programmatically **generate** images using code.
Generate a route segment's shared image by creating an `opengraph-image` or `twitter-image` route that default exports a function.
File convention| Supported file types  
---|---  
`opengraph-image`| `.js`, `.ts`, `.tsx`  
`twitter-image`| `.js`, `.ts`, `.tsx`  
> **Good to know** :
>   * By default, generated images are **statically optimized** (generated at build time and cached) unless they use Dynamic APIs or uncached data.
>   * You can generate multiple Images in the same file using `generateImageMetadata`.
>   * `opengraph-image.js` and `twitter-image.js` are special Route Handlers that is cached by default unless it uses a Dynamic API or dynamic config option.
> 

The easiest way to generate an image is to use the ImageResponse API from `next/og`.
app/about/opengraph-image.tsx
```
import { ImageResponse } from'next/og'
import { readFile } from'node:fs/promises'
import { join } from'node:path'
// Image metadata
exportconstalt='About Acme'
exportconstsize= {
 width:1200,
 height:630,
}
exportconstcontentType='image/png'
// Image generation
exportdefaultasyncfunctionImage() {
// Font loading, process.cwd() is Next.js project directory
constinterSemiBold=awaitreadFile(
join(process.cwd(),'assets/Inter-SemiBold.ttf')
 )
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
    About Acme
   </div>
  ),
// ImageResponse options
  {
// For convenience, we can re-use the exported opengraph-image
// size config to also set the ImageResponse's width and height.
...size,
   fonts: [
    {
     name:'Inter',
     data: interSemiBold,
     style:'normal',
     weight:400,
    },
   ],
  }
 )
}
```

<head> output
```
<metaproperty="og:image"content="<generated>" />
<metaproperty="og:image:alt"content="About Acme" />
<metaproperty="og:image:type"content="image/png" />
<metaproperty="og:image:width"content="1200" />
<metaproperty="og:image:height"content="630" />
```

### Props
The default export function receives the following props:
#### `params` (optional)
An object containing the dynamic route parameters object from the root segment down to the segment `opengraph-image` or `twitter-image` is colocated in.
app/shop/[slug]/opengraph-image.tsx
```
exportdefaultfunctionImage({ params }: { params: { slug:string } }) {
// ...
}
```

Route| URL| `params`  
---|---|---  
`app/shop/opengraph-image.js`| `/shop`| `undefined`  
`app/shop/[slug]/opengraph-image.js`| `/shop/1`| `{ slug: '1' }`  
`app/shop/[tag]/[item]/opengraph-image.js`| `/shop/1/2`| `{ tag: '1', item: '2' }`  
### Returns
The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.
> **Good to know** : `ImageResponse` satisfies this return type.
### Config exports
You can optionally configure the image's metadata by exporting `alt`, `size`, and `contentType` variables from `opengraph-image` or `twitter-image` route.
Option| Type  
---|---  
`alt`| `string`  
`size`| `{ width: number; height: number }`  
`contentType`| `string` -   
#### `alt`
opengraph-image.tsx | twitter-image.tsx
```
exportconstalt='My images alt text'
exportdefaultfunctionImage() {}
```

<head> output
```
<metaproperty="og:image:alt"content="My images alt text" />
```

#### `size`
opengraph-image.tsx | twitter-image.tsx
```
exportconstsize= { width:1200, height:630 }
exportdefaultfunctionImage() {}
```

<head> output
```
<metaproperty="og:image:width"content="1200" />
<metaproperty="og:image:height"content="630" />
```

#### `contentType`
opengraph-image.tsx | twitter-image.tsx
```
exportconstcontentType='image/png'
exportdefaultfunctionImage() {}
```

<head> output
```
<metaproperty="og:image:type"content="image/png" />
```

#### Route Segment Config
`opengraph-image` and `twitter-image` are specialized Route Handlers that can use the same route segment configuration options as Pages and Layouts.
### Examples
#### Using external data
This example uses the `params` object and external data to generate the image.
> **Good to know** : By default, this generated image will be statically optimized. You can configure the individual `fetch` `options` or route segments options to change this behavior.
app/posts/[slug]/opengraph-image.tsx
```
import { ImageResponse } from'next/og'
exportconstalt='About Acme'
exportconstsize= {
 width:1200,
 height:630,
}
exportconstcontentType='image/png'
exportdefaultasyncfunctionImage({ params }: { params: { slug:string } }) {
constpost=awaitfetch(`{params.slug}`).then((res) =>
res.json()
 )
returnnewImageResponse(
  (
   <div
style={{
     fontSize:48,
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
  ),
  {
...size,
  }
 )
}
```

#### Using Node.js runtime with local assets
This example uses the Node.js runtime to fetch a local image on the file system and passes it as an `ArrayBuffer` to the `src` attribute of an `<img>` element. The local asset should be placed relative to the root of your project, rather than the location of the example source file.
app/opengraph-image.tsx
```
import { ImageResponse } from'next/og'
import { join } from'node:path'
import { readFile } from'node:fs/promises'
exportdefaultasyncfunctionImage() {
constlogoData=awaitreadFile(join(process.cwd(),'logo.png'))
constlogoSrc=Uint8Array.from(logoData).buffer
returnnewImageResponse(
  (
   <div
style={{
     display:'flex',
     alignItems:'center',
     justifyContent:'center',
    }}
   >
    <imgsrc={logoSrc} height="100" />
   </div>
  )
 )
}
```

## Version History
Version| Changes  
---|---  
`v13.3.0`| `opengraph-image` and `twitter-image` introduced.
