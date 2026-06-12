# Playwright Test-Ausfuehrung — Vollstaendige Referenz

## CLI-Grundbefehle

```bash
# Alle Tests
npx playwright test

# Bestimmte Datei(en)
npx playwright test landing-page.spec.ts
npx playwright test tests/todo/ tests/login/

# Nach Dateinamen-Stichwort
npx playwright test landing login         # Dateien mit "landing" ODER "login"

# Nach Test-Titel (Regex)
npx playwright test -g "add a todo item"

# Nur zuletzt fehlgeschlagene Tests
npx playwright test --last-failed

# Zeilenangabe (bestimmter Test)
npx playwright test example.spec.ts:10

# Report anzeigen
npx playwright show-report
```

---

## Alle CLI-Flags (`npx playwright test`)

| Flag | Kurz | Typ | Beschreibung |
|---|---|---|---|
| `--debug` | | boolean | Playwright Inspector oeffnen (Schritt-fuer-Schritt) |
| `--headed` | | boolean | Tests im sichtbaren Browser-Fenster ausfuehren |
| `--ui` | | boolean | Interaktiver UI-Modus |
| `--ui-host` | | string | Host fuer UI-Server (Default: localhost; `0.0.0.0` fuer Docker) |
| `--ui-port` | | number | Port fuer UI-Server (0 = zufaellig) |
| `--grep` | `-g` | string (Regex) | Nur Tests, deren Titel zum Regex passen |
| `--grep-invert` | | string (Regex) | Tests AUSSCHLIESSEN, die dem Regex entsprechen |
| `--workers` | `-j` | number \| `'N%'` | Anzahl paralleler Worker (z.B. `4` oder `'50%'`) |
| `--project` | | string[] | Nur Tests aus diesem Projekt ausfuehren |
| `--config` | `-c` | Dateipfad | Konfigurationsdatei oder Testverzeichnis |
| `--fail-on-flaky-tests` | | boolean | Fehler wenn ein Test als "flaky" markiert wird |
| `--forbid-only` | | boolean | Fehler bei `test.only` (fuer CI) |
| `--fully-parallel` | | boolean | Alle Tests parallel |
| `--global-timeout` | | ms | Max. Laufzeit der gesamten Suite |
| `--ignore-snapshots` | | boolean | Screenshot/Snapshot-Assertions ignorieren |
| `--last-failed` | | boolean | Nur zuvor fehlgeschlagene Tests |
| `--list` | | boolean | Tests auflisten ohne Ausfuehren |
| `--max-failures` | `-x` | number | Nach N Fehlern abbrechen |
| `--no-deps` | | boolean | Projekt-Dependencies ignorieren |
| `--only-changed` | | ref? | Nur geaenderte Testdateien seit ref/HEAD |
| `--output` | | Verzeichnis | Ordner fuer Artefakte |
| `--pass-with-no-tests` | | boolean | Erfolg auch wenn keine Tests gefunden |
| `--quiet` | | boolean | Stdout unterdruecken |
| `--repeat-each` | | number | Jeden Test N-mal ausfuehren |
| `--reporter` | | string | Reporter (dot, line, list, html, json, junit, blob) |
| `--retries` | | number | Max. Wiederholungsversuche |
| `--shard` | | `N/M` | Shard N von M (1-basiert) |
| `--test-list` | | Dateipfad | Datei mit auszufuehrenden Tests |
| `--test-list-invert` | | Dateipfad | Datei mit zu ueberspringenden Tests |
| `--timeout` | | ms | Test-Timeout |
| `--trace` | | mode | Trace-Modus (on, off, on-first-retry, retain-on-failure) |
| `--tsconfig` | | Dateipfad | TypeScript-Konfiguration |
| `--update-snapshots` | `-u` | `all \| changed \| missing` | Snapshots aktualisieren |
| `--update-source-method` | | `patch \| 3way \| overwrite` | Snapshot-Update-Methode |

### Weitere Unterbefehle

```bash
# Installationen
npx playwright install [browser...]          # Browser installieren
npx playwright install --with-deps chromium  # inkl. Systemabhaengigkeiten

# Reports zusammenfuehren
npx playwright merge-reports ./blob-reports --reporter html

# Trace anzeigen
npx playwright show-trace trace.zip

# Code generieren
npx playwright codegen https://example.com

# Cache leeren
npx playwright clear-cache
```

---

## Parallelitaet

### Standard-Verhalten

- Test-Dateien werden standardmaessig parallel ausgefuehrt (eine Datei pro Worker)
- Tests INNERHALB einer Datei laufen sequenziell im selben Worker

### Worker konfigurieren

```typescript
// playwright.config.ts
export default defineConfig({
  workers: process.env.CI ? 2 : undefined,  // undefined = automatisch (Anzahl CPU-Kerne)
});
```

```bash
npx playwright test --workers 4
npx playwright test --workers=50%   # 50% der CPUs
npx playwright test --workers=1     # komplett sequenziell
```

### `fullyParallel` — Tests innerhalb einer Datei parallelisieren

```typescript
// Global
export default defineConfig({ fullyParallel: true });

// Per Projekt
projects: [{ name: 'chromium', fullyParallel: true }],
```

```typescript
// Per Datei
import { test } from '@playwright/test';
test.describe.configure({ mode: 'parallel' });
```

### `serial` — Abhaengige Tests in Reihe

```typescript
test.describe.configure({ mode: 'serial' });

test('schritt 1', async ({ page }) => { /* ... */ });
test('schritt 2', async ({ page }) => { /* ... */ });
// Schritt 2 wird uebersprungen wenn Schritt 1 fehlschlaegt (ohne retries)
```

### Selektiv aus fullyParallel ausnehmen

```typescript
test.describe('sequenziell', () => {
  test.describe.configure({ mode: 'default' });
  test('in order 1', async ({ page }) => { /* ... */ });
  test('in order 2', async ({ page }) => { /* ... */ });
});
```

### Worker-Identifikation

```typescript
// In Fixtures/Tests:
testInfo.workerIndex       // 0 bis (maxWorkers - 1)
testInfo.parallelIndex     // 0 bis (aktive Worker - 1)

// Umgebungsvariablen (auch in globalSetup):
process.env.TEST_WORKER_INDEX
process.env.TEST_PARALLEL_INDEX
```

### Fehler limitieren

```typescript
export default defineConfig({
  maxFailures: process.env.CI ? 10 : undefined,
});
```

---

## Sharding

Verteilt Tests auf mehrere Maschinen:

```bash
# Auf 4 Maschinen (jeweils ein Shard):
npx playwright test --shard=1/4
npx playwright test --shard=2/4
npx playwright test --shard=3/4
npx playwright test --shard=4/4
```

**Granularitaet:**
- Mit `fullyParallel: true`: Sharding auf Test-Ebene (gleichmaessigere Verteilung)
- Ohne: Sharding auf Datei-Ebene

### Reports aus Shards zusammenfuehren

```typescript
// playwright.config.ts
export default defineConfig({
  reporter: process.env.CI ? 'blob' : 'html',
});
```

```bash
# Alle Blob-Reports sammeln, dann:
npx playwright merge-reports --reporter html ./all-blob-reports
```

### GitHub Actions Beispiel

```yaml
strategy:
  matrix:
    shardIndex: [1, 2, 3, 4]
    shardTotal: [4]
steps:
  - run: npx playwright test --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}
  - uses: actions/upload-artifact@v4
    with:
      name: blob-report-${{ matrix.shardIndex }}
      path: blob-report

# Nach allen Shards: merge job
merge-reports:
  needs: test
  steps:
    - uses: actions/download-artifact@v4
      with:
        path: all-blob-reports
        pattern: blob-report-*
        merge-multiple: true
    - run: npx playwright merge-reports --reporter html ./all-blob-reports
```

---

## Retries

### Konfiguration

```typescript
// playwright.config.ts
export default defineConfig({ retries: 2 });

// Per Projekt
projects: [{ name: 'ci', retries: 2 }],
```

```bash
npx playwright test --retries=3
```

```typescript
// Per Test-Gruppe
test.describe.configure({ retries: 2 });
```

### Test-Status mit Retries

| Status | Bedeutung |
|---|---|
| `passed` | Im ersten Versuch bestanden |
| `flaky` | Im ersten Versuch fehlgeschlagen, dann bestanden |
| `failed` | In allen Versuchen fehlgeschlagen |

### `testInfo.retry` — Retry erkennen

```typescript
test('example', async ({ page }, testInfo) => {
  if (testInfo.retry > 0) {
    // Beim Retry: Cache/State zuruecksetzen
    await page.context().clearCookies();
  }
  // ...
});
```

Auch in Fixtures verfuegbar:

```typescript
myFixture: async ({}, use, testInfo) => {
  if (testInfo.retry) {
    await cleanupFromPreviousAttempt();
  }
  await use(value);
}
```

### Worker-Verhalten bei Fehlschlag

Nach einem fehlgeschlagenen Test: Worker-Prozess und Browser werden verworfen.
Neuer Worker startet fuer den Retry-Versuch.

### serial + retries

Bei `test.describe.configure({ mode: 'serial' })` und aktivierten Retries:
Alle Tests der Gruppe werden gemeinsam wiederholt.

---

## Timeouts

### Uebersicht aller Timeout-Typen

| Typ | Default | Gilt fuer | Konfiguration |
|---|---|---|---|
| Test-Timeout | 30.000 ms | Test-Funktion + Fixture-Setup + beforeEach | `timeout` in Config |
| Expect-Timeout | 5.000 ms | Auto-retrying Assertions | `expect.timeout` in Config |
| Action-Timeout | 0 (kein Limit) | click, fill, hover etc. | `use.actionTimeout` |
| Navigation-Timeout | 0 (kein Limit) | page.goto, page.waitForURL etc. | `use.navigationTimeout` |
| Global-Timeout | 0 (kein Limit) | Gesamte Test-Suite | `globalTimeout` in Config |
| Fixture-Timeout | (wie Test) | Einzelnes Fixture | `{ timeout }` in extend |
| beforeAll/afterAll | 30.000 ms | Hook-Funktion | `test.setTimeout()` im Hook |

### Test-Timeout

```typescript
// Global
export default defineConfig({ timeout: 120_000 });

// Per Test
test('slow test', async ({ page }) => {
  test.setTimeout(120_000);
});

// test.slow() = dreifacher Timeout
test('very slow test', async ({ page }) => {
  test.slow();
});

// Aus beforeEach
test.beforeEach(async ({ page }, testInfo) => {
  testInfo.setTimeout(testInfo.timeout + 30_000);
});
```

### Expect-Timeout

```typescript
// Global
export default defineConfig({
  expect: { timeout: 10_000 },
});

// Per Assertion
await expect(locator).toHaveText('hello', { timeout: 10_000 });

// Vorkonfiguriert
const slowExpect = expect.configure({ timeout: 30_000 });
await slowExpect(locator).toBeVisible();
```

### Action-Timeout

```typescript
// Global
export default defineConfig({
  use: { actionTimeout: 10_000 },
});

// Per Aktion
await page.getByRole('button').click({ timeout: 10_000 });
```

### Navigation-Timeout

```typescript
// Global
export default defineConfig({
  use: { navigationTimeout: 30_000 },
});

// Per Navigation
await page.goto('https://example.com', { timeout: 30_000 });
```

### Global-Timeout

```typescript
export default defineConfig({
  globalTimeout: 60 * 60 * 1000,  // 1 Stunde
});
```

```bash
npx playwright test --global-timeout=3600000
```

### Fixture-Timeout

```typescript
const test = base.extend({
  slowFixture: [async ({}, use) => {
    await heavyOperation();
    await use('result');
  }, { timeout: 120_000, scope: 'worker' }],
});
```

---

## UI-Modus

```bash
npx playwright test --ui
# Docker / GitHub Codespaces:
npx playwright test --ui-host=0.0.0.0 --ui-port=8080
```

**Features:**
- Timeline mit Aktionen und DOM-Snapshots (Time Travel)
- Vor/Nach-Ansicht fuer jede Aktion
- Locator-Picker zum Verifizieren von Selektoren
- Watch-Modus: Auto-Rerun bei Code-Aenderungen
- Tabs: Call, Log, Errors, Console, Network, Attachments, Metadata
- "Open in VSCode" fuer direkten Code-Sprung

**Sicherheit:** Bei `--ui-host=0.0.0.0` sind Traces inkl. Passworten fuer andere Netzwerkteilnehmer zugaenglich.

---

## webServer

Komplette Konfiguration — siehe auch `playwright-test-config`:

```typescript
webServer: {
  command: 'npm run start',
  url: 'http://localhost:3000',
  reuseExistingServer: !process.env.CI,
  timeout: 120_000,
  env: { NODE_ENV: 'test' },
  stdout: 'pipe',
  stderr: 'pipe',
},
use: {
  baseURL: 'http://localhost:3000',
},
```

Mit `baseURL` koennen Tests relative Pfade verwenden: `await page.goto('/login')`

---

Source: https://playwright.dev/docs/running-tests | https://playwright.dev/docs/test-cli | https://playwright.dev/docs/test-parallel | https://playwright.dev/docs/test-sharding | https://playwright.dev/docs/test-retries | https://playwright.dev/docs/test-timeouts | https://playwright.dev/docs/test-ui-mode | https://playwright.dev/docs/test-webserver
