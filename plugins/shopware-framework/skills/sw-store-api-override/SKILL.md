---
name: sw-store-api-override
description: >
  Eine bestehende Shopware-6 Store-API-Route anpassen via Decoration (AbstractRoute dekorieren, getDecorated, inner-Route).
  Trigger: "Store API Route überschreiben", "Route dekorieren store-api", "getDecorated route", "decorate AbstractRoute",
  "store-api response anreichern". Shopware 6.7.
---

# Shopware 6 — Store-API-Route überschreiben

Core-Routen sind als `Abstract*Route` ausgelegt und werden per Decoration erweitert (nicht ersetzt).

```php
class FfProductRouteDecorator extends AbstractProductListingRoute
{
    public function __construct(private readonly AbstractProductListingRoute $decorated) {}
    public function getDecorated(): AbstractProductListingRoute { return $this->decorated; }

    public function load(string $categoryId, Request $request, SalesChannelContext $context, Criteria $criteria): ProductListingRouteResponse
    {
        $response = $this->decorated->load($categoryId, $request, $context, $criteria);
        // Response anreichern / Criteria vorab anpassen
        return $response;
    }
}
```

In `services.xml` mit `decorates="..."` registrieren, `.inner` injizieren (`sw-service-decoration`). Oft reicht ein
Event/Subscriber zum Anreichern (z.B. Criteria-/Result-Events) — erst prüfen. Eigene neue Route: `sw-store-api-route`.
