---
name: sw-phpunit
description: Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin.
---

# Shopware PHPUnit testing

The PHP side. Integration tests need the kernel; unit tests need the mocks listed here instead.

## Read the standard first

**[`sw-testing-standard`](../sw-testing-standard/SKILL.md) decides what must exist**; this
skill covers how to write it.

- **PHPUnit belongs to the project, never to the plugin.** Scripts call
  `../../../vendor/bin/phpunit`. A plugin that pins its own version pins one that goes
  stale. → `STANDARD-GATE.md`, which also carries the five phpunit configs and both
  bootstraps.
- **100 % coverage, no exemptions** beyond `src/Resources/config`. Every test names its
  subject with `#[CoversClass]`, or the figure depends on test order.
  → `STANDARD-COVERAGE.md`
- **A mutation baseline**, every survivor killed or documented. → `STANDARD-MUTATION.md`
- **Architecture tests are mandatory** and run inside PHPStan via phpat.
  → `STANDARD-ARCHITECTURE.md`
- **Test first, and the test fails first.** Names state rules, not methods.
  → `STANDARD-WORKFLOW.md`

## Reference map

**Setup**

- **[SETUP.md](references/SETUP.md)**: the two bootstraps, the four test directories, and why PHPUnit belongs to the project.
- **[BASE-TEST-CLASS.md](references/BASE-TEST-CLASS.md)**: what a plugin's own base test class should and should not carry.

**Writing a test**

- **[UNIT-TEST.md](references/UNIT-TEST.md)**: isolated logic, no kernel, no database. Where most of the 100 % comes from.
- **[INTEGRATION-TEST.md](references/INTEGRATION-TEST.md)**: against a real container and DAL, with `IntegrationTestBehaviour`.
- **[REPOSITORY-TEST.md](references/REPOSITORY-TEST.md)**: testing repositories and DAL semantics for real.
- **[STORE-API-TEST.md](references/STORE-API-TEST.md)**: Store API routes through a sales channel browser.
- **[ADMIN-API-TEST.md](references/ADMIN-API-TEST.md)**: admin API endpoints with an authenticated client, including ACL cases.

**Test data**

- **[TEST-BUILDER.md](references/TEST-BUILDER.md)**: fluent builders for complex entity payloads, with `IdsCollection`.
- **[TEST-FIXTURES.md](references/TEST-FIXTURES.md)**: reusable test data through helpers and traits.

**Doubles**

- **[MOCK-REPOSITORY.md](references/MOCK-REPOSITORY.md)**: `StaticEntityRepository` rather than a hand-rolled repository mock.
- **[MOCK-DEFINITION-REGISTRY.md](references/MOCK-DEFINITION-REGISTRY.md)**: Compile a DAL definition without a kernel — and the static cache that makes every mutant in `defineFields()` survive by construction.
- **[MOCK-LOGGER.md](references/MOCK-LOGGER.md)**: Assert **what** was logged, not that logging happened. Plus the helper name that takes the whole suite down.
- **[MOCK-SYSTEM-CONFIG.md](references/MOCK-SYSTEM-CONFIG.md)**: `StaticSystemConfigService` for config-dependent logic.
- **[MOCK-SERVICE.md](references/MOCK-SERVICE.md)**: replacing a service in the container, and stub versus mock.

**Assertions**

- **[ASSERT-SAME.md](references/ASSERT-SAME.md)**: `static::assertSame` over `assertEquals`, and why.
- **[ASSERT-EXCEPTIONS.md](references/ASSERT-EXCEPTIONS.md)**: `expectExceptionObject` asserts the message too.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
