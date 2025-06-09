---
title: Image
path: "App / Api Reference / Components / Image"
source_url: https://nextjs.org/docs/app/api-reference/components/image
content_length: 32315
---

# Image
The Next.js Image component extends the HTML `<img>` element for automatic image optimization.
app/page.js
```
import Image from'next/image'
exportdefaultfunctionPage() {
return (
  <Image
src="/profile.png"
width={500}
height={500}
alt="Picture of the author"
  />
 )
}
```

## Reference
### Props
The following props are available:
Prop| Example| Type| Status  
---|---|---|---  
`src`| `src="/profile.png"`| String| Required  
`alt`| `alt="Picture of the author"`| String| Required  
`width`| `width={500}`| Integer (px)| -  
`height`| `height={500}`| Integer (px)| -  
`fill`| `fill={true}`| Boolean| -  
`loader`| `loader={imageLoader}`| Function| -  
`sizes`| `sizes="(max-width: 768px) 100vw, 33vw"`| String| -  
`quality`| `quality={80}`| Integer (1-100)| -  
`priority`| `priority={true}`| Boolean| -  
`placeholder`| `placeholder="blur"`| String| -  
`style`| `style={{objectFit: "contain"}}`| Object| -  
`onLoadingComplete`| `onLoadingComplete={img => done())}`| Function| Deprecated  
`onLoad`| `onLoad={event => done())}`| Function| -  
`onError`| `onError(event => fail()}`| Function| -  
`loading`| `loading="lazy"`| String| -  
`blurDataURL`| `blurDataURL="data:image/jpeg..."`| String| -  
`overrideSrc`| `overrideSrc="/seo.png"`| String| -  
#### `src`
The source of the image. Can be one of the following:
An internal path string.
```
<Imagesrc="/profile.png" />
```

An absolute external URL (must be configured with remotePatterns).
```
<Imagesrc="" />
```

A static import.
```
import profile from'./profile.png'
exportdefaultfunctionPage() {
return <Imagesrc={profile} />
}
```

#### `alt`
The `alt` property is used to describe the image for screen readers and search engines. It is also the fallback text if images have been disabled or an error occurs while loading the image.
It should contain text that could replace the image . It is not meant to supplement the image and should not repeat information that is already provided in the captions above or below the image.
If the image is or , the `alt` property should be an empty string (`alt=""`).
> Learn more about .
#### `width` and `height`
The `width` and `height` properties represent the image size in pixels. This property is used to infer the correct **aspect ratio** used by browsers to reserve space for the image and avoid layout shift during loading. It does not determine the _rendered size_ of the image, which is controlled by CSS.
```
<Imagesrc="/profile.png"width={500} height={500} />
```

You **must** set both `width` and `height` properties unless:
  * The image is statically imported
  * The image has the `fill` property


If the height and width are unknown, we recommend using the `fill` property.
#### `fill`
A boolean that causes the image to expand to the size of the parent element.
```
<Imagesrc="/profile.png"fill={true} />
```

**Positioning** :
  * The parent element **must** assign `position: "relative"`, `"fixed"`, `"absolute"`.
  * By default, the `<img>` element uses `position: "absolute"`.


**Object Fit** :
If no styles are applied to the image, the image will stretch to fit the container. You can use `objectFit` to control cropping and scaling.
  * `"contain"`: The image will be scaled down to fit the container and preserve aspect ratio.
  * `"cover"`: The image will fill the container and be cropped.


> Learn more about and .
#### `loader`
A custom function used to generate the image URL. The function receives the following parameters, and returns a URL string for the image:
  * `src`
  * `width`
  * `quality`


```
'use client'
import Image from'next/image'
constimageLoader= ({ src, width, quality }) => {
return`{src}?w=${width}&q=${quality ||75}`
}
exportdefaultfunctionPage() {
return (
  <Image
loader={imageLoader}
src="me.png"
alt="Picture of the author"
width={500}
height={500}
  />
 )
}
```

> **Good to know** : Using props like `onLoad`, which accept a function, requires using to serialize the provided function.
Alternatively, you can use the loaderFile configuration in `next.config.js` to configure every instance of `next/image` in your application, without passing a prop.
#### `sizes`
Define the sizes of the image at different breakpoints. Used by the browser to choose the most appropriate size from the generated `srcset`.
```
import Image from'next/image'
exportdefaultfunctionPage() {
return (
  <divclassName="grid-element">
   <Image
fill
src="/example.png"
sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
   />
  </div>
 )
}
```

`sizes` should be used when:
  * The image is using the `fill` prop
  * CSS is used to make the image responsive


If `sizes` is missing, the browser assumes the image will be as wide as the viewport (`100vw`). This can cause unnecessarily large images to be downloaded.
In addition, `sizes` affects how `srcset` is generated:
  * Without `sizes`: Next.js generates a limited `srcset` (e.g. 1x, 2x), suitable for fixed-size images.
  * With `sizes`: Next.js generates a full `srcset` (e.g. 640w, 750w, etc.), optimized for responsive layouts.


> Learn more about `srcset` and `sizes` on and .
#### `quality`
An integer between `1` and `100` that sets the quality of the optimized image. Higher values increase file size and visual fidelity. Lower values reduce file size but may affect sharpness.
```
// Default quality is 75
<Imagequality={75} />
```

If you’ve configured qualities in `next.config.js`, the value must match one of the allowed entries.
> **Good to know** : If the original image is already low quality, setting a high quality value will increase the file size without improving appearance.
#### `style`
Allows passing CSS styles to the underlying image element.
```
constimageStyle= {
 borderRadius:'50%',
 border:'1px solid #fff',
 width:'100px',
 height:'auto',
}
exportdefaultfunctionProfileImage() {
return <Imagesrc="..."style={imageStyle} />
}
```

> **Good to know** : If you’re using the `style` prop to set a custom width, be sure to also set `height: 'auto'` to preserve the image’s aspect ratio.
#### `priority`
A boolean that indicates if the image should be preloaded.
```
// Default priority is false
<Imagepriority={false} />
```

  * `true`: the image. Disables lazy loading.
  * `false`: Lazy loads the image.


**When to use it:**
  * The image is above the fold.
  * The image is the Largest Contentful Paint (LCP) element.
  * You want to improve the initial loading performance of your page.


**When not to use it:**
  * When the `loading` prop isused (will trigger warnings).


#### `loading`
Controls when the image should start loading.
```
// Defaults to lazy
<Imageloading="lazy" />
```

  * `lazy`: Defer loading the image until it reaches a calculated distance from the viewport.
  * `eager`: Load the image immediately, regardless of its position in the page.


Use `eager` only when you want to ensure the image is loaded immediately.
> Learn more about the .
#### `placeholder`
Specifies a placeholder to use while the image is loading, improving the perceived loading performance.
```
// defaults to empty
<Imageplaceholder="empty" />
```

  * `empty`: No placeholder while the image is loading.
  * `blur`: Use a blurred version of the image as a placeholder. Must be used with the `blurDataURL` property.
  * `data:image/...`: Uses the as the placeholder.


**Examples:**
> Learn more about the .
#### `blurDataURL`
A to be used as a placeholder image before the image successfully loads. Can be automatically set or used with the `placeholder="blur"` property.
```
<Imageplaceholder="blur"blurDataURL="..." />
```

The image is automatically enlarged and blurred, so a very small image (10px or less) is recommended.
**Automatic**
If `src` is a static import of a `jpg`, `png`, `webp`, or `avif` file, `blurDataURL` is added automatically—unless the image is animated.
**Manually set**
If the image is dynamic or remote, you must provide `blurDataURL` yourself. To generate one, you can use:
A large blurDataURL may hurt performance. Keep it small and simple.
**Examples:**
#### `onLoad`
A callback function that is invoked once the image is completely loaded and the placeholder has been removed.
```
<ImageonLoad={(e) =>console.log(e.target.naturalWidth)} />
```

The callback function will be called with one argument, the event which has a `target` that references the underlying `<img>` element.
> **Good to know** : Using props like `onLoad`, which accept a function, requires using to serialize the provided function.
#### `onError`
A callback function that is invoked if the image fails to load.
```
<ImageonError={(e) =>console.error(e.target.id)} />
```

> **Good to know** : Using props like `onError`, which accept a function, requires using to serialize the provided function.
#### `unoptimized`
A boolean that indicates if the image should be optimized. This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).
```
import Image from'next/image'
constUnoptimizedImage= (props) => {
// Default is false
return <Image {...props} unoptimized />
}
```

  * `true`: The source image will be served as-is from the `src` instead of changing quality, size, or format.
  * `false`: The source image will be optimized.


Since Next.js 12.3.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:
next.config.js
```
module.exports= {
 images: {
  unoptimized:true,
 },
}
```

#### `overrideSrc`
When providing the `src` prop to the `<Image>` component, both the `srcset` and `src` attributes are generated automatically for the resulting `<img>`.
input.js
```
<Imagesrc="/profile.jpg" />
```

output.html
```
<img
srcset="
  /_next/image?url=%2Fme.jpg&w=640&q=75 1x,
  /_next/image?url=%2Fme.jpg&w=828&q=75 2x
 "
src="/_next/image?url=%2Fme.jpg&w=828&q=75"
/>
```

In some cases, it is not desirable to have the `src` attribute generated and you may wish to override it using the `overrideSrc` prop.
For example, when upgrading an existing website from `<img>` to `<Image>`, you may wish to maintain the same `src` attribute for SEO purposes such as image ranking or avoiding recrawl.
input.js
```
<Imagesrc="/profile.jpg"overrideSrc="/override.jpg" />
```

output.html
```
<img
srcset="
  /_next/image?url=%2Fme.jpg&w=640&q=75 1x,
  /_next/image?url=%2Fme.jpg&w=828&q=75 2x
 "
src="/override.jpg"
/>
```

#### `decoding`
A hint to the browser indicating if it should wait for the image to be decoded before presenting other content updates or not.
```
// Default is async
<Imagedecoding="async" />
```

  * `async`: Asynchronously decode the image and allow other content to be rendered before it completes.
  * `sync`: Synchronously decode the image for atomic presentation with other content.
  * `auto`: No preference. The browser chooses the best approach.


> Learn more about the .
### Other Props
Other properties on the `<Image />` component will be passed to the underlying `img` element with the exception of the following:
  * `srcSet`: Use Device Sizes instead.


### Deprecated props
#### `onLoadingComplete`
> **Warning** : Deprecated in Next.js 14, use `onLoad` instead.
A callback function that is invoked once the image is completely loaded and the placeholder has been removed.
The callback function will be called with one argument, a reference to the underlying `<img>` element.
```
'use client'
<ImageonLoadingComplete={(img) =>console.log(img.naturalWidth)} />
```

> **Good to know** : Using props like `onLoadingComplete`, which accept a function, requires using to serialize the provided function.
### Configuration options
You can configure the Image Component in `next.config.js`. The following options are available:
#### `localPatterns`
Use `localPatterns` in your `next.config.js` file to allow images from specific local paths to be optimized and block all others.
next.config.js
```
module.exports= {
 images: {
  localPatterns: [
   {
    pathname:'/assets/images/**',
    search:'',
   },
  ],
 },
}
```

The example above will ensure the `src` property of `next/image` must start with `/assets/images/` and must not have a query string. Attempting to optimize any other path will respond with `400` Bad Request error.
#### `remotePatterns`
Use `remotePatterns` in your `next.config.js` file to allow images from specific external paths and block all others. This ensures that only external images from your account can be served.
next.config.js
```
module.exports= {
 images: {
  remotePatterns: [newURL('],
 },
}
```

If using a version prior to 15.3.0, you can configure `remotePatterns` using the object:
next.config.js
```
module.exports= {
 images: {
  remotePatterns: [
   {
    protocol:'https',
    hostname:'example.com',
    port:'',
    pathname:'/account123/**',
    search:'',
   },
  ],
 },
}
```

The example above will ensure the `src` property of `next/image` must start with `` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with `400` Bad Request.
**Wildcard Patterns:**
Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:
  * `*` match a single path segment or subdomain
  * `**` match any number of path segments at the end or subdomains at the beginning. This syntax does not work in the middle of the pattern.


next.config.js
```
module.exports= {
 images: {
  remotePatterns: [
   {
    protocol:'https',
    hostname:'**.example.com',
    port:'',
    search:'',
   },
  ],
 },
}
```

This allows subdomains like `image.example.com`. Query strings and custom ports are still blocked.
> **Good to know** : When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.
**Query Strings** :
You can also restrict query strings using the `search` property:
next.config.js
```
module.exports= {
 images: {
  remotePatterns: [
   {
    protocol:'https',
    hostname:'assets.example.com',
    search:'?v=1727111025337',
   },
  ],
 },
}
```

The example above will ensure the `src` property of `next/image` must start with `` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with `400` Bad Request.
#### `loaderFile`
`loaderFiles` allows you to use a custom image optimization service instead of Next.js.
next.config.js
```
module.exports= {
 images: {
  loader:'custom',
  loaderFile:'./my/image/loader.js',
 },
}
```

The path must be relative to the project root. The file must export a default function that returns a URL string:
my/image/loader.js
```
'use client'
exportdefaultfunctionmyImageLoader({ src, width, quality }) {
return`{src}?w=${width}&q=${quality ||75}`
}
```

**Example:**
  * Custom Image Loader Configuration


> Alternatively, you can use the `loader` prop to configure each instance of `next/image`.
#### `deviceSizes`
`deviceSizes` allows you to specify a list of device width breakpoints. These widths are used when the `next/image` component uses `sizes` prop to ensure the correct image is served for the user's device.
If no configuration is provided, the default below is used:
next.config.js
```
module.exports= {
 images: {
  deviceSizes: [640,750,828,1080,1200,1920,2048,3840],
 },
}
```

#### `imageSizes`
`imageSizes` allows you to specify a list of image widths. These widths are concatenated with the array of device sizes to form the full array of sizes used to generate image .
If no configuration is provided, the default below is used:
next.config.js
```
module.exports= {
 images: {
  imageSizes: [16,32,48,64,96,128,256,384],
 },
}
```

`imageSizes` is only used for images which provide a `sizes` prop, which indicates that the image is less than the full width of the screen. Therefore, the sizes in `imageSizes` should all be smaller than the smallest size in `deviceSizes`.
#### `qualities`
`qualities` allows you to specify a list of image quality values.
next.config.js
```
module.exports= {
 images: {
  qualities: [25,50,75],
 },
}
```

In the example above, only three qualities are allowed: 25, 50, and 75. If the `quality` prop does not match a value in this array, the image will fail with a `400` Bad Request.
#### `formats`
`formats` allows you to specify a list of image formats to be used.
next.config.js
```
module.exports= {
 images: {
// Default
  formats: ['image/webp'],
 },
}
```

Next.js automatically detects the browser's supported image formats via the request's `Accept` header in order to determine the best output format.
If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is animated), it will use the original image's format.
You can enable AVIF support, which will fallback to the original format of the src image if the browser :
next.config.js
```
module.exports= {
 images: {
  formats: ['image/avif'],
 },
}
```

> **Good to know** :
>   * We still recommend using WebP for most use cases.
>   * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower, but subsequent requests that are cached will be faster.
>   * If you self-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.
> 

#### `minimumCacheTTL`
`minimumCacheTTL` allows you to configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a Static Image Import which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.
If no configuration is provided, the default below is used.
next.config.js
```
module.exports= {
 images: {
  minimumCacheTTL:60,// 1 minute
 },
}
```

You can increase the TTL to reduce the number of revalidations and potentionally lower cost:
next.config.js
```
module.exports= {
 images: {
  minimumCacheTTL:2678400,// 31 days
 },
}
```

The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.
If you need to change the caching behavior per image, you can configure `headers` to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).
There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the `src` prop or delete the cached file `<distDir>/cache/images`.
#### `disableStaticImages`
`disableStaticImages` allows you to disable static image imports.
The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property. In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.
You can disable static image imports inside your `next.config.js`:
next.config.js
```
module.exports= {
 images: {
  disableStaticImages:true,
 },
}
```

#### `dangerouslyAllowSVG`
`dangerouslyAllowSVG` allows you to serve SVG images.
next.config.js
```
module.exports= {
 images: {
  dangerouslyAllowSVG:true,
 },
}
```

By default, Next.js does not optimize SVG images for a few reasons:
  * SVG is a vector format meaning it can be resized losslessly.
  * SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper Content Security Policy (CSP) headers.


We recommend using the `unoptimized` prop when the `src` prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.
```
<Imagesrc="/my-image.svg"unoptimized />
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.
next.config.js
```
module.exports= {
 images: {
  dangerouslyAllowSVG:true,
  contentDispositionType:'attachment',
  contentSecurityPolicy:"default-src 'self'; script-src 'none'; sandbox;",
 },
}
```

#### `contentDispositionType`
`contentDispositionType` allows you to configure the header.
next.config.js
```
module.exports= {
 images: {
  contentDispositionType:'inline',
 },
}
```

By default, the loader sets the header to `attachment` for added protection since the API can serve arbitrary remote images.
The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when `dangerouslyAllowSVG` is true.
You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.
### Deprecated configuration options
#### `domains`
> **Warning** : Deprecated since Next.js 14 in favor of strict `remotePatterns` in order to protect your application from malicious users. Only use `domains` if you own all the content served from the domain.
Similar to `remotePatterns`, the `domains` configuration can be used to provide a list of allowed hostnames for external images. However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.
Below is an example of the `domains` property in the `next.config.js` file:
next.config.js
```
module.exports= {
 images: {
  domains: ['assets.acme.com'],
 },
}
```

## Functions
### `getImageProps`
The `getImageProps` function can be used to get the props that would be passed to the underlying `<img>` element, and instead pass them to another component, style, canvas, etc.
```
import { getImageProps } from'next/image'
constprops=getImageProps({
 src:'
 alt:'A scenic mountain view',
 width:1200,
 height:800,
})
functionImageWithCaption() {
return (
  <figure>
   <img {...props} />
   <figcaption>A scenic mountain view</figcaption>
  </figure>
 )
}
```

This also avoid calling React `useState()` so it can lead to better performance, but it cannot be used with the `placeholder` prop because the placeholder will never be removed.
## Known browser bugs
This `next/image` component uses browser native , which may fallback to eager loading for older browsers before Safari 15.4. When using the blur-up placeholder, older browsers before Safari 12 will fallback to empty placeholder. When using styles with `width`/`height` of `auto`, it is possible to cause on older browsers before Safari 15 that don't . For more details, see .
  * display a gray border while loading. Safari 16.4 . Possible solutions:
    * Use CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }`
    * Use `priority` if the image is above the fold
  * displays a white background while loading. Possible solutions:
    * Enable AVIF `formats`
    * Use `placeholder`


## Examples
### Styling images
Styling the Image component is similar to styling a normal `<img>` element, but there are a few guidelines to keep in mind:
Use `className` or `style`, not `styled-jsx`. In most cases, we recommend using the `className` prop. This can be an imported CSS Module, a global stylesheet, etc.
```
import styles from'./styles.module.css'
exportdefaultfunctionMyImage() {
return <ImageclassName={styles.image} src="/my-image.png"alt="My Image" />
}
```

You can also use the `style` prop to assign inline styles.
```
exportdefaultfunctionMyImage() {
return (
  <Imagestyle={{ borderRadius:'8px' }} src="/my-image.png"alt="My Image" />
 )
}
```

When using `fill`, the parent element must have `position: relative` or `display: block`. This is necessary for the proper rendering of the image element in that layout mode.
```
<divstyle={{ position:'relative' }}>
 <Imagefillsrc="/my-image.png"alt="My Image" />
</div>
```

You cannot use styled-jsx because it's scoped to the current component (unless you mark the style as `global`).
### Responsive images with a static export
When you import a static image, Next.js automatically sets its width and height based on the file. You can make the image responsive by setting the style:
!Responsive image filling the width and height of its parent container!Responsive image filling the width and height of its parent container
```
import Image from'next/image'
import mountains from'../public/mountains.jpg'
exportdefaultfunctionResponsive() {
return (
  <divstyle={{ display:'flex', flexDirection:'column' }}>
   <Image
alt="Mountains"
// Importing an image will
// automatically set the width and height
src={mountains}
sizes="100vw"
// Make the image display full width
// and preserve its aspect ratio
style={{
     width:'100%',
     height:'auto',
    }}
   />
  </div>
 )
}
```

### Responsive images with a remote URL
If the source image is a dynamic or a remote URL, you must provide the width and height props so Next.js can calculate the aspect ratio:
components/page.js
```
import Image from'next/image'
exportdefaultfunctionPage({ photoUrl }) {
return (
  <Image
src={photoUrl}
alt="Picture of the author"
sizes="100vw"
style={{
    width:'100%',
    height:'auto',
   }}
width={500}
height={300}
  />
 )
}
```

Try it out:
### Responsive image with `fill`
If you don't know the aspect ratio of the image, you can add the `fill` prop with the `objectFit` prop set to `cover`. This will make the image fill the full width of its parent container.
!Grid of images filling parent container width!Grid of images filling parent container width
```
import Image from'next/image'
import mountains from'../public/mountains.jpg'
exportdefaultfunctionFill() {
return (
  <div
style={{
    display:'grid',
    gridGap:'8px',
    gridTemplateColumns:'repeat(auto-fit, minmax(400px, auto))',
   }}
  >
   <divstyle={{ position:'relative', width:'400px' }}>
    <Image
alt="Mountains"
src={mountains}
fill
sizes="(min-width: 808px) 50vw, 100vw"
style={{
      objectFit:'cover',// cover, contain, none
     }}
    />
   </div>
   {/* And more images in the grid... */}
  </div>
 )
}
```

### Background Image
Use the `fill` prop to make the image cover the entire screen area:
!Background image taking full width and height of page!Background image taking full width and height of page
```
import Image from'next/image'
import mountains from'../public/mountains.jpg'
exportdefaultfunctionBackground() {
return (
  <Image
alt="Mountains"
src={mountains}
placeholder="blur"
quality={100}
fill
sizes="100vw"
style={{
    objectFit:'cover',
   }}
  />
 )
}
```

For examples of the Image component used with the various styles, see the .
### Remote images
To use a remote image, the `src` property should be a URL string.
app/page.js
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

Since Next.js does not have access to remote files during the build process, you'll need to provide the `width`, `height` and optional `blurDataURL` props manually.
The `width` and `height` attributes are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. The `width` and `height` do _not_ determine the rendered size of the image file.
To safely allow optimizing images, define a list of supported URL patterns in `next.config.js`. Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:
next.config.js
```
module.exports= {
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
```

### Theme detection
If you want to display a different image for light and dark mode, you can create a new component that wraps two `<Image>` components and reveals the correct one based on a CSS media query.
components/theme-image.module.css
```
.imgDark {
display:none;
}
@media (prefers-color-scheme: dark) {
.imgLight {
display:none;
 }
.imgDark {
display:unset;
 }
}
```

components/theme-image.tsx
```
import styles from'./theme-image.module.css'
import Image, { ImageProps } from'next/image'
typeProps=Omit<ImageProps,'src'|'priority'|'loading'> & {
 srcLight:string
 srcDark:string
}
constThemeImage= (props:Props) => {
const { srcLight,srcDark,...rest } = props
return (
  <>
   <Image {...rest} src={srcLight} className={styles.imgLight} />
   <Image {...rest} src={srcDark} className={styles.imgDark} />
  </>
 )
}
```

> **Good to know** : The default behavior of `loading="lazy"` ensures that only the correct image is loaded. You cannot use `priority` or `loading="eager"` because that would cause both images to load. Instead, you can use .
Try it out:
### Art direction
If you want to display a different image for mobile and desktop, sometimes called , you can provide different `src`, `width`, `height`, and `quality` props to `getImageProps()`.
app/page.js
```
import { getImageProps } from'next/image'
exportdefaultfunctionHome() {
constcommon= { alt:'Art Direction Example', sizes:'100vw' }
const {
  props: { srcSet: desktop },
 } =getImageProps({
...common,
  width:1440,
  height:875,
  quality:80,
  src:'/desktop.jpg',
 })
const {
  props: { srcSet: mobile,...rest },
 } =getImageProps({
...common,
  width:750,
  height:1334,
  quality:70,
  src:'/mobile.jpg',
 })
return (
  <picture>
   <sourcemedia="(min-width: 1000px)"srcSet={desktop} />
   <sourcemedia="(min-width: 500px)"srcSet={mobile} />
   <img {...rest} style={{ width:'100%', height:'auto' }} />
  </picture>
 )
}
```

### Background CSS
You can even convert the `srcSet` string to the CSS function to optimize a background image.
app/page.js
```
import { getImageProps } from'next/image'
functiongetBackgroundImage(srcSet ='') {
constimageSet= srcSet
.split(', ')
.map((str) => {
const [url,dpi] =str.split(' ')
return`url("${url}") ${dpi}`
  })
.join(', ')
return`image-set(${imageSet})`
}
exportdefaultfunctionHome() {
const {
  props: { srcSet },
 } =getImageProps({ alt:'', width:128, height:128, src:'/img.png' })
constbackgroundImage=getBackgroundImage(srcSet)
conststyle= { height:'100vh', width:'100vw', backgroundImage }
return (
  <mainstyle={style}>
   <h1>Hello World</h1>
  </main>
 )
}
```

## Version History
Version| Changes  
---|---  
`v15.3.0`| `remotePatterns` added support for array of `URL` objects.  
`v15.0.0`| `contentDispositionType` configuration default changed to `attachment`.  
`v14.2.23`| `qualities` configuration added.  
`v14.2.15`| `decoding` prop added and `localPatterns` configuration added.  
`v14.2.14`| `remotePatterns.search` prop added.  
`v14.2.0`| `overrideSrc` prop added.  
`v14.1.0`| `getImageProps()` is stable.  
`v14.0.0`| `onLoadingComplete` prop and `domains` config deprecated.  
`v13.4.14`| `placeholder` prop support for `data:/image...`  
`v13.2.0`| `contentDispositionType` configuration added.  
`v13.0.6`| `ref` prop added.  
`v13.0.0`| The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A codemod is available to safely and automatically rename your imports. `<span>` wrapper removed. `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` props removed. `alt` is required. `onLoadingComplete` receives reference to `img` element. Built-in loader config removed.  
`v12.3.0`| `remotePatterns` and `unoptimized` configuration is stable.  
`v12.2.0`| Experimental `remotePatterns` and experimental `unoptimized` configuration added. `layout="raw"` removed.  
`v12.1.1`| `style` prop added. Experimental support for `layout="raw"` added.  
`v12.1.0`| `dangerouslyAllowSVG` and `contentSecurityPolicy` configuration added.  
`v12.0.9`| `lazyRoot` prop added.  
`v12.0.0`| `formats` configuration added.AVIF support added.Wrapper `<div>` changed to `<span>`.  
`v11.1.0`| `onLoadingComplete` and `lazyBoundary` props added.  
`v11.0.0`| `src` prop support for static import.`placeholder` prop added.`blurDataURL` prop added.  
`v10.0.5`| `loader` prop added.  
`v10.0.1`| `layout` prop added.  
`v10.0.0`| `next/image` introduced.
