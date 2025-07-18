---
title: "Next CLI"
path: "App / Api Reference / Cli / Next"
source_url: https://nextjs.org/docs/app/api-reference/cli/next
content_length: 10783
---

# next CLI
The Next.js CLI allows you to develop, build, start your application, and more.
Basic usage:
Terminal
```
npxnext [command] [options]
```

## Reference
The following options are available:
Options| Description  
---|---  
`-h` or `--help`| Shows all available options  
`-v` or `--version`| Outputs the Next.js version number  
### Commands
The following commands are available:
Command| Description  
---|---  
`dev`| Starts Next.js in development mode with Hot Module Reloading, error reporting, and more.  
`build`| Creates an optimized production build of your application. Displaying information about each route.  
`start`| Starts Next.js in production mode. The application should be compiled with `next build` first.  
`info`| Prints relevant details about the current system which can be used to report Next.js bugs.  
`lint`| Runs ESLint for all files in the `/src`, `/app`, `/pages`, `/components`, and `/lib` directories. It also provides a guided setup to install any required dependencies if ESLint it is not already configured in your application.  
`telemetry`| Allows you to enable or disable Next.js' completely anonymous telemetry collection.  
> **Good to know** : Running `next` without a command is an alias for `next dev`.
### `next dev` options
`next dev` starts the application in development mode with Hot Module Reloading (HMR), error reporting, and more. The following options are available when running `next dev`:
Option| Description  
---|---  
`-h, --help`| Show all available options.  
`[directory]`| A directory in which to build the application. If not provided, current directory is used.  
`--turbopack`| Starts development mode using Turbopack.  
`-p` or `--port <port>`| Specify a port number on which to start the application. Default: 3000, env: PORT  
`-H`or `--hostname <hostname>`| Specify a hostname on which to start the application. Useful for making the application available for other devices on the network. Default: 0.0.0.0  
`--experimental-https`| Starts the server with HTTPS and generates a self-signed certificate.  
`--experimental-https-key <path>`| Path to a HTTPS key file.  
`--experimental-https-cert <path>`| Path to a HTTPS certificate file.  
`--experimental-https-ca <path>`| Path to a HTTPS certificate authority file.  
`--experimental-upload-trace <traceUrl>`| Reports a subset of the debugging trace to a remote HTTP URL.  
### `next build` options
`next build` creates an optimized production build of your application. The output displays information about each route. For example:
Terminal
```
Route (app)               Size   First Load JS
┌○/_not-found0B0kB
└ƒ/products/[id]0B0kB
○ (Static)  prerendered as static content
ƒ (Dynamic) server-rendered on demand
```

  * **Size** : The size of assets downloaded when navigating to the page client-side. The size for each route only includes its dependencies.
  * **First Load JS** : The size of assets downloaded when visiting the page from the server. The amount of JS shared by all is shown as a separate metric.


Both of these values are **compressed with gzip**. The first load is indicated by green, yellow, or red. Aim for green for performant applications.
The following options are available for the `next build` command:
Option| Description  
---|---  
`-h, --help`| Show all available options.  
`[directory]`| A directory on which to build the application. If not provided, the current directory will be used.  
`-d` or `--debug`| Enables a more verbose build output. With this flag enabled additional build output like rewrites, redirects, and headers will be shown.  
|   
`--profile`| Enables production .  
`--no-lint`| Disables linting.  
`--no-mangling`| Disables . This may affect performance and should only be used for debugging purposes.  
`--experimental-app-only`| Builds only App Router routes.  
`--experimental-build-mode [mode]`| Uses an experimental build mode. (choices: "compile", "generate", default: "default")  
### `next start` options
`next start` starts the application in production mode. The application should be compiled with `next build` first.
The following options are available for the `next start` command:
Option| Description  
---|---  
`-h` or `--help`| Show all available options.  
`[directory]`| A directory on which to start the application. If no directory is provided, the current directory will be used.  
`-p` or `--port <port>`| Specify a port number on which to start the application. (default: 3000, env: PORT)  
`-H` or `--hostname <hostname>`| Specify a hostname on which to start the application (default: 0.0.0.0).  
`--keepAliveTimeout <keepAliveTimeout>`| Specify the maximum amount of milliseconds to wait before closing the inactive connections.  
### `next info` options
`next info` prints relevant details about the current system which can be used to report Next.js bugs when opening a . This information includes Operating System platform/arch/version, Binaries (Node.js, npm, Yarn, pnpm), package versions (`next`, `react`, `react-dom`), and more.
The output should look like this:
Terminal
```
OperatingSystem:
Platform:darwin
Arch:arm64
Version:DarwinKernelVersion23.6.0
Availablememory (MB): 65536
AvailableCPUcores:10
Binaries:
Node:20.12.0
npm:10.5.0
Yarn:1.22.19
pnpm:9.6.0
RelevantPackages:
next:15.0.0-canary.115//Latestavailableversionisdetected (15.0.0-canary.115).
eslint-config-next:14.2.5
react:19.0.0-rc
react-dom:19.0.0
typescript:5.5.4
Next.jsConfig:
output:N/A
```

The following options are available for the `next info` command:
Option| Description  
---|---  
`-h` or `--help`| Show all available options  
`--verbose`| Collects additional information for debugging.  
### `next lint` options
`next lint` runs ESLint for all files in the `pages/`, `app/`, `components/`, `lib/`, and `src/` directories. It also provides a guided setup to install any required dependencies if ESLint is not already configured in your application.
The following options are available for the `next lint` command:
Option| Description  
---|---  
`[directory]`| A base directory on which to lint the application. If not provided, the current directory will be used.  
`-d, --dir, <dirs...>`| Include directory, or directories, to run ESLint.  
`--file, <files...>`| Include file, or files, to run ESLint.  
`--ext, [exts...]`| Specify JavaScript file extensions. (default: [".js", ".mjs", ".cjs", ".jsx", ".ts", ".mts", ".cts", ".tsx"])  
`-c, --config, <config>`| Uses this configuration file, overriding all other configuration options.  
`--resolve-plugins-relative-to, <rprt>`| Specify a directory where plugins should be resolved from.  
`--strict`| Creates a `.eslintrc.json` file using the Next.js strict configuration.  
`--rulesdir, <rulesdir...>`| Uses additional rules from this directory(s).  
`--fix`| Automatically fix linting issues.  
`--fix-type <fixType>`| Specify the types of fixes to apply (e.g., problem, suggestion, layout).  
`--ignore-path <path>`| Specify a file to ignore.  
`--no-ignore <path>`| Disables the `--ignore-path` option.  
`--quiet`| Reports errors only.  
`--max-warnings [maxWarnings]`| Specify the number of warnings before triggering a non-zero exit code. (default: -1)  
`-o, --output-file, <outputFile>`| Specify a file to write report to.  
`-f, --format, <format>`| Uses a specific output format.  
`--no-inline-config`| Prevents comments from changing config or rules.  
`--report-unused-disable-directives-severity <level>`| Specify severity level for unused eslint-disable directives. (choices: "error", "off", "warn")  
`--no-cache`| Disables caching.  
`--cache-location, <cacheLocation>`| Specify a location for cache.  
`--cache-strategy, [cacheStrategy]`| Specify a strategy to use for detecting changed files in the cache. (default: "metadata")  
`--error-on-unmatched-pattern`| Reports errors when any file patterns are unmatched.  
`-h, --help`| Displays this message.  
### `next telemetry` options
Next.js collects **completely anonymous** telemetry data about general usage. Participation in this anonymous program is optional, and you can opt-out if you prefer not to share information.
The following options are available for the `next telemetry` command:
Option| Description  
---|---  
`-h, --help`| Show all available options.  
`--enable`| Enables Next.js' telemetry collection.  
`--disable`| Disables Next.js' telemetry collection.  
Learn more about Telemetry.
## Examples
### Changing the default port
By default, Next.js uses `` during development and with `next start`. The default port can be changed with the `-p` option, like so:
Terminal
```
nextdev-p4000
```

Or using the `PORT` environment variable:
Terminal
```
PORT=4000nextdev
```

> **Good to know** : `PORT` cannot be set in `.env` as booting up the HTTP server happens before any other code is initialized.
### Using HTTPS during development
For certain use cases like webhooks or authentication, you can use to have a secure environment on `localhost`. Next.js can generate a self-signed certificate with `next dev` using the `--experimental-https` flag:
Terminal
```
nextdev--experimental-https
```

With the generated certificate, the Next.js development server will exist at ``. The default port `3000` is used unless a port is specified with `-p`, `--port`, or `PORT`.
You can also provide a custom certificate and key with `--experimental-https-key` and `--experimental-https-cert`. Optionally, you can provide a custom CA certificate with `--experimental-https-ca` as well.
Terminal
```
nextdev--experimental-https--experimental-https-key./certificates/localhost-key.pem--experimental-https-cert./certificates/localhost.pem
```

`next dev --experimental-https` is only intended for development and creates a locally trusted certificate with . In production, use properly issued certificates from trusted authorities.
### Configuring a timeout for downstream proxies
When deploying Next.js behind a downstream proxy (e.g. a load-balancer like AWS ELB/ALB), it's important to configure Next's underlying HTTP server with that are _larger_ than the downstream proxy's timeouts. Otherwise, once a keep-alive timeout is reached for a given TCP connection, Node.js will immediately terminate that connection without notifying the downstream proxy. This results in a proxy error whenever it attempts to reuse a connection that Node.js has already terminated.
To configure the timeout values for the production Next.js server, pass `--keepAliveTimeout` (in milliseconds) to `next start`, like so:
Terminal
```
nextstart--keepAliveTimeout70000
```

### Passing Node.js arguments
You can pass any to `next` commands. For example:
Terminal
```
NODE_OPTIONS='--throw-deprecation'next
NODE_OPTIONS='-r esm'next
NODE_OPTIONS='--inspect'next
```
