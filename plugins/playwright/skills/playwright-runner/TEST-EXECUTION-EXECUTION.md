# Playwright Test Execution — Complete Reference

## Contents

- [Basic CLI commands](#basic-cli-commands)
- [All CLI flags (`npx playwright test`)](#all-cli-flags-npx-playwright-test)
- [Parallelism](#parallelism)
- [Sharding](#sharding)
- [Retries](#retries)
- [Timeouts](#timeouts)
- [UI mode](#ui-mode)
- [webServer](#webserver)

## Basic CLI commands

```bash
# All tests
npx playwright test

# Specific file(s)
npx playwright test landing-page.spec.ts
npx playwright test tests/todo/ tests/login/

# By filename keyword
npx playwright test landing login         # Files containing "landing" OR "login"

# By test title (regex)
npx playwright test -g "add a todo item"

# Only the most recently failed tests
npx playwright test --last-failed

# Line number (specific test)
npx playwright test example.spec.ts:10

# Show report
npx playwright show-report
```

---

## All CLI flags (`npx playwright test`)

| Flag | Short | Type | Description |
|---|---|---|---|
| `--debug` | | boolean | Open the Playwright Inspector (step by step) |
| `--headed` | | boolean | Run tests in a visible browser window |
| `--ui` | | boolean | Interactive UI mode |
| `--ui-host` | | string | Host for the UI server (default: localhost; `0.0.0.0` for Docker) |
| `--ui-port` | | number | Port for the UI server (0 = random) |
| `--grep` | `-g` | string (regex) | Only tests whose title matches the regex |
| `--grep-invert` | | string (regex) | EXCLUDE tests matching the regex |
| `--workers` | `-j` | number \| `'N%'` | Number of parallel workers (e.g. `4` or `'50%'`) |
| `--project` | | string[] | Run only tests from this project |
| `--config` | `-c` | file path | Configuration file or test directory |
| `--fail-on-flaky-tests` | | boolean | Fail if a test is marked "flaky" |
| `--forbid-only` | | boolean | Fail on `test.only` (for CI) |
| `--fully-parallel` | | boolean | All tests in parallel |
| `--global-timeout` | | ms | Max. runtime of the entire suite |
| `--ignore-snapshots` | | boolean | Ignore screenshot/snapshot assertions |
| `--last-failed` | | boolean | Only previously failed tests |
| `--list` | | boolean | List tests without running them |
| `--max-failures` | `-x` | number | Abort after N failures |
| `--no-deps` | | boolean | Ignore project dependencies |
| `--only-changed` | | ref? | Only test files changed since ref/HEAD |
| `--output` | | directory | Folder for artifacts |
| `--pass-with-no-tests` | | boolean | Succeed even if no tests were found |
| `--quiet` | | boolean | Suppress stdout |
| `--repeat-each` | | number | Run each test N times |
| `--reporter` | | string | Reporter (dot, line, list, html, json, junit, blob) |
| `--retries` | | number | Max. retry attempts |
| `--shard` | | `N/M` | Shard N of M (1-based) |
| `--test-list` | | file path | File listing the tests to run |
| `--test-list-invert` | | file path | File listing the tests to skip |
| `--timeout` | | ms | Test timeout |
| `--trace` | | mode | Trace mode (on, off, on-first-retry, retain-on-failure) |
| `--tsconfig` | | file path | TypeScript configuration |
| `--update-snapshots` | `-u` | `all \| changed \| missing` | Update snapshots |
| `--update-source-method` | | `patch \| 3way \| overwrite` | Snapshot update method |

### Further subcommands

```bash
# Installations
npx playwright install [browser...]          # Install browsers
npx playwright install --with-deps chromium  # including system dependencies

# Merge reports
npx playwright merge-reports ./blob-reports --reporter html

# Show trace
npx playwright show-trace trace.zip

# Generate code
npx playwright codegen https://example.com

# Clear cache
npx playwright clear-cache
```

---

## Parallelism

### Default behavior

- Test files are run in parallel by default (one file per worker)
- Tests WITHIN a file run sequentially in the same worker

### Configuring workers

```typescript
// playwright.config.ts
export default defineConfig({
  workers: process.env.CI ? 2 : undefined,  // undefined = automatic (number of CPU cores)
});
```

```bash
npx playwright test --workers 4
npx playwright test --workers=50%   # 50% of the CPUs
npx playwright test --workers=1     # fully sequential
```

### `fullyParallel` — parallelize tests within a file

```typescript
// Global
export default defineConfig({ fullyParallel: true });

// Per project
projects: [{ name: 'chromium', fullyParallel: true }],
```

```typescript
// Per file
import { test } from '@playwright/test';
test.describe.configure({ mode: 'parallel' });
```

### `serial` — dependent tests in sequence

```typescript
test.describe.configure({ mode: 'serial' });

test('step 1', async ({ page }) => { /* ... */ });
test('step 2', async ({ page }) => { /* ... */ });
// Step 2 is skipped if step 1 fails (without retries)
```

### Selectively opting out of fullyParallel

```typescript
test.describe('sequential', () => {
  test.describe.configure({ mode: 'default' });
  test('in order 1', async ({ page }) => { /* ... */ });
  test('in order 2', async ({ page }) => { /* ... */ });
});
```

### Worker identification

```typescript
// In fixtures/tests:
testInfo.workerIndex       // 0 to (maxWorkers - 1)
testInfo.parallelIndex     // 0 to (active workers - 1)

// Environment variables (also in globalSetup):
process.env.TEST_WORKER_INDEX
process.env.TEST_PARALLEL_INDEX
```

### Limiting failures

```typescript
export default defineConfig({
  maxFailures: process.env.CI ? 10 : undefined,
});
```

---

## Sharding

Distributes tests across multiple machines:

```bash
# Across 4 machines (one shard each):
npx playwright test --shard=1/4
npx playwright test --shard=2/4
npx playwright test --shard=3/4
npx playwright test --shard=4/4
```

**Granularity:**
- With `fullyParallel: true`: sharding at test level (more even distribution)
- Without: sharding at file level

### Merging reports from shards

```typescript
// playwright.config.ts
export default defineConfig({
  reporter: process.env.CI ? 'blob' : 'html',
});
```

```bash
# Collect all blob reports, then:
npx playwright merge-reports --reporter html ./all-blob-reports
```

### GitHub Actions example

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

# After all shards: merge job
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

### Configuration

```typescript
// playwright.config.ts
export default defineConfig({ retries: 2 });

// Per project
projects: [{ name: 'ci', retries: 2 }],
```

```bash
npx playwright test --retries=3
```

```typescript
// Per test group
test.describe.configure({ retries: 2 });
```

### Test status with retries

| Status | Meaning |
|---|---|
| `passed` | Passed on the first attempt |
| `flaky` | Failed on the first attempt, then passed |
| `failed` | Failed on all attempts |

### `testInfo.retry` — detecting a retry

```typescript
test('example', async ({ page }, testInfo) => {
  if (testInfo.retry > 0) {
    // On retry: reset cache/state
    await page.context().clearCookies();
  }
  // ...
});
```

Also available in fixtures:

```typescript
myFixture: async ({}, use, testInfo) => {
  if (testInfo.retry) {
    await cleanupFromPreviousAttempt();
  }
  await use(value);
}
```

### Worker behavior on failure

After a failed test: the worker process and browser are discarded.
A new worker starts for the retry attempt.

### serial + retries

With `test.describe.configure({ mode: 'serial' })` and retries enabled:
all tests of the group are retried together.

---

## Timeouts

### Overview of all timeout types

| Type | Default | Applies to | Configuration |
|---|---|---|---|
| Test timeout | 30,000 ms | Test function + fixture setup + beforeEach | `timeout` in config |
| Expect timeout | 5,000 ms | Auto-retrying assertions | `expect.timeout` in config |
| Action timeout | 0 (no limit) | click, fill, hover etc. | `use.actionTimeout` |
| Navigation timeout | 0 (no limit) | page.goto, page.waitForURL etc. | `use.navigationTimeout` |
| Global timeout | 0 (no limit) | Entire test suite | `globalTimeout` in config |
| Fixture timeout | (same as test) | Individual fixture | `{ timeout }` in extend |
| beforeAll/afterAll | 30,000 ms | Hook function | `test.setTimeout()` in the hook |

### Test timeout

```typescript
// Global
export default defineConfig({ timeout: 120_000 });

// Per test
test('slow test', async ({ page }) => {
  test.setTimeout(120_000);
});

// test.slow() = triple the timeout
test('very slow test', async ({ page }) => {
  test.slow();
});

// From beforeEach
test.beforeEach(async ({ page }, testInfo) => {
  testInfo.setTimeout(testInfo.timeout + 30_000);
});
```

### Expect timeout

```typescript
// Global
export default defineConfig({
  expect: { timeout: 10_000 },
});

// Per assertion
await expect(locator).toHaveText('hello', { timeout: 10_000 });

// Preconfigured
const slowExpect = expect.configure({ timeout: 30_000 });
await slowExpect(locator).toBeVisible();
```

### Action timeout

```typescript
// Global
export default defineConfig({
  use: { actionTimeout: 10_000 },
});

// Per action
await page.getByRole('button').click({ timeout: 10_000 });
```

### Navigation timeout

```typescript
// Global
export default defineConfig({
  use: { navigationTimeout: 30_000 },
});

// Per navigation
await page.goto('https://example.com', { timeout: 30_000 });
```

### Global timeout

```typescript
export default defineConfig({
  globalTimeout: 60 * 60 * 1000,  // 1 hour
});
```

```bash
npx playwright test --global-timeout=3600000
```

### Fixture timeout

```typescript
const test = base.extend({
  slowFixture: [async ({}, use) => {
    await heavyOperation();
    await use('result');
  }, { timeout: 120_000, scope: 'worker' }],
});
```

---

## UI mode

```bash
npx playwright test --ui
# Docker / GitHub Codespaces:
npx playwright test --ui-host=0.0.0.0 --ui-port=8080
```

**Features:**
- Timeline with actions and DOM snapshots (time travel)
- Before/after view for each action
- Locator picker for verifying selectors
- Watch mode: auto-rerun on code changes
- Tabs: Call, Log, Errors, Console, Network, Attachments, Metadata
- "Open in VSCode" for jumping straight to the code

**Security:** With `--ui-host=0.0.0.0`, traces including passwords are accessible to others on the network.

---

## webServer

Complete configuration — see also `playwright-test-config`:

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

With `baseURL`, tests can use relative paths: `await page.goto('/login')`

---

Source: https://playwright.dev/docs/running-tests | https://playwright.dev/docs/test-cli | https://playwright.dev/docs/test-parallel | https://playwright.dev/docs/test-sharding | https://playwright.dev/docs/test-retries | https://playwright.dev/docs/test-timeouts | https://playwright.dev/docs/test-ui-mode | https://playwright.dev/docs/test-webserver
