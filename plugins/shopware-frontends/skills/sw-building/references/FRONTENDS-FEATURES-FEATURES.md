# Shopware Frontends – Features

Source: `apps/docs/src/getting-started/features/`, `apps/docs/src/getting-started/page-elements/`

---

## Contents

- [1. Wishlist](#1-wishlist)
- [2. Broadcasting (tab synchronization)](#2-broadcasting-tab-synchronization)
- [3. Maintenance Mode](#3-maintenance-mode)
- [4. Sitemap](#4-sitemap)
- [5. Custom Products Extension](#5-custom-products-extension)
- [6. Navigation & breadcrumbs](#6-navigation--breadcrumbs)

## 1. Wishlist

### Composables overview

| Composable | Description |
|------------|-------------|
| `useLocalWishlist` | Local (in-memory) wishlist for users who are not logged in |
| `useSyncWishlist` | Remote wishlist (server, only for logged-in users) |
| `useWishlist` | View helper for the wishlist page (detects the login state automatically) |
| `useProductWishlist` | View helper for a single product |

### Loading and displaying the wishlist

```vue
<script setup lang="ts">
import type { Schemas } from "#shopware";

const { getWishlistProducts, items } = useWishlist();
const { apiClient } = useShopwareContext();
const products = ref([]);

const loadProductsByItemIds = async (itemIds: string[]) => {
  const result = await apiClient.invoke("readProduct post /product", {
    body: { ids: itemIds || items.value },
  });
  products.value = result.data.elements;
};

watch(
  items,
  (items, oldItems) => {
    if (items.length !== oldItems?.length) {
      products.value = products.value.filter(({ id }) => items.includes(id));
    }
    if (!items.length) return;
    loadProductsByItemIds(items);
  },
  { immediate: true }
);

onMounted(async () => {
  await getWishlistProducts();
});
</script>

<template>
  <div v-if="products.length">
    <h1>Wishlist</h1>
    <ProductCard v-for="product in products" :key="product.id" :product="product" />
  </div>
</template>
```

### Adding a product to the wishlist

```vue
<script setup lang="ts">
const product: Schemas["Product"] = { id: "7b5b97bd48454979b14f21c8ef38ce08" };
const { addToWishlist, isInWishlist } = useProductWishlist(product);
</script>
<template>
  <button v-if="!isInWishlist" @click="addToWishlist">
    Add to wishlist
  </button>
</template>
```

> `addToWishlist` automatically detects whether the user is logged in.

### Removing a product from the wishlist

```vue
<script setup lang="ts">
const { removeFromWishlist, isInWishlist } = useProductWishlist(product);
</script>
<template>
  <button v-if="isInWishlist" @click="removeFromWishlist">
    Remove from wishlist
  </button>
</template>
```

### Merging the local and remote wishlist

After login, synchronize the local wishlist with the server wishlist:

```ts
const invokeLogin = async () => {
  await login(formData.value);
  mergeWishlistProducts(); // <-- call right after login
};
```

---

## 2. Broadcasting (tab synchronization)

Synchronization of cart and session data between browser tabs via the [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API).

### Enabling it (vue-demo template)

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  runtimeConfig: {
    broadcasting: true,  // default: false
  },
});
```

> **Note:** broadcasting and BFCache (back-forward cache) are incompatible. With broadcasting enabled, BFCache is disabled.

### Implementation (`useBroadcastChannelSync`)

```ts
import type { Schemas } from "#shopware";

export function useSyncChannel<Entity>(
  name: string,
): [Ref<Entity | undefined>, (data: Entity) => void] {
  const { data, post } = useBroadcastChannel<Entity, Entity>({ name });
  return [data, post];
}

export const useBroadcastChannelSync = createSharedComposable(() => {
  const { apiClient } = useShopwareContext();

  // synchronize the CART
  const { refreshCart } = useCart();
  const [cartData, notifyCartDataChanged] =
    useSyncChannel<Schemas["Cart"]>("shopware-cart");
  watch([cartData], () => {
    refreshCart(cartData.value);
  });

  // synchronize the SESSION
  const { setContext } = useSessionContext();
  const [sessionData, notifySessionDataChanged] =
    useSyncChannel<Schemas["SalesChannelContext"]>("shopware-session-data");
  watch([sessionData], () => {
    if (sessionData.value) setContext(sessionData.value);
  });

  // intercept API responses and post them into the channels
  apiClient.hook("onSuccessResponse", (response) => {
    if (response._data?.apiAlias === "cart") {
      notifyCartDataChanged(response._data);
    } else if (response._data?.apiAlias === "sales_channel_context") {
      notifySessionDataChanged(response._data);
    }
  });
});
```

---

## 3. Maintenance Mode

### Detection via the API

```ts
import { isMaintenanceMode } from "@shopware/helpers";

apiClient.hook("onResponseError", (response) => {
  const error = isMaintenanceMode(response._data?.errors ?? []);
  // implement the reaction
});
```

### Nuxt 3: throw a 503 error and show a page

```ts
// In the apiClient setup / plugin:
import { isMaintenanceMode } from "@shopware/helpers";

apiClient.hook("onResponseError", (response) => {
  const error = isMaintenanceMode(response._data?.errors ?? []);
  if (error) {
    throw createError({
      statusCode: 503,
      statusMessage: "MAINTENANCE_MODE",
    });
  }
});
```

```vue
<!-- error.vue -->
<script setup lang="ts">
const props = defineProps<{
  error: { statusCode: number; statusMessage: string; message: string };
}>();

const isMaintenanceMode = computed(() =>
  props.error.statusMessage === "MAINTENANCE_MODE"
);
</script>
<template>
  <div v-if="isMaintenanceMode">Maintenance Mode Page Content</div>
</template>
```

### IP allowlisting (server middleware)

Disable SSR while maintenance mode is active – so the backend IP is not blocked:

```ts
// server/middleware/maintenance.ts
import { ApiClientError } from "@shopware/api-client";
import { isMaintenanceMode } from "@shopware/helpers";
import apiClient from "../apiBuilder";

export default defineEventHandler(async (event) => {
  try {
    await apiClient.invoke("readContext get /context");
  } catch (error) {
    if (error instanceof ApiClientError) {
      if (isMaintenanceMode(error.details.errors ?? [])) {
        event.context.nuxt = event.context.nuxt ?? {};
        event.context.nuxt.noSSR = true;
      }
    }
  }
});
```

---

## 4. Sitemap

### Structure

The sitemap combines two sources:

```
http://<domain>/sitemap.xml
```

| Source | File | Content |
|--------|-------|--------|
| Admin sitemap | `/server/routes/sitemap.xml.ts` | Product, category and CMS pages (via Shopware) |
| Frontends sitemap | `/server/routes/sitemap-local.xml.ts` | Static pages of the frontend |

**Registering static pages manually:**

```ts
// server/sitemap.ts
// Every static page of the Frontends app must be registered here manually
```

More information about the admin sitemap: https://docs.shopware.com/en/shopware-6-en/settings/sitemap

---

## 5. Custom Products Extension

> Only available with the Shopware Rise Plan.

### Composable `useProductCustomizedProductConfigurator`

The central building block for Custom Products logic:

```ts
const {
  isActive,        // boolean: the product has an active custom product template
  customizedProduct, // template data
  state,           // state for form binding
  addToCart,       // add to the cart (with custom options)
  handleFileUpload, // upload an image → get a mediaId back
} = useProductCustomizedProductConfigurator();
```

### Integrating it into ProductAddToCart

```ts
const {
  addToCart: customizedProductAddToCart,
  isActive: isCustomizedProductActive,
} = useProductCustomizedProductConfigurator();

const addToCartProxy = async () => {
  if (isCustomizedProductActive.value) {
    await customizedProductAddToCart();
  } else {
    await addToCart();
  }
};
```

### Wiring it into the template

```html
<!-- In ProductStatic.vue or similar -->
<ProductVariantConfigurator @change="handleVariantChange" />
<ProductCustomizedProductConfigurator />  <!-- add this -->
<ProductAddToCart :product="product" />
```

**Known limitations:**
- Missing images for the "Image select" option type
- Missing cover image for a custom product in the cart
- Selected options are not shown on the cart item

---

## 6. Navigation & breadcrumbs

### Loading and rendering the navigation

```vue
<script setup lang="ts">
import { getCategoryRoute } from "@shopware/helpers";
const { loadNavigationElements, navigationElements } = useNavigation();
await loadNavigationElements({ depth: 2 });
</script>

<template>
  <ul>
    <li v-for="item in navigationElements" :key="item.id">
      <RouterLink
        :to="getCategoryRoute(item)"
        :target="item.externalLink || item.linkNewTab ? '_blank' : ''"
      >
        {{ item.translated.name }}
      </RouterLink>
    </li>
  </ul>
</template>
```

### Breadcrumbs

**Static page:**
```ts
useBreadcrumbs([{ name: "Shopware", path: "/shopware" }]);
```

**Dynamic page (category/product):**
```ts
const { buildDynamicBreadcrumbs } = useBreadcrumbs();
buildDynamicBreadcrumbs(props.navigationId);
```

**CMS page without an additional request:**
```ts
import { getCategoryBreadcrumbs } from "@shopware/helpers";
const breadcrumbs = getCategoryBreadcrumbs(productResponse.value?.product?.seoCategory);
useBreadcrumbs(breadcrumbs);
```

**Clearing breadcrumbs on page change:**
```ts
const { clearBreadcrumbs } = useBreadcrumbs();
onBeforeRouteLeave(() => {
  clearBreadcrumbs();
});
```

**Displaying breadcrumbs:**
```vue
<script setup lang="ts">
const { breadcrumbs } = useBreadcrumbs();
</script>
<template>
  <nav>
    <ol>
      <li v-for="(crumb, index) in breadcrumbs" :key="crumb.path">
        <NuxtLink v-if="crumb.path" :to="crumb.path">{{ crumb.name }}</NuxtLink>
        <span v-else>{{ crumb.name }}</span>
      </li>
    </ol>
  </nav>
</template>
```
