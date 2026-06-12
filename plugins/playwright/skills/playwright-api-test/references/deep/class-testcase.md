# class-testcase — Playwright TestCase Reference

`TestCase` represents a single test in the Reporter API. It is available in reporter hook
arguments and in `suite.tests` / `suite.allTests()`.

```ts
import { Reporter, TestCase, TestResult } from '@playwright/test/reporter';

class MyReporter implements Reporter {
  onTestEnd(test: TestCase, result: TestResult) {
    console.log(test.title, test.outcome());
  }
}
```

---

## Methods

### `ok()`

Returns whether this test should be considered "passing" from a CI perspective.

**Returns:** `boolean`

- `true` when the test passed, was expected to fail and did fail, or was skipped.
- `false` for unexpected failures, unexpected passes, or timeouts.

```ts
onTestEnd(test, result) {
  if (!test.ok()) {
    process.exitCode = 1;
  }
}
```

---

### `outcome()`

Returns the semantic outcome of all test runs combined (includes retries).

**Returns:** `"skipped" \| "expected" \| "unexpected" \| "flaky"`

| Value | Meaning |
|-------|---------|
| `"expected"` | Test passed (or was expected to fail and did fail) |
| `"unexpected"` | Test failed unexpectedly on all attempts |
| `"flaky"` | Test passed on at least one attempt but failed on another |
| `"skipped"` | Test was skipped |

```ts
if (test.outcome() === 'flaky') {
  metrics.increment('flaky_tests');
}
```

---

### `titlePath()`

Returns the full path of titles from the root down to this test.

**Returns:** `Array<string>`

Elements: `['', projectName, 'path/to/file.spec.ts', 'describe title', 'test title']`
(root is an empty string).

```ts
console.log(test.titlePath().join(' > '));
```

---

## Properties

### `annotations`

| Type | Description |
|------|-------------|
| `Array<{ type: string, description?: string, location?: Location }>` | Annotations from the last test run; includes `fail`, `skip`, `fixme`, and custom annotations |

---

### `expectedStatus`

| Type | Description |
|------|-------------|
| `"passed" \| "failed" \| "timedOut" \| "skipped" \| "interrupted"` | The status this test is expected to reach (e.g. `"failed"` for `test.fail()`) |

---

### `id`

| Type | Description |
|------|-------------|
| `string` | Unique identifier derived from file path, test title, and project name; stable across runs |

---

### `location`

| Type | Description |
|------|-------------|
| `Location` | Source code position: `{ file: string, line: number, column: number }` |

---

### `parent`

| Type | Description |
|------|-------------|
| `Suite` | The suite that directly contains this test |

---

### `repeatEachIndex`

| Type | Description |
|------|-------------|
| `number` | Index when the test runs multiple times via `repeatEach` |

---

### `results`

| Type | Description |
|------|-------------|
| `Array<TestResult>` | One entry per execution attempt; `results[0]` = first run, `results[1]` = first retry, etc. |

```ts
const lastResult = test.results[test.results.length - 1];
```

---

### `retries`

| Type | Description |
|------|-------------|
| `number` | Maximum number of retries configured for this test |

---

### `tags`

| Type | Description |
|------|-------------|
| `Array<string>` | Tags declared via `test('title @tag', …)` or `test('title', { tag: '@tag' }, …)` |

---

### `timeout`

| Type | Description |
|------|-------------|
| `number` | Timeout in ms for this test |

---

### `title`

| Type | Description |
|------|-------------|
| `string` | The title string passed to `test()` |

---

### `type`

| Type | Description |
|------|-------------|
| `"test"` | Constant discriminator; use to distinguish `TestCase` from `Suite` in `suite.entries()` |

```ts
for (const entry of suite.entries()) {
  if (entry.type === 'test') {
    // entry is TestCase
  } else {
    // entry is Suite
  }
}
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 3 (`ok`, `outcome`, `titlePath`) |
| Properties | 12 (`annotations`, `expectedStatus`, `id`, `location`, `parent`, `repeatEachIndex`, `results`, `retries`, `tags`, `timeout`, `title`, `type`) |

**Fazit:** `TestCase` ist die Reporter-Sicht auf einen einzelnen Test. `outcome()` ist die
wichtigste Methode fuer CI-Entscheidungen. `results` enthaelt alle Ausfuehrungs-Instanzen
inklusive Retries mit vollstaendigen Timing- und Fehlerinformationen.

---

Source: https://playwright.dev/docs/api/class-testcase
