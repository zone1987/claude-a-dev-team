# class-teststep — Playwright TestStep Reference

`TestStep` represents a single step within a test result. It is available in the Reporter API
via `testResult.steps` and as `step` arguments in `reporter.onStepBegin()` and
`reporter.onStepEnd()`.

Steps are created by `test.step()`, Playwright API calls (`pw:api`), fixture setup/teardown
(`fixture`), hooks (`hook`), assertions (`expect`), and attachments (`test.attach`).

---

## Methods

### `titlePath()`

Returns the full chain of step titles from the root step down to this step.

**Returns:** `Array<string>`

```ts
// reporter usage
onStepEnd(test, result, step) {
  console.log(step.titlePath().join(' > '));
  // e.g. ['Log in', 'Fill username']
}
```

---

## Properties

### `annotations`

| Type | Description |
|------|-------------|
| `Array<{ type: string, description?: string, location?: Location }>` | Annotations attached to this step |

---

### `attachments`

| Type | Description |
|------|-------------|
| `Array<{ name: string, contentType: string, path?: string, body?: Buffer }>` | Files or buffers attached to this step via `testStepInfo.attach()` |

---

### `category`

| Type | Description |
|------|-------------|
| `string` | Step origin classification; used to filter reporter output by verbosity |

Built-in category values:

| Value | Source |
|-------|--------|
| `"test.step"` | `test.step()` calls in test code |
| `"expect"` | Assertion calls like `expect(locator).toBeVisible()` |
| `"pw:api"` | Playwright API actions (`click`, `fill`, `goto`, etc.) |
| `"fixture"` | Fixture setup and teardown |
| `"hook"` | `beforeEach`, `afterAll`, etc. |
| `"test.attach"` | `testInfo.attach()` / `testStepInfo.attach()` calls |

---

### `duration`

| Type | Description |
|------|-------------|
| `number` | Duration of this step in milliseconds |

---

### `error`

| Type | Description |
|------|-------------|
| `TestError \| undefined` | Error thrown during this step, if any |

---

### `location`

| Type | Description |
|------|-------------|
| `Location \| undefined` | Source code location where the step was declared |

`Location` fields: `{ file: string, line: number, column: number }`

---

### `parent`

| Type | Description |
|------|-------------|
| `TestStep \| undefined` | The parent step; `undefined` for top-level steps |

---

### `startTime`

| Type | Description |
|------|-------------|
| `Date` | Absolute start time of this step |

---

### `steps`

| Type | Description |
|------|-------------|
| `Array<TestStep>` | Nested child steps |

---

### `title`

| Type | Description |
|------|-------------|
| `string` | Human-readable step label |

---

## Reporter Usage Example

```ts
import { Reporter, TestCase, TestResult, TestStep } from '@playwright/test/reporter';

class StepLogger implements Reporter {
  onStepEnd(test: TestCase, result: TestResult, step: TestStep) {
    if (step.error) {
      console.error(
        `[FAIL] ${step.titlePath().join(' > ')} (${step.duration}ms)`,
        step.error.message,
      );
    }
  }
}
export default StepLogger;
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 1 (`titlePath`) |
| Properties | 10 (`annotations`, `attachments`, `category`, `duration`, `error`, `location`, `parent`, `startTime`, `steps`, `title`) |

**Fazit:** `TestStep` bildet die Baumstruktur von Test-Aktionen ab. Die `category`-Property
erlaubt Reporter das Filtern nach Abstraktion (API-Calls vs. fachliche Schritte). Ueber
`steps` koennen Reporter die komplette Step-Hierarchie rekursiv traversieren.

---

Source: https://playwright.dev/docs/api/class-teststep
