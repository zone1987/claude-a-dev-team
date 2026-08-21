# Shopware Frontends – Customization

Source: `apps/docs/src/getting-started/routing.md`, `src/getting-started/languages.md`,
`src/getting-started/features/`, `src/framework/composables/overwriting-composables.md`,
`src/getting-started/cms/`

---

## Contents

- [Routing](#routing)
- [Multi-language support (i18n)](#multi-language-support-i18n)
- [Overriding/extending composables](#overridingextending-composables)
- [Customizing CMS components](#customizing-cms-components)
- [Sitemap](#sitemap)
- [Nuxt layers (multi-brand / customization pattern)](#nuxt-layers-multi-brand--customization-pattern)
- [Features](#features)

## Routing

### Resolving a URL path to a route

Shopware uses the `SeoUrl` concept. URL path → route configuration.

```ts
import { useNavigationContext, useNavigationSearch } from "@shopware/composables";

const { resolvePath } = useNavigationSearch();
const seoResult = await resolvePath("/Winter-Season/My-Product");
const { routeName, foreignKey } = useNavigationContext(ref(seoResult));
// { routeName: "frontend.detail.page", foreignKey: "f2f6b..." }
```

### Route types

| routeName | Page type |
|---|---|
| `frontend.detail.page` | Product detail page |
| `frontend.navigation.page` | Category/navigation page |
| `frontend.landing.page` | Landing page |

### Catch-all route (`[...all].vue`)

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

### SEO URLs without a duplicate API call

On the first server request the SeoUrl is resolved. After that the SEO data is already known and can be passed on through the History State API → no second API call.

**Helpers for direct links:**
```vue
<!-- NuxtLink with getCategoryRoute -->
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
<!-- RouterLink with getProductRoute -->
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

## Multi-language support (i18n)

### Sources of translations

**Backend:**
- CMS translations
- Products and categories
- Routing paths

**Frontend:**
- Static content of the app

**Important:** backend language codes and frontend language codes must be identical!

### Same-domain configuration

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

### Multi-domain configuration

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

### Routing with a language prefix

```vue
<script setup lang="ts">
const localePath = useLocalePath();
const { formatLink } = useInternationalization(localePath);
</script>
<template>
  <NuxtLink :to="formatLink('/account')">Account</NuxtLink>
</template>
```

### Switching languages (testing locally)

**Problem:** after a language switch the backend redirects to its own domain.

**Solution 1: hosts file**
```
127.0.0.1       yourDomainFromBackend.com
```

**Solution 2: dev resolver**
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

### localeId (differing backend/frontend codes)

```ts
locales: [
  { code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
  {
    code: "testde",           // frontend code
    iso: "de-DE",             // ISO code
    file: "de-DE.ts",
    localeId: "c19b753b5f2c4bea8ad15e00027802d4",  // backend language ID
  },
],
```

Backend language IDs: Shopware Admin → Settings → Languages.

### Testing locally

```
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=http://127.0.0.1:3000
```

### Reverse proxy & caching

- The i18n module reads the `x-forwarded-host` header (important behind proxies)
- Strategy options: `prefix_except_default` or `prefix_and_default`
- Disable browser detection: `detectBrowserLanguage: false`
- The cache must be configured per language

---

## Overriding/extending composables

A file with the same name in the `composables/` directory overrides automatically.

### Extending a method (analytics)

```ts
// composables/useAddToCart.ts
import { useAddToCart as coreUseAddToCart } from "@shopware/composables";

export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  const addToCart = async (quantity: number) => {
    const result = await coreFunctionality.addToCart(quantity);
    // analytics here
    return result;
  };

  return { ...coreFunctionality, addToCart };
}
```

### Adding a new property

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

### Replacing a method entirely

```ts
export function useAddToCart(product: Ref<Product>) {
  const coreFunctionality = coreUseAddToCart(product);

  const addToCart = async (quantity: number) => {
    // your own implementation
  };

  return { ...coreFunctionality, addToCart };
}
```

### Replacing an entire composable

```ts
// composables/useAddToCart.ts
export function useAddToCart(product: Ref<Product>) {
  // completely custom implementation (no core call)
  // return the same interface!
}
```

### Extending shared composables

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

## Customizing CMS components

### Implementing a missing component

Dev mode shows a placeholder with:
- Component name (e.g. `CmsElementMyCustomSlider`)
- Docs link
- A "Copy AI Prompt" button (with the complete API JSON)

```vue
<!-- app/components/CmsElementMyCustomSlider.vue -->
<script setup lang="ts">
import type { Schemas } from "#shopware";
const props = defineProps<{ content: Schemas["CmsSlot"] }>();
// props.content.data – data from the API
// props.content.config – configuration
</script>
<template>
  <!-- your own implementation -->
</template>
```

Nuxt auto-imports the component → the placeholder disappears.

### Overriding an existing component

```
app/components/
  SwProductCard.vue      # overrides the base-layer SwProductCard
  CmsBlockImageText.vue  # overrides the base-layer CmsBlockImageText
```

Nuxt prioritizes project-owned components over layer components.

### CMS component naming convention

| Type | Naming scheme | Example |
|---|---|---|
| Section | `CmsSection{Type}` | `CmsSectionDefault` |
| Block | `CmsBlock{type-in-pascal}` | `CmsBlockImageText` |
| Element/slot | `CmsElement{Type}` | `CmsElementImage` |

---

## Sitemap

The sitemap combines two sources:
```
http://your-domain/sitemap.xml
```

**Admin sitemap** (`/server/routes/sitemap.xml.ts`):
- Product pages
- Category pages
- CMS pages

Configuration: Shopware Admin → Settings → Sitemap

**Frontend sitemap** (`/server/routes/sitemap-local.xml.ts`):
- Static app pages
- Add manually to `/server/sitemap.ts`

---

## Nuxt layers (multi-brand / customization pattern)

Enables brand-specific storefronts without code duplication.

**Base template as a dependency:**
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ["../vue-starter-template"],
  // brand-specific configuration
})
```

**Or as an npm package:**
```ts
extends: ["@your-company/store-base"],
```

**Multiple layers:**
```ts
extends: [
  "@your-company/store-base",
  "@your-company/payment-layer",
],
```

Components in the layer hierarchy: project components have the highest priority.

---

## Features

### Maintenance Mode

Shopware can activate a maintenance mode. The Frontends app must handle it correctly.

### Custom Products

For configurable products (personalization). Not to be confused with variants.
Documentation: https://docs.shopware.com/en/shopware-6-en/extensions/customproducts

### Sitemap

Automatically combined from backend + frontend (see above).

### Broadcasting

Synchronizes cart & session between browser tabs via the BroadcastChannel API.
**Default: disabled** (BFCache incompatibility).
