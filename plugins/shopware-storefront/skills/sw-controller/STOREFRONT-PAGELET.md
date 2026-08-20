# Shopware 6 — Storefront pagelet

A pagelet is an independently loadable section (e.g. offcanvas cart, listing block) — usable in multiple
pages and reloadable via AJAX.

```php
class ExamplePagelet extends Pagelet
{
    protected ExampleCollection $items;
    public function getItems(): ExampleCollection { return $this->items; }
    public function setItems(ExampleCollection $i): void { $this->items = $i; }
}
```

A dedicated `PageletLoader` populates the struct and dispatches an `ExamplePageletLoadedEvent`. A pagelet knows
**no** header/footer (that is the page's responsibility). For complete pages → `sw-storefront-page`.
