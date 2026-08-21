# Playwright — class: Video

> **Manifest:** 3 methods, 0 properties, 0 events.
> Represents the video recording of a browser page.
> Available when the BrowserContext was created with the `recordVideo` option.
> Access: `page.video()`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [BrowserContext configuration for video](#browsercontext-configuration-for-video)
- [Typical usage scenarios](#typical-usage-scenarios)
- [Manifest](#manifest)

## Overview

`Video` gives access to the recorded video file of a page
session. Videos are only written completely once the BrowserContext
is closed. `saveAs()` can be called safely while the
recording is still running.

```javascript
const context = await browser.newContext({
  recordVideo: {
    dir: './videos/',
    size: { width: 1280, height: 720 }
  }
});
const page = await context.newPage();
await page.goto('https://example.com');
// ... interactions ...
await context.close(); // the video is saved now
const videoPath = await page.video().path();
```

---

## Methods

### video.delete()

Deletes the video file. Waits for the recording to finish if necessary.

**Signature:**
```typescript
video.delete(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.11

**Example:**
```javascript
// Delete the video after the test (e.g. when the test passed)
await page.video().delete();
```

---

### video.path()

Returns the filesystem path under which the video is stored.
The video is guaranteed to be written as soon as the BrowserContext has been
closed.

**Signature:**
```typescript
video.path(): Promise<string>
```

**Parameters:** None

**Returns:** `Promise<string>` — absolute file path to the video file

**Added:** Before v1.9

**Note:** Throws an error when Playwright is connected to a remote browser
(no local filesystem control).

**Example:**
```javascript
const path = await page.video().path();
console.log('Video saved at:', path);
// e.g. "./videos/test-2024-01-15-abc123.webm"
```

---

### video.saveAs(path)

Saves the video at a custom path. Safe to call while
recording is running and after the page has been closed.

**Signature:**
```typescript
video.saveAs(path: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `path` | `string` | yes | — | Target file path including file name (absolute or relative to the CWD) |

**Returns:** `Promise<void>`

**Added:** v1.11

**Example:**
```javascript
await page.video().saveAs('/recordings/test-login-flow.webm');
```

---

## BrowserContext configuration for video

```javascript
const context = await browser.newContext({
  recordVideo: {
    dir: './test-videos/',     // directory for automatic videos
    size: {
      width: 1280,
      height: 720
    }
  }
});
```

With Playwright Test (`playwright.config.ts`):

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on-first-retry',    // 'off' | 'on' | 'retain-on-failure' | 'on-first-retry'
  }
});
```

---

## Typical usage scenarios

### Keep the video only on failure

```javascript
// In a Playwright test
test('my test', async ({ page }, testInfo) => {
  const context = await browser.newContext({ recordVideo: { dir: './videos' } });
  const page = await context.newPage();

  try {
    await page.goto('https://example.com');
    // ... test steps ...
  } finally {
    await context.close();
    if (testInfo.status !== 'passed') {
      await page.video()?.saveAs(testInfo.outputPath('video.webm'));
    } else {
      await page.video()?.delete();
    }
  }
});
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 3      |
| Properties | 0     |
| Events    | 0      |

**Summary:** `saveAs()` is the most important method — it allows videos
to be stored deliberately and independently of the default location. `path()` returns
the automatically chosen path. `delete()` enables explicit
cleanup, e.g. for passed tests, in order to save disk space.

---

*Source: https://playwright.dev/docs/api/class-video*
