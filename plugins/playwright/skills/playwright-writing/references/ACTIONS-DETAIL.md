# Playwright Actions and Actionability

All actions perform actionability checks before execution and wait
automatically until the conditions are met (auto-waiting).

---

## Contents

- [Actionability checks](#actionability-checks)
- [click()](#click)
- [dblclick()](#dblclick)
- [fill()](#fill)
- [clear()](#clear)
- [pressSequentially()](#presssequentially)
- [press()](#press)
- [hover()](#hover)
- [check() and uncheck()](#check-and-uncheck)
- [selectOption()](#selectoption)
- [setInputFiles()](#setinputfiles)
- [dragTo()](#dragto)
- [tap()](#tap)
- [focus() and blur()](#focus-and-blur)
- [dispatchEvent()](#dispatchevent)
- [scrollIntoViewIfNeeded()](#scrollintoviewifneeded)
- [evaluate() and evaluateAll()](#evaluate-and-evaluateall)
- [State query methods](#state-query-methods)
- [waitFor()](#waitfor)
- [selectText()](#selecttext)
- [Complete interaction example](#complete-interaction-example)

## Actionability checks

### The five checks

| Check | Criterion |
|---|---|
| **Visible** | Element has a non-empty bounding box AND does NOT have `visibility:hidden`. Elements with `display:none` or size 0 fail. `opacity:0` passes the check. |
| **Stable** | Element has the same bounding box for at least two consecutive animation frames (no running animation). |
| **Receives Events** | At the action's coordinate point, the target element receives pointer events (no overlay on top of it). |
| **Enabled** | Element is NOT disabled. Disabled by: `[disabled]` attribute (button/select/input/textarea/option/optgroup), disabled fieldset ancestor, `[aria-disabled=true]` ancestor. |
| **Editable** | Element is Enabled AND does NOT have a `[readonly]` or `[aria-readonly=true]` attribute. |

### Which action checks what

| Action | Visible | Stable | Receives Events | Enabled | Editable |
|---|---|---|---|---|---|
| `click`, `check`, `tap` | Yes | Yes | Yes | Yes | — |
| `hover`, `dragTo` | Yes | Yes | Yes | — | — |
| `fill`, `clear` | Yes | — | — | Yes | Yes |
| `screenshot` | Yes | Yes | — | — | — |
| `blur`, `focus`, `press`, `dispatchEvent` | — | — | — | — | — |

### force: true — skip the checks

```typescript
await page.getByRole('button').click({ force: true });
// Skips the receives-events check; all other checks remain
```

### trial: true — checks only, no execution

```typescript
await page.getByRole('button').click({ trial: true });
// Performs all actionability checks but does NOT execute the action
// Useful for checking up front whether an element is clickable
```

### Timeout behavior

If the actionability checks do not pass within the timeout: `TimeoutError`.
Default timeout: `0` (no timeout) — can be overridden with the `timeout` option
or `page.setDefaultTimeout()` / `browserContext.setDefaultTimeout()`.

---

## click()

```typescript
await locator.click(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `button` | `'left' \| 'right' \| 'middle'` | `'left'` | Mouse button |
| `clickCount` | `number` | `1` | Number of clicks |
| `delay` | `number` | `0` | Delay in ms between mousedown and mouseup |
| `force` | `boolean` | `false` | Skip actionability checks |
| `modifiers` | `Array<'Alt' \| 'Control' \| 'ControlOrMeta' \| 'Meta' \| 'Shift'>` | — | Modifier keys |
| `noWaitAfter` | `boolean` | `false` | **Deprecated**, no longer has any effect |
| `position` | `{ x: number; y: number }` | Center | Position relative to the padding box |
| `steps` | `number` | `1` | Interpolated mouse movement steps |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only, do not execute the action |

```typescript
// Simple click
await page.getByRole('button', { name: 'Submit' }).click();

// Right click
await page.getByRole('button').click({ button: 'right' });

// Double click (alternative to dblclick)
await page.getByRole('button').click({ clickCount: 2 });

// With modifier
await page.getByRole('link').click({ modifiers: ['Shift'] });

// Precise position
await page.getByRole('button').click({ position: { x: 10, y: 5 } });

// Ctrl+click (macOS: Meta)
await page.getByRole('link').click({ modifiers: ['ControlOrMeta'] });
```

---

## dblclick()

```typescript
await locator.dblclick(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `button` | `'left' \| 'right' \| 'middle'` | `'left'` | Mouse button |
| `delay` | `number` | `0` | Delay between clicks in ms |
| `force` | `boolean` | `false` | Skip checks |
| `modifiers` | `Array<...>` | — | Modifier keys |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `position` | `{ x: number; y: number }` | Center | Position |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only |

```typescript
await page.getByRole('listitem').dblclick();
```

---

## fill()

Clears the existing value and enters new text. For `<input>`, `<textarea>` and
`contenteditable` elements.

```typescript
await locator.fill(value: string, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | — | **Required** — text to enter |
| `force` | `boolean` | `false` | Skip checks |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
await page.getByLabel('Email').fill('user@example.com');
await page.getByPlaceholder('Password').fill('secret');

// Clear the content (empty string)
await page.getByRole('textbox').fill('');
```

---

## clear()

Clears the content of an input field.

```typescript
await locator.clear(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
await page.getByRole('textbox').clear();
```

---

## pressSequentially()

Enters text character by character (fires keyboard events). Useful for
fields with autocomplete or character-by-character validation.

```typescript
await locator.pressSequentially(text: string, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `text` | `string` | — | **Required** — text to enter |
| `delay` | `number` | `0` | Delay in ms between keystrokes |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
// With typing delay for a more realistic simulation
await page.getByRole('textbox').pressSequentially('Hallo Welt', { delay: 50 });
```

---

## press()

Presses a single key or key combination.

```typescript
await locator.press(key: string, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `key` | `string` | — | **Required** — key or combination |
| `delay` | `number` | `0` | Time in ms between keydown and keyup |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

### Key format

- Single key: `'Enter'`, `'Tab'`, `'Escape'`, `'Space'`, `'Backspace'`
- Combination: `'Control+A'`, `'Shift+Tab'`, `'Control+ArrowRight'`
- Cross-platform: `'ControlOrMeta+A'` (Control on Windows/Linux, Meta on macOS)

```typescript
await page.getByRole('textbox').press('Enter');
await page.getByRole('textbox').press('Control+A');
await page.getByRole('textbox').press('Shift+Tab');
await page.keyboard.press('Escape');    // Global key press
```

---

## hover()

Moves the mouse over an element.

```typescript
await locator.hover(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `modifiers` | `Array<'Alt' \| 'Control' \| 'ControlOrMeta' \| 'Meta' \| 'Shift'>` | — | Modifier keys |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `position` | `{ x: number; y: number }` | Center | Position relative to the padding box |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only |

```typescript
await page.getByRole('button').hover();
await page.locator('.menu-item').hover({ position: { x: 5, y: 5 } });
```

---

## check() and uncheck()

```typescript
await locator.check(options?)
await locator.uncheck(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `position` | `{ x: number; y: number }` | Center | Position |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only |

```typescript
await page.getByRole('checkbox', { name: 'AGB akzeptieren' }).check();
await page.getByRole('checkbox').uncheck();
await expect(page.getByRole('checkbox')).toBeChecked();
```

### setChecked() — combines check/uncheck

```typescript
await locator.setChecked(checked: boolean, options?)
```

```typescript
await page.getByRole('checkbox').setChecked(true);
await page.getByRole('checkbox').setChecked(false);
```

---

## selectOption()

Selects one or more options in a `<select>` element.

```typescript
await locator.selectOption(values, options?)
```

### values parameter

| Format | Description | Example |
|---|---|---|
| `string` | Single value | `'option-value'` |
| `string[]` | Multiple values | `['val1', 'val2']` |
| `{ value?: string }` | Object with value | `{ value: 'rot' }` |
| `{ label?: string }` | Object with label | `{ label: 'Rot' }` |
| `{ index?: number }` | Object with index | `{ index: 0 }` |
| Combined arrays | Multiple objects | `[{ label: 'Rot' }, { value: 'blau' }]` |

### options parameter

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
// Select by value
await page.getByRole('combobox').selectOption('farbe-rot');

// Select by label
await page.getByRole('combobox').selectOption({ label: 'Rot' });

// Select by index
await page.getByRole('combobox').selectOption({ index: 2 });

// Multiple options (multi-select)
await page.getByRole('listbox').selectOption(['rot', 'blau', 'gruen']);

// Mixed
await page.getByRole('listbox').selectOption([
  { label: 'Rot' },
  { value: 'blau' },
]);
```

---

## setInputFiles()

Sets files for `<input type="file">` elements.

```typescript
await locator.setInputFiles(files, options?)
```

### files parameter

| Format | Description |
|---|---|
| `string` | Single file path |
| `string[]` | Multiple file paths |
| `FilePayload` | File object (no file system needed) |
| `FilePayload[]` | Multiple file objects |
| `[]` | Empty array = clear the selection |

### FilePayload object

```typescript
interface FilePayload {
  name: string;       // File name
  mimeType: string;   // MIME type, e.g. 'image/png'
  buffer: Buffer;     // File content as a Buffer
}
```

### Options

| Option | Type | Default | Description |
|---|---|---|---|
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
// Single file
await page.getByLabel('Upload file').setInputFiles('/pfad/zur/datei.pdf');

// Multiple files
await page.getByLabel('Bilder').setInputFiles([
  '/pfad/bild1.png',
  '/pfad/bild2.jpg',
]);

// From a buffer (no file system)
await page.getByLabel('Upload').setInputFiles({
  name: 'document.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('File content'),
});

// Clear the selection
await page.getByLabel('Upload').setInputFiles([]);
```

---

## dragTo()

Drags an element to another locator.

```typescript
await locator.dragTo(target: Locator, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `sourcePosition` | `{ x: number; y: number }` | Center | Start point relative to the padding box |
| `targetPosition` | `{ x: number; y: number }` | Center | Target point relative to the padding box |
| `steps` | `number` | `1` | Interpolated mouse movement steps |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only |

```typescript
// Simple drag & drop
await page.getByText('Aufgabe 1').dragTo(page.getByText('Erledigt'));

// With positioning
await page.locator('#element').dragTo(page.locator('#ziel'), {
  sourcePosition: { x: 10, y: 10 },
  targetPosition: { x: 5, y: 5 },
});
```

### Manual drag & drop with the mouse API

```typescript
await page.mouse.move(startX, startY);
await page.mouse.down();
await page.mouse.move(zielX, zielY, { steps: 10 });
await page.mouse.up();
```

---

## tap()

Taps an element (touch gesture). Requires `hasTouch: true` in the context options.

```typescript
await locator.tap(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `modifiers` | `Array<...>` | — | Modifier keys |
| `noWaitAfter` | `boolean` | `false` | Deprecated |
| `position` | `{ x: number; y: number }` | Center | Position |
| `timeout` | `number` | `0` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Checks only |

```typescript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
await page.getByRole('button').tap();
```

---

## focus() and blur()

```typescript
await locator.focus(options?)
await locator.blur(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
await page.getByRole('textbox').focus();
await page.getByRole('textbox').blur();
```

---

## dispatchEvent()

Fires a DOM event programmatically (ignores actionability checks).

```typescript
await locator.dispatchEvent(type: string, eventInit?, options?)
```

| Parameter | Type | Description |
|---|---|---|
| `type` | `string` | Event type, e.g. `'click'`, `'input'`, `'change'` |
| `eventInit` | `object` | Event initialization object |
| `timeout` | `number` | Max. wait time in ms |

```typescript
await page.getByRole('button').dispatchEvent('click');
await page.locator('#datepicker').dispatchEvent('change', {
  bubbles: true,
});
```

---

## scrollIntoViewIfNeeded()

Scrolls the element into the visible area.

```typescript
await locator.scrollIntoViewIfNeeded(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
await page.getByRole('button').scrollIntoViewIfNeeded();
```

### Mouse wheel

```typescript
await page.mouse.wheel(deltaX, deltaY);
// deltaX: horizontal scrolling, deltaY: vertical scrolling
await page.mouse.wheel(0, 500);  // scroll 500px down
```

---

## evaluate() and evaluateAll()

Executes JavaScript in the browser context.

```typescript
// On a single element
const result = await locator.evaluate(fn, arg?, options?)

// On all matching elements
const results = await locator.evaluateAll(fn, arg?)
```

```typescript
// Read an element property
const value = await page.getByRole('textbox').evaluate(el => el.value);

// Collect all element texts
const texte = await page.getByRole('listitem').evaluateAll(
  items => items.map(el => el.textContent?.trim())
);
```

---

## State query methods

```typescript
await locator.getAttribute(name: string, options?): Promise<string | null>
await locator.innerHTML(options?):  Promise<string>
await locator.innerText(options?):  Promise<string>
await locator.inputValue(options?): Promise<string>
await locator.textContent(options?): Promise<string | null>
await locator.isChecked(options?):  Promise<boolean>
await locator.isDisabled(options?): Promise<boolean>
await locator.isEditable(options?): Promise<boolean>
await locator.isEnabled(options?):  Promise<boolean>
await locator.isHidden(options?):   Promise<boolean>
await locator.isVisible(options?):  Promise<boolean>
```

All accept `{ timeout?: number }`.

```typescript
const titel = await page.getByRole('heading').innerText();
const wert = await page.getByRole('textbox').inputValue();
const istAktiv = await page.getByRole('checkbox').isChecked();
const html = await page.locator('.container').innerHTML();
```

---

## waitFor()

Waits until an element is in a certain state.

```typescript
await locator.waitFor(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `state` | `'attached' \| 'detached' \| 'visible' \| 'hidden'` | `'visible'` | Expected state |
| `timeout` | `number` | `0` | Max. wait time in ms |

```typescript
await page.getByText('Laden...').waitFor({ state: 'hidden' });
await page.getByRole('dialog').waitFor({ state: 'visible' });
await page.getByRole('button').waitFor({ state: 'attached' });
```

---

## selectText()

Selects the text content of an element.

```typescript
await locator.selectText(options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `force` | `boolean` | `false` | Skip checks |
| `timeout` | `number` | `0` | Max. wait time in ms |

---

## Complete interaction example

```typescript
import { test, expect } from '@playwright/test';

test('Bestellformular ausfullen', async ({ page }) => {
  await page.goto('https://shop.example.com/checkout');

  // Text input
  await page.getByLabel('Vorname').fill('Anna');
  await page.getByLabel('Nachname').fill('Muster');
  await page.getByLabel('Email').fill('anna@example.com');

  // Dropdown
  await page.getByLabel('Land').selectOption({ label: 'Deutschland' });

  // Checkbox
  await page.getByRole('checkbox', { name: 'Expresszustellung' }).check();

  // Radio button
  await page.getByRole('radio', { name: 'Kreditkarte' }).check();

  // File upload
  await page.getByLabel('Rechnung hochladen').setInputFiles('/pfad/rechnung.pdf');

  // Submit
  await page.getByRole('button', { name: 'Bestellen' }).click();

  // Check the result
  await expect(page.getByRole('heading', { name: 'Bestellung erfolgreich' }))
    .toBeVisible({ timeout: 10000 });
});
```

<!-- Sources:
https://playwright.dev/docs/input
https://playwright.dev/docs/actionability
https://playwright.dev/docs/api/class-locator
-->
