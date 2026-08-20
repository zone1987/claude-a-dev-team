# Shopware Frontends — Session/Context

The `sw-context-token` represents the session (cart, login, selected currency/language). `useSessionContext`
loads/refreshes it; the `api-client` sends it along automatically.

```ts
const { sessionContext, refreshSessionContext, setCurrency, setLanguage } = useSessionContext();
await refreshSessionContext();
await setCurrency(currencyId);
```

**Persistence**: store the token in a cookie/storage and load it into the client on startup (`apiClient.hook('onContextChanged', ...)`),
so that cart/login survive reloads. **SSR (Nuxt)**: isolate the token per request (no global
shared state between users) — read/set the cookie server-side. API foundation: `shopware-api` (`sw-store-api-auth`).

→ Complete reference: [FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE.md](FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE.md)
