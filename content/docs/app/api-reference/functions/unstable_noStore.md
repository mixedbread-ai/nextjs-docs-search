---
title: Unstable_noStore
path: "App / Api Reference / Functions / Unstable_Nostore"
source_url: https://nextjs.org/docs/app/api-reference/functions/unstable_noStore
content_length: 1476
---

# unstable_noStore
This is a legacy API and no longer recommended. It's still supported for backward compatibility.
**In version 15, we recommend using`connection` instead of `unstable_noStore`.**
`unstable_noStore` can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.
```
import { unstable_noStore as noStore } from'next/cache';
exportdefaultasyncfunctionServerComponent() {
noStore();
constresult=awaitdb.query(...);
...
}
```

> **Good to know** :
>   * `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
>   * `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis
> 

  * Using `unstable_noStore` inside `unstable_cache` will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.


## Usage
If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.
```
import { unstable_noStore as noStore } from'next/cache';
exportdefaultasyncfunctionServerComponent() {
noStore();
constresult=awaitdb.query(...);
...
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0`| `unstable_noStore` deprecated for `connection`.  
`v14.0.0`| `unstable_noStore` introduced.
