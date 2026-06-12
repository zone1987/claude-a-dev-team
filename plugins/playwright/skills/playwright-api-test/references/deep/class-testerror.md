# class-testerror — Playwright TestError Reference

`TestError` is the error type used in the **Reporter API**. It is available as
`testResult.error`, elements of `testResult.errors`, `testStep.error`, and as the argument to
`reporter.onError()`.

`TestError` differs from `TestInfoError` (which is used inside running tests via `testInfo`)
in that `TestError` carries additional reporter-centric fields like `location` and `snippet`.

---

## Properties

### `cause`

| Type | Added | Description |
|------|-------|-------------|
| `TestError \| undefined` | v1.49 | The underlying cause error, if the thrown `Error` had a `.cause` property that was itself an `Error` instance |

```ts
onError(error) {
  if (error.cause) {
    console.log('Caused by:', error.cause.message);
  }
}
```

---

### `location`

| Type | Added | Description |
|------|-------|-------------|
| `Location \| undefined` | v1.30 | Source code location where the error occurred: `{ file: string, line: number, column: number }` |

---

### `message`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | Error message. Set when an `Error` (or subclass) was thrown. |

---

### `snippet`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.33 | Source code snippet with the error line highlighted, as shown in the terminal output |

```ts
onTestEnd(test, result) {
  if (result.error?.snippet) {
    console.log(result.error.snippet);
  }
}
```

---

### `stack`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | Full stack trace. Set when an `Error` (or subclass) was thrown. |

---

### `value`

| Type | Added | Description |
|------|-------|-------------|
| `string \| undefined` | v1.10 | Stringified thrown value when something other than an `Error` was thrown |

---

## Comparison: TestError vs. TestInfoError

| Property | `TestError` (Reporter) | `TestInfoError` (Runtime) |
|----------|------------------------|---------------------------|
| `message` | yes | yes |
| `stack` | yes | yes |
| `value` | yes | yes |
| `cause` | yes (v1.49) | yes (v1.49) |
| `location` | yes (v1.30) | no |
| `snippet` | yes (v1.33) | no |
| `errorContext` | no | yes (v1.60) |

---

## Usage Example

```ts
import { Reporter, TestCase, TestResult, TestError } from '@playwright/test/reporter';

class ErrorReporter implements Reporter {
  onError(error: TestError) {
    // global error (outside any test)
    console.error('Global error:', error.message);
    if (error.location) {
      console.error(`  at ${error.location.file}:${error.location.line}`);
    }
  }

  onTestEnd(test: TestCase, result: TestResult) {
    for (const err of result.errors) {
      console.error(`Test "${test.title}" failed:`, err.message);
      if (err.snippet) console.error(err.snippet);
    }
  }
}
export default ErrorReporter;
```

---

## Manifest

| Category | Count |
|----------|-------|
| Properties | 6 (`cause`, `location`, `message`, `snippet`, `stack`, `value`) |
| Methods | 0 |

**Fazit:** `TestError` erweitert `TestInfoError` um `location` und `snippet` — die
reporter-spezifischen Properties fuer Quelltextanzeige. `snippet` ist besonders nuetzlich
fuer angereicherte Fehlerausgaben in CI-Logs oder Notification-Systemen.

---

Source: https://playwright.dev/docs/api/class-testerror
