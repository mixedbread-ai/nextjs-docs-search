---
title: "How to optimize your Next.js application for production"
path: "App / Guides / Production Checklist"
source_url: https://nextjs.org/docs/app/guides/production-checklist
content_length: 6955
---

# How to optimize your Next.js application for production
Before taking your Next.js application to production, there are some optimizations and patterns you should consider implementing for the best user experience, performance, and security.
This page provides best practices that you can use as a reference when building your application and before going to production, as well as the automatic Next.js optimizations you should be aware of.
## Automatic optimizations
These Next.js optimizations are enabled by default and require no configuration:
  * **Server Components:** Next.js uses Server Components by default. Server Components run on the server, and don't require JavaScript to render on the client. As such, they have no impact on the size of your client-side JavaScript bundles. You can then use Client Components as needed for interactivity.
  * **Code-splitting:** Server Components enable automatic code-splitting by route segments. You may also consider lazy loading Client Components and third-party libraries, where appropriate.
  * **Prefetching:** When a link to a new route enters the user's viewport, Next.js prefetches the route in background. This makes navigation to new routes almost instant. You can opt out of prefetching, where appropriate.
  * **Static Rendering:** Next.js statically renders Server and Client Components on the server at build time and caches the rendered result to improve your application's performance. You can opt into Dynamic Rendering for specific routes, where appropriate. 
  * **Caching:** Next.js caches data requests, the rendered result of Server and Client Components, static assets, and more, to reduce the number of network requests to your server, database, and backend services. You may opt out of caching, where appropriate.


These defaults aim to improve your application's performance, and reduce the cost and amount of data transferred on each network request.
## During development
While building your application, we recommend using the following features to ensure the best performance and user experience:
### Routing and rendering
  * **Layouts:** Use layouts to share UI across pages and enable partial rendering on navigation.
  * **`<Link>`component:** Use the `<Link>` component for client-side navigation and prefetching.
  * **Error Handling:** Gracefully handle catch-all errors and 404 errors in production by creating custom error pages.
  * **Client and Server Components:** Follow the recommended composition patterns for Server and Client Components, and check the placement of your `"use client"` boundaries to avoid unnecessarily increasing your client-side JavaScript bundle.
  * **Dynamic APIs:** Be aware that Dynamic APIs like `cookies` and the `searchParams` prop will opt the entire route into Dynamic Rendering (or your whole application if used in the Root Layout). Ensure Dynamic API usage is intentional and wrap them in `<Suspense>` boundaries where appropriate.


> **Good to know** : Partial Prerendering (experimental) will allow parts of a route to be dynamic without opting the whole route into dynamic rendering.
### Data fetching and caching
  * **Server Components:** Leverage the benefits of fetching data on the server using Server Components.
  * **Route Handlers:** Use Route Handlers to access your backend resources from Client Components. But do not call Route Handlers from Server Components to avoid an additional server request.
  * **Streaming:** Use Loading UI and React Suspense to progressively send UI from the server to the client, and prevent the whole route from blocking while data is being fetched.
  * **Parallel Data Fetching:** Reduce network waterfalls by fetching data in parallel, where appropriate. Also, consider preloading data where appropriate.
  * **Data Caching:** Verify whether your data requests are being cached or not, and opt into caching, where appropriate. Ensure requests that don't use `fetch` are cached.
  * **Static Images:** Use the `public` directory to automatically cache your application's static assets, e.g. images.


### UI and accessibility
  * **Forms and Validation:** Use Server Actions to handle form submissions, server-side validation, and handle errors.


  * **Font Module:** Optimize fonts by using the Font Module, which automatically hosts your font files with other static assets, removes external network requests, and reduces .
  * **`<Image>`Component:** Optimize images by using the Image Component, which automatically optimizes images, prevents layout shift, and serves them in modern formats like WebP.
  * **`<Script>`Component:** Optimize third-party scripts by using the Script Component, which automatically defers scripts and prevents them from blocking the main thread.
  * **ESLint:** Use the built-in `eslint-plugin-jsx-a11y` plugin to catch accessibility issues early.


### Security
  * **Tainting:** Prevent sensitive data from being exposed to the client by tainting data objects and/or specific values.
  * **Server Actions:** Ensure users are authorized to call Server Actions. Review the recommended security practices.


  * **Environment Variables:** Ensure your `.env.*` files are added to `.gitignore` and only public variables are prefixed with `NEXT_PUBLIC_`.
  * **Content Security Policy:** Consider adding a Content Security Policy to protect your application against various security threats such as cross-site scripting, clickjacking, and other code injection attacks.


### Metadata and SEO
  * **Metadata API:** Use the Metadata API to improve your application's Search Engine Optimization (SEO) by adding page titles, descriptions, and more.
  * **Open Graph (OG) images:** Create OG images to prepare your application for social sharing.
  * **Sitemaps and Robots:** Help Search Engines crawl and index your pages by generating sitemaps and robots files.


### Type safety
  * **TypeScript andTS Plugin:** Use TypeScript and the TypeScript plugin for better type-safety, and to help you catch errors early.


## Before going to production
Before going to production, you can run `next build` to build your application locally and catch any build errors, then run `next start` to measure the performance of your application in a production-like environment.
### Core Web Vitals
  * **:** Run lighthouse in incognito to gain a better understanding of how your users will experience your site, and to identify areas for improvement. This is a simulated test and should be paired with looking at field data (such as Core Web Vitals).


  * **`useReportWebVitals`hook:** Use this hook to send data to analytics tools.


### Analyzing bundles
Use the `@next/bundle-analyzer` plugin to analyze the size of your JavaScript bundles and identify large modules and dependencies that might be impacting your application's performance.
Additionally, the following tools can help you understand the impact of adding new dependencies to your application:
