# Shopware 6 — Mocking a Repository

Simulate repositories without a DB in unit tests — preferably with `StaticEntityRepository` (ADR "mocking repositories"),
which returns predefined search results.

```php
$repo = new StaticEntityRepository([
    new EntitySearchResult('ff_example', 1, new EntityCollection([$entity]), null, new Criteria(), $context),
]);
$sut = new FfService($repo);
```

This avoids the fragile manual `createMock(EntityRepository::class)` with `search` stubs. Verify write operations with
a spy where needed. For real DAL semantics → an integration test (`sw-integration-test`). Mocking config: `sw-mock-system-config`.

→ [../shopware-phpunit/`MOCK-REPOSITORY-MOCK-STATIC-ENTITY-REPOSITORY.md`](../shopware-phpunit/`MOCK-REPOSITORY-MOCK-STATIC-ENTITY-REPOSITORY.md`)
