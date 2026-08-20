# Shopware 6 — Integrationstest

Testet gegen echte DB/Container (DAL, Services). `IntegrationTestBehaviour` kapselt jede Testmethode in eine
Transaktion (Rollback danach) → isolierte, schnelle Tests.

```php
public function testWrite(): void
{
    $id = Uuid::randomHex();
    $this->repo->create([['id' => $id, 'name' => 'X']], Context::createDefaultContext());
    $entity = $this->repo->search(new Criteria([$id]), Context::createDefaultContext())->first();
    static::assertSame('X', $entity->getName());
}
```

Services via `$this->getContainer()->get(...)`. Bevorzugt `assertSame` (ADR), Daten über Builder/Fixtures
(`sw-test-builder`, `sw-test-fixtures`). Für reine Logik ohne DB → Unit-Test (`sw-unit-test`).

→ [../shopware-phpunit/`INTEGRATION-TEST-INTEGRATION-REPOSITORY-TESTING.md`](../shopware-phpunit/`INTEGRATION-TEST-INTEGRATION-REPOSITORY-TESTING.md`)
