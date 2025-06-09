---
title: "How to optimize images"
path: "App / Getting Started / Images"
source_url: https://nextjs.org/docs/app/getting-started/images
content_length: 3186
---

# How to optimize images
The Next.js `<Image>` component extends the HTML `<img>` element to provide:
  * **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP.
  * **Visual stability:** Preventing automatically when images are loading.
  * **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
  * **Asset flexibility:** Resizing images on-demand, even images stored on remote servers.


To start using `<Image>`, import it from `next/image` and render it within your component.
app/page.tsx
```
import Image from'next/image'
exportdefaultfunctionPage() {
return <Imagesrc=""alt="" />
}
```

The `src` property can be a local or remote image.
> **🎥 Watch:** Learn more about how to use `next/image` → .
## Local images
You can store static files, like images and fonts, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).
!Folder structure showing app and public folders!Folder structure showing app and public folders
app/page.tsx
```
import Image from'next/image'
exportdefaultfunctionPage() {
return (
  <Image
src="/profile.png"
alt="Picture of the author"
width={500}
height={500}
  />
 )
}
```

### Statically imported images
You can also import and use local image files. Next.js will automatically determine the intrinsic `width` and `height` of your image based on the imported file. These values are used to determine the image ratio and prevent while your image is loading.
app/page.tsx
```
import Image from'next/image'
import ProfileImage from'./profile.png'
exportdefaultfunctionPage() {
return (
  <Image
src={ProfileImage}
alt="Picture of the author"
// width={500} automatically provided
// height={500} automatically provided
// blurDataURL="data:..." automatically provided
// placeholder="blur" // Optional blur-up while loading
  />
 )
}
```

In this case, Next.js expects the `app/profile.png` file to be available.
## Remote images
To use a remote image, you can provide a URL string for the `src` property.
app/page.tsx
```
import Image from'next/image'
exportdefaultfunctionPage() {
return (
  <Image
src=""
alt="Picture of the author"
width={500}
height={500}
  />
 )
}
```

Since Next.js does not have access to remote files during the build process, you'll need to provide the `width`, `height` and optional `blurDataURL` props manually. The `width` and `height` are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in.
To safely allow images from remote servers, you need to define a list of supported URL patterns in `next.config.js`. Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:
next.config.ts
```
importtype { NextConfig } from'next'
constconfig:NextConfig= {
 images: {
  remotePatterns: [
   {
    protocol:'https',
    hostname:'s3.amazonaws.com',
    port:'',
    pathname:'/my-bucket/**',
    search:'',
   },
  ],
 },
}
exportdefault config
```
