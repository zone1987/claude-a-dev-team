# class-fullproject — Playwright FullProject Reference

`FullProject` is the runtime-resolved version of `TestProject`. It is available as:

- `fullConfig.projects[n]` — in reporters via `reporter.onBegin()`
- `suite.project()` — on any suite in the reporter API
- `testInfo.project` — inside any test or hook
- `workerInfo.project` — in worker-scoped fixtures

Unlike `TestProject`, all paths are absolute and all options are resolved.

```ts
test('check project', async ({}, testInfo) => {
  console.log(testInfo.project.name, testInfo.project.testDir);
});
```

---

## All Properties

All properties correspond directly to their `TestProject` counterparts (fully resolved).

### `dependencies`

| Type | Added | Description |
|------|-------|-------------|
| `string[]` | v1.31 | Names of projects that must complete before this one starts |

---

### `grep`

| Type | Added | Description |
|------|-------|-------------|
| `RegExp \| RegExp[]` | v1.10 | Test title filter; combined with global `grep` |

---

### `grepInvert`

| Type | Added | Description |
|------|-------|-------------|
| `RegExp \| RegExp[] \| null` | v1.10 | Inverse test title filter |

---

### `ignoreSnapshots`

| Type | Added | Description |
|------|-------|-------------|
| `boolean` | v1.59 | Whether snapshot assertions are skipped in this project |

---

### `metadata`

| Type | Added | Description |
|------|-------|-------------|
| `Object<string, any>` | v1.10 | Project-level metadata serialised into reports |

---

### `name`

| Type | Added | Description |
|------|-------|-------------|
| `string` | v1.10 | Project name (e.g. `"chromium"`, `"Mobile Safari"`) |

---

### `outputDir`

| Type | Added | Description |
|------|-------|-------------|
| `string` | v1.10 | Absolute path to the output directory for this project |

---

### `repeatEach`

| Type | Added | Description |
|------|-------|-------------|
| `number` | v1.10 | How many times each test is repeated |

---

### `retries`

| Type | Added | Description |
|------|-------|-------------|
| `number` | v1.10 | Max retry attempts for failed tests |

---

### `snapshotDir`

| Type | Added | Description |
|------|-------|-------------|
| `string` | v1.10 | Absolute path to the snapshot directory |

---

### `teardown`

| Type | Added | Description |
|------|-------|-------------|
| `string` | v1.34 | Name of the project to run after this project completes |

---

### `testDir`

| Type | Added | Description |
|------|-------|-------------|
| `string` | v1.10 | Absolute path of the directory scanned for test files |

---

### `testIgnore`

| Type | Added | Description |
|------|-------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | v1.10 | Patterns for excluded test files |

---

### `testMatch`

| Type | Added | Description |
|------|-------|-------------|
| `string \| RegExp \| Array<string \| RegExp>` | v1.10 | Patterns for included test files |

---

### `timeout`

| Type | Added | Description |
|------|-------|-------------|
| `number` | v1.10 | Per-test timeout in ms |

---

### `use`

| Type | Added | Description |
|------|-------|-------------|
| `Fixtures` | v1.10 | Resolved `use` options for all tests in this project |

Note: The type here is `Fixtures` (the merged resolved value), not `TestOptions`.

---

## Usage Example

```ts
// Reporter: group slow tests by project
onTestEnd(test, result) {
  const proj = test.parent.project();
  if (proj && result.duration > 10_000) {
    console.log(`[${proj.name}] Slow test: ${test.title} (${result.duration}ms)`);
  }
}
```

---

## Manifest

| Category | Count |
|----------|-------|
| Properties | 16 |
| Methods | 0 |

**Fazit:** `FullProject` spiegelt `TestProject` mit aufgeloesten absoluten Pfaden wider.
Es ist die primaere Quelle fuer projekt-spezifische Konfiguration in Reportern und Fixtures.
`name` und `use` sind die am haeufigsten abgefragten Properties.

---

Source: https://playwright.dev/docs/api/class-fullproject
