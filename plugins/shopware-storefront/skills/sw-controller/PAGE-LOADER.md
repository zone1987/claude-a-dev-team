# Shopware 6 — PageLoader

The PageLoader builds the page struct: first the generic page (header/footer/meta), then its own data,
then the event.

```php
public function load(Request $request, SalesChannelContext $context): ExamplePage
{
    $page = ExamplePage::createFrom($this->genericLoader->load($request, $context));
    $page->setExample($this->loadExample($request, $context));
    $this->eventDispatcher->dispatch(new ExamplePageLoadedEvent($page, $context, $request));
    return $page;
}
```

Always use `GenericPageLoader` as the base (`createFrom`). The `*PageLoadedEvent` is the extension point for other
plugins (`sw-events-subscriber` / `sw-storefront-data`). Minimize heavy queries (use targeted criteria).
