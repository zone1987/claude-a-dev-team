# Playwright: Browser, Contexts, Pages, Extensions, WebView2

## Browser-Engines

| Engine | Beschreibung |
|---|---|
| `chromium` | Open-Source-Build, laeuft der aktuellen Chrome-Version voraus |
| `firefox` | Entspricht Firefox Stable; funktioniert NICHT mit dem installierten Firefox |
| `webkit` | Basiert auf dem aktuellen WebKit-Main-Branch; nicht kompatibel mit Safari |

### Chromium-Varianten

| Variante | Channel | Beschreibung |
|---|---|---|
| Headless Shell | — | Leichtgewichtiger Build fuer reinen Headless-Betrieb |
| New Headless (echter Chrome) | `'chromium'` | Vollstaendiger Chrome-Browser im Headless-Modus |
| Google Chrome | `'chrome'`, `'chrome-beta'`, `'chrome-dev'`, `'chrome-canary'` | Echte Chrome-Kanaele |
| Microsoft Edge | `'msedge'`, `'msedge-beta'`, `'msedge-dev'`, `'msedge-canary'` | Echte Edge-Kanaele |

---

## Browser-Installation

### Installationsbefehle

```bash
# Alle Standard-Browser
npx playwright install

# Bestimmten Browser
npx playwright install webkit
npx playwright install chromium firefox

# Mit OS-Abhaengigkeiten (empfohlen fuer CI)
npx playwright install --with-deps
npx playwright install --with-deps chromium

# Nur Headless Shell (kompakter fuer CI)
npx playwright install --with-deps --only-shell

# New Headless (ohne Shell, echter Chrome)
npx playwright install --with-deps --no-shell

# Alle installierbaren Browser auflisten
npx playwright install --help
```

### Verwaltungsbefehle

```bash
npx playwright install --list          # Installierte Browser anzeigen
npx playwright uninstall               # Aktuelle Version entfernen
npx playwright uninstall --all         # Alle Playwright-Versionen entfernen
npx playwright --version               # Playwright-Version anzeigen
```

### Speicherpfade (Standard)

| OS | Pfad |
|---|---|
| Windows | `%USERPROFILE%\AppData\Local\ms-playwright` |
| macOS | `~/Library/Caches/ms-playwright` |
| Linux | `~/.cache/ms-playwright` |

Typische Groesse: ~650 MB (Chromium 281 MB, Firefox 187 MB, WebKit 180 MB)

### Benutzerdefinierten Installationspfad setzen

```bash
# Browser an benutzerdefiniertem Ort installieren
PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers npx playwright install

# Tests mit benutzerdefiniertem Pfad ausfuehren
PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers npx playwright test

# Hermetic Install: lokal in node_modules
PLAYWRIGHT_BROWSERS_PATH=0 npx playwright install
```

### Garbage Collection deaktivieren

```bash
PLAYWRIGHT_SKIP_BROWSER_GC=1 npx playwright test
```

### Proxy und Download-Konfiguration (Umgebungsvariablen)

| Variable | Beschreibung | Beispiel |
|---|---|---|
| `HTTPS_PROXY` | Proxy-Server | `https://192.0.2.1` |
| `NODE_EXTRA_CA_CERTS` | Benutzerdefiniertes CA-Zertifikat | `/pfad/zum/cert.pem` |
| `PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT` | Timeout in ms | `120000` |
| `PLAYWRIGHT_DOWNLOAD_HOST` | Benutzerdefiniertes Artefakt-Repository | `http://192.0.2.1` |
| `PLAYWRIGHT_CHROMIUM_DOWNLOAD_HOST` | Chromium-spezifisch | `http://203.0.113.3` |
| `PLAYWRIGHT_FIREFOX_DOWNLOAD_HOST` | Firefox-spezifisch | `http://203.0.113.3` |
| `PLAYWRIGHT_WEBKIT_DOWNLOAD_HOST` | WebKit-spezifisch | `http://203.0.113.3` |

---

## Browser-Konfiguration (playwright.config.ts)

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // Desktop-Browser
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
    // Mobile-Emulation
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
    // Echte Browser
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

### Bestimmtes Projekt ausfuehren

```bash
npx playwright test --project=firefox
npx playwright test --project=webkit --project=firefox
```

---

## BrowserContext: Isolierte Browser-Sitzungen

Ein `BrowserContext` entspricht einer vollstaendig isolierten Browser-Sitzung (eigene Cookies,
localStorage, Sitzung). Mehrere Contexts koennen in einem Browser parallel laufen.

### Context erstellen

```typescript
const context = await browser.newContext(options);
```

### Alle newContext()-Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `viewport` | `{ width: number; height: number } \| null` | `1280x720` | Viewport-Groesse; `null` = kein fester Viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | CSS `prefers-color-scheme` |
| `locale` | `string` | — | Browser-Locale, z.B. `'de-DE'` |
| `timezoneId` | `string` | — | ICU-Timezone-ID |
| `geolocation` | `{ latitude: number; longitude: number; accuracy?: number }` | — | GPS-Koordinaten |
| `offline` | `boolean` | `false` | Offline-Modus |
| `proxy` | `{ server: string; bypass?: string; username?: string; password?: string }` | — | Proxy |
| `httpCredentials` | `{ username: string; password: string; origin?: string; send?: 'always' \| 'unauthorized' }` | — | HTTP-Auth |
| `extraHTTPHeaders` | `Record<string, string>` | — | Zus. HTTP-Header |
| `userAgent` | `string` | — | User-Agent |
| `deviceScaleFactor` | `number` | `1` | DPR |
| `isMobile` | `boolean` | `false` | Mobile-Emulation |
| `hasTouch` | `boolean` | `false` | Touch-Events |
| `javaScriptEnabled` | `boolean` | `true` | JavaScript an/aus |
| `bypassCSP` | `boolean` | `false` | CSP umgehen |
| `ignoreHTTPSErrors` | `boolean` | `false` | SSL-Fehler ignorieren |
| `acceptDownloads` | `boolean` | `true` | Downloads annehmen |
| `baseURL` | `string` | — | Basis-URL fuer `goto()` |
| `storageState` | `string \| object` | — | Gespeicherter Auth-Zustand |
| `recordHar` | `object` | — | HAR-Aufnahme |
| `recordVideo` | `object` | — | Video-Aufnahme |
| `permissions` | `string[]` | — | Vorab erteilte Permissions |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Service Worker |
| `strictSelectors` | `boolean` | `false` | Strikte Selektor-Pruefung |
| `contrast` | `'no-preference' \| 'more' \| 'null'` | — | `prefers-contrast` |
| `forcedColors` | `'active' \| 'none' \| 'null'` | — | `forced-colors` |
| `reducedMotion` | `'reduce' \| 'no-preference' \| 'null'` | — | `prefers-reduced-motion` |
| `screen` | `{ width: number; height: number }` | — | Bildschirmgroesse |
| `clientCertificates` | `object[]` | — | Client-Zertifikate fuer mTLS |

### BrowserContext-Methoden

| Methode | Signatur | Beschreibung |
|---|---|---|
| `addCookies` | `(cookies: Cookie[]) => Promise<void>` | Cookies hinzufuegen |
| `addInitScript` | `(script, arg?) => Promise<Disposable>` | Script vor Seiten-Laden einfuegen |
| `browser` | `() => Browser \| null` | Zugehoeriger Browser |
| `clearCookies` | `(options?) => Promise<void>` | Cookies loeschen (nach domain/name/path filterbar) |
| `clearPermissions` | `() => Promise<void>` | Alle Permissions entfernen |
| `close` | `(options?) => Promise<void>` | Context schliessen (`reason?: string`) |
| `cookies` | `(urls?) => Promise<Cookie[]>` | Cookies abrufen |
| `exposeBinding` | `(name, callback) => Promise<Disposable>` | JS-Funktion mit Source-Zugang |
| `exposeFunction` | `(name, callback) => Promise<Disposable>` | JS-Funktion exponieren |
| `grantPermissions` | `(permissions, options?) => Promise<void>` | Permissions erteilen |
| `newPage` | `() => Promise<Page>` | Neue Seite im Context |
| `pages` | `() => Page[]` | Alle offenen Seiten |
| `route` | `(url, handler, options?) => Promise<Disposable>` | Netzwerk-Route |
| `setDefaultNavigationTimeout` | `(timeout: number) => void` | Navigation-Timeout in ms |
| `setDefaultTimeout` | `(timeout: number) => void` | Default-Timeout fuer alle Operationen |
| `setExtraHTTPHeaders` | `(headers: Record<string, string>) => Promise<void>` | Extra-Header setzen |
| `setGeolocation` | `(geolocation: \| null) => Promise<void>` | GPS aendern |
| `setOffline` | `(offline: boolean) => Promise<void>` | Offline-Modus aendern |
| `setStorageState` | `(storageState) => Promise<void>` | Auth-Zustand laden |
| `storageState` | `(options?) => Promise<object>` | Auth-Zustand exportieren |
| `unroute` | `(url, handler?) => Promise<void>` | Route entfernen |
| `waitForEvent` | `(event, predicate?) => Promise<object>` | Auf Context-Event warten |

#### Context-Events

`'close'`, `'console'`, `'dialog'`, `'page'`, `'request'`, `'response'`,
`'requestfailed'`, `'requestfinished'`, `'serviceworker'`, `'weberror'`

### Cookie-Struktur

```typescript
interface Cookie {
  name: string;
  value: string;
  url?: string;           // entweder url oder domain+path
  domain?: string;
  path?: string;
  expires?: number;       // Unix-Timestamp in Sekunden
  httpOnly?: boolean;
  secure?: boolean;
  sameSite?: 'Strict' | 'Lax' | 'None';
  partitionKey?: string;
}
```

### Mehrere Contexts (Multi-User-Test)

```typescript
test('Admin und Benutzer gleichzeitig', async ({ browser }) => {
  const adminContext = await browser.newContext({ storageState: 'admin-auth.json' });
  const userContext  = await browser.newContext({ storageState: 'user-auth.json' });

  const adminPage = await adminContext.newPage();
  const userPage  = await userContext.newPage();

  await adminPage.goto('/admin/chat');
  await userPage.goto('/chat');

  // Beide Seiten gleichzeitig bedienen
  await adminPage.getByRole('textbox').fill('Hallo User!');
  await adminPage.keyboard.press('Enter');

  await expect(userPage.getByText('Hallo User!')).toBeVisible();

  await adminContext.close();
  await userContext.close();
});
```

---

## Pages: Mehrere Seiten und Tabs

### Seite erstellen

```typescript
const page = await context.newPage();
await page.goto('https://example.com');
```

### Alle offenen Seiten

```typescript
const allPages = context.pages();
```

### Neuen Tab abfangen (target="_blank")

```typescript
// Variante 1: Erwartetes Ereignis
const pagePromise = context.waitForEvent('page');
await page.getByText('Neuen Tab oeffnen').click();
const newPage = await pagePromise;
await newPage.waitForLoadState();

// Variante 2: Alle neuen Seiten ueberwachen
context.on('page', async (newPage) => {
  await newPage.waitForLoadState();
  console.log(await newPage.title());
});
```

### Popups abfangen

```typescript
// Variante 1: Erwartet
const popupPromise = page.waitForEvent('popup');
await page.getByText('Popup oeffnen').click();
const popup = await popupPromise;

// Variante 2: Listener
page.on('popup', async (popup) => {
  await popup.waitForLoadState();
  console.log(popup.url());
});
```

### Browser-Methoden fuer Pages

| Methode | Signatur | Beschreibung |
|---|---|---|
| `newPage` | `(options?) => Promise<Page>` | Neue Seite in neuem Context |
| `contexts` | `() => BrowserContext[]` | Alle offenen Contexts |
| `close` | `(options?) => Promise<void>` | Browser schliessen (`reason?: string`) |
| `isConnected` | `() => boolean` | Verbindungsstatus |
| `version` | `() => string` | Browser-Version |
| `browserType` | `() => BrowserType` | Chromium / Firefox / WebKit |

### Browser-Events

- `on('disconnected')` — Browser-Verbindung getrennt
- `on('context')` — Neuer Context erstellt

---

## Chrome-Extensions testen

Extensions funktionieren nur mit Chromium im Persistent-Context.

### Extension laden

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
  headless: false, // Extensions benoetigen headed-Modus oder neuen Headless
});
```

### Extension-ID und Service Worker (Manifest V3)

```typescript
// Service Worker abrufen
let [serviceWorker] = context.serviceWorkers();
if (!serviceWorker) {
  serviceWorker = await context.waitForEvent('serviceworker');
}

// Extension-ID aus der Service-Worker-URL extrahieren
const extensionId = serviceWorker.url().split('/')[2];
// Format: chrome-extension://<id>/service-worker.js

// Extension-Popup testen
const popupPage = await context.newPage();
await popupPage.goto(`chrome-extension://${extensionId}/popup.html`);
```

### Test-Fixture fuer Extensions

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

### Hinweis: MV3 Service Worker Suspension

Chrome suspendiert MV3 Service Worker nach ~30 Sekunden Inaktivitaet.
Playwright haelt dasselbe Worker-Objekt waehrend Neustarts — `evaluate()`-Aufrufe
bleiben transparent. Bereits laufende Calls zum Suspension-Zeitpunkt werfen einen Fehler.

---

## WebView2 testen (Windows)

WebView2 ist ein WinForms-Steuerelement, das Microsoft Edge zur Darstellung verwendet.

### Remote-Debugging aktivieren (C#)

```csharp
await this.webView.EnsureCoreWebView2Async(
  await CoreWebView2Environment.CreateAsync(null, null,
    new CoreWebView2EnvironmentOptions() {
      AdditionalBrowserArguments = "--remote-debugging-port=9222"
    })
).ConfigureAwait(false);
```

Oder als Umgebungsvariable: `WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=9222`

### Playwright verbinden

```typescript
import { chromium } from '@playwright/test';

const browser = await chromium.connectOverCDP('http://localhost:9222');
const context = browser.contexts()[0];
const page = context.pages()[0];
```

### Test-Fixture (vollstaendig)

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

### Wichtiger Hinweis: User-Data-Directory

WebView2 teilt standardmaessig dasselbe Verzeichnis fuer alle Instanzen.
Fuer parallele Tests muss `WEBVIEW2_USER_DATA_FOLDER` pro Worker eindeutig sein.

<!-- Quellen:
https://playwright.dev/docs/browsers
https://playwright.dev/docs/browser-contexts
https://playwright.dev/docs/pages
https://playwright.dev/docs/chrome-extensions
https://playwright.dev/docs/webview2
https://playwright.dev/docs/api/class-browser
https://playwright.dev/docs/api/class-browsercontext
-->
