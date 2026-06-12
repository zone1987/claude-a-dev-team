# Playwright Reporter & Annotationen — Vollstaendige Referenz

## Reporter konfigurieren

```typescript
// playwright.config.ts — einzeln
export default defineConfig({ reporter: 'html' });

// Mehrere Reporter
export default defineConfig({
  reporter: [
    ['list'],
    ['json', { outputFile: 'results.json' }],
    ['html', { open: 'never', outputFolder: 'playwright-report' }],
  ],
});

// Umgebungsabhaengig
export default defineConfig({
  reporter: process.env.CI ? 'dot' : 'list',
});
```

CLI-Override: `npx playwright test --reporter=html`

---

## Eingebaute Reporter

### list (Standard lokal)

Eine Zeile pro Test.

```typescript
reporter: [['list', { printSteps: true }]]
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `printSteps` | `boolean` | `false` | Einzelne `test.step()`-Schritte ausgeben |

Umgebungsvariablen: `PLAYWRIGHT_LIST_PRINT_STEPS=1`, `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### line

Kompakter als list; eine Zeile zeigt den letzten fertigen Test.

Umgebungsvariablen: `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### dot (Standard CI)

Eines Zeichen pro Test.

| Zeichen | Bedeutung |
|---|---|
| `.` | bestanden |
| `F` | fehlgeschlagen |
| `x` | fehlgeschlagen/Timeout, wird wiederholt |
| `+` | flaky (erst fehlgeschlagen, dann bestanden) |
| `T` | Timeout |
| `o` | uebersprungen |

Umgebungsvariablen: `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### html

Eigenstaendige HTML-Report-Seite.

```typescript
reporter: [['html', {
  open: 'on-failure',
  outputFolder: 'playwright-report',
  title: 'My Test Report',
  attachmentsBaseURL: 'https://storage.example.com/reports/',
  host: 'localhost',
  port: 9323,
  noCopyPrompt: false,
  noSnippets: false,
  doNotInlineAssets: false,
}]]
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `open` | `'always' \| 'never' \| 'on-failure'` | `'on-failure'` | Wann Report oeffnen |
| `outputFolder` | `string` | `'playwright-report'` | Report-Verzeichnis |
| `title` | `string` | — | Benutzerdefinierter Titel |
| `attachmentsBaseURL` | `string` | — | Externe Storage-URL |
| `host` | `string` | `'localhost'` | Server-Host |
| `port` | `number` | zufaellig | Server-Port |
| `noCopyPrompt` | `boolean` | `false` | Fehler-Copy-Prompt deaktivieren |
| `noSnippets` | `boolean` | `false` | Code-Snippets ausblenden |
| `doNotInlineAssets` | `boolean` | `false` | Assets separat (CSP-Konformitaet) |

```bash
npx playwright show-report
npx playwright show-report my-report
npx playwright show-report report.zip
```

### json

JSON-Ergebnisdatei.

```typescript
reporter: [['json', { outputFile: 'test-results.json' }]]
```

Umgebungsvariablen: `PLAYWRIGHT_JSON_OUTPUT_NAME`, `PLAYWRIGHT_JSON_OUTPUT_DIR`, `PLAYWRIGHT_JSON_OUTPUT_FILE`

### junit

JUnit-kompatibles XML.

```typescript
reporter: [['junit', {
  outputFile: 'results.xml',
  stripANSIControlSequences: true,
  includeProjectInTestName: false,
  suiteId: 'root',
  suiteName: 'playwright',
}]]
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `outputFile` | `string` | — | XML-Ausgabedatei |
| `stripANSIControlSequences` | `boolean` | `false` | ANSI-Sequenzen entfernen |
| `includeProjectInTestName` | `boolean` | `false` | Projektname als Praefix |
| `suiteId` | `string` | — | id-Attribut von testsuites |
| `suiteName` | `string` | — | name-Attribut von testsuites |

Umgebungsvariablen: `PLAYWRIGHT_JUNIT_OUTPUT_NAME`, `PLAYWRIGHT_JUNIT_OUTPUT_DIR`, `PLAYWRIGHT_JUNIT_STRIP_ANSI`, `PLAYWRIGHT_JUNIT_INCLUDE_PROJECT_IN_TEST_NAME`

### blob

Vollstaendige Rohdaten fuer Sharding-Zusammenfuehrung.

```typescript
reporter: [['blob', {
  outputDir: 'blob-report',
  fileName: 'report.zip',
}]]
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `outputDir` | `string` | `'blob-report'` | Ausgabeverzeichnis |
| `fileName` | `string` | `'report-<hash>.zip'` | Dateiname |
| `outputFile` | `string` | — | Voller Pfad (alternativ zu outputDir+fileName) |

```bash
npx playwright merge-reports --reporter html ./all-blob-reports
npx playwright merge-reports --reporter=html,github ./blob-reports
```

### github

GitHub Actions Fehler-Annotationen.

```typescript
reporter: 'github'
```

Nicht empfohlen bei Matrix-Strategien (duplizierte Stack-Traces).

---

## Custom Reporter API

```typescript
// my-reporter.ts
import type {
  Reporter,
  FullConfig,
  Suite,
  TestCase,
  TestResult,
  FullResult,
  TestStep,
  TestError,
} from '@playwright/test/reporter';

class MyReporter implements Reporter {
  onBegin(config: FullConfig, suite: Suite): void {
    console.log(`Tests: ${suite.allTests().length}`);
  }

  onTestBegin(test: TestCase, result: TestResult): void {
    console.log(`Starte: ${test.title}`);
  }

  onStepBegin(test: TestCase, result: TestResult, step: TestStep): void {}
  onStepEnd(test: TestCase, result: TestResult, step: TestStep): void {}

  onTestEnd(test: TestCase, result: TestResult): void {
    console.log(`Ergebnis: ${result.status} (${result.duration}ms)`);
  }

  onError(error: TestError): void {
    console.error(error.message);
  }

  async onEnd(result: FullResult): Promise<void> {
    console.log(`Suite: ${result.status}`);
  }

  async onExit(): Promise<void> {}

  printsToStdio(): boolean { return true; }
}

export default MyReporter;
```

```typescript
// playwright.config.ts
reporter: [['./my-reporter.ts', { myOption: 'value' }]]
```

### TestCase-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `title` | `string` | Test-Titel |
| `titlePath()` | `string[]` | Pfad vom Root |
| `location` | `{ file, line, column }` | Quellort |
| `annotations` | `{ type, description? }[]` | Annotationen |
| `tags` | `string[]` | Tags |
| `timeout` | `number` | Timeout in ms |
| `results` | `TestResult[]` | Alle Versuche |
| `outcome()` | `'skipped' \| 'expected' \| 'unexpected' \| 'flaky'` | Gesamtergebnis |
| `ok()` | `boolean` | Bestanden (incl. flaky) |

### TestResult-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `status` | `'passed' \| 'failed' \| 'timedOut' \| 'skipped' \| 'interrupted'` | Status |
| `duration` | `number` | Dauer in ms |
| `startTime` | `Date` | Startzeit |
| `retry` | `number` | Retry-Nummer |
| `errors` | `TestError[]` | Fehlermeldungen |
| `attachments` | `Attachment[]` | Anhaenge |
| `stdout` | `string[]` | Stdout-Zeilen |
| `stderr` | `string[]` | Stderr-Zeilen |
| `steps` | `TestStep[]` | test.step()-Schritte |

---

## Annotationen

### Eingebaute Annotationen

```typescript
// test.skip
test.skip();
test.skip(browserName === 'firefox', 'reason');

// test.fail
test.fail();
test.fail(browserName === 'webkit', 'reason');

// test.fixme
test.fixme();
test.fixme(isDesktop, 'desktop only');

// test.slow (dreifacher Timeout)
test.slow();
test.slow(isMobile, 'mobile is slow');
```

### test.only

```typescript
test.only('nur dieser Test laeuft im Projekt', async ({ page }) => {});
// Mit --forbid-only bricht CI ab
```

### Tags

```typescript
test('schnell', { tag: '@fast' }, async ({ page }) => {});
test('komplex', { tag: ['@slow', '@smoke'] }, async ({ page }) => {});
// Im Titel (Legacy):
test('example @smoke', async ({ page }) => {});
```

```bash
npx playwright test --grep @fast
npx playwright test --grep "@smoke"
npx playwright test --grep-invert @slow
```

### Strukturierte Annotationen

```typescript
test('mit Issue', {
  annotation: { type: 'issue', description: 'https://github.com/org/repo/issues/123' },
}, async ({ page }) => {});

// Zur Laufzeit
test.info().annotations.push({ type: 'env', description: 'staging' });
```

### test.step()

```typescript
test('checkout', async ({ page }) => {
  await test.step('navigate to shop', async () => {
    await page.goto('/shop');
  });

  const price = await test.step('read price', async () => {
    return page.getByTestId('price').textContent();
  });

  await test.step('add to cart', async () => {
    await page.getByRole('button', { name: 'Add to cart' }).click();
  });
});
```

Steps erscheinen in HTML-Report und Trace Viewer.

### test.info() und Anhaenge

```typescript
test('example', async ({ page }, testInfo) => {
  const info = test.info();   // oder testInfo aus Parameter

  await info.attach('screenshot', {
    body: await page.screenshot(),
    contentType: 'image/png',
  });

  await info.attach('logs', {
    path: './test.log',
    contentType: 'text/plain',
  });
});
```

---

Source: https://playwright.dev/docs/test-reporters | https://playwright.dev/docs/test-annotations
