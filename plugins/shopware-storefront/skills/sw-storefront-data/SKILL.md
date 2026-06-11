---
name: sw-storefront-data
description: >
  Zusätzliche Daten an eine bestehende Storefront-Page hängen (ohne eigenen Controller) via Subscriber auf das
  PageLoadedEvent und addExtension. Trigger: "Daten an Page hängen", "ProductPageLoadedEvent", "addExtension page",
  "PageLoadedEvent subscriber", "Daten zu bestehender Seite", "page extension storefront". Shopware 6.7.
---

# Shopware 6 — Daten an bestehende Pages hängen

Um Core-Seiten (Produkt, Listing, Checkout …) anzureichern, auf ihr `*PageLoadedEvent` hören und das Ergebnis als
**Extension** an die Page hängen — kein eigener Controller nötig.

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

Im Template via `page.extensions.ffRelated` zugreifen. Für ganz eigene Seiten → Controller + PageLoader
(`sw-storefront-controller`, `sw-page-loader`). Performance: nur laden, was gebraucht wird.
