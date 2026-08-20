# Shopware Frontends – Routing

Source: `apps/docs/src/getting-started/routing.md`

---

## Contents

- [Concept: SeoUrl-based routing](#concept-seourl-based-routing)
- [Step 1: resolve URL path to route](#step-1-resolve-url-path-to-route)
- [Step 2: resolve route to page data](#step-2-resolve-route-to-page-data)
- [Saving SEO API calls (History State Optimization)](#saving-seo-api-calls-history-state-optimization)
- [Further reading](#further-reading)

## Concept: SeoUrl-based routing

Shopware uses `SeoUrl` objects to map URL paths to page types and entities.
A SeoUrl contains `routeName` and `foreignKey`.

**Three native route types:**
- `frontend.detail.page` → product detail page
- `frontend.navigation.page` → category page
- `frontend.landing.page` → landing page

---

## Step 1: resolve URL path to route

```ts
import {
  useNavigationContext,
  useNavigationSearch,
} from "@shopware/composables";

const { resolvePath } = useNavigationSearch();
const seoResult = await resolvePath("/Winter-Season/My-Product");

const { routeName, foreignKey } = useNavigationContext(ref(seoResult));
// routeName.value: "frontend.detail.page"
// foreignKey.value: "f2f6b6b3a0a04e2a8b0f8a2b2b5b5b1a"
```

---

## Step 2: resolve route to page data

Catch-all component `[...all].vue` – the standard pattern in all templates:

```ts
import type { Schemas } from "#shopware";
import {
  useNavigation,
  useNavigationContext,
  useNavigationSearch,
  useCategorySearch,
} from "@shopware/composables";

const seoResult: Schemas["SeoUrl"] | null = await resolvePath(route.path);
const { routeName, foreignKey } = useNavigationContext(ref(seoResult));

const data = ref(null);

switch (routeName.value) {
  case "frontend.navigation.page":
    let { search: categorySearch } = useCategorySearch();
    const categoryResponse = await categorySearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    const { category } = useCategory(categoryResponse);
    data.value = category;
    break;

  case "frontend.detail.page":
    let { search: productSearch } = useProductSearch();
    const productResponse = await productSearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    const { product } = useProduct(productResponse);
    data.value = product;
    break;

  case "frontend.landing.page":
    let { search: landingSearch } = useLandingSearch();
    const landing = await landingSearch(foreignKey.value, {
      withCmsAssociations: true,
    });
    data.value = ref(landing);
    break;
}
```

> Tip: with `@shopware/nuxt-module` all composables are imported automatically.

---

## Saving SEO API calls (History State Optimization)

**Problem:** by default, 2 API calls are required for every navigation:
1. SeoURL lookup → page type + entity ID
2. Load entity data

**Solution:** after the first SSR rendering, SeoURL data is already contained in the links (History State API). The browser-side page transition then no longer needs a SeoURL lookup.

### getCategoryRoute and getProductRoute

Helper functions that embed SeoURL metadata directly into the link:

```vue
<!-- Category link with NuxtLink -->
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
<!-- Product link with RouterLink -->
<script setup lang="ts">
import { getProductRoute } from "@shopware/helpers";
</script>
<template>
  <RouterLink :to="getProductRoute(product)">
    {{ getTranslatedProperty(product, "name") }}
  </RouterLink>
</template>
```

**How it works (simplified):**
1. Server rendering: the SeoURL is resolved via the Store API, CMS data including the SeoURL is loaded
2. Links automatically receive SEO path metadata
3. On client navigation: metadata from the History State → no SeoURL API call needed
4. Direct access to a URL: a SeoURL API call on the server is required (cached via `useAsyncData`)

### When is SeoURL resolution still necessary?

Only on the **first page request** (server-side rendering), because no History State exists yet.

---

## Further reading

- Creating a product listing: call the Skill tool with `sw-practice`, then see `FRONTENDS-EXAMPLES-EXAMPLES.md`
- [CMS content pages](../../sw-frontends-cms/references/deep/)
