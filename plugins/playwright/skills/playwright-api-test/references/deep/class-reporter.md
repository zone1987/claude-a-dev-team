# class-reporter — Playwright Reporter API Reference

`Reporter` is the interface to implement for custom test reporters. Create a file that exports
a `default` class (or factory function) implementing some or all of the hook methods.

```ts
// my-reporter.ts
import type { Reporter, FullConfig, Suite, TestCase, TestResult, TestStep, TestError } from '@playwright/test/reporter';

class MyReporter implements Reporter {
  onBegin(config: FullConfig, suite: Suite): void { /* … */ }
  onTestEnd(test: TestCase, result: TestResult): void { /* … */ }
}
export default MyReporter;
```

Register in `playwright.config.ts`:

```ts
reporter: [['./my-reporter.ts', { /* options */ }]]
```

---

## Hook Methods

All methods are optional. Implement only the hooks you need.

---

### `onBegin(config, suite)`

Called once before any test runs. All tests have already been discovered.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `config` | `FullConfig` | yes | Fully resolved configuration |
| `suite` | `Suite` | yes | Root suite containing the entire test tree |

**Returns:** `void`

```ts
onBegin(config, suite) {
  console.log(`Starting ${suite.allTests().length} tests`);
}
```

---

### `onTestBegin(test, result)`

Called when a test starts executing in a worker.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `test` | `TestCase` | yes | The test that has started |
| `result` | `TestResult` | yes | Result object that will be populated as the test runs |

**Returns:** `void`

```ts
onTestBegin(test) {
  console.log(`Starting: ${test.title}`);
}
```

---

### `onStepBegin(test, result, step)`

Called when a test step starts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `test` | `TestCase` | yes | Test containing the step |
| `result` | `TestResult` | yes | Running result |
| `step` | `TestStep` | yes | The step that started |

**Returns:** `void`

```ts
onStepBegin(test, result, step) {
  if (step.category === 'test.step') {
    console.log(`  Step: ${step.title}`);
  }
}
```

---

### `onStepEnd(test, result, step)`

Called when a test step finishes. `step.duration` is now populated.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `test` | `TestCase` | yes | Test containing the step |
| `result` | `TestResult` | yes | Running result |
| `step` | `TestStep` | yes | The step that finished; `step.error` is set if it failed |

**Returns:** `void`

---

### `onTestEnd(test, result)`

Called after a test finishes. `result` is fully populated.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `test` | `TestCase` | yes | The completed test |
| `result` | `TestResult` | yes | Final result with status, errors, attachments, steps |

**Returns:** `void`

```ts
onTestEnd(test, result) {
  if (result.status !== 'passed') {
    notifySlack(`FAIL: ${test.title} — ${result.errors[0]?.message}`);
  }
}
```

---

### `onEnd(result)`

Called after all tests have finished or the run was interrupted.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `result.status` | `"passed" \| "failed" \| "timedout" \| "interrupted"` | yes | Overall run status |
| `result.startTime` | `Date` | yes | When the run started |
| `result.duration` | `number` | yes | Total run duration in ms |

**Returns:** `Promise<{ status?: "passed" \| "failed" \| "timedout" \| "interrupted" } \| void>`

If you return a status, it overrides the exit code.

```ts
async onEnd(result) {
  await uploadReport('report.zip');
  return { status: result.status };
}
```

---

### `onError(error, workerInfo?)`

Called when an error occurs outside of any test (e.g. in a global setup or unhandled rejection
in a worker).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `error` | `TestError` | yes | The error that occurred |
| `workerInfo` | `WorkerInfo` | no | Info about the worker that produced the error |

**Returns:** `void`

`WorkerInfo` shape: `{ config: FullConfig, project: FullProject, parallelIndex: number, workerIndex: number }`

```ts
onError(error) {
  console.error('Unhandled error:', error.message, error.stack);
}
```

---

### `onStdOut(chunk, test?, result?)`

Called when the test (or fixture/hook) writes to `stdout`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `chunk` | `string \| Buffer` | yes | Output data |
| `test` | `TestCase \| undefined` | no | Associated test, if known |
| `result` | `TestResult \| undefined` | no | Associated result, if known |

**Returns:** `void`

```ts
onStdOut(chunk, test) {
  process.stdout.write(chunk);  // pass-through
}
```

---

### `onStdErr(chunk, test?, result?)`

Called when the test (or fixture/hook) writes to `stderr`.

Same signature as `onStdOut`.

**Returns:** `void`

---

### `onExit()`

Called immediately before the test runner exits. All reporters have already received `onEnd`.
Use for last-chance uploads or cleanup.

**Returns:** `Promise<void>`

```ts
async onExit() {
  await s3.upload('report/', 'playwright-report/');
}
```

---

### `printsToStdio()`

Declares whether this reporter writes to the terminal.

**Returns:** `boolean`

- Return `true` if your reporter prints to console (suppresses other stdio reporters in some modes).
- Return `false` if your reporter only writes to files, databases, etc.

```ts
printsToStdio(): boolean {
  return false;
}
```

---

## Custom Reporter with Options

Pass options via the config tuple:

```ts
// playwright.config.ts
reporter: [['./slack-reporter.ts', { webhookUrl: process.env.SLACK_WEBHOOK }]]

// slack-reporter.ts
class SlackReporter implements Reporter {
  constructor(private options: { webhookUrl: string }) {}
  // …
}
```

---

## Manifest

| Category | Count |
|----------|-------|
| Hook methods | 10 (`onBegin`, `onTestBegin`, `onStepBegin`, `onStepEnd`, `onTestEnd`, `onEnd`, `onError`, `onStdOut`, `onStdErr`, `onExit`) |
| Utility methods | 1 (`printsToStdio`) |
| Total | 11 |

**Fazit:** Die Reporter-Schnittstelle deckt den vollstaendigen Lebenszyklus einer Testausfuehrung
ab. Fuer die meisten Integrationen genuegen `onBegin`, `onTestEnd` und `onEnd`. `onStepBegin`/
`onStepEnd` ermoeglicht granulare Step-Level-Metriken. `onExit` ist der richtige Ort fuer
asynchrone Upload-Operationen nach Abschluss aller Berichte.

---

Source: https://playwright.dev/docs/api/class-reporter
