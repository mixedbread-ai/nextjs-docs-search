---
title: "Use server"
path: "App / Api Reference / Directives / Use Server"
source_url: https://nextjs.org/docs/app/api-reference/directives/use-server
content_length: 2812
---

# use server
The `use server` directive designates a function or file to be executed on the **server side**. It can be used at the top of a file to indicate that all functions in the file are server-side, or inline at the top of a function to mark the function as a . This is a React feature.
## Using `use server` at the top of a file
The following example shows a file with a `use server` directive at the top. All functions in the file are executed on the server.
app/actions.ts
```
'use server'
import { db } from'@/lib/db'// Your database client
exportasyncfunctioncreateUser(data: { name:string; email:string }) {
constuser=awaitdb.user.create({ data })
return user
}
```

### Using Server Functions in a Client Component
To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the `use server` directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.
Assuming you have a `fetchUsers` Server Function in `actions.ts`:
app/actions.ts
```
'use server'
import { db } from'@/lib/db'// Your database client
exportasyncfunctionfetchUsers() {
constusers=awaitdb.user.findMany()
return users
}
```

Then you can import the `fetchUsers` Server Function into a Client Component and execute it on the client-side.
app/components/my-button.tsx
```
'use client'
import { fetchUsers } from'../actions'
exportdefaultfunctionMyButton() {
return <buttononClick={() =>fetchUsers()}>Fetch Users</button>
}
```

## Using `use server` inline
In the following example, `use server` is used inline at the top of a function to mark it as a :
app/posts/[id]/page.tsx
```
import { EditPost } from'./edit-post'
import { revalidatePath } from'next/cache'
exportdefaultasyncfunctionPostPage({ params }: { params: { id:string } }) {
constpost=awaitgetPost(params.id)
asyncfunctionupdatePost(formData:FormData) {
'use server'
awaitsavePost(params.id, formData)
revalidatePath(`/posts/${params.id}`)
 }
return <EditPostupdatePostAction={updatePost} post={post} />
}
```

## Security considerations
When using the `use server` directive, it's important to ensure that all server-side logic is secure and that sensitive data remains protected.
### Authentication and authorization
Always authenticate and authorize users before performing sensitive server-side operations.
app/actions.ts
```
'use server'
import { db } from'@/lib/db'// Your database client
import { authenticate } from'@/lib/auth'// Your authentication library
exportasyncfunctioncreateUser(
 data: { name:string; email:string },
 token:string
) {
constuser=authenticate(token)
if (!user) {
thrownewError('Unauthorized')
 }
constnewUser=awaitdb.user.create({ data })
return newUser
}
```

## Reference
See the for more information on `use server`.
