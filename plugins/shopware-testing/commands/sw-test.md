---
name: sw-test
description: Scaffolds a fitting test for a Shopware 6 class (unit/integration/Store API/Admin API or Jest), including setup, fixtures or builders, and mocks.
argument-hint: <ClassOrPath> [--plugin <PluginName>] [--type unit|integration|store-api|admin-api|jest]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-test

Produce a test for the given class or file. Delegate to `shopware-tester`.

## Steps
1. Analyse the target class (dependencies, database use), then pick the test level (or take `--type`).
2. Create the test file under `tests/`, mirroring the class:
   - Unit: no kernel, mock the dependencies (`StaticEntityRepository`/`StaticSystemConfigService`).
   - Integration: `IntegrationTestBehaviour`, real repositories, builders and fixtures.
   - Store or Admin API: `SalesChannelApiTestBehaviour`/`AdminApiTestBehaviour`.
   - Jest (admin/storefront): a `.spec.js` with `@vue/test-utils` or a plugin instance.
3. `assertSame`, test names that state the expectation, arrange-act-assert.
4. Note how to run them (`vendor/bin/phpunit`, `composer admin:unit`/`storefront:unit`).

Never overwrite existing tests; only add to them.
