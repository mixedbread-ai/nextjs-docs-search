---
title: Forbidden
path: "App / Api Reference / Functions / Forbidden"
source_url: https://nextjs.org/docs/app/api-reference/functions/forbidden
content_length: 2448
---

# forbidden
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the `forbidden.js` file.
To start using `forbidden`, enable the experimental `authInterrupts` configuration option in your `next.config.js` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  authInterrupts:true,
 },
}
exportdefault nextConfig
```

`forbidden` can be invoked in Server Components, Server Actions, and Route Handlers.
app/auth/page.tsx
```
import { verifySession } from'@/app/lib/dal'
import { forbidden } from'next/navigation'
exportdefaultasyncfunctionAdminPage() {
constsession=awaitverifySession()
// Check if the user has the 'admin' role
if (session.role !=='admin') {
forbidden()
 }
// Render the admin page for authorized users
return <></>
}
```

## Good to know
  * The `forbidden` function cannot be called in the root layout.


## Examples
### Role-based route protection
You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.
app/admin/page.tsx
```
import { verifySession } from'@/app/lib/dal'
import { forbidden } from'next/navigation'
exportdefaultasyncfunctionAdminPage() {
constsession=awaitverifySession()
// Check if the user has the 'admin' role
if (session.role !=='admin') {
forbidden()
 }
// Render the admin page for authorized users
return (
  <main>
   <h1>Admin Dashboard</h1>
   <p>Welcome, {session.user.name}!</p>
  </main>
 )
}
```

### Mutations with Server Actions
When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.
app/actions/update-role.ts
```
'use server'
import { verifySession } from'@/app/lib/dal'
import { forbidden } from'next/navigation'
import db from'@/app/lib/db'
exportasyncfunctionupdateRole(formData:FormData) {
constsession=awaitverifySession()
// Ensure only admins can update roles
if (session.role !=='admin') {
forbidden()
 }
// Perform the role update for authorized users
// ...
}
```

## Version History
Version| Changes  
---|---  
`v15.1.0`| `forbidden` introduced.
