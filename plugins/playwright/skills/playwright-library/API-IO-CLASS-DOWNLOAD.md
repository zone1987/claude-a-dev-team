# Playwright — class: Download

> **Manifest:** 9 methods, 0 properties, 0 events (1 external page event).
> Represents a started or completed file download operation.
> Instances are obtained via `page.on('download')` or `page.waitForEvent('download')`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Page event: 'download'](#page-event-download)
- [Complete example](#complete-example)
- [Manifest](#manifest)

## Overview

`Download` objects are created when a page triggers a download.
Playwright stores downloaded files temporarily in the system temp
directory; they are deleted automatically when the context closes.
For permanent storage `saveAs()` must be called.

```javascript
const downloadPromise = page.waitForEvent('download');
await page.getByText('Download').click();
const download = await downloadPromise;
await download.saveAs('/tmp/my-file.pdf');
```

---

## Methods

### download.cancel()

Cancels the running download. Does not fail if the download
has already completed or been cancelled.

**Signature:**
```typescript
download.cancel(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.13

**Example:**
```javascript
await download.cancel();
```

---

### download.createReadStream()

Returns a readable Node.js stream for the downloaded content.
Throws an error for a failed or cancelled download.

**Signature:**
```typescript
download.createReadStream(): Promise<Readable>
```

**Parameters:** None

**Returns:** `Promise<Readable>` — Node.js readable stream

**Added:** v1.9

**Example:**
```javascript
const stream = await download.createReadStream();
const chunks: Buffer[] = [];
for await (const chunk of stream) {
  chunks.push(Buffer.from(chunk));
}
const content = Buffer.concat(chunks).toString('utf-8');
```

---

### download.delete()

Deletes the downloaded temporary file. Waits for the download to
complete if necessary.

**Signature:**
```typescript
download.delete(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.9

**Example:**
```javascript
await download.delete();
```

---

### download.failure()

Returns the error text if the download failed.
Returns `null` for a successful download. Waits for completion if necessary.

**Signature:**
```typescript
download.failure(): Promise<null | string>
```

**Parameters:** None

**Returns:** `Promise<null | string>` — error string or `null`

**Added:** v1.9

**Example:**
```javascript
const error = await download.failure();
if (error) {
  console.error('Download failed:', error);
}
```

---

### download.page()

Returns the page this download belongs to.

**Signature:**
```typescript
download.page(): Page
```

**Parameters:** None

**Returns:** `Page`

**Added:** v1.12

**Example:**
```javascript
const sourcePage = download.page();
console.log('Download from:', sourcePage.url());
```

---

### download.path()

Returns the absolute file path to the downloaded temporary file.
Throws an error for a failed or cancelled download.
Waits for completion if necessary.

**Signature:**
```typescript
download.path(): Promise<string>
```

**Parameters:** None

**Returns:** `Promise<string>` — absolute path to the temporary file

**Added:** v1.9

**Note:** The path is only valid while the BrowserContext is open.

**Example:**
```javascript
const tmpPath = await download.path();
console.log('Temporary path:', tmpPath);
```

---

### download.saveAs(path)

Copies the downloaded file to the given path. Safe to call while
the download is still running.

**Signature:**
```typescript
download.saveAs(path: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `path` | `string` | yes | — | Target file path (absolute or relative to the CWD) |

**Returns:** `Promise<void>`

**Added:** v1.9

**Example:**
```javascript
await download.saveAs('/downloads/' + download.suggestedFilename());
```

---

### download.suggestedFilename()

Returns the filename suggested by the browser (from the
`Content-Disposition` header or the `download` attribute).

**Signature:**
```typescript
download.suggestedFilename(): string
```

**Parameters:** None

**Returns:** `string` — suggested filename

**Added:** v1.9

**Example:**
```javascript
console.log(download.suggestedFilename()); // e.g. "report-2024.pdf"
await download.saveAs('/tmp/' + download.suggestedFilename());
```

---

### download.url()

Returns the URL the file was downloaded from.

**Signature:**
```typescript
download.url(): string
```

**Parameters:** None

**Returns:** `string` — download URL

**Added:** v1.9

**Example:**
```javascript
console.log('Download URL:', download.url());
```

---

## Page event: 'download'

```javascript
page.on('download', async (download) => {
  console.log('New download:', download.suggestedFilename());
  await download.saveAs('./downloads/' + download.suggestedFilename());
});
```

Or as a one-time wait:

```javascript
const download = await page.waitForEvent('download');
```

---

## Complete example

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();
const context = await browser.newContext({ acceptDownloads: true });
const page = await context.newPage();
await page.goto('https://example.com/downloads');

const downloadPromise = page.waitForEvent('download');
await page.click('#download-button');
const download = await downloadPromise;

// Error check
const err = await download.failure();
if (err) throw new Error(err);

// Save
await download.saveAs(`/tmp/${download.suggestedFilename()}`);
console.log('Saved:', download.suggestedFilename());

await browser.close();
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 9      |
| Properties | 0     |
| Events    | 0 (1 page event: 'download') |

**Conclusion:** `saveAs()` + `suggestedFilename()` are the core methods for
typical download tests. `failure()` should always be checked before
`path()` is called. `createReadStream()` allows in-memory processing
without intermediate storage.

---

*Source: https://playwright.dev/docs/api/class-download*
