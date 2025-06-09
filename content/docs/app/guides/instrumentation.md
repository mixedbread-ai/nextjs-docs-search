---
title: "How to set up instrumentation"
path: "App / Guides / Instrumentation"
source_url: https://nextjs.org/docs/app/guides/instrumentation
content_length: 2582
---

# How to set up instrumentation
Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.
## Convention
To set up instrumentation, create `instrumentation.ts|js` file in the **root directory** of your project (or inside the `src` folder if using one).
Then, export a `register` function in the file. This function will be called **once** when a new Next.js server instance is initiated.
For example, to use Next.js with and :
instrumentation.ts
```
import { registerOTel } from'@vercel/otel'
exportfunctionregister() {
registerOTel('next-app')
}
```

See the for a complete implementation.
> **Good to know** :
>   * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
>   * If you use the `pageExtensions` config option to add a suffix, you will also need to update the `instrumentation` filename to match.
> 

## Examples
### Importing files with side effects
Sometimes, it may be useful to import a file in your code because of the side effects it will cause. For example, you might import a file that defines a set of global variables, but never explicitly use the imported file in your code. You would still have access to the global variables the package has declared.
We recommend importing files using JavaScript `import` syntax within your `register` function. The following example demonstrates a basic usage of `import` in a `register` function:
instrumentation.ts
```
exportasyncfunctionregister() {
awaitimport('package-with-side-effect')
}
```

> **Good to know:**
> We recommend importing the file from within the `register` function, rather than at the top of the file. By doing this, you can colocate all of your side effects in one place in your code, and avoid any unintended consequences from importing globally at the top of the file.
### Importing runtime-specific code
Next.js calls `register` in all environments, so it's important to conditionally import any code that doesn't support specific runtimes (e.g. Edge or Node.js). You can use the `NEXT_RUNTIME` environment variable to get the current environment:
instrumentation.ts
```
exportasyncfunctionregister() {
if (process.env.NEXT_RUNTIME==='nodejs') {
awaitimport('./instrumentation-node')
 }
if (process.env.NEXT_RUNTIME==='edge') {
awaitimport('./instrumentation-edge')
 }
}
```
