# Shopware 6 — Storefront caching

Storefront pages are HTTP-cached. Mark your own controller routes and invalidate the cache correctly.

```php
#[Route(path: '/ff/example', name: 'frontend.ff.example', defaults: ['_httpCache' => true])]
```

- `_httpCache` enables caching for the route; without it the route is dynamic (e.g. cart).
- **Cache tags** for targeted invalidation (`CacheTagCollection` / tags on the entity cache) when data changes.
- **ESI/pagelets** for dynamic sections within cached pages (`sw-storefront-pagelet`).
- Never put customer-specific content into the shared cache (no-store / pagelet).

Behavior depends on the configured cache/reverse proxy. Set caching deliberately on AJAX endpoints (`sw-ajax-data`).
