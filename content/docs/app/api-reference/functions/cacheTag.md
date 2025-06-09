---
title: CacheTag
path: "App / Api Reference / Functions / Cachetag"
source_url: https://nextjs.org/docs/app/api-reference/functions/cacheTag
content_length: 2713
---

# cacheTag
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on .
The `cacheTag` function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.
## Usage
To use `cacheTag`, enable the `dynamicIO` flag in your `next.config.js` file:
next.config.ts
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  dynamicIO:true,
 },
}
exportdefault nextConfig
```

The `cacheTag` function takes a single string value, or a string array.
app/data.ts
```
import { unstable_cacheTag as cacheTag } from'next/cache'
exportasyncfunctiongetData() {
'use cache'
cacheTag('my-data')
constdata=awaitfetch('/api/data')
return data
}
```

You can then purge the cache on-demand using `revalidateTag` API in another function, for example, a route handler or Server Action:
app/action.ts
```
'use server'
import { revalidateTag } from'next/cache'
exportdefaultasyncfunctionsubmit() {
awaitaddPost()
revalidateTag('my-data')
}
```

## Good to know
  * **Idempotent Tags** : Applying the same tag multiple times has no additional effect.
  * **Multiple Tags** : You can assign multiple tags to a single cache entry by passing an array to `cacheTag`.


```
cacheTag('tag-one','tag-two')
```

## Examples
### Tagging components or functions
Tag your cached data by calling `cacheTag` within a cached function or component:
app/components/bookings.tsx
```
import { unstable_cacheTag as cacheTag } from'next/cache'
interfaceBookingsProps {
 type:string
}
exportasyncfunctionBookings({ type ='haircut' }:BookingsProps) {
'use cache'
cacheTag('bookings-data')
asyncfunctiongetBookingsData() {
constdata=awaitfetch(`/api/bookings?type=${encodeURIComponent(type)}`)
return data
 }
return//...
}
```

### Creating tags from external data
You can use the data returned from an async function to tag the cache entry.
app/components/bookings.tsx
```
import { unstable_cacheTag as cacheTag } from'next/cache'
interfaceBookingsProps {
 type:string
}
exportasyncfunctionBookings({ type ='haircut' }:BookingsProps) {
asyncfunctiongetBookingsData() {
'use cache'
constdata=awaitfetch(`/api/bookings?type=${encodeURIComponent(type)}`)
cacheTag('bookings-data',data.id)
return data
 }
return//...
}
```

### Invalidating tagged cache
Using `revalidateTag`, you can invalidate the cache for a specific tag when needed:
app/actions.ts
```
'use server'
import { revalidateTag } from'next/cache'
exportasyncfunctionupdateBookings() {
awaitupdateBookingData()
revalidateTag('bookings-data')
}
```
