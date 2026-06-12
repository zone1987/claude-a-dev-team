# shopware-testing

> Testen über alle Ebenen (PHPUnit, Jest, Playwright).

`shopware-testing` deckt das **Testen über alle Ebenen der Test-Pyramide** ab.

**PHP/PHPUnit:** Setup & Kernel-Bootstrap (`IntegrationTestBehaviour`), **Unit-Tests** (reine Logik, gemockt) vs.
**Integrationstests** (echte DAL/DB mit Transaktions-Rollback), **Store-API-** und **Admin-API-Tests**, **Fixtures**
und **Builder** (mit `IdsCollection`) sowie **Static-Mocks** (`StaticEntityRepository`, `StaticSystemConfigService`).
**JavaScript:** **Jest** für die Administration (inkl. `fail-on-console`) und Vue-Komponententests (`@vue/test-utils`,
`Shopware.Component.build`) sowie Jest für **Storefront**-JS-Plugins. **E2E:** **Playwright** (Acceptance Test Suite)
für kritische End-to-End-Flows.

Spezialist: **`shopware-tester`**; Scaffolder **`/sw-test`** erzeugt den passenden Test je Klasse/Ebene. **Wann
nutzen:** beim Schreiben/Reparieren von Tests oder zum Absichern nach Code-Änderungen (z. B. delegiert von
`shopware-dev`). Konventionen/Static-Analysis ergänzt `shopware-quality`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-testing@claude-a-dev-team
```

## Skills (14)

`shopware-phpunit`, `sw-admin-api-test`, `sw-integration-test`, `sw-jest-admin`, `sw-jest-storefront`, `sw-mock-repository`, `sw-mock-system-config`, `sw-phpunit-setup`, `sw-playwright-e2e`, `sw-store-api-test`, `sw-test-builder`, `sw-test-fixtures`, `sw-unit-test`, `sw-vue-test`

## Agents (1)

- **`shopware-tester`** — Test-Spezialist für Shopware-6-Plugins über alle Ebenen: PHPUnit (Unit/Integration/Store-API/Admin-API), Test-Daten (Fixtures/Builder), Mocks (StaticEntityRepository/StaticSystemConfigService), Jest (Admin/Vue, Storefron

## Commands (1)

- **`/sw-test`** — Scaffold eines passenden Tests für eine Shopware-6-Klasse (Unit/Integration/Store-API/Admin-API bzw.
