---
title: "How to use and optimize videos"
path: "App / Guides / Videos"
source_url: https://nextjs.org/docs/app/guides/videos
content_length: 11882
---

# How to use and optimize videos
This page outlines how to use videos with Next.js applications, showing how to store and display video files without affecting performance.
## Using `<video>` and `<iframe>`
Videos can be embedded on the page using the HTML **`<video>`**tag for direct video files and**`<iframe>`**for external platform-hosted videos.
### `<video>`
The HTML tag can embed self-hosted or directly served video content, allowing full control over the playback and appearance.
app/ui/video.jsx
```
exportfunctionVideo() {
return (
  <videowidth="320"height="240"controlspreload="none">
   <sourcesrc="/path/to/video.mp4"type="video/mp4" />
   <track
src="/path/to/captions.vtt"
kind="subtitles"
srcLang="en"
label="English"
   />
   Your browser does not support the video tag.
  </video>
 )
}
```

### Common `<video>` tag attributes
Attribute| Description| Example Value  
---|---|---  
`src`| Specifies the source of the video file.| `<video src="/path/to/video.mp4" />`  
`width`| Sets the width of the video player.| `<video width="320" />`  
`height`| Sets the height of the video player.| `<video height="240" />`  
`controls`| If present, it displays the default set of playback controls.| `<video controls />`  
`autoPlay`| Automatically starts playing the video when the page loads. Note: Autoplay policies vary across browsers.| `<video autoPlay />`  
`loop`| Loops the video playback.| `<video loop />`  
`muted`| Mutes the audio by default. Often used with `autoPlay`.| `<video muted />`  
`preload`| Specifies how the video is preloaded. Values: `none`, `metadata`, `auto`.| `<video preload="none" />`  
`playsInline`| Enables inline playback on iOS devices, often necessary for autoplay to work on iOS Safari.| `<video playsInline />`  
> **Good to know** : When using the `autoPlay` attribute, it is important to also include the `muted` attribute to ensure the video plays automatically in most browsers and the `playsInline` attribute for compatibility with iOS devices.
For a comprehensive list of video attributes, refer to the .
### Video best practices
  * **Fallback Content:** When using the `<video>` tag, include fallback content inside the tag for browsers that do not support video playback.
  * **Subtitles or Captions:** Include subtitles or captions for users who are deaf or hard of hearing. Utilize the tag with your `<video>` elements to specify caption file sources.
  * **Accessible Controls:** Standard HTML5 video controls are recommended for keyboard navigation and screen reader compatibility. For advanced needs, consider third-party players like or , which offer accessible controls and consistent browser experience.


### `<iframe>`
The HTML `<iframe>` tag allows you to embed videos from external platforms like YouTube or Vimeo.
app/page.jsx
```
exportdefaultfunctionPage() {
return (
  <iframesrc=""allowFullScreen />
 )
}
```

### Common `<iframe>` tag attributes
Attribute| Description| Example Value  
---|---|---  
`src`| The URL of the page to embed.| `<iframe src="" />`  
`width`| Sets the width of the iframe.| `<iframe width="500" />`  
`height`| Sets the height of the iframe.| `<iframe height="300" />`  
`allowFullScreen`| Allows the iframe content to be displayed in full-screen mode.| `<iframe allowFullScreen />`  
`sandbox`| Enables an extra set of restrictions on the content within the iframe.| `<iframe sandbox />`  
`loading`| Optimize loading behavior (e.g., lazy loading).| `<iframe loading="lazy" />`  
`title`| Provides a title for the iframe to support accessibility.| `<iframe title="Description" />`  
For a comprehensive list of iframe attributes, refer to the .
### Choosing a video embedding method
There are two ways you can embed videos in your Next.js application:
  * **Self-hosted or direct video files:** Embed self-hosted videos using the `<video>` tag for scenarios requiring detailed control over the player's functionality and appearance. This integration method within Next.js allows for customization and control of your video content.
  * **Using video hosting services (YouTube, Vimeo, etc.):** For video hosting services like YouTube or Vimeo, you'll embed their iframe-based players using the `<iframe>` tag. While this method limits some control over the player, it offers ease of use and features provided by these platforms.


Choose the embedding method that aligns with your application's requirements and the user experience you aim to deliver.
### Embedding externally hosted videos
To embed videos from external platforms, you can use Next.js to fetch the video information and React Suspense to handle the fallback state while loading.
**1. Create a Server Component for video embedding**
The first step is to create a Server Component that generates the appropriate iframe for embedding the video. This component will fetch the source URL for the video and render the iframe.
app/ui/video-component.jsx
```
exportdefaultasyncfunctionVideoComponent() {
constsrc=awaitgetVideoSrc()
return <iframesrc={src} allowFullScreen />
}
```

**2. Stream the video component using React Suspense**
After creating the Server Component to embed the video, the next step is to stream the component using .
app/page.jsx
```
import { Suspense } from'react'
import VideoComponent from'../ui/VideoComponent.jsx'
exportdefaultfunctionPage() {
return (
  <section>
   <Suspensefallback={<p>Loading video...</p>}>
    <VideoComponent />
   </Suspense>
   {/* Other content of the page */}
  </section>
 )
}
```

> **Good to know** : When embedding videos from external platforms, consider the following best practices:
>   * Ensure the video embeds are responsive. Use CSS to make the iframe or video player adapt to different screen sizes.
>   * Implement based on network conditions, especially for users with limited data plans.
> 

This approach results in a better user experience as it prevents the page from blocking, meaning the user can interact with the page while the video component streams in.
For a more engaging and informative loading experience, consider using a loading skeleton as the fallback UI. So instead of showing a simple loading message, you can show a skeleton that resembles the video player like this:
app/page.jsx
```
import { Suspense } from'react'
import VideoComponent from'../ui/VideoComponent.jsx'
import VideoSkeleton from'../ui/VideoSkeleton.jsx'
exportdefaultfunctionPage() {
return (
  <section>
   <Suspensefallback={<VideoSkeleton />}>
    <VideoComponent />
   </Suspense>
   {/* Other content of the page */}
  </section>
 )
}
```

## Self-hosted videos
Self-hosting videos may be preferable for several reasons:
  * **Complete control and independence** : Self-hosting gives you direct management over your video content, from playback to appearance, ensuring full ownership and control, free from external platform constraints.
  * **Customization for specific needs** : Ideal for unique requirements, like dynamic background videos, it allows for tailored customization to align with design and functional needs.
  * **Performance and scalability considerations** : Choose storage solutions that are both high-performing and scalable, to support increasing traffic and content size effectively.
  * **Cost and integration** : Balance the costs of storage and bandwidth with the need for easy integration into your Next.js framework and broader tech ecosystem.


### Using Vercel Blob for video hosting
offers an efficient way to host videos, providing a scalable cloud storage solution that works well with Next.js. Here's how you can host a video using Vercel Blob:
**1. Uploading a video to Vercel Blob**
In your Vercel dashboard, navigate to the "Storage" tab and select your store. In the Blob table's upper-right corner, find and click the "Upload" button. Then, choose the video file you wish to upload. After the upload completes, the video file will appear in the Blob table.
Alternatively, you can upload your video using a server action. For detailed instructions, refer to the Vercel documentation on . Vercel also supports . This method may be preferable for certain use cases.
**2. Displaying the video in Next.js**
Once the video is uploaded and stored, you can display it in your Next.js application. Here's an example of how to do this using the `<video>` tag and React Suspense:
app/page.jsx
```
import { Suspense } from'react'
import { list } from'@vercel/blob'
exportdefaultfunctionPage() {
return (
  <Suspensefallback={<p>Loading video...</p>}>
   <VideoComponentfileName="my-video.mp4" />
  </Suspense>
 )
}
asyncfunctionVideoComponent({ fileName }) {
const { blobs } =awaitlist({
  prefix: fileName,
  limit:1,
 })
const { url } = blobs[0]
return (
  <videocontrolspreload="none"aria-label="Video player">
   <sourcesrc={url} type="video/mp4" />
   Your browser does not support the video tag.
  </video>
 )
}
```

In this approach, the page uses the video's `@vercel/blob` URL to display the video using the `VideoComponent`. React Suspense is used to show a fallback until the video URL is fetched and the video is ready to be displayed.
### Adding subtitles to your video
If you have subtitles for your video, you can easily add them using the `<track>` element inside your `<video>` tag. You can fetch the subtitle file from in a similar way as the video file. Here's how you can update the `<VideoComponent>` to include subtitles.
app/page.jsx
```
asyncfunctionVideoComponent({ fileName }) {
const { blobs } =awaitlist({
  prefix: fileName,
  limit:2,
 })
const { url } = blobs[0]
const { url: captionsUrl } = blobs[1]
return (
  <videocontrolspreload="none"aria-label="Video player">
   <sourcesrc={url} type="video/mp4" />
   <tracksrc={captionsUrl} kind="subtitles"srcLang="en"label="English" />
   Your browser does not support the video tag.
  </video>
 )
}
```

By following this approach, you can effectively self-host and integrate videos into your Next.js applications.
## Resources
To continue learning more about video optimization and best practices, please refer to the following resources:
  * **Understanding video formats and codecs** : Choose the right format and codec, like MP4 for compatibility or WebM for web optimization, for your video needs. For more details, see .
  * **Video compression** : Use tools like FFmpeg to effectively compress videos, balancing quality with file size. Learn about compression techniques at .
  * **Resolution and bitrate adjustment** : Adjust based on the viewing platform, with lower settings for mobile devices.
  * **Content Delivery Networks (CDNs)** : Utilize a CDN to enhance video delivery speed and manage high traffic. When using some storage solutions, such as Vercel Blob, CDN functionality is automatically handled for you. about CDNs and their benefits.


Explore these video streaming platforms for integrating video into your Next.js projects:
### Open source `next-video` component
  * Provides a `<Video>` component for Next.js, compatible with various hosting services including , S3, Backblaze, and Mux.
  * for using `next-video.dev` with different hosting services.


### Cloudinary Integration
  * Official for using Cloudinary with Next.js.
  * Includes a `<CldVideoPlayer>` component for .
  * Find of integrating Cloudinary with Next.js including .
  * Other including a Node.js SDK are also available.


### Mux Video API
  * Mux provides a for creating a video course with Mux and Next.js.
  * Learn about Mux's recommendations for embedding .
  * Explore an demonstrating Mux with Next.js.


### Fastly
  * Learn more about integrating Fastly's solutions for and streaming media into Next.js.


### ImageKit.io Integration
  * Check out the for integrating ImageKit with Next.js.
  * The integration provides an `<IKVideo>` component, offering .
  * You can also explore other , such as the Node.js SDK, which is also available.
