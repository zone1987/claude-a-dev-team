# shopware-testing

> Testing across every level (PHPUnit, Jest, Playwright).

`shopware-testing` covers **testing across every level of the test pyramid**.

**`sw-testing-standard` is law, not advice.** It settles what must exist in every Shopware
plugin, configured how, and when the work is finished: `composer gate`, 100 % coverage on
PHP and on both JavaScript sides, a mutation baseline with every survivor documented,
architecture rules through phpat, a Playwright suite — and the rule that **a test run
leaves the shop as it found it**. Where a required file does not exist yet, it is created.
The other three skills explain how to write a given test; this one settles what has to be
there.

**PHP/PHPUnit:** setup and kernel bootstrap (`IntegrationTestBehaviour`), **unit tests** (pure logic, mocked) vs.
**integration tests** (real DAL/DB with transaction rollback), **Store API** and **Admin API tests**, **fixtures**
and **builders** (with `IdsCollection`) as well as **static mocks** (`StaticEntityRepository`, `StaticSystemConfigService`).
**JavaScript:** **Jest** for the administration (including `fail-on-console`) and Vue component tests (`@vue/test-utils`,
`Shopware.Component.build`) as well as Jest for **storefront** JS plugins. **E2E:** **Playwright** (Acceptance Test Suite)
for critical end-to-end flows.

Entry point: **`shopware-test-lead`** — it settles what has to exist and routes. Specialist:
**`shopware-tester`**, which writes the individual tests. The scaffolder **`/sw-test`** generates the
appropriate test per class/level. **When to use:** when setting up or extending a plugin's test
suite, when writing or repairing tests, when asking whether a plugin is finished (for example,
delegated by `shopware-dev`). Conventions and static analysis beyond the gate are covered by
`shopware-quality`.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official sources and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-testing@claude-a-dev-team
```

## Skills (4)

Read `sw-testing-standard` first; the other three explain how to write what it requires.

| Skill | Description |
|---|---|
| **`sw-testing-standard`** | **The binding standard every Shopware plugin is built to** — which tools, which configuration, which thresholds, the clean-up rule. Read this before the others |
| `sw-e2e` | Shopware end-to-end testing with Playwright: setup, fixtures and the shop-specific helpers. Use when writing a Playwright end-to-end test against a Shopware shop |
| `sw-javascript` | Shopware JavaScript testing: Jest for the administration and the storefront, Vue component tests. Use when writing a Jest or Vue test for Shopware |
| `sw-phpunit` | Shopware PHPUnit: setup, unit and integration tests, Store API and Admin API tests, fixtures and builders, repository and config mocks. Use when writing a PHPUnit test for a Shopware plugin |

## Agents (2)

| Agent | Description |
|---|---|
| **`shopware-test-lead`** | **Orchestrator and entry point.** Decides what must exist against the standard, audits a plugin against it, routes to the right skill or specialist. Start here when the task is not clearly one single level |
| `shopware-tester` | Test specialist for Shopware 6 plugins across every level: PHPUnit (unit/integration/Store API/Admin API), test data (fixtures/builders), mocks (StaticEntityRepository/StaticSystemConfigService), Jest (admin/Vue, storefront), Playwright E2E |

## Commands (1)

| Command | Description |
|---|---|
| `/sw-test` | Scaffolds a suitable test for a Shopware 6 class (unit/integration/Store API/Admin API, respectively) |
