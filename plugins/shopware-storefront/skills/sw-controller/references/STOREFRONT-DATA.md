# Shopware 6 — Attaching data to existing pages

To enrich core pages (product, listing, checkout …), listen to their `*PageLoadedEvent` and attach the result as an
**extension** to the page — no custom controller needed.

```php
public static function getSubscribedEvents(): array
{
    return [ ProductPageLoadedEvent::class => 'onProductPage' ];
}
public function onProductPage(ProductPageLoadedEvent $event): void
{
    $page = $event->getPage();
    $page->addExtension('ffRelated', $this->loadRelated($page->getProduct(), $event->getSalesChannelContext()));
}
```

Access it in the template via `page.extensions.ffRelated`. For entirely custom pages → controller + PageLoader
(`sw-storefront-controller`, `sw-page-loader`). Performance: load only what is needed.
