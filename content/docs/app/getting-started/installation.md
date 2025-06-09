---
title: "How to set up a new Next.js project"
path: "App / Getting Started / Installation"
source_url: https://nextjs.org/docs/app/getting-started/installation
content_length: 6859
---

# How to set up a new Next.js project
## System requirements
Before you begin, make sure your system meets the following requirements:
  * or later.
  * macOS, Windows (including WSL), or Linux.


## Automatic installation
The quickest way to create a new Next.js app is using `create-next-app`, which sets up everything automatically for you. To create a project, run:
Terminal
```
npxcreate-next-app@latest
```

On installation, you'll see the following prompts:
Terminal
```
What is your project named? my-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for `next dev`? No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

After the prompts, `create-next-app` will create a folder with your project name and install the required dependencies.
## Manual installation
To manually create a new Next.js app, install the required packages:
Terminal
```
npminstallnext@latestreact@latestreact-dom@latest
```

Then, add the following scripts to your `package.json` file:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start",
"lint":"next lint"
 }
}
```

These scripts refer to the different stages of developing an application:
  * `next dev`: Starts the development server.
  * `next build`: Builds the application for production.
  * `next start`: Starts the production server.
  * `next lint`: Runs ESLint.


### Create the `app` directory
Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.
Create an `app` folder. Then, inside `app`, create a `layout.tsx` file. This file is the root layout. It's required and must contain the `<html>` and `<body>` tags.
app/layout.tsx
```
exportdefaultfunctionRootLayout({
 children,
}: {
 children:React.ReactNode
}) {
return (
  <htmllang="en">
   <body>{children}</body>
  </html>
 )
}
```

Create a home page `app/page.tsx` with some initial content:
app/page.tsx
```
exportdefaultfunctionPage() {
return <h1>Hello, Next.js!</h1>
}
```

Both `layout.tsx` and `page.tsx` will be rendered when the user visits the root of your application (`/`).
!App Folder Structure!App Folder Structure
> **Good to know** :
>   * If you forget to create the root layout, Next.js will automatically create this file when running the development server with `next dev`.
>   * You can optionally use a `src` folder in the root of your project to separate your application's code from configuration files.
> 

### Create the `public` folder (optional)
Create a `public` folder at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).
You can then reference these assets using the root path (`/`). For example, `public/profile.png` can be referenced as `/profile.png`:
app/page.tsx
```
import Image from'next/image'
exportdefaultfunctionPage() {
return <Imagesrc="/profile.png"alt="Profile"width={100} height={100} />
}
```

## Run the development server
  1. Run `npm run dev` to start the development server.
  2. Visit `` to view your application.
  3. Edit the `app/page.tsx` file and save it to see the updated result in your browser.


## Set up TypeScript
> Minimum TypeScript version: `v4.5.2`
Next.js comes with built-in TypeScript support. To add TypeScript to your project, rename a file to `.ts` / `.tsx` and run `next dev`. Next.js will automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.
### IDE Plugin
Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.
You can enable the plugin in VS Code by:
  1. Opening the command palette (`Ctrl/⌘` + `Shift` + `P`)
  2. Searching for "TypeScript: Select TypeScript Version"
  3. Selecting "Use Workspace Version"

!TypeScript Command Palette!TypeScript Command Palette
See the TypeScript reference page for more information.
## Set up ESLint
Next.js comes with built-in ESLint. It automatically installs the necessary packages and configures the proper settings when you create a new project with `create-next-app`.
To manually add ESLint to an existing project, add `next lint` as a script to `package.json`:
package.json
```
{
"scripts": {
"lint":"next lint"
 }
}
```

Then, run `npm run lint` and you will be guided through the installation and configuration process.
Terminal
```
npmrunlint
```

You'll see a prompt like this:
> ? How would you like to configure ESLint?
> ❯ Strict (recommended) Base Cancel
  * **Strict** : Includes Next.js' base ESLint configuration along with a stricter Core Web Vitals rule-set. This is the recommended configuration for developers setting up ESLint for the first time.
  * **Base** : Includes Next.js' base ESLint configuration.
  * **Cancel** : Skip configuration. Select this option if you plan on setting up your own custom ESLint configuration.


If `Strict` or `Base` are selected, Next.js will automatically install `eslint` and `eslint-config-next` as dependencies in your application and create an `.eslintrc.json` file in the root of your project that includes your selected configuration.
You can now run `next lint` every time you want to run ESLint to catch errors. Once ESLint has been set up, it will also automatically run during every build (`next build`). Errors will fail the build, while warnings will not.
See the ESLint Plugin page for more information.
## Set up Absolute Imports and Module Path Aliases
Next.js has in-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files.
These options allow you to alias project directories to absolute paths, making it easier and cleaner to import modules. For example:
```
// Before
import { Button } from'../../../components/button'
// After
import { Button } from'@/components/button'
```

To configure absolute imports, add the `baseUrl` configuration option to your `tsconfig.json` or `jsconfig.json` file. For example:
tsconfig.json or jsconfig.json
```
{
"compilerOptions": {
"baseUrl":"src/"
 }
}
```

In addition to configuring the `baseUrl` path, you can use the `"paths"` option to `"alias"` module paths.
For example, the following configuration maps `@/components/*` to `components/*`:
tsconfig.json or jsconfig.json
```
{
"compilerOptions": {
"baseUrl":"src/",
"paths": {
"@/styles/*": ["styles/*"],
"@/components/*": ["components/*"]
  }
 }
}
```

Each of the `"paths"` are relative to the `baseUrl` location.
