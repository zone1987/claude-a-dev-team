# Playwright Intro: Installation, Library, Languages

## Was ist Playwright

Playwright ist ein End-to-End-Testframework fuer moderne Webanwendungen. Es buendelt:
- Test-Runner mit Parallelisierung
- Assertions mit Web-First-Retry
- Isolation ueber BrowserContext
- Tooling: Trace Viewer, UI Mode, Codegen, VS Code Extension

Unterstuetzte Browser-Engines: **Chromium**, **WebKit**, **Firefox** (headless und headed,
native Mobile-Emulation fuer Android Chrome und Mobile Safari).

---

## Systemanforderungen

| Komponente | Anforderung |
|---|---|
| Node.js | 20.x, 22.x oder 24.x |
| Windows | 11+ oder Server 2019+ (inkl. WSL) |
| macOS | 14 (Sonoma) oder neuer |
| Linux | Debian 12/13 oder Ubuntu 22.04/24.04 (x86-64 oder arm64) |

---

## Installation: @playwright/test (empfohlen)

```bash
# npm
npm init playwright@latest

# yarn
yarn create playwright

# pnpm
pnpm create playwright
```

Der interaktive Setup fragt:
- Sprache: TypeScript (Standard) oder JavaScript
- Testverzeichnis (Standard: `tests`)
- GitHub Actions Workflow anlegen
- Browser-Binaries herunterladen

Erzeugte Dateien:
- `playwright.config.ts` — zentrale Konfiguration
- `tests/example.spec.ts` — Beispieltest
- `package.json` / Lock-Dateien

---

## Library-Modus (ohne Test-Runner)

Fuer Skripte ohne `@playwright/test`:

```bash
npm i -D playwright
npx playwright install chromium firefox webkit
```

Oder mit automatischem Browser-Download ueber Helper-Packages:

```bash
npm i -D @playwright/browser-chromium @playwright/browser-firefox @playwright/browser-webkit
```

### Grundstruktur eines Library-Skripts

Alle Playwright-APIs sind asynchron und geben `Promise`-Objekte zurueck.
Empfohlenes Muster: `async/await`.

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

### TypeScript-Unterstuetzung in Library-Skripten

```typescript
// @ts-check  (fuer .js-Dateien)
/** @type {import('playwright').Page} */
let page;
```

### Library vs. @playwright/test

| Merkmal | Library (`playwright`) | Test-Runner (`@playwright/test`) |
|---|---|---|
| Test-Framework | Keins (selbst waehlen) | Integriert |
| Fixtures | Manuell | `page`, `context`, `browser` etc. |
| Assertions | Einfach (kein Retry) | Web-First mit Auto-Retry |
| Parallelisierung | Manuell | Automatisch |
| Isolation | Manuell (`newContext()`) | Automatisch pro Test |
| Trace/Reporting | Manuell konfigurieren | Integriert |

---

## BrowserType.launch() — Alle Optionen

```typescript
const browser = await chromium.launch(options);
// auch: firefox.launch(options), webkit.launch(options)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `headless` | `boolean` | `true` | Headless-Modus; `false` zeigt das Browserfenster |
| `channel` | `string` | — | Browser-Channel: `'chrome'`, `'chrome-beta'`, `'chrome-dev'`, `'chrome-canary'`, `'msedge'`, `'msedge-beta'`, `'msedge-dev'`, `'msedge-canary'`, `'chromium'` |
| `executablePath` | `string` | gebundeltes Binary | Pfad zum Browser-Binary |
| `args` | `string[]` | — | Zus. CLI-Argumente fuer den Browser-Prozess |
| `ignoreDefaultArgs` | `boolean \| string[]` | `false` | Standard-Args deaktivieren (`true` = alle, `string[]` = bestimmte) |
| `proxy` | `object` | — | `{ server, bypass?, username?, password? }` |
| `downloadsPath` | `string` | temp. Verzeichnis | Pfad fuer heruntergeladene Dateien |
| `tracesDir` | `string` | — | Verzeichnis fuer Trace-Dateien |
| `chromiumSandbox` | `boolean` | `false` | Chromium-Sandbox aktivieren |
| `firefoxUserPrefs` | `Record<string, string \| number \| boolean>` | — | Firefox-Benutzereinstellungen |
| `handleSIGINT` | `boolean` | `true` | Browser bei Ctrl+C schliessen |
| `handleSIGTERM` | `boolean` | `true` | Browser bei SIGTERM schliessen |
| `handleSIGHUP` | `boolean` | `true` | Browser bei SIGHUP schliessen |
| `logger` | `Logger` | — | Benutzerdefiniertes Logger-Objekt |
| `timeout` | `number` | `30000` | Max. Zeit fuer Browser-Start in ms |
| `env` | `Record<string, string \| undefined>` | — | Umgebungsvariablen fuer den Browser-Prozess |
| `slowMo` | `number` | — | Verzoegerung in ms zwischen Aktionen (Debugging) |
| `artifactsDir` | `string` | temp. Verzeichnis | Verzeichnis fuer Artefakte |

### Beispiel: Browser sichtbar mit Slow-Motion

```typescript
const browser = await firefox.launch({
  headless: false,
  slowMo: 50,
});
```

---

## Browser.newContext() — Alle Optionen

```typescript
const context = await browser.newContext(options);
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `viewport` | `{ width: number; height: number } \| null` | `1280x720` | Viewport-Groesse; `null` = kein fester Viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | CSS `prefers-color-scheme` Emulation |
| `locale` | `string` | — | Browser-Locale, z.B. `'de-DE'`, `'en-GB'` |
| `timezoneId` | `string` | — | ICU-Timezone-ID, z.B. `'Europe/Berlin'` |
| `geolocation` | `{ latitude: number; longitude: number; accuracy?: number }` | — | GPS-Position |
| `offline` | `boolean` | `false` | Offline-Modus simulieren |
| `proxy` | `{ server: string; bypass?: string; username?: string; password?: string }` | — | Proxy-Konfiguration |
| `httpCredentials` | `{ username: string; password: string; origin?: string; send?: 'always' \| 'unauthorized' }` | — | HTTP-Authentifizierung |
| `extraHTTPHeaders` | `Record<string, string>` | — | Zus. HTTP-Header fuer alle Requests |
| `userAgent` | `string` | — | User-Agent-String |
| `deviceScaleFactor` | `number` | `1` | Geraetepixelverhaeltnis (DPR) |
| `isMobile` | `boolean` | `false` | Mobile-Emulation |
| `hasTouch` | `boolean` | `false` | Touch-Events aktivieren |
| `javaScriptEnabled` | `boolean` | `true` | JavaScript deaktivieren |
| `bypassCSP` | `boolean` | `false` | Content Security Policy umgehen |
| `ignoreHTTPSErrors` | `boolean` | `false` | SSL-Fehler ignorieren |
| `acceptDownloads` | `boolean` | `true` | Downloads akzeptieren |
| `baseURL` | `string` | — | Basis-URL fuer `page.goto()` (relative Pfade) |
| `storageState` | `string \| object` | — | Gespeicherter Auth-Zustand (Pfad oder Objekt) |
| `recordHar` | `object` | — | HAR-Aufnahme konfigurieren |
| `recordVideo` | `object` | — | Video-Aufnahme konfigurieren |
| `permissions` | `string[]` | — | Vorab erteilte Browser-Permissions |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Service Worker steuern |
| `strictSelectors` | `boolean` | `false` | Strikte Selektor-Pruefung (Fehler bei mehreren Matches) |
| `contrast` | `'no-preference' \| 'more' \| 'null'` | — | `prefers-contrast` Emulation |
| `forcedColors` | `'active' \| 'none' \| 'null'` | — | `forced-colors` Emulation |
| `reducedMotion` | `'reduce' \| 'no-preference' \| 'null'` | — | `prefers-reduced-motion` Emulation |
| `screen` | `{ width: number; height: number }` | — | Bildschirmgroesse (unabh. von Viewport) |
| `clientCertificates` | `object[]` | — | Client-Zertifikate fuer mTLS |

### Geraete-Emulation

```typescript
import { chromium, devices } from 'playwright';

const browser = await chromium.launch();
const context = await browser.newContext({
  ...devices['iPhone 15'],
});
const page = await context.newPage();
```

---

## Browser-Lifecycle-Muster

```typescript
import { chromium } from 'playwright';

(async () => {
  // 1. Browser starten
  const browser = await chromium.launch({ headless: false });

  // 2. Isolierten Context erstellen
  const context = await browser.newContext({
    locale: 'de-DE',
    timezoneId: 'Europe/Berlin',
  });

  // 3. Seite oeffnen
  const page = await context.newPage();
  await page.goto('https://example.com');

  // 4. Aktionen ausfuehren
  await page.screenshot({ path: 'screenshot.png' });

  // 5. Ressourcen freigeben (Reihenfolge wichtig)
  await context.close();
  await browser.close();
})();
```

---

## Unterstuetzte Sprachen

| Sprache | Package | Test-Integration |
|---|---|---|
| **JavaScript / TypeScript** | `@playwright/test` | Eigener Test-Runner (Standard) |
| **Python** | `playwright` (pip) | `pytest-playwright`-Plugin (empfohlen) |
| **Java** | `com.microsoft.playwright` | JUnit / TestNG |
| **.NET** | `Microsoft.Playwright` | MSTest / NUnit / xUnit / xUnit v3 |

Alle Sprachen teilen dieselbe Kern-Implementierung und unterstuetzen die gleichen Browser-Automatisierungs-APIs. Das Testing-Ecosystem variiert je Sprache.

---

## Update-Prozess

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

# Version pruefen
npx playwright --version
```

---

## Tests ausfuehren (Schnellreferenz)

```bash
npx playwright test              # Alle Tests (headless, parallel)
npx playwright test --headed     # Browser sichtbar
npx playwright test --ui         # UI-Modus (Watch + Debugger)
npx playwright test --debug      # Inspector-Debugging
npx playwright show-report       # HTML-Report oeffnen
```

<!-- Quellen:
https://playwright.dev/docs/intro
https://playwright.dev/docs/library
https://playwright.dev/docs/languages
https://playwright.dev/docs/api/class-browsertype#browser-type-launch
https://playwright.dev/docs/api/class-browser
-->
