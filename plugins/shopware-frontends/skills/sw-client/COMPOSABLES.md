# Shopware Frontends — @shopware/composables

Opinionated Vue composables that encapsulate business logic + state on top of the `api-client`.

| Composable | Purpose |
|---|---|
| `useSessionContext` | current context (language/currency/customer), context token |
| `useCart` | load/modify the cart (`addProduct`, `removeItem`, `cart`, `count`) |
| `useCheckout` | payment/shipping methods, place an order |
| `useProductSearch` / `useProduct` | load product(s) |
| `useListing` / `useCategoryListing` | listing incl. filter/sorting/pagination |
| `useCustomer` / `useUser` | login/register/account |
| `useNavigation` / `useCms` | menus / CMS pages |

```ts
const { cart, addProduct, count } = useCart();
await addProduct({ id: productId, quantity: 1 });
```

Composables require the provided `apiClient` context (setup in the app plugin/Nuxt layer). CMS rendering of the
loaded pages: `sw-frontends-cms`. Context/token lifecycle: `sw-frontends-session-context`.

→ Complete reference: [COMPOSABLES-REFERENCE.md](COMPOSABLES-REFERENCE.md)
