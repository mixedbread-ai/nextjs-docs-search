---
title: ReactMaxHeadersLength
path: "App / Api Reference / Config / Next Config Js / Reactmaxheaderslength"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength
content_length: 755
---

# reactMaxHeadersLength
During static rendering, React can emit headers that can be added to the response. These can be used to improve performance by allowing the browser to preload resources like fonts, scripts, and stylesheets. The default value is `6000`, but you can override this value by configuring the `reactMaxHeadersLength` option in `next.config.js`:
next.config.js
```
module.exports= {
 reactMaxHeadersLength:1000,
}
```

> **Good to know** : This option is only available in App Router.
Depending on the type of proxy between the browser and the server, the headers can be truncated. For example, if you are using a reverse proxy that doesn't support long headers, you should set a lower value to ensure that the headers are not truncated.
