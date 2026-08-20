# class-playwright

The `Playwright` object is the root entry point of the Playwright API. It is provided by `require('playwright')` or the test runner and contains the browser types as well as global helper objects.

Methods: 0 | Properties: 6 | Events: 0

---

## Contents

- [Properties](#properties)
- [Import Patterns](#import-patterns)
- [Manifest](#manifest)

## Properties

### playwright.chromium

**Type:** `BrowserType`

Object for launching or connecting to Chromium browser instances (including Chrome and Edge via the `channel` option).

```js
const { chromium } = require('playwright');
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();
```

---

### playwright.firefox

**Type:** `BrowserType`

Object for launching or connecting to Firefox browser instances.

```js
const { firefox } = require('playwright');
const browser = await firefox.launch();
```

---

### playwright.webkit

**Type:** `BrowserType`

Object for launching or connecting to WebKit browser instances (Safari engine).

```js
const { webkit } = require('playwright');
const browser = await webkit.launch();
```

---

### playwright.devices

**Type:** `Object`

Dictionary of predefined device descriptors for mobile emulation. Can be used with `browser.newContext()` or `browser.newPage()` (spread operator).

**Available devices:** All devices listed in the [Playwright device descriptors](https://playwright.dev/docs/emulation#devices), e.g. `"iPhone 15"`, `"Pixel 7"`, `"Galaxy S9+"`, etc.

Each entry contains: `userAgent`, `viewport`, `deviceScaleFactor`, `isMobile`, `hasTouch`, `defaultBrowserType`.

```js
const { webkit, devices } = require('playwright');
const iPhone = devices['iPhone 15'];

const browser = await webkit.launch();
const context = await browser.newContext({
  ...iPhone,
  locale: 'de-DE',
});
const page = await context.newPage();
await page.goto('https://example.com');
```

---

### playwright.request

**Type:** `APIRequest`

Singleton instance of the `APIRequest` class for creating independent `APIRequestContext` instances (without a browser context).

```js
const { request } = require('playwright');
const context = await request.newContext({
  baseURL: 'https://api.example.com',
  extraHTTPHeaders: { 'Authorization': 'Bearer token123' },
});
const response = await context.get('/users');
console.log(await response.json());
await context.dispose();
```

---

### playwright.selectors

**Type:** `Selectors`

Allows installing custom selector engines (e.g. data-binding selectors for specific frameworks).

```js
const { selectors, chromium } = require('playwright');

// Register a selector engine
await selectors.register('tag', {
  query(root, selector) {
    return root.querySelector(selector);
  },
  queryAll(root, selector) {
    return Array.from(root.querySelectorAll(selector));
  },
});

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
const element = await page.locator('tag=h1');
```

---

### playwright.errors

**Type:** `Object`

Contains error classes thrown by Playwright methods.

**Sub-properties:**

| Property | Type | Description |
|----------|------|-------------|
| `TimeoutError` | Function | Thrown when a timeout expires |

```js
const { errors } = require('playwright');

try {
  await page.locator('.nonexistent').waitFor({ timeout: 1000 });
} catch (e) {
  if (e instanceof errors.TimeoutError) {
    console.log('Element not found within the timeout');
  }
}
```

---

## Import Patterns

```js
// CommonJS
const { chromium, firefox, webkit, devices, request, selectors } = require('playwright');

// ES Modules
import { chromium, firefox, webkit, devices } from 'playwright';

// In the Playwright test framework (injected automatically)
import { test, expect } from '@playwright/test';
// browserType via test.use({ browserName: 'chromium' })
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 0 |
| Properties | 6 |
| Events | 0 |

**Conclusion:** The `Playwright` object is a pure namespace without methods of its own. The three BrowserType properties (`chromium`, `firefox`, `webkit`) are the starting point of every browser interaction. `devices` and `request` are global helper objects for device emulation and standalone API tests respectively.

---

Source: https://playwright.dev/docs/api/class-playwright
