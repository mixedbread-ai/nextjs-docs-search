---
title: "How to create forms with Server Actions"
path: "App / Guides / Forms"
source_url: https://nextjs.org/docs/app/guides/forms
content_length: 7488
---

# How to create forms with Server Actions
React Server Actions are that execute on the server. They can be called in Server and Client Components to handle form submissions. This guide will walk you through how to create forms in Next.js with Server Actions.
## How it works
React extends the HTML element to allow Server Actions to be invoked with the attribute.
When used in a form, the function automatically receives the object. You can then extract the data using the native :
app/invoices/page.tsx
```
exportdefaultfunctionPage() {
asyncfunctioncreateInvoice(formData:FormData) {
'use server'
constrawFormData= {
   customerId:formData.get('customerId'),
   amount:formData.get('amount'),
   status:formData.get('status'),
  }
// mutate data
// revalidate the cache
 }
return <formaction={createInvoice}>...</form>
}
```

> **Good to know:** When working with forms that have multiple fields, you can use the method with JavaScript's . For example: `const rawFormData = Object.fromEntries(formData)`.
## Passing additional arguments
Outside of form fields, you can pass additional arguments to a Server Function using the JavaScript method. For example, to pass the `userId` argument to the `updateUser` Server Function:
app/client-component.tsx
```
'use client'
import { updateUser } from'./actions'
exportfunctionUserProfile({ userId }: { userId:string }) {
constupdateUserWithId=updateUser.bind(null, userId)
return (
  <formaction={updateUserWithId}>
   <inputtype="text"name="name" />
   <buttontype="submit">Update User Name</button>
  </form>
 )
}
```

The Server Function will receive the `userId` as an additional argument:
app/actions.ts
```
'use server'
exportasyncfunctionupdateUser(userId:string, formData:FormData) {}
```

> **Good to know** :
>   * An alternative is to pass arguments as hidden input fields in the form (e.g. `<input type="hidden" name="userId" value={userId} />`). However, the value will be part of the rendered HTML and will not be encoded.
>   * `bind` works in both Server and Client Components and supports progressive enhancement.
> 

## Form validation
Forms can be validate on the client or server.
  * For **client-side validation** , you can use the HTML attributes like `required` and `type="email"` for basic validation.
  * For **server-side validation** , you can use a library like to validate the form fields. For example:


app/actions.ts
```
'use server'
import { z } from'zod'
constschema=z.object({
 email:z.string({
  invalid_type_error:'Invalid Email',
 }),
})
exportdefaultasyncfunctioncreateUser(formData:FormData) {
constvalidatedFields=schema.safeParse({
  email:formData.get('email'),
 })
// Return early if the form data is invalid
if (!validatedFields.success) {
return {
   errors:validatedFields.error.flatten().fieldErrors,
  }
 }
// Mutate data
}
```

## Validation errors
To display validation errors or messages, turn the component that defines the `<form>` into a Client Component and use React .
When using `useActionState`, the Server function signature will change to receive a new `prevState` or `initialState` parameter as its first argument.
app/actions.ts
```
'use server'
import { z } from'zod'
exportasyncfunctioncreateUser(initialState:any, formData:FormData) {
constvalidatedFields=schema.safeParse({
  email:formData.get('email'),
 })
// ...
}
```

You can then conditionally render the error message based on the `state` object.
app/ui/signup.tsx
```
'use client'
import { useActionState } from'react'
import { createUser } from'@/app/actions'
constinitialState= {
 message:'',
}
exportfunctionSignup() {
const [state,formAction,pending] =useActionState(createUser, initialState)
return (
  <formaction={formAction}>
   <labelhtmlFor="email">Email</label>
   <inputtype="text"id="email"name="email"required />
   {/* ... */}
   <paria-live="polite">{state?.message}</p>
   <buttondisabled={pending}>Sign up</button>
  </form>
 )
}
```

## Pending states
The hook exposes a `pending` boolean that can be used to show a loading indicator or disable the submit button while the action is being executed.
app/ui/signup.tsx
```
'use client'
import { useActionState } from'react'
import { createUser } from'@/app/actions'
exportfunctionSignup() {
const [state,formAction,pending] =useActionState(createUser, initialState)
return (
  <formaction={formAction}>
   {/* Other form elements */}
   <buttondisabled={pending}>Sign up</button>
  </form>
 )
}
```

Alternatively, you can use the hook to show a loading indicator while the action is being executed. When using this hook, you'll need to create a separate component to render the loading indicator. For example, to disable the button when the action is pending:
app/ui/button.tsx
```
'use client'
import { useFormStatus } from'react-dom'
exportfunctionSubmitButton() {
const { pending } =useFormStatus()
return (
  <buttondisabled={pending} type="submit">
   Sign Up
  </button>
 )
}
```

You can then nest the `SubmitButton` component inside the form:
app/ui/signup.tsx
```
import { SubmitButton } from'./button'
import { createUser } from'@/app/actions'
exportfunctionSignup() {
return (
  <formaction={createUser}>
   {/* Other form elements */}
   <SubmitButton />
  </form>
 )
}
```

> **Good to know:** In React 19, `useFormStatus` includes additional keys on the returned object, like data, method, and action. If you are not using React 19, only the `pending` key is available.
## Optimistic updates
You can use the React hook to optimistically update the UI before the Server Function finishes executing, rather than waiting for the response:
app/page.tsx
```
'use client'
import { useOptimistic } from'react'
import { send } from'./actions'
typeMessage= {
 message:string
}
exportfunctionThread({ messages }: { messages:Message[] }) {
const [optimisticMessages,addOptimisticMessage] = useOptimistic<
  Message[],
  string
>(messages, (state, newMessage) => [...state, { message: newMessage }])
constformAction=async (formData:FormData) => {
constmessage=formData.get('message') asstring
addOptimisticMessage(message)
awaitsend(message)
 }
return (
  <div>
   {optimisticMessages.map((m, i) => (
    <divkey={i}>{m.message}</div>
   ))}
   <formaction={formAction}>
    <inputtype="text"name="message" />
    <buttontype="submit">Send</button>
   </form>
  </div>
 )
}
```

## Nested form elements
You can call Server Actions in elements nested inside `<form>` such as `<button>`, `<input type="submit">`, and `<input type="image">`. These elements accept the `formAction` prop or event handlers.
This is useful in cases where you want to call multiple Server Actions within a form. For example, you can create a specific `<button>` element for saving a post draft in addition to publishing it. See the for more information.
## Programmatic form submission
You can trigger a form submission programmatically using the method. For example, when the user submits a form using the `⌘` + `Enter` keyboard shortcut, you can listen for the `onKeyDown` event:
app/entry.tsx
```
'use client'
exportfunctionEntry() {
consthandleKeyDown= (e:React.KeyboardEvent<HTMLTextAreaElement>) => {
if (
   (e.ctrlKey ||e.metaKey) &&
   (e.key ==='Enter'||e.key ==='NumpadEnter')
  ) {
e.preventDefault()
e.currentTarget.form?.requestSubmit()
  }
 }
return (
  <div>
   <textareaname="entry"rows={20} requiredonKeyDown={handleKeyDown} />
  </div>
 )
}
```

This will trigger the submission of the nearest `<form>` ancestor, which will invoke the Server Function.
