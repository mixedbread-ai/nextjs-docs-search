---
title: Template.js
path: "App / Api Reference / File Conventions / Template"
source_url: https://nextjs.org/docs/app/api-reference/file-conventions/template
content_length: 2002
---

# template.js
A **template** file is similar to a layout in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.
They are useful when you need to:
  * Resynchronize `useEffect` on navigation.
  * Reset the state of a child Client Components on navigation. For example, an input field.
  * To change default framework behavior. For example, Suspense boundaries inside layouts only show a fallback on first load, while templates show it on every navigation.


## Convention
A template can be defined by exporting a default React component from a `template.js` file. The component should accept a `children` prop.
!template.js special file!template.js special file
app/template.tsx
```
exportdefaultfunctionTemplate({ children }: { children:React.ReactNode }) {
return <div>{children}</div>
}
```

In terms of nesting, `template.js` is rendered between a layout and its children. Here's a simplified output:
Output
```
<Layout>
 {/* Note that the template is given a unique key. */}
 <Templatekey={routeParam}>{children}</Template>
</Layout>
```

## Props
### `children` (required)
Template accepts a `children` prop.
Output
```
<Layout>
 {/* Note that the template is automatically given a unique key. */}
 <Templatekey={routeParam}>{children}</Template>
</Layout>
```

## Behavior
  * **Server Components** : By default, templates are Server Components.
  * **Remount on navigation** : Templates receive a unique key automatically. Navigating to a new route causes the template and its children to remount.
  * **State reset** : Any Client Component inside the template will reset its state on navigation.
  * **Effect re-run** : Effects like `useEffect` will re-synchronize as the component remounts.
  * **DOM reset** : DOM elements inside the template are fully recreated.


## Version History
Version| Changes  
---|---  
`v13.0.0`| `template` introduced.
