---
title: Taint
path: "App / Api Reference / Config / Next Config Js / Taint"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/taint
content_length: 4611
---

# taint
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on .
## Usage
The `taint` option enables support for experimental React APIs for tainting objects and values. This feature helps prevent sensitive data from being accidentally passed to the client. When enabled, you can use:
  * taint objects references.
  * to taint unique values.


> **Good to know** : Activating this flag also enables the React `experimental` channel for `app` directory.
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  taint:true,
 },
}
exportdefault nextConfig
```

> **Warning:** Do not rely on the taint API as your only mechanism to prevent exposing sensitive data to the client. See our security recommendations.
The taint APIs allows you to be defensive, by declaratively and explicitly marking data that is not allowed to pass through the Server-Client boundary. When an object or value, is passed through the Server-Client boundary, React throws an error.
This is helpful for cases where:
  * The methods to read data are out of your control
  * You have to work with sensitive data shapes not defined by you
  * Sensitive data is accessed during Server Component rendering


It is recommended to model your data and APIs so that sensitive data is not returned to contexts where it is not needed.
## Caveats
  * Tainting can only keep track of objects by reference. Copying an object creates an untainted version, which loses all guarantees given by the API. You'll need to taint the copy.
  * Tainting cannot keep track of data derived from a tainted value. You also need to taint the derived value.
  * Values are tainted for as long as their lifetime reference is within scope. See the , for more information.


## Examples
### Tainting an object reference
In this case, the `getUserDetails` function returns data about a given user. We taint the user object reference, so that it cannot cross a Server-Client boundary. For example, assuming `UserCard` is a Client Component.
```
import { experimental_taintObjectReference } from'react'
functiongetUserDetails(id:string):UserDetails {
constuser=awaitdb.queryUserById(id)
experimental_taintObjectReference(
'Do not use the entire user info object. Instead, select only the fields you need.',
  user
 )
return user
}
```

We can still access individual fields from the tainted `userDetails` object.
```
exportasyncfunctionContactPage({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
constuserDetails=awaitgetUserDetails(id)
return (
  <UserCard
firstName={userDetails.firstName}
lastName={userDetails.lastName}
  />
 )
}
```

Now, passing the entire object to the Client Component will throw an error.
```
exportasyncfunctionContactPage({
 params,
}: {
 params:Promise<{ id:string }>
}) {
constuserDetails=awaitgetUserDetails(id)
// Throws an error
return <UserCarduser={userDetails} />
}
```

### Tainting a unique value
In this case, we can access the server configuration by awaiting calls to `config.getConfigDetails`. However, the system configuration contains the `SERVICE_API_KEY` that we don't want to expose to clients.
We can taint the `config.SERVICE_API_KEY` value.
```
import { experimental_taintUniqueValue } from'react'
functiongetSystemConfig():SystemConfig {
constconfig=awaitconfig.getConfigDetails()
experimental_taintUniqueValue(
'Do not pass configuration tokens to the client',
  config,
config.SERVICE_API_KEY
 )
return config
}
```

We can still access other properties of the `systemConfig` object.
```
exportasyncfunctionDashboard() {
constsystemConfig=awaitgetSystemConfig()
return <ClientDashboardversion={systemConfig.SERVICE_API_VERSION} />
}
```

However, passing `SERVICE_API_KEY` to `ClientDashboard` throws an error.
```
exportasyncfunctionDashboard() {
constsystemConfig=awaitgetSystemConfig()
// Someone makes a mistake in a PR
constversion=systemConfig.SERVICE_API_KEY
return <ClientDashboardversion={version} />
}
```

Note that, even though, `systemConfig.SERVICE_API_KEY` is reassigned to a new variable. Passing it to a Client Component still throws an error.
Whereas, a value derived from a tainted unique value, will be exposed to the client.
```
exportasyncfunctionDashboard() {
constsystemConfig=awaitgetSystemConfig()
// Someone makes a mistake in a PR
constversion=`version::${systemConfig.SERVICE_API_KEY}`
return <ClientDashboardversion={version} />
}
```

A better approach is to remove `SERVICE_API_KEY` from the data returned by `getSystemConfig`.
