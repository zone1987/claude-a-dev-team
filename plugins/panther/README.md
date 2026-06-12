# panther

Vollumfängliche Bibliothek für **[Symfony Panther](https://symfony.com/doc/current/testing/end_to_end.html)** — die PHP-Library für **End-to-End- & Browser-Testing** (und Web-Scraping). Panther steuert **echte Browser** (Chrome/Firefox) über das WebDriver-Protokoll und bietet zugleich einen **headless HTTP-Client** via BrowserKit/`HttpBrowser` — mit derselben API wie Symfonys `WebTestCase`/DomCrawler.

Diese Bibliothek dokumentiert **jede öffentliche Methode, jedes Argument, jede `PANTHER_*`-Umgebungsvariable und jede Option** — destilliert aus der Symfony-Doku **und gegen den echten Quellcode des Pakets `symfony/panther` verifiziert** (`Client`, `Crawler`, Form/Field-Klassen, `WebDriverMouse`/`WebDriverCheckbox`, `PantherWebDriverExpectedCondition`, `PantherTestCase`/Trait, `WebTestAssertionsTrait`, die ProcessManager). Dadurch sind auch die Feinheiten korrekt — z. B. die exakten `waitFor*`-Default-Timeouts und dass Panthers Crawler `evaluate()`/`parents()`/`innerText()` **nicht** implementiert. Schlanke `SKILL.md`, Tiefe in `references/deep/`. Beispiele in PHP.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install panther@claude-a-dev-team
```

## Nutzung

- **Skills** laden automatisch bei passendem Kontext (z.B. „PantherTestCase", „createPantherClient", „waitForVisibility", „Panther Selenium", „PANTHER_ env").
- **Agents:** `panther-expert` (Tests/Client/Crawler/Interaktion/JS) und `panther-ops` (Installation/Treiber/Env/Selenium/Docker/CI).
- **Commands:** `/panther-init` (Setup) und `/panther-test` (Test aus Beschreibung).
- **Hook** erinnert in Panther-Test-/`phpunit.xml`-Dateien an `waitFor*` statt `sleep()`, nicht-implementierte Crawler-Methoden, `getElement(int)`, Extension-Registrierung und Credential-Hygiene.
- **Utils** (`utils/`): einsatzfertige Vorlagen — siehe unten.

## Agents

| Agent | Beschreibung |
|---|---|
| `panther-expert` | E2E-/Browser-Test-Spezialist: PantherTestCase, Client-API (request/click/submitForm, `waitFor*`, executeScript, Screenshots), Crawler/Form, Mouse/Keyboard, Assertions, Client-Wahl. |
| `panther-ops` | Konfigurations-/Betriebs-Spezialist: Web-Driver-Installation, PHPUnit-Extension, alle `PANTHER_*`-Env-Vars, Selenium/Proxy/SSL, Docker & CI, Troubleshooting. |

## Commands

| Command | Beschreibung |
|---|---|
| `/panther-init` | Setup-Scaffold: `composer require`, Web-Driver (bdi), PHPUnit-Extension in `phpunit.xml.dist`, `PANTHER_*`-Env-Vars, Basis-`PantherTestCase` + erster Test. |
| `/panther-test` | Test-Scaffold aus Beschreibung: passender Client (WebDriver/KernelBrowser/HttpBrowser), Navigation, Formular-Interaktion, korrekte `waitFor*`-Aufrufe, Panther-/Web-Assertions, optional POM. |

## Hooks

| Hook | Beschreibung |
|---|---|
| `panther-reminder.py` (PostToolUse) | Feuert in Panther-Test-/`phpunit.xml`-Dateien: warnt vor `sleep()` (→ `waitFor*`), nicht-implementierten Crawler-Methoden (`evaluate`/`parents`/`innerText`), `getElement()` ohne Index, fehlender Extension-Registrierung und Klartext-Credentials. |

## Utils

Einsatzfertige Vorlagen unter `utils/` (kopieren & anpassen — keine echten Credentials):

| Datei | Zweck |
|---|---|
| `phpunit.panther.xml` | PHPUnit-10/11-Config mit registrierter `ServerExtension` + sinnvollen `PANTHER_*`-Env-Vars. |
| `AbstractPantherTestCase.php` | Basis-TestCase mit Helfern (`visit`, `waitVisible`, `screenshot`) — quellverifizierte Signaturen. |
| `Dockerfile.panther` | PHP + Chrome + ChromeDriver für headless Tests (no-sandbox, `--disable-dev-shm-usage`). |
| `docker-compose.selenium.yml` | Selenium-Grid (Standalone Chrome) für Remote-WebDriver-Tests. |
| `github-actions-panther.yml` | GitHub-Actions-Workflow: Treiber, AssetMapper-Build, headless Tests, Screenshot-Upload bei Fehler. |

## Skills

| Skill | Beschreibung |
|---|---|
| `panther-overview` | Was ist Panther, Architektur (echter Browser via WebDriver + headless HTTP via BrowserKit), Client-Wahl, Abgrenzung zu WebTestCase/Goutte. |
| `panther-installation` | Installation: `composer require`, Web-Driver (bdi/ChromeDriver/GeckoDriver), PHPUnit-Extension, Anforderungen, Docker, CI-Env-Vars. |
| `panther-testcase` | `PantherTestCase`/`PantherTestCaseTrait`: Factory-Methoden mit allen Optionen, WebTestCase-Integration, alle 22 `assert*`-Assertions (sofort + waitFor). |
| `panther-client` | Komplette Client-API: request/click/submitForm, alle `waitFor*`-Varianten (mit Timeout/Interval), executeScript, takeScreenshot, getWebDriver/getMouse/getCookieJar u.v.m. |
| `panther-crawler` | Komplette Crawler-API: filter/filterXPath, selectButton/Link/Image, form/`getElement(int)`, attr/text/html, each/eq/first/last, links/images — inkl. nicht-implementierter Methoden. |
| `panther-interactions` | Interaktionen: click/submitForm, Form-Objekt & alle FormField-Typen, Mouse-API (clickTo/doubleClickTo/contextClickTo), Keyboard (sendKeys), Drag&Drop, File-Upload. |
| `panther-javascript-screenshots` | JavaScript (executeScript/executeAsyncScript), Console-Logs, Screenshots/Fehler-Screenshots, Real-Time-Apps (Mercure/WebSocket, mehrere Clients). |
| `panther-config-env` | Alle `PANTHER_*`-Umgebungsvariablen: Name/Typ/Default/Wirkung — headless, sandbox, web-server-dir/port, external-base-uri, chrome/firefox-arguments, devtools, error-screenshot, window-size. |
| `panther-browserkit-clients` | BrowserKit-Clients als WebDriver-Alternative: `HttpBrowser` (HTTP-only, Goutte-Ersatz), KernelBrowser (`createClient`), Performance-Abwägung. |
| `panther-selenium-remote` | Selenium-Grid & Remote-WebDriver (`createSeleniumClient`), Proxy, Self-Signed-SSL, externer Webserver, Multi-Domain, ChromeDriver-Argumente, Timeouts, DesiredCapabilities. |
| `panther-docker-ci` | Docker (Chrome/Firefox-Image, no-sandbox), Interactive Mode, vollständige CI-YAMLs (GitHub Actions/Travis/GitLab/AppVeyor), Known Limitations & Troubleshooting. |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quellen: offizielle Symfony-Doku & der Quellcode von `symfony/panther`.
