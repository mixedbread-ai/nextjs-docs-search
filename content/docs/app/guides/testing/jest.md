---
title: "How to set up Jest with Next.js"
path: "App / Guides / Testing / Jest"
source_url: https://nextjs.org/docs/app/guides/testing/jest
content_length: 5934
---

# How to set up Jest with Next.js
Jest and React Testing Library are frequently used together for **Unit Testing** and **Snapshot Testing**. This guide will show you how to set up Jest with Next.js and write your first tests.
> **Good to know:** Since `async` Server Components are new to the React ecosystem, Jest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using an **E2E tests** for `async` components.
## Quickstart
You can use `create-next-app` with the Next.js example to quickly get started:
Terminal
```
npxcreate-next-app@latest--examplewith-jestwith-jest-app
```

## Manual setup
Since the release of Next.js 12, Next.js now has built-in configuration for Jest.
To set up Jest, install `jest` and the following packages as dev dependencies:
Terminal
```
npminstall-Djestjest-environment-jsdom@testing-library/react@testing-library/dom@testing-library/jest-domts-node@types/jest
# or
yarnadd-Djestjest-environment-jsdom@testing-library/react@testing-library/dom@testing-library/jest-domts-node@types/jest
# or
pnpminstall-Djestjest-environment-jsdom@testing-library/react@testing-library/dom@testing-library/jest-domts-node@types/jest
```

Generate a basic Jest configuration file by running the following command:
Terminal
```
npminitjest@latest
# or
yarncreatejest@latest
# or
pnpmcreatejest@latest
```

This will take you through a series of prompts to setup Jest for your project, including automatically creating a `jest.config.ts|js` file.
Update your config file to use `next/jest`. This transformer has all the necessary configuration options for Jest to work with Next.js:
jest.config.ts
```
importtype { Config } from'jest'
import nextJest from'next/jest.js'
constcreateJestConfig=nextJest({
// Provide the path to your Next.js app to load next.config.js and .env files in your test environment
 dir:'./',
})
// Add any custom config to be passed to Jest
constconfig:Config= {
 coverageProvider:'v8',
 testEnvironment:'jsdom',
// Add more setup options before each test is run
// setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
}
// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
exportdefaultcreateJestConfig(config)
```

Under the hood, `next/jest` is automatically configuring Jest for you, including:
  * Setting up `transform` using the Next.js Compiler.
  * Auto mocking stylesheets (`.css`, `.module.css`, and their scss variants), image imports and `next/font`.
  * Loading `.env` (and all variants) into `process.env`.
  * Ignoring `node_modules` from test resolving and transforms.
  * Ignoring `.next` from test resolving.
  * Loading `next.config.js` for flags that enable SWC transforms.


> **Good to know** : To test environment variables directly, load them manually in a separate setup script or in your `jest.config.ts` file. For more information, please see Test Environment Variables.
## Optional: Handling Absolute Imports and Module Path Aliases
If your project is using Module Path Aliases, you will need to configure Jest to resolve the imports by matching the paths option in the `jsconfig.json` file with the `moduleNameMapper` option in the `jest.config.js` file. For example:
tsconfig.json or jsconfig.json
```
{
"compilerOptions": {
"module":"esnext",
"moduleResolution":"bundler",
"baseUrl":"./",
"paths": {
"@/components/*": ["components/*"]
  }
 }
}
```

jest.config.js
```
moduleNameMapper: {
// ...
'^@/components/(.*)$': '<rootDir>/components/$1',
}
```

## Optional: Extend Jest with custom matchers
`@testing-library/jest-dom` includes a set of convenient such as `.toBeInTheDocument()` making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:
jest.config.ts
```
setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
```

Then, inside `jest.setup`, add the following import:
jest.setup.ts
```
import'@testing-library/jest-dom'
```

> **Good to know:** , so if you are using `@testing-library/jest-dom` before version 6, you will need to import `@testing-library/jest-dom/extend-expect` instead.
If you need to add more setup options before each test, you can add them to the `jest.setup` file above.
## Add a test script to `package.json`
Finally, add a Jest `test` script to your `package.json` file:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start",
"test":"jest",
"test:watch":"jest --watch"
 }
}
```

`jest --watch` will re-run tests when a file is changed. For more Jest CLI options, please refer to the .
### Creating your first test
Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.
For example, we can add a test to check if the `<Page />` component successfully renders a heading:
app/page.js
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

__tests__/page.test.jsx
```
import'@testing-library/jest-dom'
import { render, screen } from'@testing-library/react'
import Page from'../app/page'
describe('Page', () => {
it('renders a heading', () => {
render(<Page />)
constheading=screen.getByRole('heading', { level:1 })
expect(heading).toBeInTheDocument()
 })
})
```

Optionally, add a to keep track of any unexpected changes in your component:
__tests__/snapshot.js
```
import { render } from'@testing-library/react'
import Page from'../app/page'
it('renders homepage unchanged', () => {
const { container } =render(<Page />)
expect(container).toMatchSnapshot()
})
```

## Running your tests
Then, run the following command to run your tests:
Terminal
```
npmruntest
# or
yarntest
# or
pnpmtest
```

## Additional Resources
For further reading, you may find these resources helpful:
  * - use good testing practices to match elements.
