# class-test — Playwright Test Runner API

The global `test` object (also importable as `{ test }` from `@playwright/test`) is the primary
entry point for declaring tests, hooks, steps, fixtures and modifiers.

---

## 1. Declaring a Test

### `test(title, body)`

Declares a single test case.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | yes | Human-readable test name |
| `body` | `(fixtures: Fixtures, testInfo: TestInfo) => Promise<void>` | yes | Async test function |

```ts
import { test, expect } from '@playwright/test';

test('basic navigation', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

### `test(title, details, body)`

Declares a test with annotations and tags.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | yes | Test name |
| `details` | `TestDetails` | yes | Object with `tag` and/or `annotation` |
| `details.tag` | `string \| string[]` | no | One or more tag strings (e.g. `'@smoke'`) |
| `details.annotation` | `Annotation \| Annotation[]` | no | `{ type: string, description?: string }` |
| `body` | `(fixtures, testInfo) => Promise<void>` | yes | Async test function |

```ts
test('login smoke', {
  tag: ['@smoke', '@auth'],
  annotation: { type: 'issue', description: 'https://github.com/org/repo/issues/42' },
}, async ({ page }) => {
  await page.goto('/login');
});
```

---

## 2. Hooks

All hooks accept an optional `title` as first argument (named hooks) or just the function.

### `test.beforeAll(hookFunction)`
### `test.beforeAll(title, hookFunction)`

Runs once per worker before all tests in the file/describe block.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | no | Name shown in reports |
| `hookFunction` | `(fixtures, workerInfo) => Promise<void>` | yes | Hook body |

```ts
test.beforeAll(async ({ browser }) => {
  // shared setup — runs once per worker
});
```

### `test.afterAll(hookFunction)`
### `test.afterAll(title, hookFunction)`

Runs once per worker after all tests in the file/describe block.

Same signature as `beforeAll`.

```ts
test.afterAll(async () => {
  await globalDb.disconnect();
});
```

### `test.beforeEach(hookFunction)`
### `test.beforeEach(title, hookFunction)`

Runs before each individual test. Receives the full fixture set.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | no | Hook label in report |
| `hookFunction` | `(fixtures, testInfo) => Promise<void>` | yes | Hook body |

```ts
test.beforeEach(async ({ page }) => {
  await page.goto('/');
});
```

### `test.afterEach(hookFunction)`
### `test.afterEach(title, hookFunction)`

Runs after each test, even on failure. Same signature as `beforeEach`.

```ts
test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== 'passed') {
    await page.screenshot({ path: testInfo.outputPath('screenshot.png') });
  }
});
```

---

## 3. Modifiers — Annotations

### `test.skip()`  (inside test body)

Skips the currently running test immediately.

```ts
test('conditional skip', async ({ browserName }) => {
  test.skip(browserName === 'firefox', 'Not supported in Firefox');
  // rest of test
});
```

Overloads:

| Signature | Description |
|-----------|-------------|
| `test.skip()` | Unconditional skip |
| `test.skip(condition)` | Skip when `condition === true` |
| `test.skip(condition, description)` | Skip with message |

### `test.skip(title, body)` — declaration form

Declares a test that is never executed.

```ts
test.skip('not yet implemented', async ({ page }) => { /* skipped */ });
```

### `test.fixme()`  (inside test body)

Marks test as fixme; aborts execution immediately.

| Signature | Description |
|-----------|-------------|
| `test.fixme()` | Unconditional fixme |
| `test.fixme(condition)` | Fixme when condition is true |
| `test.fixme(condition, description)` | Fixme with message |

```ts
test.fixme('broken upstream', async ({ page }) => { /* aborted */ });
```

### `test.fail()`  (inside test body)

Marks the test as "expected to fail". If the test passes, it is reported as unexpected.

| Signature | Description |
|-----------|-------------|
| `test.fail()` | Unconditional expected-failure |
| `test.fail(condition)` | Expected-failure when condition is true |
| `test.fail(condition, description)` | Expected-failure with message |

```ts
test('expected failure', async ({ page }) => {
  test.fail(true, 'Bug #123 still open');
  // test body that currently fails
});
```

### `test.slow()`  (inside test body)

Triples the default timeout for the current test.

| Signature | Description |
|-----------|-------------|
| `test.slow()` | Always triple timeout |
| `test.slow(condition)` | Triple timeout when condition is true |
| `test.slow(condition, description)` | Triple timeout with message |

```ts
test('heavy computation', async ({ page }) => {
  test.slow();
  // up to 3 × default timeout
});
```

---

## 4. Focus Modifiers

### `test.only(title, body)`
### `test.only(title, details, body)`

Declares a focused test. Only focused tests (and tests in focused describe blocks) run.

```ts
test.only('debug this one', async ({ page }) => {
  // only this test runs
});
```

### `test.fail.only(title, body)`

Focused test expected to fail.

```ts
test.fail.only('flaky check', async ({ page }) => { /* must fail */ });
```

---

## 5. Test Organization — `test.describe`

### `test.describe(title, callback)`

Groups tests; hooks and `test.use()` inside apply only to the group.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | yes | Suite name |
| `callback` | `() => void` | yes | Synchronous block declaring tests |

```ts
test.describe('Dashboard', () => {
  test('loads', async ({ page }) => { /* … */ });
  test('shows stats', async ({ page }) => { /* … */ });
});
```

### `test.describe(callback)`

Anonymous describe — useful to scope `test.use()` without a title.

```ts
test.describe(() => {
  test.use({ colorScheme: 'dark' });
  test('dark mode test', async ({ page }) => { /* … */ });
});
```

### `test.describe(title, details, callback)`

Describe with annotations/tags.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | yes | Suite name |
| `details` | `TestDetails` | yes | `{ tag?, annotation? }` |
| `callback` | `() => void` | yes | Suite body |

### `test.describe.only(title, callback)`

Focused describe block — only this block and other focused blocks run.

### `test.describe.skip(title, callback)`

Skips all tests in the group.

### `test.describe.fixme(title, callback)`

Marks all tests in the group as fixme.

### `test.describe.configure(options)`

Configures execution mode and timing for the enclosing group.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `mode` | `"default" \| "parallel" \| "serial"` | `"default"` | Test execution order within group |
| `retries` | `number` | — | Per-test retry count |
| `timeout` | `number` | — | Per-test timeout in ms |

```ts
test.describe.configure({ mode: 'serial', retries: 1 });
```

### Deprecated describe variants

| Method | Replacement |
|--------|-------------|
| `test.describe.parallel(title, cb)` | `test.describe.configure({ mode: 'parallel' })` |
| `test.describe.parallel.only(title, cb)` | focused + parallel configure |
| `test.describe.serial(title, cb)` | `test.describe.configure({ mode: 'serial' })` |
| `test.describe.serial.only(title, cb)` | focused + serial configure |

---

## 6. Steps

### `test.step(title, body)`
### `test.step(title, body, options)`

Declares a named step shown in reports and traces.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | `string` | yes | Step label |
| `body` | `(stepInfo: TestStepInfo) => Promise<T>` | yes | Step implementation |
| `options.box` | `boolean` | no | When true, errors point to the `step()` call site rather than inside the step |
| `options.timeout` | `number` | no | Step-level timeout in ms |
| `options.location` | `Location` | no | Custom source location shown in reports |

Returns: `Promise<T>` (the return value of `body`).

```ts
const result = await test.step('Login flow', async (step) => {
  await page.fill('#user', 'admin');
  await page.fill('#pass', 'secret');
  await page.click('button[type=submit]');
  return 'logged-in';
}, { box: true, timeout: 10_000 });
```

### `test.step.skip(title, body)`

Skipped step — body is not executed; step appears as skipped in reports.

```ts
await test.step.skip('not ready yet', async () => { /* … */ });
```

---

## 7. Fixtures & Options

### `test.use(options)`

Applies fixture overrides or options to the current file or describe block.
Must be called at the top level of a file or describe callback (not inside a test).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `options` | `Partial<TestOptions & CustomFixtures>` | yes | Fixture values or option overrides |

```ts
test.use({ locale: 'de-DE', timezoneId: 'Europe/Berlin' });
```

### `test.extend(fixtures)`

Creates a new `test` object with additional fixtures or overridden options.
The returned value should be exported and used instead of the base `test`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fixtures` | `Object` | yes | Fixture definitions (see below) |

**Fixture definition forms:**

| Form | Example | Description |
|------|---------|-------------|
| Worker-scoped | `myFixture: [async ({}, use) => { … }, { scope: 'worker' }]` | Shared across tests in worker |
| Test-scoped (default) | `myFixture: async ({}, use) => { … }` | Fresh per test |
| Option | `myOption: ['default', { option: true }]` | Overridable via `test.use()` |
| Auto | `setup: [async ({}, use) => { … }, { auto: true }]` | Always runs, no explicit request needed |

```ts
export const test = base.extend<{ todoPage: TodoPage }, { dbPool: DbPool }>({
  dbPool: [async ({}, use) => {
    const pool = await DbPool.create();
    await use(pool);
    await pool.close();
  }, { scope: 'worker' }],

  todoPage: async ({ page, dbPool }, use) => {
    const tp = new TodoPage(page, dbPool);
    await tp.goto();
    await use(tp);
  },
});
```

---

## 8. Utilities

### `test.info()`

Returns the `TestInfo` object for the currently running test.

**Returns:** `TestInfo`

```ts
const info = test.info();
console.log(info.title, info.retry);
```

### `test.setTimeout(timeout)`

Changes the timeout for the currently running test.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `timeout` | `number` | yes | New timeout in ms; 0 = no timeout |

```ts
test('very slow', async ({ page }) => {
  test.setTimeout(120_000);
});
```

### `test.abort(message)`

Aborts the currently running test immediately with a given message.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `message` | `string` | no | Reason for abort |

```ts
await page.route('**/publish', route => {
  test.abort('Tests must not call /publish');
  route.abort();
});
```

---

## 9. Properties

### `test.expect`

The Playwright assertion function. Alias for the `expect` export.

```ts
await test.expect(page).toHaveTitle('Home');
```

---

## Manifest

| Category | Count |
|----------|-------|
| Test declaration methods | 2 (`test`, `test` with details) |
| Hook methods | 8 (`beforeAll`×2, `afterAll`×2, `beforeEach`×2, `afterEach`×2) |
| Modifier methods | 12 (skip/fixme/fail/slow × inline + declaration, only, fail.only) |
| describe variants | 9 (describe, describe.only, .skip, .fixme, .configure + deprecated×4) |
| Step methods | 2 (step, step.skip) |
| Fixture/option methods | 2 (use, extend) |
| Utility methods | 3 (info, setTimeout, abort) |
| Properties | 1 (expect) |
| **Total** | **39** |

**Fazit:** `test` ist der zentrale Einstiegspunkt des Test-Runners. Es vereint Deklaration,
Organisation (describe), Lebenszyklus-Hooks, Modifier (skip/fail/slow/fixme), Steps,
Fixture-Erweiterung (extend) und Konfiguration (use) in einem einzigen Objekt.

---

Source: https://playwright.dev/docs/api/class-test
