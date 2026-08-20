# Shopware 6 — Test Fixtures

Create reusable test data through helpers/traits; manage IDs centrally in an `IdsCollection`
(readable, stable references).

```php
$ids = new IdsCollection();
$this->getContainer()->get('product.repository')->create([
    (new ProductBuilder($ids, 'p1'))->price(10)->build(),
], Context::createDefaultContext());
$productId = $ids->get('p1');
```

Build complex entities with **builders** (`sw-test-builder`). Encapsulate recurring setups in a trait/helper. For DB tests
use `IntegrationTestBehaviour` (rollback). For Symfony-Foundry-style factories see the generic skills.

→ [../shopware-phpunit/`TEST-FIXTURES-DATA-TEST-FIXTURES.md`](../shopware-phpunit/`TEST-FIXTURES-DATA-TEST-FIXTURES.md`)
