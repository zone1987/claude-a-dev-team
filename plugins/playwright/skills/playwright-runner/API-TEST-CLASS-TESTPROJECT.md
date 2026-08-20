# class-testproject — Playwright Project Configuration

`TestProject` defines a single entry in `testConfig.projects[]`. Each project can target a
different browser, device emulation, base URL, or fixture set.

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
```

---

## All Fields

### `dependencies`

| Type | Default | Description |
|------|---------|-------------|
| `string[]` | — | Names of other projects that must complete before this project starts |

```ts
{ name: 'e2e', dependencies: ['setup'] }
```

---

### `expect`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Assertion library configuration for this project |

Sub-fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `timeout` | `number` | 5000 | Default timeout (ms) for async matchers |
| `toHaveScreenshot` | `Object` | — | Screenshot comparison options |
| `toHaveScreenshot.threshold` | `number` | 0.2 | Max acceptable colour difference per pixel (0–1) |
| `toHaveScreenshot.maxDiffPixels` | `number` | — | Max absolute pixel difference |
| `toHaveScreenshot.maxDiffPixelRatio` | `number` | — | Max ratio of differing pixels (0–1) |
| `toHaveScreenshot.animations` | `"allow" \| "disabled"` | `"disabled"` | Animation handling during screenshot capture |
| `toHaveScreenshot.caret` | `"hide" \| "initial"` | `"hide"` | Caret visibility |
| `toHaveScreenshot.scale` | `"css" \| "device"` | `"css"` | Screenshot coordinate space |
| `toHaveScreenshot.stylePath` | `string \| string[]` | — | CSS file(s) injected before screenshotting |
| `toHaveScreenshot.pathTemplate` | `string` | — | Custom path template for screenshot files |
| `toMatchAriaSnapshot` | `Object` | — | ARIA snapshot matching options |
| `toMatchAriaSnapshot.pathTemplate` | `string` | — | Custom path for ARIA snapshot files |
| `toMatchSnapshot` | `Object` | — | Binary/text snapshot options |
| `toMatchSnapshot.threshold` | `number` | 0.2 | Pixel colour threshold |
| `toMatchSnapshot.maxDiffPixels` | `number` | — | Max absolute pixel difference |
| `toMatchSnapshot.maxDiffPixelRatio` | `number` | — | Max ratio of differing pixels |
| `toPass` | `Object` | — | Options for `expect.toPass()` polling |
| `toPass.timeout` | `number` | — | Max polling duration |
| `toPass.intervals` | `number[]` | — | Retry intervals |

---

### `fullyParallel`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | — | Run all tests in this project concurrently (overrides global setting) |

---

### `grep`

| Type | Default | Description |
|------|---------|-------------|
| `RegExp \| RegExp[]` | — | Only run tests whose title matches; combined with global `grep` |

---

### `grepInvert`

| Type | Default | Description |
|------|---------|-------------|
| `RegExp \| RegExp[]` | — | Skip tests whose title matches |

---

### `ignoreSnapshots`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Skip all snapshot assertions for this project |

---

### `metadata`

| Type | Default | Description |
|------|---------|-------------|
| `Object<string, any>` | — | Arbitrary metadata serialised into test reports |

---

### `name`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Project name shown in reports and used by `dependencies` / `teardown` |

---

### `outputDir`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `test-results` | Directory for this project's test artifacts |

---

### `repeatEach`

| Type | Default | Description |
|------|---------|-------------|
| `number` | — | Run each test N times in this project |

---

### `respectGitIgnore`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | — | Skip `.gitignore`-listed files when scanning for tests |

---

### `retries`

| Type | Default | Description |
|------|---------|-------------|
| `number` | — | Max retry attempts for failed tests in this project |

---

### `snapshotDir`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `testDir` | Base directory for snapshot files (relative to config); prefer `snapshotPathTemplate` |

---

### `snapshotPathTemplate`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Template controlling snapshot paths; supports the same tokens as `testConfig.snapshotPathTemplate` |

---

### `teardown`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Name of project to run after this project finishes (even on failure) |

```ts
{ name: 'setup', teardown: 'cleanup' }
```

---

### `testDir`

| Type | Default | Description |
|------|---------|-------------|
| `string` | config directory | Directory scanned for test files; overrides global `testDir` |

---

### `testIgnore`

| Type | Default | Description |
|------|---------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | — | Exclude files matching pattern from this project |

---

### `testMatch`

| Type | Default | Description |
|------|---------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | `**/*.@(spec\|test).?(c\|m)[jt]s?(x)` | Include files matching pattern |

---

### `timeout`

| Type | Default | Description |
|------|---------|-------------|
| `number` | 30_000 | Per-test timeout in ms for this project |

---

### `use`

| Type | Default | Description |
|------|---------|-------------|
| `TestOptions` | — | Browser, network, and emulation options for all tests in this project |

```ts
use: {
  ...devices['iPhone 13'],
  baseURL: 'https://staging.example.com',
}
```

---

### `workers`

| Type | Default | Description |
|------|---------|-------------|
| `number \| string` | — | Override global `workers` setting for this project |

---

## Manifest

| Category | Count |
|----------|-------|
| Top-level project fields | 20 |
| expect sub-fields | 14 |

**Fazit:** `TestProject` ermoeglicht Matrix-Konfigurationen (Browser, Geraete, Umgebungen) mit
gemeinsamen oder ueberschriebenen Optionen. `dependencies` und `teardown` erlauben geordnete
Setup/Teardown-Projekte (z.B. Authentifizierung vor E2E-Tests).

---

Source: https://playwright.dev/docs/api/class-testproject
