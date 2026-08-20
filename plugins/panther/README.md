# panther

Comprehensive library for **[Symfony Panther](https://symfony.com/doc/current/testing/end_to_end.html)** — the PHP library for **end-to-end and browser testing** (and web scraping). Panther drives **real browsers** (Chrome/Firefox) over the WebDriver protocol and at the same time offers a **headless HTTP client** via BrowserKit/`HttpBrowser` — with the same API as Symfony's `WebTestCase`/DomCrawler.

This library documents **every public method, every argument, every `PANTHER_*` environment variable and every option** — distilled from the Symfony documentation **and verified against the real source code of the `symfony/panther` package** (`Client`, `Crawler`, form/field classes, `WebDriverMouse`/`WebDriverCheckbox`, `PantherWebDriverExpectedCondition`, `PantherTestCase`/trait, `WebTestAssertionsTrait`, the ProcessManager). That makes even the fine points correct — for example the exact `waitFor*` default timeouts and the fact that Panther's crawler does **not** implement `evaluate()`/`parents()`/`innerText()`. Each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it. Examples in PHP.

Part of the marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install panther@claude-a-dev-team
```

## Usage

- **Skills** load automatically in matching context (for example "PantherTestCase", "createPantherClient", "waitForVisibility", "Panther Selenium", "PANTHER_ env").
- **Agents:** `panther-expert` (tests/client/crawler/interaction/JS) and `panther-ops` (installation/drivers/env/Selenium/Docker/CI).
- **Commands:** `/panther-init` (setup) and `/panther-test` (test from a description).
- **Hook** reminds you, in Panther test and `phpunit.xml` files, about `waitFor*` instead of `sleep()`, unimplemented crawler methods, `getElement(int)`, extension registration and credential hygiene.
- **Utils** (`utils/`): ready-to-use templates — see below.

## Agents

| Agent | Description |
|---|---|
| `panther-expert` | E2E/browser test specialist: PantherTestCase, client API (request/click/submitForm, `waitFor*`, executeScript, screenshots), crawler/form, mouse/keyboard, assertions, choosing the client. |
| `panther-ops` | Configuration/operations specialist: web driver installation, PHPUnit extension, all `PANTHER_*` env vars, Selenium/proxy/SSL, Docker and CI, troubleshooting. |

## Commands

| Command | Description |
|---|---|
| `/panther-init` | Setup scaffold: `composer require`, web driver (bdi), PHPUnit extension in `phpunit.xml.dist`, `PANTHER_*` env vars, a base `PantherTestCase` and a first test. |
| `/panther-test` | Test scaffold from a description: the matching client (WebDriver/KernelBrowser/HttpBrowser), navigation, form interaction, correct `waitFor*` calls, Panther/web assertions, optional POM. |

## Hooks

| Hook | Description |
|---|---|
| `panther-reminder.py` (PostToolUse) | Fires in Panther test and `phpunit.xml` files: warns about `sleep()` (→ `waitFor*`), unimplemented crawler methods (`evaluate`/`parents`/`innerText`), `getElement()` without an index, a missing extension registration and plaintext credentials. |

## Utils

Ready-to-use templates under `utils/` (copy and adapt — no real credentials):

| File | Purpose |
|---|---|
| `phpunit.panther.xml` | PHPUnit 10/11 config with a registered `ServerExtension` plus sensible `PANTHER_*` env vars. |
| `AbstractPantherTestCase.php` | Base test case with helpers (`visit`, `waitVisible`, `screenshot`) — signatures verified against the source. |
| `Dockerfile.panther` | PHP + Chrome + ChromeDriver for headless tests (no-sandbox, `--disable-dev-shm-usage`). |
| `docker-compose.selenium.yml` | Selenium Grid (standalone Chrome) for remote WebDriver tests. |
| `github-actions-panther.yml` | GitHub Actions workflow: drivers, AssetMapper build, headless tests, screenshot upload on failure. |

## Skills (2)

| Skill | Description |
|---|---|
| `panther-testing` | Writing Panther tests: what Panther is and its architecture (a real browser via WebDriver plus headless HTTP via BrowserKit), choosing a client and the distinction from WebTestCase/Goutte; `PantherTestCase`/`PantherTestCaseTrait` (factory methods with all options, WebTestCase integration, all 22 `assert*` assertions — immediate and waitFor); the complete client API (request/click/submitForm, all `waitFor*` variants with timeout/interval, executeScript, takeScreenshot, getWebDriver/getMouse/getCookieJar and more); the complete crawler API (filter/filterXPath, selectButton/Link/Image, form/`getElement(int)`, attr/text/html, each/eq/first/last, links/images — including the unimplemented methods); interactions (click/submitForm, the form object and all FormField types, the mouse API clickTo/doubleClickTo/contextClickTo, keyboard sendKeys, drag & drop, file upload); JavaScript (executeScript/executeAsyncScript), console logs, screenshots and error screenshots, real-time apps (Mercure/WebSocket, multiple clients); and the BrowserKit clients as a WebDriver alternative (`HttpBrowser` for HTTP only as a Goutte replacement, KernelBrowser via `createClient`, the performance trade-off). |
| `panther-setup` | Panther setup and operation: installation (`composer require`, web driver via bdi/ChromeDriver/GeckoDriver, PHPUnit extension, requirements, Docker, CI env vars); all `PANTHER_*` environment variables with name/type/default/effect — headless, sandbox, web-server-dir/port, external-base-uri, chrome/firefox-arguments, devtools, error-screenshot, window-size; Selenium Grid and remote WebDriver (`createSeleniumClient`), proxy, self-signed SSL, an external web server, multi-domain, ChromeDriver arguments, timeouts, DesiredCapabilities; Docker (Chrome/Firefox image, no-sandbox), interactive mode, complete CI YAML files (GitHub Actions/Travis/GitLab/AppVeyor), known limitations and troubleshooting. |

## License & author

proprietary — Andreas Gerhardt, A-Dev-Team. Sources: the official Symfony documentation and the source code of `symfony/panther`.
