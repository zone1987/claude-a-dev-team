---
name: sw-test-builder
description: >
  Test-Daten-Builder in Shopware 6: ProductBuilder & eigene Builder (fluent API) für komplexe Entity-Payloads in Tests.
  Trigger: "ProductBuilder", "Test Builder shopware", "fluent test data", "Builder pattern test", "eigener TestDataBuilder".
  Shopware 6.7.
---

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

→ [../shopware-phpunit/references/data-product-builder.md](../shopware-phpunit/references/data-product-builder.md)
