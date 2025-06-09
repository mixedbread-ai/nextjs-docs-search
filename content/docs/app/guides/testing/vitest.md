---
title: "How to set up Vitest with Next.js"
path: "App / Guides / Testing / Vitest"
source_url: https://nextjs.org/docs/app/guides/testing/vitest
content_length: 2629
---

# How to set up Vitest with Next.js
Vite and React Testing Library are frequently used together for **Unit Testing**. This guide will show you how to setup Vitest with Next.js and write your first tests.
> **Good to know:** Since `async` Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using **E2E tests** for `async` components.
## Quickstart
You can use `create-next-app` with the Next.js example to quickly get started:
Terminal
```
npxcreate-next-app@latest--examplewith-vitestwith-vitest-app
```

## Manual Setup
To manually set up Vitest, install `vitest` and the following packages as dev dependencies:
Terminal
```
# Using TypeScript
npminstall-Dvitest@vitejs/plugin-reactjsdom@testing-library/react@testing-library/domvite-tsconfig-paths
# Using JavaScript
npminstall-Dvitest@vitejs/plugin-reactjsdom@testing-library/react@testing-library/dom
```

Create a `vitest.config.mts|js` file in the root of your project, and add the following options:
vitest.config.mts
```
import { defineConfig } from'vitest/config'
import react from'@vitejs/plugin-react'
import tsconfigPaths from'vite-tsconfig-paths'
exportdefaultdefineConfig({
 plugins: [tsconfigPaths(),react()],
 test: {
  environment:'jsdom',
 },
})
```

For more information on configuring Vitest, please refer to the docs.
Then, add a `test` script to your `package.json`:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start",
"test":"vitest"
 }
}
```

When you run `npm run test`, Vitest will **watch** for changes in your project by default.
## Creating your first Vitest Unit Test
Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:
app/page.tsx
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <div>
   <h1>Home</h1>
   <Linkhref="/about">About</Link>
  </div>
 )
}
```

__tests__/page.test.tsx
```
import { expect, test } from'vitest'
import { render, screen } from'@testing-library/react'
import Page from'../app/page'
test('Page', () => {
render(<Page />)
expect(screen.getByRole('heading', { level:1, name:'Home' })).toBeDefined()
})
```

> **Good to know** : The example above uses the common `__tests__` convention, but test files can also be colocated inside the `app` router.
## Running your tests
Then, run the following command to run your tests:
Terminal
```
npmruntest
# or
yarntest
# or
pnpmtest
# or
buntest
```

## Additional Resources
You may find these resources helpful:
