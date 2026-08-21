# Playwright: Browsers, contexts, pages, extensions, WebView2

## Contents

- [Browser engines](#browser-engines)
- [Browser installation](#browser-installation)
- [Browser configuration (playwright.config.ts)](#browser-configuration-playwrightconfigts)
- [BrowserContext: isolated browser sessions](#browsercontext-isolated-browser-sessions)
- [Pages: multiple pages and tabs](#pages-multiple-pages-and-tabs)
- [Testing Chrome extensions](#testing-chrome-extensions)
- [Testing WebView2 (Windows)](#testing-webview2-windows)

## Browser engines

| Engine | Description |
|---|---|
| `chromium` | Open-source build, runs ahead of the current Chrome version |
| `firefox` | Matches Firefox Stable; does NOT work with the installed Firefox |
| `webkit` | Based on the current WebKit main branch; not compatible with Safari |

### Chromium variants

| Variant | Channel | Description |
|---|---|---|
| Headless Shell | — | Lightweight build for pure headless operation |
| New Headless (real Chrome) | `'chromium'` | Full Chrome browser in headless mode |
| Google Chrome | `'chrome'`, `'chrome-beta'`, `'chrome-dev'`, `'chrome-canary'` | Real Chrome channels |
| Microsoft Edge | `'msedge'`, `'msedge-beta'`, `'msedge-dev'`, `'msedge-canary'` | Real Edge channels |

---

## Browser installation

### Installation commands

```bash
# All default browsers
npx playwright install

# A specific browser
npx playwright install webkit
npx playwright install chromium firefox

# With OS dependencies (recommended for CI)
npx playwright install --with-deps
npx playwright install --with-deps chromium

# Headless Shell only (more compact for CI)
npx playwright install --with-deps --only-shell

# New Headless (without shell, real Chrome)
npx playwright install --with-deps --no-shell

# List all installable browsers
npx playwright install --help
```

### Management commands

```bash
npx playwright install --list          # Show installed browsers
npx playwright uninstall               # Remove the current version
npx playwright uninstall --all         # Remove all Playwright versions
npx playwright --version               # Show the Playwright version
```

### Storage paths (default)

| OS | Path |
|---|---|
| Windows | `%USERPROFILE%\AppData\Local\ms-playwright` |
| macOS | `~/Library/Caches/ms-playwright` |
| Linux | `~/.cache/ms-playwright` |

Typical size: ~650 MB (Chromium 281 MB, Firefox 187 MB, WebKit 180 MB)

### Setting a custom installation path

```bash
# Install browsers in a custom location
PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers npx playwright install

# Run tests with the custom path
PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers npx playwright test

# Hermetic install: locally in node_modules
PLAYWRIGHT_BROWSERS_PATH=0 npx playwright install
```

### Disabling garbage collection

```bash
PLAYWRIGHT_SKIP_BROWSER_GC=1 npx playwright test
```

### Proxy and download configuration (environment variables)

| Variable | Description | Example |
|---|---|---|
| `HTTPS_PROXY` | Proxy server | `https://192.0.2.1` |
| `NODE_EXTRA_CA_CERTS` | Custom CA certificate | `/pfad/zum/cert.pem` |
| `PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT` | Timeout in ms | `120000` |
| `PLAYWRIGHT_DOWNLOAD_HOST` | Custom artifact repository | `http://192.0.2.1` |
| `PLAYWRIGHT_CHROMIUM_DOWNLOAD_HOST` | Chromium-specific | `http://203.0.113.3` |
| `PLAYWRIGHT_FIREFOX_DOWNLOAD_HOST` | Firefox-specific | `http://203.0.113.3` |
| `PLAYWRIGHT_WEBKIT_DOWNLOAD_HOST` | WebKit-specific | `http://203.0.113.3` |

---

## Browser configuration (playwright.config.ts)

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // Desktop browsers
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    // Mobile emulation
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
    // Real browsers
    {
      name: 'Google Chrome',
      use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    },
    {
      name: 'Microsoft Edge',
      use: { ...devices['Desktop Edge'], channel: 'msedge' },
    },
  ],
});
```

### Running a specific project

```bash
npx playwright test --project=firefox
npx playwright test --project=webkit --project=firefox
```

---

## BrowserContext: isolated browser sessions

A `BrowserContext` corresponds to a fully isolated browser session (its own cookies,
localStorage, session). Several contexts can run in parallel within one browser.

### Creating a context

```typescript
const context = await browser.newContext(options);
```

### All newContext() options

| Option | Type | Default | Description |
|---|---|---|---|
| `viewport` | `{ width: number; height: number } \| null` | `1280x720` | Viewport size; `null` = no fixed viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | CSS `prefers-color-scheme` |
| `locale` | `string` | — | Browser locale, e.g. `'de-DE'` |
| `timezoneId` | `string` | — | ICU timezone ID |
| `geolocation` | `{ latitude: number; longitude: number; accuracy?: number }` | — | GPS coordinates |
| `offline` | `boolean` | `false` | Offline mode |
| `proxy` | `{ server: string; bypass?: string; username?: string; password?: string }` | — | Proxy |
| `httpCredentials` | `{ username: string; password: string; origin?: string; send?: 'always' \| 'unauthorized' }` | — | HTTP auth |
| `extraHTTPHeaders` | `Record<string, string>` | — | Additional HTTP headers |
| `userAgent` | `string` | — | User agent |
| `deviceScaleFactor` | `number` | `1` | DPR |
| `isMobile` | `boolean` | `false` | Mobile emulation |
| `hasTouch` | `boolean` | `false` | Touch events |
| `javaScriptEnabled` | `boolean` | `true` | JavaScript on/off |
| `bypassCSP` | `boolean` | `false` | Bypass CSP |
| `ignoreHTTPSErrors` | `boolean` | `false` | Ignore SSL errors |
| `acceptDownloads` | `boolean` | `true` | Accept downloads |
| `baseURL` | `string` | — | Base URL for `goto()` |
| `storageState` | `string \| object` | — | Saved auth state |
| `recordHar` | `object` | — | HAR recording |
| `recordVideo` | `object` | — | Video recording |
| `permissions` | `string[]` | — | Permissions granted upfront |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Service workers |
| `strictSelectors` | `boolean` | `false` | Strict selector checking |
| `contrast` | `'no-preference' \| 'more' \| 'null'` | — | `prefers-contrast` |
| `forcedColors` | `'active' \| 'none' \| 'null'` | — | `forced-colors` |
| `reducedMotion` | `'reduce' \| 'no-preference' \| 'null'` | — | `prefers-reduced-motion` |
| `screen` | `{ width: number; height: number }` | — | Screen size |
| `clientCertificates` | `object[]` | — | Client certificates for mTLS |

### BrowserContext methods

| Method | Signature | Description |
|---|---|---|
| `addCookies` | `(cookies: Cookie[]) => Promise<void>` | Add cookies |
| `addInitScript` | `(script, arg?) => Promise<Disposable>` | Inject a script before the page loads |
| `browser` | `() => Browser \| null` | The associated browser |
| `clearCookies` | `(options?) => Promise<void>` | Delete cookies (filterable by domain/name/path) |
| `clearPermissions` | `() => Promise<void>` | Remove all permissions |
| `close` | `(options?) => Promise<void>` | Close the context (`reason?: string`) |
| `cookies` | `(urls?) => Promise<Cookie[]>` | Retrieve cookies |
| `exposeBinding` | `(name, callback) => Promise<Disposable>` | JS function with source access |
| `exposeFunction` | `(name, callback) => Promise<Disposable>` | Expose a JS function |
| `grantPermissions` | `(permissions, options?) => Promise<void>` | Grant permissions |
| `newPage` | `() => Promise<Page>` | New page in the context |
| `pages` | `() => Page[]` | All open pages |
| `route` | `(url, handler, options?) => Promise<Disposable>` | Network route |
| `setDefaultNavigationTimeout` | `(timeout: number) => void` | Navigation timeout in ms |
| `setDefaultTimeout` | `(timeout: number) => void` | Default timeout for all operations |
| `setExtraHTTPHeaders` | `(headers: Record<string, string>) => Promise<void>` | Set extra headers |
| `setGeolocation` | `(geolocation: \| null) => Promise<void>` | Change GPS |
| `setOffline` | `(offline: boolean) => Promise<void>` | Change offline mode |
| `setStorageState` | `(storageState) => Promise<void>` | Load auth state |
| `storageState` | `(options?) => Promise<object>` | Export auth state |
| `unroute` | `(url, handler?) => Promise<void>` | Remove a route |
| `waitForEvent` | `(event, predicate?) => Promise<object>` | Wait for a context event |

#### Context events

`'close'`, `'console'`, `'dialog'`, `'page'`, `'request'`, `'response'`,
`'requestfailed'`, `'requestfinished'`, `'serviceworker'`, `'weberror'`

### Cookie structure

```typescript
interface Cookie {
  name: string;
  value: string;
  url?: string;           // either url or domain+path
  domain?: string;
  path?: string;
  expires?: number;       // Unix timestamp in seconds
  httpOnly?: boolean;
  secure?: boolean;
  sameSite?: 'Strict' | 'Lax' | 'None';
  partitionKey?: string;
}
```

### Multiple contexts (multi-user test)

```typescript
test('Admin and user at the same time', async ({ browser }) => {
  const adminContext = await browser.newContext({ storageState: 'admin-auth.json' });
  const userContext  = await browser.newContext({ storageState: 'user-auth.json' });

  const adminPage = await adminContext.newPage();
  const userPage  = await userContext.newPage();

  await adminPage.goto('/admin/chat');
  await userPage.goto('/chat');

  // Operate both pages at the same time
  await adminPage.getByRole('textbox').fill('Hallo User!');
  await adminPage.keyboard.press('Enter');

  await expect(userPage.getByText('Hallo User!')).toBeVisible();

  await adminContext.close();
  await userContext.close();
});
```

---

## Pages: multiple pages and tabs

### Creating a page

```typescript
const page = await context.newPage();
await page.goto('https://example.com');
```

### All open pages

```typescript
const allPages = context.pages();
```

### Intercepting a new tab (target="_blank")

```typescript
// Variant 1: expected event
const pagePromise = context.waitForEvent('page');
await page.getByText('Neuen Tab oeffnen').click();
const newPage = await pagePromise;
await newPage.waitForLoadState();

// Variant 2: monitor all new pages
context.on('page', async (newPage) => {
  await newPage.waitForLoadState();
  console.log(await newPage.title());
});
```

### Intercepting popups

```typescript
// Variant 1: expected
const popupPromise = page.waitForEvent('popup');
await page.getByText('Popup oeffnen').click();
const popup = await popupPromise;

// Variant 2: listener
page.on('popup', async (popup) => {
  await popup.waitForLoadState();
  console.log(popup.url());
});
```

### Browser methods for pages

| Method | Signature | Description |
|---|---|---|
| `newPage` | `(options?) => Promise<Page>` | New page in a new context |
| `contexts` | `() => BrowserContext[]` | All open contexts |
| `close` | `(options?) => Promise<void>` | Close the browser (`reason?: string`) |
| `isConnected` | `() => boolean` | Connection status |
| `version` | `() => string` | Browser version |
| `browserType` | `() => BrowserType` | Chromium / Firefox / WebKit |

### Browser events

- `on('disconnected')` — the browser connection was closed
- `on('context')` — a new context was created

---

## Testing Chrome extensions

Extensions only work with Chromium in a persistent context.

### Loading an extension

```typescript
import { chromium } from '@playwright/test';
import path from 'path';

const pathToExtension = path.join(__dirname, 'my-extension');

const context = await chromium.launchPersistentContext('', {
  channel: 'chromium',
  args: [
    `--disable-extensions-except=${pathToExtension}`,
    `--load-extension=${pathToExtension}`,
  ],
  headless: false, // Extensions require headed mode or new headless
});
```

### Extension ID and service worker (Manifest V3)

```typescript
// Retrieve the service worker
let [serviceWorker] = context.serviceWorkers();
if (!serviceWorker) {
  serviceWorker = await context.waitForEvent('serviceworker');
}

// Extract the extension ID from the service worker URL
const extensionId = serviceWorker.url().split('/')[2];
// Format: chrome-extension://<id>/service-worker.js

// Test the extension popup
const popupPage = await context.newPage();
await popupPage.goto(`chrome-extension://${extensionId}/popup.html`);
```

### Test fixture for extensions

```typescript
// fixtures.ts
import { test as base, chromium, type BrowserContext } from '@playwright/test';
import path from 'path';

export const test = base.extend<{
  context: BrowserContext;
  extensionId: string;
}>({
  context: async ({}, use) => {
    const pathToExtension = path.join(__dirname, 'extension');
    const context = await chromium.launchPersistentContext('', {
      channel: 'chromium',
      args: [
        `--disable-extensions-except=${pathToExtension}`,
        `--load-extension=${pathToExtension}`,
      ],
    });
    await use(context);
    await context.close();
  },
  extensionId: async ({ context }, use) => {
    let [background] = context.serviceWorkers();
    if (!background) {
      background = await context.waitForEvent('serviceworker');
    }
    const extensionId = background.url().split('/')[2];
    await use(extensionId);
  },
});

export const expect = test.expect;
```

### Note: MV3 service worker suspension

Chrome suspends MV3 service workers after ~30 seconds of inactivity.
Playwright keeps the same worker object across restarts — `evaluate()` calls
remain transparent. Calls already running at the moment of suspension throw an error.

---

## Testing WebView2 (Windows)

WebView2 is a WinForms control that uses Microsoft Edge for rendering.

### Enabling remote debugging (C#)

```csharp
await this.webView.EnsureCoreWebView2Async(
  await CoreWebView2Environment.CreateAsync(null, null,
    new CoreWebView2EnvironmentOptions() {
      AdditionalBrowserArguments = "--remote-debugging-port=9222"
    })
).ConfigureAwait(false);
```

Or as an environment variable: `WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=9222`

### Connecting Playwright

```typescript
import { chromium } from '@playwright/test';

const browser = await chromium.connectOverCDP('http://localhost:9222');
const context = browser.contexts()[0];
const page = context.pages()[0];
```

### Test fixture (complete)

```typescript
import { test as base } from '@playwright/test';
import { spawn, type ChildProcess } from 'child_process';
import fs from 'fs';

const test = base.extend<{ page: Page }, { appProcess: ChildProcess }>({
  appProcess: [async ({}, use, workerInfo) => {
    const port = 10000 + workerInfo.workerIndex;
    const dataDir = `/tmp/webview2-test-${workerInfo.workerIndex}`;

    const proc = spawn('path/to/app.exe', [], {
      env: {
        ...process.env,
        WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS: `--remote-debugging-port=${port}`,
        WEBVIEW2_USER_DATA_FOLDER: dataDir,
      },
    });

    await use(proc);
    proc.kill();
    fs.rmSync(dataDir, { recursive: true, force: true });
  }, { scope: 'worker' }],

  page: async ({ appProcess }, use) => {
    const browser = await chromium.connectOverCDP(`http://localhost:${10000 + test.info().workerIndex}`);
    const context = browser.contexts()[0];
    const page = context.pages()[0];
    await use(page);
  },
});
```

### Important note: user data directory

By default WebView2 shares the same directory for all instances.
For parallel tests `WEBVIEW2_USER_DATA_FOLDER` must be unique per worker.

<!-- Sources:
https://playwright.dev/docs/browsers
https://playwright.dev/docs/browser-contexts
https://playwright.dev/docs/pages
https://playwright.dev/docs/chrome-extensions
https://playwright.dev/docs/webview2
https://playwright.dev/docs/api/class-browser
https://playwright.dev/docs/api/class-browsercontext
-->
