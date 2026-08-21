# Playwright Reporters & Annotations — Complete Reference

## Contents

- [Configuring reporters](#configuring-reporters)
- [Built-in reporters](#built-in-reporters)
- [Custom Reporter API](#custom-reporter-api)
- [Annotations](#annotations)

## Configuring reporters

```typescript
// playwright.config.ts — single
export default defineConfig({ reporter: 'html' });

// Multiple reporters
export default defineConfig({
  reporter: [
    ['list'],
    ['json', { outputFile: 'results.json' }],
    ['html', { open: 'never', outputFolder: 'playwright-report' }],
  ],
});

// Environment-dependent
export default defineConfig({
  reporter: process.env.CI ? 'dot' : 'list',
});
```

CLI override: `npx playwright test --reporter=html`

---

## Built-in reporters

### list (default locally)

One line per test.

```typescript
reporter: [['list', { printSteps: true }]]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `printSteps` | `boolean` | `false` | Print individual `test.step()` steps |

Environment variables: `PLAYWRIGHT_LIST_PRINT_STEPS=1`, `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### line

More compact than list; a single line shows the most recently finished test.

Environment variables: `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### dot (default in CI)

One character per test.

| Character | Meaning |
|---|---|
| `.` | passed |
| `F` | failed |
| `x` | failed/timed out, will be retried |
| `+` | flaky (failed first, then passed) |
| `T` | timeout |
| `o` | skipped |

Environment variables: `PLAYWRIGHT_FORCE_TTY=1`, `FORCE_COLOR=1`

### html

Self-contained HTML report page.

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

| Option | Type | Default | Description |
|---|---|---|---|
| `open` | `'always' \| 'never' \| 'on-failure'` | `'on-failure'` | When to open the report |
| `outputFolder` | `string` | `'playwright-report'` | Report directory |
| `title` | `string` | — | Custom title |
| `attachmentsBaseURL` | `string` | — | External storage URL |
| `host` | `string` | `'localhost'` | Server host |
| `port` | `number` | random | Server port |
| `noCopyPrompt` | `boolean` | `false` | Disable the error copy prompt |
| `noSnippets` | `boolean` | `false` | Hide code snippets |
| `doNotInlineAssets` | `boolean` | `false` | Assets separately (CSP compliance) |

```bash
npx playwright show-report
npx playwright show-report my-report
npx playwright show-report report.zip
```

### json

JSON result file.

```typescript
reporter: [['json', { outputFile: 'test-results.json' }]]
```

Environment variables: `PLAYWRIGHT_JSON_OUTPUT_NAME`, `PLAYWRIGHT_JSON_OUTPUT_DIR`, `PLAYWRIGHT_JSON_OUTPUT_FILE`

### junit

JUnit-compatible XML.

```typescript
reporter: [['junit', {
  outputFile: 'results.xml',
  stripANSIControlSequences: true,
  includeProjectInTestName: false,
  suiteId: 'root',
  suiteName: 'playwright',
}]]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `outputFile` | `string` | — | XML output file |
| `stripANSIControlSequences` | `boolean` | `false` | Strip ANSI sequences |
| `includeProjectInTestName` | `boolean` | `false` | Project name as a prefix |
| `suiteId` | `string` | — | id attribute of testsuites |
| `suiteName` | `string` | — | name attribute of testsuites |

Environment variables: `PLAYWRIGHT_JUNIT_OUTPUT_NAME`, `PLAYWRIGHT_JUNIT_OUTPUT_DIR`, `PLAYWRIGHT_JUNIT_STRIP_ANSI`, `PLAYWRIGHT_JUNIT_INCLUDE_PROJECT_IN_TEST_NAME`

### blob

Complete raw data for merging shards.

```typescript
reporter: [['blob', {
  outputDir: 'blob-report',
  fileName: 'report.zip',
}]]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `outputDir` | `string` | `'blob-report'` | Output directory |
| `fileName` | `string` | `'report-<hash>.zip'` | File name |
| `outputFile` | `string` | — | Full path (alternative to outputDir+fileName) |

```bash
npx playwright merge-reports --reporter html ./all-blob-reports
npx playwright merge-reports --reporter=html,github ./blob-reports
```

### github

GitHub Actions error annotations.

```typescript
reporter: 'github'
```

Not recommended with matrix strategies (duplicated stack traces).

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
    console.log(`Starting: ${test.title}`);
  }

  onStepBegin(test: TestCase, result: TestResult, step: TestStep): void {}
  onStepEnd(test: TestCase, result: TestResult, step: TestStep): void {}

  onTestEnd(test: TestCase, result: TestResult): void {
    console.log(`Result: ${result.status} (${result.duration}ms)`);
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

### TestCase properties

| Property | Type | Description |
|---|---|---|
| `title` | `string` | Test title |
| `titlePath()` | `string[]` | Path from the root |
| `location` | `{ file, line, column }` | Source location |
| `annotations` | `{ type, description? }[]` | Annotations |
| `tags` | `string[]` | Tags |
| `timeout` | `number` | Timeout in ms |
| `results` | `TestResult[]` | All attempts |
| `outcome()` | `'skipped' \| 'expected' \| 'unexpected' \| 'flaky'` | Overall result |
| `ok()` | `boolean` | Passed (including flaky) |

### TestResult properties

| Property | Type | Description |
|---|---|---|
| `status` | `'passed' \| 'failed' \| 'timedOut' \| 'skipped' \| 'interrupted'` | Status |
| `duration` | `number` | Duration in ms |
| `startTime` | `Date` | Start time |
| `retry` | `number` | Retry number |
| `errors` | `TestError[]` | Error messages |
| `attachments` | `Attachment[]` | Attachments |
| `stdout` | `string[]` | Stdout lines |
| `stderr` | `string[]` | Stderr lines |
| `steps` | `TestStep[]` | test.step() steps |

---

## Annotations

### Built-in annotations

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

// test.slow (triple the timeout)
test.slow();
test.slow(isMobile, 'mobile is slow');
```

### test.only

```typescript
test('only this test runs in the project', async ({ page }) => {});
// With --forbid-only, CI aborts
```

### Tags

```typescript
test('fast', { tag: '@fast' }, async ({ page }) => {});
test('complex', { tag: ['@slow', '@smoke'] }, async ({ page }) => {});
// In the title (legacy):
test('example @smoke', async ({ page }) => {});
```

```bash
npx playwright test --grep @fast
npx playwright test --grep "@smoke"
npx playwright test --grep-invert @slow
```

### Structured annotations

```typescript
test('with issue', {
  annotation: { type: 'issue', description: 'https://github.com/org/repo/issues/123' },
}, async ({ page }) => {});

// At runtime
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

Steps appear in the HTML report and the Trace Viewer.

### test.info() and attachments

```typescript
test('example', async ({ page }, testInfo) => {
  const info = test.info();   // or testInfo from the parameter

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
