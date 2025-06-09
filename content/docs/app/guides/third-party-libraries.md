---
title: "How to optimize third-party libraries"
path: "App / Guides / Third Party Libraries"
source_url: https://nextjs.org/docs/app/guides/third-party-libraries
content_length: 8143
---

# How to optimize third-party libraries
**`@next/third-parties`**is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application.
All third-party integrations provided by `@next/third-parties` have been optimized for performance and ease of use.
## Getting Started
To get started, install the `@next/third-parties` library:
Terminal
```
npminstall@next/third-parties@latestnext@latest
```

`@next/third-parties` is currently an **experimental** library under active development. We recommend installing it with the **latest** or **canary** flags while we work on adding more third-party integrations.
## Google Third-Parties
All supported third-party libraries from Google can be imported from `@next/third-parties/google`.
### Google Tag Manager
The `GoogleTagManager` component can be used to instantiate a container to your page. By default, it fetches the original inline script after hydration occurs on the page.
To load Google Tag Manager for all routes, include the component directly in your root layout and pass in your GTM container ID:
app/layout.tsx
```
import { GoogleTagManager } from'@next/third-parties/google'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <GoogleTagManagergtmId="GTM-XYZ" />
   <body>{children}</body>
  </html>
 )
}
```

To load Google Tag Manager for a single route, include the component in your page file:
app/page.js
```
import { GoogleTagManager } from'@next/third-parties/google'
exportdefaultfunctionPage() {
return <GoogleTagManagergtmId="GTM-XYZ" />
}
```

#### Sending Events
The `sendGTMEvent` function can be used to track user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleTagManager />` component must be included in either a parent layout, page, or component, or directly in the same file.
app/page.js
```
'use client'
import { sendGTMEvent } from'@next/third-parties/google'
exportfunctionEventButton() {
return (
  <div>
   <button
onClick={() =>sendGTMEvent({ event:'buttonClicked', value:'xyz' })}
   >
    Send Event
   </button>
  </div>
 )
}
```

Refer to the Tag Manager to learn about the different variables and events that can be passed into the function.
#### Server-side Tagging
If you're using a server-side tag manager and serving `gtm.js` scripts from your tagging server you can use `gtmScriptUrl` option to specify the URL of the script.
#### Options
Options to pass to the Google Tag Manager. For a full list of options, read the .
Name| Type| Description  
---|---|---  
`gtmId`| Required| Your GTM container ID. Usually starts with `GTM-`.  
`gtmScriptUrl`| Optional| GTM script URL. Defaults to ``.  
`dataLayer`| Optional| Data layer object to instantiate the container with.  
`dataLayerName`| Optional| Name of the data layer. Defaults to `dataLayer`.  
`auth`| Optional| Value of authentication parameter (`gtm_auth`) for environment snippets.  
`preview`| Optional| Value of preview parameter (`gtm_preview`) for environment snippets.  
### Google Analytics
The `GoogleAnalytics` component can be used to include to your page via the Google tag (`gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.
> **Recommendation** : If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the to learn more about the differences between Tag Manager and `gtag.js`.
To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:
app/layout.tsx
```
import { GoogleAnalytics } from'@next/third-parties/google'
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <body>{children}</body>
   <GoogleAnalyticsgaId="G-XYZ" />
  </html>
 )
}
```

To load Google Analytics for a single route, include the component in your page file:
app/page.js
```
import { GoogleAnalytics } from'@next/third-parties/google'
exportdefaultfunctionPage() {
return <GoogleAnalyticsgaId="G-XYZ" />
}
```

#### Sending Events
The `sendGAEvent` function can be used to measure user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleAnalytics />` component must be included in either a parent layout, page, or component, or directly in the same file.
app/page.js
```
'use client'
import { sendGAEvent } from'@next/third-parties/google'
exportfunctionEventButton() {
return (
  <div>
   <button
onClick={() =>sendGAEvent('event','buttonClicked', { value:'xyz' })}
   >
    Send Event
   </button>
  </div>
 )
}
```

Refer to the Google Analytics to learn more about event parameters.
#### Tracking Pageviews
Google Analytics automatically tracks pageviews when the browser history state changes. This means that client-side navigations between Next.js routes will send pageview data without any configuration.
To ensure that client-side navigations are being measured correctly, verify that the property is enabled in your Admin panel and the _“Page changes based on browser history events”_ checkbox is selected.
> **Note** : If you decide to manually send pageview events, make sure to disable the default pageview measurement to avoid having duplicate data. Refer to the Google Analytics to learn more.
#### Options
Options to pass to the `<GoogleAnalytics>` component.
Name| Type| Description  
---|---|---  
`gaId`| Required| Your . Usually starts with `G-`.  
`dataLayerName`| Optional| Name of the data layer. Defaults to `dataLayer`.  
`nonce`| Optional| A nonce.  
### Google Maps Embed
The `GoogleMapsEmbed` component can be used to add a to your page. By default, it uses the `loading` attribute to lazy-load the embed below the fold.
app/page.js
```
import { GoogleMapsEmbed } from'@next/third-parties/google'
exportdefaultfunctionPage() {
return (
  <GoogleMapsEmbed
apiKey="XYZ"
height={200}
width="100%"
mode="place"
q="Brooklyn+Bridge,New+York,NY"
  />
 )
}
```

#### Options
Options to pass to the Google Maps Embed. For a full list of options, read the .
Name| Type| Description  
---|---|---  
`apiKey`| Required| Your api key.  
`mode`| Required|   
`height`| Optional| Height of the embed. Defaults to `auto`.  
`width`| Optional| Width of the embed. Defaults to `auto`.  
`style`| Optional| Pass styles to the iframe.  
`allowfullscreen`| Optional| Property to allow certain map parts to go full screen.  
`loading`| Optional| Defaults to lazy. Consider changing if you know your embed will be above the fold.  
`q`| Optional| Defines map marker location. _This may be required depending on the map mode_.  
`center`| Optional| Defines the center of the map view.  
`zoom`| Optional| Sets initial zoom level of the map.  
`maptype`| Optional| Defines type of map tiles to load.  
`language`| Optional| Defines the language to use for UI elements and for the display of labels on map tiles.  
`region`| Optional| Defines the appropriate borders and labels to display, based on geo-political sensitivities.  
### YouTube Embed
The `YouTubeEmbed` component can be used to load and display a YouTube embed. This component loads faster by using under the hood.
app/page.js
```
import { YouTubeEmbed } from'@next/third-parties/google'
exportdefaultfunctionPage() {
return <YouTubeEmbedvideoid="ogfYd705cRs"height={400} params="controls=0" />
}
```

#### Options
Name| Type| Description  
---|---|---  
`videoid`| Required| YouTube video id.  
`width`| Optional| Width of the video container. Defaults to `auto`  
`height`| Optional| Height of the video container. Defaults to `auto`  
`playlabel`| Optional| A visually hidden label for the play button for accessibility.  
`params`| Optional| The video player params defined . Params are passed as a query param string. Eg: `params="controls=0&start=10&end=30"`  
`style`| Optional| Used to apply styles to the video container.
