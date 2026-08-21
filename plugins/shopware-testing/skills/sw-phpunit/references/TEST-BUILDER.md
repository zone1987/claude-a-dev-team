# Shopware 6 — Test Builder

Builders make complex entity payloads readable (fluent). Shopware ships `ProductBuilder` among others; your own builders
follow the same pattern.

```php
$product = (new ProductBuilder($ids, 'SW-1'))
    ->price(19.99)
    ->stock(10)
    ->category('cat-1')
    ->visibility()
    ->build();
```

Your own builder holds an `IdsCollection`, offers fluent setters and a `build(): array` (DAL payload).
It cuts boilerplate and makes tests resilient to changes in required fields. Use it with fixtures (`sw-test-fixtures`).

→ [../shopware-phpunit/`TEST-BUILDER-DATA-PRODUCT-BUILDER.md`](../shopware-phpunit/`TEST-BUILDER-DATA-PRODUCT-BUILDER.md`)
