---
title: RevalidateTag
path: "App / Api Reference / Functions / Revalidatetag"
source_url: https://nextjs.org/docs/app/api-reference/functions/revalidateTag
content_length: 1260
---

# revalidateTag
`revalidateTag` allows you to purge cached data on-demand for a specific cache tag.
> **Good to know** :
>   * `revalidateTag` only invalidates the cache when the path is next visited. This means calling `revalidateTag` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.
> 

## Parameters
```
revalidateTag(tag: string): void;
```

  * `tag`: A string representing the cache tag associated with the data you want to revalidate. Must be less than or equal to 256 characters. This value is case-sensitive.


You can add tags to `fetch` as follows:
```
fetch(url, { next: { tags: [...] } });
```

## Returns
`revalidateTag` does not return a value.
## Examples
### Server Action
app/actions.ts
```
'use server'
import { revalidateTag } from'next/cache'
exportdefaultasyncfunctionsubmit() {
awaitaddPost()
revalidateTag('posts')
}
```

### Route Handler
app/api/revalidate/route.ts
```
importtype { NextRequest } from'next/server'
import { revalidateTag } from'next/cache'
exportasyncfunctionGET(request:NextRequest) {
consttag=request.nextUrl.searchParams.get('tag')
revalidateTag(tag)
returnResponse.json({ revalidated:true, now:Date.now() })
}
```
