---
name: panther-testing
description: Symfony Panther tests: PantherTestCase, client API, crawler, interactions, waitFor mechanics, screenshots. Use when writing a Symfony Panther browser test.
---

# Symfony Panther: writing tests

Panther drives a real browser through the familiar BrowserKit API. waitFor* is what makes a JavaScript-heavy page testable.

## Reference map

- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Symfony Panther ist eine Browser-Testing- und Web-Crawling-Bibliothek fur PHP.
- **[BROWSERKIT-CLIENTS.md](BROWSERKIT-CLIENTS.md)**: BrowserKit-Clients als schnelle Alternative zum WebDriver fuer Tests ohne JavaScript- Bedarf. [BROWSERKIT-CLIENTS-DETAIL](BROWSERKIT-CLIENTS-DETAIL.md).
- **[CLIENT.md](CLIENT.md)**: Alle waitFor-Methoden: `timeoutInSecond = 30`, `intervalInMillisecond = 250`. [CLIENT-DETAIL](CLIENT-DETAIL.md), [CLIENT-EXPECTED-CONDITIONS](CLIENT-EXPECTED-CONDITIONS.md), [CLIENT-WEBDRIVER-CHECKBOX](CLIENT-WEBDRIVER-CHECKBOX.md).
- **[CRAWLER.md](CRAWLER.md)** [CRAWLER-DETAIL](CRAWLER-DETAIL.md).
- **[INTERACTIONS.md](INTERACTIONS.md)** [INTERACTIONS-DETAIL](INTERACTIONS-DETAIL.md).
- **[JAVASCRIPT-SCREENSHOTS.md](JAVASCRIPT-SCREENSHOTS.md)**: JavaScript ausfuehren, Browser-Logs auslesen, Screenshots erstellen und Real-Time- Applikationen mit mehreren…. [JAVASCRIPT-SCREENSHOTS-DETAIL](JAVASCRIPT-SCREENSHOTS-DETAIL.md).
- **[OVERVIEW.md](OVERVIEW.md)**: Panther ist eine Browser-Testing- und Web-Crawling-Bibliothek fur PHP, die echte Browser uber das W3C-WebDriv….
- **[TESTCASE.md](TESTCASE.md)**: Direkte: `assertPageTitleSame`, `assertPageTitleContains`, `assertSelectorExists`, `assertSelectorNotExists`,…. [TESTCASE-DETAIL](TESTCASE-DETAIL.md).

## Source

Distilled from the [symfony/panther](https://github.com/symfony/panther) documentation and package source, retrieved 2026-08-20.
