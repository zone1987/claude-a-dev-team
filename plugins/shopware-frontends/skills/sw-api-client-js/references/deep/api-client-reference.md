# @shopware/api-client — Vollständige API-Referenz

Version: **1.5.0**

## Installation

```bash
npm install @shopware/api-client
```

---

## `createAPIClient` — Store-API-Client

### Vollständige Signatur

```ts
import { createAPIClient } from '@shopware/api-client';
import type { operations } from '#shopware'; // aus @shopware/api-gen generiert

function createAPIClient<
  OPERATIONS extends Record<string, any> = operations,
  PATHS extends string | number | symbol = keyof OPERATIONS
>(params: {
  baseURL?: string;           // Store-API-URL, z.B. "https://shop.example.com/store-api"
  accessToken?: string;       // sw-access-key Header
  contextToken?: string;      // sw-context-token (z.B. aus Cookie beim SSR-Start)
  defaultHeaders?: ClientHeaders;
  fetchOptions?: GlobalFetchOptions;
}): ApiClient
```

### Rückgabe-Objekt (`ApiClient`)

```ts
{
  invoke<OPERATION>(pathParam: string, params?: InvokeParameters<OPERATION>): Promise<RequestReturnType<OPERATION>>
  defaultHeaders: ClientHeadersProxy
  hook: Hookable['hook']  // zum Registrieren von Hooks
  updateBaseConfig(config: { baseURL?: string; accessToken?: string }): void
  getBaseConfig(): { baseURL: string | undefined; accessToken: string | undefined }
}
```

---

## `invoke` — Operationsaufruf

### Syntax

```ts
const result = await apiClient.invoke('OPERATION_NAME METHOD /path', params)
```

Das erste Argument ist ein **typisierter String** in der Form:
```
"operationName METHOD /path/with/{param}"
```

Beispiele:
```ts
// GET ohne Body
const { data } = await apiClient.invoke('readCart get /checkout/cart', {})

// POST mit Body
const { data } = await apiClient.invoke('addLineItem post /checkout/cart/line-item', {
  body: { items: [{ id: productId, quantity: 1, type: 'product', referencedId: productId }] }
})

// GET mit Pfad-Parameter
const { data } = await apiClient.invoke('readProduct post /product', {
  body: { limit: 10, filter: [{ type: 'equals', field: 'active', value: true }] }
})

// Mit PathParams
const { data } = await apiClient.invoke('readProductDetail post /product/{productId}', {
  pathParams: { productId: '550e8400-e29b-41d4-a716-446655440000' }
})
```

### `InvokeParameters<OPERATION>`

```ts
type InvokeParameters<CURRENT_OPERATION> = {
  // Aus der Operation:
  body?: ...         // Request-Body (aus Operation definiert)
  query?: ...        // Query-Parameter
  pathParams?: ...   // Pfad-Parameter (ersetzen {paramName})
  headers?: ClientHeaders  // per-Request-Header (überschreiben defaultHeaders)

  // Zusätzlich:
  fetchOptions?: {
    cache?: RequestCache
    duplex?: string
    keepalive?: boolean
    priority?: string
    redirect?: RequestRedirect
    retry?: number
    retryDelay?: number
    retryStatusCodes?: number[]
    signal?: AbortSignal     // für Abbruch
    timeout?: number         // in Millisekunden
  }
}
```

### Rückgabe `RequestReturnType`

```ts
type RequestReturnType<OPERATION> = {
  data: OPERATION['response']    // typisierte Response-Daten
  status: OPERATION['responseCode']  // HTTP-Statuscode
}
```

---

## `createAdminAPIClient` — Admin-API-Client

### Vollständige Signatur

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
    client_secret?: string   // für client_credentials
    username?: string        // für password
    password?: string        // für password
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
  expirationTime: number   // Unix-Timestamp (ms)
}
```

### Admin-Client Rückgabe-Objekt

```ts
{
  invoke<OPERATION>(pathParam: string, params?: InvokeParameters<OPERATION>): Promise<RequestReturnType<OPERATION>>
  setSessionData(data: AdminSessionData): AdminSessionData
  getSessionData(): AdminSessionData
  defaultHeaders: ClientHeadersProxy
  hook: Hookable['hook']
}
```

### Auto-Refresh der OAuth-Token

Der Admin-Client prüft in jedem `onRequest`-Interceptor die Ablaufzeit des `accessToken`. Ist er abgelaufen oder nicht gesetzt, wird automatisch ein neuer Token via `/oauth/token` geholt:

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

// Vorhandene Session wiederverwenden (z.B. aus Storage)
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

## `defaultHeaders` — Proxy-Objekt

`defaultHeaders` ist ein reaktiver Proxy. Direktes Setzen löst den konfigurierten Hook aus.

### Unterstützte Header-Namen (`ClientHeaders`)

```ts
type ClientHeaders = Partial<Record<
  | 'sw-context-token'     // Session-Token (Warenkorb, Login)
  | 'sw-access-key'        // Sales-Channel-Access-Key
  | 'sw-language-id'       // Sprache überschreiben
  | 'sw-currency-id'       // Währung überschreiben
  | 'sw-inheritance'       // Vererbung aktivieren
  | 'sw-version-id'        // Versions-Kontext (Draft-Modus)
  | 'sw-include-seo-urls'  // SEO-URLs in Response einschließen
  | 'sw-skip-trigger-flow' // Flows nicht triggern
  | 'sw-app-integration-id'// App-Integration
  | 'indexing-behavior'    // Indexierungs-Verhalten
  | 'indexing-skip'        // Indexierung überspringen
  | 'content-type'
  | 'accept'
  , string
>>
```

### `ClientHeadersProxy` — bulk update

```ts
// Einzelne Header direkt setzen:
apiClient.defaultHeaders['sw-language-id'] = 'de-DE-uuid'

// Oder bulk via .apply():
apiClient.defaultHeaders.apply({
  'sw-language-id': 'de-DE-uuid',
  'sw-currency-id': null,   // null/undefined = löschen
})
```

---

## Hooks

Hooks werden mit `apiClient.hook(eventName, handler)` registriert.

### Store-API-Hooks (`ApiClientHooks`)

```ts
// Context-Token hat sich geändert (z.B. nach Login)
apiClient.hook('onContextChanged', (newContextToken: string) => {
  // Token in Cookie/localStorage speichern
  document.cookie = `sw-context-token=${newContextToken}`
})

// HTTP-Fehler aufgetreten (nach errorInterceptor — wird nach dem Throw aufgerufen)
apiClient.hook('onResponseError', (response: FetchResponse) => {
  console.error('API Error:', response.status, response.url)
})

// Erfolgreiche Response
apiClient.hook('onSuccessResponse', (response: FetchResponse) => {
  // z.B. Metrics
})

// Default-Header hat sich geändert
apiClient.hook('onDefaultHeaderChanged', (headerName: string, value?: string) => {
  console.log(`Header ${headerName} changed to ${value}`)
})

// Vor jedem Request (für z.B. Logging)
apiClient.hook('onRequest', (context: FetchContext) => {
  // context.request = URL, context.options = FetchOptions
})
```

### Admin-API-Hooks (`AdminApiClientHooks`)

```ts
adminClient.hook('onAuthChange', (sessionData: AdminSessionData) => {
  // Neuen Token persistieren
})
adminClient.hook('onResponseError', (response) => { ... })
adminClient.hook('onSuccessResponse', (response) => { ... })
adminClient.hook('onDefaultHeaderChanged', (headerName, value) => { ... })
```

---

## Fehlerbehandlung

Der Client wirft bei HTTP-Fehlerantworten automatisch eine `ApiClientError`-Instanz:

```ts
import { ApiClientError } from '@shopware/api-client'
import type { ApiError } from '@shopware/api-client'

try {
  const { data } = await apiClient.invoke('login post /account/login', {
    body: { username: 'user@example.com', password: 'wrong' }
  })
} catch (e) {
  if (e instanceof ApiClientError) {
    console.log(e.status)       // HTTP-Statuscode, z.B. 401
    console.log(e.statusText)   // z.B. "Unauthorized"
    console.log(e.url)          // angefragt URL
    console.log(e.ok)           // false
    console.log(e.message)      // String aus erstem Shopware-Fehler

    // Einzelne Fehler iterieren:
    for (const err of e.details.errors) {
      console.log(err.title)    // z.B. "Unauthorized"
      console.log(err.detail)   // detaillierte Fehlermeldung
      console.log(err.code)     // z.B. "CHECKOUT__CUSTOMER_NOT_LOGGED_IN"
      console.log(err.status)   // HTTP-Status als String
      console.log(err.source?.pointer)  // JSON-Pointer auf fehlerhaftes Feld
      console.log(err.meta?.parameters) // Template-Parameter für die Fehlermeldung
    }
  }
}
```

### `ApiError`-Typ

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

## `GlobalFetchOptions` — globale Retry-Konfiguration

```ts
const apiClient = createAPIClient({
  baseURL: 'https://shop.example.com/store-api',
  accessToken: 'SWSC...',
  fetchOptions: {
    retry: 3,                    // 3 Wiederholungsversuche
    retryDelay: 500,             // 500 ms Pause zwischen Versuchen
    retryStatusCodes: [503, 429],// nur bei diesen Statuscodes wiederholen
    timeout: 10_000,             // 10 Sekunden Timeout
  }
})
```

---

## `updateBaseConfig` / `getBaseConfig`

```ts
// Aktuelle Konfiguration lesen
const config = apiClient.getBaseConfig()
// { baseURL: 'https://...', accessToken: 'SWSC...' }

// Konfiguration zur Laufzeit ändern
// (löst internen Fetch-Client-Neuaufbau aus wenn baseURL geändert)
apiClient.updateBaseConfig({
  baseURL: 'https://new-endpoint.example.com/store-api',
  accessToken: 'SWSC_NEW...'
})
```

---

## `encodeForQuery` — Hilfsfunktion

Gzip-komprimiert ein Objekt und codiert es als Base64url. Nützlich um komplexe Criteria-Objekte als einzelnen Query-Parameter zu übergeben (Workaround für URL-Längenbeschränkungen).

```ts
import { encodeForQuery } from '@shopware/api-client/helpers'

const encoded = encodeForQuery({
  filter: [{ type: 'equals', field: 'active', value: true }],
  associations: { categories: {} }
})
// Verwendung: /store-api/product?_criteria=<encoded>
```

---

## Context-Token-Mechanik

Der `sw-context-token` identifiziert die Shop-Session (Warenkorb, eingeloggter Nutzer, gewählte Währung/Sprache).

**Automatisches Update**: Bei jeder Response prüft der Client, ob der `sw-context-token`-Antwortheader einen neuen Wert enthält. Falls ja, wird `defaultHeaders['sw-context-token']` automatisch aktualisiert und `onContextChanged` gefeuert.

**Initialisierung aus Cookie (SSR)**:
```ts
// Nuxt-Plugin / server-side
const contextToken = useCookie('sw-context-token').value
const apiClient = createAPIClient({
  baseURL: runtimeConfig.public.shopware.endpoint,
  accessToken: runtimeConfig.public.shopware.accessToken,
  contextToken: contextToken ?? undefined,
})

// Token persistieren wenn er sich ändert:
apiClient.hook('onContextChanged', (newToken) => {
  useCookie('sw-context-token').value = newToken
})
```

---

## Vollständiges Nuxt-Plugin-Beispiel

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

  // Context-Token persistieren
  apiClient.hook('onContextChanged', (newToken) => {
    contextToken.value = newToken
  })

  // Sprach-Header setzen
  if (languageId.value) {
    apiClient.defaultHeaders['sw-language-id'] = languageId.value
  }

  // Maintenance-Mode abfangen
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

## TypeScript-Typen anpassen

Eigene/Plugin-Endpunkte können die generierten Typen erweitern:

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

## Exports des Pakets

```ts
export { createAPIClient }    from './createAPIClient'
export { createAdminAPIClient } from './createAdminAPIClient'
export { ApiClientError }     from './ApiError'
export type { ApiError }      from './ApiError'
// Typen:
export type { ApiClientHooks, RequestReturnType, RequestParameters, InvokeParameters, GlobalFetchOptions }
export type { AdminApiClientHooks, AdminSessionData }
export type { ClientHeaders, ClientHeadersProxy }
```
