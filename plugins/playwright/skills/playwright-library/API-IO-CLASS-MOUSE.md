# Playwright — class: Mouse

> **Manifest:** 6 methods, 0 properties, 0 events.
> Complete mouse control in CSS pixel coordinates relative to the top-left viewport corner.
> Access: `page.mouse`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Complete example: drawing a drag rectangle](#complete-example-drawing-a-drag-rectangle)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Mouse` emulates all mouse interactions of the browser. The coordinates refer
to the main frame viewport. The instance is reachable via `page.mouse`.

---

## Methods

### mouse.click(x, y, options?)

Combination of `move()`, `down()` and `up()` — clicks at a coordinate.

**Signature:**
```typescript
mouse.click(x: number, y: number, options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
  delay?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `x` | `number` | yes | — | X coordinate in CSS pixels |
| `y` | `number` | yes | — | Y coordinate in CSS pixels |
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Which mouse button |
| `options.clickCount` | `number` | no | `1` | Number of clicks (for single/double click etc.) |
| `options.delay` | `number` | no | `0` | Milliseconds between mousedown and mouseup |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.mouse.click(100, 200);
await page.mouse.click(100, 200, { button: 'right' });
await page.mouse.click(100, 200, { clickCount: 2, delay: 50 });
```

---

### mouse.dblclick(x, y, options?)

Double click: `move()`, `down()`, `up()`, `down()`, `up()`.

**Signature:**
```typescript
mouse.dblclick(x: number, y: number, options?: {
  button?: 'left' | 'right' | 'middle';
  delay?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `x` | `number` | yes | — | X coordinate in CSS pixels |
| `y` | `number` | yes | — | Y coordinate in CSS pixels |
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Which mouse button |
| `options.delay` | `number` | no | `0` | Milliseconds between the individual clicks |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.mouse.dblclick(150, 300);
```

---

### mouse.down(options?)

Sends a `mousedown` event at the current mouse position.

**Signature:**
```typescript
mouse.down(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Which mouse button is pressed |
| `options.clickCount` | `number` | no | `1` | Click count in the event (relevant for double-click sequences) |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.mouse.move(100, 100);
await page.mouse.down();
```

---

### mouse.move(x, y, options?)

Moves the mouse to the given coordinates. Sends `mousemove` events.

**Signature:**
```typescript
mouse.move(x: number, y: number, options?: {
  steps?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `x` | `number` | yes | — | Target X coordinate in CSS pixels |
| `y` | `number` | yes | — | Target Y coordinate in CSS pixels |
| `options.steps` | `number` | no | `1` | Number of interpolated intermediate positions (produces several mousemove events) |

**Returns:** `Promise<void>`

**Example:**
```javascript
// Direct movement
await page.mouse.move(200, 300);

// Smooth movement with intermediate points (e.g. for hover animations)
await page.mouse.move(200, 300, { steps: 10 });
```

---

### mouse.up(options?)

Sends a `mouseup` event at the current mouse position.

**Signature:**
```typescript
mouse.up(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Which mouse button is released |
| `options.clickCount` | `number` | no | `1` | Click count in the event |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.mouse.up();
```

---

### mouse.wheel(deltaX, deltaY)

Simulates a mouse wheel event (horizontal and vertical scrolling).

**Signature:**
```typescript
mouse.wheel(deltaX: number, deltaY: number): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `deltaX` | `number` | yes | — | Horizontal scroll delta in pixels (positive = right) |
| `deltaY` | `number` | yes | — | Vertical scroll delta in pixels (positive = down) |

**Returns:** `Promise<void>`

**Note:** The `wheel` event can trigger scrolling without waiting for
the scrolling to complete. If needed, afterwards await `page.waitForTimeout()` or
a visible state change.

**Example:**
```javascript
// Scroll down
await page.mouse.wheel(0, 500);

// Scroll horizontally
await page.mouse.wheel(200, 0);
```

---

## Complete example: drawing a drag rectangle

```javascript
// Draw a square from (0,0) to (100,100) (drag gesture)
await page.mouse.move(0, 0);
await page.mouse.down();
await page.mouse.move(0, 100);
await page.mouse.move(100, 100);
await page.mouse.move(100, 0);
await page.mouse.move(0, 0);
await page.mouse.up();
```

---

## Properties

No public properties.

## Events

No own events — mouse interactions trigger events on the page
elements, not on the Mouse object itself.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 6      |
| Properties | 0     |
| Events    | 0      |

**Summary:** `click()` and `dblclick()` cover the majority of use cases.
`down()` / `move()` / `up()` are needed for drag-and-drop or complex
mouse gestures. `wheel()` is the only scroll method at the mouse level.

---

*Source: https://playwright.dev/docs/api/class-mouse*
