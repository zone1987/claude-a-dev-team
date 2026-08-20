# shopware-testing

> Testing across every level (PHPUnit, Jest, Playwright).

`shopware-testing` covers **testing across every level of the test pyramid**.

**PHP/PHPUnit:** setup and kernel bootstrap (`IntegrationTestBehaviour`), **unit tests** (pure logic, mocked) vs.
**integration tests** (real DAL/DB with transaction rollback), **Store API** and **Admin API tests**, **fixtures**
and **builders** (with `IdsCollection`) as well as **static mocks** (`StaticEntityRepository`, `StaticSystemConfigService`).
**JavaScript:** **Jest** for the administration (including `fail-on-console`) and Vue component tests (`@vue/test-utils`,
`Shopware.Component.build`) as well as Jest for **storefront** JS plugins. **E2E:** **Playwright** (Acceptance Test Suite)
for critical end-to-end flows.

Specialist: **`shopware-tester`**; the scaffolder **`/sw-test`** generates the appropriate test per class/level. **When
to use:** when writing/repairing tests or to safeguard code changes (for example, delegated by
`shopware-dev`). Conventions/static analysis are covered by `shopware-quality`.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official sources and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-testing@claude-a-dev-team
```

## Skills (3)

| Skill | Description |
|---|---|
| `sw-e2e` | Shopware end-to-end testing with Playwright: setup, fixtures and the shop-specific helpers. Use when writing a Playwright end-to-end test against a Shopware shop |
| `sw-javascript` | Shopware JavaScript testing: Jest for the administration and the storefront, Vue component tests. Use when writing a Jest or Vue test for Shopware |
| `sw-phpunit` | Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-tester` | Test specialist for Shopware 6 plugins across every level: PHPUnit (unit/integration/Store API/Admin API), test data (fixtures/builders), mocks (StaticEntityRepository/StaticSystemConfigService), Jest (admin/Vue, storefront), Playwright E2E |

## Commands (1)

| Command | Description |
|---|---|
| `/sw-test` | Scaffolds a suitable test for a Shopware 6 class (unit/integration/Store API/Admin API, respectively) |
