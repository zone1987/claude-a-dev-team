---
name: playwright-runner
description: Playwright test runner: playwright.config, projects, fixtures, parallelism and sharding, retries, reporters, component testing, page object model, CI. Use when configuring a Playwright suite.
---

# Playwright: test runner

How a suite is structured and executed, rather than what a single test does.

## Reference map

- **[API-TEST.md](API-TEST.md)**: Erschoepfende API-Referenz aller Playwright Test Runner-Klassen mit vollstaendigen Signaturen, allen Paramete…. [API-TEST-CLASS-FIXTURES](API-TEST-CLASS-FIXTURES.md), [API-TEST-CLASS-FULLCONFIG](API-TEST-CLASS-FULLCONFIG.md), [API-TEST-CLASS-FULLPROJECT](API-TEST-CLASS-FULLPROJECT.md), [API-TEST-CLASS-REPORTER](API-TEST-CLASS-REPORTER.md), [API-TEST-CLASS-SUITE](API-TEST-CLASS-SUITE.md), [API-TEST-CLASS-TEST](API-TEST-CLASS-TEST.md), [API-TEST-CLASS-TESTCASE](API-TEST-CLASS-TESTCASE.md), [API-TEST-CLASS-TESTCONFIG](API-TEST-CLASS-TESTCONFIG.md), [API-TEST-CLASS-TESTERROR](API-TEST-CLASS-TESTERROR.md), [API-TEST-CLASS-TESTINFO](API-TEST-CLASS-TESTINFO.md), [API-TEST-CLASS-TESTINFOERROR](API-TEST-CLASS-TESTINFOERROR.md), [API-TEST-CLASS-TESTOPTIONS](API-TEST-CLASS-TESTOPTIONS.md), [API-TEST-CLASS-TESTPROJECT](API-TEST-CLASS-TESTPROJECT.md), [API-TEST-CLASS-TESTRESULT](API-TEST-CLASS-TESTRESULT.md), [API-TEST-CLASS-TESTSTEP](API-TEST-CLASS-TESTSTEP.md), [API-TEST-CLASS-TESTSTEPINFO](API-TEST-CLASS-TESTSTEPINFO.md), [API-TEST-CLASS-TIMEOUTERROR](API-TEST-CLASS-TIMEOUTERROR.md).
- **[CI.md](CI.md)**: Playwright in CI/CD: GitHub Actions/GitLab/Jenkins/Azure/CircleCI/Docker, Browser-Caching, Sharding, Artefakt…. [CI-DETAIL](CI-DETAIL.md).
- **[POM.md](POM.md)**: Page Object Model-Muster mit Playwright: Klassen-Struktur, Locator-Eigenschaften, zusammengesetzte Methoden. [POM-BEST-PRACTICES](POM-BEST-PRACTICES.md).
- **[TEST-COMPONENTS.md](TEST-COMPONENTS.md)**: Experimentelles Component Testing fuer React/Vue/Svelte: Setup, `mount`-API mit Props, Slots, Events, `update…. [TEST-COMPONENTS-COMPONENTS](TEST-COMPONENTS-COMPONENTS.md).
- **[TEST-CONFIG.md](TEST-CONFIG.md)**: Konfigurationsdatei `playwright.config.ts` mit `defineConfig`. [TEST-CONFIG-CONFIG](TEST-CONFIG-CONFIG.md).
- **[TEST-EXECUTION.md](TEST-EXECUTION.md)**: Alle CLI-Optionen, Parallelitaet, Sharding, Retries und Timeout-Typen. [TEST-EXECUTION-EXECUTION](TEST-EXECUTION-EXECUTION.md).
- **[TEST-FIXTURES.md](TEST-FIXTURES.md)**: Playwright-Fixtures: eingebaute Fixtures, `test.extend` fuer eigene Test-/Worker-Fixtures, auto/option-Fixtur…. [TEST-FIXTURES-FIXTURES](TEST-FIXTURES-FIXTURES.md).
- **[TEST-REPORTERS.md](TEST-REPORTERS.md)**: Alle eingebauten Reporter mit Optionen, Custom-Reporter-API mit allen Callback-Methoden, Annotationen. [TEST-REPORTERS-REPORTERS](TEST-REPORTERS-REPORTERS.md).

## Source

Distilled from [playwright.dev](https://playwright.dev) — the guides, the test-runner reference and the full library API — retrieved 2026-08-20.
