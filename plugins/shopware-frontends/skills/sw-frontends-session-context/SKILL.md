---
name: sw-frontends-session-context
description: >
  Session-/Kontext-Handling in Shopware-Frontends: useSessionContext, der sw-context-token (Persistenz in Cookie/Storage),
  Sprache/Währung/Versand/Zahlung wechseln, SSR-sicheres Token-Handling in Nuxt. Trigger: "useSessionContext",
  "context token frontends", "sw-context-token persist", "Währung wechseln frontends", "session context shopware",
  "ssr token nuxt shopware". Shopware Frontends.
---

# Shopware Frontends — Session/Context

Der `sw-context-token` repräsentiert die Session (Warenkorb, Login, gewählte Währung/Sprache). `useSessionContext`
lädt/aktualisiert ihn; der `api-client` schickt ihn automatisch mit.

```ts
const { sessionContext, refreshSessionContext, setCurrency, setLanguage } = useSessionContext();
await refreshSessionContext();
await setCurrency(currencyId);
```

**Persistenz**: Token in Cookie/Storage speichern und beim Start in den Client laden (`apiClient.hook('onContextChanged', ...)`),
damit Warenkorb/Login über Reloads erhalten bleiben. **SSR (Nuxt)**: Token pro Request isolieren (kein globaler
Shared State zwischen Nutzern) — Cookie serverseitig lesen/setzen. API-Grundlage: `shopware-api` (`sw-store-api-auth`).

→ Vollständige Referenz: [references/deep/session-context-reference.md](references/deep/session-context-reference.md)
