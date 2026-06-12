# Playwright Test Configuration — Vollstaendige Referenz

## Grundstruktur `playwright.config.ts`

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit',   use: { ...devices['Desktop Safari'] } },
  ],
  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

---

## Top-Level-Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `testDir` | `string` | — | Verzeichnis mit Testdateien |
| `testMatch` | `string \| RegExp \| (string \| RegExp)[]` | `**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}` | Glob/Regex-Muster fuer Testdateien |
| `testIgnore` | `string \| RegExp \| (string \| RegExp)[]` | `**/node_modules/**` | Glob/Regex-Muster zum Ignorieren |
| `fullyParallel` | `boolean` | `false` | Alle Tests in allen Dateien parallel ausfuehren |
| `forbidOnly` | `boolean` | `false` | Fehler, wenn `test.only` vorhanden (fuer CI) |
| `retries` | `number` | `0` | Max. Wiederholungsversuche pro Test |
| `workers` | `number \| string` | `undefined` | Parallele Worker-Prozesse; auch Prozentsatz z.B. `'50%'` |
| `timeout` | `number` | `30000` | Timeout pro Test in ms |
| `globalTimeout` | `number` | `0` | Max. Laufzeit der gesamten Test-Suite in ms (0 = kein Limit) |
| `outputDir` | `string` | `'test-results'` | Ordner fuer Artefakte (Screenshots, Videos, Traces) |
| `reporter` | `string \| [string, object][] \| 'dot' \| 'line' \| 'list' \| 'html' \| 'json' \| 'junit' \| 'blob'` | `'list'` | Reporter(n) |
| `globalSetup` | `string` | — | Pfad zu globalem Setup-Modul |
| `globalTeardown` | `string` | — | Pfad zu globalem Teardown-Modul |
| `projects` | `Project[]` | `[]` | Projektdefinitionen |
| `webServer` | `WebServerConfig \| WebServerConfig[]` | — | Webserver-Konfiguration |
| `maxFailures` | `number` | `0` | Stop nach N Fehlern (0 = nie) |
| `preserveOutput` | `'always' \| 'never' \| 'failures-only'` | `'failures-only'` | Wann Artefakte behalten werden |
| `quiet` | `boolean` | `false` | Stdout-Ausgabe unterdruecken |
| `shard` | `{ current: number, total: number } \| null` | `null` | Sharding-Konfiguration |
| `tsconfig` | `string` | — | Expliziter Pfad zur tsconfig |
| `use` | `PlaywrightTestOptions & BrowserContextOptions & LaunchOptions` | `{}` | Geteilte Browser/Context-Optionen |
| `expect` | `ExpectSettings` | — | Assertion-Einstellungen (timeout, toHaveScreenshot, toMatchSnapshot) |
| `snapshotDir` | `string` | `'__snapshots__'` | Basisverzeichnis fuer Snapshots |
| `snapshotPathTemplate` | `string` | — | Template fuer Snapshot-Pfade |
| `metadata` | `object` | — | Freie Metadaten fuer Reporter |
| `updateSnapshots` | `'all' \| 'none' \| 'missing'` | `'missing'` | Snapshot-Update-Verhalten |
| `ignoreSnapshots` | `boolean` | `false` | Screenshot/Snapshot-Assertions ignorieren |

### `expect`-Optionen

```typescript
expect: {
  timeout: 5000,                           // Assertion-Timeout in ms (Default: 5000)
  toHaveScreenshot: {
    maxDiffPixels: 100,                    // Max. Pixel-Unterschiede
    maxDiffPixelRatio: 0.01,              // Max. Anteil abweichender Pixel (0-1)
    threshold: 0.2,                        // Pixelmatch-Schwellenwert (0-1)
    animations: 'disabled',               // Animationen deaktivieren
    caret: 'hide',                         // Cursor ausblenden
    scale: 'css',                          // CSS oder Device-Skalierung
    stylePath: './screenshot.css',         // CSS zum Ueberlagern
  },
  toMatchSnapshot: {
    maxDiffPixels: 100,
    maxDiffPixelRatio: 0.01,
    threshold: 0.2,
  },
},
```

---

## `use`-Optionen (vollstaendig)

### Browser-Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `browserName` | `'chromium' \| 'firefox' \| 'webkit'` | `'chromium'` | Browser-Engine |
| `channel` | `string` | — | Browser-Channel: `'chrome'`, `'chrome-beta'`, `'msedge'`, `'msedge-beta'` |
| `headless` | `boolean` | `true` | Headless-Modus |
| `launchOptions` | `object` | `{}` | Alle `browserType.launch()`-Optionen (slowMo, devtools, executablePath …) |
| `connectOptions` | `object` | `{}` | Alle `browserType.connect()`-Optionen |
| `screenshot` | `'off' \| 'on' \| 'only-on-failure'` | `'off'` | Screenshots automatisch aufnehmen |
| `trace` | `'off' \| 'on' \| 'retain-on-failure' \| 'on-first-retry' \| 'on-all-retries'` | `'off'` | Trace-Aufnahme |
| `video` | `'off' \| 'on' \| 'retain-on-failure' \| 'on-first-retry'` | `'off'` | Video-Aufnahme |

### Browser-Context-Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `baseURL` | `string` | — | Basis-URL fuer `page.goto('/')` |
| `storageState` | `string \| object` | — | Storage State (Auth, Cookies) |
| `viewport` | `{ width: number, height: number } \| null` | `{ width: 1280, height: 720 }` | Viewport-Groesse; `null` = kein fester Viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | prefers-color-scheme emulieren |
| `geolocation` | `{ longitude: number, latitude: number, accuracy?: number }` | — | Geoposition |
| `locale` | `string` | — | Browser-Locale z.B. `'de-DE'` |
| `timezoneId` | `string` | — | Zeitzone z.B. `'Europe/Berlin'` |
| `permissions` | `string[]` | `[]` | Browser-Permissions: `'geolocation'`, `'notifications'` … |
| `acceptDownloads` | `boolean` | `true` | Downloads automatisch akzeptieren |
| `bypassCSP` | `boolean` | `false` | Content-Security-Policy umgehen |
| `extraHTTPHeaders` | `Record<string, string>` | `{}` | Zusaetzliche HTTP-Header |
| `httpCredentials` | `{ username: string, password: string }` | — | HTTP Basic Auth |
| `ignoreHTTPSErrors` | `boolean` | `false` | HTTPS-Fehler ignorieren |
| `javaScriptEnabled` | `boolean` | `true` | JavaScript im Browser |
| `offline` | `boolean` | `false` | Offline-Modus emulieren |
| `proxy` | `{ server: string, bypass?: string, username?: string, password?: string }` | — | Proxy-Einstellungen |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Service Workers zulassen/blockieren |
| `userAgent` | `string` | — | User-Agent-String |
| `deviceScaleFactor` | `number` | — | Device Pixel Ratio |
| `hasTouch` | `boolean` | `false` | Touch-Events emulieren |
| `isMobile` | `boolean` | `false` | Mobile-Modus |
| `contextOptions` | `object` | `{}` | Alle `browser.newContext()`-Optionen |

### Timeout-Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `actionTimeout` | `number` | `0` | Max. Dauer fuer Aktionen (click, fill …) in ms |
| `navigationTimeout` | `number` | `0` | Max. Dauer fuer Navigation in ms |

### Test-ID-Option

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `testIdAttribute` | `string` | `'data-testid'` | HTML-Attribut fuer `getByTestId()` |

---

## `webServer`-Konfiguration

```typescript
webServer: {
  command: 'npm run start',          // (required) Shell-Befehl zum Starten
  url: 'http://localhost:3000',      // (required) URL, die 2xx/3xx/4xx zurueckgibt
  cwd: '.',                          // Arbeitsverzeichnis (Default: config-Verzeichnis)
  env: { NODE_ENV: 'test' },         // Zusaetzliche Env-Variablen
  timeout: 60000,                    // Wartezeit in ms (Default: 60000)
  reuseExistingServer: true,         // Vorhandenen Server wiederverwenden
  stdout: 'pipe',                    // 'pipe' | 'ignore' (Default: 'ignore')
  stderr: 'pipe',                    // 'pipe' | 'ignore' (Default: 'pipe')
  name: 'Frontend',                  // Anzeigename fuer Logs
  ignoreHTTPSErrors: false,          // HTTPS-Fehler ignorieren
  gracefulShutdown: {                // Sanftes Beenden
    signal: 'SIGTERM',
    timeout: 5000,
  },
  wait: {                            // Auf bestimmte Ausgabe warten
    regex: /Server started/,
  },
}
```

Mehrere Server als Array:

```typescript
webServer: [
  { command: 'npm run frontend', url: 'http://localhost:3000', name: 'Frontend' },
  { command: 'npm run backend',  url: 'http://localhost:3333', name: 'Backend' },
]
```

---

## Projects-Konfiguration

### Mehrere Browser

```typescript
projects: [
  { name: 'chromium',      use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox',       use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit',        use: { ...devices['Desktop Safari'] } },
  { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } },
  { name: 'Mobile Safari', use: { ...devices['iPhone 12'] } },
  { name: 'Edge',          use: { ...devices['Desktop Edge'], channel: 'msedge' } },
  { name: 'Chrome',        use: { ...devices['Desktop Chrome'], channel: 'chrome' } },
],
```

### Project-Optionen

| Option | Typ | Beschreibung |
|---|---|---|
| `name` | `string` | Eindeutiger Projektname |
| `use` | `object` | Alle `use`-Optionen; ueberschreibt globale `use` |
| `testDir` | `string` | Testverzeichnis fuer dieses Projekt |
| `testMatch` | `string \| RegExp` | Testdatei-Filter fuer dieses Projekt |
| `testIgnore` | `string \| RegExp` | Ignorier-Muster fuer dieses Projekt |
| `retries` | `number` | Wiederholungen fuer dieses Projekt |
| `timeout` | `number` | Test-Timeout fuer dieses Projekt |
| `fullyParallel` | `boolean` | Vollparallelisierung fuer dieses Projekt |
| `dependencies` | `string[]` | Projekte, die vorher laufen muessen |
| `teardown` | `string` | Projekt-Name fuer Teardown nach diesem Projekt |
| `metadata` | `object` | Freie Metadaten |
| `snapshotDir` | `string` | Snapshot-Verzeichnis fuer dieses Projekt |

### Project Dependencies (Setup/Teardown)

```typescript
projects: [
  {
    name: 'setup',
    testMatch: /global\.setup\.ts/,
    teardown: 'cleanup',             // laeuft nach allen abhaengigen Projekten
  },
  {
    name: 'cleanup',
    testMatch: /global\.teardown\.ts/,
  },
  {
    name: 'chromium',
    use: { ...devices['Desktop Chrome'] },
    dependencies: ['setup'],         // wartet auf 'setup'
  },
],
```

**Ausfuehrungsreihenfolge:**
1. `setup`-Projekt laeuft vollstaendig
2. Bei Erfolg: abhaengige Projekte parallel
3. Danach: `teardown`-Projekt (wenn konfiguriert)
4. Bei Fehler im Setup: abhaengige Projekte werden uebersprungen

`--no-deps` ignoriert Dependencies (nur direkt ausgewaehlte Projekte).

---

## TypeScript-Setup

### Automatische Erkennung

Playwright erkennt `tsconfig.json` / `jsconfig.json` automatisch (Directory-Traversal aufwaerts).

### Unterstuetzte tsconfig-Optionen

| Option | Beschreibung |
|---|---|
| `allowJs` | JS-Dateien erlauben |
| `baseUrl` | Basis-URL fuer Module |
| `paths` | Pfad-Aliase |
| `references` | Projekt-Referenzen |

### Pfad-Aliase

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@helpers/*": ["src/helpers/*"],
      "@fixtures/*": ["tests/fixtures/*"]
    }
  }
}
```

```typescript
// Test-Datei
import { myHelper } from '@helpers/utils';
```

### Explizite tsconfig

```typescript
// playwright.config.ts
export default defineConfig({
  tsconfig: './tsconfig.test.json',
});
```

Oder CLI: `npx playwright test --tsconfig=tsconfig.test.json`

### Type-Checking parallel

```bash
# Typ-Check ohne Ausfuehren
npx tsc -p tsconfig.json --noEmit

# Watch-Modus
npx tsc -p tsconfig.json --noEmit -w
```

Playwright fuehrt Tests auch bei TS-Fehlern aus (keine Blockierung).

---

Source: https://playwright.dev/docs/test-configuration | https://playwright.dev/docs/test-use-options | https://playwright.dev/docs/test-projects | https://playwright.dev/docs/test-typescript
