---
name: sw-phpunit
description: Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin.
---

# Shopware PHPUnit testing

The PHP side. Integration tests need the kernel; unit tests need the mocks listed here instead.

## Reference map

- **[ADMIN-API-TEST.md](ADMIN-API-TEST.md)**: Tests admin API endpoints with an authenticated client.
- **[INTEGRATION-TEST.md](INTEGRATION-TEST.md)**: Tests against a real DB/container.
- **[MOCK-REPOSITORY.md](MOCK-REPOSITORY.md)**: Simulate repositories without a DB in unit tests — preferably with `StaticEntityRepository`, which returns ….
- **[MOCK-SYSTEM-CONFIG.md](MOCK-SYSTEM-CONFIG.md)**: Test config-dependent logic in unit tests without a DB using `StaticSystemConfigService`.
- **[SETUP.md](SETUP.md)**: Plugin tests run against the Shopware kernel. [SETUP-TESTING](SETUP-TESTING.md).
- **[SHOPWARE-PHPUNIT.md](SHOPWARE-PHPUNIT.md)**: Read relevant reference files from the `references/` directory based on the task at hand. [SHOPWARE-PHPUNIT--SECTIONS](SHOPWARE-PHPUNIT--SECTIONS.md), [SHOPWARE-PHPUNIT--TEMPLATE](SHOPWARE-PHPUNIT--TEMPLATE.md), [SHOPWARE-PHPUNIT-API-STORE-API-TESTING](SHOPWARE-PHPUNIT-API-STORE-API-TESTING.md), [SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER](SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER.md), [SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES](SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES.md), [SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING](SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING.md), [SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION](SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY](SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE](SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md), [SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS](SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS.md), [SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP](SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME](SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT](SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT.md).
- **[STORE-API-TEST.md](STORE-API-TEST.md)**: Tests Store API routes end-to-end through a sales channel browser.
- **[TEST-BUILDER.md](TEST-BUILDER.md)**: Builders make complex entity payloads readable.
- **[TEST-FIXTURES.md](TEST-FIXTURES.md)**: Create reusable test data through helpers/traits; manage IDs centrally in an `IdsCollection`.
- **[UNIT-TEST.md](UNIT-TEST.md)**: Tests isolated logic **without** kernel or DB — dependencies are mocked.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
