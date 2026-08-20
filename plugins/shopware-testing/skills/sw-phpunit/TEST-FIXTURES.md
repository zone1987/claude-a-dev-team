# Shopware 6 — Test-Fixtures

Wiederverwendbare Testdaten über Helper/Traits anlegen; IDs zentral über eine `IdsCollection` verwalten
(lesbare, stabile Referenzen).

```php
$ids = new IdsCollection();
$this->getContainer()->get('product.repository')->create([
    (new ProductBuilder($ids, 'p1'))->price(10)->build(),
], Context::createDefaultContext());
$productId = $ids->get('p1');
```

Komplexe Entities über **Builder** (`sw-test-builder`). Wiederkehrende Setups in Trait/Helper kapseln. Bei DB-Tests
mit `IntegrationTestBehaviour` (Rollback). Für Symfony-Foundry-artige Factories siehe generische Skills.

→ [../shopware-phpunit/`TEST-FIXTURES-DATA-TEST-FIXTURES.md`](../shopware-phpunit/`TEST-FIXTURES-DATA-TEST-FIXTURES.md`)
