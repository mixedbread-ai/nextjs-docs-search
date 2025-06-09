---
title: ImageResponse
path: "App / Api Reference / Functions / Image Response"
source_url: https://nextjs.org/docs/app/api-reference/functions/image-response
content_length: 4611
---

# ImageResponse
The `ImageResponse` constructor allows you to generate dynamic images using JSX and CSS. This is useful for generating social media images such as Open Graph images, Twitter cards, and more.
## Reference
### Parameters
The following parameters are available for `ImageResponse`:
```
import { ImageResponse } from'next/og'
newImageResponse(
 element: ReactElement,
 options: {
  width?: number =1200
  height?: number =630
  emoji?:'twemoji'|'blobmoji'|'noto'|'openmoji'='twemoji',
  fonts?: {
   name: string,
   data: ArrayBuffer,
   weight: number,
   style:'normal'|'italic'
  }[]
  debug?: boolean =false
// Options that will be passed to the HTTP response
  status?: number =200
  statusText?: string
  headers?: Record<string, string>
 },
)
```

> Examples are available in the .
### Supported HTML and CSS features
`ImageResponse` supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images.
Please refer to for a list of supported HTML and CSS features.
## Behavior
  * `ImageResponse` uses , , and Resvg to convert HTML and CSS into PNG.
  * Only flexbox and a subset of CSS properties are supported. Advanced layouts (e.g. `display: grid`) will not work.
  * Maximum bundle size of `500KB`. The bundle size includes your JSX, CSS, fonts, images, and any other assets. If you exceed the limit, consider reducing the size of any assets or fetching at runtime.
  * Only `ttf`, `otf`, and `woff` font formats are supported. To maximize the font parsing speed, `ttf` or `otf` are preferred over `woff`.


## Examples
### Route Handlers
`ImageResponse` can be used in Route Handlers to generate images dynamically at request time.
app/api/route.js
```
import { ImageResponse } from'next/og'
exportasyncfunctionGET() {
try {
returnnewImageResponse(
   (
    <div
style={{
      height:'100%',
      width:'100%',
      display:'flex',
      flexDirection:'column',
      alignItems:'center',
      justifyContent:'center',
      backgroundColor:'white',
      padding:'40px',
     }}
    >
     <div
style={{
       fontSize:60,
       fontWeight:'bold',
       color:'black',
       textAlign:'center',
      }}
     >
      Welcome to My Site
     </div>
     <div
style={{
       fontSize:30,
       color:'#666',
       marginTop:'20px',
      }}
     >
      Generated with Next.js ImageResponse
     </div>
    </div>
   ),
   {
    width:1200,
    height:630,
   }
  )
 } catch (e) {
console.log(`${e.message}`)
returnnewResponse(`Failed to generate the image`, {
   status:500,
  })
 }
}
```

### File-based Metadata
You can use `ImageResponse` in a `opengraph-image.tsx` file to generate Open Graph images at build time or dynamically at request time.
app/opengraph-image.tsx
```
import { ImageResponse } from'next/og'
// Image metadata
exportconstalt='My site'
exportconstsize= {
 width:1200,
 height:630,
}
exportconstcontentType='image/png'
// Image generation
exportdefaultasyncfunctionImage() {
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
    My site
   </div>
  ),
// ImageResponse options
  {
// For convenience, we can re-use the exported opengraph-image
// size config to also set the ImageResponse's width and height.
...size,
  }
 )
}
```

### Custom fonts
You can use custom fonts in your `ImageResponse` by providing a `fonts` array in the options.
app/opengraph-image.tsx
```
import { ImageResponse } from'next/og'
import { readFile } from'node:fs/promises'
import { join } from'node:path'
// Image metadata
exportconstalt='My site'
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
// ...
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

## Version History
Version| Changes  
---|---  
`v14.0.0`| `ImageResponse` moved from `next/server` to `next/og`  
`v13.3.0`| `ImageResponse` can be imported from `next/server`.  
`v13.0.0`| `ImageResponse` introduced via `@vercel/og` package.
