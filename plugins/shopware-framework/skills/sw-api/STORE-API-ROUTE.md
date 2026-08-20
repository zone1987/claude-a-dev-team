# Shopware 6 — Store API route

Customer-facing API route (headless/storefront). Abstract base class + concrete route, route scope `store-api`.

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

The response extends `StoreApiResponse` (cacheable). The abstract class enables decoration. Auth via `sw-access-key`
(`shopware-api` → `sw-store-api-auth`). Type it for frontends (`@shopware/api-gen`). Change an existing route: `sw-store-api-override`.

→ Store API details: [STORE-API.md](STORE-API.md) · Examples: [examples/StoreApiRoute.php](examples/StoreApiRoute.php), [examples/StoreApiRouteResponse.php](examples/StoreApiRouteResponse.php)
