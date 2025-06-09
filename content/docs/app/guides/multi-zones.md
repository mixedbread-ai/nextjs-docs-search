---
title: "How to build micro-frontends using multi-zones and Next.js"
path: "App / Guides / Multi Zones"
source_url: https://nextjs.org/docs/app/guides/multi-zones
content_length: 6051
---

# How to build micro-frontends using multi-zones and Next.js
Examples
Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.
For example, let's say you have the following set of pages that you would like to split up:
  * `/blog/*` for all blog posts
  * `/dashboard/*` for all pages when the user is logged-in to the dashboard
  * `/*` for the rest of your website not covered by other zones


With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.
!Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.!Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.
Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from `/` to `/products` will be a soft navigation.
Navigating from a page in one zone to a page in another zone, such as from `/` to `/dashboard`, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.
## How to define a zone
A zone is a normal Next.js application where you also configure an assetPrefix to avoid conflicts with pages and static files in other zones.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 assetPrefix:'/blog-static',
}
```

Next.js assets, such as JavaScript and CSS, will be prefixed with `assetPrefix` to make sure that they don't conflict with assets from other zones. These assets will be served under `/assetPrefix/_next/...` for each of the zones.
The default application handling all paths not routed to another more specific zone does not need an `assetPrefix`.
In versions older than Next.js 15, you may also need an additional rewrite to handle the static assets. This is no longer necessary in Next.js 15.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 assetPrefix:'/blog-static',
asyncrewrites() {
return {
   beforeFiles: [
    {
     source:'/blog-static/_next/:path+',
     destination:'/_next/:path+',
    },
   ],
  }
 },
}
```

## How to route requests to the right zone
With the Multi Zones set-up, you need to route the paths to the correct zone since they are served by different applications. You can use any HTTP proxy to do this, but one of the Next.js applications can also be used to route requests for the entire domain.
To route to the correct zone using a Next.js application, you can use `rewrites`. For each path served by a different zone, you would add a rewrite rule to send that path to the domain of the other zone, and you also need to rewrite the requests for the static assets. For example:
next.config.js
```
async rewrites() {
return [
    {
      source:'/blog',
      destination:`${process.env.BLOG_DOMAIN}/blog`,
    },
    {
      source:'/blog/:path+',
      destination:`${process.env.BLOG_DOMAIN}/blog/:path+`,
    },
    {
      source:'/blog-static/:path+',
      destination:`${process.env.BLOG_DOMAIN}/blog-static/:path+`,
    }
  ];
}
```

`destination` should be a URL that is served by the zone, including scheme and domain. This should point to the zone's production domain, but it can also be used to route requests to `localhost` in local development.
> **Good to know** : URL paths should be unique to a zone. For example, two zones trying to serve `/blog` would create a routing conflict.
### Routing requests using middleware
Routing requests through `rewrites` is recommended to minimize latency overhead for the requests, but middleware can also be used when there is a need for a dynamic decision when routing. For example, if you are using a feature flag to decide where a path should be routed such as during a migration, you can use middleware.
middleware.js
```
exportasyncfunctionmiddleware(request) {
const { pathname,search } =req.nextUrl;
if (pathname ==='/your-path'&&myFeatureFlag.isEnabled()) {
returnNextResponse.rewrite(`${rewriteDomain}${pathname}${search});
 }
}
```

## Linking between zones
Links to paths in a different zone should use an `a` tag instead of the Next.js `<Link>` component. This is because Next.js will try to prefetch and soft navigate to any relative path in `<Link>` component, which will not work across zones.
## Sharing code
The Next.js applications that make up the different zones can live in any repository. However, it is often convenient to put these zones in a to more easily share code. For zones that live in different repositories, code can also be shared using public or private NPM packages.
Since the pages in different zones may be released at different times, feature flags can be useful for enabling or disabling features in unison across the different zones.
## Server Actions
When using Server Actions with Multi-Zones, you must explicitly allow the user-facing origin since your user facing domain may serve multiple applications. In your `next.config.js` file, add the following lines:
next.config.js
```
constnextConfig= {
 experimental: {
  serverActions: {
   allowedOrigins: ['your-production-domain.com'],
  },
 },
}
```

See `serverActions.allowedOrigins` for more information.
