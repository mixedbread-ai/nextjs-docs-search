---
title: Env
path: "App / Api Reference / Config / Next Config Js / Env"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/env
content_length: 1225
---

# env
This is a legacy API and no longer recommended. It's still supported for backward compatibility.
> Since the release of Next.js 9.4 we now have a more intuitive and ergonomic experience for adding environment variables. Give it a try!
> **Good to know** : environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them through the environment or .env files.
To add environment variables to the JavaScript bundle, open `next.config.js` and add the `env` config:
next.config.js
```
module.exports= {
 env: {
  customKey:'my-value',
 },
}
```

Now you can access `process.env.customKey` in your code. For example:
```
functionPage() {
return <h1>The value of customKey is: {process.env.customKey}</h1>
}
exportdefault Page
```

Next.js will replace `process.env.customKey` with `'my-value'` at build time. Trying to destructure `process.env` variables won't work due to the nature of webpack .
For example, the following line:
```
return <h1>The value of customKey is: {process.env.customKey}</h1>
```

Will end up being:
```
return <h1>The value of customKey is: {'my-value'}</h1>
```
