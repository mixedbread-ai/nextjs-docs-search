---
title: Error.js
path: "App / Api Reference / File Conventions / Error"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/error
content_length: 5376
---

# error.js
An **error** file allows you to handle unexpected runtime errors and display fallback UI.
!error.js special file!error.js special file
app/dashboard/error.tsx
```
'use client'// Error boundaries must be Client Components
import { useEffect } from'react'
exportdefaultfunctionError({
 error,
 reset,
}: {
 error:Error& { digest?:string }
reset: () =>void
}) {
useEffect(() => {
// Log the error to an error reporting service
console.error(error)
 }, [error])
return (
  <div>
   <h2>Something went wrong!</h2>
   <button
onClick={
// Attempt to recover by trying to re-render the segment
     () =>reset()
    }
   >
    Try again
   </button>
  </div>
 )
}
```

`error.js` wraps a route segment and its nested children in a . When an error throws within the boundary, the `error` component shows as the fallback UI.
!How error.js works!How error.js works
> **Good to know** :
>   * The allow you to toggle error boundaries to test error states.
>   * If you want errors to bubble up to the parent error boundary, you can `throw` when rendering the `error` component.
> 

## Reference
### Props
#### `error`
An instance of an object forwarded to the `error.js` Client Component.
> **Good to know:** During development, the `Error` object forwarded to the client will be serialized and include the `message` of the original error for easier debugging. However, **this behavior is different in production** to avoid leaking potentially sensitive details included in the error to the client.
#### `error.message`
  * Errors forwarded from Client Components show the original `Error` message.
  * Errors forwarded from Server Components show a generic message with an identifier. This is to prevent leaking sensitive details. You can use the identifier, under `errors.digest`, to match the corresponding server-side logs.


#### `error.digest`
An automatically generated hash of the error thrown. It can be used to match the corresponding error in server-side logs.
#### `reset`
The cause of an error can sometimes be temporary. In these cases, trying again might resolve the issue.
An error component can use the `reset()` function to prompt the user to attempt to recover from the error. When executed, the function will try to re-render the error boundary's contents. If successful, the fallback error component is replaced with the result of the re-render.
app/dashboard/error.tsx
```
'use client'// Error boundaries must be Client Components
exportdefaultfunctionError({
 error,
 reset,
}: {
 error:Error& { digest?:string }
reset: () =>void
}) {
return (
  <div>
   <h2>Something went wrong!</h2>
   <buttononClick={() =>reset()}>Try again</button>
  </div>
 )
}
```

## Examples
### Global Error
While less common, you can handle errors in the root layout or template using `global-error.js`, located in the root app directory, even when leveraging internationalization. Global error UI must define its own `<html>` and `<body>` tags. This file replaces the root layout or template when active.
app/global-error.tsx
```
'use client'// Error boundaries must be Client Components
exportdefaultfunctionGlobalError({
 error,
 reset,
}: {
 error:Error& { digest?:string }
reset: () =>void
}) {
return (
// global-error must include html and body tags
  <html>
   <body>
    <h2>Something went wrong!</h2>
    <buttononClick={() =>reset()}>Try again</button>
   </body>
  </html>
 )
}
```

### Graceful error recovery with a custom error boundary
When rendering fails on the client, it can be useful to show the last known server rendered UI for a better user experience.
The `GracefullyDegradingErrorBoundary` is an example of a custom error boundary that captures and preserves the current HTML before an error occurs. If a rendering error happens, it re-renders the captured HTML and displays a persistent notification bar to inform the user.
app/dashboard/error.tsx
```
'use client'
import React, { Component, ErrorInfo, ReactNode } from'react'
interfaceErrorBoundaryProps {
 children:ReactNode
onError?: (error:Error, errorInfo:ErrorInfo) =>void
}
interfaceErrorBoundaryState {
 hasError:boolean
}
exportclassGracefullyDegradingErrorBoundaryextendsComponent<
ErrorBoundaryProps,
ErrorBoundaryState
> {
private contentRef:React.RefObject<HTMLDivElement>
constructor(props:ErrorBoundaryProps) {
super(props)
this.state = { hasError:false }
this.contentRef =React.createRef()
 }
staticgetDerivedStateFromError(_:Error):ErrorBoundaryState {
return { hasError:true }
 }
componentDidCatch(error:Error, errorInfo:ErrorInfo) {
if (this.props.onError) {
this.props.onError(error, errorInfo)
  }
 }
render() {
if (this.state.hasError) {
// Render the current HTML content without hydration
return (
    <>
     <div
ref={this.contentRef}
suppressHydrationWarning
dangerouslySetInnerHTML={{
       __html:this.contentRef.current?.innerHTML ||'',
      }}
     />
     <divclassName="fixed bottom-0 left-0 right-0 bg-red-600 text-white py-4 px-6 text-center">
      <pclassName="font-semibold">
       An error occurred during page rendering
      </p>
     </div>
    </>
   )
  }
return <divref={this.contentRef}>{this.props.children}</div>
 }
}
exportdefault GracefullyDegradingErrorBoundary
```

## Version History
Version| Changes  
---|---  
`v15.2.0`| Also display `global-error` in development.  
`v13.1.0`| `global-error` introduced.  
`v13.0.0`| `error` introduced.
