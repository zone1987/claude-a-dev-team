# Shopware 6 — Storefront page

A page bundles all data of a complete page. Pattern: **page struct** (data) + **PageLoader** (populates it).

```php
class ExamplePage extends Page
{
    protected ExampleEntity $example;
    public function getExample(): ExampleEntity { return $this->example; }
    public function setExample(ExampleEntity $e): void { $this->example = $e; }
}
```

The page extends `Page` (which already contains header/footer/meta via `GenericPageLoader`). The PageLoader (`sw-page-loader`)
first loads the generic page, adds its own data and dispatches an `ExamplePageLoadedEvent` (extensibility).
Build partial sections (e.g. AJAX reloading) as a **pagelet** (`sw-storefront-pagelet`).
