# Shopware 6 — Store-API-Route

Kundenseitige API-Route (Headless/Storefront). Abstrakte Basisklasse + konkrete Route, Route-Scope `store-api`.

```php
#[Route(defaults: ['_routeScope' => ['store-api']])]
class FfExampleRoute extends AbstractFfExampleRoute
{
    #[Route(path: '/store-api/ff/example', name: 'store-api.ff.example', methods: ['GET','POST'])]
    public function load(Request $request, SalesChannelContext $context): FfExampleRouteResponse
    {
        return new FfExampleRouteResponse($this->load(...));
    }
    public function getDecorated(): AbstractFfExampleRoute { throw new DecorationPatternException(self::class); }
}
```

Response erweitert `StoreApiResponse` (cacheable). Abstract-Klasse ermöglicht Decoration. Auth via `sw-access-key`
(`shopware-api` → `sw-store-api-auth`). Für Frontends typisieren (`@shopware/api-gen`). Bestehende Route ändern: `sw-store-api-override`.

→ Store-API-Details: [STORE-API.md](STORE-API.md) · Beispiele: [examples/StoreApiRoute.php](examples/StoreApiRoute.php), [examples/StoreApiRouteResponse.php](examples/StoreApiRouteResponse.php)
