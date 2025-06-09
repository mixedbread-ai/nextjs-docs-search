---
title: "Server Actions and Mutations"
path: "App / Building Your Application / Data Fetching / Server Actions And Mutations"
source_url: https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations
content_length: 12832
---

# Server Actions and Mutations
are **asynchronous functions** that are executed on the server. They can be called in Server and Client Components to handle form submissions and data mutations in Next.js applications.
> **🎥 Watch:** Learn more about mutations with Server Actions → .
## Convention
A Server Action can be defined with the React directive. You can place the directive at the top of an `async` function to mark the function as a Server Action, or at the top of a separate file to mark all exports of that file as Server Actions.
### Server Components
Server Components can use the inline function level or module level `"use server"` directive. To inline a Server Action, add `"use server"` to the top of the function body:
app/page.tsx
```
exportdefaultfunctionPage() {
// Server Action
asyncfunctioncreate() {
'use server'
// Mutate data
 }
return'...'
}
```

### Client Components
To call a Server Function in a Client Component, create a new file and add the `"use server"` directive at the top of it. All exported functions within the file will be marked as Server Functions that can be reused in both Client and Server Components:
app/actions.ts
```
'use server'
exportasyncfunctioncreate() {}
```

app/button.tsx
```
'use client'
import { create } from'./actions'
exportfunctionButton() {
return <buttononClick={() =>create()}>Create</button>
}
```

### Passing actions as props
You can also pass a Server Action to a Client Component as a prop:
```
<ClientComponentupdateItemAction={updateItem} />
```

app/client-component.tsx
```
'use client'
exportdefaultfunctionClientComponent({
 updateItemAction,
}: {
updateItemAction: (formData:FormData) =>void
}) {
return <formaction={updateItemAction}>{/* ... */}</form>
}
```

Usually, the Next.js TypeScript plugin would flag `updateItemAction` in `client-component.tsx` since it is a function which generally can't be serialized across client-server boundaries. However, props named `action` or ending with `Action` are assumed to receive Server Actions. This is only a heuristic since the TypeScript plugin doesn't actually know if it receives a Server Action or an ordinary function. Runtime type-checking will still ensure you don't accidentally pass a function to a Client Component.
## Behavior
  * Server actions can be invoked using the `action` attribute in a `<form>` element. 
    * Server Components support progressive enhancement by default, meaning the form will be submitted even if JavaScript hasn't loaded yet or is disabled.
    * In Client Components, forms invoking Server Actions will queue submissions if JavaScript isn't loaded yet, prioritizing client hydration.
    * After hydration, the browser does not refresh on form submission.
  * Server Actions are not limited to `<form>` and can be invoked from event handlers, `useEffect`, third-party libraries, and other form elements like `<button>`.
  * Server Actions integrate with the Next.js caching and revalidation architecture. When an action is invoked, Next.js can return both the updated UI and new data in a single server roundtrip.
  * Behind the scenes, actions use the `POST` method, and only this HTTP method can invoke them.
  * The arguments and return value of Server Actions must be serializable by React. See the React docs for a list of .
  * Server Actions are functions. This means they can be reused anywhere in your application.
  * Server Actions inherit the runtime from the page or layout they are used on.
  * Server Actions inherit the Route Segment Config from the page or layout they are used on, including fields like `maxDuration`.


## Examples
### Event handlers
While it's common to use Server Actions within `<form>` elements, they can also be invoked with event handlers such as `onClick`. For example, to increment a like count:
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

You can also add event handlers to form elements, for example, to save a form field `onChange`:
app/ui/edit-post.tsx
```
'use client'
import { publishPost, saveDraft } from'./actions'
exportdefaultfunctionEditPost() {
return (
  <formaction={publishPost}>
   <textarea
name="content"
onChange={async (e) => {
awaitsaveDraft(e.target.value)
    }}
   />
   <buttontype="submit">Publish</button>
  </form>
 )
}
```

For cases like this, where multiple events might be fired in quick succession, we recommend **debouncing** to prevent unnecessary Server Action invocations.
### `useEffect`
You can use the React hook to invoke a Server Action when the component mounts or a dependency changes. This is useful for mutations that depend on global events or need to be triggered automatically. For example, `onKeyDown` for app shortcuts, an intersection observer hook for infinite scrolling, or when the component mounts to update a view count:
app/view-count.tsx
```
'use client'
import { incrementViews } from'./actions'
import { useState, useEffect, useTransition } from'react'
exportdefaultfunctionViewCount({ initialViews }: { initialViews:number }) {
const [views,setViews] =useState(initialViews)
const [isPending,startTransition] =useTransition()
useEffect(() => {
startTransition(async () => {
constupdatedViews=awaitincrementViews()
setViews(updatedViews)
  })
 }, [])
// You can use `isPending` to give users feedback
return <p>Total Views: {views}</p>
}
```

Remember to consider the of `useEffect`.
### Error Handling
When an error is thrown, it'll be caught by the nearest `error.js` or `<Suspense>` boundary on the client. See Error Handling for more information.
> **Good to know:**
>   * Aside from throwing the error, you can also return an object to be handled by `useActionState`.
> 

### Revalidating data
You can revalidate the Next.js Cache inside your Server Actions with the `revalidatePath` API:
app/actions.ts
```
'use server'
import { revalidatePath } from'next/cache'
exportasyncfunctioncreatePost() {
try {
// ...
 } catch (error) {
// ...
 }
revalidatePath('/posts')
}
```

Or invalidate a specific data fetch with a cache tag using `revalidateTag`:
app/actions.ts
```
'use server'
import { revalidateTag } from'next/cache'
exportasyncfunctioncreatePost() {
try {
// ...
 } catch (error) {
// ...
 }
revalidateTag('posts')
}
```

### Redirecting
If you would like to redirect the user to a different route after the completion of a Server Action, you can use `redirect` API. `redirect` needs to be called outside of the `try/catch` block:
app/actions.ts
```
'use server'
import { redirect } from'next/navigation'
import { revalidateTag } from'next/cache'
exportasyncfunctioncreatePost(id:string) {
try {
// ...
 } catch (error) {
// ...
 }
revalidateTag('posts') // Update cached posts
redirect(`/post/${id}`) // Navigate to the new post page
}
```

### Cookies
You can `get`, `set`, and `delete` cookies inside a Server Action using the `cookies` API:
app/actions.ts
```
'use server'
import { cookies } from'next/headers'
exportasyncfunctionexampleAction() {
constcookieStore=awaitcookies()
// Get cookie
cookieStore.get('name')?.value
// Set cookie
cookieStore.set('name','Delba')
// Delete cookie
cookieStore.delete('name')
}
```

See additional examples for deleting cookies from Server Actions.
## Security
By default, when a Server Action is created and exported, it creates a public HTTP endpoint and should be treated with the same security assumptions and authorization checks. This means, even if a Server Action or utility function is not imported elsewhere in your code, it’s still publicly accessible.
To improve security, Next.js has the following built-in features:
  * **Secure action IDs:** Next.js creates encrypted, non-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.
  * **Dead code elimination:** Unused Server Actions (referenced by their IDs) are removed from client bundle to avoid public access by third-party.


> **Good to know** :
> The IDs are created during compilation and are cached for a maximum of 14 days. They will be regenerated when a new build is initiated or when the build cache is invalidated. This security improvement reduces the risk in cases where an authentication layer is missing. However, you should still treat Server Actions like public HTTP endpoints.
```
// app/actions.js
'use server'
// This action **is** used in our application, so Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
exportasyncfunctionupdateUserAction(formData) {}
// This action **is not** used in our application, so Next.js
// will automatically remove this code during `next build`
// and will not create a public endpoint.
exportasyncfunctiondeleteUserAction(formData) {}
```

### Authentication and authorization
You should ensure that the user is authorized to perform the action. For example:
app/actions.ts
```
'use server'
import { auth } from'./lib'
exportfunctionaddItem() {
const { user } =auth()
if (!user) {
thrownewError('You must be signed in to perform this action')
 }
// ...
}
```

### Closures and encryption
Defining a Server Action inside a component creates a where the action has access to the outer function's scope. For example, the `publish` action has access to the `publishVersion` variable:
app/page.tsx
```
exportdefaultasyncfunctionPage() {
constpublishVersion=awaitgetLatestVersion();
asyncfunctionpublish() {
"use server";
if (publishVersion !==awaitgetLatestVersion()) {
thrownewError('The version has changed since pressing publish');
  }
...
 }
return (
  <form>
   <buttonformAction={publish}>Publish</button>
  </form>
 );
}
```

Closures are useful when you need to capture a _snapshot_ of data (e.g. `publishVersion`) at the time of rendering so that it can be used later when the action is invoked.
However, for this to happen, the captured variables are sent to the client and back to the server when the action is invoked. To prevent sensitive data from being exposed to the client, Next.js automatically encrypts the closed-over variables. A new private key is generated for each action every time a Next.js application is built. This means actions can only be invoked for a specific build.
> **Good to know:** We don't recommend relying on encryption alone to prevent sensitive values from being exposed on the client. Instead, you should use the React taint APIs to proactively prevent specific data from being sent to the client.
### Overwriting encryption keys (advanced)
When self-hosting your Next.js application across multiple servers, each server instance may end up with a different encryption key, leading to potential inconsistencies.
To mitigate this, you can overwrite the encryption key using the `process.env.NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` environment variable. Specifying this variable ensures that your encryption keys are persistent across builds, and all server instances use the same key. This variable **must** be AES-GCM encrypted.
This is an advanced use case where consistent encryption behavior across multiple deployments is critical for your application. You should consider standard security practices such key rotation and signing.
> **Good to know:** Next.js applications deployed to Vercel automatically handle this.
### Allowed origins (advanced)
Since Server Actions can be invoked in a `<form>` element, this opens them up to .
Behind the scenes, Server Actions use the `POST` method, and only this HTTP method is allowed to invoke them. This prevents most CSRF vulnerabilities in modern browsers, particularly with being the default.
As an additional protection, Server Actions in Next.js also compare the to the (or `X-Forwarded-Host`). If these don't match, the request will be aborted. In other words, Server Actions can only be invoked on the same host as the page that hosts it.
For large applications that use reverse proxies or multi-layered backend architectures (where the server API differs from the production domain), it's recommended to use the configuration option `serverActions.allowedOrigins` option to specify a list of safe origins. The option accepts an array of strings.
next.config.js
```
/** @type{import('next').NextConfig} */
module.exports= {
 experimental: {
  serverActions: {
   allowedOrigins: ['my-proxy.com','*.my-proxy.com'],
  },
 },
}
```

Learn more about Security and Server Actions.
## Additional resources
For more information, check out the following React docs:
