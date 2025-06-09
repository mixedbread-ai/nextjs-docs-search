---
title: "How to implement JSON-LD in your Next.js application"
path: "App / Guides / Json Ld"
source_url: https://nextjs.org/docs/app/guides/json-ld
content_length: 1793
---

# How to implement JSON-LD in your Next.js application
is a format for structured data that can be used by search engines and AI to to help them understand the structure of the page beyond pure content. For example, you can use it to describe a person, an event, an organization, a movie, a book, a recipe, and many other types of entities.
Our current recommendation for JSON-LD is to render structured data as a `<script>` tag in your `layout.js` or `page.js` components.
The following snippet uses `JSON.stringify`, which does not sanitize malicious strings used in XSS injection. To prevent this type of vulnerability, you can scrub `HTML` tags from the `JSON-LD` payload, for example, by replacing the character, `<`, with its unicode equivalent, `\u003c`.
Review your organization's recommended approach to sanitize potentially dangerous strings, or use community maintained alternatives for `JSON.stringify` such as, .
app/products/[id]/page.tsx
```
exportdefaultasyncfunctionPage({ params }) {
const { id } =await params
constproduct=awaitgetProduct(id)
constjsonLd= {
'@context':'
'@type':'Product',
  name:product.name,
  image:product.image,
  description:product.description,
 }
return (
  <section>
   {/* Add JSON-LD to your page */}
   <script
type="application/ld+json"
dangerouslySetInnerHTML={{
     __html:JSON.stringify(jsonLd).replace(/</g,'\\u003c'),
    }}
   />
   {/* ... */}
  </section>
 )
}
```

You can validate and test your structured data with the for Google or the generic .
You can type your JSON-LD with TypeScript using community packages like :
```
import { Product, WithContext } from'schema-dts'
constjsonLd:WithContext<Product> = {
'@context':'
'@type':'Product',
 name:'Next.js Sticker',
 image:'
 description:'Dynamic at the speed of static.',
}
```
