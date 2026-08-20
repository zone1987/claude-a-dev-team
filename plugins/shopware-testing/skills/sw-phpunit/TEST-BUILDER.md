# Shopware 6 — Test-Builder

Builder erzeugen komplexe Entity-Payloads lesbar (fluent). Shopware liefert u.a. `ProductBuilder`; eigene Builder
folgen demselben Muster.

```php
$product = (new ProductBuilder($ids, 'SW-1'))
    ->price(19.99)
    ->stock(10)
    ->category('cat-1')
    ->visibility()
    ->build();
```

Ein eigener Builder hält eine `IdsCollection`, bietet fluent-Setter und ein `build(): array` (DAL-Payload).
Reduziert Boilerplate und macht Tests robust gegen Pflichtfeld-Änderungen. Nutzung mit Fixtures (`sw-test-fixtures`).

→ [../shopware-phpunit/`TEST-BUILDER-DATA-PRODUCT-BUILDER.md`](../shopware-phpunit/`TEST-BUILDER-DATA-PRODUCT-BUILDER.md`)
