---
title: Forbidden.js
path: "App / Api Reference / File Conventions / Forbidden"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/forbidden
content_length: 745
---

# forbidden.js
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
The **forbidden** file is used to render UI when the `forbidden` function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.
app/forbidden.tsx
```
import Link from'next/link'
exportdefaultfunctionForbidden() {
return (
  <div>
   <h2>Forbidden</h2>
   <p>You are not authorized to access this resource.</p>
   <Linkhref="/">Return Home</Link>
  </div>
 )
}
```

## Reference
### Props
`forbidden.js` components do not accept any props.
## Version History
Version| Changes  
---|---  
`v15.1.0`| `forbidden.js` introduced.
