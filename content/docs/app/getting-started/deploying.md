---
title: "How to deploy your Next.js application"
path: "App / Getting Started / Deploying"
source_url: https://nextjs.org/docs/app/getting-started/deploying
content_length: 1950
---

# How to deploy your Next.js application
Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms.
Deployment Option| Feature Support  
---|---  
Node.js server| All  
Docker container| All  
Static export| Limited  
Adapters| Platform-specific  
## Node.js server
Next.js can be deployed to any provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start"
 }
}
```

Then, run `npm run build` to build your application and `npm run start` to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a custom server.
Node.js deployments support all Next.js features. Learn how to configure them for your infrastructure.
### Templates
## Docker
Next.js can be deployed to any provider that supports containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker.
Docker deployments support all Next.js features. Learn how to configure them for your infrastructure.
### Templates
## Static export
Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.
Since Next.js supports static exports, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.
Running as a static export **does not** support Next.js features that require a server. Learn more.
### Templates
## Adapters
Next.js can be adapted to run on different platforms to support their infrastructure capabilities.
Refer to each provider's documentation for information on supported Next.js features:
> **Note:** We are working on a for all platforms to adopt. After completion, we will add documentation on how to write your own adapters.
