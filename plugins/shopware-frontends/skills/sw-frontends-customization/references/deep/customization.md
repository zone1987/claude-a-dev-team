# Shopware Frontends – Customization

Quelle: `apps/docs/src/getting-started/routing.md`, `src/getting-started/languages.md`,
`src/getting-started/features/`, `src/framework/composables/overwriting-composables.md`,
`src/getting-started/cms/`

---

## Routing

### URL-Pfad zu Route auflösen

Shopware nutzt `SeoUrl`-Konzept. URL-Pfad → Route-Konfiguration.

```ts
import { useNavigationContext, useNavigationSearch } from "@shopware/composables";

const { resolvePath } = useNavigationSearch();
const seoResult = await resolvePath("/Winter-Season/My-Product");
const { routeName, foreignKey } = useNavigationContext(ref(seoResult));
// { routeName: "frontend.detail.page", foreignKey: "f2f6b..." }
```

### Routen-Typen

| routeName | Seiten-Typ |
|---|---|
| `frontend.detail.page` | Produktdetailseite |
| `frontend.navigation.page` | Kategorie-/Navigationsseite |
| `frontend.landing.page` | Landing Page |

### Catch-All Route (`[...all].vue`)

```ts
import type { Schemas } from "#shopware";

const seoResult: Schemas["SeoUrl"] | null = await resolvePath(route.path);
const { routeName, foreignKey } = useNavigationContext(ref(seoResult));

switch (routeName.value) {
  case "frontend.navigation.page":
    const { search: categorySearch } = useCategorySearch();
    const categoryResponse = await categorySearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    const { category } = useCategory(categoryResponse);
    data.value = category;
    break;

  case "frontend.detail.page":
    const { search: productSearch } = useProductSearch();
    const productResponse = await productSearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    const { product } = useProduct(productResponse);
    data.value = product;
    break;

  case "frontend.landing.page":
    const { search: landingSearch } = useLandingSearch();
    const landing = await landingSearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    data.value = ref(landing);
    break;
}
```

### SEO-URLs ohne doppelten API-Call

Beim ersten Server-Request wird die SeoUrl aufgelöst. Danach sind die SEO-Daten bereits bekannt und können über die History State API weitergegeben werden → kein zweiter API-Call.

**Helpers für direkte Links:**
```vue
<!-- NuxtLink mit getCategoryRoute -->
<script setup lang="ts">
import { getCategoryRoute } from "@shopware/helpers";
</script>
<template>
  <NuxtLink :to="getCategoryRoute(navigationChild)">
    {{ getTranslatedProperty(navigationChild, "name") }}
  </NuxtLink>
</template>
```

```vue
<!-- RouterLink mit getProductRoute -->
<script setup lang="ts">
import { getProductRoute } from "@shopware/helpers";
</script>
<template>
  <RouterLink :to="getProductRoute(product)">
    {{ getTranslatedProperty(product, "name") }}
  </RouterLink>
</template>
```

---

## Mehrsprachigkeit (i18n)

### Quellen für Übersetzungen

**Backend:**
- CMS-Übersetzungen
- Produkte und Kategorien
- Routing-Pfade

**Frontend:**
- Statische Inhalte der App

**Wichtig:** Backend-Sprachcodes und Frontend-Sprachcodes müssen identisch sein!

### Same-Domain Konfiguration

```
www.example.com         // GB site
www.example.com/de-DE   // DE site
```

```ts
// nuxt.config.ts
i18n: {
  vueI18n: { fallbackLocale: "en-GB" },
  strategy: "prefix_except_default",
  defaultLocale: "en-GB",
  langDir: "i18n/src/",
  locales: [
    { code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
    { code: "de-DE", iso: "de-DE", file: "de-DE.ts" },
  ],
},
```

### Multi-Domain Konfiguration

```
www.example1.com     // GB site
www.example2.com     // DE site
```

```ts
locales: [
  { domain: 'example1.com', code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
  { domain: 'example2.com', code: "de-DE", iso: "de-DE", file: "de-DE.ts" },
],
```

### Routing mit Sprachprefix

```vue
<script setup lang="ts">
const localePath = useLocalePath();
const { formatLink } = useInternationalization(localePath);
</script>
<template>
  <NuxtLink :to="formatLink('/account')">Account</NuxtLink>
</template>
```

### Sprachentausch (lokal testen)

**Problem:** Nach Sprachwechsel leitet Backend auf seine Domain um.

**Lösung 1: hosts-Datei**
```
127.0.0.1       yourDomainFromBackend.com
```

**Lösung 2: Dev-Resolver**
```ts
const onChangeHandler = async (option: Event) => {
  const data = await changeLanguage((option.target as HTMLSelectElement).value);

  if (process.dev) {
    locale.value = getLanguageCodeFromId((option.target as HTMLSelectElement).value);
    window.location.replace(`${window.location.origin}/${locale.value}`);
    return;
  }

  if (data.redirectUrl) {
    window.location.replace(replaceToDevStorefront(data.redirectUrl));
  } else {
    window.location.reload();
  }
};
```

### localeId (abweichende Codes Backend/Frontend)

```ts
locales: [
  { code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
  {
    code: "testde",           // Frontend-Code
    iso: "de-DE",             // ISO-Code
    file: "de-DE.ts",
    localeId: "c19b753b5f2c4bea8ad15e00027802d4",  // Backend-Sprach-ID
  },
],
```

Backend-Sprach-IDs: Shopware Admin → Einstellungen → Sprachen.

### Lokales Testen

```
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=http://127.0.0.1:3000
```

### Reverse Proxy & Caching

- i18n-Modul liest `x-forwarded-host`-Header (wichtig hinter Proxies)
- Strategie-Optionen: `prefix_except_default` oder `prefix_and_default`
- Browser-Erkennung deaktivieren: `detectBrowserLanguage: false`
- Cache muss sprach-spezifisch konfiguriert sein

---

## Composables überschreiben/erweitern

Datei mit gleichem Namen in `composables/`-Verzeichnis erstellt überschreibt automatisch.

### Methode erweitern (Analytics)

```ts
// composables/useAddToCart.ts
import { useAddToCart as coreUseAddToCart } from "@shopware/composables";

export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  const addToCart = async (quantity: number) => {
    const result = await coreFunctionality.addToCart(quantity);
    // Analytics hier
    return result;
  };

  return { ...coreFunctionality, addToCart };
}
```

### Neue Eigenschaft hinzufügen

```ts
export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);
  const { cartItems } = useCart();

  const getQuantityInCart = computed(() =>
    cartItems.value.find(
      (item) => item.referencedId === product.value?.id
    )?.quantity
  );

  return { ...coreFunctionality, getQuantityInCart };
}
```

### Methode komplett ersetzen

```ts
export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  const addToCart = async (quantity: number) => {
    // Eigene Implementierung
  };

  return { ...coreFunctionality, addToCart };
}
```

### Ganzes Composable ersetzen

```ts
// composables/useAddToCart.ts
export function useAddToCart(product: Ref<Product>) {
  // Komplett eigene Implementierung (kein Core-Aufruf)
  // Selbes Interface zurückgeben!
}
```

### Shared Composables erweitern

```ts
import { useCartFunction } from "@shopware/composables";
import { createSharedComposable } from "@vueuse/core";

function myUseCart() {
  const coreCartFunctions = useCartFunction();
  const myCustomFunction = () => { /* eigene Logik */ };
  return { ...coreCartFunctions, myCustomFunction };
}

export const useCart = createSharedComposable(myUseCart);
```

---

## CMS-Komponenten anpassen

### Fehlende Komponente implementieren

Dev-Mode zeigt Placeholder mit:
- Komponentenname (z.B. `CmsElementMyCustomSlider`)
- Docs-Link
- "Copy AI Prompt" Button (mit vollständigem API-JSON)

```vue
<!-- app/components/CmsElementMyCustomSlider.vue -->
<script setup lang="ts">
import type { Schemas } from "#shopware";
const props = defineProps<{ content: Schemas["CmsSlot"] }>();
// props.content.data – Daten aus der API
// props.content.config – Konfiguration
</script>
<template>
  <!-- eigene Implementierung -->
</template>
```

Nuxt auto-importiert die Komponente → Placeholder verschwindet.

### Bestehende Komponente überschreiben

```
app/components/
  SwProductCard.vue      # überschreibt Base-Layer SwProductCard
  CmsBlockImageText.vue  # überschreibt Base-Layer CmsBlockImageText
```

Nuxt priorisiert projekt-eigene Komponenten vor Layer-Komponenten.

### CMS-Komponenten-Namen Konvention

| Typ | Namensschema | Beispiel |
|---|---|---|
| Section | `CmsSection{Type}` | `CmsSectionDefault` |
| Block | `CmsBlock{type-in-pascal}` | `CmsBlockImageText` |
| Element/Slot | `CmsElement{Type}` | `CmsElementImage` |

---

## Sitemap

Sitemap kombiniert zwei Quellen:
```
http://your-domain/sitemap.xml
```

**Admin-Sitemap** (`/server/routes/sitemap.xml.ts`):
- Produktseiten
- Kategorieseiten
- CMS-Seiten

Konfiguration: Shopware Admin → Einstellungen → Sitemap

**Frontend-Sitemap** (`/server/routes/sitemap-local.xml.ts`):
- Statische App-Seiten
- Manuell zu `/server/sitemap.ts` hinzufügen

---

## Nuxt Layers (Multi-Brand / Customization-Pattern)

Ermöglicht markenspezifische Storefronts ohne Code-Duplizierung.

**Basis-Template als Dependency:**
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ["../vue-starter-template"],
  // Marken-spezifische Konfiguration
})
```

**Oder als npm-Paket:**
```ts
extends: ["@your-company/store-base"],
```

**Mehrere Layers:**
```ts
extends: [
  "@your-company/store-base",
  "@your-company/payment-layer",
],
```

Komponenten in der Layer-Hierarchie: Projekt-Komponenten haben höchste Priorität.

---

## Features

### Maintenance Mode

Shopware kann einen Wartungsmodus aktivieren. Die Frontends-App muss diesen korrekt behandeln.

### Custom Products

Für konfigurierbare Produkte (Personalisierung). Nicht zu verwechseln mit Varianten.
Dokumentation: https://docs.shopware.com/en/shopware-6-en/extensions/customproducts

### Sitemap

Automatisch aus Backend + Frontend kombiniert (siehe oben).

### Broadcasting

Synchronisiert Cart & Session zwischen Browser-Tabs via BroadcastChannel API.
**Standard: deaktiviert** (BFCache-Inkompatibilität).
