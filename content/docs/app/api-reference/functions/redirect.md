---
title: Redirect
path: "App / Api Reference / Functions / Redirect"
source_url: https://nextjs.org/docs/app/api-reference/functions/redirect
content_length: 4532
---

# redirect
The `redirect` function allows you to redirect the user to another URL. `redirect` can be used in Server Components, Route Handlers, and Server Actions.
When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.
If a resource doesn't exist, you can use the `notFound` function instead.
> **Good to know** :
>   * In Server Actions and Route Handlers, `redirect` should be called after the `try/catch` block.
>   * If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the `permanentRedirect` function instead.
> 

## Parameters
The `redirect` function accepts two arguments:
```
redirect(path, type)
```

Parameter| Type| Description  
---|---|---  
`path`| `string`| The URL to redirect to. Can be a relative or absolute path.  
`type`| `'replace'` (default) or `'push'` (default in Server Actions)| The type of redirect to perform.  
By default, `redirect` will use `push` (adding a new entry to the browser history stack) in Server Actions and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.
The `type` parameter has no effect when used in Server Components.
## Returns
`redirect` does not return a value.
## Example
### Server Component
Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.
app/team/[id]/page.tsx
```
import { redirect } from'next/navigation'
asyncfunctionfetchTeam(id:string) {
constres=awaitfetch('
if (!res.ok) returnundefined
returnres.json()
}
exportdefaultasyncfunctionProfile({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
constteam=awaitfetchTeam(id)
if (!team) {
redirect('/login')
 }
// ...
}
```

> **Good to know** : `redirect` does not require you to use `return redirect()` as it uses the TypeScript type.
### Client Component
`redirect` can be directly used in a Client Component.
components/client-redirect.tsx
```
'use client'
import { redirect, usePathname } from'next/navigation'
exportfunctionClientRedirect() {
constpathname=usePathname()
if (pathname.startsWith('/admin') &&!pathname.includes('/login')) {
redirect('/admin/login')
 }
return <div>Login Page</div>
}
```

> **Good to know** : When using `redirect` in a Client Component on initial page load during Server-Side Rendering (SSR), it will perform a server-side redirect.
`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the `useRouter` hook.
app/client-redirect.tsx
```
'use client'
import { navigate } from'./actions'
exportfunctionClientRedirect() {
return (
  <formaction={navigate}>
   <inputtype="text"name="id" />
   <button>Submit</button>
  </form>
 )
}
```

app/actions.ts
```
'use server'
import { redirect } from'next/navigation'
exportasyncfunctionnavigate(data:FormData) {
redirect(`/posts/${data.get('id')}`)
}
```

## FAQ
### Why does `redirect` use 307 and 308?
When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.
Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.
The introduction of the `307` status code means that the request method is preserved as `POST`.
  * `302` - Temporary redirect, will change the request method from `POST` to `GET`
  * `307` - Temporary redirect, will preserve the request method as `POST`


The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will _always_ be preserved as `POST` requests.
about HTTP Redirects.
## Version History
Version| Changes  
---|---  
`v13.0.0`| `redirect` introduced.
