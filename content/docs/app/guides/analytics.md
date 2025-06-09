---
title: "How to add analytics to your Next.js application"
path: "App / Guides / Analytics"
source_url: https://nextjs.org/docs/app/guides/analytics
content_length: 3231
---

# How to add analytics to your Next.js application
Next.js has built-in support for measuring and reporting performance metrics. You can either use the `useReportWebVitals` hook to manage reporting yourself, or alternatively, Vercel provides a to automatically collect and visualize metrics for you.
## Client Instrumentation
For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.
To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:
instrumentation-client.js
```
// Initialize analytics before the app starts
console.log('Analytics initialized')
// Set up global error tracking
window.addEventListener('error', (event) => {
// Send to your error tracking service
reportError(event.error)
})
```

## Build Your Own
app/_components/web-vitals.js
```
'use client'
import { useReportWebVitals } from'next/web-vitals'
exportfunctionWebVitals() {
useReportWebVitals((metric) => {
console.log(metric)
 })
}
```

app/layout.js
```
import { WebVitals } from'./_components/web-vitals'
exportdefaultfunctionLayout({ children }) {
return (
  <html>
   <body>
    <WebVitals />
    {children}
   </body>
  </html>
 )
}
```

> Since the `useReportWebVitals` hook requires the `'use client'` directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the `WebVitals` component.
View the API Reference for more information.
## Web Vitals
are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:
  * (TTFB)
  * (FCP)
  * (LCP)
  * (FID)
  * (CLS)
  * (INP)


You can handle all the results of these metrics using the `name` property.
app/_components/web-vitals.tsx
```
'use client'
import { useReportWebVitals } from'next/web-vitals'
exportfunctionWebVitals() {
useReportWebVitals((metric) => {
switch (metric.name) {
case'FCP': {
// handle FCP results
   }
case'LCP': {
// handle LCP results
   }
// ...
  }
 })
}
```

## Sending results to external systems
You can send results to any endpoint to measure and track real user performance on your site. For example:
```
useReportWebVitals((metric) => {
constbody=JSON.stringify(metric)
consturl='
// Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
if (navigator.sendBeacon) {
navigator.sendBeacon(url, body)
 } else {
fetch(url, { body, method:'POST', keepalive:true })
 }
})
```

> **Good to know** : If you use , using the `id` value can allow you to construct metric distributions manually (to calculate percentiles, etc.)
> ```
useReportWebVitals((metric) => {
// Use `window.gtag` if you initialized Google Analytics as this example:
// 
window.gtag('event',metric.name, {
  value:Math.round(
metric.name ==='CLS'?metric.value *1000:metric.value
  ),// values must be integers
  event_label:metric.id,// id unique to current page load
  non_interaction:true,// avoids affecting bounce rate.
 })
})
```

> Read more about .
