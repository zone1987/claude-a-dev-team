# playwright

Comprehensive library for **[Playwright](https://playwright.dev)** — the framework for **end-to-end testing and browser automation** (Chromium, Firefox, WebKit). It covers both halves: the **library API** (Browser/Context/Page/Locator/Network/…) and the test runner `@playwright/test` (config, fixtures, assertions, reporters, parallelism, sharding) — plus **Trace Viewer**, **Codegen**, **CI/Docker**, **emulation**, **auth**, **accessibility**, **component testing**, **migration** (Puppeteer/Protractor/Selenium) as well as **Playwright MCP** and the **agent CLI**.

At its core is the **complete API reference for all ~70 classes** — every method, property and event with its full signature, all parameters (type/default/required), return value and an example. Distilled from the official documentation (playwright.dev, stable version) and embedded in the skills. Each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it (over 30,000 lines of reference). Examples in TypeScript.

Part of the marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install playwright@claude-a-dev-team
```

## Usage

- **Skills** load automatically in matching context (for example "write an E2E test", "getByRole", "expect(locator)", "playwright.config", "trace viewer").
- **Agents:** `playwright-expert` (tests/library/API), `playwright-test-architect` (config/fixtures/parallel/CI), `playwright-debugger` (trace/flaky/debug).
- **Commands:** `/playwright-init` (project), `/playwright-test` (test), `/playwright-ci` (CI pipeline).
- **Hook** reminds you, in test and config files, about web-first assertions instead of sleeps, `await expect`, role-based locators, the `trace` option and credential hygiene.

## MCP server (included)

The plugin ships the official **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** via a `.mcp.json` — after `/plugin install playwright@claude-a-dev-team` the MCP server `playwright` (started via `npx @playwright/mcp@latest`) is available automatically; Claude can then navigate live in the browser, click, fill in forms, create snapshots/screenshots and much more. Requirement: Node.js/`npx` in the PATH.

```jsonc
// plugins/playwright/.mcp.json
{ "mcpServers": { "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] } } }
```

Customization (headed mode, browser choice, capabilities, isolated/persistent profiles, transport, vision mode and so on) — all flags are documented in the skill **`playwright-tooling`**, along with the tools. Example with options:

```jsonc
{ "mcpServers": { "playwright": { "command": "npx",
  "args": ["@playwright/mcp@latest", "--browser=chromium", "--headless", "--caps=core,network,pdf"] } } }
```

## Agents

| Agent | Description |
|---|---|
| `playwright-expert` | E2E/automation specialist: tests, locators, actions and auto-waiting, web-first assertions, network/mock, API testing, auth, emulation, the complete library API. |
| `playwright-test-architect` | Suite architecture and scaling: `playwright.config.ts`, projects/dependencies, fixtures, parallelism/sharding/retries, reporters, POM, CI/CD. |
| `playwright-debugger` | Debugging and flaky tests: Trace Viewer, Playwright Inspector/PWDEBUG, UI mode, Codegen, root cause instead of symptom, CI failures. |

## Commands

| Command | Description |
|---|---|
| `/playwright-init` | Project scaffold: installation, `playwright.config.ts` (browser matrix, reporter, use options, webServer, trace), a first test, optional POM. |
| `/playwright-test` | Test scaffold from a description: role-based locators, web-first assertions, fixtures; UI flow, `--api` (APIRequestContext), `--auth-setup` (storageState), `--pom`. |
| `/playwright-ci` | CI pipeline scaffold: GitHub Actions/GitLab/Jenkins/Azure, `install --with-deps` or a Docker image, caching, sharding (blob + merge), artifact and HTML report upload. |

## Hooks

| Hook | Description |
|---|---|
| `playwright-reminder.py` (PostToolUse) | Fires in `*.spec`/`*.test` and `playwright.config` files: warns about `waitForTimeout`, a missing `await expect` and outdated `$` selectors, recommends `trace: 'on-first-retry'`, warns about plaintext credentials. |

## Skills (5)

| Skill | Description |
|---|---|
| `playwright-writing` | Writing and fixing tests: getting started (installation, library vs. `@playwright/test`, the browser/context/page lifecycle, supported languages); writing and running tests (`test()`/`expect()`, hooks, `describe`, the Codegen recorder, the VS Code extension, CLI flags); locators in full (`getByRole`/`getByText`/`getByLabel`/…, CSS/XPath, `filter`/`and`/`or`/`nth`, FrameLocator, pseudo-classes); interactions and auto-waiting (click/fill/press/check/selectOption/setInputFiles/dragTo/… with all their options, actionability checks); JS in the browser (`evaluate`/`evaluateHandle`, JSHandle/ElementHandle, `addInitScript`, `exposeFunction`, events/`waitForEvent`); emulation (devices/viewport, geolocation/locale/timezone/permissions/colorScheme/media, the clock API, screenshots); authentication (saving and reusing `storageState`, a single login in the setup project, multiple roles, worker isolation); and a11y testing (`toMatchAriaSnapshot` with its format/matching/regex, axe-core integration, `AxeBuilder`, WCAG tags). |
| `playwright-library` | The library API outside the test runner: Page (~102 methods + 17 events), Frame, ElementHandle, JSHandle — every method with its full signature; Locator (all methods), FrameLocator, Selectors; Browser, BrowserContext, BrowserType, BrowserServer, Playwright, CDPSession; Request, Response, Route, WebSocket, WebSocketRoute, APIRequest, APIRequestContext, APIResponse; Keyboard, Mouse, Touchscreen, Dialog, Download, FileChooser, ConsoleMessage, Clock, Coverage, Worker, WebError, Video, Tracing and others; the experimental Android (ADB) and Electron classes; browser management (channels, `install` flags, isolated contexts with all `newContext()` options, popups/tabs, extensions, WebView2); network interception (`route`/`fulfill`/`abort`/`continue`/`fetch`, request/response, HAR replay, WebSocket routing, API and browser-API mocking, service workers); downloads, dialogs (alert/confirm/prompt/beforeunload), navigation and waiting (`waitForURL`/`waitForLoadState`), touch/gestures; API tests without a browser (the `request` fixture, `APIRequestContext` with all HTTP methods and options, auth, `storageState`, UI plus API combined); and extensibility (custom selector engines via `selectors.register`, video recording, release channels/canary). |
| `playwright-runner` | Configuring a suite: `playwright.config.ts` (all top-level and `use` options, projects/dependencies, TypeScript setup); fixtures (built-in and custom via `test.extend`, test and worker scope, auto/option, `mergeTests`, globalSetup/teardown, parameterization); all `expect` matchers (Locator/Page/APIResponse/Generic/Snapshot, soft assertions, `expect.poll`/`toPass`/`extend`, asymmetric matchers); execution (all CLI flags, parallelism via workers/fullyParallel/serial, sharding, retries, every kind of timeout, UI mode, webServer); reporters list/line/dot/html/json/junit/blob/github plus the custom reporter API, annotations (skip/fail/fixme/slow/tags/step); the Test API (all modifiers/hooks/steps/extend), TestConfig/TestProject/TestOptions, TestInfo, TestCase/TestResult, the reporter API, FullConfig and others; component testing (experimental) for React/Vue/Svelte with the `mount()` API (props/slots/events), lifecycle hooks, Testing Library migration; the Page Object Model and best practices (structure, isolation, user-facing locators, web-first assertions, CI optimization); and CI/CD (GitHub Actions/GitLab/Jenkins/Azure/CircleCI YAML, Docker images, browser caching, sharding, artifact upload). |
| `playwright-debugging` | Debugging unclear or flaky tests: Trace Viewer and debugger — recording and opening traces, the UI inspector tabs, PWDEBUG, Playwright Inspector, VS Code debugging; and migration from Puppeteer and Protractor plus Selenium Grid integration — API mappings, before/after. |
| `playwright-tooling` | Playwright tooling: the Playwright MCP server (installation, configuration for headed/headless and transport, capabilities, profile modes, clients, vision mode) with all 40+ MCP tools and their parameters (navigation, interaction, forms, screenshots, tabs, network, storage, testing, tracing, video, PDF); and the agent CLI — introduction, installation, configuration, sessions, snapshots, vision mode, capabilities, skills, plus the command reference: attach, interaction, keyboard-mouse, navigation, network-routing, dialogs, console-eval, storage, tabs, screenshots-pdf, video, tracing, test-debugging. |

## License & author

MIT. Source: the official Playwright documentation (https://playwright.dev).
