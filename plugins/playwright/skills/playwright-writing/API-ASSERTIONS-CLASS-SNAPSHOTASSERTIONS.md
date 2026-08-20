# class-snapshotassertions — Playwright API Reference

`SnapshotAssertions` offers methods for comparing strings or buffer values against stored snapshots. No auto-retry. For screenshots of pages or elements, `expect(page).toHaveScreenshot()` or `expect(locator).toHaveScreenshot()` should be used instead.

Accessed via `expect(value).toMatchSnapshot(...)`.

Method count: 2 (toMatchSnapshot with and without name)

---

## Contents

- [toMatchSnapshot() — with name](#tomatchsnapshot-with-name)
- [toMatchSnapshot() — automatic](#tomatchsnapshot-automatic)
- [Usage notes](#usage-notes)
- [Method overview (2 methods)](#method-overview-2-methods)

## toMatchSnapshot() — with name

```typescript
toMatchSnapshot(
  name: string | string[],
  options?: {
    maxDiffPixels?: number;
    maxDiffPixelRatio?: number;
    threshold?: number;
  }
): Promise<void>
```

Compares a `string` or `Buffer` value against the snapshot stored under the given name.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string \| string[]` | yes | — | Snapshot file name or array of path segments |
| `options.maxDiffPixels` | `number` | no | from `TestConfig.expect` | Maximum number of differing pixels allowed |
| `options.maxDiffPixelRatio` | `number` | no | from `TestConfig.expect` | Maximum ratio of differing pixels (0-1) |
| `options.threshold` | `number` | no | `0.2` | Perceived color difference tolerance in the YIQ color space (0 = strict, 1 = permissive) |

**Returns:** `Promise<void>`

```typescript
// String snapshot
expect(generatedCSV).toMatchSnapshot('export.csv');

// Buffer snapshot (e.g. PDF)
const pdfBuffer = await page.pdf();
expect(pdfBuffer).toMatchSnapshot('report.pdf');

// Path segments
expect(xmlData).toMatchSnapshot(['exports', 'data.xml']);
```

---

## toMatchSnapshot() — automatic

```typescript
toMatchSnapshot(options?: {
  name?: string | string[];
  maxDiffPixels?: number;
  maxDiffPixelRatio?: number;
  threshold?: number;
}): Promise<void>
```

Compares against a snapshot; the name is generated from the test name and an ordinal number when `name` is missing.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.name` | `string \| string[]` | no | auto (test name + counter) | Optional snapshot name |
| `options.maxDiffPixels` | `number` | no | from `TestConfig.expect` | Maximum number of differing pixels allowed |
| `options.maxDiffPixelRatio` | `number` | no | from `TestConfig.expect` | Maximum ratio of differing pixels (0-1) |
| `options.threshold` | `number` | no | `0.2` | Color difference tolerance (YIQ color space, 0-1) |

**Returns:** `Promise<void>`

```typescript
// Automatically named (first call in the test = "-1", second = "-2", etc.)
expect(jsonOutput).toMatchSnapshot();

// With an explicit name in the options object
expect(htmlContent).toMatchSnapshot({ name: 'rendered-template.html' });
expect(imageBuffer).toMatchSnapshot({
  name: 'thumbnail.png',
  threshold: 0.1,
  maxDiffPixels: 100,
});
```

---

## Usage notes

**Snapshot updating:** On the first call the snapshot is created. To update:

```bash
npx playwright test --update-snapshots
```

**Storage location:** Snapshots are stored by default in a `__snapshots__` directory next to the test file. Configurable via `TestConfig.snapshotDir`.

**Distinction from `toHaveScreenshot`:**
- `toMatchSnapshot` for arbitrary `string` or `Buffer` values
- `expect(page).toHaveScreenshot()` for page screenshots (with stabilization wait time)
- `expect(locator).toHaveScreenshot()` for element screenshots

---

## Method overview (2 methods)

| Method | Description |
|---|---|
| `toMatchSnapshot(name, options?)` | Comparison against a named snapshot |
| `toMatchSnapshot(options?)` | Comparison against an auto-named snapshot |

---

Source: https://playwright.dev/docs/api/class-snapshotassertions
