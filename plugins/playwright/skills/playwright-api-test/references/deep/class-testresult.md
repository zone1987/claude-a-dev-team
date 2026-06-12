# class-testresult — Playwright TestResult Reference

`TestResult` describes a single execution attempt of a test (one entry in `testCase.results`).
It is also passed live to reporter hooks during a run.

```ts
import { Reporter, TestCase, TestResult } from '@playwright/test/reporter';

class MyReporter implements Reporter {
  onTestEnd(test: TestCase, result: TestResult) {
    console.log(result.status, result.duration);
  }
}
```

---

## Properties

### `annotations`

| Type | Description |
|------|-------------|
| `Array<{ type: string, description?: string, location?: Location }>` | Annotations applicable to this execution — includes those declared statically and those added at runtime via `testInfo.annotations.push(...)` |

---

### `attachments`

| Type | Description |
|------|-------------|
| `Array<{ name: string, contentType: string, path?: string, body?: Buffer }>` | All attachments added during this run via `testInfo.attach()` |

```ts
for (const att of result.attachments) {
  if (att.contentType === 'image/png') {
    uploadScreenshot(att.path!);
  }
}
```

---

### `duration`

| Type | Description |
|------|-------------|
| `number` | Total time this attempt took in milliseconds |

---

### `error`

| Type | Description |
|------|-------------|
| `TestError \| undefined` | First error thrown; shorthand for `errors[0]` |

---

### `errors`

| Type | Description |
|------|-------------|
| `Array<TestError>` | All errors thrown during this execution attempt |

---

### `parallelIndex`

| Type | Description |
|------|-------------|
| `number` | Worker index in the range `[0, workers − 1]`; identifies the slot, not the OS PID |

---

### `retry`

| Type | Description |
|------|-------------|
| `number` | Retry counter: `0` = first run, `1` = first retry, etc. |

---

### `startTime`

| Type | Description |
|------|-------------|
| `Date` | Absolute start time of this execution attempt |

---

### `status`

| Type | Description |
|------|-------------|
| `"passed" \| "failed" \| "timedOut" \| "skipped" \| "interrupted"` | Outcome of this specific execution attempt |

| Value | Meaning |
|-------|---------|
| `"passed"` | Test completed without errors |
| `"failed"` | Test threw an error or assertion failed |
| `"timedOut"` | Test exceeded its timeout |
| `"skipped"` | Test was skipped via `test.skip()` / `testInfo.skip()` |
| `"interrupted"` | Test was interrupted by a signal or `--max-failures` |

---

### `stderr`

| Type | Description |
|------|-------------|
| `Array<string \| Buffer>` | All output written to `process.stderr` during this attempt |

---

### `stdout`

| Type | Description |
|------|-------------|
| `Array<string \| Buffer>` | All output written to `process.stdout` during this attempt |

---

### `steps`

| Type | Description |
|------|-------------|
| `Array<TestStep>` | Top-level steps; each step may have nested `step.steps` children |

```ts
function printSteps(steps: TestStep[], indent = 0) {
  for (const s of steps) {
    console.log(' '.repeat(indent * 2) + s.title, `(${s.duration}ms)`);
    printSteps(s.steps, indent + 1);
  }
}
printSteps(result.steps);
```

---

### `workerIndex`

| Type | Description |
|------|-------------|
| `number` | Unique, stable index of the worker OS process that ran this attempt |

---

## Manifest

| Category | Count |
|----------|-------|
| Properties | 13 |
| Methods | 0 |

**Fazit:** `TestResult` ist das vollstaendige Protokoll eines einzelnen Ausfuehrungs-Versuchs.
Mit `status`, `errors`, `attachments`, `steps` und Timing-Daten hat ein Reporter alle
Informationen, die er benoetigt, um Dashboards, Slack-Nachrichten oder Artefakt-Uploads zu
implementieren.

---

Source: https://playwright.dev/docs/api/class-testresult
