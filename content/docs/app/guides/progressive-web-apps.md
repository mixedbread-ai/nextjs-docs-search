---
title: "How to build a Progressive Web Application (PWA) with Next.js"
path: "App / Guides / Progressive Web Apps"
source_url: https://nextjs.org/docs/app/guides/progressive-web-apps
content_length: 13862
---

# How to build a Progressive Web Application (PWA) with Next.js
Progressive Web Applications (PWAs) offer the reach and accessibility of web applications combined with the features and user experience of native mobile apps. With Next.js, you can create PWAs that provide a seamless, app-like experience across all platforms without the need for multiple codebases or app store approvals.
PWAs allow you to:
  * Deploy updates instantly without waiting for app store approval
  * Create cross-platform applications with a single codebase
  * Provide native-like features such as home screen installation and push notifications


## Creating a PWA with Next.js
### 1. Creating the Web App Manifest
Next.js provides built-in support for creating a web app manifest using the App Router. You can create either a static or dynamic manifest file:
For example, create a `app/manifest.ts` or `app/manifest.json` file:
app/manifest.ts
```
importtype { MetadataRoute } from'next'
exportdefaultfunctionmanifest():MetadataRoute.Manifest {
return {
  name:'Next.js PWA',
  short_name:'NextPWA',
  description:'A Progressive Web App built with Next.js',
  start_url:'/',
  display:'standalone',
  background_color:'#ffffff',
  theme_color:'#000000',
  icons: [
   {
    src:'/icon-192x192.png',
    sizes:'192x192',
    type:'image/png',
   },
   {
    src:'/icon-512x512.png',
    sizes:'512x512',
    type:'image/png',
   },
  ],
 }
}
```

This file should contain information about the name, icons, and how it should be displayed as an icon on the user's device. This will allow users to install your PWA on their home screen, providing a native app-like experience.
You can use tools like to create the different icon sets and place the generated files in your `public/` folder.
### 2. Implementing Web Push Notifications
Web Push Notifications are supported with all modern browsers, including:
  * iOS 16.4+ for applications installed to the home screen
  * Safari 16 for macOS 13 or later
  * Chromium based browsers
  * Firefox


This makes PWAs a viable alternative to native apps. Notably, you can trigger install prompts without needing offline support.
Web Push Notifications allow you to re-engage users even when they're not actively using your app. Here's how to implement them in a Next.js application:
First, let's create the main page component in `app/page.tsx`. We'll break it down into smaller parts for better understanding. First, we’ll add some of the imports and utilities we’ll need. It’s okay that the referenced Server Actions do not yet exist:
```
'use client'
import { useState, useEffect } from'react'
import { subscribeUser, unsubscribeUser, sendNotification } from'./actions'
functionurlBase64ToUint8Array(base64String:string) {
constpadding='='.repeat((4- (base64String.length%4)) %4)
constbase64= (base64String + padding).replace(/-/g,'+').replace(/_/g,'/')
constrawData=window.atob(base64)
constoutputArray=newUint8Array(rawData.length)
for (let i =0; i <rawData.length; ++i) {
  outputArray[i] =rawData.charCodeAt(i)
 }
return outputArray
}
```

Let’s now add a component to manage subscribing, unsubscribing, and sending push notifications.
```
functionPushNotificationManager() {
const [isSupported,setIsSupported] =useState(false)
const [subscription,setSubscription] =useState<PushSubscription|null>(
null
 )
const [message,setMessage] =useState('')
useEffect(() => {
if ('serviceWorker'in navigator &&'PushManager'in window) {
setIsSupported(true)
registerServiceWorker()
  }
 }, [])
asyncfunctionregisterServiceWorker() {
constregistration=awaitnavigator.serviceWorker.register('/sw.js', {
   scope:'/',
   updateViaCache:'none',
  })
constsub=awaitregistration.pushManager.getSubscription()
setSubscription(sub)
 }
asyncfunctionsubscribeToPush() {
constregistration=awaitnavigator.serviceWorker.ready
constsub=awaitregistration.pushManager.subscribe({
   userVisibleOnly:true,
   applicationServerKey:urlBase64ToUint8Array(
process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!
   ),
  })
setSubscription(sub)
constserializedSub=JSON.parse(JSON.stringify(sub))
awaitsubscribeUser(serializedSub)
 }
asyncfunctionunsubscribeFromPush() {
awaitsubscription?.unsubscribe()
setSubscription(null)
awaitunsubscribeUser()
 }
asyncfunctionsendTestNotification() {
if (subscription) {
awaitsendNotification(message)
setMessage('')
  }
 }
if (!isSupported) {
return <p>Push notifications are not supported in this browser.</p>
 }
return (
  <div>
   <h3>Push Notifications</h3>
   {subscription ? (
    <>
     <p>You are subscribed to push notifications.</p>
     <buttononClick={unsubscribeFromPush}>Unsubscribe</button>
     <input
type="text"
placeholder="Enter notification message"
value={message}
onChange={(e) =>setMessage(e.target.value)}
     />
     <buttononClick={sendTestNotification}>Send Test</button>
    </>
   ) : (
    <>
     <p>You are not subscribed to push notifications.</p>
     <buttononClick={subscribeToPush}>Subscribe</button>
    </>
   )}
  </div>
 )
}
```

Finally, let’s create a component to show a message for iOS devices to instruct them to install to their home screen, and only show this if the app is not already installed.
```
functionInstallPrompt() {
const [isIOS,setIsIOS] =useState(false)
const [isStandalone,setIsStandalone] =useState(false)
useEffect(() => {
setIsIOS(
/iPad|iPhone|iPod/.test(navigator.userAgent) &&!(window asany).MSStream
  )
setIsStandalone(window.matchMedia('(display-mode: standalone)').matches)
 }, [])
if (isStandalone) {
returnnull// Don't show install button if already installed
 }
return (
  <div>
   <h3>Install App</h3>
   <button>Add to Home Screen</button>
   {isIOS && (
    <p>
     To install this app on your iOS device, tap the share button
     <spanrole="img"aria-label="share icon">
      {' '}
      ⎋{' '}
     </span>
     and then "Add to Home Screen"
     <spanrole="img"aria-label="plus icon">
      {' '}
      ➕{' '}
     </span>.
    </p>
   )}
  </div>
 )
}
exportdefaultfunctionPage() {
return (
  <div>
   <PushNotificationManager />
   <InstallPrompt />
  </div>
 )
}
```

Now, let’s create the Server Actions which this file calls.
### 3. Implementing Server Actions
Create a new file to contain your actions at `app/actions.ts`. This file will handle creating subscriptions, deleting subscriptions, and sending notifications.
app/actions.ts
```
'use server'
import webpush from'web-push'
webpush.setVapidDetails(
'<mailto:your-email@example.com>',
process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!,
process.env.VAPID_PRIVATE_KEY!
)
let subscription:PushSubscription|null=null
exportasyncfunctionsubscribeUser(sub:PushSubscription) {
 subscription = sub
// In a production environment, you would want to store the subscription in a database
// For example: await db.subscriptions.create({ data: sub })
return { success:true }
}
exportasyncfunctionunsubscribeUser() {
 subscription =null
// In a production environment, you would want to remove the subscription from the database
// For example: await db.subscriptions.delete({ where: { ... } })
return { success:true }
}
exportasyncfunctionsendNotification(message:string) {
if (!subscription) {
thrownewError('No subscription available')
 }
try {
awaitwebpush.sendNotification(
   subscription,
JSON.stringify({
    title:'Test Notification',
    body: message,
    icon:'/icon.png',
   })
  )
return { success:true }
 } catch (error) {
console.error('Error sending push notification:', error)
return { success:false, error:'Failed to send notification' }
 }
}
```

Sending a notification will be handled by our service worker, created in step 5.
In a production environment, you would want to store the subscription in a database for persistence across server restarts and to manage multiple users' subscriptions.
### 4. Generating VAPID Keys
To use the Web Push API, you need to generate keys. The simplest way is to use the web-push CLI directly:
First, install web-push globally:
Terminal
```
npminstall-gweb-push
```

Generate the VAPID keys by running:
Terminal
```
web-pushgenerate-vapid-keys
```

Copy the output and paste the keys into your `.env` file:
```
NEXT_PUBLIC_VAPID_PUBLIC_KEY=your_public_key_here
VAPID_PRIVATE_KEY=your_private_key_here
```

### 5. Creating a Service Worker
Create a `public/sw.js` file for your service worker:
public/sw.js
```
self.addEventListener('push',function (event) {
if (event.data) {
constdata=event.data.json()
constoptions= {
   body:data.body,
   icon:data.icon ||'/icon.png',
   badge:'/badge.png',
   vibrate: [100,50,100],
   data: {
    dateOfArrival:Date.now(),
    primaryKey:'2',
   },
  }
event.waitUntil(self.registration.showNotification(data.title, options))
 }
})
self.addEventListener('notificationclick',function (event) {
console.log('Notification click received.')
event.notification.close()
event.waitUntil(clients.openWindow('<>'))
})
```

This service worker supports custom images and notifications. It handles incoming push events and notification clicks.
  * You can set custom icons for notifications using the `icon` and `badge` properties.
  * The `vibrate` pattern can be adjusted to create custom vibration alerts on supported devices.
  * Additional data can be attached to the notification using the `data` property.


Remember to test your service worker thoroughly to ensure it behaves as expected across different devices and browsers. Also, make sure to update the `'` link in the `notificationclick` event listener to the appropriate URL for your application.
### 6. Adding to Home Screen
The `InstallPrompt` component defined in step 2 shows a message for iOS devices to instruct them to install to their home screen.
To ensure your application can be installed to a mobile home screen, you must have:
  1. A valid web app manifest (created in step 1)
  2. The website served over HTTPS


Modern browsers will automatically show an installation prompt to users when these criteria are met. You can provide a custom installation button with , however, we do not recommend this as it is not cross browser and platform (does not work on Safari iOS).
### 7. Testing Locally
To ensure you can view notifications locally, ensure that:
  * You are running locally with HTTPS
    * Use `next dev --experimental-https` for testing
  * Your browser (Chrome, Safari, Firefox) has notifications enabled 
    * When prompted locally, accept permissions to use notifications
    * Ensure notifications are not disabled globally for the entire browser
    * If you are still not seeing notifications, try using another browser to debug


### 8. Securing your application
Security is a crucial aspect of any web application, especially for PWAs. Next.js allows you to configure security headers using the `next.config.js` file. For example:
next.config.js
```
module.exports= {
asyncheaders() {
return [
   {
    source:'/(.*)',
    headers: [
     {
      key:'X-Content-Type-Options',
      value:'nosniff',
     },
     {
      key:'X-Frame-Options',
      value:'DENY',
     },
     {
      key:'Referrer-Policy',
      value:'strict-origin-when-cross-origin',
     },
    ],
   },
   {
    source:'/sw.js',
    headers: [
     {
      key:'Content-Type',
      value:'application/javascript; charset=utf-8',
     },
     {
      key:'Cache-Control',
      value:'no-cache, no-store, must-revalidate',
     },
     {
      key:'Content-Security-Policy',
      value:"default-src 'self'; script-src 'self'",
     },
    ],
   },
  ]
 },
}
```

Let’s go over each of these options:
  1. Global Headers (applied to all routes): 
    1. `X-Content-Type-Options: nosniff`: Prevents MIME type sniffing, reducing the risk of malicious file uploads.
    2. `X-Frame-Options: DENY`: Protects against clickjacking attacks by preventing your site from being embedded in iframes.
    3. `Referrer-Policy: strict-origin-when-cross-origin`: Controls how much referrer information is included with requests, balancing security and functionality.
  2. Service Worker Specific Headers: 
    1. `Content-Type: application/javascript; charset=utf-8`: Ensures the service worker is interpreted correctly as JavaScript.
    2. `Cache-Control: no-cache, no-store, must-revalidate`: Prevents caching of the service worker, ensuring users always get the latest version.
    3. `Content-Security-Policy: default-src 'self'; script-src 'self'`: Implements a strict Content Security Policy for the service worker, only allowing scripts from the same origin.


Learn more about defining Content Security Policies with Next.js.
## Next Steps
  1. **Exploring PWA Capabilities** : PWAs can leverage various web APIs to provide advanced functionality. Consider exploring features like background sync, periodic background sync, or the File System Access API to enhance your application. For inspiration and up-to-date information on PWA capabilities, you can refer to resources like .
  2. **Static Exports:** If your application requires not running a server, and instead using a static export of files, you can update the Next.js configuration to enable this change. Learn more in the Next.js Static Export documentation. However, you will need to move from Server Actions to calling an external API, as well as moving your defined headers to your proxy.
  3. **Offline Support** : To provide offline functionality, one option is with Next.js. You can find an example of how to integrate Serwist with Next.js in their . **Note:** this plugin currently requires webpack configuration.
  4. **Security Considerations** : Ensure that your service worker is properly secured. This includes using HTTPS, validating the source of push messages, and implementing proper error handling.
  5. **User Experience** : Consider implementing progressive enhancement techniques to ensure your app works well even when certain PWA features are not supported by the user's browser.
