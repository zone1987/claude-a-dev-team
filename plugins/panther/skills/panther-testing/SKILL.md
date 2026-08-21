---
name: panther-testing
description: Symfony Panther tests: PantherTestCase, client API, crawler, interactions, waitFor mechanics, screenshots. Use when writing a Symfony Panther browser test.
---

# Symfony Panther: writing tests

Panther drives a real browser through the familiar BrowserKit API. waitFor* is what makes a JavaScript-heavy page testable.

## Reference map

- **[ARCHITECTURE.md](references/ARCHITECTURE.md)**: Symfony Panther is a browser-testing and web-crawling library for PHP.
- **[BROWSERKIT-CLIENTS.md](references/BROWSERKIT-CLIENTS.md)**: BrowserKit clients as a fast alternative to the WebDriver for tests that do not need JavaScript. [BROWSERKIT-CLIENTS-DETAIL](references/BROWSERKIT-CLIENTS-DETAIL.md).
- **[CLIENT.md](references/CLIENT.md)**: All waitFor methods: `timeoutInSecond = 30`, `intervalInMillisecond = 250`. [CLIENT-DETAIL](references/CLIENT-DETAIL.md), [CLIENT-EXPECTED-CONDITIONS](references/CLIENT-EXPECTED-CONDITIONS.md), [CLIENT-WEBDRIVER-CHECKBOX](references/CLIENT-WEBDRIVER-CHECKBOX.md).
- **[CRAWLER.md](references/CRAWLER.md)** [CRAWLER-DETAIL](references/CRAWLER-DETAIL.md).
- **[INTERACTIONS.md](references/INTERACTIONS.md)** [INTERACTIONS-DETAIL](references/INTERACTIONS-DETAIL.md).
- **[JAVASCRIPT-SCREENSHOTS.md](references/JAVASCRIPT-SCREENSHOTS.md)**: Execute JavaScript, read browser logs, create screenshots and test real-time applications with multiple…. [JAVASCRIPT-SCREENSHOTS-DETAIL](references/JAVASCRIPT-SCREENSHOTS-DETAIL.md).
- **[OVERVIEW.md](references/OVERVIEW.md)**: Panther is a browser-testing and web-crawling library for PHP that drives real browsers via the W3C WebDriv….
- **[TESTCASE.md](references/TESTCASE.md)**: Direct: `assertPageTitleSame`, `assertPageTitleContains`, `assertSelectorExists`, `assertSelectorNotExists`,…. [TESTCASE-DETAIL](references/TESTCASE-DETAIL.md).

## Source

Distilled from the [symfony/panther](https://github.com/symfony/panther) documentation and package source, retrieved 2026-08-20.
