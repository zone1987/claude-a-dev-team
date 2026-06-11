---
name: sw-storefront-pagelet
description: >
  Ein Storefront-Pagelet in Shopware 6: wiederverwendbarer Teilbereich (extends Pagelet) mit eigenem PageletLoader,
  ideal für AJAX-Nachladung. Trigger: "Pagelet", "PageletLoader", "Teilbereich Seite", "AJAX block storefront",
  "wiederverwendbarer Seitenteil". Shopware 6.7.
---

# Shopware 6 — Storefront-Pagelet

Ein Pagelet ist ein eigenständig ladbarer Teilbereich (z.B. Offcanvas-Cart, Listing-Block) — nutzbar in mehreren
Pages und per AJAX nachladbar.

```php
class ExamplePagelet extends Pagelet
{
    protected ExampleCollection $items;
    public function getItems(): ExampleCollection { return $this->items; }
    public function setItems(ExampleCollection $i): void { $this->items = $i; }
}
```

Eigener `PageletLoader` befüllt das Struct und dispatcht ein `ExamplePageletLoadedEvent`. Ein Pagelet kennt
**keinen** Header/Footer (das ist Sache der Page). Für komplette Seiten → `sw-storefront-page`.
