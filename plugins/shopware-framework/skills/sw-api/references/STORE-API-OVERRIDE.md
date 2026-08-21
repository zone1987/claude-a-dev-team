# Shopware 6 — Overriding a Store API route

Core routes are designed as `Abstract*Route` and are extended through decoration (not replaced).

```php
class FfProductRouteDecorator extends AbstractProductListingRoute
{
    public function __construct(private readonly AbstractProductListingRoute $decorated) {}
    public function getDecorated(): AbstractProductListingRoute { return $this->decorated; }

    public function load(string $categoryId, Request $request, SalesChannelContext $context, Criteria $criteria): ProductListingRouteResponse
    {
        $response = $this->decorated->load($categoryId, $request, $context, $criteria);
        // Enrich response / adjust criteria beforehand
        return $response;
    }
}
```

Register in `services.xml` with `decorates="..."`, inject `.inner` (`sw-service-decoration`). Often an
event/subscriber is enough for enrichment (e.g. criteria/result events) — check that first. Own new route: `sw-store-api-route`.
