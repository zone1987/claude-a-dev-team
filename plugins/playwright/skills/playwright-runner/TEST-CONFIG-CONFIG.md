# Playwright Test Configuration — Complete Reference

## Contents

- [Basic structure `playwright.config.ts`](#basic-structure-playwrightconfigts)
- [Top-level configuration options](#top-level-configuration-options)
- [`use` options (complete)](#use-options-complete)
- [`webServer` configuration](#webserver-configuration)
- [Projects configuration](#projects-configuration)
- [TypeScript setup](#typescript-setup)

## Basic structure `playwright.config.ts`

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit',   use: { ...devices['Desktop Safari'] } },
  ],
  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

---

## Top-level configuration options

| Option | Type | Default | Description |
|---|---|---|---|
| `testDir` | `string` | — | Directory containing test files |
| `testMatch` | `string \| RegExp \| (string \| RegExp)[]` | `**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}` | Glob/regex pattern for test files |
| `testIgnore` | `string \| RegExp \| (string \| RegExp)[]` | `**/node_modules/**` | Glob/regex pattern to ignore |
| `fullyParallel` | `boolean` | `false` | Run all tests in all files in parallel |
| `forbidOnly` | `boolean` | `false` | Fail if `test.only` is present (for CI) |
| `retries` | `number` | `0` | Max. retry attempts per test |
| `workers` | `number \| string` | `undefined` | Parallel worker processes; also a percentage e.g. `'50%'` |
| `timeout` | `number` | `30000` | Timeout per test in ms |
| `globalTimeout` | `number` | `0` | Max. runtime of the entire test suite in ms (0 = no limit) |
| `outputDir` | `string` | `'test-results'` | Folder for artifacts (screenshots, videos, traces) |
| `reporter` | `string \| [string, object][] \| 'dot' \| 'line' \| 'list' \| 'html' \| 'json' \| 'junit' \| 'blob'` | `'list'` | Reporter(s) |
| `globalSetup` | `string` | — | Path to a global setup module |
| `globalTeardown` | `string` | — | Path to a global teardown module |
| `projects` | `Project[]` | `[]` | Project definitions |
| `webServer` | `WebServerConfig \| WebServerConfig[]` | — | Web server configuration |
| `maxFailures` | `number` | `0` | Stop after N failures (0 = never) |
| `preserveOutput` | `'always' \| 'never' \| 'failures-only'` | `'failures-only'` | When artifacts are kept |
| `quiet` | `boolean` | `false` | Suppress stdout output |
| `shard` | `{ current: number, total: number } \| null` | `null` | Sharding configuration |
| `tsconfig` | `string` | — | Explicit path to the tsconfig |
| `use` | `PlaywrightTestOptions & BrowserContextOptions & LaunchOptions` | `{}` | Shared browser/context options |
| `expect` | `ExpectSettings` | — | Assertion settings (timeout, toHaveScreenshot, toMatchSnapshot) |
| `snapshotDir` | `string` | `'__snapshots__'` | Base directory for snapshots |
| `snapshotPathTemplate` | `string` | — | Template for snapshot paths |
| `metadata` | `object` | — | Arbitrary metadata for reporters |
| `updateSnapshots` | `'all' \| 'none' \| 'missing'` | `'missing'` | Snapshot update behavior |
| `ignoreSnapshots` | `boolean` | `false` | Ignore screenshot/snapshot assertions |

### `expect` options

```typescript
expect: {
  timeout: 5000,                           // Assertion timeout in ms (default: 5000)
  toHaveScreenshot: {
    maxDiffPixels: 100,                    // Max. pixel differences
    maxDiffPixelRatio: 0.01,              // Max. ratio of differing pixels (0-1)
    threshold: 0.2,                        // Pixelmatch threshold (0-1)
    animations: 'disabled',               // Disable animations
    caret: 'hide',                         // Hide the caret
    scale: 'css',                          // CSS or device scaling
    stylePath: './screenshot.css',         // CSS to overlay
  },
  toMatchSnapshot: {
    maxDiffPixels: 100,
    maxDiffPixelRatio: 0.01,
    threshold: 0.2,
  },
},
```

---

## `use` options (complete)

### Browser options

| Option | Type | Default | Description |
|---|---|---|---|
| `browserName` | `'chromium' \| 'firefox' \| 'webkit'` | `'chromium'` | Browser engine |
| `channel` | `string` | — | Browser channel: `'chrome'`, `'chrome-beta'`, `'msedge'`, `'msedge-beta'` |
| `headless` | `boolean` | `true` | Headless mode |
| `launchOptions` | `object` | `{}` | All `browserType.launch()` options (slowMo, devtools, executablePath …) |
| `connectOptions` | `object` | `{}` | All `browserType.connect()` options |
| `screenshot` | `'off' \| 'on' \| 'only-on-failure'` | `'off'` | Capture screenshots automatically |
| `trace` | `'off' \| 'on' \| 'retain-on-failure' \| 'on-first-retry' \| 'on-all-retries'` | `'off'` | Trace recording |
| `video` | `'off' \| 'on' \| 'retain-on-failure' \| 'on-first-retry'` | `'off'` | Video recording |

### Browser context options

| Option | Type | Default | Description |
|---|---|---|---|
| `baseURL` | `string` | — | Base URL for `page.goto('/')` |
| `storageState` | `string \| object` | — | Storage state (auth, cookies) |
| `viewport` | `{ width: number, height: number } \| null` | `{ width: 1280, height: 720 }` | Viewport size; `null` = no fixed viewport |
| `colorScheme` | `'light' \| 'dark' \| 'no-preference'` | `'light'` | Emulate prefers-color-scheme |
| `geolocation` | `{ longitude: number, latitude: number, accuracy?: number }` | — | Geolocation |
| `locale` | `string` | — | Browser locale e.g. `'de-DE'` |
| `timezoneId` | `string` | — | Time zone e.g. `'Europe/Berlin'` |
| `permissions` | `string[]` | `[]` | Browser permissions: `'geolocation'`, `'notifications'` … |
| `acceptDownloads` | `boolean` | `true` | Accept downloads automatically |
| `bypassCSP` | `boolean` | `false` | Bypass the Content Security Policy |
| `extraHTTPHeaders` | `Record<string, string>` | `{}` | Additional HTTP headers |
| `httpCredentials` | `{ username: string, password: string }` | — | HTTP basic auth |
| `ignoreHTTPSErrors` | `boolean` | `false` | Ignore HTTPS errors |
| `javaScriptEnabled` | `boolean` | `true` | JavaScript in the browser |
| `offline` | `boolean` | `false` | Emulate offline mode |
| `proxy` | `{ server: string, bypass?: string, username?: string, password?: string }` | — | Proxy settings |
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Allow/block service workers |
| `userAgent` | `string` | — | User agent string |
| `deviceScaleFactor` | `number` | — | Device pixel ratio |
| `hasTouch` | `boolean` | `false` | Emulate touch events |
| `isMobile` | `boolean` | `false` | Mobile mode |
| `contextOptions` | `object` | `{}` | All `browser.newContext()` options |

### Timeout options

| Option | Type | Default | Description |
|---|---|---|---|
| `actionTimeout` | `number` | `0` | Max. duration for actions (click, fill …) in ms |
| `navigationTimeout` | `number` | `0` | Max. duration for navigation in ms |

### Test ID option

| Option | Type | Default | Description |
|---|---|---|---|
| `testIdAttribute` | `string` | `'data-testid'` | HTML attribute for `getByTestId()` |

---

## `webServer` configuration

```typescript
webServer: {
  command: 'npm run start',          // (required) Shell command to start it
  url: 'http://localhost:3000',      // (required) URL that returns 2xx/3xx/4xx
  cwd: '.',                          // Working directory (default: config directory)
  env: { NODE_ENV: 'test' },         // Additional env variables
  timeout: 60000,                    // Wait time in ms (default: 60000)
  reuseExistingServer: true,         // Reuse an existing server
  stdout: 'pipe',                    // 'pipe' | 'ignore' (default: 'ignore')
  stderr: 'pipe',                    // 'pipe' | 'ignore' (default: 'pipe')
  name: 'Frontend',                  // Display name for logs
  ignoreHTTPSErrors: false,          // Ignore HTTPS errors
  gracefulShutdown: {                // Graceful shutdown
    signal: 'SIGTERM',
    timeout: 5000,
  },
  wait: {                            // Wait for specific output
    regex: /Server started/,
  },
}
```

Multiple servers as an array:

```typescript
webServer: [
  { command: 'npm run frontend', url: 'http://localhost:3000', name: 'Frontend' },
  { command: 'npm run backend',  url: 'http://localhost:3333', name: 'Backend' },
]
```

---

## Projects configuration

### Multiple browsers

```typescript
projects: [
  { name: 'chromium',      use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox',       use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit',        use: { ...devices['Desktop Safari'] } },
  { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } },
  { name: 'Mobile Safari', use: { ...devices['iPhone 12'] } },
  { name: 'Edge',          use: { ...devices['Desktop Edge'], channel: 'msedge' } },
  { name: 'Chrome',        use: { ...devices['Desktop Chrome'], channel: 'chrome' } },
],
```

### Project options

| Option | Type | Description |
|---|---|---|
| `name` | `string` | Unique project name |
| `use` | `object` | All `use` options; overrides the global `use` |
| `testDir` | `string` | Test directory for this project |
| `testMatch` | `string \| RegExp` | Test file filter for this project |
| `testIgnore` | `string \| RegExp` | Ignore pattern for this project |
| `retries` | `number` | Retries for this project |
| `timeout` | `number` | Test timeout for this project |
| `fullyParallel` | `boolean` | Full parallelization for this project |
| `dependencies` | `string[]` | Projects that must run beforehand |
| `teardown` | `string` | Project name for teardown after this project |
| `metadata` | `object` | Arbitrary metadata |
| `snapshotDir` | `string` | Snapshot directory for this project |

### Project dependencies (setup/teardown)

```typescript
projects: [
  {
    name: 'setup',
    testMatch: /global\.setup\.ts/,
    teardown: 'cleanup',             // runs after all dependent projects
  },
  {
    name: 'cleanup',
    testMatch: /global\.teardown\.ts/,
  },
  {
    name: 'chromium',
    use: { ...devices['Desktop Chrome'] },
    dependencies: ['setup'],         // waits for 'setup'
  },
],
```

**Execution order:**
1. The `setup` project runs to completion
2. On success: dependent projects in parallel
3. Afterwards: the `teardown` project (if configured)
4. On a setup failure: dependent projects are skipped

`--no-deps` ignores dependencies (only the directly selected projects).

---

## TypeScript setup

### Automatic detection

Playwright detects `tsconfig.json` / `jsconfig.json` automatically (directory traversal upwards).

### Supported tsconfig options

| Option | Description |
|---|---|
| `allowJs` | Allow JS files |
| `baseUrl` | Base URL for modules |
| `paths` | Path aliases |
| `references` | Project references |

### Path aliases

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@helpers/*": ["src/helpers/*"],
      "@fixtures/*": ["tests/fixtures/*"]
    }
  }
}
```

```typescript
// Test file
import { myHelper } from '@helpers/utils';
```

### Explicit tsconfig

```typescript
// playwright.config.ts
export default defineConfig({
  tsconfig: './tsconfig.test.json',
});
```

Or via CLI: `npx playwright test --tsconfig=tsconfig.test.json`

### Type checking in parallel

```bash
# Type check without running
npx tsc -p tsconfig.json --noEmit

# Watch mode
npx tsc -p tsconfig.json --noEmit -w
```

Playwright runs tests even when there are TS errors (no blocking).

---

Source: https://playwright.dev/docs/test-configuration | https://playwright.dev/docs/test-use-options | https://playwright.dev/docs/test-projects | https://playwright.dev/docs/test-typescript
