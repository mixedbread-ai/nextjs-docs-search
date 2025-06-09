---
title: UseReportWebVitals
path: "App / Api Reference / Functions / Use Report Web Vitals"
source_url: https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals
content_length: 4211
---

# useReportWebVitals
The `useReportWebVitals` hook allows you to report , and can be used in combination with your analytics service.
New functions passed to `useReportWebVitals` are called with the available metrics up to that point. To prevent reporting duplicated data, ensure that the callback function reference does not change (as shown in the code examples below).
app/_components/web-vitals.js
```
'use client'
import { useReportWebVitals } from'next/web-vitals'
constlogWebVitals= (metric) => {
console.log(metric)
}
exportfunctionWebVitals() {
useReportWebVitals(logWebVitals)
returnnull
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
## useReportWebVitals
The `metric` object passed as the hook's argument consists of a number of properties:
  * `id`: Unique identifier for the metric in the context of the current page load
  * `name`: The name of the performance metric. Possible values include names of Web Vitals metrics (TTFB, FCP, LCP, FID, CLS) specific to a web application.
  * `delta`: The difference between the current value and the previous value of the metric. The value is typically in milliseconds and represents the change in the metric's value over time.
  * `entries`: An array of associated with the metric. These entries provide detailed information about the performance events related to the metric.
  * `navigationType`: Indicates the that triggered the metric collection. Possible values include `"navigate"`, `"reload"`, `"back_forward"`, and `"prerender"`.
  * `rating`: A qualitative rating of the metric value, providing an assessment of the performance. Possible values are `"good"`, `"needs-improvement"`, and `"poor"`. The rating is typically determined by comparing the metric value against predefined thresholds that indicate acceptable or suboptimal performance.
  * `value`: The actual value or duration of the performance entry, typically in milliseconds. The value provides a quantitative measure of the performance aspect being tracked by the metric. The source of the value depends on the specific metric being measured and can come from various s.


## Web Vitals
are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:
  * (TTFB)
  * (FCP)
  * (LCP)
  * (FID)
  * (CLS)
  * (INP)


You can handle all the results of these metrics using the `name` property.
app/components/web-vitals.tsx
```
'use client'
import { useReportWebVitals } from'next/web-vitals'
typeReportWebVitalsCallback=Parameters<typeof useReportWebVitals>[0]
consthandleWebVitals:ReportWebVitalsCallback= (metric) => {
switch (metric.name) {
case'FCP': {
// handle FCP results
  }
case'LCP': {
// handle LCP results
  }
// ...
 }
}
exportfunctionWebVitals() {
useReportWebVitals(handleWebVitals)
}
```

## Sending results to external systems
You can send results to any endpoint to measure and track real user performance on your site. For example:
```
functionpostWebVitals(metrics) {
constbody=JSON.stringify(metric)
consturl='
// Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
if (navigator.sendBeacon) {
navigator.sendBeacon(url, body)
 } else {
fetch(url, { body, method:'POST', keepalive:true })
 }
}
useReportWebVitals(postWebVitals)
```

> **Good to know** : If you use , using the `id` value can allow you to construct metric distributions manually (to calculate percentiles, etc.)
> ```
useReportWebVitals(metric => {
// Use `window.gtag` if you initialized Google Analytics as this example:
// 
window.gtag('event',metric.name, {
  value:Math.round(metric.name ==='CLS'?metric.value *1000:metric.value),// values must be integers
  event_label:metric.id,// id unique to current page load
  non_interaction:true,// avoids affecting bounce rate.
 });
}
```

> Read more about .
