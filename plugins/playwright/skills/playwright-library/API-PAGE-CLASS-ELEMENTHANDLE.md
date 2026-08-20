# Playwright class-elementhandle: Complete API reference

`ElementHandle` represents a DOM element handle. It is a special `JSHandle` with
additional DOM-specific methods. **Important:** the Playwright documentation explicitly
recommends NOT using `ElementHandle` directly any more, and using `Locator` objects
and web-first assertions instead. All interaction methods of ElementHandle are marked
"deprecated" (discouraged).

Exceptions: `boundingBox()`, `contentFrame()`, `ownerFrame()` and `waitForElementState()`
are considered not deprecated and may still be used when an ElementHandle
is already available (e.g. from `page.waitForSelector()`).

ElementHandle inherits all methods from [JSHandle](API-PAGE-CLASS-JSHANDLE.md).

---

## Contents

- [Table of contents](#table-of-contents)
- [1. Non-deprecated methods](#1-non-deprecated-methods)
- [2. Deprecated: selector methods](#2-deprecated-selector-methods)
- [3. Deprecated: interaction methods](#3-deprecated-interaction-methods)
- [4. Deprecated: content/state methods](#4-deprecated-content-state-methods)
- [5. Deprecated: helper methods](#5-deprecated-helper-methods)
- [6. Inherited JSHandle methods](#6-inherited-jshandle-methods)
- [7. Manifest](#7-manifest)

## Table of contents

1. [Non-deprecated methods](#1-non-deprecated-methods)
2. [Deprecated: selector methods](#2-deprecated-selector-methods)
3. [Deprecated: interaction methods](#3-deprecated-interaction-methods)
4. [Deprecated: content/state methods](#4-deprecated-contentstate-methods)
5. [Deprecated: helper methods](#5-deprecated-helper-methods)
6. [Inherited JSHandle methods](#6-inherited-jshandle-methods)
7. [Manifest](#7-manifest)

---

## 1. Non-deprecated methods

### elementHandle.boundingBox()

```typescript
elementHandle.boundingBox(): Promise<null | {
  x: number,
  y: number,
  width: number,
  height: number
}>
```

**Parameters:** None

**Returns:** Promise with a bounding box object, or `null` if the element is not visible.

| Field | Type | Description |
|---|---|---|
| `x` | `number` | X coordinate of the top-left corner (relative to the viewport) |
| `y` | `number` | Y coordinate of the top-left corner |
| `width` | `number` | Width of the element in pixels |
| `height` | `number` | Height of the element in pixels |

Returns `null` if the element is not visible (e.g. `display: none`).

```typescript
const handle = await page.waitForSelector('.my-element');
const box = await handle?.boundingBox();
if (box) {
  console.log(`Element at (${box.x}, ${box.y}), ${box.width}x${box.height}px`);
  // Manual mouse movement to the element center
  await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
}
```

---

### elementHandle.contentFrame()

```typescript
elementHandle.contentFrame(): Promise<null | Frame>
```

**Parameters:** None

**Returns:** Promise with a Frame object or `null`.

Returns the frame content of an `<iframe>` element. Returns `null` if the element
is not an `<iframe>`.

```typescript
const iframeHandle = await page.$('iframe#my-frame');
const frame = await iframeHandle?.contentFrame();
if (frame) {
  await frame.getByRole('button', { name: 'Submit' }).click();
}
```

---

### elementHandle.ownerFrame()

```typescript
elementHandle.ownerFrame(): Promise<null | Frame>
```

**Parameters:** None

**Returns:** Promise with a Frame object or `null`.

Returns the frame that contains this element. `null` if the frame no longer exists
or has been detached.

```typescript
const handle = await page.$('h1');
const frame = await handle?.ownerFrame();
console.log('Element belongs to frame:', frame?.url());
```

---

### elementHandle.waitForElementState()

```typescript
elementHandle.waitForElementState(
  state: 'visible' | 'hidden' | 'stable' | 'enabled' | 'disabled' | 'editable',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `state` | `string` | yes | — | Desired state of the element |
| `options.timeout` | `number` | no | `0` (no timeout) | Max. wait time in ms |

**States:**

| State | Description |
|---|---|
| `'visible'` | Element has a non-empty bounding box, no `visibility:hidden`, no `opacity:0` |
| `'hidden'` | Opposite of `visible` (or the element does not exist in the DOM) |
| `'stable'` | Element is not moving and is visible |
| `'enabled'` | Not disabled (`disabled` attribute absent) |
| `'disabled'` | Has a `disabled` attribute or `aria-disabled` |
| `'editable'` | Neither `disabled` nor `readonly` |

```typescript
const spinnerHandle = await page.$('.spinner');
// Wait until the spinner disappears
await spinnerHandle?.waitForElementState('hidden');

const buttonHandle = await page.$('button#save');
// Wait until the button is clickable
await buttonHandle?.waitForElementState('enabled', { timeout: 5000 });

// Wait until an animated element comes to rest
const animHandle = await page.$('.animated-card');
await animHandle?.waitForElementState('stable');
```

---

## 2. Deprecated: selector methods

**Recommendation:** use `locator.locator()` instead.

### elementHandle.$()

```typescript
elementHandle.$(selector: string): Promise<null | ElementHandle>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `selector` | `string` | yes | CSS/XPath selector |

Finds the first element matching the selector in the context of this element.

```typescript
const row = await page.$('tr.selected');
const cell = await row?.$('td.price');
const text = await cell?.textContent();
```

---

### elementHandle.$$()

```typescript
elementHandle.$$(selector: string): Promise<Array<ElementHandle>>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `selector` | `string` | yes | CSS/XPath selector |

Finds all elements matching the selector in the context of this element.

```typescript
const list = await page.$('ul.items');
const items = await list?.$$('li') ?? [];
for (const item of items) {
  console.log(await item.textContent());
}
```

---

### elementHandle.$eval()

```typescript
elementHandle.$eval<T>(
  selector: string,
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `selector` | `string` | yes | CSS selector relative to this element |
| `pageFunction` | `Function\|string` | yes | Function executed in the browser |
| `arg` | `Serializable\|JSHandle` | no | Argument |

Runs the function on the first matched child element.

```typescript
const form = await page.$('form#login');
const emailValue = await form?.$eval('input[name=email]', el => (el as HTMLInputElement).value);
```

---

### elementHandle.$$eval()

```typescript
elementHandle.$$eval<T>(
  selector: string,
  pageFunction: (elements: Element[], arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

Runs the function on ALL matched child elements.

```typescript
const table = await page.$('table');
const cellTexts = await table?.$$eval('td', cells => cells.map(c => c.textContent));
```

---

## 3. Deprecated: interaction methods

**Recommendation:** use `page.locator().click()`, `locator.fill()` etc.

### elementHandle.click()

```typescript
elementHandle.click(options?: {
  button?: 'left' | 'right' | 'middle',
  clickCount?: number,
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  steps?: number,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `button` | `string` | `'left'` | Mouse button |
| `clickCount` | `number` | `1` | Number of clicks |
| `delay` | `number` | `0` | Ms between mousedown and mouseup |
| `force` | `boolean` | `false` | Skip actionability checks |
| `modifiers` | `string[]` | `[]` | Keys held during the click |
| `position` | `{x,y}` | Element center | Click position relative to the element |
| `steps` | `number` | `1` | Movement steps to the click position |
| `timeout` | `number` | `0` | Max. wait time |
| `trial` | `boolean` | `false` | Only check without performing |

```typescript
const button = await page.$('button.submit');
await button?.click();
await button?.click({ button: 'right' });
await button?.click({ position: { x: 5, y: 5 } });
```

---

### elementHandle.dblclick()

```typescript
elementHandle.dblclick(options?: {
  button?: 'left' | 'right' | 'middle',
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  steps?: number,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Double click.

```typescript
const cell = await page.$('.editable-cell');
await cell?.dblclick();
```

---

### elementHandle.check()

```typescript
elementHandle.check(options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Checks a checkbox or radio button.

```typescript
const checkbox = await page.$('#accept-terms');
await checkbox?.check();
await checkbox?.check({ force: true });
```

---

### elementHandle.uncheck()

```typescript
elementHandle.uncheck(options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Unchecks a checkbox.

```typescript
const checkbox = await page.$('#newsletter');
await checkbox?.uncheck();
```

---

### elementHandle.setChecked()

```typescript
elementHandle.setChecked(checked: boolean, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `checked` | `boolean` | yes | `true` = check, `false` = uncheck |

```typescript
const checkbox = await page.$('#newsletter');
await checkbox?.setChecked(true);
await checkbox?.setChecked(false);
```

---

### elementHandle.fill()

```typescript
elementHandle.fill(value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `value` | `string` | yes | Text to insert |

Clears the existing value and refills the input field.

```typescript
const input = await page.$('input[name=email]');
await input?.fill('test@example.com');
```

---

### elementHandle.focus()

```typescript
elementHandle.focus(): Promise<void>
```

Sets focus on the element.

```typescript
const input = await page.$('input[autofocus]');
await input?.focus();
```

---

### elementHandle.hover()

```typescript
elementHandle.hover(options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Moves the mouse over the element.

```typescript
const trigger = await page.$('.dropdown-trigger');
await trigger?.hover();
```

---

### elementHandle.tap()

```typescript
elementHandle.tap(options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch tap (touchscreen emulation required).

```typescript
const button = await page.$('.mobile-btn');
await button?.tap();
```

---

### elementHandle.press()

```typescript
elementHandle.press(key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `string` | yes | — | Key or combination (e.g. `'Enter'`, `'Control+a'`) |
| `options.delay` | `number` | no | `0` | Ms between keydown and keyup |

```typescript
const input = await page.$('input[type=search]');
await input?.press('Enter');
await input?.press('Control+a');
```

---

### elementHandle.type()

```typescript
elementHandle.type(text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated.** Simulates real keyboard input without clearing the existing value.

```typescript
const input = await page.$('input');
await input?.type('Hello World', { delay: 50 });
```

---

### elementHandle.dispatchEvent()

```typescript
elementHandle.dispatchEvent(
  type: string,
  eventInit?: EvaluationArgument
): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `type` | `string` | yes | DOM event type |
| `eventInit` | `EvaluationArgument` | no | Event initialization object |

```typescript
const button = await page.$('button');
await button?.dispatchEvent('click');
await button?.dispatchEvent('mouseover', { bubbles: true });
```

---

### elementHandle.selectOption()

```typescript
elementHandle.selectOption(
  values: null | string | ElementHandle | string[] | SelectOptionObject | ElementHandle[] | SelectOptionObject[],
  options?: {
    force?: boolean,
    noWaitAfter?: boolean,
    timeout?: number
  }
): Promise<string[]>
```

| `values` variants | Description |
|---|---|
| `'value'` | Option by value attribute |
| `{ label: 'Text' }` | Option by visible label |
| `{ index: 2 }` | Option by index (0-based) |
| `['val1', 'val2']` | Multiple selection |
| `null` | Clear the selection |

```typescript
const select = await page.$('select#country');
await select?.selectOption('de');
await select?.selectOption({ label: 'Germany' });
await select?.selectOption(null); // Clear the selection
```

---

### elementHandle.selectText()

```typescript
elementHandle.selectText(options?: {
  force?: boolean,
  timeout?: number
}): Promise<void>
```

Selects the entire text of the input field.

```typescript
const input = await page.$('input[name=title]');
await input?.selectText();
```

---

### elementHandle.setInputFiles()

```typescript
elementHandle.setInputFiles(
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    timeout?: number
  }
): Promise<void>
```

| `files` variants | Description |
|---|---|
| `'path/to/file'` | Single file |
| `['file1', 'file2']` | Multiple files |
| `{ name, mimeType, buffer }` | In-memory file |
| `[]` | Remove all files |

```typescript
const fileInput = await page.$('input[type=file]');
await fileInput?.setInputFiles('/path/to/test.pdf');
await fileInput?.setInputFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Hello')
});
```

---

## 4. Deprecated: content/state methods

### elementHandle.getAttribute()

```typescript
elementHandle.getAttribute(name: string): Promise<null | string>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Attribute name |

```typescript
const link = await page.$('a.nav-link');
const href = await link?.getAttribute('href');
const className = await link?.getAttribute('class');
```

---

### elementHandle.innerHTML()

```typescript
elementHandle.innerHTML(): Promise<string>
```

Returns the inner HTML content.

```typescript
const div = await page.$('.content');
const html = await div?.innerHTML();
```

---

### elementHandle.innerText()

```typescript
elementHandle.innerText(): Promise<string>
```

Returns the visible text content (respects CSS `display`, `visibility`).

```typescript
const h1 = await page.$('h1');
const text = await h1?.innerText();
```

---

### elementHandle.textContent()

```typescript
elementHandle.textContent(): Promise<null | string>
```

Returns the `textContent` (including hidden elements). `null` if not present.

```typescript
const el = await page.$('#description');
const text = await el?.textContent();
```

---

### elementHandle.inputValue()

```typescript
elementHandle.inputValue(options?: { timeout?: number }): Promise<string>
```

Returns the current value of an `<input>`, `<textarea>` or `<select>`.

```typescript
const input = await page.$('input[name=email]');
const value = await input?.inputValue();
```

---

### elementHandle.isChecked()

```typescript
elementHandle.isChecked(): Promise<boolean>
```

Returns `true` if the checkbox/radio is checked.

```typescript
const checkbox = await page.$('#terms');
const checked = await checkbox?.isChecked();
```

---

### elementHandle.isDisabled()

```typescript
elementHandle.isDisabled(): Promise<boolean>
```

Returns `true` if the element is disabled.

```typescript
const button = await page.$('button[type=submit]');
const disabled = await button?.isDisabled();
```

---

### elementHandle.isEditable()

```typescript
elementHandle.isEditable(): Promise<boolean>
```

Returns `true` if the element is editable (neither `disabled` nor `readonly`).

```typescript
const input = await page.$('input[name=username]');
const editable = await input?.isEditable();
```

---

### elementHandle.isEnabled()

```typescript
elementHandle.isEnabled(): Promise<boolean>
```

Opposite of `isDisabled()`.

```typescript
const submit = await page.$('button[type=submit]');
const enabled = await submit?.isEnabled();
```

---

### elementHandle.isHidden()

```typescript
elementHandle.isHidden(): Promise<boolean>
```

Returns `true` if the element is not visible.

```typescript
const spinner = await page.$('.loading-spinner');
const hidden = await spinner?.isHidden();
```

---

### elementHandle.isVisible()

```typescript
elementHandle.isVisible(): Promise<boolean>
```

Returns `true` if the element is visible.

```typescript
const modal = await page.$('.modal');
const visible = await modal?.isVisible();
```

---

## 5. Deprecated: helper methods

### elementHandle.screenshot()

```typescript
elementHandle.screenshot(options?: {
  animations?: 'disabled' | 'allow',
  caret?: 'hide' | 'initial',
  mask?: Locator[],
  maskColor?: string,
  omitBackground?: boolean,
  path?: string,
  quality?: number,
  scale?: 'css' | 'device',
  style?: string,
  timeout?: number,
  type?: 'png' | 'jpeg'
}): Promise<Buffer>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `animations` | `string` | `'allow'` | Disable CSS animations for the screenshot |
| `caret` | `string` | `'hide'` | Hide the text cursor |
| `mask` | `Locator[]` | — | Cover areas with a color |
| `maskColor` | `string` | `'#FF00FF'` | Mask color |
| `omitBackground` | `boolean` | `false` | Transparency (PNG only) |
| `path` | `string` | — | Save path |
| `quality` | `number` | — | JPEG quality 0–100 |
| `scale` | `string` | `'device'` | CSS or device pixels |
| `type` | `string` | `'png'` | Image format |

Takes a screenshot of the element (only the element's bounding box).

```typescript
const card = await page.$('.product-card');
await card?.screenshot({ path: 'card.png' });
const buffer = await card?.screenshot({ type: 'jpeg', quality: 80 });
```

---

### elementHandle.scrollIntoViewIfNeeded()

```typescript
elementHandle.scrollIntoViewIfNeeded(options?: {
  timeout?: number
}): Promise<void>
```

Scrolls the element into the visible area if needed.

```typescript
const element = await page.$('#footer-element');
await element?.scrollIntoViewIfNeeded();
// Now visible and interactable
await element?.click();
```

---

### elementHandle.waitForSelector()

```typescript
elementHandle.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<null | ElementHandle>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `state` | `string` | `'visible'` | Desired state |
| `strict` | `boolean` | `false` | Error on multiple matches |
| `timeout` | `number` | `0` | Max. wait time in ms |

**Deprecated** — waits for a child element in the context of this element.

```typescript
const form = await page.$('form');
const submitBtn = await form?.waitForSelector('button[type=submit]', {
  state: 'visible'
});
```

---

## 6. Inherited JSHandle methods

ElementHandle inherits all methods from `JSHandle`:

### elementHandle.asElement()

```typescript
elementHandle.asElement(): ElementHandle
```

Returns itself (since an ElementHandle is already an ElementHandle).

```typescript
const handle = await page.$('h1');
const el = handle?.asElement(); // identical to handle
```

---

### elementHandle.dispose()

```typescript
elementHandle.dispose(): Promise<void>
```

Releases the element handle object. After `dispose()` no further operations are possible.

```typescript
const handle = await page.$('.temp-element');
// Work with handle...
await handle?.dispose();
```

---

### elementHandle.evaluate()

```typescript
elementHandle.evaluate<T>(
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pageFunction` | `Function\|string` | yes | Function with this element as the first argument |
| `arg` | `Serializable\|JSHandle` | no | Additional argument |

```typescript
const el = await page.$('input');
const value = await el?.evaluate(input => (input as HTMLInputElement).value);
const len = await el?.evaluate((el, attr) => el.getAttribute(attr)?.length ?? 0, 'class');
```

---

### elementHandle.evaluateHandle()

```typescript
elementHandle.evaluateHandle<T>(
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<JSHandle<T>>
```

Like `evaluate()`, but returns a `JSHandle`.

```typescript
const el = await page.$('ul');
const firstChild = await el?.evaluateHandle(ul => ul.firstElementChild);
```

---

### elementHandle.getProperties()

```typescript
elementHandle.getProperties(): Promise<Map<string, JSHandle>>
```

Returns all own properties as a map of JSHandles.

```typescript
const el = await page.$('a');
const props = await el?.getProperties();
const hrefHandle = props?.get('href');
const href = await hrefHandle?.jsonValue();
```

---

### elementHandle.getProperty()

```typescript
elementHandle.getProperty(propertyName: string): Promise<JSHandle>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `propertyName` | `string` | yes | Name of the property |

```typescript
const input = await page.$('input[type=text]');
const valueHandle = await input?.getProperty('value');
const value = await valueHandle?.jsonValue();
```

---

### elementHandle.jsonValue()

```typescript
elementHandle.jsonValue(): Promise<Serializable>
```

Returns a JSON representation. For DOM elements the result is an empty object `{}`.

```typescript
const handle = await page.$('input');
const json = await handle?.jsonValue(); // {}
```

---

## 7. Manifest

| Category | Documented methods |
|---|---|
| Non-deprecated | 4 (boundingBox, contentFrame, ownerFrame, waitForElementState) |
| Deprecated: selector | 4 ($, $$, $eval, $$eval) |
| Deprecated: interaction | 14 (click, dblclick, check, uncheck, setChecked, fill, focus, hover, tap, press, type, dispatchEvent, selectOption, selectText, setInputFiles) |
| Deprecated: content/state | 11 (getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible) |
| Deprecated: helpers | 3 (screenshot, scrollIntoViewIfNeeded, waitForSelector) |
| Inherited from JSHandle | 6 (asElement, dispose, evaluate, evaluateHandle, getProperties, getProperty, jsonValue) |

**Total: ~42 methods**

**Conclusion:** `ElementHandle` is the legacy API for DOM element interactions in Playwright.
All interaction methods are officially marked "discouraged". New tests should
use locator-based methods exclusively. The three non-deprecated methods
(`boundingBox`, `contentFrame`, `waitForElementState`) are useful when an ElementHandle
is already available from legacy code or `waitForSelector()`.

---

**Source:** https://playwright.dev/docs/api/class-elementhandle
