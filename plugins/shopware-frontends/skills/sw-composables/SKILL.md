---
name: sw-composables
description: >
  Die @shopware/composables (Vue 3) für headless Shopware-Frontends: useCart, useCheckout, useProductSearch,
  useListing, useCustomer, useUser, useSessionContext, useNavigation, useCms; Bereitstellung via app context.
  Trigger: "@shopware/composables", "useCart", "useCheckout", "useProductSearch", "useCustomer composable",
  "useListing shopware", "frontends composable". Shopware Frontends.
---

# Shopware Frontends — @shopware/composables

Opinionierte Vue-Composables, die Geschäftslogik + State über dem `api-client` kapseln.

| Composable | Zweck |
|---|---|
| `useSessionContext` | aktueller Kontext (Sprache/Währung/Kunde), Context-Token |
| `useCart` | Warenkorb laden/ändern (`addProduct`, `removeItem`, `cart`, `count`) |
| `useCheckout` | Zahl-/Versandarten, Bestellung anlegen |
| `useProductSearch` / `useProduct` | Produkt(e) laden |
| `useListing` / `useCategoryListing` | Listing inkl. Filter/Sorting/Pagination |
| `useCustomer` / `useUser` | Login/Register/Konto |
| `useNavigation` / `useCms` | Menüs / CMS-Seiten |

```ts
const { cart, addProduct, count } = useCart();
await addProduct({ id: productId, quantity: 1 });
```

Composables benötigen den bereitgestellten `apiClient`-Kontext (Setup im App-Plugin/Nuxt-Layer). CMS-Rendering der
geladenen Seiten: `sw-frontends-cms`. Kontext-/Token-Lebenszyklus: `sw-frontends-session-context`.

→ Vollständige Referenz: [references/deep/composables-reference.md](references/deep/composables-reference.md)
