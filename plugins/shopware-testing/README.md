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

| Skill | Beschreibung |
|---|---|
| `shopware-phpunit` | Best practices for writing PHPUnit tests in Shopware 6 projects, including integration tests, unit tests, and common testing patterns for plugins and apps |
| `sw-admin-api-test` | Admin-API-Tests in Shopware 6: AdminApiTestBehaviour, getBrowser (authentifizierter Admin-Client), Requests gegen /api, ACL-Fälle |
| `sw-integration-test` | Integrationstests in Shopware 6: IntegrationTestBehaviour, echte DAL-Repositories, Container-Services, DB-Transaktion je Test, Daten anlegen/prüfen |
| `sw-jest-admin` | Jest-Tests für die Shopware-6-Administration: Test-Setup (composer admin:unit), Komponenten/Services testen, fail-on-console, JS-only Testfiles |
| `sw-jest-storefront` | Jest-Tests für Storefront-JS-Plugins in Shopware 6: Test-Setup (composer storefront:unit), PluginManager/DOM mocken, Plugin-Methoden testen |
| `sw-mock-repository` | EntityRepository in Shopware-6-Unit-Tests mocken: StaticEntityRepository (ADR mocking-repositories), Such-Ergebnisse ohne DB simulieren |
| `sw-mock-system-config` | SystemConfigService in Shopware-6-Unit-Tests mocken: StaticSystemConfigService, Plugin-Config-Werte ohne DB setzen |
| `sw-phpunit-setup` | PHPUnit-Setup für Shopware-6-Plugins: phpunit.xml.dist, Kernel-Bootstrap (TestBootstrapper), IntegrationTestBehaviour, Test-Datenbank, Tests ausführen |
| `sw-playwright-e2e` | End-to-End-Tests für Shopware 6 mit Playwright (Acceptance Test Suite): Setup, Page-Objects/Fixtures, Storefront- & Admin-Flows, gegen laufende Instanz |
| `sw-store-api-test` | Store-API-Tests in Shopware 6: SalesChannelApiTestBehaviour, getSalesChannelBrowser, Requests gegen /store-api, Response prüfen |
| `sw-test-builder` | Test-Daten-Builder in Shopware 6: ProductBuilder & eigene Builder (fluent API) für komplexe Entity-Payloads in Tests |
| `sw-test-fixtures` | Testdaten in Shopware 6: Fixtures/Helper zum Anlegen von Entities (Produkt, Kunde, SalesChannel) für Tests, IdsCollection, wiederverwendbare Daten |
| `sw-unit-test` | Unit-Tests in Shopware 6: reine Logik ohne Kernel/DB, Abhängigkeiten mocken, schnelle Tests, assertSame |
| `sw-vue-test` | Vue-3-Komponententests im Shopware-6-Admin: @vue/test-utils mount/shallowMount, Shopware.Component.build, Props/Events, Pinia-Store mocken |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-tester` | Test-Spezialist für Shopware-6-Plugins über alle Ebenen: PHPUnit (Unit/Integration/Store-API/Admin-API), Test-Daten (Fixtures/Builder), Mocks (StaticEntityRepository/StaticSystemConfigService), Jest (Admin/Vue, Storefront), Playwright-E2E |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/sw-test` | Scaffold eines passenden Tests für eine Shopware-6-Klasse (Unit/Integration/Store-API/Admin-API bzw |
