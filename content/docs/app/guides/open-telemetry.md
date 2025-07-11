---
title: "How to set up instrumentation with OpenTelemetry"
path: "App / Guides / Open Telemetry"
source_url: https://nextjs.org/docs/app/guides/open-telemetry
content_length: 10089
---

# How to set up instrumentation with OpenTelemetry
Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app.
As applications become more complex, it becomes increasingly difficult to identify and diagnose issues that may arise. By leveraging observability tools, such as logging and metrics, developers can gain insights into their application's behavior and identify areas for optimization. With observability, developers can proactively address issues before they become major problems and provide a better user experience. Therefore, it is highly recommended to use observability in your Next.js applications to improve performance, optimize resources, and enhance user experience.
We recommend using OpenTelemetry for instrumenting your apps. It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code. Read for more information about OpenTelemetry and how it works.
This documentation uses terms like _Span_ , _Trace_ or _Exporter_ throughout this doc, all of which can be found in .
Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.
## Getting Started
OpenTelemetry is extensible but setting it up properly can be quite verbose. That's why we prepared a package `@vercel/otel` that helps you get started quickly.
### Using `@vercel/otel`
To get started, install the following packages:
Terminal
```
npminstall@vercel/otel@opentelemetry/sdk-logs@opentelemetry/api-logs@opentelemetry/instrumentation
```

Next, create a custom `instrumentation.ts` (or `.js`) file in the **root directory** of the project (or inside `src` folder if using one):
your-project/instrumentation.ts
```
import { registerOTel } from'@vercel/otel'
exportfunctionregister() {
registerOTel({ serviceName:'next-app' })
}
```

See the for additional configuration options.
> **Good to know** :
>   * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
>   * If you use the `pageExtensions` config option to add a suffix, you will also need to update the `instrumentation` filename to match.
>   * We have created a basic example that you can use.
> 

### Manual OpenTelemetry configuration
The `@vercel/otel` package provides many configuration options and should serve most of common use cases. But if it doesn't suit your needs, you can configure OpenTelemetry manually.
Firstly you need to install OpenTelemetry packages:
Terminal
```
npminstall@opentelemetry/sdk-node@opentelemetry/resources@opentelemetry/semantic-conventions@opentelemetry/sdk-trace-node@opentelemetry/exporter-trace-otlp-http
```

Now you can initialize `NodeSDK` in your `instrumentation.ts`. Unlike `@vercel/otel`, `NodeSDK` is not compatible with edge runtime, so you need to make sure that you are importing them only when `process.env.NEXT_RUNTIME === 'nodejs'`. We recommend creating a new file `instrumentation.node.ts` which you conditionally import only when using node:
instrumentation.ts
```
exportasyncfunctionregister() {
if (process.env.NEXT_RUNTIME==='nodejs') {
awaitimport('./instrumentation.node.ts')
 }
}
```

instrumentation.node.ts
```
import { OTLPTraceExporter } from'@opentelemetry/exporter-trace-otlp-http'
import { Resource } from'@opentelemetry/resources'
import { NodeSDK } from'@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from'@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from'@opentelemetry/semantic-conventions'
constsdk=newNodeSDK({
 resource:newResource({
  [ATTR_SERVICE_NAME]:'next-app',
 }),
 spanProcessor:newSimpleSpanProcessor(newOTLPTraceExporter()),
})
sdk.start()
```

Doing this is equivalent to using `@vercel/otel`, but it's possible to modify and extend some features that are not exposed by the `@vercel/otel`. If edge runtime support is necessary, you will have to use `@vercel/otel`.
## Testing your instrumentation
You need an OpenTelemetry collector with a compatible backend to test OpenTelemetry traces locally. We recommend using our .
If everything works well you should be able to see the root server span labeled as `GET /requested/pathname`. All other spans from that particular trace will be nested under it.
Next.js traces more spans than are emitted by default. To see more spans, you must set `NEXT_OTEL_VERBOSE=1`.
## Deployment
### Using OpenTelemetry Collector
When you are deploying with OpenTelemetry Collector, you can use `@vercel/otel`. It will work both on Vercel and when self-hosted.
#### Deploying on Vercel
We made sure that OpenTelemetry works out of the box on Vercel.
Follow to connect your project to an observability provider.
#### Self-hosting
Deploying to other platforms is also straightforward. You will need to spin up your own OpenTelemetry Collector to receive and process the telemetry data from your Next.js app.
To do this, follow the , which will walk you through setting up the collector and configuring it to receive data from your Next.js app.
Once you have your collector up and running, you can deploy your Next.js app to your chosen platform following their respective deployment guides.
### Custom Exporters
OpenTelemetry Collector is not necessary. You can use a custom OpenTelemetry exporter with `@vercel/otel` or manual OpenTelemetry configuration.
## Custom Spans
You can add a custom span with .
Terminal
```
npminstall@opentelemetry/api
```

The following example demonstrates a function that fetches GitHub stars and adds a custom `fetchGithubStars` span to track the fetch request's result:
```
import { trace } from'@opentelemetry/api'
exportasyncfunctionfetchGithubStars() {
returnawait trace
.getTracer('nextjs-example')
.startActiveSpan('fetchGithubStars',async (span) => {
try {
returnawaitgetValue()
   } finally {
span.end()
   }
  })
}
```

The `register` function will execute before your code runs in a new environment. You can start creating new spans, and they should be correctly added to the exported trace.
## Default Spans in Next.js
Next.js automatically instruments several spans for you to provide useful insights into your application's performance.
Attributes on spans follow . We also add some custom attributes under the `next` namespace:
  * `next.span_name` - duplicates span name
  * `next.span_type` - each span type has a unique identifier
  * `next.route` - The route pattern of the request (e.g., `/[param]/user`).
  * `next.rsc` (true/false) - Whether the request is an RSC request, such as prefetch.
  * `next.page`
    * This is an internal value used by an app router.
    * You can think about it as a route to a special file (like `page.ts`, `layout.ts`, `loading.ts` and others)
    * It can be used as a unique identifier only when paired with `next.route` because `/layout` can be used to identify both `/(groupA)/layout.ts` and `/(groupB)/layout.ts`


### [`[http.method] [next.route]`](
  * `next.span_type`: `BaseServer.handleRequest`


This span represents the root span for each incoming request to your Next.js application. It tracks the HTTP method, route, target, and status code of the request.
Attributes:
  *     * `http.method`
    * `http.status_code`
  *     * `http.route`
    * `http.target`
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`render route (app) [next.route]`](
  * `next.span_type`: `AppRender.getBodyResult`.


This span represents the process of rendering a route in the app router.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`fetch [http.method] [http.url]`](
  * `next.span_type`: `AppRender.fetch`


This span represents the fetch request executed in your code.
Attributes:
  *     * `http.method`
  *     * `http.url`
    * `net.peer.name`
    * `net.peer.port` (only if specified)
  * `next.span_name`
  * `next.span_type`


This span can be turned off by setting `NEXT_OTEL_FETCH_DISABLED=1` in your environment. This is useful when you want to use a custom fetch instrumentation library.
### [`executing api route (app) [next.route]`](
  * `next.span_type`: `AppRouteRouteHandlers.runHandler`.


This span represents the execution of an API Route Handler in the app router.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`getServerSideProps [next.route]`](
  * `next.span_type`: `Render.getServerSideProps`.


This span represents the execution of `getServerSideProps` for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`getStaticProps [next.route]`](
  * `next.span_type`: `Render.getStaticProps`.


This span represents the execution of `getStaticProps` for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`render route (pages) [next.route]`](
  * `next.span_type`: `Render.renderDocument`.


This span represents the process of rendering the document for a specific route.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### [`generateMetadata [next.page]`](
  * `next.span_type`: `ResolveMetadata.generateMetadata`.


This span represents the process of generating metadata for a specific page (a single route can have multiple of these spans).
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.page`


### `resolve page components`
  * `next.span_type`: `NextNodeServer.findPageComponents`.


This span represents the process of resolving page components for a specific page.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.route`


### `resolve segment modules`
  * `next.span_type`: `NextNodeServer.getLayoutOrPageModule`.


This span represents loading of code modules for a layout or a page.
Attributes:
  * `next.span_name`
  * `next.span_type`
  * `next.segment`


### `start response`
  * `next.span_type`: `NextNodeServer.startResponse`.


This zero-length span represents the time when the first byte has been sent in the response.
