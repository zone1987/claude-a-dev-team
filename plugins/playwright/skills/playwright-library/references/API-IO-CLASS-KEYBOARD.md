# Playwright — class: Keyboard

> **Manifest:** 5 methods, 0 properties, 0 events.
> Provides complete keyboard control via keydown/keyup/press/type/insertText.
> Modifier combinations such as `Control+A` are supported natively.
> Access: `page.keyboard`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Keyboard` controls the browser's virtual keyboard. All coordinates operate
in the context of the currently focused element. The instance is reachable via
`page.keyboard` and cannot be instantiated directly.

---

## Methods

### keyboard.down(key)

Sends a `keydown` event for the given key.

**Signature:**
```typescript
keyboard.down(key: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `key` | `string` | yes | — | Key name or single character, e.g. `"ArrowLeft"`, `"a"`, `"F5"` |

**Supported keys (selection):**
F1–F12, Digit0–Digit9, KeyA–KeyZ, Backquote, Minus, Equal, Backslash,
Backspace, Tab, Delete, Escape, ArrowLeft, ArrowRight, ArrowUp, ArrowDown,
End, Enter, Home, Insert, PageDown, PageUp, Space,
Shift, Control, Alt, Meta, ShiftLeft, ControlOrMeta

`ControlOrMeta` resolves automatically to `Control` (Windows/Linux) or
`Meta` (macOS).

**Returns:** `Promise<void>`

**Notes:**
- Modifier keys (Shift, Control etc.) affect the character case
  of subsequent `type()` calls.
- Repeated `down()` without an intervening `up()` sets `repeat: true`.

**Example:**
```javascript
// Press Shift, then type the letter A (uppercase), then release Shift
await page.keyboard.down('Shift');
await page.keyboard.press('KeyA');
await page.keyboard.up('Shift');
```

---

### keyboard.up(key)

Sends a `keyup` event for the given key.

**Signature:**
```typescript
keyboard.up(key: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `key` | `string` | yes | — | Key name or character; same values as for `down()` |

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.keyboard.up('Shift');
```

---

### keyboard.press(key, options?)

Combination of `down()` and `up()`. Sends keydown, optionally waits, sends keyup.

**Signature:**
```typescript
keyboard.press(key: string, options?: {
  delay?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `key` | `string` | yes | — | Key name or character. Shortcuts such as `"Control+o"`, `"Shift+T"`, `"ControlOrMeta+A"` are possible |
| `options.delay` | `number` | no | `0` | Milliseconds between keydown and keyup |

**Returns:** `Promise<void>`

**Example:**
```javascript
// Single key
await page.keyboard.press('ArrowLeft');

// Shortcut
await page.keyboard.press('Control+a');

// With delay
await page.keyboard.press('Enter', { delay: 50 });
```

---

### keyboard.type(text, options?)

Sends `keydown`, `keypress`/`input` and `keyup` for each character of the string.

**Signature:**
```typescript
keyboard.type(text: string, options?: {
  delay?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `text` | `string` | yes | — | Text that is typed character by character |
| `options.delay` | `number` | no | `0` | Milliseconds between consecutive key presses |

**Returns:** `Promise<void>`

**Notes:**
- Modifier keys do **not** affect the case — `type()` is independent
  of the current Shift/Caps state.
- For non-US characters (e.g. umlauts) only the `input` event is fired,
  no `keydown`/`keyup`.

**Example:**
```javascript
await page.keyboard.type('Hello, World!');
await page.keyboard.type('Slowly', { delay: 100 });
```

---

### keyboard.insertText(text)

Sends only an `input` event — no `keydown`, no `keypress`,
no `keyup`.

**Signature:**
```typescript
keyboard.insertText(text: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `text` | `string` | yes | — | Text that is inserted directly as an input event |

**Returns:** `Promise<void>`

**Notes:**
- Suitable for characters that have no key equivalent of their own (e.g. emoji,
  CJK characters).
- Modifier keys have no effect.

**Example:**
```javascript
await page.keyboard.insertText('嗨');
await page.keyboard.insertText('🎉');
```

---

## Properties

No public properties.

## Events

No events of its own — keyboard interactions trigger events on the page
elements, not on the keyboard object itself.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 5      |
| Properties | 0     |
| Events    | 0      |

**Summary:** The class covers all low-level keyboard input. `press()`
and `type()` are the general-purpose methods; `down()`/`up()` are needed when
modifier keys have to be held during other actions. `insertText()`
is the most efficient option for pure text input without event overhead.

---

*Source: https://playwright.dev/docs/api/class-keyboard*
