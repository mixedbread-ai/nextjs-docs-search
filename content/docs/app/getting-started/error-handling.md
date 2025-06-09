---
title: "How to handle errors"
path: "App / Getting Started / Error Handling"
source_url: https://nextjs.org/docs/app/getting-started/error-handling
content_length: 4581
---

# How to handle errors
Errors can be divided into two categories: expected errors and uncaught exceptions. This page will walk you through how you can handle these errors in your Next.js application.
## Handling expected errors
Expected errors are those that can occur during the normal operation of the application, such as those from server-side form validation or failed requests. These errors should be handled explicitly and returned to the client.
### Server Functions
You can use the hook to handle expected errors in .
For these errors, avoid using `try`/`catch` blocks and throw errors. Instead, model expected errors as return values.
app/actions.ts
```
'use server'
exportasyncfunctioncreatePost(prevState:any, formData:FormData) {
consttitle=formData.get('title')
constcontent=formData.get('content')
constres=awaitfetch(' {
  method:'POST',
  body: { title, content },
 })
constjson=awaitres.json()
if (!res.ok) {
return { message:'Failed to create post' }
 }
}
```

You can pass your action to the `useActionState` hook and use the returned `state` to display an error message.
app/ui/form.tsx
```
'use client'
import { useActionState } from'react'
import { createPost } from'@/app/actions'
constinitialState= {
 message:'',
}
exportfunctionForm() {
const [state,formAction,pending] =useActionState(createPost, initialState)
return (
  <formaction={formAction}>
   <labelhtmlFor="title">Title</label>
   <inputtype="text"id="title"name="title"required />
   <labelhtmlFor="content">Content</label>
   <textareaid="content"name="content"required />
   {state?.message && <paria-live="polite">{state.message}</p>}
   <buttondisabled={pending}>Create Post</button>
  </form>
 )
}
```

### Server Components
When fetching data inside of a Server Component, you can use the response to conditionally render an error message or `redirect`.
app/page.tsx
```
exportdefaultasyncfunctionPage() {
constres=awaitfetch(``)
constdata=awaitres.json()
if (!res.ok) {
return'There was an error.'
 }
return'...'
}
```

### Not found
You can call the `notFound` function within a route segment and use the `not-found.js` file to show a 404 UI.
app/blog/[slug]/page.tsx
```
import { getPostBySlug } from'@/lib/posts'
exportdefaultasyncfunctionPage({ params }: { params: { slug:string } }) {
const { slug } =await params
constpost=getPostBySlug(slug)
if (!post) {
notFound()
 }
return <div>{post.title}</div>
}
```

app/blog/[slug]/not-found.tsx
```
exportdefaultfunctionNotFound() {
return <div>404 - Page Not Found</div>
}
```

## Handling uncaught exceptions
Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.
### Nested error boundaries
Next.js uses error boundaries to handle uncaught exceptions. Error boundaries catch errors in their child components and display a fallback UI instead of the component tree that crashed.
Create an error boundary by adding an `error.js` file inside a route segment and exporting a React component:
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

Errors will bubble up to the nearest parent error boundary. This allows for granular error handling by placing `error.tsx` files at different levels in the route hierarchy.
!Nested Error Component Hierarchy!Nested Error Component Hierarchy
### Global errors
While less common, you can handle errors in the root layout using the `global-error.js` file, located in the root app directory, even when leveraging internationalization. Global error UI must define its own `<html>` and `<body>` tags, since it is replacing the root layout or template when active.
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
