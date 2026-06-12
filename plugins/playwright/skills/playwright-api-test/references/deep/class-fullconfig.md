# class-fullconfig — Playwright FullConfig Reference

`FullConfig` is the runtime-resolved version of `TestConfig`. It is available in:

- `reporter.onBegin(config, suite)` — first reporter hook argument
- `testInfo.config` — inside any test or hook
- Global setup/teardown functions (first argument)

Unlike `TestConfig`, `FullConfig` contains resolved absolute paths and cannot be mutated.

```ts
// global-setup.ts
import { FullConfig } from '@playwright/test';

export default async function globalSetup(config: FullConfig) {
  console.log(config.rootDir, config.version);
}
```

---

## All Properties

### `configFile`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `""` | Absolute path to the configuration file; empty string when no config file was used |

---

### `forbidOnly`

| Type | Description |
|------|-------------|
| `boolean` | Resolved value of `testConfig.forbidOnly` |

---

### `fullyParallel`

| Type | Description |
|------|-------------|
| `boolean` | Resolved value of `testConfig.fullyParallel` |

---

### `globalSetup`

| Type | Default | Description |
|------|---------|-------------|
| `string \| null` | `null` | Absolute path of the global setup module; `null` when not configured |

---

### `globalTeardown`

| Type | Default | Description |
|------|---------|-------------|
| `string \| null` | `null` | Absolute path of the global teardown module; `null` when not configured |

---

### `globalTimeout`

| Type | Description |
|------|-------------|
| `number` | Resolved value of `testConfig.globalTimeout` |

---

### `grep`

| Type | Description |
|------|-------------|
| `RegExp \| RegExp[]` | Resolved test title filter pattern(s) |

---

### `grepInvert`

| Type | Default | Description |
|------|---------|-------------|
| `RegExp \| RegExp[] \| null` | `null` | Resolved inverse filter pattern(s) |

---

### `maxFailures`

| Type | Description |
|------|-------------|
| `number` | Resolved value of `testConfig.maxFailures` |

---

### `metadata`

| Type | Description |
|------|-------------|
| `Object<string, any>` | Resolved metadata key-value pairs |

---

### `preserveOutput`

| Type | Description |
|------|-------------|
| `"always" \| "never" \| "failures-only"` | Resolved output preservation strategy |

---

### `projects`

| Type | Description |
|------|-------------|
| `FullProject[]` | All resolved project configurations (see class-fullproject.md) |

---

### `quiet`

| Type | Description |
|------|-------------|
| `boolean` | Whether stdio output is suppressed |

---

### `reportSlowTests`

| Type | Default | Description |
|------|---------|-------------|
| `null \| { max: number, threshold: number }` | `null` | Slow-test reporting configuration |

---

### `reporter`

| Type | Description |
|------|-------------|
| `string \| Array<[string, Object]>` | Resolved reporter list with options |

---

### `rootDir`

| Type | Description |
|------|-------------|
| `string` | Absolute base directory used for resolving relative paths in reporters and config |

---

### `shard`

| Type | Default | Description |
|------|---------|-------------|
| `null \| { total: number, current: number }` | `null` | Shard configuration; `null` when no sharding is active |

---

### `tags`

| Type | Description |
|------|-------------|
| `string[]` | Resolved global tags |

---

### `updateSnapshots`

| Type | Description |
|------|-------------|
| `"all" \| "changed" \| "missing" \| "none"` | Snapshot update strategy |

---

### `updateSourceMethod`

| Type | Description |
|------|-------------|
| `"overwrite" \| "3way" \| "patch"` | Source update method |

---

### `version`

| Type | Description |
|------|-------------|
| `string` | Playwright version string (e.g. `"1.48.0"`) |

---

### `webServer`

| Type | Default | Description |
|------|---------|-------------|
| `null \| Object` | `null` | Resolved web server configuration |

---

### `workers`

| Type | Description |
|------|-------------|
| `number` | Resolved worker count (percentage strings converted to absolute numbers) |

---

## Manifest

| Category | Count |
|----------|-------|
| Properties | 24 |
| Methods | 0 |

**Fazit:** `FullConfig` ist die aufgeloeste, read-only Laufzeit-Variante von `TestConfig`.
Besonders nuetzlich sind `rootDir` (fuer pfad-relative Operationen in Reportern), `version`
(fuer Kompatibilitaetspruefungen) und `projects` (fuer den Zugriff auf alle Projekt-Configs).

---

Source: https://playwright.dev/docs/api/class-fullconfig
