# class-testconfig — Playwright Configuration Reference

`TestConfig` describes the shape of the top-level object passed to `defineConfig()` in
`playwright.config.ts`. Every field is optional; Playwright uses sensible defaults.

```ts
import { defineConfig } from '@playwright/test';
export default defineConfig({ /* TestConfig fields */ });
```

---

## All Fields

### `build`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Playwright transpiler configuration |

Sub-fields:

| Field | Type | Description |
|-------|------|-------------|
| `external` | `string[]` | Glob patterns for modules NOT transpiled by Playwright |

```ts
build: { external: ['node_modules/**'] }
```

---

### `captureGitInfo`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Capture Git metadata into test reports |

Sub-fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `commit` | `boolean` | false | Include current commit information |
| `diff` | `boolean` | false | Include `git diff` output |

---

### `expect`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Configuration for the assertion library |

Sub-fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `timeout` | `number` | 5000 | Default timeout (ms) for async expect matchers |
| `toHaveScreenshot` | `Object` | — | Screenshot assertion defaults (see TestProject) |
| `toMatchAriaSnapshot` | `Object` | — | ARIA snapshot assertion defaults |
| `toMatchSnapshot` | `Object` | — | Pixel/diff snapshot assertion defaults |
| `toPass` | `Object` | — | `toPass` polling defaults (`timeout`, `intervals`) |

---

### `failOnFlakyTests`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Exit with non-zero code if any test is detected as flaky |

---

### `forbidOnly`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Error if `test.only` or `describe.only` is used (useful in CI) |

```ts
forbidOnly: !!process.env.CI
```

---

### `fullyParallel`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Run all tests in all files concurrently (not just file-level parallelism) |

---

### `globalSetup`

| Type | Default | Description |
|------|---------|-------------|
| `string \| string[]` | — | Path(s) to global setup module(s) executed before the first test |

The module must export a default async function. Receives `FullConfig`.

```ts
globalSetup: require.resolve('./global-setup')
```

---

### `globalTeardown`

| Type | Default | Description |
|------|---------|-------------|
| `string \| string[]` | — | Path(s) to global teardown module(s) executed after the last test |

---

### `globalTimeout`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `0` (disabled) | Maximum total duration (ms) for the entire test suite |

---

### `grep`

| Type | Default | Description |
|------|---------|-------------|
| `RegExp \| RegExp[]` | — | Only run tests whose title matches the pattern(s) |

```ts
grep: /@smoke/
```

---

### `grepInvert`

| Type | Default | Description |
|------|---------|-------------|
| `RegExp \| RegExp[]` | — | Skip tests whose title matches the pattern(s) |

---

### `ignoreSnapshots`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Skip snapshot assertions (`toMatchSnapshot`, `toHaveScreenshot`) |

---

### `maxFailures`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `0` (disabled) | Stop the entire test run after N cumulative failures |

---

### `metadata`

| Type | Default | Description |
|------|---------|-------------|
| `Object<string, any>` | `{}` | Arbitrary key-value pairs serialised into test reports |

---

### `name`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Configuration name shown in reports |

---

### `outputDir`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `./test-results` | Directory for all test execution artifacts (traces, screenshots, videos) |

---

### `preserveOutput`

| Type | Default | Description |
|------|---------|-------------|
| `"always" \| "never" \| "failures-only"` | `"always"` | When to keep files in `outputDir` after a run |

---

### `projects`

| Type | Default | Description |
|------|---------|-------------|
| `TestProject[]` | `[]` | List of named test projects (browser configurations, etc.) |

```ts
projects: [
  { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
]
```

---

### `quiet`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Suppress `stdout` and `stderr` from tests |

---

### `repeatEach`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `1` | Run each test N times (useful for detecting flakiness) |

---

### `reportSlowTests`

| Type | Default | Description |
|------|---------|-------------|
| `null \| Object` | `{ max: 5, threshold: 300_000 }` | Report test files that take longer than `threshold` ms; show top `max` |

Sub-fields:

| Field | Type | Description |
|-------|------|-------------|
| `max` | `number` | Maximum number of slow files to report (0 = unlimited) |
| `threshold` | `number` | Milliseconds threshold to consider a file "slow" |

---

### `reporter`

| Type | Default | Description |
|------|---------|-------------|
| `string \| ReporterDescription[]` | `"dot"` (CI) / `"list"` | Reporter(s) to use |

Accepted formats:

```ts
// single built-in
reporter: 'html'

// multiple with options
reporter: [
  ['html', { outputFolder: 'playwright-report', open: 'never' }],
  ['json', { outputFile: 'results.json' }],
]
```

Built-in reporters: `list`, `dot`, `line`, `github`, `json`, `junit`, `html`, `blob`, `null`

---

### `respectGitIgnore`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `true` | Skip files matched by `.gitignore` when scanning for tests |

---

### `retries`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `0` | Maximum retry attempts for each failed test |

```ts
retries: process.env.CI ? 2 : 0
```

---

### `shard`

| Type | Default | Description |
|------|---------|-------------|
| `null \| Object` | — | Run a subset of tests for parallelising across CI machines |

Sub-fields:

| Field | Type | Description |
|-------|------|-------------|
| `total` | `number` | Total number of shards |
| `current` | `number` | This shard's index (1-based) |

```ts
shard: { total: 4, current: parseInt(process.env.SHARD_INDEX || '1') }
```

---

### `snapshotDir` *(discouraged)*

| Type | Default | Description |
|------|---------|-------------|
| `string` | `testDir` | Base directory for snapshot files; prefer `snapshotPathTemplate` |

---

### `snapshotPathTemplate`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Template with tokens controlling snapshot file paths |

Available tokens: `{testDir}`, `{snapshotDir}`, `{testFilePath}`, `{testFileName}`,
`{testFileDir}`, `{testName}`, `{projectName}`, `{platform}`, `{snapshotSuffix}`, `{arg}`, `{ext}`

---

### `tag`

| Type | Default | Description |
|------|---------|-------------|
| `string \| string[]` | — | Tags prepended to every test in reports |

---

### `testDir`

| Type | Default | Description |
|------|---------|-------------|
| `string` | config file directory | Directory recursively scanned for test files |

---

### `testIgnore`

| Type | Default | Description |
|------|---------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | — | Patterns matching files that must not be treated as tests |

---

### `testMatch`

| Type | Default | Description |
|------|---------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | `**/*.@(spec\|test).?(c\|m)[jt]s?(x)` | Patterns for files that should be treated as tests |

---

### `timeout`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `30_000` | Default per-test timeout in ms |

```ts
timeout: 60_000
```

---

### `tsconfig`

| Type | Default | Description |
|------|---------|-------------|
| `string` | auto-detected | Path to a `tsconfig.json` used for all imported files |

---

### `updateSnapshots`

| Type | Default | Description |
|------|---------|-------------|
| `"all" \| "changed" \| "missing" \| "none"` | `"missing"` | When to update snapshot files |

| Value | Behaviour |
|-------|-----------|
| `"missing"` | Create new snapshots only |
| `"changed"` | Update differing snapshots |
| `"all"` | Always overwrite snapshots |
| `"none"` | Never update snapshots |

---

### `updateSourceMethod`

| Type | Default | Description |
|------|---------|-------------|
| `"overwrite" \| "3way" \| "patch"` | `"patch"` | How Playwright writes snapshot updates back to source |

---

### `use`

| Type | Default | Description |
|------|---------|-------------|
| `TestOptions` | `{}` | Global options applied to every test (see class-testoptions.md) |

---

### `webServer`

| Type | Default | Description |
|------|---------|-------------|
| `Object \| Object[]` | — | Launch (or reuse) a dev server before running tests |

Sub-fields:

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `command` | `string` | yes | — | Shell command to start the server |
| `url` | `string` | no* | — | URL Playwright polls until ready |
| `port` | `number` | no* | — | Port Playwright polls; mutually exclusive with `url` |
| `reuseExistingServer` | `boolean` | no | `!CI` | Reuse an already-running server on that port/url |
| `timeout` | `number` | no | 60_000 | Max ms to wait for server readiness |
| `stdout` | `"pipe" \| "ignore"` | no | `"ignore"` | Server stdout handling |
| `stderr` | `"pipe" \| "ignore"` | no | `"pipe"` | Server stderr handling |
| `env` | `Object<string, string>` | no | — | Additional env vars for the server process |
| `cwd` | `string` | no | config dir | Working directory for the command |
| `gracefulShutdown` | `Object` | no | — | `{ signal, timeout }` for graceful stop |

---

### `workers`

| Type | Default | Description |
|------|---------|-------------|
| `number \| string` | 50% of CPU cores | Concurrent worker processes; string = percentage e.g. `'75%'` |

```ts
workers: process.env.CI ? 1 : '50%'
```

---

## Manifest

| Category | Count |
|----------|-------|
| Top-level fields | 38 (including deprecated `snapshotDir`) |
| Deprecated fields | 1 |

**Fazit:** `TestConfig` ist die vollstaendige Beschreibung der `playwright.config.ts`. Die
wichtigsten Felder fuer CI-Setups sind `projects`, `workers`, `retries`, `reporter` und
`webServer`. Mit `use` koennen globale Browser-/Netzwerk-Einstellungen gesetzt werden.

---

Source: https://playwright.dev/docs/api/class-testconfig
