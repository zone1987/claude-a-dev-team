# Playwright Downloads, Dialogs, Navigation and Touch Events - Complete Reference

---

## Contents

- [1. Downloads](#1-downloads)
- [2. Dialogs](#2-dialogs)
- [3. Navigation and Waiting](#3-navigation-and-waiting)
- [4. Touch Events and Gestures](#4-touch-events-and-gestures)
- [5. File Chooser (file upload)](#5-file-chooser-file-upload)

## 1. Downloads

### Basic principle

Every download fires the `'download'` event on the page. The file is
first placed in a temporary directory. Downloads are deleted when the
browser context is closed.

### Intercepting a download

```typescript
// Safe: set up the promise before the click
const downloadPromise = page.waitForEvent('download');
await page.getByText('Download Report').click();
const download = await downloadPromise;

// File name and path
console.log(download.suggestedFilename()); // e.g. 'report-2024.pdf'
const tmpPath = await download.path();     // Temporary path

// Save under your own path
await download.saveAs('./downloads/' + download.suggestedFilename());
```

### Download object - all methods

| Method | Returns | Description |
|---------|-----------|--------------|
| `download.url()` | `string` | Original URL of the download |
| `download.suggestedFilename()` | `string` | Suggested file name (from Content-Disposition or URL) |
| `download.path()` | `Promise<string>` | Path to the temp file (waits for completion, throws on error) |
| `download.saveAs(path)` | `Promise<void>` | Copies the download to your own path |
| `download.failure()` | `Promise<string \| null>` | Error message if it failed |
| `download.createReadStream()` | `Promise<Readable>` | Readable stream (only on success) |
| `download.cancel()` | `Promise<void>` | Cancel the download (no exception if already finished) |
| `download.delete()` | `Promise<void>` | Delete the temp file |
| `download.page()` | `Page` | Triggering page object |

### Event-based handling

```typescript
// Log all downloads of a session
page.on('download', async download => {
  const path = await download.path();
  console.log(`Downloaded: ${download.suggestedFilename()} -> ${path}`);
});
```

### Configuring the download path

```typescript
// Persistent download directory (no automatic deletion)
const browser = await chromium.launch();
const context = await browser.newContext({
  acceptDownloads: true, // Default: true
});
```

### Awaiting a download with a predicate

```typescript
const pdfDownload = await page.waitForEvent('download', {
  predicate: d => d.suggestedFilename().endsWith('.pdf'),
  timeout: 30000,
});
```

### Complete example

```typescript
test('download and verify CSV', async ({ page }) => {
  await page.goto('/reports');

  const downloadPromise = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Export CSV' }).click();
  const download = await downloadPromise;

  expect(download.suggestedFilename()).toMatch(/report.*\.csv$/);

  const savePath = `./test-results/${download.suggestedFilename()}`;
  await download.saveAs(savePath);

  const content = fs.readFileSync(savePath, 'utf-8');
  expect(content).toContain('Date,Amount');
});
```

---

## 2. Dialogs

Playwright closes dialogs automatically by default (dismiss). Custom
handlers must be registered BEFORE the triggering action.

**Important:** An unhandled dialog blocks the page (modal). Without a
handler it is dismissed automatically.

### Dialog types

| Type | Description | accept() behavior |
|-----|--------------|-------------------|
| `'alert'` | Simple message | Close |
| `'confirm'` | Confirmation | OK (true) |
| `'prompt'` | Text input | OK with the entered text |
| `'beforeunload'` | Navigation warning | Confirm leaving |

### Dialog methods

| Method | Returns | Description |
|---------|-----------|--------------|
| `dialog.type()` | `string` | `'alert'`, `'confirm'`, `'prompt'`, `'beforeunload'` |
| `dialog.message()` | `string` | Displayed message |
| `dialog.defaultValue()` | `string` | Prefilled value on a prompt (otherwise empty) |
| `dialog.accept(promptText?)` | `Promise<void>` | Accept the dialog; on a prompt: enter text |
| `dialog.dismiss()` | `Promise<void>` | Dismiss the dialog (Cancel) |
| `dialog.page()` | `Page \| null` | Triggering page object |

### Alert

```typescript
page.on('dialog', dialog => dialog.dismiss()); // or accept()
await page.evaluate(() => alert('Hello!'));
```

### Confirm

```typescript
// Confirm
page.on('dialog', dialog => {
  expect(dialog.type()).toBe('confirm');
  expect(dialog.message()).toBe('Really delete?');
  dialog.accept();
});
await page.getByRole('button', { name: 'Delete' }).click();

// Dismiss
page.on('dialog', dialog => dialog.dismiss());
await page.getByRole('button', { name: 'Delete' }).click();
```

### Prompt

```typescript
page.on('dialog', async dialog => {
  expect(dialog.type()).toBe('prompt');
  expect(dialog.defaultValue()).toBe('Your name');
  await dialog.accept('Alice');
});
await page.evaluate("prompt('Your name', 'Your name')");
```

### once pattern (recommended)

```typescript
// Register a one-time dialog handler with once
page.once('dialog', dialog => dialog.accept('2024-01-01'));
await page.getByRole('button', { name: 'Enter date' }).click();
```

### beforeunload

```typescript
page.on('dialog', async dialog => {
  expect(dialog.type()).toBe('beforeunload');
  await dialog.dismiss(); // Stay on the page
  // or: await dialog.accept(); // Leave the page
});

// runBeforeUnload triggers the dialog
await page.close({ runBeforeUnload: true });
// Note: page.close() does NOT wait for the close to complete
```

### Print dialog (window.print)

```typescript
// Override window.print before the button is clicked
await page.goto('/invoice');
await page.evaluate(() => {
  window.waitForPrintDialog = new Promise(resolve => {
    window.print = resolve as any;
  });
});
await page.getByText('Print').click();
await page.waitForFunction(() => (window as any).waitForPrintDialog);
```

---

## 3. Navigation and Waiting

### page.goto(url, options?)

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `url` | `string` | - | Target URL |
| `waitUntil` | `'load' \| 'domcontentloaded' \| 'networkidle' \| 'commit'` | `'load'` | When to consider it complete |
| `timeout` | `number` | `30000` | Timeout in ms |
| `referer` | `string` | - | Referer header |

```typescript
await page.goto('https://example.com');
await page.goto('/dashboard', { waitUntil: 'networkidle' });
await page.goto('/fast-page', { waitUntil: 'domcontentloaded' });
```

### waitUntil values

| Value | Description |
|------|--------------|
| `'load'` | Load event fired |
| `'domcontentloaded'` | DOMContentLoaded fired |
| `'networkidle'` | No network requests for 500ms |
| `'commit'` | Network response received and navigation started |

### page.waitForURL(url, options?)

| Parameter | Type | Description |
|-----------|-----|--------------|
| `url` | `string \| RegExp \| (url: URL) => boolean` | Expected URL |
| `options.waitUntil` | as in goto | Wait state |
| `options.timeout` | `number` | Timeout in ms |

```typescript
// Wait after clicking a link
await page.getByRole('button', { name: 'Submit' }).click();
await page.waitForURL('/confirmation');

// With a regex
await page.waitForURL(/\/orders\/\d+/);

// With a predicate
await page.waitForURL(url => url.searchParams.get('status') === 'success');
```

### page.waitForLoadState(state?, options?)

| Parameter | Type | Default | Description |
|-----------|-----|---------|--------------|
| `state` | `'load' \| 'domcontentloaded' \| 'networkidle'` | `'load'` | Target state |
| `options.timeout` | `number` | - | Timeout in ms |

```typescript
await page.waitForLoadState('networkidle');
await page.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

### Navigation pattern (click + wait)

```typescript
// Wait for navigation and click simultaneously
await Promise.all([
  page.waitForURL('/dashboard'),
  page.getByRole('button', { name: 'Login' }).click(),
]);

// Wait for a network request
const [response] = await Promise.all([
  page.waitForResponse('**/api/user'),
  page.click('#refresh'),
]);
const data = await response.json();

// Await navigation after SPA routing
await page.locator('nav a').filter({ hasText: 'Profile' }).click();
await page.waitForURL('**/profile');
await page.waitForLoadState('networkidle');
```

### Navigation events

```typescript
page.on('domcontentloaded', () => console.log('DOM ready'));
page.on('load', () => console.log('Page loaded'));
page.on('framenavigated', frame => {
  if (frame === page.mainFrame()) {
    console.log('Main frame navigated to:', frame.url());
  }
});
```

### Hydration problems

With SSR frameworks the page can be visually finished while the JS has not
hydrated yet.

```typescript
// Wait until the element is interactive (not just visible)
await page.locator('#checkout-button').click(); // Auto-waits until enabled

// Wait explicitly
await expect(page.locator('#form')).toBeEnabled();
await page.locator('#form input[name="email"]').fill('test@example.com');
```

---

## 4. Touch Events and Gestures

Playwright supports legacy touch events (TouchEvent API) via
`locator.dispatchEvent()`.

**Note:** `dispatchEvent()` sets `Event.isTrusted = false`. Apps that
check isTrusted have to be adapted.

### locator.dispatchEvent(type, eventInit?)

| Parameter | Type | Description |
|-----------|-----|--------------|
| `type` | `string` | Event type: `'touchstart'`, `'touchmove'`, `'touchend'` |
| `eventInit` | `Object` | TouchEvent properties |

### TouchEvent properties

| Property | Type | Description |
|-------------|-----|--------------|
| `touches` | `Touch[]` | Current touch points |
| `targetTouches` | `Touch[]` | Touch points on the target |
| `changedTouches` | `Touch[]` | Changed touch points |

### Touch object properties

| Property | Type | Description |
|-------------|-----|--------------|
| `identifier` | `number` | Unique ID of the touch point |
| `clientX` | `number` | X coordinate relative to the viewport |
| `clientY` | `number` | Y coordinate relative to the viewport |
| `pageX` | `number` | X coordinate relative to the page |
| `pageY` | `number` | Y coordinate relative to the page |

### Device configuration for touch

```typescript
test.use({ ...devices['Pixel 7'] });
// or manually:
test.use({ hasTouch: true, isMobile: true });
```

---

### Pan gesture (swipe/move)

```typescript
async function pan(
  locator: Locator,
  deltaX = 0,
  deltaY = 0,
  steps = 5
): Promise<void> {
  const box = await locator.boundingBox();
  if (!box) throw new Error('Element not visible');

  const centerX = box.x + box.width / 2;
  const centerY = box.y + box.height / 2;

  await locator.dispatchEvent('touchstart', {
    touches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
    targetTouches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
    changedTouches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
  });

  for (let i = 1; i <= steps; i++) {
    const x = centerX + (deltaX * i) / steps;
    const y = centerY + (deltaY * i) / steps;
    await locator.dispatchEvent('touchmove', {
      touches: [{ identifier: 0, clientX: x, clientY: y }],
      targetTouches: [{ identifier: 0, clientX: x, clientY: y }],
      changedTouches: [{ identifier: 0, clientX: x, clientY: y }],
    });
  }

  await locator.dispatchEvent('touchend', {
    touches: [],
    targetTouches: [],
    changedTouches: [{ identifier: 0, clientX: centerX + deltaX, clientY: centerY + deltaY }],
  });
}

// Usage
test('map pan', async ({ page }) => {
  test.use({ ...devices['Pixel 7'] });
  await page.goto('https://www.google.com/maps');
  const map = page.locator('#map');
  for (let i = 0; i < 5; i++) {
    await pan(map, 100, 0); // 100px to the right
  }
  await expect(page).toHaveScreenshot('map-panned.png');
});
```

---

### Pinch gesture (zoom in/out)

```typescript
async function pinch(
  locator: Locator,
  arg: { deltaX?: number; steps?: number; direction?: 'in' | 'out' } = {}
): Promise<void> {
  const { deltaX = 50, steps = 5, direction = 'in' } = arg;
  const box = await locator.boundingBox();
  if (!box) throw new Error('Element not visible');

  const centerX = box.x + box.width / 2;
  const centerY = box.y + box.height / 2;

  // Initial input: two points around the center
  const startDistance = direction === 'in' ? deltaX : 0;
  await locator.dispatchEvent('touchstart', {
    touches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
    targetTouches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
    changedTouches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
  });

  for (let i = 1; i <= steps; i++) {
    const offset = direction === 'in'
      ? deltaX - (deltaX * i) / steps  // Bring the points together
      : (deltaX * i) / steps;           // Pull the points apart

    await locator.dispatchEvent('touchmove', {
      touches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
      targetTouches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
      changedTouches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
    });
  }

  const endOffset = direction === 'in' ? 0 : deltaX;
  await locator.dispatchEvent('touchend', {
    touches: [],
    targetTouches: [],
    changedTouches: [
      { identifier: 0, clientX: centerX - endOffset, clientY: centerY },
      { identifier: 1, clientX: centerX + endOffset, clientY: centerY },
    ],
  });
}

// Usage
test('map zoom', async ({ page }) => {
  await page.goto('https://www.google.com/maps');
  const map = page.locator('#map');

  // Zoom in
  for (let i = 0; i < 3; i++) {
    await pinch(map, { direction: 'out', deltaX: 80 }); // pulling fingers apart = zoom in
  }
  // Zoom out
  for (let i = 0; i < 3; i++) {
    await pinch(map, { direction: 'in', deltaX: 80 }); // bringing fingers together = zoom out
  }
});
```

---

## 5. File Chooser (file upload)

```typescript
// File upload via the file dialog
const fileChooserPromise = page.waitForEvent('filechooser');
await page.getByLabel('Upload avatar').click();
const fileChooser = await fileChooserPromise;

// Single file
await fileChooser.setFiles('./fixtures/avatar.png');

// Multiple files
await fileChooser.setFiles(['./a.pdf', './b.pdf']);

// File object without a file on disk
await fileChooser.setFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('file content'),
});
```

---

Source: https://playwright.dev/docs/downloads | https://playwright.dev/docs/dialogs | https://playwright.dev/docs/navigations | https://playwright.dev/docs/touch-events | https://playwright.dev/docs/api/class-download | https://playwright.dev/docs/api/class-dialog
