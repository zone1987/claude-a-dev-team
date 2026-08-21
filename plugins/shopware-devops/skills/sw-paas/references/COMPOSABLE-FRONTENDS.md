# Shopware PaaS — Composable Frontends (Nuxt.js)

## Store API caching (backend)

```bash
composer require shopware-labs/swag-store-api-cache
```

- Caches selected POST `/store-api/` requests via Fastly
- Ships its own Fastly snippets (they replace the standard snippets)
- Additional routes configurable via `SwagStoreAPICache.config.additionalCacheableRoutes`
- Enable soft purge!

## Frontend caching (Nuxt.js)

In `nuxt.config.ts` with ISR (Incremental Static Regeneration):

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

Frontend cache invalidation: only the Fastly backend service.
Shopware does not trigger frontend cache invalidation.

## Avoiding CORS (OPTIONS requests)

The Fastly frontend service as a proxy for backend requests:

```vcl
if (req.url.path ~ "^/store-api/") {
  set req.http.host = "backend.mydomain.com";
  set req.backend = F_Backend__Shopware_instance_;
  return (pass);  # IMPORTANT: no caching on the frontend Fastly service
}
```

## Blackfire Node.js profiling

```bash
npm install @blackfireio/node-tracing
```

Env: `BLACKFIRE_ENABLE=1`

Create the file `server/plugins/blackfire.ts` (details → Deep Reference).

## Deep dive

[COMPOSABLE-FRONTENDS-DETAIL.md](COMPOSABLE-FRONTENDS-DETAIL.md)
