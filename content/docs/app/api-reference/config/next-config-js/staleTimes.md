---
title: StaleTimes
path: "App / Api Reference / Config / Next Config Js / Staletimes"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes
content_length: 1705
---

# staleTimes
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
`staleTimes` is an experimental feature that enables caching of page segments in the client-side router cache.
You can enable this experimental feature and provide custom revalidation times by setting the experimental `staleTimes` flag:
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 experimental: {
  staleTimes: {
   dynamic:30,
   static:180,
  },
 },
}
module.exports= nextConfig
```

The `static` and `dynamic` properties correspond with the time period (in seconds) based on different types of link prefetching.
  * The `dynamic` property is used when the page is neither statically generated nor fully prefetched (e.g. with `prefetch={true}`). 
    * Default: 0 seconds (not cached)
  * The `static` property is used for statically generated pages, or when the `prefetch` prop on `Link` is set to `true`, or when calling `router.prefetch`. 
    * Default: 5 minutes


> **Good to know:**
>   * Loading boundaries are considered reusable for the `static` period defined in this configuration.
>   * This doesn't affect partial rendering, **meaning shared layouts won't automatically be refetched on every navigation, only the page segment that changes.**
>   * This doesn't change back/forward caching behavior to prevent layout shift and to prevent losing the browser scroll position.
> 

You can learn more about the Client Router Cache here.
### Version History
Version| Changes  
---|---  
`v15.0.0`| The `dynamic` `staleTimes` default changed from 30s to 0s.  
`v14.2.0`| Experimental `staleTimes` introduced.
