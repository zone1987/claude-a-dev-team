---
name: sw-page-loader
description: >
  Einen Storefront-PageLoader in Shopware 6 bauen: GenericPageLoader nutzen, eigene Daten ergänzen, PageLoadedEvent
  dispatchen; Page-Loader-Extension-Architektur. Trigger: "PageLoader", "GenericPageLoader", "Page laden",
  "PageLoadedEvent dispatch", "load() page", "Seitendaten laden". Shopware 6.7.
---

# Shopware 6 — PageLoader

Der PageLoader erzeugt das Page-Struct: zuerst die generische Page (Header/Footer/Meta), dann eigene Daten,
dann Event.

```php
public function load(Request $request, SalesChannelContext $context): ExamplePage
{
    $page = ExamplePage::createFrom($this->genericLoader->load($request, $context));
    $page->setExample($this->loadExample($request, $context));
    $this->eventDispatcher->dispatch(new ExamplePageLoadedEvent($page, $context, $request));
    return $page;
}
```

Immer `GenericPageLoader` als Basis (`createFrom`). Das `*PageLoadedEvent` ist der Erweiterungspunkt für andere
Plugins (`sw-events-subscriber` / `sw-storefront-data`). Schwere Queries minimieren (Criteria gezielt).
