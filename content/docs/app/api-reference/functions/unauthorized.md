---
title: Unauthorized
path: "App / Api Reference / Functions / Unauthorized"
source_url: https://nextjs.org/docs/app/api-reference/functions/unauthorized
content_length: 3047
---

# unauthorized
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
The `unauthorized` function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the `unauthorized.js` file.
To start using `unauthorized`, enable the experimental `authInterrupts` configuration option in your `next.config.js` file:
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

`unauthorized` can be invoked in Server Components, Server Actions, and Route Handlers.
app/dashboard/page.tsx
```
import { verifySession } from'@/app/lib/dal'
import { unauthorized } from'next/navigation'
exportdefaultasyncfunctionDashboardPage() {
constsession=awaitverifySession()
if (!session) {
unauthorized()
 }
// Render the dashboard for authenticated users
return (
  <main>
   <h1>Welcome to the Dashboard</h1>
   <p>Hi, {session.user.name}.</p>
  </main>
 )
}
```

## Good to know
  * The `unauthorized` function cannot be called in the root layout.


## Examples
### Displaying login UI to unauthenticated users
You can use `unauthorized` function to display the `unauthorized.js` file with a login UI.
app/dashboard/page.tsx
```
import { verifySession } from'@/app/lib/dal'
import { unauthorized } from'next/navigation'
exportdefaultasyncfunctionDashboardPage() {
constsession=awaitverifySession()
if (!session) {
unauthorized()
 }
return <div>Dashboard</div>
}
```

app/unauthorized.tsx
```
import Login from'@/app/components/Login'
exportdefaultfunctionUnauthorizedPage() {
return (
  <main>
   <h1>401 - Unauthorized</h1>
   <p>Please log in to access this page.</p>
   <Login />
  </main>
 )
}
```

### Mutations with Server Actions
You can invoke `unauthorized` in Server Actions to ensure only authenticated users can perform specific mutations.
app/actions/update-profile.ts
```
'use server'
import { verifySession } from'@/app/lib/dal'
import { unauthorized } from'next/navigation'
import db from'@/app/lib/db'
exportasyncfunctionupdateProfile(data:FormData) {
constsession=awaitverifySession()
// If the user is not authenticated, return a 401
if (!session) {
unauthorized()
 }
// Proceed with mutation
// ...
}
```

### Fetching data with Route Handlers
You can use `unauthorized` in Route Handlers to ensure only authenticated users can access the endpoint.
app/api/profile/route.ts
```
import { NextRequest, NextResponse } from'next/server'
import { verifySession } from'@/app/lib/dal'
import { unauthorized } from'next/navigation'
exportasyncfunctionGET(req:NextRequest):Promise<NextResponse> {
// Verify the user's session
constsession=awaitverifySession()
// If no session exists, return a 401 and render unauthorized.tsx
if (!session) {
unauthorized()
 }
// Fetch data
// ...
}
```

## Version History
Version| Changes  
---|---  
`v15.1.0`| `unauthorized` introduced.
