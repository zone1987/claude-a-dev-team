# Shopware 6 — Storefront controller

Extends `Storefront\Controller\StorefrontController`. Routes use `_routeScope: ['storefront']`.

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

Route name convention `frontend.*`. Data comes from a **PageLoader** (`sw-page-loader`), not directly from the controller.
Use `renderStorefront()` for HTML, `$this->json()`/`renderStorefront` for AJAX (`sw-ajax-data`). Caching: `sw-storefront-caching`.

→ Controllers, routing, examples: [STOREFRONT.md](STOREFRONT.md)
→ Scaffold: [examples/StorefrontController.php](examples/StorefrontController.php) · [examples/routes.xml](examples/routes.xml)
