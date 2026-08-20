# Shopware 6 — Storefront-Controller

Erweitert `Storefront\Controller\StorefrontController`. Routen mit `_routeScope: ['storefront']`.

```php
#[Route(defaults: ['_routeScope' => ['storefront']])]
class ExampleController extends StorefrontController
{
    public function __construct(private readonly ExamplePageLoader $pageLoader) {}

    #[Route(path: '/ff/example', name: 'frontend.ff.example', methods: ['GET'])]
    public function index(Request $request, SalesChannelContext $context): Response
    {
        $page = $this->pageLoader->load($request, $context);
        return $this->renderStorefront('@FfExample/storefront/page/example/index.html.twig', ['page' => $page]);
    }
}
```

Route-Name-Konvention `frontend.*`. Daten kommen aus einem **PageLoader** (`sw-page-loader`), nicht direkt im Controller.
`renderStorefront()` für HTML, `$this->json()`/`renderStorefront` für AJAX (`sw-ajax-data`). Caching: `sw-storefront-caching`.

→ Controller, Routing, Beispiele: [STOREFRONT.md](STOREFRONT.md)
→ Gerüst: [examples/StorefrontController.php](examples/StorefrontController.php) · [examples/routes.xml](examples/routes.xml)
