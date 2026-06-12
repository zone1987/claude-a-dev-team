# Shopware Frontends – Framework & Architektur

Quelle: `apps/docs/src/framework/`

---

## Package-Hierarchie (von abstrakt zu konkret)

```
api-client          (TypeScript only)
helpers             (TypeScript only)
composables         (TypeScript + Vue 3)
nuxt-module         (TypeScript + Vue 3 + Nuxt 3)
cms-base-layer      (TypeScript + Vue 3 + Nuxt 3 + UnoCSS)
unocss-design-tokens-layer  (Nuxt Layer für Styling/Tokens)
```

---

## 1. api-client (`@shopware/api-client`)

Einheitliches Interface für die Shopware Store-API.
Kann standalone in jedem JavaScript-Projekt verwendet werden.

- Typesafe via generierte Typen (`@shopware/api-gen`)
- `createAPIClient<operations>({ baseURL, accessToken })`
- `apiClient.invoke("endpoint verb /path", { body, pathParams, query })`
- `apiClient.onConfigChange(callback)` für Context-Token-Änderungen
- `apiClient.hook("onSuccessResponse", callback)` für Response-Hooks

---

## 2. helpers (`@shopware/helpers`)

Stateless-Utility-Funktionen für Formatierung und Datenmanipulation.
Nicht an Vue oder Nuxt gebunden.

Wichtige Funktionen:
- `getTranslatedProperty(entity, "name")` – übersetzten Wert holen
- `getProductUrl(product)` – SEO-URL des Produkts
- `getCategoryRoute(category)` – SEO-URL der Kategorie  
- `getProductRoute(product)` – Route für RouterLink/NuxtLink
- `getSmallestThumbnailUrl(product)` – kleinste Thumbnail-URL
- `getFormattedPrice(price)` – Preis mit Währungssymbol

---

## 3. composables (`@shopware/composables`)

Vue 3 Composition Functions für State Management, UI-Logik und Data Fetching.

### Context Composables

Ermöglichen granulares State-Sharing zwischen Parent-/Child-Komponenten ohne Prop-Drilling via `provide`/`inject`.

**Prinzip:**
- Composable mit `context`-Parameter aufrufen = neue Context-Boundary erstellen
- Composable ohne Parameter = Context vom nächsten Parent holen

**Beispiel:**
```vue
<!-- Category.vue – erstellt Context-Boundary -->
<script setup>
const { search } = useCategorySearch();
const categoryResponse = await search(path);
const { category } = useCategory(categoryResponse);  // mit Param = Provider
</script>

<!-- CategoryHeader.vue – liest aus Context -->
<script setup>
const { category } = useCategory();  // ohne Param = Consumer
</script>
<template>
  <h1>{{ category.name }}</h1>
</template>
```

**Verfügbare Context-Composables:**
- `useCategory(categoryResponse?)` – Kategorie-Kontext
- `useProduct(product?)` – Produkt-Kontext
- `useNavigationContext(seoResult?)` – Navigation/Route-Kontext
  - `{ routeName, foreignKey }` aus `useNavigationContext()`

**Visualisierung (Wireframe):**
```
App
├─ useNavigationContext (blau, global)
│
└─ ProductDetailPage
   └─ useProduct(detailProduct)  (rot, Seiten-Kontext)
      ├─ ProductConfigurator → useProduct() ← kein Prop-Drilling
      └─ Quickview
         └─ useProduct(quickViewProduct)  (grün, eigener Kontext)
            └─ ProductPrice → useProduct()
```

---

### Shared Composables

Einmalige Instanz für die gesamte App (via `createSharedComposable` aus VueUse).

**Wann nötig:** Wenn Daten (z.B. Cart-Inhalt) nicht mehrfach im Speicher dupliziert werden sollen.

**Beispiel `useCart`:**
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

### Composables überschreiben/erweitern

Datei mit gleichem Namen in `composables/` erstellen (Nuxt auto-importiert sie mit Vorrang):

```ts
// composables/useAddToCart.ts
import { useAddToCart as coreUseAddToCart } from "@shopware/composables";

export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  // 1. Methode erweitern (z.B. Analytics)
  const addToCart = async (quantity: number) => {
    const result = await coreFunctionality.addToCart(quantity);
    // Analytics-Call hier
    return result;
  };

  // 2. Neue Eigenschaft hinzufügen
  const { cartItems } = useCart();
  const getQuantityInCart = computed(() =>
    cartItems.value.find(
      (item) => item.referencedId === product.value?.id
    )?.quantity
  );

  return { ...coreFunctionality, addToCart, getQuantityInCart };
}
```

---

## 4. nuxt-module (`@shopware/nuxt-module`)

Nuxt-3-Modul für Shopware Frontends. Stellt Composables und API-Client bereit.
Auto-importiert alle Composables.

**nuxt.config.ts:**
```ts
export default defineNuxtConfig({
  extends: [
    "@shopware/composables/nuxt-layer",  // PFLICHT wenn nuxt-module genutzt
    "@shopware/cms-base-layer",
    "@shopware/unocss-design-tokens-layer",
  ],
  modules: ["@shopware/nuxt-module", "@unocss/nuxt"],
  css: ["@unocss/reset/tailwind-compat.css"],
  unocss: { nuxtLayers: true },
});
```

**Wichtig:** `@shopware/composables/nuxt-layer` MUSS erweitert werden, sonst:
```
[unimport] failed to find "createShopwareContext" imported from "#imports"
```

---

## 5. cms-base-layer (`@shopware/cms-base-layer`)

Nuxt-Layer mit fertigen Vue-Komponenten für alle Standard-Shopware-CMS-Blöcke und -Elemente.

**Installation:**
```bash
npm install -D @shopware/cms-base-layer
```

### CMS-Rendering-Workflow

**API-Struktur:**
```
CmsPage
  └── CmsSection  (type: "default", "sidebar")
        └── CmsBlock    (type: "image-text", "product-slider")
              └── CmsSlot     (type: "image", "text")
```

**Komponenten-Auflösung (PascalCase):**

| API-Node | type | Komponente |
|---|---|---|
| `cms_section` | `default` | `CmsSectionDefault` |
| `cms_block` | `image-text` | `CmsBlockImageText` |
| `cms_slot` | `image` | `CmsElementImage` |

Die Auflösung erfolgt via `resolveCmsComponent` aus `@shopware/composables`.

**Dev-Mode Placeholder:**
Wenn eine Komponente fehlt, zeigt der Dev-Mode:
- Erwarteten Komponentennamen (z.B. `CmsElementMyCustomSlider`)
- Link zur Dokumentation
- "Copy AI Prompt"-Button mit vollständigem API-JSON

**Fehlende Komponente implementieren:**
```vue
<!-- components/CmsElementMyCustomSlider.vue -->
<script setup lang="ts">
import type { Schemas } from "#shopware";
defineProps<{ content: Schemas["CmsSlot"] }>();
</script>
<template>
  <!-- content.data und content.config nutzen -->
</template>
```

In Produktion: fehlende Komponenten rendern unsichtbar (kein Fehler).

---

## 6. Styling mit UnoCSS

Shopware Frontends verwendet **UnoCSS** (Tailwind-kompatibel).

**Schichten:**
- `@shopware/cms-base-layer` – CMS-Komponenten, Bild-Config
- `@shopware/unocss-design-tokens-layer` – UnoCSS-Setup, Design Tokens, Laufzeit-Auflösung
- Projektspezifisches `uno.config.ts` – markenspezifische Erweiterungen

**Utility-CSS Prinzipien:**
```html
<!-- Responsive Design (Mobile First) -->
<div class="grid md:grid-cols-2"></div>

<!-- State Variants -->
<input class="hover:shadow-xl border-indigo rounded-md p-3" />
```

**Wiederverwendbarkeit:** Statt langen Klassen-Listen: Vue-Komponenten erstellen.

**Custom CSS Framework:** Blank Template verwenden, UnoCSS entfernen:
1. `@unocss/nuxt` aus `modules` entfernen
2. `@shopware/unocss-design-tokens-layer` aus `extends` entfernen
3. UnoCSS-Reset-Import aus `css` entfernen
4. `unocss`-Config aus `nuxt.config.ts` entfernen
5. Eigene `uno.config.ts` löschen

---

## 7. Design Tokens (`@shopware/unocss-design-tokens-layer`)

Color Design Tokens als UnoCSS-Theme-Colors. Material-Style Naming.

**Namensmuster:** `<category>-<role>[-<variant>]`

| Kategorie | Zweck | Beispiele |
|---|---|---|
| `brand` | Primär-, Sekundär-, Tertiär-Farben | `brand-primary`, `brand-on-secondary` |
| `surface` | Hintergründe, Container | `surface-surface-container-high` |
| `outline` | Rahmen, Trennlinien | `outline-outline`, `outline-outline-focus` |
| `states` | Semantisches Feedback | `states-error`, `states-on-warning-container` |
| `fixed` | Theme-unabhängige Farben | `fixed-fixed-on-image` |
| `other` | Diverse | `other-sale`, `other-shadow` |
| `overlay` | Halbtransparente Overlays | `overlay-dark-high`, `overlay-light-low` |

**Verwendung:**
```html
<div class="bg-brand-primary text-brand-on-primary">Button</div>
<p class="text-states-error">Fehler</p>
<div class="border border-outline-outline rounded-md">Card</div>
```

**Anpassen (uno.config.ts):**
```ts
theme: {
  colors: {
    "brand-primary": "#123456",   // bestehenden Token überschreiben
    "custom-accent": "#FF00FF",   // neuen Token hinzufügen
  },
}
```

---

## 3D/Spatial Media Support

CMS unterstützt 3D-Modelle (GLB-Format) in Bildelementen, Bildgalerien und dem Spatial Viewer Block. Der 3D-Viewer wird on-demand geladen.
