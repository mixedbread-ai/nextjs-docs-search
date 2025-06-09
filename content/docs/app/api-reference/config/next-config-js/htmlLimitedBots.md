---
title: HtmlLimitedBots
path: "App / Api Reference / Config / Next Config Js / Htmllimitedbots"
source_url: https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots
content_length: 713
---

# htmlLimitedBots
The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of streaming metadata.
next.config.ts
```
importtype { NextConfig } from'next'
constconfig:NextConfig= {
 htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
exportdefault config
```

## Default list
Next.js includes .
Specifying a `htmlLimitedBots` config will override the Next.js' default list, allowing you full control over what user agents should opt into this behavior. However, this is advanced behavior, and the default should be sufficient for most cases.
## Version History
Version| Changes  
---|---  
15.2.0| `htmlLimitedBots` option introduced.
