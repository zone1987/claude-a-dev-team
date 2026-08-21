# @shopware/api-client — Complete API reference

Version: **1.5.0**

## Contents

- [Installation](#installation)
- [`createAPIClient` — Store API client](#createapiclient-store-api-client)
- [`invoke` — calling an operation](#invoke-calling-an-operation)
- [`createAdminAPIClient` — Admin API client](#createadminapiclient-admin-api-client)
- [`defaultHeaders` — proxy object](#defaultheaders-proxy-object)
- [Hooks](#hooks)
- [Error handling](#error-handling)
- [`GlobalFetchOptions` — global retry configuration](#globalfetchoptions-global-retry-configuration)
- [`updateBaseConfig` / `getBaseConfig`](#updatebaseconfig-getbaseconfig)
- [`encodeForQuery` — helper function](#encodeforquery-helper-function)
- [Context token mechanics](#context-token-mechanics)
- [Complete Nuxt plugin example](#complete-nuxt-plugin-example)
- [Customizing the TypeScript types](#customizing-the-typescript-types)
- [Exports of the package](#exports-of-the-package)

## Installation

```bash
npm install @shopware/api-client
```

---

## `createAPIClient` — Store API client

### Complete signature

```ts
import { createAPIClient } from '@shopware/api-client';
import type { operations } from '#shopware'; // generated from @shopware/api-gen

function createAPIClient<
  OPERATIONS extends Record<string, any> = operations,
  PATHS extends string | number | symbol = keyof OPERATIONS
>(params: {
  baseURL?: string;           // Store API URL, e.g. "https://shop.example.com/store-api"
  accessToken?: string;       // sw-access-key header
  contextToken?: string;      // sw-context-token (e.g. from a cookie at SSR start)
  defaultHeaders?: ClientHeaders;
  fetchOptions?: GlobalFetchOptions;
}): ApiClient
```

### Returned object (`ApiClient`)

```ts
{
  invoke<OPERATION>(pathParam: string, params?: InvokeParameters<OPERATION>): Promise<RequestReturnType<OPERATION>>
  defaultHeaders: ClientHeadersProxy
  hook: Hookable['hook']  // for registering hooks
  updateBaseConfig(config: { baseURL?: string; accessToken?: string }): void
  getBaseConfig(): { baseURL: string | undefined; accessToken: string | undefined }
}
```

---

## `invoke` — calling an operation

### Syntax

```ts
const result = await apiClient.invoke('OPERATION_NAME METHOD /path', params)
```

The first argument is a **typed string** of the form:
```
"operationName METHOD /path/with/{param}"
```

Examples:
```ts
// GET without a body
const { data } = await apiClient.invoke('readCart get /checkout/cart', {})

// POST with a body
const { data } = await apiClient.invoke('addLineItem post /checkout/cart/line-item', {
  body: { items: [{ id: productId, quantity: 1, type: 'product', referencedId: productId }] }
})

// GET with a path parameter
const { data } = await apiClient.invoke('readProduct post /product', {
  body: { limit: 10, filter: [{ type: 'equals', field: 'active', value: true }] }
})

// With pathParams
const { data } = await apiClient.invoke('readProductDetail post /product/{productId}', {
  pathParams: { productId: '550e8400-e29b-41d4-a716-446655440000' }
})
```

### `InvokeParameters<OPERATION>`

```ts
type InvokeParameters<CURRENT_OPERATION> = {
  // From the operation:
  body?: ...         // request body (defined by the operation)
  query?: ...        // query parameters
  pathParams?: ...   // path parameters (replace {paramName})
  headers?: ClientHeaders  // per-request headers (override defaultHeaders)

  // In addition:
  fetchOptions?: {
    cache?: RequestCache
    duplex?: string
    keepalive?: boolean
    priority?: string
    redirect?: RequestRedirect
    retry?: number
    retryDelay?: number
    retryStatusCodes?: number[]
    signal?: AbortSignal     // for aborting
    timeout?: number         // in milliseconds
  }
}
```

### Return value `RequestReturnType`

```ts
type RequestReturnType<OPERATION> = {
  data: OPERATION['response']    // typed response data
  status: OPERATION['responseCode']  // HTTP status code
}
```

---

## `createAdminAPIClient` — Admin API client

### Complete signature

```ts
import { createAdminAPIClient } from '@shopware/api-client';
import type { operations } from '#shopware'; // adminApiTypes

function createAdminAPIClient<
  OPERATIONS extends Record<string, any> = adminOperations,
  PATHS extends string | number | symbol = keyof OPERATIONS
>(params: {
  baseURL?: string;
  credentials?: {
    grant_type: 'password' | 'client_credentials'
    client_id: string
    client_secret?: string   // for client_credentials
    username?: string        // for password
    password?: string        // for password
    scopes?: string
  }
  sessionData?: AdminSessionData
  defaultHeaders?: ClientHeaders
  fetchOptions?: GlobalFetchOptions
}): AdminApiClient
```

### `AdminSessionData`

```ts
type AdminSessionData = {
  accessToken: string
  refreshToken?: string
  expirationTime: number   // Unix timestamp (ms)
}
```

### Admin client returned object

```ts
{
  invoke<OPERATION>(pathParam: string, params?: InvokeParameters<OPERATION>): Promise<RequestReturnType<OPERATION>>
  setSessionData(data: AdminSessionData): AdminSessionData
  getSessionData(): AdminSessionData
  defaultHeaders: ClientHeadersProxy
  hook: Hookable['hook']
}
```

### Auto-refresh of the OAuth token

The admin client checks the expiry time of the `accessToken` in every `onRequest` interceptor. If it has expired or is not set, a new token is fetched automatically via `/oauth/token`:

```ts
// client_credentials
const adminClient = createAdminAPIClient({
  baseURL: 'https://shop.example.com/api',
  credentials: {
    grant_type: 'client_credentials',
    client_id: 'SWIABC...',
    client_secret: 'mySecret'
  }
})

// password grant
const adminClient = createAdminAPIClient({
  baseURL: 'https://shop.example.com/api',
  credentials: {
    grant_type: 'password',
    client_id: 'administration',
    username: 'admin',
    password: 'shopware'
  }
})

// Reuse an existing session (e.g. from storage)
const adminClient = createAdminAPIClient({
  baseURL: 'https://shop.example.com/api',
  sessionData: {
    accessToken: 'eyJ...',
    refreshToken: 'def50200...',
    expirationTime: Date.now() + 600_000
  }
})
```

---

## `defaultHeaders` — proxy object

`defaultHeaders` is a reactive proxy. Setting it directly triggers the configured hook.

### Supported header names (`ClientHeaders`)

```ts
type ClientHeaders = Partial<Record<
  | 'sw-context-token'     // session token (cart, login)
  | 'sw-access-key'        // sales channel access key
  | 'sw-language-id'       // override the language
  | 'sw-currency-id'       // override the currency
  | 'sw-inheritance'       // enable inheritance
  | 'sw-version-id'        // version context (draft mode)
  | 'sw-include-seo-urls'  // include SEO URLs in the response
  | 'sw-skip-trigger-flow' // do not trigger flows
  | 'sw-app-integration-id'// app integration
  | 'indexing-behavior'    // indexing behavior
  | 'indexing-skip'        // skip indexing
  | 'content-type'
  | 'accept'
  , string
>>
```

### `ClientHeadersProxy` — bulk update

```ts
// Set individual headers directly:
apiClient.defaultHeaders['sw-language-id'] = 'de-DE-uuid'

// Or in bulk via .apply():
apiClient.defaultHeaders.apply({
  'sw-language-id': 'de-DE-uuid',
  'sw-currency-id': null,   // null/undefined = delete
})
```

---

## Hooks

Hooks are registered with `apiClient.hook(eventName, handler)`.

### Store API hooks (`ApiClientHooks`)

```ts
// The context token has changed (e.g. after login)
apiClient.hook('onContextChanged', (newContextToken: string) => {
  // Store the token in a cookie/localStorage
  document.cookie = `sw-context-token=${newContextToken}`
})

// An HTTP error occurred (after errorInterceptor — called after the throw)
apiClient.hook('onResponseError', (response: FetchResponse) => {
  console.error('API Error:', response.status, response.url)
})

// Successful response
apiClient.hook('onSuccessResponse', (response: FetchResponse) => {
  // e.g. metrics
})

// A default header has changed
apiClient.hook('onDefaultHeaderChanged', (headerName: string, value?: string) => {
  console.log(`Header ${headerName} changed to ${value}`)
})

// Before every request (for e.g. logging)
apiClient.hook('onRequest', (context: FetchContext) => {
  // context.request = URL, context.options = FetchOptions
})
```

### Admin API hooks (`AdminApiClientHooks`)

```ts
adminClient.hook('onAuthChange', (sessionData: AdminSessionData) => {
  // Persist the new token
})
adminClient.hook('onResponseError', (response) => { ... })
adminClient.hook('onSuccessResponse', (response) => { ... })
adminClient.hook('onDefaultHeaderChanged', (headerName, value) => { ... })
```

---

## Error handling

On HTTP error responses the client automatically throws an `ApiClientError` instance:

```ts
import { ApiClientError } from '@shopware/api-client'
import type { ApiError } from '@shopware/api-client'

try {
  const { data } = await apiClient.invoke('login post /account/login', {
    body: { username: 'user@example.com', password: 'wrong' }
  })
} catch (e) {
  if (e instanceof ApiClientError) {
    console.log(e.status)       // HTTP status code, e.g. 401
    console.log(e.statusText)   // e.g. "Unauthorized"
    console.log(e.url)          // requested URL
    console.log(e.ok)           // false
    console.log(e.message)      // string from the first Shopware error

    // Iterate the individual errors:
    for (const err of e.details.errors) {
      console.log(err.title)    // e.g. "Unauthorized"
      console.log(err.detail)   // detailed error message
      console.log(err.code)     // e.g. "CHECKOUT__CUSTOMER_NOT_LOGGED_IN"
      console.log(err.status)   // HTTP status as a string
      console.log(err.source?.pointer)  // JSON pointer to the offending field
      console.log(err.meta?.parameters) // template parameters for the error message
    }
  }
}
```

### The `ApiError` type

```ts
type ApiError = {
  title?: string
  detail?: string
  code?: string
  status?: string
  source?: { pointer?: string }
  meta?: { parameters?: Record<string, string> | [] }
}
```

---

## `GlobalFetchOptions` — global retry configuration

```ts
const apiClient = createAPIClient({
  baseURL: 'https://shop.example.com/store-api',
  accessToken: 'SWSC...',
  fetchOptions: {
    retry: 3,                    // 3 retry attempts
    retryDelay: 500,             // 500 ms pause between attempts
    retryStatusCodes: [503, 429],// retry only on these status codes
    timeout: 10_000,             // 10 second timeout
  }
})
```

---

## `updateBaseConfig` / `getBaseConfig`

```ts
// Read the current configuration
const config = apiClient.getBaseConfig()
// { baseURL: 'https://...', accessToken: 'SWSC...' }

// Change the configuration at runtime
// (triggers an internal rebuild of the fetch client when baseURL changes)
apiClient.updateBaseConfig({
  baseURL: 'https://new-endpoint.example.com/store-api',
  accessToken: 'SWSC_NEW...'
})
```

---

## `encodeForQuery` — helper function

Gzip-compresses an object and encodes it as base64url. Useful for passing complex Criteria objects as a single query parameter (workaround for URL length limits).

```ts
import { encodeForQuery } from '@shopware/api-client/helpers'

const encoded = encodeForQuery({
  filter: [{ type: 'equals', field: 'active', value: true }],
  associations: { categories: {} }
})
// Usage: /store-api/product?_criteria=<encoded>
```

---

## Context token mechanics

The `sw-context-token` identifies the shop session (cart, logged-in user, chosen currency/language).

**Automatic update**: on every response the client checks whether the `sw-context-token` response header contains a new value. If so, `defaultHeaders['sw-context-token']` is updated automatically and `onContextChanged` is fired.

**Initialization from a cookie (SSR)**:
```ts
// Nuxt plugin / server-side
const contextToken = useCookie('sw-context-token').value
const apiClient = createAPIClient({
  baseURL: runtimeConfig.public.shopware.endpoint,
  accessToken: runtimeConfig.public.shopware.accessToken,
  contextToken: contextToken ?? undefined,
})

// Persist the token whenever it changes:
apiClient.hook('onContextChanged', (newToken) => {
  useCookie('sw-context-token').value = newToken
})
```

---

## Complete Nuxt plugin example

```ts
// plugins/shopware.client.ts
import { createAPIClient } from '@shopware/api-client'
import { createShopwareContext } from '@shopware/composables'
import type { operations } from '#shopware'

export default defineNuxtPlugin((nuxtApp) => {
  const runtimeConfig = useRuntimeConfig()
  const contextToken = useCookie<string>('sw-context-token')
  const languageId = useCookie<string>('sw-language-id')

  const apiClient = createAPIClient<operations>({
    baseURL: runtimeConfig.public.shopware.endpoint,
    accessToken: runtimeConfig.public.shopware.accessToken,
    contextToken: contextToken.value,
  })

  // Persist the context token
  apiClient.hook('onContextChanged', (newToken) => {
    contextToken.value = newToken
  })

  // Set the language header
  if (languageId.value) {
    apiClient.defaultHeaders['sw-language-id'] = languageId.value
  }

  // Catch maintenance mode
  apiClient.hook('onResponseError', (response) => {
    if (response.status === 503) {
      navigateTo('/maintenance')
    }
  })

  createShopwareContext(nuxtApp.vueApp, {
    apiClient,
    devStorefrontUrl: runtimeConfig.public.shopware.devStorefrontUrl,
  })
})
```

---

## Customizing the TypeScript types

Own/plugin endpoints can extend the generated types:

```ts
// shopware.d.ts
import type { operationsType } from './api-types/storeApiTypes'
import type { myPluginOperations } from './api-types/myPluginTypes'
import type { components } from './api-types/storeApiTypes'

declare module '#shopware' {
  type operations = operationsType & myPluginOperations
  type Schemas = components['schemas']
}
```

---

## Exports of the package

```ts
export { createAPIClient }    from './createAPIClient'
export { createAdminAPIClient } from './createAdminAPIClient'
export { ApiClientError }     from './ApiError'
export type { ApiError }      from './ApiError'
// Types:
export type { ApiClientHooks, RequestReturnType, RequestParameters, InvokeParameters, GlobalFetchOptions }
export type { AdminApiClientHooks, AdminSessionData }
export type { ClientHeaders, ClientHeadersProxy }
```
