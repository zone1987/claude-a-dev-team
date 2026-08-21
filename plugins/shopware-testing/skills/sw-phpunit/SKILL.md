---
name: sw-phpunit
description: Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin.
---

# Shopware PHPUnit testing

The PHP side. Integration tests need the kernel; unit tests need the mocks listed here instead.

## Reference map

- **[ADMIN-API-TEST.md](references/ADMIN-API-TEST.md)**: Tests admin API endpoints with an authenticated client.
- **[INTEGRATION-TEST.md](references/INTEGRATION-TEST.md)**: Tests against a real DB/container.
- **[MOCK-REPOSITORY.md](references/MOCK-REPOSITORY.md)**: Simulate repositories without a DB in unit tests — preferably with `StaticEntityRepository`, which returns ….
- **[MOCK-SYSTEM-CONFIG.md](references/MOCK-SYSTEM-CONFIG.md)**: Test config-dependent logic in unit tests without a DB using `StaticSystemConfigService`.
- **[SETUP.md](references/SETUP.md)**: Plugin tests run against the Shopware kernel. [SETUP-TESTING](references/SETUP-TESTING.md).
- **[SHOPWARE-PHPUNIT.md](references/SHOPWARE-PHPUNIT.md)**: Read relevant reference files from the `references/` directory based on the task at hand. [SHOPWARE-PHPUNIT--SECTIONS](references/SHOPWARE-PHPUNIT--SECTIONS.md), [SHOPWARE-PHPUNIT--TEMPLATE](references/SHOPWARE-PHPUNIT--TEMPLATE.md), [SHOPWARE-PHPUNIT-API-STORE-API-TESTING](references/SHOPWARE-PHPUNIT-API-STORE-API-TESTING.md), [SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER](references/SHOPWARE-PHPUNIT-DATA-PRODUCT-BUILDER.md), [SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES](references/SHOPWARE-PHPUNIT-DATA-TEST-FIXTURES.md), [SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING](references/SHOPWARE-PHPUNIT-INTEGRATION-REPOSITORY-TESTING.md), [SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION](references/SHOPWARE-PHPUNIT-MOCK-SERVICE-DECORATION.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY](references/SHOPWARE-PHPUNIT-MOCK-STATIC-ENTITY-REPOSITORY.md), [SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE](references/SHOPWARE-PHPUNIT-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md), [SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS](references/SHOPWARE-PHPUNIT-SETUP-BASE-TEST-CLASS.md), [SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP](references/SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME](references/SHOPWARE-PHPUNIT-SETUP-PREFER-ASSERTSAME.md), [SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT](references/SHOPWARE-PHPUNIT-SETUP-PREFER-EXPECT-EXCEPTION-OBJECT.md).
- **[STORE-API-TEST.md](references/STORE-API-TEST.md)**: Tests Store API routes end-to-end through a sales channel browser.
- **[TEST-BUILDER.md](references/TEST-BUILDER.md)**: Builders make complex entity payloads readable.
- **[TEST-FIXTURES.md](references/TEST-FIXTURES.md)**: Create reusable test data through helpers/traits; manage IDs centrally in an `IdsCollection`.
- **[UNIT-TEST.md](references/UNIT-TEST.md)**: Tests isolated logic **without** kernel or DB — dependencies are mocked.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
