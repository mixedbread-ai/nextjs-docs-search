---
title: "Edge Runtime"
path: "App / Api Reference / Edge"
source_url: https://nextjs.org/docs/app/api-reference/edge
content_length: 7909
---

# Edge Runtime
Next.js has two server runtimes you can use in your application:
  * The **Node.js Runtime** (default), which has access to all Node.js APIs and is used for rendering your application.
  * The **Edge Runtime** which contains a more limited set of APIs, used in Middleware.


## Caveats
  * The Edge Runtime does not support all Node.js APIs. Some packages may not work as expected.
  * The Edge Runtime does not support Incremental Static Regeneration (ISR).
  * Both runtimes can support streaming depending on your deployment adapter.


## Reference
The Edge Runtime supports the following APIs:
### Network APIs
API| Description  
---|---  
| Represents a blob  
| Fetches a resource  
| Represents a fetch event  
| Represents a file  
| Represents form data  
| Represents HTTP headers  
| Represents an HTTP request  
| Represents an HTTP response  
| Represents URL search parameters  
| Represents a websocket connection  
### Encoding APIs
API| Description  
---|---  
| Decodes a base-64 encoded string  
| Encodes a string in base-64  
| Decodes a Uint8Array into a string  
| Chainable decoder for streams  
| Encodes a string into a Uint8Array  
| Chainable encoder for streams  
### Stream APIs
API| Description  
---|---  
| Represents a readable stream  
| Represents a reader of a ReadableStream  
| Represents a reader of a ReadableStream  
| Represents a transform stream  
| Represents a writable stream  
| Represents a writer of a WritableStream  
### Crypto APIs
API| Description  
---|---  
| Provides access to the cryptographic functionality of the platform  
| Represents a cryptographic key  
| Provides access to common cryptographic primitives, like hashing, signing, encryption or decryption  
### Web Standard APIs
API| Description  
---|---  
| Allows you to abort one or more DOM requests as and when desired  
| Represents an array of values  
| Represents a generic, fixed-length raw binary data buffer  
| Provides atomic operations as static methods  
| Represents a whole number with arbitrary precision  
| Represents a typed array of 64-bit signed integers  
| Represents a typed array of 64-bit unsigned integers  
| Represents a logical entity and can have two values: `true` and `false`  
| Cancels a timed, repeating action which was previously established by a call to `setInterval()`  
| Cancels a timed, repeating action which was previously established by a call to `setTimeout()`  
| Provides access to the browser's debugging console  
| Represents a generic view of an `ArrayBuffer`  
| Represents a single moment in time in a platform-independent format  
| Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI` or by a similar routine  
| Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent` or by a similar routine  
| Represents an error that occurs in the DOM  
| Encodes a Uniform Resource Identifier (URI) by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character  
| Encodes a Uniform Resource Identifier (URI) component by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character  
| Represents an error when trying to execute a statement or accessing a property  
| Represents an error that occurs regarding the global function `eval()`  
| Represents a typed array of 32-bit floating point numbers  
| Represents a typed array of 64-bit floating point numbers  
| Represents a function  
| Represents the mathematical Infinity value  
| Represents a typed array of 8-bit signed integers  
| Represents a typed array of 16-bit signed integers  
| Represents a typed array of 32-bit signed integers  
| Provides access to internationalization and localization functionality  
| Determines whether a value is a finite number  
| Determines whether a value is `NaN` or not  
| Provides functionality to convert JavaScript values to and from the JSON format  
| Represents a collection of values, where each value may occur only once  
| Provides access to mathematical functions and constants  
| Represents a numeric value  
| Represents the object that is the base of all JavaScript objects  
| Parses a string argument and returns a floating point number  
| Parses a string argument and returns an integer of the specified radix  
| Represents the eventual completion (or failure) of an asynchronous operation, and its resulting value  
| Represents an object that is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc)  
| Queues a microtask to be executed  
| Represents an error when a value is not in the set or range of allowed values  
| Represents an error when a non-existent variable is referenced  
| Provides methods for interceptable JavaScript operations  
| Represents a regular expression, allowing you to match combinations of characters  
| Represents a collection of values, where each value may occur only once  
| Repeatedly calls a function, with a fixed time delay between each call  
| Calls a function or evaluates an expression after a specified number of milliseconds  
| Represents a generic, fixed-length raw binary data buffer  
| Represents a sequence of characters  
| Creates a deep copy of a value  
| Represents a unique and immutable data type that is used as the key of an object property  
| Represents an error when trying to interpret syntactically invalid code  
| Represents an error when a value is not of the expected type  
| Represents a typed array of 8-bit unsigned integers  
| Represents a typed array of 8-bit unsigned integers clamped to 0-255  
| Represents a typed array of 32-bit unsigned integers  
| Represents an error when a global URI handling function was used in a wrong way  
| Represents an object providing static methods used for creating object URLs  
| Represents a URL pattern  
| Represents a collection of key/value pairs  
| Represents a collection of key/value pairs in which the keys are weakly referenced  
| Represents a collection of objects in which each object may occur only once  
| Provides access to WebAssembly  
### Next.js Specific Polyfills
### Environment Variables
You can use `process.env` to access Environment Variables for both `next dev` and `next build`.
### Unsupported APIs
The Edge Runtime has some restrictions including:
  * Native Node.js APIs **are not supported**. For example, you can't read or write to the filesystem.
  * `node_modules` _can_ be used, as long as they implement ES Modules and do not use native Node.js APIs.
  * Calling `require` directly is **not allowed**. Use ES Modules instead.


The following JavaScript language features are disabled, and **will not work:**
API| Description  
---|---  
| Evaluates JavaScript code represented as a string  
| Creates a new function with the code provided as an argument  
| Compiles a WebAssembly module from a buffer source  
| Compiles and instantiates a WebAssembly module from a buffer source  
In rare cases, your code could contain (or import) some dynamic code evaluation statements which _can not be reached at runtime_ and which can not be removed by treeshaking. You can relax the check to allow specific files with your Middleware configuration:
middleware.ts
```
exportconstconfig= {
 unstable_allowDynamic: [
// allows a single file
'/lib/utilities.js',
// use a glob to allow anything in the function-bind 3rd party module
'**/node_modules/function-bind/**',
 ],
}
```

`unstable_allowDynamic` is a , or an array of globs, ignoring dynamic code evaluation for specific files. The globs are relative to your application root folder.
Be warned that if these statements are executed on the Edge, _they will throw and cause a runtime error_.
