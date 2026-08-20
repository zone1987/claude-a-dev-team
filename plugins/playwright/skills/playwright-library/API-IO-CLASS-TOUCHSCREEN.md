# Playwright — class: Touchscreen

> **Manifest:** 1 method, 0 properties, 0 events.
> Simulates touch gestures. Only available when the BrowserContext was created with `hasTouch: true`.
> Access: `page.touchscreen`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Manual multi-touch gestures](#manual-multi-touch-gestures)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Touchscreen` allows sending touch events to the browser. The class
is limited to a single tap command; more complex gestures (pinch,
swipe, multi-touch) must be implemented manually via
`page.dispatchEvent()`.

**Prerequisite:** the BrowserContext must be created with `hasTouch: true`:

```javascript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
```

---

## Methods

### touchscreen.tap(x, y)

Sends a `touchstart` followed by a `touchend` event at the
given position.

**Signature:**
```typescript
touchscreen.tap(x: number, y: number): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `x` | `number` | yes | — | X coordinate in CSS pixels, relative to the main frame viewport |
| `y` | `number` | yes | — | Y coordinate in CSS pixels, relative to the main frame viewport |

**Returns:** `Promise<void>`

**Notes:**
- Throws an error if `hasTouch` was not enabled in the BrowserContext.
- Triggers `touchstart` + `touchend`; no `touchmove`.
- Coordinates refer to the main frame — with iframes, calculate the offset
  if necessary.

**Example:**
```javascript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
await page.goto('https://example.com');
await page.touchscreen.tap(150, 200);
```

---

## Manual multi-touch gestures

Since `Touchscreen` only offers `tap()`, more complex gestures are implemented via
`page.dispatchEvent()`:

```javascript
// Swipe to the left (touchstart -> touchmove -> touchend)
const element = await page.$('#swipeable');
const box = await element.boundingBox();

await page.dispatchEvent('#swipeable', 'touchstart', {
  touches: [{ clientX: box.x + box.width / 2, clientY: box.y + box.height / 2 }]
});
await page.dispatchEvent('#swipeable', 'touchmove', {
  touches: [{ clientX: box.x, clientY: box.y + box.height / 2 }]
});
await page.dispatchEvent('#swipeable', 'touchend', { touches: [] });
```

---

## Properties

No public properties.

## Events

No events of its own.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 1      |
| Properties | 0     |
| Events    | 0      |

**Summary:** the class is deliberately kept minimal. For simple touch tests
`tap()` is sufficient. For realistic mobile emulation, the combination with
`page.emulate({ device: playwright.devices['iPhone 14'] })` and
`hasTouch: true` in the context is recommended. Complex gestures require manual
`dispatchEvent`.

---

*Source: https://playwright.dev/docs/api/class-touchscreen*
