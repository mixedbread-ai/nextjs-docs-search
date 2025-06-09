---
title: UseLinkStatus
path: "App / Api Reference / Functions / Use Link Status"
source_url: https://nextjs.org/docs/app/api-reference/functions/use-link-status
content_length: 3448
---

# useLinkStatus
The `useLinkStatus` hook lets you tracks the **pending** state of a `<Link>`. You can use it to show inline visual feedback to the user (like spinners or text glimmers) while a navigation to a new route completes.
`useLinkStatus` is useful when:
  * Prefetching is disabled or in progress meaning navigation is blocked.
  * The destination route is dynamic **and** doesn't include a `loading.js` file that would allow an instant navigation.


app/loading-indicator.tsx
```
'use client'
import { useLinkStatus } from'next/link'
exportdefaultfunctionLoadingIndicator() {
const { pending } =useLinkStatus()
return pending ? (
  <divrole="status"aria-label="Loading"className="spinner" />
 ) :null
}
```

app/header.tsx
```
import Link from'next/link'
import LoadingIndicator from'./loading-indicator'
exportdefaultfunctionHeader() {
return (
  <header>
   <Linkhref="/dashboard"prefetch={false}>
    Dashboard <LoadingIndicator />
   </Link>
  </header>
 )
}
```

> **Good to know** :
>   * `useLinkStatus` must be used within a descendant component of a `Link` component
>   * The hook is most useful when `prefetch={false}` is set on the `Link` component
>   * If the linked route has been prefetched, the pending state will be skipped
>   * When clicking multiple links in quick succession, only the last link's pending state is shown
>   * This hook is not supported in the Pages Router and will always return `{ pending: false }`
> 

## Parameters
```
const { pending } =useLinkStatus()
```

`useLinkStatus` does not take any parameters.
## Returns
`useLinkStatus` returns an object with a single property:
Property| Type| Description  
---|---|---  
pending| boolean| `true` before history updates, `false` after  
## Example
### Inline loading indicator
It's helpful to add visual feedback that navigation is happening in case the user clicks a link before prefetching is complete.
app/components/loading-indicator.tsx
```
'use client'
import { useLinkStatus } from'next/link'
exportdefaultfunctionLoadingIndicator() {
const { pending } =useLinkStatus()
return pending ? (
  <divrole="status"aria-label="Loading"className="spinner" />
 ) :null
}
```

app/shop/layout.tsx
```
import Link from'next/link'
import LoadingIndicator from'./components/loading-indicator'
constlinks= [
 { href:'/shop/electronics', label:'Electronics' },
 { href:'/shop/clothing', label:'Clothing' },
 { href:'/shop/books', label:'Books' },
]
functionMenubar() {
return (
  <div>
   {links.map((link) => (
    <Linkkey={link.label} href={link.href}>
     {link.label} <LoadingIndicator />
    </Link>
   ))}
  </div>
 )
}
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return (
  <div>
   <Menubar />
   {children}
  </div>
 )
}
```

## Gracefully handling fast navigation
If the navigation to a new route is fast, users may see an unecessary flash of the loading indicator. One way to improve the user experience and only show the loading indicator when the navigation takes time to complete is to add an initial animation delay (e.g. 100ms) and start the animation as invisible (e.g. `opacity: 0`).
app/styles/global.css
```
.spinner {
/* ... */
opacity:0;
animation:
  fadeIn 500ms 100ms forwards,
  rotate 1s linear infinite;
}
@keyframes fadeIn {
 from {
opacity:0;
 }
 to {
opacity:1;
 }
}
@keyframes rotate {
 to {
transform:rotate(360deg);
 }
}
```

Version| Changes  
---|---  
`v15.3.0`| `useLinkStatus` introduced.
