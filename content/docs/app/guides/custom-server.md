---
title: "How to set up a custom server in Next.js"
path: "App / Guides / Custom Server"
source_url: https://nextjs.org/docs/app/guides/custom-server
content_length: 2892
---

# How to set up a custom server in Next.js
Next.js includes its own server with `next start` by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server). A custom Next.js server allows you to programmatically start a server for custom patterns. The majority of the time, you will not need this approach. However, it's available if you need to eject.
> **Good to know** :
>   * Before deciding to use a custom server, keep in mind that it should only be used when the integrated router of Next.js can't meet your app requirements. A custom server will remove important performance optimizations, like **Automatic Static Optimization.**
>   * When using standalone output mode, it does not trace custom server files. This mode outputs a separate minimal `server.js` file, instead. These cannot be used together.
> 

Take a look at the of a custom server:
server.ts
```
import { createServer } from'http'
import { parse } from'url'
import next from'next'
constport=parseInt(process.env.PORT||'3000',10)
constdev=process.env.NODE_ENV!=='production'
constapp=next({ dev })
consthandle=app.getRequestHandler()
app.prepare().then(() => {
createServer((req, res) => {
constparsedUrl=parse(req.url!,true)
handle(req, res, parsedUrl)
 }).listen(port)
console.log(
`> Server listening at {port} as ${
   dev ?'development':process.env.NODE_ENV
}`
 )
})
```

> `server.js` does not run through the Next.js Compiler or bundling process. Make sure the syntax and source code this file requires are compatible with the current Node.js version you are using. .
To run the custom server, you'll need to update the `scripts` in `package.json` like so:
package.json
```
{
"scripts": {
"dev":"node server.js",
"build":"next build",
"start":"NODE_ENV=production node server.js"
 }
}
```

Alternatively, you can set up `nodemon` (). The custom server uses the following import to connect the server with the Next.js application:
```
import next from'next'
constapp=next({})
```

The above `next` import is a function that receives an object with the following options:
Option| Type| Description  
---|---|---  
`conf`| `Object`| The same object you would use in `next.config.js`. Defaults to `{}`  
`dev`| `Boolean`| (_Optional_) Whether or not to launch Next.js in dev mode. Defaults to `false`  
`dir`| `String`| (_Optional_) Location of the Next.js project. Defaults to `'.'`  
`quiet`| `Boolean`| (_Optional_) Hide error messages containing server information. Defaults to `false`  
`hostname`| `String`| (_Optional_) The hostname the server is running behind  
`port`| `Number`| (_Optional_) The port the server is running behind  
`httpServer`| `node:http#Server`| (_Optional_) The HTTP Server that Next.js is running behind  
`turbo`| `Boolean`| (_Optional_) Enable Turbopack  
The returned `app` can then be used to let Next.js handle requests as required.
