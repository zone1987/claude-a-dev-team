# Playwright class-page: Complete API reference

The `Page` class represents a single browser page (tab). It is the central
entry class for nearly all Playwright operations: navigation, interaction, evaluation,
network routing, screenshot/PDF and event handling.

---

## Contents

- [Table of contents](#table-of-contents)
- [1. Navigation](#1-navigation)
- [2. Reading/setting page content](#2-readingsetting-page-content)
- [3. Locator factory methods](#3-locator-factory-methods)
- [4. Frame management](#4-frame-management)
- [5. Element interactions (selector-based, deprecated)](#5-element-interactions-selector-based-deprecated)
- [6. JavaScript execution](#6-javascript-execution)
- [7. Script and style injection](#7-script-and-style-injection)
- [8. Network / routing](#8-network-routing)
- [9. Waiting / synchronization](#9-waiting-synchronization)
- [10. Screenshots & PDF](#10-screenshots-pdf)
- [11. Browser configuration](#11-browser-configuration)
- [12. Event handling / listeners](#12-event-handling-listeners)
- [13. Miscellaneous helper methods](#13-miscellaneous-helper-methods)
- [14. Properties](#14-properties)
- [15. Events](#15-events)
- [16. Manifest](#16-manifest)

## Table of contents

1. [Navigation](#1-navigation)
2. [Reading/setting page content](#2-readingsetting-page-content)
3. [Locator factory methods](#3-locator-factory-methods)
4. [Frame management](#4-frame-management)
5. [Element interactions (selector-based, deprecated)](#5-element-interactions-selector-based-deprecated)
6. [JavaScript execution](#6-javascript-execution)
7. [Script and style injection](#7-script-and-style-injection)
8. [Network / routing](#8-network--routing)
9. [Waiting / synchronization](#9-waiting--synchronization)
10. [Screenshots & PDF](#10-screenshots--pdf)
11. [Browser configuration](#11-browser-configuration)
12. [Event handling / listeners](#12-event-handling--listeners)
13. [Miscellaneous helper methods](#13-miscellaneous-helper-methods)
14. [Properties](#14-properties)
15. [Events](#15-events)
16. [Manifest](#16-manifest)

---

## 1. Navigation

### page.goto()

```typescript
page.goto(url: string, options?: {
  referer?: string,
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | `string` | yes | — | Target URL (absolute, data:, about:blank allowed) |
| `options.referer` | `string` | no | — | HTTP Referer header |
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms (0 = unlimited) |
| `options.waitUntil` | `string` | no | `'load'` | `'load'`: waits for the load event; `'domcontentloaded'`: DOMContentLoaded; `'networkidle'`: no open network connections for 500ms; `'commit'`: network response received only |

Returns the main resource response. `null` when navigating to `about:blank` or to the same URL with a different hash.

```typescript
const response = await page.goto('https://example.com');
console.log(response?.status()); // 200

await page.goto('https://example.com', {
  waitUntil: 'networkidle',
  timeout: 30000
});
```

---

### page.goBack()

```typescript
page.goBack(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |
| `options.waitUntil` | `string` | no | `'load'` | When navigation counts as complete |

Navigates one page back in the browser history. `null` if no previous entry exists.

```typescript
await page.goBack();
await page.goBack({ waitUntil: 'domcontentloaded' });
```

---

### page.goForward()

```typescript
page.goForward(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |
| `options.waitUntil` | `string` | no | `'load'` | When navigation counts as complete |

Navigates forward in the browser history. `null` if no next entry exists.

```typescript
await page.goForward();
```

---

### page.reload()

```typescript
page.reload(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |
| `options.waitUntil` | `string` | no | `'load'` | When the reload counts as complete |

Reloads the current page (equivalent to `Ctrl+R`/`F5`).

```typescript
await page.reload();
await page.reload({ waitUntil: 'networkidle' });
```

---

### page.url()

```typescript
page.url(): string
```

Returns the current URL of the page (synchronously, no promise).

```typescript
console.log(page.url()); // 'https://example.com/path'
```

---

### page.title()

```typescript
page.title(): Promise<string>
```

Returns the title (`<title>` element) of the page.

```typescript
const title = await page.title();
expect(title).toBe('My page');
```

---

## 2. Reading/setting page content

### page.content()

```typescript
page.content(): Promise<string>
```

Returns the complete HTML content of the page, including the doctype.

```typescript
const html = await page.content();
console.log(html.includes('<title>'));
```

---

### page.setContent()

```typescript
page.setContent(html: string, options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `html` | `string` | yes | — | Complete HTML string |
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |
| `options.waitUntil` | `string` | no | `'load'` | When setting counts as complete |

```typescript
await page.setContent('<h1>Hello World</h1>');
await page.setContent('<html><body><p>Test</p></body></html>', {
  waitUntil: 'domcontentloaded'
});
```

---

### page.getAttribute()

```typescript
page.getAttribute(selector: string, name: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | CSS/XPath selector |
| `name` | `string` | yes | — | Attribute name |
| `options.strict` | `boolean` | no | `false` | Error if more than one element is found |
| `options.timeout` | `number` | no | `defaultTimeout` | Max. wait time in ms |

```typescript
const href = await page.getAttribute('a', 'href');
const checked = await page.getAttribute('input[type=checkbox]', 'checked');
```

---

### page.innerHTML()

```typescript
page.innerHTML(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Returns the inner HTML of the first matched element.

```typescript
const content = await page.innerHTML('.article-body');
```

---

### page.innerText()

```typescript
page.innerText(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Returns the visible text (like `HTMLElement.innerText`); ignores hidden elements.

```typescript
const text = await page.innerText('h1');
```

---

### page.textContent()

```typescript
page.textContent(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

Returns the `textContent` value (including hidden elements). `null` if no element is found.

```typescript
const text = await page.textContent('#description');
```

---

### page.inputValue()

```typescript
page.inputValue(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Returns the current value of an `<input>`, `<textarea>` or `<select>`.

```typescript
const value = await page.inputValue('input[name=email]');
```

---

### page.isChecked()

```typescript
page.isChecked(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Checks whether a checkbox or radio button is checked.

```typescript
const checked = await page.isChecked('#terms');
```

---

### page.isDisabled()

```typescript
page.isDisabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Checks whether an element is disabled (`disabled` attribute or `aria-disabled`).

```typescript
if (await page.isDisabled('button[type=submit]')) { /* ... */ }
```

---

### page.isEditable()

```typescript
page.isEditable(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Checks whether an element is editable (neither `disabled` nor `readonly`).

```typescript
const editable = await page.isEditable('input[name=username]');
```

---

### page.isEnabled()

```typescript
page.isEnabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Opposite of `isDisabled()`.

```typescript
await expect(page.locator('button')).toBeEnabled();
```

---

### page.isHidden()

```typescript
page.isHidden(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Returns `true` if the element is hidden OR no element was found.

```typescript
const hidden = await page.isHidden('.spinner');
```

---

### page.isVisible()

```typescript
page.isVisible(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Returns `true` if the element is visible (not `display:none`, not `visibility:hidden`, not `opacity:0`).

```typescript
const visible = await page.isVisible('.success-message');
```

---

## 3. Locator factory methods

### page.locator()

```typescript
page.locator(selector: string, options?: {
  has?: Locator,
  hasNot?: Locator,
  hasText?: string | RegExp,
  hasNotText?: string | RegExp
}): Locator
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | CSS, XPath, text=, role=, etc. |
| `options.has` | `Locator` | no | — | Element must contain this sub-locator |
| `options.hasNot` | `Locator` | no | — | Element must NOT contain this sub-locator |
| `options.hasText` | `string\|RegExp` | no | — | Element must contain this text (substring) |
| `options.hasNotText` | `string\|RegExp` | no | — | Element must NOT contain this text |

Creates a locator. **Recommended method** over direct selector-based methods.

```typescript
const button = page.locator('button.primary');
await button.click();

// With a filter
const row = page.locator('tr', { hasText: 'John Doe' });
await row.locator('td.actions button').click();

// Combined
const item = page.locator('.list-item', {
  has: page.locator('.badge'),
  hasNotText: 'archived'
});
```

---

### page.getByRole()

```typescript
page.getByRole(role: AriaRole, options?: {
  checked?: boolean,
  description?: string | RegExp,
  disabled?: boolean,
  exact?: boolean,
  expanded?: boolean,
  includeHidden?: boolean,
  level?: number,
  name?: string | RegExp,
  pressed?: boolean,
  selected?: boolean
}): Locator
```

| Option | Type | Default | Description |
|---|---|---|---|
| `role` | `AriaRole` | — | ARIA role (button, link, textbox, checkbox, ...) |
| `name` | `string\|RegExp` | — | Accessible name (case-insensitive, substring) |
| `exact` | `boolean` | `false` | Exact matching for `name` |
| `checked` | `boolean` | — | `aria-checked` |
| `disabled` | `boolean` | — | `aria-disabled` or `disabled` |
| `expanded` | `boolean` | — | `aria-expanded` |
| `includeHidden` | `boolean` | `false` | Include ARIA-hidden elements |
| `level` | `number` | — | For headings: 1–6 |
| `pressed` | `boolean` | — | `aria-pressed` |
| `selected` | `boolean` | — | `aria-selected` |
| `description` | `string\|RegExp` | — | Accessible description |

```typescript
await page.getByRole('button', { name: 'Submit' }).click();
await page.getByRole('heading', { name: /welcome/i, level: 1 });
await page.getByRole('checkbox', { name: 'Newsletter' }).check();
await page.getByRole('textbox', { name: 'E-mail' }).fill('test@example.com');
```

---

### page.getByText()

```typescript
page.getByText(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string\|RegExp` | yes | — | Search text (substring for a string, case-insensitive) |
| `options.exact` | `boolean` | no | `false` | Exact, case-sensitive matching |

```typescript
page.getByText('Sign in');
page.getByText(/sign in/i);
page.getByText('Sign in', { exact: true });
```

---

### page.getByLabel()

```typescript
page.getByLabel(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Finds form elements associated with a `<label>` element (via `for`/`aria-labelledby`/`aria-label`).

```typescript
await page.getByLabel('Password').fill('secret123');
await page.getByLabel(/e-mail/i).fill('test@example.com');
```

---

### page.getByPlaceholder()

```typescript
page.getByPlaceholder(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Finds inputs/textareas with a matching `placeholder` attribute.

```typescript
await page.getByPlaceholder('Username').fill('admin');
await page.getByPlaceholder(/search/i).fill('Playwright');
```

---

### page.getByAltText()

```typescript
page.getByAltText(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Finds elements (mostly `<img>`) with a matching `alt` attribute.

```typescript
await page.getByAltText('Company logo').click();
await expect(page.getByAltText('Product image')).toBeVisible();
```

---

### page.getByTitle()

```typescript
page.getByTitle(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Finds elements with a matching `title` attribute.

```typescript
await page.getByTitle('Close').click();
await page.getByTitle(/tooltip/i);
```

---

### page.getByTestId()

```typescript
page.getByTestId(testId: string | RegExp): Locator
```

Finds elements by the `data-testid` attribute (configurable via `playwright.config.ts`).

```typescript
await page.getByTestId('submit-button').click();
await page.getByTestId(/user-row-\d+/).first();
```

---

### page.frameLocator()

```typescript
page.frameLocator(selector: string): FrameLocator
```

Creates a locator for content inside an `<iframe>`. All further methods are applied to the iframe content.

```typescript
const frame = page.frameLocator('#my-iframe');
await frame.getByRole('button', { name: 'Submit' }).click();

// Nested iframes
const nested = page.frameLocator('.outer').frameLocator('.inner');
await nested.getByText('Hello').click();
```

---

## 4. Frame management

### page.frames()

```typescript
page.frames(): Frame[]
```

Returns all frames of the page (including the main frame and iframes).

```typescript
const frames = page.frames();
console.log(frames.length);
```

---

### page.frame()

```typescript
page.frame(frameSelector: string | {
  name?: string,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean)
}): Frame | null
```

| Parameter | Type | Description |
|---|---|---|
| `frameSelector` | `string` | Frame name as a string |
| `frameSelector.name` | `string` | Name attribute of the iframe |
| `frameSelector.url` | `string\|RegExp\|...` | URL of the frame (match) |

```typescript
const frame = page.frame({ url: /my-frame/ });
const namedFrame = page.frame('my-frame-name');
```

---

### page.mainFrame()

```typescript
page.mainFrame(): Frame
```

Returns the main frame of the page.

```typescript
const main = page.mainFrame();
```

---

## 5. Element interactions (selector-based, deprecated)

**Note:** these methods accept direct CSS/XPath selectors. According to the Playwright documentation
`page.locator()` + `locator.click()` etc. should be used instead.
They remain supported, however.

### page.click()

```typescript
page.click(selector: string, options?: {
  button?: 'left' | 'right' | 'middle',
  clickCount?: number,
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `selector` | `string` | — | CSS/XPath selector |
| `button` | `string` | `'left'` | Mouse button |
| `clickCount` | `number` | `1` | Number of clicks |
| `delay` | `number` | `0` | Ms between mousedown and mouseup |
| `force` | `boolean` | `false` | Skip actionability checks |
| `modifiers` | `string[]` | `[]` | Hold additional keys |
| `noWaitAfter` | `boolean` | `false` | Do not wait for navigations |
| `position` | `{x,y}` | Element center | Click position relative to the element |
| `strict` | `boolean` | `false` | Error if multiple elements are found |
| `timeout` | `number` | `defaultTimeout` | Max. wait time in ms |
| `trial` | `boolean` | `false` | Only check without performing |

```typescript
await page.click('button.submit');
await page.click('#menu-item', { button: 'right' });
await page.click('a', { modifiers: ['Control'] }); // Ctrl+Click
await page.click('.target', { position: { x: 10, y: 5 } });
```

---

### page.dblclick()

```typescript
page.dblclick(selector: string, options?: {
  button?: 'left' | 'right' | 'middle',
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Double click on an element. Parameters identical to `click()` (without `clickCount`).

```typescript
await page.dblclick('.editable-cell');
```

---

### page.check()

```typescript
page.check(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Checks a checkbox or a radio button (no error if already checked).

```typescript
await page.check('#accept-terms');
await page.check('input[name=newsletter]', { force: true });
```

---

### page.uncheck()

```typescript
page.uncheck(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Unchecks a checkbox (no error if already unchecked).

```typescript
await page.uncheck('#newsletter');
```

---

### page.setChecked()

```typescript
page.setChecked(selector: string, checked: boolean, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `selector` | `string` | yes | CSS/XPath selector |
| `checked` | `boolean` | yes | `true` = check, `false` = uncheck |

```typescript
await page.setChecked('#newsletter', true);
await page.setChecked('#terms', false);
```

---

### page.fill()

```typescript
page.fill(selector: string, value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `selector` | `string` | yes | Input/textarea selector |
| `value` | `string` | yes | Text to insert (replaces the existing value) |

Clears the existing value and fills the field. For `<input type=file>` use `setInputFiles()` instead.

```typescript
await page.fill('input[name=email]', 'test@example.com');
await page.fill('textarea', 'My comment');
```

---

### page.focus()

```typescript
page.focus(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Sets focus on an element.

```typescript
await page.focus('input[name=search]');
```

---

### page.hover()

```typescript
page.hover(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Moves the mouse over an element (triggers `mouseenter`/`mousemove`).

```typescript
await page.hover('.dropdown-trigger');
await page.hover('canvas', { position: { x: 100, y: 200 } });
```

---

### page.press()

```typescript
page.press(selector: string, key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | Element to focus |
| `key` | `string` | yes | — | Key combination (e.g. `'Enter'`, `'Tab'`, `'Control+a'`, `'F5'`) |
| `options.delay` | `number` | no | `0` | Ms between keydown and keyup |

```typescript
await page.press('input', 'Enter');
await page.press('body', 'Control+a');
await page.press('[contenteditable]', 'Shift+End');
```

---

### page.type()

```typescript
page.type(selector: string, text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated** — use `page.locator().pressSequentially()`. Simulates real keyboard input
(one character after another) without clearing the existing content.

```typescript
await page.type('input', 'Hello', { delay: 50 });
```

---

### page.tap()

```typescript
page.tap(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch tap on an element (touchscreen simulation required).

```typescript
await page.tap('.mobile-menu-button');
```

---

### page.selectOption()

```typescript
page.selectOption(
  selector: string,
  values: null | string | ElementHandle | string[] | SelectOptionObject | ElementHandle[] | SelectOptionObject[],
  options?: {
    force?: boolean,
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<string[]>
```

| `values` variants | Description |
|---|---|
| `'value'` | Option by value attribute |
| `{ label: 'Text' }` | Option by visible text |
| `{ index: 2 }` | Option by index |
| `['val1', 'val2']` | Multiple selection |
| `null` | Clear the selection |

Returns an array of the selected `value` attributes.

```typescript
await page.selectOption('select', 'de');
await page.selectOption('select', { label: 'Germany' });
await page.selectOption('select[multiple]', ['de', 'at', 'ch']);
```

---

### page.setInputFiles()

```typescript
page.setInputFiles(
  selector: string,
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

| `files` variants | Description |
|---|---|
| `'path/to/file.pdf'` | Single file by path |
| `['file1.pdf', 'file2.pdf']` | Multiple files by path |
| `{ name, mimeType, buffer }` | In-memory file (no file system needed) |
| `[]` | Remove all files |

```typescript
await page.setInputFiles('input[type=file]', 'test.pdf');
await page.setInputFiles('input', ['file1.pdf', 'file2.jpg']);
await page.setInputFiles('input', {
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Hello')
});
await page.setInputFiles('input', []); // Reset
```

---

### page.dispatchEvent()

```typescript
page.dispatchEvent(
  selector: string,
  type: string,
  eventInit?: EvaluationArgument,
  options?: {
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Triggers a DOM event on the element (e.g. `'click'`, `'input'`, `'change'`, custom events).

```typescript
await page.dispatchEvent('button', 'click');
await page.dispatchEvent('#field', 'input', { data: 'new value' });
await page.dispatchEvent('.el', 'custom:event', { detail: { key: 'value' } });
```

---

### page.dragAndDrop()

```typescript
page.dragAndDrop(source: string, target: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  sourcePosition?: { x: number, y: number },
  steps?: number,
  strict?: boolean,
  targetPosition?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | `string` | yes | — | Selector of the element to drag |
| `target` | `string` | yes | — | Selector of the target element |
| `sourcePosition` | `{x,y}` | no | Element center | Start position |
| `targetPosition` | `{x,y}` | no | Element center | Target position |
| `steps` | `number` | no | `1` | Number of movement steps |

```typescript
await page.dragAndDrop('#source', '#target');
await page.dragAndDrop('.card', '.dropzone', { steps: 10 });
```

---

### page.selectText()

```typescript
page.selectText(selector: string, options?: {
  force?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Selects the text of an input or textarea element (`select()`).

```typescript
await page.selectText('input[name=title]');
// Afterwards: Ctrl+C or typing overwrites the content
```

---

## 6. JavaScript execution

### page.evaluate()

```typescript
page.evaluate<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pageFunction` | `function\|string` | yes | Function or JS code string executed in the browser |
| `arg` | `Serializable\|JSHandle` | no | Argument passed into the function |

Returns a serialized return value (JSON-capable). Non-serializable values become `undefined`.

```typescript
const url = await page.evaluate(() => window.location.href);
const title = await page.evaluate('document.title');

const result = await page.evaluate(({ a, b }) => a + b, { a: 1, b: 2 });

// With DOM manipulation
const count = await page.evaluate(() => document.querySelectorAll('li').length);

// Pass an element handle
const el = await page.locator('h1').elementHandle();
const text = await page.evaluate(el => el.textContent, el);
```

---

### page.evaluateHandle()

```typescript
page.evaluateHandle<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

Like `evaluate()`, but returns a `JSHandle` (no JSON serialization overhead). Useful
for complex browser objects.

```typescript
const arrayHandle = await page.evaluateHandle(() => Array.from(document.querySelectorAll('a')));
const len = await page.evaluate(arr => arr.length, arrayHandle);
await arrayHandle.dispose();
```

---

### page.exposeFunction()

```typescript
page.exposeFunction(name: string, callback: Function): Promise<Disposable>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Function name on `window` |
| `callback` | `Function` | yes | Node.js function callable from the browser |

Makes a Node.js function callable in the browser under `window[name]`. Page reloads keep the exposure.

```typescript
await page.exposeFunction('sha256', async (text: string) => {
  const { createHash } = require('crypto');
  return createHash('sha256').update(text).digest('hex');
});
const hash = await page.evaluate(() => (window as any).sha256('Hello'));
```

---

### page.exposeBinding()

```typescript
page.exposeBinding(
  name: string,
  callback: (source: BindingSource, ...args: any[]) => any,
  options?: { handle?: boolean }
): Promise<Disposable>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Function name on `window` |
| `callback` | `Function` | yes | Callback with a context object as the first argument |
| `options.handle` | `boolean` | no | If `true`: pass arguments as JSHandles |

Like `exposeFunction()`, but the callback additionally receives a `source` object with `{browserContext, page, frame}`.

```typescript
await page.exposeBinding('openBrowser', async (source, url) => {
  console.log(`Called from ${source.frame.url()}`);
  await source.page.goto(url);
});
```

---

### page.addInitScript()

```typescript
page.addInitScript(
  script: Function | string | { path?: string, content?: string },
  arg?: Serializable
): Promise<Disposable>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `script` | `Function\|string\|{path?,content?}` | yes | Script executed BEFORE every page load |
| `arg` | `Serializable` | no | Argument for the function |

Runs again on every navigation event (also after `reload()`).

```typescript
// Set a global variable before the page loads
await page.addInitScript(() => {
  (window as any).__TEST_MODE__ = true;
});

// With an argument
await page.addInitScript(({ key, value }) => {
  (window as any)[key] = value;
}, { key: 'API_BASE', value: 'http://mock-server' });

// From a file
await page.addInitScript({ path: './preload.js' });
```

Returns a `Disposable` — `await script[Symbol.asyncDispose]()` removes the script.

---

## 7. Script and style injection

### page.addScriptTag()

```typescript
page.addScriptTag(options?: {
  content?: string,
  path?: string,
  type?: string,
  url?: string
}): Promise<ElementHandle>
```

| Option | Type | Description |
|---|---|---|
| `content` | `string` | Inline JS code |
| `path` | `string` | Local file path (base64-encoded automatically) |
| `type` | `string` | Script type attribute (e.g. `'module'`) |
| `url` | `string` | External URL |

Inserts a `<script>` tag into the `<head>` of the page.

```typescript
await page.addScriptTag({ url: 'https://cdn.example.com/lib.js' });
await page.addScriptTag({ content: 'window.__LOADED = true;' });
await page.addScriptTag({ path: './fixtures/helper.js', type: 'module' });
```

---

### page.addStyleTag()

```typescript
page.addStyleTag(options?: {
  content?: string,
  path?: string,
  url?: string
}): Promise<ElementHandle>
```

Inserts a `<style>` tag or `<link rel=stylesheet>`.

```typescript
await page.addStyleTag({ content: 'body { display: none }' });
await page.addStyleTag({ url: 'https://cdn.example.com/style.css' });
await page.addStyleTag({ path: './fixtures/test.css' });
```

---

## 8. Network / routing

### page.route()

```typescript
page.route(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  handler: (route: Route, request: Request) => void | Promise<void>,
  options?: { times?: number }
): Promise<Disposable>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `url` | `string\|RegExp\|URLPattern\|Function` | yes | URL pattern or filter function |
| `handler` | `Function` | yes | Callback for every matched request |
| `options.times` | `number` | no | Max. number of handler invocations |

Intercepts network requests. Inside the handler, `route.fulfill()`, `route.abort()` or
`route.continue()` must be called.

```typescript
// Abort a request
await page.route('**/*.png', route => route.abort());

// Mocking
await page.route('**/api/users', route => route.fulfill({
  status: 200,
  contentType: 'application/json',
  body: JSON.stringify([{ id: 1, name: 'Test' }])
}));

// Modifying
await page.route('**/api/**', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.extra = 'added';
  await route.fulfill({ response, json });
});

// Only once
await page.route('**/api/data', route => route.fulfill({ body: '[]' }), { times: 1 });
```

---

### page.unroute()

```typescript
page.unroute(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  handler?: Function
): Promise<void>
```

Removes route handlers. Without `handler`, all handlers for the URL are removed.

```typescript
await page.unroute('**/*.png');
await page.unroute('**/api/**', specificHandler);
```

---

### page.unrouteAll()

```typescript
page.unrouteAll(options?: {
  behavior?: 'wait' | 'ignoreErrors' | 'default'
}): Promise<void>
```

Removes all route handlers.

```typescript
await page.unrouteAll();
await page.unrouteAll({ behavior: 'wait' });
```

---

### page.routeFromHAR()

```typescript
page.routeFromHAR(har: string, options?: {
  content?: 'omit' | 'embed' | 'attach',
  fallback?: 'abort' | 'continue',
  notFound?: 'abort' | 'fallback',
  update?: boolean,
  updateContent?: 'embed' | 'attach',
  updateMode?: 'full' | 'minimal',
  url?: string | RegExp
}): Promise<Disposable>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `har` | `string` | — | Path to the HAR file |
| `fallback` | `string` | `'abort'` | What to do when there is no match: `'abort'` or `'continue'` |
| `notFound` | `string` | `'abort'` | What to do when the HAR has no entry |
| `update` | `boolean` | `false` | Update the HAR file automatically |
| `url` | `string\|RegExp` | — | Only requests to this URL/these URLs |

```typescript
await page.routeFromHAR('./tests/fixtures/api.har');
await page.routeFromHAR('./api.har', { fallback: 'continue', url: '**/api/**' });
```

---

### page.requests()

```typescript
page.requests(): Promise<Request[]>
```

Returns up to 100 most recent network requests.

```typescript
const requests = await page.requests();
const apiRequests = requests.filter(r => r.url().includes('/api/'));
```

---

### page.setExtraHTTPHeaders()

```typescript
page.setExtraHTTPHeaders(headers: { [key: string]: string }): Promise<void>
```

Sets additional HTTP headers for all requests of the page.

```typescript
await page.setExtraHTTPHeaders({
  'Authorization': 'Bearer my-token',
  'X-Custom-Header': 'value'
});
```

---

## 9. Waiting / synchronization

### page.waitForLoadState()

```typescript
page.waitForLoadState(
  state?: 'load' | 'domcontentloaded' | 'networkidle',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `state` | `string` | no | `'load'` | Desired load state |
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |

```typescript
await page.waitForLoadState('networkidle');
await page.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

---

### page.waitForNavigation()

```typescript
page.waitForNavigation(options?: {
  timeout?: number,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean),
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

**Deprecated** — use `page.waitForURL()` or `page.goto()` with `waitUntil`.
Waits for the next navigation.

```typescript
await Promise.all([
  page.waitForNavigation(),
  page.click('a.nav-link')
]);
```

---

### page.waitForURL()

```typescript
page.waitForURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    timeout?: number,
    waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
  }
): Promise<void>
```

Waits until the page URL matches the pattern.

```typescript
await page.waitForURL('**/dashboard');
await page.waitForURL(/profile/, { waitUntil: 'networkidle' });
await page.waitForURL(url => url.searchParams.get('tab') === 'settings');
```

---

### page.waitForFunction()

```typescript
page.waitForFunction<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg,
  options?: {
    polling?: number | 'raf',
    timeout?: number
  }
): Promise<JSHandle<T>>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | `Function\|string` | yes | — | Function in the browser context, must return truthy |
| `arg` | `any` | no | — | Argument for the function |
| `options.polling` | `number\|'raf'` | no | `'raf'` | Polling interval in ms or `'raf'` |
| `options.timeout` | `number` | no | `defaultTimeout` | Max. wait time in ms |

```typescript
await page.waitForFunction(() => document.readyState === 'complete');
await page.waitForFunction(n => window.scrollY > n, 200, { polling: 100 });

const handle = await page.waitForFunction('window.__APP_READY === true');
await handle.dispose();
```

---

### page.waitForSelector()

```typescript
page.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<ElementHandle | null>
```

**Deprecated** — use `page.locator().waitFor()`.

| Option | Type | Default | Description |
|---|---|---|---|
| `state` | `string` | `'visible'` | Desired state |
| `strict` | `boolean` | `false` | Error on multiple elements |
| `timeout` | `number` | `defaultTimeout` | Max. wait time in ms |

```typescript
const el = await page.waitForSelector('.success-message');
await page.waitForSelector('.spinner', { state: 'hidden' });
```

---

### page.waitForRequest()

```typescript
page.waitForRequest(
  urlOrPredicate: string | RegExp | ((request: Request) => boolean | Promise<boolean>),
  options?: { timeout?: number }
): Promise<Request>
```

Waits for an outgoing network request.

```typescript
const request = await page.waitForRequest('**/api/login');
const postRequest = await page.waitForRequest(
  req => req.url().includes('/api/') && req.method() === 'POST'
);
```

---

### page.waitForResponse()

```typescript
page.waitForResponse(
  urlOrPredicate: string | RegExp | ((response: Response) => boolean | Promise<boolean>),
  options?: { timeout?: number }
): Promise<Response>
```

Waits for a network response.

```typescript
const response = await page.waitForResponse('**/api/data');
const [response2] = await Promise.all([
  page.waitForResponse(r => r.url().includes('/api/save') && r.status() === 200),
  page.click('#save-button')
]);
const json = await response2.json();
```

---

### page.waitForEvent()

```typescript
page.waitForEvent(event: string, optionsOrPredicate?: {
  predicate?: Function,
  timeout?: number
} | Function): Promise<any>
```

Waits for a page event.

```typescript
const popup = await page.waitForEvent('popup');
const download = await page.waitForEvent('download');

// With a predicate
const dialog = await page.waitForEvent('dialog', {
  predicate: d => d.type() === 'confirm'
});

// With a timeout
const frame = await page.waitForEvent('frameattached', { timeout: 5000 });
```

---

### page.waitForPopup()

```typescript
page.waitForPopup(
  callback: () => Promise<void>,
  options?: { timeout?: number }
): Promise<Page>
```

Waits for a popup triggered by `callback`.

```typescript
const popup = await page.waitForPopup(async () => {
  await page.click('a[target=_blank]');
});
await popup.waitForLoadState();
```

---

## 10. Screenshots & PDF

### page.screenshot()

```typescript
page.screenshot(options?: {
  animations?: 'disabled' | 'allow',
  caret?: 'hide' | 'initial',
  clip?: { x: number, y: number, width: number, height: number },
  fullPage?: boolean,
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
| `animations` | `string` | `'allow'` | Disable CSS animations |
| `caret` | `string` | `'hide'` | Hide the text cursor |
| `clip` | `object` | — | Capture only this area |
| `fullPage` | `boolean` | `false` | Whole page (including the non-visible area) |
| `mask` | `Locator[]` | — | Cover these elements with `maskColor` |
| `maskColor` | `string` | `'#FF00FF'` | Color for masked areas |
| `omitBackground` | `boolean` | `false` | Transparent background (PNG only) |
| `path` | `string` | — | Save path |
| `quality` | `number` | `100` (PNG) | JPEG quality 0–100 |
| `scale` | `string` | `'device'` | `'device'` respects devicePixelRatio |
| `type` | `string` | `'png'` | Image format |

```typescript
await page.screenshot({ path: 'screenshot.png' });
await page.screenshot({ fullPage: true, path: 'full.png' });
const buffer = await page.screenshot({ type: 'jpeg', quality: 80 });

// Hide areas
await page.screenshot({
  mask: [page.locator('.user-avatar')],
  maskColor: '#aabbcc'
});

// Only a viewport section
await page.screenshot({
  clip: { x: 0, y: 0, width: 800, height: 600 }
});
```

---

### page.pdf()

```typescript
page.pdf(options?: {
  displayHeaderFooter?: boolean,
  footerTemplate?: string,
  format?: string,
  headerTemplate?: string,
  height?: string | number,
  landscape?: boolean,
  margin?: {
    top?: string | number,
    right?: string | number,
    bottom?: string | number,
    left?: string | number
  },
  outline?: boolean,
  pageRanges?: string,
  path?: string,
  preferCSSPageSize?: boolean,
  printBackground?: boolean,
  scale?: number,
  tagged?: boolean,
  width?: string | number
}): Promise<Buffer>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `format` | `string` | `'Letter'` | Paper format: `'A4'`, `'Letter'`, `'A3'`, etc. |
| `landscape` | `boolean` | `false` | Landscape orientation |
| `printBackground` | `boolean` | `false` | Background colors/images |
| `displayHeaderFooter` | `boolean` | `false` | Show header/footer |
| `headerTemplate` | `string` | — | HTML template for the header |
| `footerTemplate` | `string` | — | HTML template for the footer |
| `margin` | `object` | — | Page margins |
| `scale` | `number` | `1` | Scaling (0.1–2) |
| `pageRanges` | `string` | — | e.g. `'1-5'`, `'8,10-12'` |
| `path` | `string` | — | Save path |
| `tagged` | `boolean` | `false` | Tagged PDF (accessibility) |
| `outline` | `boolean` | `false` | PDF outline from headings |

Available for Chromium only.

```typescript
await page.pdf({ path: 'output.pdf', format: 'A4' });
await page.pdf({
  format: 'A4',
  landscape: true,
  printBackground: true,
  margin: { top: '20mm', right: '20mm', bottom: '20mm', left: '20mm' }
});

const pdfBuffer = await page.pdf({ format: 'A4' });
```

---

## 11. Browser configuration

### page.setViewportSize()

```typescript
page.setViewportSize(viewportSize: {
  width: number,
  height: number
}): Promise<void>
```

```typescript
await page.setViewportSize({ width: 1280, height: 720 });
await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
```

---

### page.viewportSize()

```typescript
page.viewportSize(): { width: number, height: number } | null
```

Returns the current viewport size (`null` if not set).

```typescript
const viewport = page.viewportSize();
console.log(viewport?.width); // 1280
```

---

### page.emulateMedia()

```typescript
page.emulateMedia(options?: {
  colorScheme?: null | 'light' | 'dark' | 'no-preference',
  contrast?: null | 'no-preference' | 'more',
  forcedColors?: null | 'active' | 'none',
  media?: null | 'screen' | 'print',
  reducedMotion?: null | 'reduce' | 'no-preference'
}): Promise<void>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `colorScheme` | `string\|null` | — | Color scheme emulation; `null` = reset |
| `contrast` | `string\|null` | — | Contrast preference |
| `forcedColors` | `string\|null` | — | Windows Forced Colors Mode |
| `media` | `string\|null` | — | CSS media type; `null` = reset |
| `reducedMotion` | `string\|null` | — | Motion reduction |

```typescript
await page.emulateMedia({ colorScheme: 'dark' });
await page.emulateMedia({ media: 'print' });
await page.emulateMedia({ colorScheme: null }); // Reset
```

---

### page.setDefaultTimeout()

```typescript
page.setDefaultTimeout(timeout: number): void
```

Sets the default timeout for all actions AND assertions (in ms). `0` = unlimited.

```typescript
page.setDefaultTimeout(10000); // 10 seconds
```

---

### page.setDefaultNavigationTimeout()

```typescript
page.setDefaultNavigationTimeout(timeout: number): void
```

Sets the default timeout for navigation methods only (`goto`, `goBack`, etc.).

```typescript
page.setDefaultNavigationTimeout(30000);
```

---

## 12. Event handling / listeners

### page.on()

```typescript
page.on(event: string, listener: Function): Page
```

Registers a permanent event listener. Returns `Page` (chainable).

```typescript
page.on('console', msg => console.log('Browser:', msg.text()));
page.on('pageerror', err => console.error('Page error:', err.message));
page.on('dialog', async dialog => {
  console.log(dialog.message());
  await dialog.accept();
});
page.on('download', download => {
  console.log('Download started:', download.suggestedFilename());
});
page.on('request', request => {
  if (request.url().includes('/api/')) {
    console.log(`API request: ${request.method()} ${request.url()}`);
  }
});
```

---

### page.once()

```typescript
page.once(event: string, listener: Function): Page
```

Like `on()`, but removed automatically after the first invocation.

```typescript
page.once('dialog', dialog => dialog.accept());
```

---

### page.off()

```typescript
page.off(event: string, listener: Function): Page
```

Removes a specific event listener.

```typescript
const handler = (msg: ConsoleMessage) => console.log(msg.text());
page.on('console', handler);
// ...
page.off('console', handler);
```

---

### page.removeAllListeners()

```typescript
page.removeAllListeners(type?: string, options?: {
  behavior?: 'wait' | 'ignoreErrors' | 'default'
}): Promise<void>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `type` | `string` | no | Event type; omitted = remove all |
| `options.behavior` | `string` | no | `'wait'`: wait for running handlers; `'ignoreErrors'`: ignore errors |

```typescript
await page.removeAllListeners('console');
await page.removeAllListeners(); // All
```

---

## 13. Miscellaneous helper methods

### page.context()

```typescript
page.context(): BrowserContext
```

Returns the `BrowserContext` this page belongs to.

```typescript
const context = page.context();
await context.clearCookies();
```

---

### page.opener()

```typescript
page.opener(): Promise<Page | null>
```

Returns the page that opened this popup. `null` for normal pages.

```typescript
const opener = await page.opener();
if (opener) {
  console.log('Opened by:', opener.url());
}
```

---

### page.isClosed()

```typescript
page.isClosed(): boolean
```

Returns `true` if the page has been closed.

```typescript
if (!page.isClosed()) {
  await page.close();
}
```

---

### page.close()

```typescript
page.close(options?: {
  reason?: string,
  runBeforeUnload?: boolean
}): Promise<void>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `reason` | `string` | — | Reason for closing (reported on future actions) |
| `runBeforeUnload` | `boolean` | `false` | Run `beforeunload` handlers |

```typescript
await page.close();
await page.close({ runBeforeUnload: true });
await page.close({ reason: 'Test finished' });
```

---

### page.bringToFront()

```typescript
page.bringToFront(): Promise<void>
```

Brings the page (tab) to the foreground.

```typescript
await page.bringToFront();
```

---

### page.pause()

```typescript
page.pause(): Promise<void>
```

Pauses test execution and opens the Playwright Inspector (headed mode only).

```typescript
await page.pause(); // For debugging
```

---

### page.ariaSnapshot()

```typescript
page.ariaSnapshot(options?: {
  boxes?: boolean,
  depth?: number,
  mode?: 'ai' | 'default',
  timeout?: number
}): Promise<string>
```

Creates an ARIA accessibility tree snapshot as a YAML string.

```typescript
const snapshot = await page.ariaSnapshot();
expect(snapshot).toContain('button "Submit"');

await page.ariaSnapshot({ mode: 'ai' });
```

---

### page.consoleMessages()

```typescript
page.consoleMessages(options?: {
  filter?: 'all' | 'since-navigation'
}): Promise<ConsoleMessage[]>
```

Returns up to 200 most recently received console messages.

```typescript
const messages = await page.consoleMessages();
const errors = messages.filter(m => m.type() === 'error');
```

---

### page.pageErrors()

```typescript
page.pageErrors(options?: {
  filter?: 'all' | 'since-navigation'
}): Promise<Error[]>
```

Returns up to 200 most recently captured uncaught errors.

```typescript
const errors = await page.pageErrors();
if (errors.length > 0) {
  console.error('Page errors found:', errors[0].message);
}
```

---

### page.clearConsoleMessages()

```typescript
page.clearConsoleMessages(): Promise<void>
```

Clears the stored console message buffer.

```typescript
await page.clearConsoleMessages();
```

---

### page.clearPageErrors()

```typescript
page.clearPageErrors(): Promise<void>
```

Clears the stored page error buffer.

```typescript
await page.clearPageErrors();
```

---

### page.addLocatorHandler()

```typescript
page.addLocatorHandler(
  locator: Locator,
  handler: (locator: Locator) => void | Promise<void>,
  options?: {
    noWaitAfter?: boolean,
    times?: number
  }
): Promise<Disposable>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `locator` | `Locator` | yes | Locator of the overlay/popup |
| `handler` | `Function` | yes | Called when the overlay appears and blocks actionability |
| `options.noWaitAfter` | `boolean` | no | Do not wait for it to disappear |
| `options.times` | `number` | no | Max. invocations (then removed automatically) |

Registers handlers for cookie banners, modals etc. that block actionability checks.

```typescript
await page.addLocatorHandler(
  page.getByText('Cookie settings'),
  async () => {
    await page.getByRole('button', { name: 'Accept all' }).click();
  }
);
```

---

### page.removeLocatorHandler()

```typescript
page.removeLocatorHandler(locator: Locator): Promise<void>
```

Removes the handler for a specific locator.

```typescript
await page.removeLocatorHandler(page.getByText('Cookie settings'));
```

---

### page.pickLocator()

```typescript
page.pickLocator(): Promise<Locator>
```

Starts the interactive locator picker (Playwright Inspector). Returns the selected locator.

```typescript
const locator = await page.pickLocator();
console.log(locator); // Locator object
```

---

### page.cancelPickLocator()

```typescript
page.cancelPickLocator(): Promise<void>
```

Cancels the locator picker.

```typescript
await page.cancelPickLocator();
```

---

### page.hideHighlight()

```typescript
page.hideHighlight(): Promise<void>
```

Hides all active locator highlight overlays.

```typescript
await page.hideHighlight();
```

---

### page.requestGC()

```typescript
page.requestGC(): Promise<void>
```

Requests garbage collection in the browser (experimental, helpful for memory leak tests).

```typescript
await page.requestGC();
```

---

## 14. Properties

### page.keyboard

```typescript
page.keyboard: Keyboard
```

Access to the `Keyboard` object for low-level keyboard input.

```typescript
await page.keyboard.press('Enter');
await page.keyboard.type('Hello World');
await page.keyboard.down('Shift');
await page.keyboard.up('Shift');
await page.keyboard.insertText('Unicode: é');
```

---

### page.mouse

```typescript
page.mouse: Mouse
```

Access to the `Mouse` object for low-level mouse operations.

```typescript
await page.mouse.move(100, 200);
await page.mouse.down();
await page.mouse.up();
await page.mouse.click(100, 200);
await page.mouse.dblclick(100, 200);
await page.mouse.wheel(0, 300); // Scrolling
```

---

### page.touchscreen

```typescript
page.touchscreen: Touchscreen
```

Access to the `Touchscreen` object for touch events.

```typescript
await page.touchscreen.tap(150, 250);
```

---

## 15. Events

Events are subscribed to with `page.on(event, listener)`.

| Event | Payload type | Description |
|---|---|---|
| `'close'` | `Page` | The page was closed |
| `'console'` | `ConsoleMessage` | Browser console message (log, warn, error, dir, ...) |
| `'crash'` | `Page` | The page crashed (e.g. OOM) |
| `'dialog'` | `Dialog` | `alert()`, `confirm()`, `prompt()` or `beforeunload` |
| `'download'` | `Download` | A download is starting |
| `'error'` | `Error` | Uncaught exception in the page |
| `'filechooser'` | `FileChooser` | A file selection dialog appears |
| `'frameattached'` | `Frame` | A new frame was attached |
| `'framedetached'` | `Frame` | A frame was removed |
| `'framenavigated'` | `Frame` | A frame navigated |
| `'load'` | `Page` | `load` event of the page |
| `'pageerror'` | `Error` | Uncaught error in the page (like `window.onerror`) |
| `'popup'` | `Page` | A popup page was opened |
| `'request'` | `Request` | A network request was sent |
| `'requestfailed'` | `Request` | A network request failed |
| `'requestfinished'` | `Request` | A network request finished |
| `'response'` | `Response` | A network response was received |
| `'websocket'` | `WebSocket` | A new WebSocket object was created |
| `'worker'` | `Worker` | A web worker was created |
| `'domcontentloaded'` | `Page` | `DOMContentLoaded` event |

### Event examples

```typescript
// Capture console output
page.on('console', msg => {
  const type = msg.type();
  if (type === 'error') console.error('[BROWSER ERROR]', msg.text());
});

// Handle dialogs automatically
page.on('dialog', async dialog => {
  if (dialog.type() === 'confirm') {
    await dialog.accept();
  } else {
    await dialog.dismiss();
  }
});

// File downloads
page.on('download', async download => {
  await download.saveAs('/tmp/' + download.suggestedFilename());
});

// Handle popups
page.on('popup', async popup => {
  await popup.waitForLoadState();
  console.log('Popup URL:', popup.url());
});

// Network monitoring
page.on('response', response => {
  if (!response.ok()) {
    console.warn(`HTTP ${response.status()} for ${response.url()}`);
  }
});

// File chooser
page.on('filechooser', async fileChooser => {
  await fileChooser.setFiles('/path/to/file.pdf');
});

// Web worker
page.on('worker', worker => {
  console.log('Worker created:', worker.url());
});
```

---

## 16. Manifest

| Category | Number of documented members |
|---|---|
| Navigation | 6 methods (goto, goBack, goForward, reload, url, title) |
| Page content | 9 methods (content, setContent, getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible) |
| Locator factory | 10 methods (locator, getByRole, getByText, getByLabel, getByPlaceholder, getByAltText, getByTitle, getByTestId, frameLocator) |
| Frame management | 3 methods (frames, frame, mainFrame) |
| Element interaction | 16 methods (click, dblclick, check, uncheck, setChecked, fill, focus, hover, press, type, tap, selectOption, setInputFiles, dispatchEvent, dragAndDrop, selectText) |
| JavaScript | 5 methods (evaluate, evaluateHandle, exposeFunction, exposeBinding, addInitScript) |
| Script/style injection | 2 methods (addScriptTag, addStyleTag) |
| Network/routing | 5 methods (route, unroute, unrouteAll, routeFromHAR, requests, setExtraHTTPHeaders) |
| Waiting/sync | 8 methods (waitForLoadState, waitForNavigation, waitForURL, waitForFunction, waitForSelector, waitForRequest, waitForResponse, waitForEvent, waitForPopup) |
| Screenshots/PDF | 2 methods (screenshot, pdf) |
| Browser configuration | 5 methods (setViewportSize, viewportSize, emulateMedia, setDefaultTimeout, setDefaultNavigationTimeout) |
| Event handling | 4 methods (on, once, off, removeAllListeners) |
| Miscellaneous | 14 methods (context, opener, isClosed, close, bringToFront, pause, ariaSnapshot, consoleMessages, pageErrors, clearConsoleMessages, clearPageErrors, addLocatorHandler, removeLocatorHandler, pickLocator, cancelPickLocator, hideHighlight, requestGC) |
| Properties | 3 (keyboard, mouse, touchscreen) |
| Events | 17 events |

**Total: ~102 methods/properties + 17 events**

**Conclusion:** the `Page` class is the heart of the Playwright API. It combines navigation, element interaction
(via selector and locator), JavaScript evaluation, network interception, configuration and event handling
in a single class. For new tests, locator-based methods (`page.locator()`, `getBy*()`) should be
preferred over the outdated direct selector methods.

---

**Source:** https://playwright.dev/docs/api/class-page
