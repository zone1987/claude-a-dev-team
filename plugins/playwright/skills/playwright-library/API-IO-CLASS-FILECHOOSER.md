# Playwright — class: FileChooser

> **Manifest:** 4 methods, 0 properties, 0 events (1 external page event).
> Represents a file selection dialog opened by the browser.
> Instances are obtained via `page.on('filechooser')` or `page.waitForEvent('filechooser')`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Page event: 'filechooser'](#page-event-filechooser)
- [Manifest](#manifest)

## Overview

`FileChooser` is created when an `<input type="file">` element is activated.
The dialog is not actually opened — Playwright intercepts it and
allows files to be set programmatically via `setFiles()`.

```javascript
const fileChooserPromise = page.waitForEvent('filechooser');
await page.getByText('Upload file').click();
const fileChooser = await fileChooserPromise;
await fileChooser.setFiles('/path/to/myfile.pdf');
```

---

## Methods

### fileChooser.element()

Returns the `<input type="file">` element that triggered the
FileChooser.

**Signature:**
```typescript
fileChooser.element(): ElementHandle
```

**Parameters:** None

**Returns:** `ElementHandle` — the input element

**Added:** Before v1.9

**Example:**
```javascript
const input = fileChooser.element();
const accept = await input.getAttribute('accept');
console.log('Allowed types:', accept); // e.g. ".pdf,.docx"
```

---

### fileChooser.isMultiple()

Indicates whether the FileChooser accepts several files at once
(`multiple` attribute set).

**Signature:**
```typescript
fileChooser.isMultiple(): boolean
```

**Parameters:** None

**Returns:** `boolean` — `true` if `multiple` is set

**Added:** Before v1.9

**Example:**
```javascript
if (fileChooser.isMultiple()) {
  await fileChooser.setFiles(['/path/file1.jpg', '/path/file2.jpg']);
} else {
  await fileChooser.setFiles('/path/file1.jpg');
}
```

---

### fileChooser.page()

Returns the page this FileChooser belongs to.

**Signature:**
```typescript
fileChooser.page(): Page
```

**Parameters:** None

**Returns:** `Page`

**Added:** Before v1.9

**Example:**
```javascript
const p = fileChooser.page();
console.log('Page:', p.url());
```

---

### fileChooser.setFiles(files, options?)

Sets the files for the input element, thereby setting the dialog selection.

**Signature:**
```typescript
fileChooser.setFiles(
  files: string | Array<string> | {
    name: string;
    mimeType: string;
    buffer: Buffer;
  } | Array<{
    name: string;
    mimeType: string;
    buffer: Buffer;
  }>,
  options?: {
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `files` | `string \| string[] \| FilePayload \| FilePayload[]` | yes | — | File path(s) or file buffer objects. Relative paths are resolved relative to the CWD. An empty array clears the selection. |
| `files[].name` | `string` | yes (with buffer) | — | File name including extension |
| `files[].mimeType` | `string` | yes (with buffer) | — | MIME type, e.g. `"application/pdf"` |
| `files[].buffer` | `Buffer` | yes (with buffer) | — | File content as a buffer |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated; has no effect anymore |
| `options.timeout` | `number` | no | `0` | Maximum wait time in milliseconds (`0` = no timeout) |

**Returns:** `Promise<void>`

**Added:** Before v1.9

**Examples:**

```javascript
// Simple path
await fileChooser.setFiles('/home/user/document.pdf');

// Several paths
await fileChooser.setFiles([
  '/home/user/bild1.jpg',
  '/home/user/bild2.jpg'
]);

// In-memory buffer (no real filesystem needed)
await fileChooser.setFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('File content here')
});

// Reset the selection
await fileChooser.setFiles([]);
```

---

## Page event: 'filechooser'

```javascript
page.on('filechooser', async (fileChooser) => {
  await fileChooser.setFiles('/path/to/file.jpg');
});
```

Or as a one-off wait before the triggering click:

```javascript
const [fileChooser] = await Promise.all([
  page.waitForEvent('filechooser'),
  page.click('#upload-button')
]);
await fileChooser.setFiles('/path/to/file.jpg');
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 4      |
| Properties | 0     |
| Events    | 0 (1 page event: 'filechooser') |

**Conclusion:** `setFiles()` is the only relevant action method. `isMultiple()`
should be checked before setting several files. The buffer variant
of `setFiles()` is particularly useful in CI environments where no real
filesystem fixture is needed.

---

*Source: https://playwright.dev/docs/api/class-filechooser*
