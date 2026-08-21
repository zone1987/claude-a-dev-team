# Shopware Frontends – Framework & architecture

Source: `apps/docs/src/framework/`

---

## Contents

- [Package hierarchy (from abstract to concrete)](#package-hierarchy-from-abstract-to-concrete)
- [1. api-client (`@shopware/api-client`)](#1-api-client-shopwareapi-client)
- [2. helpers (`@shopware/helpers`)](#2-helpers-shopwarehelpers)
- [3. composables (`@shopware/composables`)](#3-composables-shopwarecomposables)
- [4. nuxt-module (`@shopware/nuxt-module`)](#4-nuxt-module-shopwarenuxt-module)
- [5. cms-base-layer (`@shopware/cms-base-layer`)](#5-cms-base-layer-shopwarecms-base-layer)
- [6. Styling with UnoCSS](#6-styling-with-unocss)
- [7. Design tokens (`@shopware/unocss-design-tokens-layer`)](#7-design-tokens-shopwareunocss-design-tokens-layer)
- [3D/spatial media support](#3dspatial-media-support)

## Package hierarchy (from abstract to concrete)

```
api-client          (TypeScript only)
helpers             (TypeScript only)
composables         (TypeScript + Vue 3)
nuxt-module         (TypeScript + Vue 3 + Nuxt 3)
cms-base-layer      (TypeScript + Vue 3 + Nuxt 3 + UnoCSS)
unocss-design-tokens-layer  (Nuxt layer for styling/tokens)
```

---

## 1. api-client (`@shopware/api-client`)

A uniform interface for the Shopware Store API.
Can be used standalone in any JavaScript project.

- Typesafe via generated types (`@shopware/api-gen`)
- `createAPIClient<operations>({ baseURL, accessToken })`
- `apiClient.invoke("endpoint verb /path", { body, pathParams, query })`
- `apiClient.onConfigChange(callback)` for context token changes
- `apiClient.hook("onSuccessResponse", callback)` for response hooks

---

## 2. helpers (`@shopware/helpers`)

Stateless utility functions for formatting and data manipulation.
Not bound to Vue or Nuxt.

Important functions:
- `getTranslatedProperty(entity, "name")` – fetch the translated value
- `getProductUrl(product)` – SEO URL of the product
- `getCategoryRoute(category)` – SEO URL of the category  
- `getProductRoute(product)` – route for RouterLink/NuxtLink
- `getSmallestThumbnailUrl(product)` – smallest thumbnail URL
- `getFormattedPrice(price)` – price with currency symbol

---

## 3. composables (`@shopware/composables`)

Vue 3 composition functions for state management, UI logic and data fetching.

### Context composables

They enable granular state sharing between parent and child components without prop drilling, via `provide`/`inject`.

**Principle:**
- Calling a composable with a `context` parameter = create a new context boundary
- Calling a composable without a parameter = get the context from the nearest parent

**Example:**
```vue
<!-- Category.vue – creates the context boundary -->
<script setup>
const { search } = useCategorySearch();
const categoryResponse = await search(path);
const { category } = useCategory(categoryResponse);  // with param = provider
</script>

<!-- CategoryHeader.vue – reads from the context -->
<script setup>
const { category } = useCategory();  // without param = consumer
</script>
<template>
  <h1>{{ category.name }}</h1>
</template>
```

**Available context composables:**
- `useCategory(categoryResponse?)` – category context
- `useProduct(product?)` – product context
- `useNavigationContext(seoResult?)` – navigation/route context
  - `{ routeName, foreignKey }` from `useNavigationContext()`

**Visualisation (wireframe):**
```
App
├─ useNavigationContext (blue, global)
│
└─ ProductDetailPage
   └─ useProduct(detailProduct)  (red, page context)
      ├─ ProductConfigurator → useProduct() ← no prop drilling
      └─ Quickview
         └─ useProduct(quickViewProduct)  (green, own context)
            └─ ProductPrice → useProduct()
```

---

### Shared composables

A single instance for the whole app (via `createSharedComposable` from VueUse).

**When needed:** when data (e.g. cart contents) must not be duplicated multiple times in memory.

**Example `useCart`:**
```ts
import { useCartFunction } from "@shopware/composables";
import { createSharedComposable } from "@vueuse/core";

function myUseCart() {
  const coreCartFunctions = useCartFunction();
  const myCustomFunction = () => { /* your own logic */ };
  return { ...coreCartFunctions, myCustomFunction };
}

export const useCart = createSharedComposable(myUseCart);
```

---

### Overriding/extending composables

Create a file with the same name in `composables/` (Nuxt auto-imports it with precedence):

```ts
// composables/useAddToCart.ts
import { useAddToCart as coreUseAddToCart } from "@shopware/composables";

export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  // 1. Extend a method (e.g. analytics)
  const addToCart = async (quantity: number) => {
    const result = await coreFunctionality.addToCart(quantity);
    // analytics call here
    return result;
  };

  // 2. Add a new property
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

Nuxt 3 module for Shopware Frontends. Provides composables and the API client.
Auto-imports all composables.

**nuxt.config.ts:**
```ts
export default defineNuxtConfig({
  extends: [
    "@shopware/composables/nuxt-layer",  // MANDATORY when nuxt-module is used
    "@shopware/cms-base-layer",
    "@shopware/unocss-design-tokens-layer",
  ],
  modules: ["@shopware/nuxt-module", "@unocss/nuxt"],
  css: ["@unocss/reset/tailwind-compat.css"],
  unocss: { nuxtLayers: true },
});
```

**Important:** `@shopware/composables/nuxt-layer` MUST be extended, otherwise:
```
[unimport] failed to find "createShopwareContext" imported from "#imports"
```

---

## 5. cms-base-layer (`@shopware/cms-base-layer`)

Nuxt layer with ready-made Vue components for all standard Shopware CMS blocks and elements.

**Installation:**
```bash
npm install -D @shopware/cms-base-layer
```

### CMS rendering workflow

**API structure:**
```
CmsPage
  └── CmsSection  (type: "default", "sidebar")
        └── CmsBlock    (type: "image-text", "product-slider")
              └── CmsSlot     (type: "image", "text")
```

**Component resolution (PascalCase):**

| API node | type | Component |
|---|---|---|
| `cms_section` | `default` | `CmsSectionDefault` |
| `cms_block` | `image-text` | `CmsBlockImageText` |
| `cms_slot` | `image` | `CmsElementImage` |

Resolution happens via `resolveCmsComponent` from `@shopware/composables`.

**Dev-mode placeholder:**
When a component is missing, dev mode shows:
- The expected component name (e.g. `CmsElementMyCustomSlider`)
- A link to the documentation
- A "Copy AI Prompt" button with the complete API JSON

**Implementing a missing component:**
```vue
<!-- components/CmsElementMyCustomSlider.vue -->
<script setup lang="ts">
import type { Schemas } from "#shopware";
defineProps<{ content: Schemas["CmsSlot"] }>();
</script>
<template>
  <!-- use content.data and content.config -->
</template>
```

In production: missing components render invisibly (no error).

---

## 6. Styling with UnoCSS

Shopware Frontends uses **UnoCSS** (Tailwind-compatible).

**Layers:**
- `@shopware/cms-base-layer` – CMS components, image config
- `@shopware/unocss-design-tokens-layer` – UnoCSS setup, design tokens, runtime resolution
- Project-specific `uno.config.ts` – brand-specific extensions

**Utility CSS principles:**
```html
<!-- Responsive design (mobile first) -->
<div class="grid md:grid-cols-2"></div>

<!-- State variants -->
<input class="hover:shadow-xl border-indigo rounded-md p-3" />
```

**Reusability:** instead of long class lists: create Vue components.

**Custom CSS framework:** use the blank template, remove UnoCSS:
1. Remove `@unocss/nuxt` from `modules`
2. Remove `@shopware/unocss-design-tokens-layer` from `extends`
3. Remove the UnoCSS reset import from `css`
4. Remove the `unocss` config from `nuxt.config.ts`
5. Delete your own `uno.config.ts`

---

## 7. Design tokens (`@shopware/unocss-design-tokens-layer`)

Color design tokens as UnoCSS theme colors. Material-style naming.

**Naming pattern:** `<category>-<role>[-<variant>]`

| Category | Purpose | Examples |
|---|---|---|
| `brand` | primary, secondary, tertiary colors | `brand-primary`, `brand-on-secondary` |
| `surface` | backgrounds, containers | `surface-surface-container-high` |
| `outline` | borders, separators | `outline-outline`, `outline-outline-focus` |
| `states` | semantic feedback | `states-error`, `states-on-warning-container` |
| `fixed` | theme-independent colors | `fixed-fixed-on-image` |
| `other` | miscellaneous | `other-sale`, `other-shadow` |
| `overlay` | semi-transparent overlays | `overlay-dark-high`, `overlay-light-low` |

**Usage:**
```html
<div class="bg-brand-primary text-brand-on-primary">Button</div>
<p class="text-states-error">Error</p>
<div class="border border-outline-outline rounded-md">Card</div>
```

**Customising (uno.config.ts):**
```ts
theme: {
  colors: {
    "brand-primary": "#123456",   // override an existing token
    "custom-accent": "#FF00FF",   // add a new token
  },
}
```

---

## 3D/spatial media support

The CMS supports 3D models (GLB format) in image elements, image galleries and the Spatial Viewer block. The 3D viewer is loaded on demand.
