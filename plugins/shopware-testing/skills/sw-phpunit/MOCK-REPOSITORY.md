# Shopware 6 — Repository mocken

Für Unit-Tests Repositories ohne DB simulieren — bevorzugt mit `StaticEntityRepository` (ADR „mocking repositories"),
das vordefinierte Suchergebnisse zurückgibt.

```php
$repo = new StaticEntityRepository([
    new EntitySearchResult('ff_example', 1, new EntityCollection([$entity]), null, new Criteria(), $context),
]);
$sut = new FfService($repo);
```

Vermeidet fragiles manuelles `createMock(EntityRepository::class)` mit `search`-Stubs. Schreibvorgänge ggf. über
einen Spy prüfen. Für echte DAL-Semantik → Integrationstest (`sw-integration-test`). Config mocken: `sw-mock-system-config`.

→ [../shopware-phpunit/`MOCK-REPOSITORY-MOCK-STATIC-ENTITY-REPOSITORY.md`](../shopware-phpunit/`MOCK-REPOSITORY-MOCK-STATIC-ENTITY-REPOSITORY.md`)
