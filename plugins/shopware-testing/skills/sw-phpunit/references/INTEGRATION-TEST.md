# Shopware 6 — Integration Test

Tests against a real DB/container (DAL, services). `IntegrationTestBehaviour` wraps every test method in a
transaction (rolled back afterwards) → isolated, fast tests.

```php
public function testWrite(): void
{
    $id = Uuid::randomHex();
    $this->repo->create([['id' => $id, 'name' => 'X']], Context::createDefaultContext());
    $entity = $this->repo->search(new Criteria([$id]), Context::createDefaultContext())->first();
    static::assertSame('X', $entity->getName());
}
```

Fetch services via `$this->getContainer()->get(...)`. Prefer `assertSame` (ADR), create data through builders/fixtures
(`sw-test-builder`, `sw-test-fixtures`). For pure logic without a DB → a unit test (`sw-unit-test`).

→ [../shopware-phpunit/`INTEGRATION-TEST-INTEGRATION-REPOSITORY-TESTING.md`](../shopware-phpunit/`INTEGRATION-TEST-INTEGRATION-REPOSITORY-TESTING.md`)
