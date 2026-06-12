# Shopware Frontends – Features

Quelle: `apps/docs/src/getting-started/features/`, `apps/docs/src/getting-started/page-elements/`

---

## 1. Wishlist (Wunschliste)

### Composables-Übersicht

| Composable | Beschreibung |
|------------|-------------|
| `useLocalWishlist` | Lokale (In-Memory) Wunschliste für nicht eingeloggte Nutzer |
| `useSyncWishlist` | Remote-Wunschliste (Server, nur für eingeloggte Nutzer) |
| `useWishlist` | View-Helper für Wishlist-Seite (erkennt Login-Status automatisch) |
| `useProductWishlist` | View-Helper für einzelnes Produkt |

### Wunschliste laden und anzeigen

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

### Produkt zur Wunschliste hinzufügen

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

> `addToWishlist` erkennt automatisch, ob der Nutzer eingeloggt ist.

### Produkt aus Wunschliste entfernen

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

### Lokale und Remote-Wunschliste zusammenführen

Nach dem Login lokale Wunschliste mit der Server-Wunschliste synchronisieren:

```ts
const invokeLogin = async () => {
  await login(formData.value);
  mergeWishlistProducts(); // <-- direkt nach Login aufrufen
};
```

---

## 2. Broadcasting (Tab-Synchronisation)

Synchronisierung von Cart- und Session-Daten zwischen Browser-Tabs über die [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API).

### Aktivieren (vue-demo Template)

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  runtimeConfig: {
    broadcasting: true,  // Standard: false
  },
});
```

> **Hinweis:** Broadcasting und BFCache (Back-Forward-Cache) sind inkompatibel. Bei aktiviertem Broadcasting ist BFCache deaktiviert.

### Implementierung (`useBroadcastChannelSync`)

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

  // CART synchronisieren
  const { refreshCart } = useCart();
  const [cartData, notifyCartDataChanged] =
    useSyncChannel<Schemas["Cart"]>("shopware-cart");
  watch([cartData], () => {
    refreshCart(cartData.value);
  });

  // SESSION synchronisieren
  const { setContext } = useSessionContext();
  const [sessionData, notifySessionDataChanged] =
    useSyncChannel<Schemas["SalesChannelContext"]>("shopware-session-data");
  watch([sessionData], () => {
    if (sessionData.value) setContext(sessionData.value);
  });

  // API-Responses abfangen und in Channels posten
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

## 3. Maintenance Mode (Wartungsmodus)

### Erkennung via API

```ts
import { isMaintenanceMode } from "@shopware/helpers";

apiClient.hook("onResponseError", (response) => {
  const error = isMaintenanceMode(response._data?.errors ?? []);
  // Reaktion implementieren
});
```

### Nuxt 3: 503-Fehler werfen und Seite anzeigen

```ts
// In apiClient Setup / Plugin:
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

### IP-Allowlisting (Server-Middleware)

SSR bei aktivem Wartungsmodus deaktivieren – damit die Backend-IP nicht blockiert wird:

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

### Aufbau

Die Sitemap kombiniert zwei Quellen:

```
http://<domain>/sitemap.xml
```

| Quelle | Datei | Inhalt |
|--------|-------|--------|
| Admin-Sitemap | `/server/routes/sitemap.xml.ts` | Produkt-, Kategorie-, CMS-Seiten (via Shopware) |
| Frontends-Sitemap | `/server/routes/sitemap-local.xml.ts` | Statische Seiten des Frontends |

**Statische Seiten manuell eintragen:**

```ts
// server/sitemap.ts
// Jede statische Seite aus dem Frontends-App muss hier manuell eingetragen werden
```

Weitere Informationen zur Admin-Sitemap: https://docs.shopware.com/en/shopware-6-en/settings/sitemap

---

## 5. Custom Products Extension

> Nur verfügbar mit Shopware Rise Plan.

### Composable `useProductCustomizedProductConfigurator`

Zentraler Baustein für Custom Products Logik:

```ts
const {
  isActive,        // boolean: Produkt hat aktives Custom-Product-Template
  customizedProduct, // Template-Daten
  state,           // Zustand für Formular-Binding
  addToCart,       // Zum Warenkorb hinzufügen (mit Custom-Options)
  handleFileUpload, // Bild hochladen → mediaId zurückbekommen
} = useProductCustomizedProductConfigurator();
```

### In ProductAddToCart integrieren

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

### Template-Einbindung

```html
<!-- In ProductStatic.vue oder ähnlichem -->
<ProductVariantConfigurator @change="handleVariantChange" />
<ProductCustomizedProductConfigurator />  <!-- Hinzufügen -->
<ProductAddToCart :product="product" />
```

**Bekannte Einschränkungen:**
- Fehlende Bilder beim "Image select"-Options-Typ
- Fehlendes Cover-Bild für Custom Product im Warenkorb
- Ausgewählte Optionen werden im Warenkorb-Item nicht angezeigt

---

## 6. Navigation & Breadcrumbs

### Navigation laden und rendern

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

**Statische Seite:**
```ts
useBreadcrumbs([{ name: "Shopware", path: "/shopware" }]);
```

**Dynamische Seite (Kategorie/Produkt):**
```ts
const { buildDynamicBreadcrumbs } = useBreadcrumbs();
buildDynamicBreadcrumbs(props.navigationId);
```

**CMS-Seite ohne zusätzlichen Request:**
```ts
import { getCategoryBreadcrumbs } from "@shopware/helpers";
const breadcrumbs = getCategoryBreadcrumbs(productResponse.value?.product?.seoCategory);
useBreadcrumbs(breadcrumbs);
```

**Breadcrumbs beim Seitenwechsel leeren:**
```ts
const { clearBreadcrumbs } = useBreadcrumbs();
onBeforeRouteLeave(() => {
  clearBreadcrumbs();
});
```

**Breadcrumbs anzeigen:**
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
