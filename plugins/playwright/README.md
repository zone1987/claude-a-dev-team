# playwright

Vollumfängliche Bibliothek für **[Playwright](https://playwright.dev)** — das Framework für **End-to-End-Testing & Browser-Automation** (Chromium, Firefox, WebKit). Deckt beide Hälften ab: die **Library-API** (Browser/Context/Page/Locator/Network/…) und den **Test-Runner** `@playwright/test` (Config, Fixtures, Assertions, Reporter, Parallelität, Sharding) — plus **Trace Viewer**, **Codegen**, **CI/Docker**, **Emulation**, **Auth**, **Accessibility**, **Component-Testing**, **Migration** (Puppeteer/Protractor/Selenium) sowie **Playwright MCP** und die **Agent-CLI**.

Das Herzstück ist die **komplette API-Referenz aller ~70 Klassen** — jede Methode, Property und jedes Event mit voller Signatur, allen Parametern (Typ/Default/required), Rückgabewert und Beispiel. Destilliert aus der offiziellen Doku (playwright.dev, stabile Version) und in die Skills eingebettet. Schlanke `SKILL.md`, Tiefe in `references/deep/` (über 30.000 Zeilen Referenz). Beispiele in TypeScript.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install playwright@claude-a-dev-team
```

## Nutzung

- **Skills** laden automatisch bei passendem Kontext (z.B. „E2E-Test schreiben", „getByRole", „expect(locator)", „playwright.config", „trace viewer").
- **Agents:** `playwright-expert` (Tests/Library/API), `playwright-test-architect` (Config/Fixtures/Parallel/CI), `playwright-debugger` (Trace/Flaky/Debug).
- **Commands:** `/playwright-init` (Projekt), `/playwright-test` (Test), `/playwright-ci` (CI-Pipeline).
- **Hook** erinnert in Test-/Config-Dateien an Web-First-Assertions statt Sleeps, `await expect`, role-basierte Locators, `trace`-Option und Credential-Hygiene.

## MCP-Server (mitgeliefert)

Das Plugin bringt den offiziellen **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** über eine `.mcp.json` mit — nach `/plugin install playwright@claude-a-dev-team` steht der MCP-Server `playwright` (gestartet via `npx @playwright/mcp@latest`) automatisch zur Verfügung; Claude kann damit live im Browser navigieren, klicken, Formulare ausfüllen, Snapshots/Screenshots erstellen u.v.m. Voraussetzung: Node.js/`npx` im PATH.

```jsonc
// plugins/playwright/.mcp.json
{ "mcpServers": { "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] } } }
```

Anpassen (headed-Modus, Browser-Wahl, Capabilities, isolierte/persistente Profile, Transport, Vision-Mode usw.) — alle Flags sind im Skill **`playwright-mcp`** dokumentiert, die Tools in **`playwright-mcp-tools`**. Beispiel mit Optionen:

```jsonc
{ "mcpServers": { "playwright": { "command": "npx",
  "args": ["@playwright/mcp@latest", "--browser=chromium", "--headless", "--caps=core,network,pdf"] } } }
```

## Agents

| Agent | Beschreibung |
|---|---|
| `playwright-expert` | E2E-/Automatisierungs-Spezialist: Tests, Locators, Aktionen & Auto-Waiting, Web-First-Assertions, Netzwerk/Mock, API-Testing, Auth, Emulation, komplette Library-API. |
| `playwright-test-architect` | Suite-Architektur & Skalierung: `playwright.config.ts`, Projects/Dependencies, Fixtures, Parallelität/Sharding/Retries, Reporter, POM, CI/CD. |
| `playwright-debugger` | Debugging & Flaky-Tests: Trace Viewer, Playwright Inspector/PWDEBUG, UI-Mode, Codegen, Root-Cause statt Symptom, CI-Fehlschläge. |

## Commands

| Command | Beschreibung |
|---|---|
| `/playwright-init` | Projekt-Scaffold: Installation, `playwright.config.ts` (Browser-Matrix, reporter, use-Options, webServer, trace), erster Test, optional POM. |
| `/playwright-test` | Test-Scaffold aus Beschreibung: role-basierte Locators, Web-First-Assertions, Fixtures; UI-Flow, `--api` (APIRequestContext), `--auth-setup` (storageState), `--pom`. |
| `/playwright-ci` | CI-Pipeline-Scaffold: GitHub Actions/GitLab/Jenkins/Azure, `install --with-deps` bzw. Docker-Image, Caching, Sharding (Blob+merge), Artefakt-/HTML-Report-Upload. |

## Hooks

| Hook | Beschreibung |
|---|---|
| `playwright-reminder.py` (PostToolUse) | Feuert in `*.spec/*.test`- & `playwright.config`-Dateien: warnt vor `waitForTimeout`/fehlendem `await expect`/veralteten `$`-Selektoren, empfiehlt `trace: 'on-first-retry'`, warnt vor Klartext-Credentials. |

## Skills

### Einstieg & Library-Kern

| Skill | Beschreibung |
|---|---|
| `playwright-intro` | Einstieg: Installation, Library vs. `@playwright/test`, Browser/Context/Page-Lifecycle, unterstützte Sprachen. |
| `playwright-writing-tests` | Tests schreiben/ausführen: `test()`/`expect()`, Hooks, `describe`, Codegen-Recorder, VS-Code-Extension, CLI-Flags. |
| `playwright-browsers` | Browser-Management: Channels, `install`-Flags, isolierte Contexts (alle `newContext()`-Optionen), Popups/Tabs, Extensions, WebView2. |
| `playwright-locators` | Locators vollständig: `getByRole`/`getByText`/`getByLabel`/…, CSS/XPath, `filter`/`and`/`or`/`nth`, FrameLocator, Pseudoklassen. |
| `playwright-actions` | Interaktionen & Auto-Waiting: click/fill/press/check/selectOption/setInputFiles/dragTo/… mit allen Options, Actionability-Checks. |
| `playwright-evaluating` | JS im Browser: `evaluate`/`evaluateHandle`, JSHandle/ElementHandle, `addInitScript`, `exposeFunction`, Events/`waitForEvent`. |
| `playwright-io-events` | Downloads, Dialoge (alert/confirm/prompt/beforeunload), Navigation/Waiting (`waitForURL`/`waitForLoadState`), Touch/Gesten. |
| `playwright-emulation` | Emulation: Devices/Viewport, Geolocation/Locale/Timezone/Permissions/ColorScheme/Media, Clock-API, Screenshots. |

### Netzwerk, API, Auth, Accessibility

| Skill | Beschreibung |
|---|---|
| `playwright-network` | Interception: `route`/`fulfill`/`abort`/`continue`/`fetch`, Request/Response, HAR-Replay, WebSocket-Routing, API-/Browser-API-Mock, Service-Worker. |
| `playwright-api-testing` | API-Tests ohne Browser: `request`-Fixture, `APIRequestContext` (alle HTTP-Methoden + Optionen), Auth, `storageState`, UI+API kombiniert. |
| `playwright-auth` | Authentifizierung: `storageState` speichern/wiederverwenden, einmaliger Login im Setup-Projekt, mehrere Rollen, Worker-Isolation. |
| `playwright-accessibility` | A11y-Testing: `toMatchAriaSnapshot` (Format/Matching/Regex), axe-core-Integration, `AxeBuilder`, WCAG-Tags. |

### Test-Runner

| Skill | Beschreibung |
|---|---|
| `playwright-test-config` | `playwright.config.ts`: alle Top-Level- & `use`-Optionen, Projects/Dependencies, TypeScript-Setup. |
| `playwright-test-fixtures` | Fixtures: eingebaute + eigene (`test.extend`), test-/worker-Scope, auto/option, `mergeTests`, globalSetup/Teardown, Parametrisierung. |
| `playwright-test-assertions` | Alle `expect`-Matcher: Locator/Page/APIResponse/Generic/Snapshot, Soft, `expect.poll`/`toPass`/`extend`, asymmetrische Matcher. |
| `playwright-test-execution` | Ausführung: alle CLI-Flags, Parallelität (workers/fullyParallel/serial), Sharding, Retries, alle Timeout-Arten, UI-Mode, webServer. |
| `playwright-test-reporters` | Reporter list/line/dot/html/json/junit/blob/github + Custom-Reporter-API, Annotations (skip/fail/fixme/slow/Tags/step). |
| `playwright-test-components` | Component-Testing (experimentell) React/Vue/Svelte: `mount()`-API (Props/Slots/Events), Lifecycle-Hooks, Testing-Library-Migration. |
| `playwright-pom` | Page Object Model & Best Practices: Struktur, Isolation, nutzerfreundliche Locators, Web-First-Assertions, CI-Optimierung. |

### Tooling, CI & Migration

| Skill | Beschreibung |
|---|---|
| `playwright-trace-viewer` | Trace Viewer & Debugger: Traces aufnehmen/öffnen, UI-Inspector-Tabs, PWDEBUG, Playwright Inspector, VS-Code-Debug. |
| `playwright-ci` | CI/CD: GitHub Actions/GitLab/Jenkins/Azure/CircleCI YAML, Docker-Images, Browser-Caching, Sharding, Artefakt-Upload. |
| `playwright-migration` | Migration von Puppeteer & Protractor, Selenium-Grid-Anbindung — API-Mappings, Vorher/Nachher. |
| `playwright-misc` | Erweiterbarkeit & Sonstiges: Custom-Selector-Engines (`selectors.register`), Video-Aufnahme, Release-Kanäle/Canary. |

### Komplette API-Referenz (alle Klassen)

| Skill | Beschreibung |
|---|---|
| `playwright-api-page` | Page (~102 Methoden + 17 Events), Frame, ElementHandle, JSHandle — jede Methode mit voller Signatur. |
| `playwright-api-locator` | Locator (alle Methoden), FrameLocator, Selectors. |
| `playwright-api-assertions` | LocatorAssertions/PageAssertions/APIResponseAssertions/GenericAssertions/SnapshotAssertions/PlaywrightAssertions — alle Matcher. |
| `playwright-api-browser` | Browser, BrowserContext, BrowserType, BrowserServer, Playwright, CDPSession. |
| `playwright-api-network` | Request, Response, Route, WebSocket, WebSocketRoute, APIRequest, APIRequestContext, APIResponse. |
| `playwright-api-io` | Keyboard, Mouse, Touchscreen, Dialog, Download, FileChooser, ConsoleMessage, Clock, Coverage, Worker, WebError, Video, Tracing u.a. |
| `playwright-api-test` | Test (alle Modifier/Hooks/Steps/extend), TestConfig/TestProject/TestOptions, TestInfo, TestCase/TestResult, Reporter-API, FullConfig u.a. |
| `playwright-api-devices` | Experimentell: Android (ADB) und Electron — alle Klassen. |

### Playwright MCP & Agent-CLI

| Skill | Beschreibung |
|---|---|
| `playwright-mcp` | Playwright MCP-Server: Installation, Konfiguration (headed/headless, Transport), Capabilities, Profil-Modi, Clients, Vision-Mode. |
| `playwright-mcp-tools` | Alle 40+ MCP-Tools mit Parametern (Navigation, Interaktion, Forms, Screenshots, Tabs, Network, Storage, Testing, Tracing, Video, PDF). |
| `playwright-agent-cli` | Agent-CLI: Einführung, Installation, Konfiguration, Sessions, Snapshots, Vision-Mode, Capabilities, Skills. |
| `playwright-agent-cli-commands` | Agent-CLI-Befehlsreferenz: attach, interaction, keyboard-mouse, navigation, network-routing, dialogs, console-eval, storage, tabs, screenshots-pdf, video, tracing, test-debugging. |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quelle: offizielle Playwright-Dokumentation (https://playwright.dev).
