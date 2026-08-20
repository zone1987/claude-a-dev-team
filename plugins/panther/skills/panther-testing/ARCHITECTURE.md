# Symfony Panther — Architecture & Decision Tree

## Contents

- [What is Panther?](#what-is-panther)
- [Architecture diagram (simplified)](#architecture-diagram-simplified)
- [Client comparison (complete)](#client-comparison-complete)
- [Decision tree: which client to use?](#decision-tree-which-client-to-use)
- [Typical use cases](#typical-use-cases)
- [Differentiation from other tools](#differentiation-from-other-tools)
- [Dependency graph (Composer)](#dependency-graph-composer)
- [PantherCrawler vs. DomCrawler](#panthercrawler-vs-domcrawler)
- [Versioning](#versioning)

## What is Panther?

Symfony Panther is a browser-testing and web-crawling library for PHP. It drives
real browsers (Chrome, Firefox) via the W3C WebDriver protocol (through `php-webdriver/webdriver`)
and can alternatively work purely HTTP-based without a browser via `BrowserKit/HttpBrowser`.
Panther implements `Symfony\Component\BrowserKit\AbstractBrowser` and always returns a
`Symfony\Component\DomCrawler\Crawler` (or `PantherCrawler`), so tests can switch seamlessly
between the client types.

## Architecture diagram (simplified)

```
PantherTestCase / PantherTestCaseTrait
        |
        |-- createPantherClient()      --> WebDriver client (Chrome/Firefox/Selenium)
        |       \--> php-webdriver/webdriver --> ChromeDriver/GeckoDriver --> Browser
        |
        |-- createHttpBrowserClient()  --> BrowserKit/HttpBrowser (cURL)
        |       \--> symfony/http-client --> HTTP stack (no browser)
        |
        \-- createClient()             --> Symfony KernelBrowser (Symfony apps only)
                \--> Symfony Kernel (in-process)
```

## Client comparison (complete)

| Criterion               | PantherClient (WebDriver) | HttpBrowserClient     | KernelBrowserClient      |
|-------------------------|---------------------------|-----------------------|--------------------------|
| Base technology         | W3C WebDriver             | BrowserKit + cURL     | Symfony Kernel           |
| JavaScript support      | Yes                       | No                    | No                       |
| Real browser            | Yes (Chrome / Firefox)    | No                    | No                       |
| Speed                   | Slow                      | Medium                | Very fast                |
| Screenshots             | Yes (`takeScreenshot`)    | No                    | No                       |
| waitFor methods         | Yes                       | No                    | No                       |
| PHP kernel access       | No                        | No                    | Yes                      |
| Symfony requirement     | No (any PHP app)          | No (any PHP app)      | Yes                      |
| Cookies                 | Yes (WebDriver CookieJar) | Yes (BrowserKit)      | Yes (BrowserKit)         |
| HTTP redirects          | Yes (automatic)           | Yes (configurable)    | Yes (configurable)       |
| Bypass SSL problems     | Yes (via Capabilities)    | Yes (via HttpClient)  | N/A                      |
| Multi-browser instances | Yes                       | No                    | No                       |
| Headless mode           | Yes (default)             | N/A                   | N/A                      |

## Decision tree: which client to use?

```
Do I need JavaScript rendering or real browser interactions?
  YES --> PantherClient (createPantherClient)
  NO
    |
    Is it a Symfony app and do I need kernel/service access?
      YES --> KernelBrowserClient (createClient)
      NO   --> HttpBrowserClient (createHttpBrowserClient)
```

## Typical use cases

### PantherClient (WebDriver)
- Single-page applications (SPA) with Vue/React/Svelte
- Forms with JavaScript validation
- Infinite scroll, dynamic loading
- WebSocket / SSE / real-time tests
- Drag & drop, hover effects
- Screenshot comparisons
- Tests that require multiple browser instances (chat tests)

### HttpBrowserClient
- REST API endpoints (JSON responses)
- Server-side-rendered pages without JS
- Performance tests (many requests)
- Web crawling / scraping

### KernelBrowserClient
- Near-unit functional tests (fast)
- Tests with database reset
- Tests that mock services, repositories etc. directly

## Differentiation from other tools

| Tool               | Relationship to Panther                                            |
|--------------------|--------------------------------------------------------------------|
| **Goutte**         | Obsolete. Its successor is `HttpBrowserClient` via `BrowserKit`.   |
| **WebTestCase**    | Symfony-internal, only `KernelBrowser`, no JS. Panther extends it. |
| **Playwright**     | Node.js-based, no PHP. For PHP apps: prefer Panther.               |
| **Selenium IDE**   | Graphical tool, Panther uses the Selenium Grid protocol.          |
| **Cypress**        | JavaScript-only, no PHP. For PHP apps: prefer Panther.             |
| **Behat/Mink**     | BDD framework, can use Panther as a driver.                       |

## Dependency graph (Composer)

```
symfony/panther
  ├── php-webdriver/webdriver        # W3C WebDriver protocol
  ├── symfony/browser-kit            # AbstractBrowser, CookieJar, History
  ├── symfony/dom-crawler            # Crawler, Form, FormFields
  ├── symfony/http-client            # for HttpBrowserClient
  ├── symfony/process                # start the PHP built-in server
  └── dbrekelmans/bdi (optional)     # automatic driver installation
```

## PantherCrawler vs. DomCrawler

`PantherCrawler` is an extension of `DomCrawler\Crawler` with WebDriver-specific
methods:
- `getElement()` returns a `WebDriverElement` (not a `\DOMElement`)
- No XML support (HTML only)
- `text()` returns visible text (like `innerText` in the browser)
- `html()` returns the current (possibly JS-modified) HTML

## Versioning

Panther follows the Symfony release cycle. From v2.0 on, PHP 8.1+ is the minimum.
Current stable: v2.4.x (as of 2026-01).

---

Sources:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther
- https://symfony.com/doc/current/components/browser_kit.html
