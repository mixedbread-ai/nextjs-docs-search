---
title: "Parallel Routes"
path: "App / Api Reference / File Conventions / Parallel Routes"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes
content_length: 9945
---

# Parallel Routes
Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.
For example, considering a dashboard, you can use parallel routes to simultaneously render the `team` and `analytics` pages:
!Parallel Routes Diagram!Parallel Routes Diagram
## Convention
### Slots
Parallel routes are created using named **slots**. Slots are defined with the `@folder` convention. For example, the following file structure defines two slots: `@analytics` and `@team`:
!Parallel Routes File-system Structure!Parallel Routes File-system Structure
Slots are passed as props to the shared parent layout. For the example above, the component in `app/layout.js` now accepts the `@analytics` and `@team` slots props, and can render them in parallel alongside the `children` prop:
app/layout.tsx
```
exportdefaultfunctionLayout({
 children,
 team,
 analytics,
}: {
 children:React.ReactNode
 analytics:React.ReactNode
 team:React.ReactNode
}) {
return (
  <>
   {children}
   {team}
   {analytics}
  </>
 )
}
```

However, slots are **not** route segments and do not affect the URL structure. For example, for `/@analytics/views`, the URL will be `/views` since `@analytics` is a slot. Slots are combined with the regular Page component to form the final page associated with the route segment. Because of this, you cannot have separate static and dynamic slots at the same route segment level. If one slot is dynamic, all slots at that level must be dynamic.
> **Good to know** :
>   * The `children` prop is an implicit slot that does not need to be mapped to a folder. This means `app/page.js` is equivalent to `app/@children/page.js`.
> 

### `default.js`
You can define a `default.js` file to render as a fallback for unmatched slots during the initial load or full-page reload.
Consider the following folder structure. The `@team` slot has a `/settings` page, but `@analytics` does not.
!Parallel Routes unmatched routes!Parallel Routes unmatched routes
When navigating to `/settings`, the `@team` slot will render the `/settings` page while maintaining the currently active page for the `@analytics` slot.
On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.
Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.
## Behavior
By default, Next.js keeps track of the active _state_ (or subpage) for each slot. However, the content rendered within a slot will depend on the type of navigation:
  * **Soft Navigation**: During client-side navigation, Next.js will perform a partial render, changing the subpage within the slot, while maintaining the other slot's active subpages, even if they don't match the current URL.
  * **Hard Navigation** : After a full-page load (browser refresh), Next.js cannot determine the active state for the slots that don't match the current URL. Instead, it will render a `default.js` file for the unmatched slots, or `404` if `default.js` doesn't exist.


> **Good to know** :
>   * The `404` for unmatched routes helps ensure that you don't accidentally render a parallel route on a page that it was not intended for.
> 

## Examples
### With `useSelectedLayoutSegment(s)`
Both `useSelectedLayoutSegment` and `useSelectedLayoutSegments` accept a `parallelRoutesKey` parameter, which allows you to read the active route segment within a slot.
app/layout.tsx
```
'use client'
import { useSelectedLayoutSegment } from'next/navigation'
exportdefaultfunctionLayout({ auth }: { auth:React.ReactNode }) {
constloginSegment=useSelectedLayoutSegment('auth')
// ...
}
```

When a user navigates to `app/@auth/login` (or `/login` in the URL bar), `loginSegment` will be equal to the string `"login"`.
### Conditional Routes
You can use Parallel Routes to conditionally render routes based on certain conditions, such as user role. For example, to render a different dashboard page for the `/admin` or `/user` roles:
!Conditional routes diagram!Conditional routes diagram
app/dashboard/layout.tsx
```
import { checkUserRole } from'@/lib/auth'
exportdefaultfunctionLayout({
 user,
 admin,
}: {
 user:React.ReactNode
 admin:React.ReactNode
}) {
constrole=checkUserRole()
return role ==='admin'? admin : user
}
```

### Tab Groups
You can add a `layout` inside a slot to allow users to navigate the slot independently. This is useful for creating tabs.
For example, the `@analytics` slot has two subpages: `/page-views` and `/visitors`.
!Analytics slot with two subpages and a layout!Analytics slot with two subpages and a layout
Within `@analytics`, create a `layout` file to share the tabs between the two pages:
app/@analytics/layout.tsx
```
import Link from'next/link'
exportdefaultfunctionLayout({ children }: { children:React.ReactNode }) {
return (
  <>
   <nav>
    <Linkhref="/page-views">Page Views</Link>
    <Linkhref="/visitors">Visitors</Link>
   </nav>
   <div>{children}</div>
  </>
 )
}
```

### Modals
Parallel Routes can be used together with Intercepting Routes to create modals that support deep linking. This allows you to solve common challenges when building modals, such as:
  * Making the modal content **shareable through a URL**.
  * **Preserving context** when the page is refreshed, instead of closing the modal.
  * **Closing the modal on backwards navigation** rather than going to the previous route.
  * **Reopening the modal on forwards navigation**.


Consider the following UI pattern, where a user can open a login modal from a layout using client-side navigation, or access a separate `/login` page:
!Parallel Routes Diagram!Parallel Routes Diagram
To implement this pattern, start by creating a `/login` route that renders your **main** login page.
!Parallel Routes Diagram!Parallel Routes Diagram
app/login/page.tsx
```
import { Login } from'@/app/ui/login'
exportdefaultfunctionPage() {
return <Login />
}
```

Then, inside the `@auth` slot, add `default.js` file that returns `null`. This ensures that the modal is not rendered when it's not active.
app/@auth/default.tsx
```
exportdefaultfunctionDefault() {
returnnull
}
```

Inside your `@auth` slot, intercept the `/login` route by updating the `/(.)login` folder. Import the `<Modal>` component and its children into the `/(.)login/page.tsx` file:
app/@auth/(.)login/page.tsx
```
import { Modal } from'@/app/ui/modal'
import { Login } from'@/app/ui/login'
exportdefaultfunctionPage() {
return (
  <Modal>
   <Login />
  </Modal>
 )
}
```

> **Good to know:**
>   * The convention used to intercept the route, e.g. `(.)`, depends on your file-system structure. See Intercepting Routes convention.
>   * By separating the `<Modal>` functionality from the modal content (`<Login>`), you can ensure any content inside the modal, e.g. forms, are Server Components. See Interleaving Client and Server Components for more information.
> 

#### Opening the modal
Now, you can leverage the Next.js router to open and close the modal. This ensures the URL is correctly updated when the modal is open, and when navigating backwards and forwards.
To open the modal, pass the `@auth` slot as a prop to the parent layout and render it alongside the `children` prop.
app/layout.tsx
```
import Link from'next/link'
exportdefaultfunctionLayout({
 auth,
 children,
}: {
 auth:React.ReactNode
 children:React.ReactNode
}) {
return (
  <>
   <nav>
    <Linkhref="/login">Open modal</Link>
   </nav>
   <div>{auth}</div>
   <div>{children}</div>
  </>
 )
}
```

When the user clicks the `<Link>`, the modal will open instead of navigating to the `/login` page. However, on refresh or initial load, navigating to `/login` will take the user to the main login page.
#### Closing the modal
You can close the modal by calling `router.back()` or by using the `Link` component.
app/ui/modal.tsx
```
'use client'
import { useRouter } from'next/navigation'
exportfunctionModal({ children }: { children:React.ReactNode }) {
constrouter=useRouter()
return (
  <>
   <button
onClick={() => {
router.back()
    }}
   >
    Close modal
   </button>
   <div>{children}</div>
  </>
 )
}
```

When using the `Link` component to navigate away from a page that shouldn't render the `@auth` slot anymore, we need to make sure the parallel route matches to a component that returns `null`. For example, when navigating back to the root page, we create a `@auth/page.tsx` component:
app/ui/modal.tsx
```
import Link from'next/link'
exportfunctionModal({ children }: { children:React.ReactNode }) {
return (
  <>
   <Linkhref="/">Close modal</Link>
   <div>{children}</div>
  </>
 )
}
```

app/@auth/page.tsx
```
exportdefaultfunctionPage() {
returnnull
}
```

Or if navigating to any other page (such as `/foo`, `/foo/bar`, etc), you can use a catch-all slot:
app/@auth/[...catchAll]/page.tsx
```
exportdefaultfunctionCatchAll() {
returnnull
}
```

> **Good to know:**
>   * We use a catch-all route in our `@auth` slot to close the modal because of how parallel routes behave(#behavior). Since client-side navigations to a route that no longer match the slot will remain visible, we need to match the slot to a route that returns `null` to close the modal.
>   * Other examples could include opening a photo modal in a gallery while also having a dedicated `/photo/[id]` page, or opening a shopping cart in a side modal.
>   * of modals with Intercepted and Parallel Routes.
> 

### Loading and Error UI
Parallel Routes can be streamed independently, allowing you to define independent error and loading states for each route:
!Parallel routes enable custom error and loading states!Parallel routes enable custom error and loading states
See the Loading UI and Error Handling documentation for more information.
