# class-testinfo — Playwright TestInfo Reference

`TestInfo` is available inside every test function and hook. It carries metadata about the
currently running test and provides methods to control its behaviour.

Access via the second fixture parameter or via `test.info()`:

```ts
test('example', async ({ page }, testInfo) => {
  console.log(testInfo.title);
});
// or anywhere inside a test:
const info = test.info();
```

---

## Methods

### `attach(name, options?)`

Attach a file or in-memory buffer to the test report.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `string` | yes | Attachment label; sanitised to be file-system safe |
| `options.body` | `string \| Buffer` | no* | Inline content; mutually exclusive with `path` |
| `options.path` | `string` | no* | Filesystem path; mutually exclusive with `body` |
| `options.contentType` | `string` | no | MIME type; inferred from `path` extension or defaults to `text/plain` |

*One of `body` or `path` is required.

**Returns:** `Promise<void>`

```ts
await testInfo.attach('screenshot', {
  body: await page.screenshot(),
  contentType: 'image/png',
});

await testInfo.attach('response.json', {
  path: './tmp/response.json',
  contentType: 'application/json',
});
```

---

### `fail(condition?, description?)`

Mark the test as "expected to fail". If the test passes, it is reported as unexpected.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `condition` | `boolean` | no | `true` | Apply the marker when condition is truthy |
| `description` | `string` | no | — | Reason shown in the report |

**Returns:** `void`

```ts
testInfo.fail(browserName === 'webkit', 'Safari bug #99');
```

---

### `fixme(condition?, description?)`

Mark the test as fixme; execution is aborted immediately.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `condition` | `boolean` | no | `true` | Apply when truthy |
| `description` | `string` | no | — | Reason for report |

**Returns:** `void`

```ts
testInfo.fixme(!featureFlag, 'Feature not yet enabled');
```

---

### `outputPath(...pathSegments)`

Returns a path inside the test's unique output directory, creating the directory if needed.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `...pathSegments` | `string[]` | yes | Path segments to join |

**Returns:** `string` — absolute, parallel-safe path

```ts
const screenshotPath = testInfo.outputPath('screenshots', 'final.png');
await page.screenshot({ path: screenshotPath });
```

---

### `setTimeout(timeout)`

Change the timeout for the currently running test.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `timeout` | `number` | yes | New timeout in ms; `0` disables the timeout |

**Returns:** `void`

```ts
testInfo.setTimeout(testInfo.timeout + 60_000); // add one minute
```

---

### `skip(condition?, description?)`

Skip the test; execution is aborted immediately.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `condition` | `boolean` | no | `true` | Skip when truthy |
| `description` | `string` | no | — | Reason for report |

**Returns:** `void`

```ts
testInfo.skip(process.env.CI === undefined, 'Only run in CI');
```

---

### `slow(condition?, description?)`

Triple the timeout for the current test.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `condition` | `boolean` | no | `true` | Apply when truthy |
| `description` | `string` | no | — | Reason for report |

**Returns:** `void`

```ts
testInfo.slow(browserName === 'firefox', 'Firefox renders slower');
```

---

### `snapshotPath(...name)`
### `snapshotPath(...name, options)`

Returns the path for a snapshot file.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `...name` | `string[]` | yes | Snapshot name or path segments |
| `options.kind` | `"snapshot" \| "screenshot" \| "aria"` | no | Snapshot category; defaults to `"snapshot"` |

**Returns:** `string` — path according to `snapshotPathTemplate`

```ts
const path = testInfo.snapshotPath('header.png', { kind: 'screenshot' });
```

---

## Properties

### `annotations`

| Type | Description |
|------|-------------|
| `Array<{ type: string, description?: string, location?: Location }>` | All annotations for this test, including those from parent `describe` blocks |

---

### `attachments`

| Type | Description |
|------|-------------|
| `Array<{ name: string, contentType: string, path?: string, body?: Buffer }>` | Files and buffers attached via `testInfo.attach()` |

---

### `column`

| Type | Description |
|------|-------------|
| `number` | Column number of the test declaration in the source file |

---

### `config`

| Type | Description |
|------|-------------|
| `FullConfig` | The fully processed configuration object (read-only) |

---

### `duration`

| Type | Description |
|------|-------------|
| `number` | Elapsed time in ms; zero while the test is still running |

---

### `error`

| Type | Description |
|------|-------------|
| `TestInfoError \| undefined` | First error thrown during execution; shorthand for `errors[0]` |

---

### `errors`

| Type | Description |
|------|-------------|
| `Array<TestInfoError>` | All errors thrown during execution |

---

### `expectedStatus`

| Type | Description |
|------|-------------|
| `"passed" \| "failed" \| "timedOut" \| "skipped" \| "interrupted"` | The status Playwright expects this test to reach |

---

### `file`

| Type | Description |
|------|-------------|
| `string` | Absolute path of the test file |

---

### `fn`

| Type | Description |
|------|-------------|
| `Function` | The test function itself |

---

### `line`

| Type | Description |
|------|-------------|
| `number` | Line number of the test declaration |

---

### `outputDir`

| Type | Description |
|------|-------------|
| `string` | Absolute path to the output directory for this specific test run |

---

### `parallelIndex`

| Type | Description |
|------|-------------|
| `number` | Index of this worker relative to the total number of workers (0 to workers−1) |

---

### `project`

| Type | Description |
|------|-------------|
| `FullProject` | Fully resolved project configuration for the currently running project |

---

### `repeatEachIndex`

| Type | Description |
|------|-------------|
| `number` | Current repeat index when `repeatEach > 1` |

---

### `retry`

| Type | Description |
|------|-------------|
| `number` | Current retry attempt index (0 = first run, 1 = first retry, …) |

---

### `snapshotDir`

| Type | Description |
|------|-------------|
| `string` | Absolute path to the snapshot directory for this test |

---

### `snapshotSuffix`

| Type | Description |
|------|-------------|
| `string` | Platform/project-specific suffix appended to snapshot filenames |

---

### `status`

| Type | Description |
|------|-------------|
| `"passed" \| "failed" \| "timedOut" \| "skipped" \| "interrupted" \| undefined` | Current test status; available after the test body completes |

---

### `tags`

| Type | Description |
|------|-------------|
| `Array<string>` | Tags applied to the test via `test()` or extracted from `@tag` in titles |

---

### `testId`

| Type | Description |
|------|-------------|
| `string` | Unique identifier used by the Reporter API |

---

### `timeout`

| Type | Description |
|------|-------------|
| `number` | Current timeout in ms; `0` means no timeout |

---

### `title`

| Type | Description |
|------|-------------|
| `string` | Test title (string passed to `test()`) |

---

### `titlePath`

| Type | Description |
|------|-------------|
| `Array<string>` | Full path of titles from file name down through all `describe` blocks to the test title |

---

### `workerIndex`

| Type | Description |
|------|-------------|
| `number` | Unique index of the worker process; stable within a worker across retries |

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 7 (`attach`, `fail`, `fixme`, `outputPath`, `setTimeout`, `skip`, `slow`, `snapshotPath`) |
| Properties | 22 |

**Fazit:** `TestInfo` ist die Laufzeitschnittstelle zum aktuellen Test. Es bietet sowohl
lesende Metadaten (Titel, Datei, Retry) als auch steuernde Methoden (skip, fail, slow,
setTimeout). `attach` und `outputPath` sind die primären Wege, Artefakte zu einem Test
hinzuzufuegen.

---

Source: https://playwright.dev/docs/api/class-testinfo
