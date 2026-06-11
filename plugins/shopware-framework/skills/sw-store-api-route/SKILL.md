---
name: sw-store-api-route
description: >
  Eigene Store-API-Route in Shopware 6: AbstractRoute + Route mit _routeScope store-api, Response-Struct, sw-access-key,
  Registrierung. Trigger: "Store API Route", "eigene store-api route", "AbstractRoute store-api", "_routeScope store-api",
  "StoreApiResponse", "custom store api endpoint". Shopware 6.7. Scaffolder: /sw-store-api-route.
---

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

→ Store-API-Details: [references/store-api.md](references/store-api.md) · Beispiele: [examples/StoreApiRoute.php](examples/StoreApiRoute.php), [examples/StoreApiRouteResponse.php](examples/StoreApiRouteResponse.php)
