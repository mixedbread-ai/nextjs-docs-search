---
title: Images
path: "App / Api Reference / Config / Next Config Js / Images"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/images
content_length: 5446
---

# images
If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure `next.config.js` with the following:
next.config.js
```
module.exports= {
 images: {
  loader:'custom',
  loaderFile:'./my/image/loader.js',
 },
}
```

This `loaderFile` must point to a file relative to the root of your Next.js application. The file must export a default function that returns a string, for example:
my/image/loader.js
```
'use client'
exportdefaultfunctionmyImageLoader({ src, width, quality }) {
return`{src}?w=${width}&q=${quality ||75}`
}
```

Alternatively, you can use the `loader` prop to pass the function to each instance of `next/image`.
> **Good to know** : Customizing the image loader file, which accepts a function, requires using Client Components to serialize the provided function.
To learn more about configuring the behavior of the built-in Image Optimization API and the Image Component, see Image Configuration Options for available options.
## Example Loader Configuration
  * Akamai
  * AWS CloudFront
  * Cloudinary
  * Cloudflare
  * Contentful
  * Fastly
  * Gumlet
  * ImageEngine
  * Imgix
  * PixelBin
  * Sanity
  * Sirv
  * Supabase
  * Thumbor
  * Imagekit
  * Nitrogen AIO


### Akamai
```
// Docs: 
exportdefaultfunctionakamaiLoader({ src, width, quality }) {
return`{src}?imwidth=${width}`
}
```

### AWS CloudFront
```
// Docs: 
exportdefaultfunctioncloudfrontLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
url.searchParams.set('format','auto')
url.searchParams.set('width',width.toString())
url.searchParams.set('quality', (quality ||75).toString())
returnurl.href
}
```

### Cloudinary
```
// Demo: 
exportdefaultfunctioncloudinaryLoader({ src, width, quality }) {
constparams= ['f_auto','c_limit',`w_${width}`,`q_${quality ||'auto'}`]
return`{params.join(',')}${src}`
}
```

### Cloudflare
```
// Docs: 
exportdefaultfunctioncloudflareLoader({ src, width, quality }) {
constparams= [`width=${width}`,`quality=${quality ||75}`,'format=auto']
return`{params.join(',')}/${src}`
}
```

### Contentful
```
// Docs: 
exportdefaultfunctioncontentfulLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
url.searchParams.set('fm','webp')
url.searchParams.set('w',width.toString())
url.searchParams.set('q', (quality ||75).toString())
returnurl.href
}
```

### Fastly
```
// Docs: 
exportdefaultfunctionfastlyLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
url.searchParams.set('auto','webp')
url.searchParams.set('width',width.toString())
url.searchParams.set('quality', (quality ||75).toString())
returnurl.href
}
```

### Gumlet
```
// Docs: 
exportdefaultfunctiongumletLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
url.searchParams.set('format','auto')
url.searchParams.set('w',width.toString())
url.searchParams.set('q', (quality ||75).toString())
returnurl.href
}
```

### ImageEngine
```
// Docs: 
exportdefaultfunctionimageengineLoader({ src, width, quality }) {
constcompression=100- (quality ||50)
constparams= [`w_${width}`,`cmpr_${compression}`)]
return`{src}?imgeng=/${params.join('/')`
}
```

### Imgix
```
// Demo: 
exportdefaultfunctionimgixLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
constparams=url.searchParams
params.set('auto',params.getAll('auto').join(',') ||'format')
params.set('fit',params.get('fit') ||'max')
params.set('w',params.get('w') ||width.toString())
params.set('q', (quality ||50).toString())
returnurl.href
}
```

### PixelBin
```
// Doc (Resize): 
// Doc (Optimise): 
// Doc (Auto Format Delivery): 
exportdefaultfunctionpixelBinLoader({ src, width, quality }) {
constname='<your-cloud-name>'
constopt=`t.resize(w:${width})~t.compress(q:${quality ||75})`
return`{name}/${opt}/${src}?f_auto=true`
}
```

### Sanity
```
// Docs: 
exportdefaultfunctionsanityLoader({ src, width, quality }) {
constprj='zp7mbokg'
constdataset='production'
consturl=newURL(`{prj}/${dataset}${src}`)
url.searchParams.set('auto','format')
url.searchParams.set('fit','max')
url.searchParams.set('w',width.toString())
if (quality) {
url.searchParams.set('q',quality.toString())
 }
returnurl.href
}
```

### Sirv
```
// Docs: 
exportdefaultfunctionsirvLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
constparams=url.searchParams
params.set('format',params.getAll('format').join(',') ||'optimal')
params.set('w',params.get('w') ||width.toString())
params.set('q', (quality ||85).toString())
returnurl.href
}
```

### Supabase
```
// Docs: 
exportdefaultfunctionsupabaseLoader({ src, width, quality }) {
consturl=newURL(`{src}`)
url.searchParams.set('width',width.toString())
url.searchParams.set('quality', (quality ||75).toString())
returnurl.href
}
```

### Thumbor
```
// Docs: 
exportdefaultfunctionthumborLoader({ src, width, quality }) {
constparams= [`${width}x0`,`filters:quality(${quality ||75})`]
return`{params.join('/')}${src}`
}
```

### ImageKit.io
```
// Docs: 
exportdefaultfunctionimageKitLoader({ src, width, quality }) {
constparams= [`w-${width}`,`q-${quality ||80}`]
return`{src}?tr=${params.join(',')}`
}
```

### Nitrogen AIO
```
// Docs: 
exportdefaultfunctionaioLoader({ src, width, quality }) {
consturl=newURL(src,window.location.href)
constparams=url.searchParams
constaioParams=params.getAll('aio')
aioParams.push(`w-${width}`)
if (quality) {
aioParams.push(`q-${quality.toString()}`)
 }
params.set('aio',aioParams.join(';'))
returnurl.href
}
```
