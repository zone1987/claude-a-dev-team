# Shopware Frontends – Routing

Quelle: `apps/docs/src/getting-started/routing.md`

---

## Konzept: SeoUrl-basiertes Routing

Shopware verwendet `SeoUrl`-Objekte, um URL-Pfade auf Seiten-Typen und Entitäten zu mappen.
Ein SeoUrl enthält `routeName` und `foreignKey`.

**Drei native Route-Typen:**
- `frontend.detail.page` → Produktdetailseite
- `frontend.navigation.page` → Kategorieseite
- `frontend.landing.page` → Landing Page

---

## Schritt 1: URL-Pfad zu Route auflösen

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

## Schritt 2: Route zu Seitendaten auflösen

Catch-all-Komponente `[...all].vue` – Standardmuster in allen Templates:

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

> Tipp: Mit `@shopware/nuxt-module` werden alle Composables automatisch importiert.

---

## SEO-API-Calls einsparen (History State Optimization)

**Problem:** Standardmäßig sind für jede Navigation 2 API-Calls nötig:
1. SeoURL-Lookup → Seiten-Typ + Entitäts-ID
2. Entitätsdaten laden

**Lösung:** Nach dem ersten SSR-Rendering sind SeoURL-Daten bereits in den Links enthalten (History State API). Der Browser-seitige Seitenübergang braucht dann keinen SeoURL-Lookup mehr.

### getCategoryRoute und getProductRoute

Helper-Funktionen, die SeoURL-Metadaten direkt in den Link einbetten:

```vue
<!-- Kategorie-Link mit NuxtLink -->
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
<!-- Produkt-Link mit RouterLink -->
<script setup lang="ts">
import { getProductRoute } from "@shopware/helpers";
</script>
<template>
  <RouterLink :to="getProductRoute(product)">
    {{ getTranslatedProperty(product, "name") }}
  </RouterLink>
</template>
```

**Funktionsweise (vereinfacht):**
1. Server-Rendering: SeoURL wird über Store-API aufgelöst, CMS-Daten inkl. SeoURL werden geladen
2. Links erhalten automatisch SEO-Pfad-Metadaten
3. Bei Client-Navigation: Metadaten aus History State → kein SeoURL-API-Call nötig
4. Direktzugriff auf URL: SeoURL-API-Call auf Server notwendig (cached via `useAsyncData`)

### Wann ist SeoURL-Auflösung trotzdem nötig?

Nur beim **ersten Seitenaufruf** (Server-Side-Rendering), da noch kein History State vorhanden ist.

---

## Weiterlesen

- [Produktlisting erstellen](../../sw-frontends-examples/references/deep/examples.md)
- [CMS-Content-Pages](../../sw-frontends-cms/references/deep/)
