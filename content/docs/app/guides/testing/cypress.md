---
title: "How to set up Cypress with Next.js"
path: "App / Guides / Testing / Cypress"
source_url: https://nextjs.org/docs/app/guides/testing/cypress
content_length: 5377
---

# How to set up Cypress with Next.js
is a test runner used for **End-to-End (E2E)** and **Component Testing**. This page will show you how to set up Cypress with Next.js and write your first tests.
> **Warning:**
>   * Cypress versions below 13.6.3 do not support with `moduleResolution:"bundler"`. However, this issue has been resolved in Cypress version 13.6.3 and later. 
> 

## Quickstart
You can use `create-next-app` with the to quickly get started.
Terminal
```
npxcreate-next-app@latest--examplewith-cypresswith-cypress-app
```

## Manual setup
To manually set up Cypress, install `cypress` as a dev dependency:
Terminal
```
npminstall-Dcypress
# or
yarnadd-Dcypress
# or
pnpminstall-Dcypress
```

Add the Cypress `open` command to the `package.json` scripts field:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start",
"lint":"next lint",
"cypress:open":"cypress open"
 }
}
```

Run Cypress for the first time to open the Cypress testing suite:
Terminal
```
npmruncypress:open
```

You can choose to configure **E2E Testing** and/or **Component Testing**. Selecting any of these options will automatically create a `cypress.config.js` file and a `cypress` folder in your project.
## Creating your first Cypress E2E test
Ensure your `cypress.config` file has the following configuration:
cypress.config.ts
```
import { defineConfig } from'cypress'
exportdefaultdefineConfig({
 e2e: {
setupNodeEvents(on, config) {},
 },
})
```

Then, create two new Next.js files:
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

app/about/page.js
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <div>
   <h1>About</h1>
   <Linkhref="/">Home</Link>
  </div>
 )
}
```

Add a test to check your navigation is working correctly:
cypress/e2e/app.cy.js
```
describe('Navigation', () => {
it('should navigate to the about page', () => {
// Start from the index page
cy.visit('
// Find a link with an href attribute containing "about" and click it
cy.get('a[href*="about"]').click()
// The new url should include "/about"
cy.url().should('include','/about')
// The new page should contain an h1 with "About"
cy.get('h1').contains('About')
 })
})
```

### Running E2E Tests
Cypress will simulate a user navigating your application, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.
Run `npm run build && npm run start` to build your Next.js application, then run `npm run cypress:open` in another terminal window to start Cypress and run your E2E Testing suite.
> **Good to know:**
>   * You can use `cy.visit("/")` instead of `cy.visit("")` by adding `baseUrl: '` to the `cypress.config.js` configuration file.
>   * Alternatively, you can install the package to run the Next.js production server in conjunction with Cypress. After installation, add `"test": "start-server-and-test start  cypress"` to your `package.json` scripts field. Remember to rebuild your application after new changes.
> 

## Creating your first Cypress component test
Component tests build and mount a specific component without having to bundle your whole application or start a server.
Select **Component Testing** in the Cypress app, then select **Next.js** as your front-end framework. A `cypress/component` folder will be created in your project, and a `cypress.config.js` file will be updated to enable Component Testing.
Ensure your `cypress.config` file has the following configuration:
cypress.config.ts
```
import { defineConfig } from'cypress'
exportdefaultdefineConfig({
 component: {
  devServer: {
   framework:'next',
   bundler:'webpack',
  },
 },
})
```

Assuming the same components from the previous section, add a test to validate a component is rendering the expected output:
cypress/component/about.cy.tsx
```
import Page from'../../app/page'
describe('<Page />', () => {
it('should render and display expected content', () => {
// Mount the React component for the Home page
cy.mount(<Page />)
// The new page should contain an h1 with "Home"
cy.get('h1').contains('Home')
// Validate that a link with the expected URL is present
// Following the link is better suited to an E2E test
cy.get('a[href="/about"]').should('be.visible')
 })
})
```

> **Good to know** :
>   * Cypress currently doesn't support Component Testing for `async` Server Components. We recommend using E2E testing.
>   * Since component tests do not require a Next.js server, features like `<Image />` that rely on a server being available may not function out-of-the-box.
> 

### Running Component Tests
Run `npm run cypress:open` in your terminal to start Cypress and run your Component Testing suite.
## Continuous Integration (CI)
In addition to interactive testing, you can also run Cypress headlessly using the `cypress run` command, which is better suited for CI environments:
package.json
```
{
"scripts": {
//...
"e2e":"start-server-and-test dev  \"cypress open --e2e\"",
"e2e:headless":"start-server-and-test dev  \"cypress run --e2e\"",
"component":"cypress open --component",
"component:headless":"cypress run --component"
 }
}
```

You can learn more about Cypress and Continuous Integration from these resources:
