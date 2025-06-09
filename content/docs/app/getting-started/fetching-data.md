---
title: "How to fetch data and stream"
path: "App / Getting Started / Fetching Data"
source_url: https://nextjs.org/docs/app/getting-started/fetching-data
content_length: 11926
---

# How to fetch data and stream
This page will walk you through how you can fetch data in Server and Client Components, and how to stream components that depend on data.
## Fetching data
### Server Components
You can fetch data in Server Components using:
  1. The `fetch` API
  2. An ORM or database


#### With the `fetch` API
To fetch data with the `fetch` API, turn your component into an asynchronous function, and await the `fetch` call. For example:
app/blog/page.tsx
```
exportdefaultasyncfunctionPage() {
constdata=awaitfetch('
constposts=awaitdata.json()
return (
  <ul>
   {posts.map((post) => (
    <likey={post.id}>{post.title}</li>
   ))}
  </ul>
 )
}
```

> **Good to know:**
>   * `fetch` responses are not cached by default. However, Next.js will prerender the route and the output will be cached for improved performance. If you'd like to opt into dynamic rendering, use the `{ cache: 'no-store' }` option. See the `fetch` API Reference.
>   * During development, you can log `fetch` calls for better visibility and debugging. See the `logging` API reference.
> 

#### With an ORM or database
Since Server Components are rendered on the server, you can safely make database queries using an ORM or database client. Turn your component into an asynchronous function, and await the call:
app/blog/page.tsx
```
import { db, posts } from'@/lib/db'
exportdefaultasyncfunctionPage() {
constallPosts=awaitdb.select().from(posts)
return (
  <ul>
   {allPosts.map((post) => (
    <likey={post.id}>{post.title}</li>
   ))}
  </ul>
 )
}
```

### Client Components
There are two ways to fetch data in Client Components, using:
  1. React's 
  2. A community library like or 


#### Streaming data with the `use` hook
You can use React's to stream data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:
app/blog/page.tsx
```
import Posts from'@/app/ui/posts
import { Suspense } from'react'
exportdefaultfunctionPage() {
// Don't await the data fetching function
constposts=getPosts()
return (
  <Suspensefallback={<div>Loading...</div>}>
   <Postsposts={posts} />
  </Suspense>
 )
}
```

Then, in your Client Component, use the `use` hook to read the promise:
app/ui/posts.tsx
```
'use client'
import { use } from'react'
exportdefaultfunctionPosts({
 posts,
}: {
 posts:Promise<{ id:string; title:string }[]>
}) {
constallPosts=use(posts)
return (
  <ul>
   {allPosts.map((post) => (
    <likey={post.id}>{post.title}</li>
   ))}
  </ul>
 )
}
```

In the example above, the `<Posts>` component is wrapped in a . This means the fallback will be shown while the promise is being resolved. Learn more about streaming.
#### Community libraries
You can use a community library like or to fetch data in Client Components. These libraries have their own semantics for caching, streaming, and other features. For example, with SWR:
app/blog/page.tsx
```
'use client'
import useSWR from'swr'
constfetcher= (url) =>fetch(url).then((r) =>r.json())
exportdefaultfunctionBlogPage() {
const { data,error,isLoading } =useSWR(
'
  fetcher
 )
if (isLoading) return <div>Loading...</div>
if (error) return <div>Error: {error.message}</div>
return (
  <ul>
   {data.map((post: { id:string; title:string }) => (
    <likey={post.id}>{post.title}</li>
   ))}
  </ul>
 )
}
```

## Deduplicating requests with `React.cache`
Deduplication is the process of _preventing duplicate requests_ for the same resource during a render pass. It allows you to fetch the same data in different components while preventing multiple network requests to your data source.
If you are using `fetch`, requests can be deduplicated by adding `cache: 'force-cache'`. This means you can safely call the same URL with the same options, and only one request will be made.
If you are _not_ using `fetch`, and instead using an ORM or database directly, you can wrap your data fetch with the function.
app/lib/data.ts
```
import { cache } from'react'
import { db, posts, eq } from'@/lib/db'
exportconstgetPost=cache(async (id:string) => {
constpost=awaitdb.query.posts.findFirst({
  where:eq(posts.id,parseInt(id)),
 })
})
```

## Streaming
> **Warning:** The content below assumes the `dynamicIO` config option is enabled in your application. The flag was introduced in Next.js 15 canary.
When using `async/await` in Server Components, Next.js will opt into dynamic rendering. This means the data will be fetched and rendered on the server for every user request. If there are any slow data requests, the whole route will be blocked from rendering.
To improve the initial load time and user experience, you can use streaming to break up the page's HTML into smaller chunks and progressively send those chunks from the server to the client.
!How Server Rendering with Streaming Works!How Server Rendering with Streaming Works
There are two ways you can implement streaming in your application:
  1. Wrapping a page with a `loading.js` file
  2. Wrapping a component with `<Suspense>`


### With `loading.js`
You can create a `loading.js` file in the same folder as your page to stream the **entire page** while the data is being fetched. For example, to stream `app/blog/page.js`, add the file inside the `app/blog` folder.
!Blog folder structure with loading.js file!Blog folder structure with loading.js file
app/blog/loading.tsx
```
exportdefaultfunctionLoading() {
// Define the Loading UI here
return <div>Loading...</div>
}
```

On navigation, the user will immediately see the layout and a loading state while the page is being rendered. The new content will then be automatically swapped in once rendering is complete.
!Loading UI!Loading UI
Behind-the-scenes, `loading.js` will be nested inside `layout.js`, and will automatically wrap the `page.js` file and any children below in a `<Suspense>` boundary.
!loading.js overview!loading.js overview
This approach works well for route segments (layouts and pages), but for more granular streaming, you can use `<Suspense>`.
### With `<Suspense>`
`<Suspense>` allows you to be more granular about what parts of the page to stream. For example, you can immediately show any page content that falls outside of the `<Suspense>` boundary, and stream in the list of blog posts inside the boundary.
app/blog/page.tsx
```
import { Suspense } from'react'
import BlogList from'@/components/BlogList'
import BlogListSkeleton from'@/components/BlogListSkeleton'
exportdefaultfunctionBlogPage() {
return (
  <div>
   {/* This content will be sent to the client immediately */}
   <header>
    <h1>Welcome to the Blog</h1>
    <p>Read the latest posts below.</p>
   </header>
   <main>
    {/* Any content wrapped in a <Suspense> boundary will be streamed */}
    <Suspensefallback={<BlogListSkeleton />}>
     <BlogList />
    </Suspense>
   </main>
  </div>
 )
}
```

### Creating meaningful loading states
An instant loading state is fallback UI that is shown immediately to the user after navigation. For the best user experience, we recommend designing loading states that are meaningful and help users understand the app is responding. For example, you can use skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc.
In development, you can preview and inspect the loading state of your components using the .
## Examples
### Sequential data fetching
Sequential data fetching happens when nested components in a tree each fetch their own data and the requests are not deduplicated, leading to longer response times.
!Sequential and Parallel Data Fetching!Sequential and Parallel Data Fetching
There may be cases where you want this pattern because one fetch depends on the result of the other.
For example, the `<Playlists>` component will only start fetching data once the `<Artist>` component has finished fetching data because `<Playlists>` depends on the `artistID` prop:
app/artist/[username]/page.tsx
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ username:string }>
}) {
const { username } =await params
// Get artist information
constartist=awaitgetArtist(username)
return (
  <>
   <h1>{artist.name}</h1>
   {/* Show fallback UI while the Playlists component is loading */}
   <Suspensefallback={<div>Loading...</div>}>
    {/* Pass the artist ID to the Playlists component */}
    <PlaylistsartistID={artist.id} />
   </Suspense>
  </>
 )
}
asyncfunctionPlaylists({ artistID }: { artistID:string }) {
// Use the artist ID to fetch playlists
constplaylists=awaitgetArtistPlaylists(artistID)
return (
  <ul>
   {playlists.map((playlist) => (
    <likey={playlist.id}>{playlist.name}</li>
   ))}
  </ul>
 )
}
```

To improve the user experience, you should use React `<Suspense>` to show a `fallback` while data is being fetch. This will enable streaming and prevent the whole route from being blocked by the sequential data requests.
### Parallel data fetching
Parallel data fetching happens when data requests in a route are eagerly initiated and start at the same time.
By default, layouts and pages are rendered in parallel. So each segment starts fetching data as soon as possible.
However, within _any_ component, multiple `async`/`await` requests can still be sequential if placed after the other. For example, `getAlbums` will be blocked until `getArtist` is resolved:
app/artist/[username]/page.tsx
```
import { getArtist, getAlbums } from'@/app/lib/data'
exportdefaultasyncfunctionPage({ params }) {
// These requests will be sequential
const { username } =await params
constartist=awaitgetArtist(username)
constalbums=awaitgetAlbums(username)
return <div>{artist.name}</div>
}
```

You can initiate requests in parallel by defining them outside the components that use the data, and resolving them together, for example, with :
app/artist/[username]/page.tsx
```
import Albums from'./albums'
asyncfunctiongetArtist(username:string) {
constres=awaitfetch(`{username}`)
returnres.json()
}
asyncfunctiongetAlbums(username:string) {
constres=awaitfetch(`{username}/albums`)
returnres.json()
}
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ username:string }>
}) {
const { username } =await params
constartistData=getArtist(username)
constalbumsData=getAlbums(username)
// Initiate both requests in parallel
const [artist,albums] =awaitPromise.all([artistData, albumsData])
return (
  <>
   <h1>{artist.name}</h1>
   <Albumslist={albums} />
  </>
 )
}
```

> **Good to know:** If one request fails when using `Promise.all`, the entire operation will fail. To handle this, you can use the method instead.
### Preloading data
You can preload data by creating an utility function that you eagerly call above blocking requests. `<Item>` conditionally renders based on the `checkIsAvailable()` function.
You can call `preload()` before `checkIsAvailable()` to eagerly initiate `<Item/>` data dependencies. By the time `<Item/>` is rendered, its data has already been fetched.
app/item/[id]/page.tsx
```
import { getItem } from'@/lib/data'
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
// starting loading item data
preload(id)
// perform another asynchronous task
constisAvailable=awaitcheckIsAvailable()
return isAvailable ? <Itemid={id} /> :null
}
exportconstpreload= (id:string) => {
// void evaluates the given expression and returns undefined
// 
voidgetItem(id)
}
exportasyncfunctionItem({ id }: { id:string }) {
constresult=awaitgetItem(id)
// ...
}
```

Additionally, you can use React's and the to create a reusable utility function. This approach allows you to cache the data fetching function and ensure that it's only executed on the server.
utils/get-item.ts
```
import { cache } from'react'
import'server-only'
import { getItem } from'@/lib/data'
exportconstpreload= (id:string) => {
voidgetItem(id)
}
exportconstgetItem=cache(async (id:string) => {
// ...
})
```
