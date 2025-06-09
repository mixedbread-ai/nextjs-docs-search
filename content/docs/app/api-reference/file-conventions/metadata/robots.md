---
title: Robots.txt
path: "App / Api Reference / File Conventions / Metadata / Robots"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots
content_length: 1842
---

# robots.txt
Add or generate a `robots.txt` file that matches the in the **root** of `app` directory to tell search engine crawlers which URLs they can access on your site.
## Static `robots.txt`
app/robots.txt
```
User-Agent: *
Allow: /
Disallow: /private/
Sitemap: 
```

## Generate a Robots file
Add a `robots.js` or `robots.ts` file that returns a `Robots` object.
> **Good to know** : `robots.js` is a special Route Handlers that is cached by default unless it uses a Dynamic API or dynamic config option.
app/robots.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionrobots():MetadataRoute.Robots {
return {
  rules: {
   userAgent:'*',
   allow:'/',
   disallow:'/private/',
  },
  sitemap:'
 }
}
```

Output:
```
User-Agent: *
Allow: /
Disallow: /private/
Sitemap: 
```

### Customizing specific user agents
You can customise how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:
app/robots.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionrobots():MetadataRoute.Robots {
return {
  rules: [
   {
    userAgent:'Googlebot',
    allow: ['/'],
    disallow:'/private/',
   },
   {
    userAgent: ['Applebot','Bingbot'],
    disallow: ['/'],
   },
  ],
  sitemap:'
 }
}
```

Output:
```
User-Agent: Googlebot
Allow: /
Disallow: /private/
User-Agent: Applebot
Disallow: /
User-Agent: Bingbot
Disallow: /
Sitemap: 
```

### Robots object
```
typeRobots= {
 rules:
| {
    userAgent?:string|string[]
    allow?:string|string[]
    disallow?:string|string[]
    crawlDelay?:number
   }
|Array<{
    userAgent:string|string[]
    allow?:string|string[]
    disallow?:string|string[]
    crawlDelay?:number
   }>
sitemap?:string|string[]
host?:string
}
```

## Version History
Version| Changes  
---|---  
`v13.3.0`| `robots` introduced.
