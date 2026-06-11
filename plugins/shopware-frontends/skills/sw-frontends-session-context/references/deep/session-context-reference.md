# Shopware Frontends — Session & Context-Token — Vollständige Referenz

---

## Konzept: `sw-context-token`

Der `sw-context-token` ist der zentrale Session-Identifier in der Shopware Store API. Er identifiziert:
- Den **Warenkorb** des Nutzers
- Den **eingeloggten Kunden** (oder Gast)
- Die gewählte **Währung, Sprache, Zahlungsart, Versandart**
- Die aktiven **Lieferadressen**

Der Token wird vom Server bei der ersten Anfrage generiert und als Antwortheader `sw-context-token` zurückgesendet. Bei jeder weiteren Anfrage muss er als Request-Header `sw-context-token` mitgeschickt werden.

---

## `useSessionContext` — vollständige API

```ts
import { useSessionContext } from '@shopware/composables'

const ctx = useSessionContext()
// oder: direktes Setzen des initialen Contexts (für SSR)
const ctx = useSessionContext(initialSalesChannelContext)
```

### Alle Members

| Member | Typ | Beschreibung |
|---|---|---|
| `sessionContext` | `ComputedRef<Schemas["SalesChannelContext"] \| undefined>` | Vollständiges Context-Objekt |
| `userFromContext` | `ComputedRef<Schemas["Customer"] \| undefined \| null>` | Eingeloggter Kunde |
| `selectedShippingMethod` | `ComputedRef<Schemas["ShippingMethod"] \| null>` | Aktuelle Versandart |
| `selectedPaymentMethod` | `ComputedRef<Schemas["PaymentMethod"] \| null>` | Aktuelle Zahlungsart |
| `currency` | `ComputedRef<Schemas["Currency"] \| null>` | Aktuelle Währung |
| `activeShippingAddress` | `ComputedRef<Schemas["CustomerAddress"] \| null>` | Aktive Lieferadresse |
| `activeBillingAddress` | `ComputedRef<Schemas["CustomerAddress"] \| null>` | Aktive Rechnungsadresse |
| `taxState` | `ComputedRef<string \| undefined>` | `"gross"` oder `"net"` |
| `countryId` | `ComputedRef<string \| undefined>` | Land-ID des Kunden |
| `salesChannelCountryId` | `ComputedRef<string \| undefined>` | Standard-Land des Sales-Channels |
| `salesChannelLanguageId` | `ComputedRef<string \| undefined>` | Aktuelle Sprach-ID |
| `currentLanguageId` | `ComputedRef<string \| undefined>` | Alias für `salesChannelLanguageId` |
| `languageId` | `ComputedRef<string \| undefined>` | **DEPRECATED** — `salesChannelLanguageId` nutzen |
| `languageIdChain` | `ComputedRef<string>` | **DEPRECATED** — `currentLanguageId` nutzen |
| `refreshSessionContext()` | `Promise<void>` | Context vom Server neu laden |
| `setShippingMethod(method)` | `Promise<void>` | Versandart setzen |
| `setPaymentMethod(method)` | `Promise<void>` | Zahlungsart setzen |
| `setCurrency(currency)` | `Promise<void>` | Währung wechseln |
| `setLanguage(language)` | `Promise<void>` | Sprache wechseln |
| `setCountry(countryId)` | `Promise<void>` | Land wechseln |
| `setActiveShippingAddress(address)` | `Promise<void>` | Lieferadresse wechseln |
| `setActiveBillingAddress(address)` | `Promise<void>` | Rechnungsadresse wechseln |
| `setContext(context)` | `void` | Lokalen State überschreiben (kein API-Call) |

---

## Token-Persistenz: Cookie-basiertes Pattern

### Vanilla Vue (ohne Nuxt)

```ts
// plugins/shopware.ts
import { createAPIClient } from '@shopware/api-client'
import { createShopwareContext } from '@shopware/composables'
import Cookies from 'js-cookie'

const TOKEN_COOKIE_NAME = 'sw-context-token'

export default (app: App) => {
  const contextToken = Cookies.get(TOKEN_COOKIE_NAME)

  const apiClient = createAPIClient({
    baseURL: import.meta.env.VITE_SHOPWARE_ENDPOINT,
    accessToken: import.meta.env.VITE_SHOPWARE_ACCESS_TOKEN,
    contextToken,  // beim Start aus Cookie laden
  })

  // Token persistieren wenn er sich ändert
  apiClient.hook('onContextChanged', (newToken: string) => {
    Cookies.set(TOKEN_COOKIE_NAME, newToken, {
      expires: 365,
      sameSite: 'strict',
      secure: location.protocol === 'https:'
    })
  })

  createShopwareContext(app, { apiClient })
}
```

---

## SSR-sicheres Token-Handling in Nuxt

Das entscheidende Problem beim SSR: der `apiClient` ist ein **Singleton** pro Request — nicht ein globaler Singleton. Sonst teilen sich alle gleichzeitigen Server-Requests denselben Context-Token (Session-Leak).

### Wie `@shopware/nuxt-module` es löst

Das Nuxt-Plugin (`plugin.ts`) erstellt pro Request eine neue `createAPIClient`-Instanz:

```ts
// Intern im @shopware/nuxt-module plugin.ts (vereinfacht)
export default defineNuxtPlugin((nuxtApp) => {
  const runtimeConfig = useRuntimeConfig()
  const shopwareConfig = runtimeConfig.public.shopware as ShopwareNuxtOptions

  // SSR: privaten Endpoint nutzen wenn konfiguriert
  const isSSR = import.meta.server
  const baseURL = isSSR
    ? (runtimeConfig.shopware?.endpoint ?? shopwareConfig.endpoint)
    : shopwareConfig.endpoint

  // Cookie aus aktuellem Request lesen (H3 + useRequestEvent)
  const contextTokenCookie = useCookie<string>('sw-context-token', {
    maxAge: 60 * 60 * 24 * 365,
    sameSite: 'strict',
    secure: true,
  })

  const apiClient = createAPIClient({
    baseURL,
    accessToken: shopwareConfig.accessToken,
    contextToken: contextTokenCookie.value ?? undefined,
  })

  // Token-Änderungen in Cookie schreiben
  apiClient.hook('onContextChanged', (newToken: string) => {
    contextTokenCookie.value = newToken
  })

  // Maintenance Mode behandeln
  apiClient.hook('onResponseError', (response) => {
    if (response.status === 503) {
      // Maintenance-Page anzeigen
    }
  })

  // In Vue-App bereitstellen
  createShopwareContext(nuxtApp.vueApp, {
    apiClient,
    devStorefrontUrl: shopwareConfig.devStorefrontUrl,
    cacheableReads: shopwareConfig.cacheableReads,
  })
})
```

### Nuxt-Konfiguration

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@shopware/nuxt-module'],

  shopware: {
    endpoint: 'https://shop.example.com/store-api',
    accessToken: 'SWSCXXXXXX',

    // Optional: separater SSR-Endpoint (z.B. internes Netzwerk)
    // → wird als runtimeConfig.shopware.endpoint gesetzt (privat)
    // CSR-Endpoint bleibt in runtimeConfig.public.shopware.endpoint

    devStorefrontUrl: 'https://shop.example.com',  // für Admin-Links im Dev-Mode
    apiClientConfig: { timeout: 10000 },
    useUserContextInSSR: false,   // User-Context (Login) nicht im SSR verwenden
    cacheableReads: false,        // GET-Anfragen cachen
  },

  runtimeConfig: {
    // Private (SSR-only) Konfiguration
    shopware: {
      endpoint: process.env.NUXT_SHOPWARE_ENDPOINT,  // interner API-Endpoint
    },
    public: {
      // Client-seitige Konfiguration
      shopware: {
        endpoint: process.env.NUXT_PUBLIC_SHOPWARE_ENDPOINT,
        accessToken: process.env.NUXT_PUBLIC_SHOPWARE_ACCESS_TOKEN,
      }
    }
  }
})
```

---

## Umgebungsvariablen

| Variable | Beschreibung | Sichtbarkeit |
|---|---|---|
| `NUXT_PUBLIC_SHOPWARE_ENDPOINT` | Store-API-URL (CSR) | Public |
| `NUXT_PUBLIC_SHOPWARE_ACCESS_TOKEN` | sw-access-key (CSR) | Public |
| `NUXT_SHOPWARE_ENDPOINT` | Store-API-URL (SSR-only, intern) | Privat |
| `NUXT_PUBLIC_SHOPWARE_SHOPWARE_ENDPOINT` | Legacy (deprecated) | Public |
| `NUXT_SHOPWARE_SHOPWARE_ENDPOINT` | Legacy (deprecated) | Privat |

---

## Währung / Sprache wechseln

```ts
const { setCurrency, setLanguage, currency, salesChannelLanguageId } = useSessionContext()

// Währung wechseln
await setCurrency({ id: 'eur-uuid' })
// → Sendet PATCH /context mit { currencyId }
// → Response enthält neuen sw-context-token
// → sessionContext wird automatisch aktualisiert

// Sprache wechseln
await setLanguage({ id: 'de-DE-uuid' })
// → Sendet PATCH /context mit { languageId }
```

---

## Aktueller Kontext-Wert direkt lesen

```ts
const { sessionContext, currency, taxState, userFromContext } = useSessionContext()

// Währung
console.log(currency.value?.isoCode)   // "EUR"
console.log(currency.value?.symbol)    // "€"

// Steuerhinweis
console.log(taxState.value)            // "gross" oder "net"

// Eingeloggter Nutzer (null wenn ausgeloggt, undefined wenn noch nicht geladen)
console.log(userFromContext.value?.email)
```

---

## Pattern: Context nach Login aktualisieren

Nach Login ändert sich der Context-Token (der neue Token enthält die Kunden-Session). `useUser.login()` gibt intern den neuen Token über `onContextChanged` durch.

```ts
const { login } = useUser()
const { refreshSessionContext } = useSessionContext()

async function handleLogin(email: string, password: string) {
  await login({ username: email, password })
  // Token wurde automatisch aktualisiert via onContextChanged
  // Context neu laden um Kundendaten zu bekommen:
  await refreshSessionContext()
}
```

---

## Pattern: Sprach-Header für mehrsprachige Shops

```ts
// In createAPIClient-Setup:
apiClient.defaultHeaders['sw-language-id'] = cookieLanguageId.value

// Wenn Sprache gewechselt wird:
apiClient.hook('onDefaultHeaderChanged', (headerName, value) => {
  if (headerName === 'sw-language-id') {
    cookieLanguageId.value = value as string
  }
})
```

---

## `SalesChannelContext` — wichtige Felder

```ts
type SalesChannelContext = {
  token: string                           // sw-context-token
  currentCustomerGroup: { displayGross: boolean }
  currency: {
    id: string
    isoCode: string    // "EUR", "USD"
    symbol: string     // "€", "$"
    factor: number
    decimalPrecision: number
  }
  salesChannel: {
    id: string
    countryId: string
    languageId: string
    languageIdChain: string[]
    currencyId: string
    // ...
  }
  customer: Customer | null
  shippingMethod: ShippingMethod
  paymentMethod: PaymentMethod
  shippingLocation: {
    country: Country
    address?: CustomerAddress
  }
  context: {
    languageIdChain: string[]
    currencyId: string
    taxState: "gross" | "net"
    // ...
  }
}
```

---

## Typische Initialisierungssequenz (vollständig)

```
Browser-Request kommt an
  ↓
Nuxt-Plugin (pro Request):
  1. Context-Token aus Cookie lesen
  2. createAPIClient({ contextToken }) erstellen
  3. onContextChanged-Hook: Token in Cookie schreiben
  4. createShopwareContext(app, { apiClient })
  ↓
Erste Seite rendert:
  5. useSessionContext().refreshSessionContext() aufrufen
     → GET /store-api/context
     → Response-Header: sw-context-token (ggf. neu)
     → onContextChanged fired → Cookie aktualisiert
     → sessionContext.value gesetzt
  ↓
Nutzereintaktion:
  6. useCart().addProduct() → POST /store-api/checkout/cart/line-item
     → Antwortheader: sw-context-token (gleich oder neu)
     → Automatisch von defaultHeaders verarbeitet
```
