---
title: "How to update data"
path: "App / Getting Started / Updating Data"
source_url: https://nextjs.org/docs/app/getting-started/updating-data
content_length: 4836
---

# How to update data
You can update data in Next.js using React's . This page will go through how you can create and invoke Server Functions.
## Server Functions
A Server Function is an asynchronous function that is executed on the server. Server Functions are inherently asynchronous because they are invoked by the client using a network request. When invoked as part of an `action`, they are also called **Server Actions**.
By convention, an `action` is an asynchronous function passed to `startTransition`. Server Functions are automatically wrapped with `startTransition` when:
  * Passed to a `<form>` using the `action` prop,
  * Passed to a `<button>` using the `formAction` prop
  * Passed to `useActionState`


## Creating Server Functions
A Server Function can be defined by using the directive. You can place the directive at the top of an **asynchronous** function to mark the function as a Server Function, or at the top of a separate file to mark all exports of that file.
app/lib/actions.ts
```
exportasyncfunctioncreatePost(formData:FormData) {
'use server'
consttitle=formData.get('title')
constcontent=formData.get('content')
// Update data
// Revalidate cache
}
exportasyncfunctiondeletePost(formData:FormData) {
'use server'
constid=formData.get('id')
// Update data
// Revalidate cache
}
```

### Server Components
Server Functions can be inlined in Server Components by adding the `"use server"` directive to the top of the function body:
app/page.tsx
```
exportdefaultfunctionPage() {
// Server Action
asyncfunctioncreatePost(formData:FormData) {
'use server'
// ...
 }
return <></>
}
```

### Client Components
It's not possible to define Server Functions in Client Components. However, you can invoke them in Client Components by importing them from a file that has the `"use server"` directive at the top of it:
app/actions.ts
```
'use server'
exportasyncfunctioncreatePost() {}
```

app/ui/button.tsx
```
'use client'
import { createPost } from'@/app/actions'
exportfunctionButton() {
return <buttonformAction={createPost}>Create</button>
}
```

## Invoking Server Functions
There are two main ways you can invoke a Server Function:
  1. Forms in Server and Client Components
  2. Event Handlers in Client Components


### Forms
React extends the HTML element to allow Server Function to be invoked with the HTML `action` prop.
When invoked in a form, the function automatically receives the object. You can extract the data using the native :
app/ui/form.tsx
```
import { createPost } from'@/app/actions'
exportfunctionForm() {
return (
  <formaction={createPost}>
   <inputtype="text"name="title" />
   <inputtype="text"name="content" />
   <buttontype="submit">Create</button>
  </form>
 )
}
```

app/actions.ts
```
'use server'
exportasyncfunctioncreatePost(formData:FormData) {
consttitle=formData.get('title')
constcontent=formData.get('content')
// Update data
// Revalidate cache
}
```

> **Good to know:** When passed to the `action` prop, Server Functions are also known as _Server Actions_.
### Event Handlers
You can invoke a Server Function in a Client Component by using event handlers such as `onClick`.
app/like-button.tsx
```
'use client'
import { incrementLike } from'./actions'
import { useState } from'react'
exportdefaultfunctionLikeButton({ initialLikes }: { initialLikes:number }) {
const [likes,setLikes] =useState(initialLikes)
return (
  <>
   <p>Total Likes: {likes}</p>
   <button
onClick={async () => {
constupdatedLikes=awaitincrementLike()
setLikes(updatedLikes)
    }}
   >
    Like
   </button>
  </>
 )
}
```

## Examples
### Showing a pending state
While executing a Server Function, you can show a loading indicator with React's hook. This hook returns a `pending` boolean:
app/ui/button.tsx
```
'use client'
import { useActionState } from'react'
import { createPost } from'@/app/actions'
import { LoadingSpinner } from'@/app/ui/loading-spinner'
exportfunctionButton() {
const [state,action,pending] =useActionState(createPost,false)
return (
  <buttononClick={async () =>action()}>
   {pending ? <LoadingSpinner /> :'Create Post'}
  </button>
 )
}
```

### Revalidating the cache
After performing an update, you can revalidate the Next.js cache and show the updated data by calling `revalidatePath` or `revalidateTag` within the Server Function:
app/lib/actions.ts
```
import { revalidatePath } from'next/cache'
exportasyncfunctioncreatePost(formData:FormData) {
'use server'
// Update data
// ...
revalidatePath('/posts')
}
```

### Redirecting
You may want to redirect the user to a different page after performing an update. You can do this by calling `redirect` within the Server Function:
app/lib/actions.ts
```
'use server'
import { redirect } from'next/navigation'
exportasyncfunctioncreatePost(formData:FormData) {
// Update data
// ...
redirect('/posts')
}
```
