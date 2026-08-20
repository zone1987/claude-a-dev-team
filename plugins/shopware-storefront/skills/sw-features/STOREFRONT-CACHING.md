# Shopware 6 — Storefront-Caching

Storefront-Seiten werden http-gecacht. Eigene Controller-Routen markieren und Cache korrekt invalidieren.

```php
#[Route(path: '/ff/example', name: 'frontend.ff.example', defaults: ['_httpCache' => true])]
```

- `_httpCache` aktiviert Caching der Route; ohne → dynamisch (z.B. Warenkorb).
- **Cache-Tags** für gezielte Invalidierung (`CacheTagCollection` / Tags am Entity-Cache) bei Datenänderung.
- **ESI/Pagelets** für dynamische Teilbereiche in gecachten Seiten (`sw-storefront-pagelet`).
- Kundenspezifische Inhalte nie in den geteilten Cache (no-store / Pagelet).

Verhalten hängt vom konfigurierten Cache/Reverse-Proxy ab. Bei AJAX-Endpunkten Cache bewusst setzen (`sw-ajax-data`).
