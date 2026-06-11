# @shopware/nuxt-module — Vollständige Referenz

Version: **1.4.4**

Nuxt-Modul das `@shopware/api-client` + `@shopware/composables` in Nuxt 4 integriert.

---

## Installation

```bash
npm install @shopware/nuxt-module
```

---

## Registrierung

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@shopware/nuxt-module'],

  shopware: {
    endpoint: 'https://shop.example.com/store-api',
    accessToken: 'SWSCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  }
})
```

---

## Alle Konfigurationsoptionen (`ShopwareNuxtOptions`)

```ts
interface ShopwareNuxtOptions {
  // Store-API-URL (wird als CSR-Endpoint verwendet)
  endpoint?: string

  // Deprecated: shopwareEndpoint (ältere Configs)
  shopwareEndpoint?: string

  // sw-access-key (Sales-Channel Public Access Key)
  accessToken?: string

  // Deprecated: shopwareAccessToken
  shopwareAccessToken?: string

  // URL des Twig-Storefronts (für Admin-Links im Dev-Mode, z.B. Produkt-Editier-Links)
  devStorefrontUrl?: string

  // ofetch-Konfiguration für den API-Client
  apiClientConfig?: {
    timeout?: number | string  // Millisekunden
  }

  // User-Context (Login-State) auch bei SSR-Anfragen verwenden
  // false = nur anonymer Context beim SSR (verhindert Cache-Poisoning)
  useUserContextInSSR?: boolean  // default: false

  // GET-Anfragen cachen (experimentell)
  cacheableReads?: boolean  // default: false
}
```

---

## Umgebungsvariablen

Das Modul liest folgende Umgebungsvariablen (überschreiben `nuxt.config.ts`):

| Variable | Nuxt-Config-Äquivalent | Sichtbarkeit |
|---|---|---|
| `NUXT_PUBLIC_SHOPWARE_ENDPOINT` | `runtimeConfig.public.shopware.endpoint` | CSR + SSR |
| `NUXT_PUBLIC_SHOPWARE_ACCESS_TOKEN` | `runtimeConfig.public.shopware.accessToken` | CSR + SSR |
| `NUXT_SHOPWARE_ENDPOINT` | `runtimeConfig.shopware.endpoint` | SSR-only (privat) |
| `NUXT_PUBLIC_SHOPWARE_SHOPWARE_ENDPOINT` | (legacy deprecated) | CSR + SSR |
| `NUXT_SHOPWARE_SHOPWARE_ENDPOINT` | (legacy deprecated) | SSR-only |

**CSR vs. SSR-Endpoint:** Wenn `NUXT_SHOPWARE_ENDPOINT` gesetzt ist, wird dieser für serverseitige Anfragen verwendet (z.B. internes Netzwerk). `NUXT_PUBLIC_SHOPWARE_ENDPOINT` wird für clientseitige Anfragen verwendet.

---

## Was das Modul registriert

### 1. Nuxt-Plugin (`plugin.ts`)

Das Plugin wird automatisch hinzugefügt. Es:
- Erstellt `createAPIClient<operations>()` mit `baseURL` und `accessToken`
- Liest den `sw-context-token` aus dem `useCookie('sw-context-token')`
- Registriert `onContextChanged`-Hook → schreibt neuen Token in Cookie
- Registriert `onResponseError`-Hook → behandelt Maintenance-Mode (503)
- Ruft `createShopwareContext(nuxtApp.vueApp, { apiClient })` auf

### 2. TypeScript-Template (`shopware.d.ts`)

Wird ins Build-Verzeichnis hinzugefügt wenn **keine** `shopware.d.ts` im Projektroot vorhanden ist. Deklariert den `#shopware`-Modul-Alias für die generierten Typen.

### 3. Nuxt DevTools-Tabs

- **"Shopware Frontends"** → `https://frontends.shopware.com/` (iframe)
- **"CMS Elements"** → `https://frontends.shopware.com/getting-started/cms/` (iframe)

---

## `#shopware`-Typen einrichten

### Automatisch (ohne Anpassung)

Das Modul erzeugt eine `shopware.d.ts` die die Standard-Typen aus `@shopware/api-client` einbindet.

### Mit `@shopware/api-gen` generierten Typen

```ts
// shopware.d.ts (im Projektroot — überschreibt die automatisch generierte)
import type { operationsType } from './api-types/storeApiTypes'
import type { components } from './api-types/storeApiTypes'

declare module '#shopware' {
  type operations = operationsType
  type Schemas = components['schemas']
}
```

### Mit Plugin-Erweiterungen

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

## Auto-importierte Composables

Durch `createShopwareContext()` sind folgende Composables in allen Vue-Komponenten ohne expliziten Import verfügbar (wenn `@shopware/nuxt-module` + `@shopware/composables` installiert sind):

```ts
// Kein Import nötig in .vue-Dateien:
const { cart, addProduct } = useCart()
const { sessionContext } = useSessionContext()
const { user, login } = useUser()
// ... alle @shopware/composables
```

---

## Vollständiges Setup-Beispiel

### 1. Installation

```bash
npm install @shopware/nuxt-module @shopware/composables @shopware/api-client @shopware/helpers
npm install --save-dev @shopware/api-gen
```

### 2. `nuxt.config.ts`

```ts
export default defineNuxtConfig({
  modules: ['@shopware/nuxt-module'],
  extends: ['@shopware/cms-base-layer'],  // optional, für CMS-Rendering

  shopware: {
    endpoint: process.env.SHOPWARE_ENDPOINT ?? 'https://shop.example.com/store-api',
    accessToken: process.env.SHOPWARE_ACCESS_TOKEN ?? 'SWSC...',
    devStorefrontUrl: 'https://shop.example.com',
    apiClientConfig: {
      timeout: 10_000
    }
  },

  runtimeConfig: {
    shopware: {
      // SSR-only (interner Endpoint)
      endpoint: process.env.SHOPWARE_INTERNAL_ENDPOINT,
    },
    public: {
      shopware: {
        // Public (CSR)
        endpoint: process.env.SHOPWARE_ENDPOINT,
        accessToken: process.env.SHOPWARE_ACCESS_TOKEN,
      }
    }
  }
})
```

### 3. Typen generieren

```bash
# .env
OPENAPI_JSON_URL=https://shop.example.com
OPENAPI_ACCESS_KEY=SWSC...

# Schema laden + Typen generieren
npx @shopware/api-gen loadSchema --apiType=store
npx @shopware/api-gen generate --apiType=store
```

### 4. `shopware.d.ts` im Projektroot

```ts
import type { operationsType } from './api-types/storeApiTypes'
import type { components } from './api-types/storeApiTypes'

declare module '#shopware' {
  type operations = operationsType
  type Schemas = components['schemas']
}
```

### 5. Erste Seite

```vue
<!-- pages/index.vue -->
<script setup lang="ts">
const { data: listing } = await useAsyncData('products', () =>
  useNuxtApp().$shopware.invoke('readProduct post /product', {
    body: { limit: 12 }
  })
)
</script>
<template>
  <div>
    <div v-for="product in listing?.data?.elements" :key="product.id">
      {{ product.name }}
    </div>
  </div>
</template>
```

Oder mit Composable:

```vue
<!-- pages/[...path].vue -->
<script setup lang="ts">
const route = useRoute()
const { resolvePath } = useNavigationSearch()
const seoUrl = await resolvePath(route.path)

if (seoUrl?.routeName === 'frontend.navigation.page') {
  const { search } = useCategorySearch()
  const category = await search(seoUrl.foreignKey, { withCmsAssociations: true })
  // category.cmsPage vorhanden wenn CMS-Seite konfiguriert
}
</script>
```

---

## Intern: Modul-Aufbau

```
packages/nuxt-module/
├── src/
│   ├── index.ts      # defineNuxtModule — registriert Plugin + TypeTemplate + DevTools
│   └── utils.ts      # isDependencyInstalledLocally, resolveOwnDependency, isConfigDeprecated
├── plugin.ts         # Nuxt-Plugin (läuft im Nuxt-App-Context)
├── shopware.d.ts     # Default #shopware-Typ-Deklaration
└── index.cjs         # CJS-Wrapper für Nuxt
```

**Abhängigkeiten:**
```json
{
  "@nuxt/kit": "4.4.6",
  "@shopware/composables": "workspace:*",
  "@shopware/helpers": "workspace:*",
  "@shopware/api-client": "workspace:*",
  "defu": "6.1.7",
  "h3": "1.15.11",
  "js-cookie": "3.0.7"
}
```

---

## Kompatibilitätsmatrix

| `@shopware/nuxt-module` | Nuxt | Vue | Node.js |
|---|---|---|---|
| 1.4.x | 4.x | 3.x | ≥18 |

---

## Bekannte Migrations-Hinweise

### Von `shopwareEndpoint`/`shopwareAccessToken` zu `endpoint`/`accessToken`

```ts
// Alt (deprecated):
shopware: {
  shopwareEndpoint: 'https://...',
  shopwareAccessToken: 'SWSC...'
}

// Neu:
shopware: {
  endpoint: 'https://...',
  accessToken: 'SWSC...'
}
```

Das Modul gibt eine Warnung aus wenn die deprecated Keys verwendet werden.
