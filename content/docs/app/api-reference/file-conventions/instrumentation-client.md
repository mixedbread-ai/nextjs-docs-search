---
title: Instrumentation-client.js
path: "App / Api Reference / File Conventions / Instrumentation Client"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client
content_length: 929
---

# instrumentation-client.js
The `instrumentation-client.js|ts` file allows you to add monitoring and analytics code that runs before your application's frontend code starts executing. This is useful for setting up performance tracking, error monitoring, or any other client-side observability tools.
To use it, place the file in the **root** of your application or inside a `src` folder.
## Usage
Unlike server-side instrumentation, you do not need to export any specific functions. You can write your monitoring code directly in the file:
instrumentation-client.ts
```
// Set up performance monitoring
performance.mark('app-init')
// Initialize analytics
console.log('Analytics initialized')
// Set up error tracking
window.addEventListener('error', (event) => {
// Send to your error tracking service
reportError(event.error)
})
```

## Version History
Version| Changes  
---|---  
`v15.3`| `instrumentation-client` introduced
