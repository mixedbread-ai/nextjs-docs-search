---
title: Sitemap.xml
path: "App / Api Reference / File Conventions / Metadata / Sitemap"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap
content_length: 6628
---

# sitemap.xml
`sitemap.(xml|js|ts)` is a special file that matches the to help search engine crawlers index your site more efficiently.
### Sitemap files (.xml)
For smaller applications, you can create a `sitemap.xml` file and place it in the root of your `app` directory.
app/sitemap.xml
```
<urlsetxmlns="">
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>yearly</changefreq>
  <priority>1</priority>
 </url>
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
 </url>
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.5</priority>
 </url>
</urlset>
```

### Generating a sitemap using code (.js, .ts)
You can use the `sitemap.(js|ts)` file convention to programmatically **generate** a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a `Sitemap` type is available.
> **Good to know** : `sitemap.js` is a special Route Handler that is cached by default unless it uses a Dynamic API or dynamic config option.
app/sitemap.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionsitemap():MetadataRoute.Sitemap {
return [
  {
   url:'
   lastModified:newDate(),
   changeFrequency:'yearly',
   priority:1,
  },
  {
   url:'
   lastModified:newDate(),
   changeFrequency:'monthly',
   priority:0.8,
  },
  {
   url:'
   lastModified:newDate(),
   changeFrequency:'weekly',
   priority:0.5,
  },
 ]
}
```

Output:
acme.com/sitemap.xml
```
<urlsetxmlns="">
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>yearly</changefreq>
  <priority>1</priority>
 </url>
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
 </url>
 <url>
  <loc></loc>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.5</priority>
 </url>
</urlset>
```

### Image Sitemaps
You can use `images` property to create image sitemaps. Learn more details in the .
app/sitemap.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionsitemap():MetadataRoute.Sitemap {
return [
  {
   url:'
   lastModified:'2021-01-01',
   changeFrequency:'weekly',
   priority:0.5,
   images: ['],
  },
 ]
}
```

Output:
acme.com/sitemap.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<urlset
xmlns=""
xmlns:image=""
>
 <url>
  <loc></loc>
  <image:image>
   <image:loc></image:loc>
  </image:image>
  <lastmod>2021-01-01</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.5</priority>
 </url>
</urlset>
```

### Video Sitemaps
You can use `videos` property to create video sitemaps. Learn more details in the .
app/sitemap.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionsitemap():MetadataRoute.Sitemap {
return [
  {
   url:'
   lastModified:'2021-01-01',
   changeFrequency:'weekly',
   priority:0.5,
   videos: [
    {
     title:'example',
     thumbnail_loc:'
     description:'this is the description',
    },
   ],
  },
 ]
}
```

Output:
acme.com/sitemap.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<urlset
xmlns=""
xmlns:video=""
>
 <url>
  <loc></loc>
  <video:video>
   <video:title>example</video:title>
   <video:thumbnail_loc></video:thumbnail_loc>
   <video:description>this is the description</video:description>
  </video:video>
  <lastmod>2021-01-01</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.5</priority>
 </url>
</urlset>
```

### Generate a localized Sitemap
app/sitemap.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionsitemap():MetadataRoute.Sitemap {
return [
  {
   url:'
   lastModified:newDate(),
   alternates: {
    languages: {
     es:'
     de:'
    },
   },
  },
  {
   url:'
   lastModified:newDate(),
   alternates: {
    languages: {
     es:'
     de:'
    },
   },
  },
  {
   url:'
   lastModified:newDate(),
   alternates: {
    languages: {
     es:'
     de:'
    },
   },
  },
 ]
}
```

Output:
acme.com/sitemap.xml
```
<urlsetxmlns=""xmlns:xhtml="">
 <url>
  <loc></loc>
  <xhtml:link
rel="alternate"
hreflang="es"
href=""/>
  <xhtml:link
rel="alternate"
hreflang="de"
href=""/>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
 </url>
 <url>
  <loc></loc>
  <xhtml:link
rel="alternate"
hreflang="es"
href=""/>
  <xhtml:link
rel="alternate"
hreflang="de"
href=""/>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
 </url>
 <url>
  <loc></loc>
  <xhtml:link
rel="alternate"
hreflang="es"
href=""/>
  <xhtml:link
rel="alternate"
hreflang="de"
href=""/>
  <lastmod>2023-04-06T15:02:24.021Z</lastmod>
 </url>
</urlset>
```

### Generating multiple sitemaps
While a single sitemap will work for most applications. For large web applications, you may need to split a sitemap into multiple files.
There are two ways you can create multiple sitemaps:
  * By nesting `sitemap.(xml|js|ts)` inside multiple route segments e.g. `app/sitemap.xml` and `app/products/sitemap.xml`.
  * By using the `generateSitemaps` function.


For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.
app/product/sitemap.ts
```
importtype { MetadataRoute } from'next'
import { BASE_URL } from'@/app/lib/constants'
exportasyncfunctiongenerateSitemaps() {
// Fetch the total number of products and calculate the number of sitemaps needed
return [{ id:0 }, { id:1 }, { id:2 }, { id:3 }]
}
exportdefaultasyncfunctionsitemap({
 id,
}: {
 id:number
}):Promise<MetadataRoute.Sitemap> {
// Google's limit is 50,000 URLs per sitemap
conststart= id *50000
constend= start +50000
constproducts=awaitgetProducts(
`SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
 )
returnproducts.map((product) => ({
  url:`${BASE_URL}/product/${product.id}`,
  lastModified:product.date,
 }))
}
```

Your generated sitemaps will be available at `/.../sitemap/[id]`. For example, `/product/sitemap/1.xml`.
See the `generateSitemaps` API reference for more information.
## Returns
The default function exported from `sitemap.(xml|ts|js)` should return an array of objects with the following properties:
```
typeSitemap=Array<{
 url:string
 lastModified?:string|Date
 changeFrequency?:
|'always'
|'hourly'
|'daily'
|'weekly'
|'monthly'
|'yearly'
|'never'
priority?:number
alternates?: {
  languages?:Languages<string>
 }
}>
```

## Version History
Version| Changes  
---|---  
`v14.2.0`| Add localizations support.  
`v13.4.14`| Add `changeFrequency` and `priority` attributes to sitemaps.  
`v13.3.0`| `sitemap` introduced.
