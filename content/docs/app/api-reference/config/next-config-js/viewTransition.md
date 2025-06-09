---
title: ViewTransition
path: "App / Api Reference / Config / Next Config Js / Viewtransition"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition
content_length: 1644
---

# viewTransition
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
`viewTransition` is an experimental flag that enables the new experimental in React. This API allows you to leverage the native View Transitions browser API to create seamless transitions between UI states.
To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 experimental: {
  viewTransition:true,
 },
}
module.exports= nextConfig
```

> Important Notice: This feature is not developed or maintained by the Next.js team — it is an experimental API from the React team. It is still in **early stages** and **not recommended for production use**. The implementation is still being iterated on, and its behavior may change in future React releases. Enabling this feature requires understanding the experimental nature of the API. To fully grasp its behavior, refer to the and related discussions.
## Usage
Once enabled, you can import the `ViewTransition` component from React in your application:
```
import { unstable_ViewTransition as ViewTransition } from'react'
```

However, documentation and examples are currently limited, and you will need to refer directly to React’s source code and discussions to understand how this works.
### Live Demo
Check out our to see this feature in action.
As this API evolves, we will update our documentation and share more examples. However, for now, we strongly advise against using this feature in production.
