---
name: sw-phpunit
description: Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin.
---

# Shopware PHPUnit testing

The PHP side. Integration tests need the kernel; unit tests need the mocks listed here instead.

## Reference map

- **[ADMIN-API-TEST.md](ADMIN-API-TEST.md)**: Testet Admin-API-Endpunkte mit authentifiziertem Client.
- **[INTEGRATION-TEST.md](INTEGRATION-TEST.md)**: Testet gegen echte DB/Container.
- **[MOCK-REPOSITORY.md](MOCK-REPOSITORY.md)**: Für Unit-Tests Repositories ohne DB simulieren — bevorzugt mit `StaticEntityRepository`, das vordefinierte Su….
- **[MOCK-SYSTEM-CONFIG.md](MOCK-SYSTEM-CONFIG.md)**: Config-abhängige Logik im Unit-Test ohne DB testen mit `StaticSystemConfigService`.
- **[SETUP.md](SETUP.md)**: Plugin-Tests laufen gegen den Shopware-Kernel. [SETUP-TESTING](SETUP-TESTING.md).
- **[SHOPWARE-PHPUNIT.md](SHOPWARE-PHPUNIT.md)**: Read relevant reference files from the `references/` directory based on the task at hand. [SHOPWARE-PHPUNIT--SECTIONS](SHOPWARE-PHPUNIT--SECTIONS.md), [SHOPWARE-PHPUNIT--TEMPLATE](SHOPWARE-PHPUNIT--TEMPLATE.md), [SHOPWARE-PHPUNIT-API-STORE-API-TESTING](SHOPWARE-PHPUNIT-API-STORE-API-TESTING.md), [SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER](SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER.md), [SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES](SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES.md), [SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING](SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING.md), [SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION](SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY](SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE](SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md), [SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS](SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS.md), [SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP](SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME](SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT](SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT.md).
- **[STORE-API-TEST.md](STORE-API-TEST.md)**: Testet Store-API-Routen end-to-end über einen SalesChannel-Browser.
- **[TEST-BUILDER.md](TEST-BUILDER.md)**: Builder erzeugen komplexe Entity-Payloads lesbar.
- **[TEST-FIXTURES.md](TEST-FIXTURES.md)**: Wiederverwendbare Testdaten über Helper/Traits anlegen; IDs zentral über eine `IdsCollection` verwalten.
- **[UNIT-TEST.md](UNIT-TEST.md)**: Testet isolierte Logik **ohne** Kernel/DB — Abhängigkeiten werden gemockt.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
