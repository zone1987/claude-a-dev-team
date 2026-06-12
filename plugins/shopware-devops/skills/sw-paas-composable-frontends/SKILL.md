---
name: sw-paas-composable-frontends
description: >
  Shopware PaaS Composable Frontends: Performance-Optimierung, Fastly-Caching
  für Nuxt.js-Frontend, Store-API Cache via SwagStoreApiCache, CORS-Vermeidung,
  Blackfire Node.js Profiling, ISR-Konfiguration. Trigger: "paas composable
  frontend", "paas nuxt caching", "paas store api cache", "paas fastly frontend",
  "paas cors store-api", "paas nuxt performance", "paas blackfire nuxt",
  "paas ssr cache fastly", "paas isr konfigurieren", "shopware paas headless".
---

# Shopware PaaS — Composable Frontends (Nuxt.js)

## Store-API Caching (Backend)

```bash
composer require shopware-labs/swag-store-api-cache
```

- Cached ausgewählte POST `/store-api/`-Anfragen via Fastly
- Eigene Fastly-Snippets (ersetzen Standard-Snippets)
- Weitere Routen konfigurierbar via `SwagStoreAPICache.config.additionalCacheableRoutes`
- Soft-Purge aktivieren!

## Frontend-Caching (Nuxt.js)

In `nuxt.config.ts` mit ISR (Incremental Static Regeneration):

```ts
routeRules: {
  '/': {
    isr: 60 * 60 * 24,
    headers: {
      'cache-control': 'public, s-maxage=3600, stale-while-revalidate=1800'
    }
  },
  '/**': {
    isr: 60 * 60 * 24,
    headers: {
      'cache-control': 'public, s-maxage=3600, stale-while-revalidate=1800'
    }
  }
}
```

Frontend-Cache-Invalidierung: Nur Fastly-Backend-Service.
Shopware triggert keine Frontend-Cache-Invalidierung.

## CORS vermeiden (OPTIONS-Requests)

Fastly-Frontend-Service als Proxy für Backend-Requests:

```vcl
if (req.url.path ~ "^/store-api/") {
  set req.http.host = "backend.mydomain.com";
  set req.backend = F_Backend__Shopware_instance_;
  return (pass);  # WICHTIG: kein Cache auf Frontend-Fastly-Service
}
```

## Blackfire Node.js Profiling

```bash
npm install @blackfireio/node-tracing
```

Env: `BLACKFIRE_ENABLE=1`

Datei `server/plugins/blackfire.ts` anlegen (Details → Deep Reference).

## Vertiefung

[references/deep/composable-frontends.md](references/deep/composable-frontends.md)
