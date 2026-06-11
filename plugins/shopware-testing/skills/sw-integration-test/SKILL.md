---
name: sw-integration-test
description: >
  Integrationstests in Shopware 6: IntegrationTestBehaviour, echte DAL-Repositories, Container-Services, DB-Transaktion
  je Test, Daten anlegen/prüfen. Trigger: "Integrationstest shopware", "IntegrationTestBehaviour", "Repository test",
  "getContainer test", "DAL test", "Datenbank test shopware". Shopware 6.7.
---

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

→ [../shopware-phpunit/references/integration-repository-testing.md](../shopware-phpunit/references/integration-repository-testing.md)
