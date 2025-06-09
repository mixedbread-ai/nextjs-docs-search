---
title: DevIndicators
path: "App / Api Reference / Config / Next Config Js / Devindicators"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators
content_length: 1756
---

# devIndicators
`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.
Types
```
 devIndicators:false| {
  position?:'bottom-right'
|'bottom-left'
|'top-right'
|'top-left',// defaults to 'bottom-left',
 },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.
## Troubleshooting
### Indicator not marking a route as static
If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.
You can confirm if a route is static or dynamic by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:
Build Output
```
Route (app)               Size   First Load JS
┌○/_not-found0B0kB
└ƒ/products/[id]0B0kB
○ (Static)  prerendered as static content
ƒ (Dynamic) server-rendered on demand
```

There are two reasons a route might opt out of static rendering:
  * The presence of Dynamic APIs which rely on runtime information.
  * An uncached data request, like a call to an ORM or database driver.


Check your route for any of these conditions, and if you are not able to statically render the route, then consider using `loading.js` or to leverage streaming.
## Version History
Version| Changes  
---|---  
`v15.2.0`| Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated.  
`v15.0.0`| Static on-screen indicator added with `appIsrStatus` option.
