# Playwright Intro: Installation, Library, Languages

## Contents

- [What is Playwright](#what-is-playwright)
- [System requirements](#system-requirements)
- [Installation: @playwright/test (recommended)](#installation-playwrighttest-recommended)
- [Library mode (without the test runner)](#library-mode-without-the-test-runner)
- [BrowserType.launch() — All options](#browsertypelaunch-all-options)
- [Browser.newContext() — All options](#browsernewcontext-all-options)
- [Browser lifecycle pattern](#browser-lifecycle-pattern)
- [Supported languages](#supported-languages)
- [Update process](#update-process)
- [Running tests (quick reference)](#running-tests-quick-reference)

## What is Playwright

Playwright is an end-to-end test framework for modern web applications. It bundles:
- Test runner with parallelization
- Assertions with web-first retry
- Isolation via BrowserContext
- Tooling: Trace Viewer, UI Mode, Codegen, VS Code extension

Supported browser engines: **Chromium**, **WebKit**, **Firefox** (headless and headed,
native mobile emulation for Android Chrome and Mobile Safari).

---

## System requirements

| Component | Requirement |
|---|---|
| Node.js | 20.x, 22.x or 24.x |
| Windows | 11+ or Server 2019+ (incl. WSL) |
| macOS | 14 (Sonoma) or newer |
| Linux | Debian 12/13 or Ubuntu 22.04/24.04 (x86-64 or arm64) |

---

## Installation: @playwright/test (recommended)

```bash
# npm
npm init playwright@latest

# yarn
yarn create playwright

# pnpm
pnpm create playwright
```

The interactive setup asks:
- Language: TypeScript (default) or JavaScript
- Test directory (default: `tests`)
- Create a GitHub Actions workflow
- Download browser binaries

Generated files:
- `playwright.config.ts` — central configuration
- `tests/example.spec.ts` — example test
- `package.json` / lock files

---

## Library mode (without the test runner)

For scripts without `@playwright/test`:

```bash
npm i -D playwright
npx playwright install chromium firefox webkit
```

Or with automatic browser download via helper packages:

```bash
npm i -D @playwright/browser-chromium @playwright/browser-firefox @playwright/browser-webkit
```

### Basic structure of a library script

All Playwright APIs are asynchronous and return `Promise` objects.
Recommended pattern: `async/await`.

```typescript
import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://playwright.dev/');
  await page.screenshot({ path: 'example.png' });

  await context.close();
  await browser.close();
})();
```

### TypeScript support in library scripts

```typescript
// @ts-check  (for .js files)
/** @type {import('playwright').Page} */
let page;
```

### Library vs. @playwright/test

| Feature | Library (`playwright`) | Test runner (`@playwright/test`) |
|---|---|---|
| Test framework | None (choose your own) | Built in |
| Fixtures | Manual | `page`, `context`, `browser` etc. |
| Assertions | Simple (no retry) | Web-first with auto retry |
| Parallelization | Manual | Automatic |
| Isolation | Manual (`newContext()`) | Automatic per test |
| Trace/reporting | Configure manually | Built in |

---

## BrowserType.launch() — All options

```typescript
const browser = await chromium.launch(options);
// also: firefox.launch(options), webkit.launch(options)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `headless` | `boolean` | `true` | Headless mode; `false` shows the browser window |
| `channel` | `string` | — | Browser channel: `'chrome'`, `'chrome-beta'`, `'chrome-dev'`, `'chrome-canary'`, `'msedge'`, `'msedge-beta'`, `'msedge-dev'`, `'msedge-canary'`, `'chromium'` |
| `executablePath` | `string` | bundled binary | Path to the browser binary |
| `args` | `string[]` | — | Additional CLI arguments for the browser process |
| `ignoreDefaultArgs` | `boolean \| string[]` | `false` | Disable default args (`true` = all, `string[]` = specific ones) |
| `proxy` | `object` | — | `{ server, bypass?, username?, password? }` |
| `downloadsPath` | `string` | temp directory | Path for downloaded files |
| `tracesDir` | `string` | — | Directory for trace files |
| `chromiumSandbox` | `boolean` | `false` | Enable the Chromium sandbox |
| `firefoxUserPrefs` | `Record<string, string \| number \| boolean>` | — | Firefox user preferences |
| `handleSIGINT` | `boolean` | `true` | Close the browser on Ctrl+C |
| `handleSIGTERM` | `boolean` | `true` | Close the browser on SIGTERM |
| `handleSIGHUP` | `boolean` | `true` | Close the browser on SIGHUP |
| `logger` | `Logger` | — | Custom logger object |
| `timeout` | `number` | `30000` | Max. time for the browser to start in ms |
| `env` | `Record<string, string \| undefined>` | — | Environment variables for the browser process |
| `slowMo` | `number` | — | Delay in ms between actions (debugging) |
| `artifactsDir` | `string` | temp directory | Directory for artifacts |

### Example: visible browser with slow motion

```typescript
const browser = await firefox.launch({
  headless: false,
  slowMo: 50,
});
```

---

## Browser.newContext() — All options

```typescript
const context = await browser.newContext(options);
```

| Option | Type | Default | Description |
|---|---|---|---|
| `viewport` | `{ width: number; height: number } \| null` | `1280x720` | Viewport size; `null` = no fixed viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | CSS `prefers-color-scheme` emulation |
| `locale` | `string` | — | Browser locale, e.g. `'de-DE'`, `'en-GB'` |
| `timezoneId` | `string` | — | ICU timezone ID, e.g. `'Europe/Berlin'` |
| `geolocation` | `{ latitude: number; longitude: number; accuracy?: number }` | — | GPS position |
| `offline` | `boolean` | `false` | Simulate offline mode |
| `proxy` | `{ server: string; bypass?: string; username?: string; password?: string }` | — | Proxy configuration |
| `httpCredentials` | `{ username: string; password: string; origin?: string; send?: 'always' \| 'unauthorized' }` | — | HTTP authentication |
| `extraHTTPHeaders` | `Record<string, string>` | — | Additional HTTP headers for all requests |
| `userAgent` | `string` | — | User agent string |
| `deviceScaleFactor` | `number` | `1` | Device pixel ratio (DPR) |
| `isMobile` | `boolean` | `false` | Mobile emulation |
| `hasTouch` | `boolean` | `false` | Enable touch events |
| `javaScriptEnabled` | `boolean` | `true` | Disable JavaScript |
| `bypassCSP` | `boolean` | `false` | Bypass the Content Security Policy |
| `ignoreHTTPSErrors` | `boolean` | `false` | Ignore SSL errors |
| `acceptDownloads` | `boolean` | `true` | Accept downloads |
| `baseURL` | `string` | — | Base URL for `page.goto()` (relative paths) |
| `storageState` | `string \| object` | — | Saved auth state (path or object) |
| `recordHar` | `object` | — | Configure HAR recording |
| `recordVideo` | `object` | — | Configure video recording |
| `permissions` | `string[]` | — | Browser permissions granted up front |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Control service workers |
| `strictSelectors` | `boolean` | `false` | Strict selector checking (error on multiple matches) |
| `contrast` | `'no-preference' \| 'more' \| 'null'` | — | `prefers-contrast` emulation |
| `forcedColors` | `'active' \| 'none' \| 'null'` | — | `forced-colors` emulation |
| `reducedMotion` | `'reduce' \| 'no-preference' \| 'null'` | — | `prefers-reduced-motion` emulation |
| `screen` | `{ width: number; height: number }` | — | Screen size (independent of the viewport) |
| `clientCertificates` | `object[]` | — | Client certificates for mTLS |

### Device emulation

```typescript
import { chromium, devices } from 'playwright';

const browser = await chromium.launch();
const context = await browser.newContext({
  ...devices['iPhone 15'],
});
const page = await context.newPage();
```

---

## Browser lifecycle pattern

```typescript
import { chromium } from 'playwright';

(async () => {
  // 1. Start the browser
  const browser = await chromium.launch({ headless: false });

  // 2. Create an isolated context
  const context = await browser.newContext({
    locale: 'de-DE',
    timezoneId: 'Europe/Berlin',
  });

  // 3. Open a page
  const page = await context.newPage();
  await page.goto('https://example.com');

  // 4. Perform actions
  await page.screenshot({ path: 'screenshot.png' });

  // 5. Release resources (order matters)
  await context.close();
  await browser.close();
})();
```

---

## Supported languages

| Language | Package | Test integration |
|---|---|---|
| **JavaScript / TypeScript** | `@playwright/test` | Own test runner (default) |
| **Python** | `playwright` (pip) | `pytest-playwright` plugin (recommended) |
| **Java** | `com.microsoft.playwright` | JUnit / TestNG |
| **.NET** | `Microsoft.Playwright` | MSTest / NUnit / xUnit / xUnit v3 |

All languages share the same core implementation and support the same browser automation APIs. The testing ecosystem varies per language.

---

## Update process

```bash
# npm
npm install -D @playwright/test@latest
npx playwright install --with-deps

# yarn
yarn add --dev @playwright/test@latest
yarn playwright install --with-deps

# pnpm
pnpm install --save-dev @playwright/test@latest
pnpm exec playwright install --with-deps

# Check the version
npx playwright --version
```

---

## Running tests (quick reference)

```bash
npx playwright test              # All tests (headless, parallel)
npx playwright test --headed     # Browser visible
npx playwright test --ui         # UI mode (watch + debugger)
npx playwright test --debug      # Inspector debugging
npx playwright show-report       # Open the HTML report
```

<!-- Sources:
https://playwright.dev/docs/intro
https://playwright.dev/docs/library
https://playwright.dev/docs/languages
https://playwright.dev/docs/api/class-browsertype#browser-type-launch
https://playwright.dev/docs/api/class-browser
-->
