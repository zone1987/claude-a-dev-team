# Playwright class-frame: Complete API reference

`Frame` represents a single frame (main frame or iframe) within a page.
Many methods of the `Page` class delegate internally to the main frame (`page.mainFrame()`).
When working directly with iframes you obtain a `Frame` object via `page.frame()`,
`page.frames()`, or as the result of `frameattached` events.

---

## Contents

- [Table of contents](#table-of-contents)
- [1. Navigation & content](#1-navigation-content)
- [2. Frame properties & hierarchy](#2-frame-properties-hierarchy)
- [3. Locator factory methods](#3-locator-factory-methods)
- [4. JavaScript execution](#4-javascript-execution)
- [5. Script and style injection](#5-script-and-style-injection)
- [6. Element interactions (selector-based, deprecated)](#6-element-interactions-selector-based-deprecated)
- [7. Element content & state (selector-based, deprecated)](#7-element-content-state-selector-based-deprecated)
- [8. Waiting / synchronization](#8-waiting-synchronization)
- [9. Legacy Selector API (deprecated)](#9-legacy-selector-api-deprecated)
- [10. Manifest](#10-manifest)

## Table of contents

1. [Navigation & content](#1-navigation--content)
2. [Frame properties & hierarchy](#2-frame-properties--hierarchy)
3. [Locator factory methods](#3-locator-factory-methods)
4. [JavaScript execution](#4-javascript-execution)
5. [Script and style injection](#5-script-and-style-injection)
6. [Element interactions (selector-based, deprecated)](#6-element-interactions-selector-based-deprecated)
7. [Element content & state (selector-based, deprecated)](#7-element-content--state-selector-based-deprecated)
8. [Waiting / synchronization](#8-waiting--synchronization)
9. [Legacy Selector API (deprecated)](#9-legacy-selector-api-deprecated)
10. [Manifest](#10-manifest)

---

## 1. Navigation & content

### frame.goto()

```typescript
frame.goto(url: string, options?: {
  referer?: string,
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | `string` | yes | — | Target URL |
| `options.referer` | `string` | no | — | HTTP Referer header |
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |
| `options.waitUntil` | `string` | no | `'load'` | When navigation counts as complete |

Navigates the frame to the given URL.

```typescript
// Navigate the main frame (equivalent to page.goto)
await page.mainFrame().goto('https://example.com');

// Navigate an iframe
const frame = page.frame({ name: 'my-frame' });
await frame?.goto('https://other-domain.com');
```

---

### frame.content()

```typescript
frame.content(): Promise<string>
```

Returns the complete HTML content of the frame (including the doctype).

```typescript
const html = await frame.content();
expect(html).toContain('<h1>');
```

---

### frame.setContent()

```typescript
frame.setContent(html: string, options?: {
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
await frame.setContent('<h1>Test</h1><p>Content</p>');
await frame.setContent(htmlString, { waitUntil: 'domcontentloaded' });
```

---

### frame.title()

```typescript
frame.title(): Promise<string>
```

Returns the page title of the frame.

```typescript
const title = await frame.title();
```

---

### frame.url()

```typescript
frame.url(): string
```

Returns the current URL of the frame (synchronously).

```typescript
console.log(frame.url()); // 'https://example.com/path'
```

---

## 2. Frame properties & hierarchy

### frame.name()

```typescript
frame.name(): string
```

Returns the `name` attribute of the `<iframe>` tag. Empty string for the main frame.

```typescript
const name = frame.name(); // 'my-frame' or ''
```

---

### frame.isDetached()

```typescript
frame.isDetached(): boolean
```

Returns `true` if the frame has been removed from the DOM.

```typescript
if (!frame.isDetached()) {
  await frame.locator('button').click();
}
```

---

### frame.page()

```typescript
frame.page(): Page
```

Returns the `Page` instance this frame belongs to.

```typescript
const page = frame.page();
await page.screenshot();
```

---

### frame.parentFrame()

```typescript
frame.parentFrame(): Frame | null
```

Returns the parent frame. `null` for the main frame and for detached frames.

```typescript
const parent = frame.parentFrame();
if (parent) {
  console.log('Parent URL:', parent.url());
}
```

---

### frame.childFrames()

```typescript
frame.childFrames(): Frame[]
```

Returns all direct child frames.

```typescript
const children = frame.childFrames();
for (const child of children) {
  console.log('Child frame:', child.url());
}
```

---

### frame.frameElement()

```typescript
frame.frameElement(): Promise<ElementHandle>
```

Returns the `<iframe>` or `<frame>` DOM element that corresponds to this frame.

```typescript
const frameElement = await frame.frameElement();
const src = await frameElement.getAttribute('src');
console.log('iframe src:', src);
```

---

## 3. Locator factory methods

All locator methods of the frame correspond 1:1 to the identically named methods on `Page`.
They operate in the context of this specific frame, however.

### frame.locator()

```typescript
frame.locator(selector: string, options?: {
  has?: Locator,
  hasNot?: Locator,
  hasText?: string | RegExp,
  hasNotText?: string | RegExp
}): Locator
```

Creates a locator relative to the frame.

```typescript
const iframe = page.frame({ name: 'payment' });
await iframe?.locator('input[name=card]').fill('4111111111111111');
```

---

### frame.frameLocator()

```typescript
frame.frameLocator(selector: string): FrameLocator
```

Creates a locator for nested iframes.

```typescript
const outerFrame = page.frame('outer');
const innerLocator = outerFrame?.frameLocator('#inner-iframe');
await innerLocator?.getByRole('button').click();
```

---

### frame.getByRole()

```typescript
frame.getByRole(role: AriaRole, options?: {
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

Finds elements by ARIA role in the frame context.

```typescript
const frame = page.frame('login-frame');
await frame?.getByRole('button', { name: 'Sign in' }).click();
await frame?.getByRole('textbox', { name: 'Password' }).fill('secret');
```

---

### frame.getByText()

```typescript
frame.getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
const frame = page.frame('content');
await frame?.getByText('Welcome').click();
```

---

### frame.getByLabel()

```typescript
frame.getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByLabel('E-mail').fill('test@example.com');
```

---

### frame.getByPlaceholder()

```typescript
frame.getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByPlaceholder('Search term').fill('Playwright');
```

---

### frame.getByAltText()

```typescript
frame.getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByAltText('Logo').click();
```

---

### frame.getByTitle()

```typescript
frame.getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByTitle('Close').click();
```

---

### frame.getByTestId()

```typescript
frame.getByTestId(testId: string | RegExp): Locator
```

```typescript
await frame?.getByTestId('submit-btn').click();
```

---

## 4. JavaScript execution

### frame.evaluate()

```typescript
frame.evaluate<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pageFunction` | `Function\|string` | yes | Function executed in the frame context |
| `arg` | `Serializable\|JSHandle` | no | Argument (serializable or JSHandle) |

Returns a serialized JSON value.

```typescript
const url = await frame.evaluate(() => window.location.href);
const sum = await frame.evaluate(({ a, b }) => a + b, { a: 5, b: 3 });
const title = await frame.evaluate('document.title');

// DOM manipulation
await frame.evaluate(() => {
  document.querySelector('.overlay')?.remove();
});
```

---

### frame.evaluateHandle()

```typescript
frame.evaluateHandle<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

Like `evaluate()`, but returns a `JSHandle` (no JSON serialization overhead).

```typescript
const bodyHandle = await frame.evaluateHandle(() => document.body);
const children = await frame.evaluate(body => body.children.length, bodyHandle);
await bodyHandle.dispose();
```

---

## 5. Script and style injection

### frame.addScriptTag()

```typescript
frame.addScriptTag(options?: {
  content?: string,
  path?: string,
  type?: string,
  url?: string
}): Promise<ElementHandle>
```

| Option | Type | Description |
|---|---|---|
| `content` | `string` | Inline JS code |
| `path` | `string` | Local file path |
| `type` | `string` | Script type attribute (e.g. `'module'`) |
| `url` | `string` | External URL |

Inserts a `<script>` tag into the frame.

```typescript
await frame.addScriptTag({ url: 'https://cdn.example.com/lib.js' });
await frame.addScriptTag({ content: 'window.__FRAME_LOADED = true;' });
await frame.addScriptTag({ path: './helper.js', type: 'module' });
```

---

### frame.addStyleTag()

```typescript
frame.addStyleTag(options?: {
  content?: string,
  path?: string,
  url?: string
}): Promise<ElementHandle>
```

Inserts a `<style>` tag or `<link rel=stylesheet>` into the frame.

```typescript
await frame.addStyleTag({ content: '.highlight { background: yellow; }' });
await frame.addStyleTag({ url: 'https://cdn.example.com/style.css' });
```

---

## 6. Element interactions (selector-based, deprecated)

**Note:** prefer `frame.locator().click()` etc. over these direct selector methods.

### frame.click()

```typescript
frame.click(selector: string, options?: {
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

Clicks the first element matching the selector.

```typescript
await frame.click('button[type=submit]');
await frame.click('#menu-item', { button: 'right' });
await frame.click('a', { modifiers: ['Control'] });
```

---

### frame.dblclick()

```typescript
frame.dblclick(selector: string, options?: {
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

Double click.

```typescript
await frame.dblclick('.editable');
```

---

### frame.check()

```typescript
frame.check(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Checks a checkbox or radio.

```typescript
await frame.check('#accept-terms');
```

---

### frame.uncheck()

```typescript
frame.uncheck(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Unchecks a checkbox.

```typescript
await frame.uncheck('#newsletter');
```

---

### frame.fill()

```typescript
frame.fill(selector: string, value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Clears the existing value and fills the input field.

```typescript
await frame.fill('input[name=email]', 'test@example.com');
await frame.fill('textarea#comment', 'My comment');
```

---

### frame.focus()

```typescript
frame.focus(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Sets focus on an element.

```typescript
await frame.focus('input[autofocus]');
```

---

### frame.hover()

```typescript
frame.hover(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Moves the mouse over an element.

```typescript
await frame.hover('.tooltip-trigger');
```

---

### frame.tap()

```typescript
frame.tap(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch tap (touchscreen emulation required).

```typescript
await frame.tap('.mobile-button');
```

---

### frame.press()

```typescript
frame.press(selector: string, key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | Element to focus |
| `key` | `string` | yes | — | Key combination |
| `options.delay` | `number` | no | `0` | Ms between keydown and keyup |

```typescript
await frame.press('input', 'Enter');
await frame.press('body', 'Escape');
```

---

### frame.type()

```typescript
frame.type(selector: string, text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated.** Simulates real keyboard input without clearing the existing content.

```typescript
await frame.type('input', 'Hello', { delay: 50 });
```

---

### frame.selectOption()

```typescript
frame.selectOption(
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

Selects options in a `<select>` element.

```typescript
await frame.selectOption('select#country', 'de');
await frame.selectOption('select', { label: 'Germany' });
await frame.selectOption('select[multiple]', ['de', 'at']);
```

---

### frame.setInputFiles()

```typescript
frame.setInputFiles(
  selector: string,
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Sets files for an `<input type=file>`.

```typescript
await frame.setInputFiles('input[type=file]', '/path/to/file.pdf');
await frame.setInputFiles('input', [], { }); // Reset
```

---

### frame.dispatchEvent()

```typescript
frame.dispatchEvent(
  selector: string,
  type: string,
  eventInit?: EvaluationArgument,
  options?: {
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Triggers a DOM event.

```typescript
await frame.dispatchEvent('button', 'click');
await frame.dispatchEvent('#field', 'input', { bubbles: true });
```

---

### frame.dragAndDrop()

```typescript
frame.dragAndDrop(source: string, target: string, options?: {
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

Drag and drop within the frame.

```typescript
await frame.dragAndDrop('#source', '#target');
await frame.dragAndDrop('.card', '.dropzone', { steps: 5 });
```

---

## 7. Element content & state (selector-based, deprecated)

### frame.getAttribute()

```typescript
frame.getAttribute(selector: string, name: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

```typescript
const href = await frame.getAttribute('a.link', 'href');
```

---

### frame.innerHTML()

```typescript
frame.innerHTML(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const content = await frame.innerHTML('.article-body');
```

---

### frame.innerText()

```typescript
frame.innerText(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const text = await frame.innerText('h1');
```

---

### frame.textContent()

```typescript
frame.textContent(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

```typescript
const text = await frame.textContent('#description');
```

---

### frame.inputValue()

```typescript
frame.inputValue(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const value = await frame.inputValue('input[name=email]');
```

---

### frame.isChecked()

```typescript
frame.isChecked(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const checked = await frame.isChecked('#terms');
```

---

### frame.isDisabled()

```typescript
frame.isDisabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const disabled = await frame.isDisabled('button[type=submit]');
```

---

### frame.isEditable()

```typescript
frame.isEditable(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const editable = await frame.isEditable('input[name=username]');
```

---

### frame.isEnabled()

```typescript
frame.isEnabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const enabled = await frame.isEnabled('.submit-btn');
```

---

### frame.isHidden()

```typescript
frame.isHidden(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const hidden = await frame.isHidden('.spinner');
```

---

### frame.isVisible()

```typescript
frame.isVisible(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const visible = await frame.isVisible('.success-message');
```

---

### frame.selectText()

```typescript
frame.selectText(selector: string, options?: {
  force?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Selects the text of an input field.

```typescript
await frame.selectText('input[name=title]');
```

---

## 8. Waiting / synchronization

### frame.waitForLoadState()

```typescript
frame.waitForLoadState(
  state?: 'load' | 'domcontentloaded' | 'networkidle',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `state` | `string` | no | `'load'` | Desired load state |
| `options.timeout` | `number` | no | `defaultNavigationTimeout` | Max. wait time in ms |

```typescript
await frame.waitForLoadState('networkidle');
await frame.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

---

### frame.waitForNavigation()

```typescript
frame.waitForNavigation(options?: {
  timeout?: number,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean),
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

**Deprecated** — use `frame.waitForURL()`. Waits for navigation in the frame.

```typescript
await Promise.all([
  frame.waitForNavigation(),
  frame.click('a.navigate')
]);
```

---

### frame.waitForURL()

```typescript
frame.waitForURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    timeout?: number,
    waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
  }
): Promise<void>
```

Waits until the frame URL matches the pattern.

```typescript
await frame.waitForURL('**/dashboard');
await frame.waitForURL(/profile/, { waitUntil: 'networkidle' });
```

---

### frame.waitForFunction()

```typescript
frame.waitForFunction<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg,
  options?: {
    polling?: number | 'raf',
    timeout?: number
  }
): Promise<JSHandle<T>>
```

| Option | Type | Default | Description |
|---|---|---|---|
| `polling` | `number\|'raf'` | `'raf'` | Polling interval |
| `timeout` | `number` | `defaultTimeout` | Max. wait time |

Waits until the function returns truthy in the frame context.

```typescript
await frame.waitForFunction(() => document.readyState === 'complete');
await frame.waitForFunction(count => window.itemCount >= count, 10);
```

---

### frame.waitForSelector()

```typescript
frame.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<ElementHandle | null>
```

**Deprecated** — use `frame.locator().waitFor()`.

```typescript
await frame.waitForSelector('.content', { state: 'visible' });
const handle = await frame.waitForSelector('.result');
```

---

## 9. Legacy Selector API (deprecated)

### frame.$()

```typescript
frame.$(selector: string, options?: { strict?: boolean }): Promise<ElementHandle | null>
```

Returns the first element matching the selector. `null` if not found.

```typescript
const el = await frame.$('h1');
if (el) {
  const text = await el.textContent();
}
```

---

### frame.$$()

```typescript
frame.$$(selector: string): Promise<ElementHandle[]>
```

Returns all elements matching the selector.

```typescript
const items = await frame.$$('li.item');
for (const item of items) {
  console.log(await item.textContent());
}
```

---

### frame.$eval()

```typescript
frame.$eval<T>(
  selector: string,
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg,
  options?: { strict?: boolean }
): Promise<T>
```

Runs the function on the first matched element.

```typescript
const text = await frame.$eval('h1', el => el.textContent);
const href = await frame.$eval('a.link', el => el.getAttribute('href'));
```

---

### frame.$$eval()

```typescript
frame.$$eval<T>(
  selector: string,
  pageFunction: (elements: Element[], arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

Runs the function on ALL matched elements.

```typescript
const texts = await frame.$$eval('li', els => els.map(el => el.textContent));
const count = await frame.$$eval('.item', els => els.length);
```

---

## 10. Manifest

| Category | Documented members |
|---|---|
| Navigation & content | 5 methods (goto, content, setContent, title, url) |
| Frame properties & hierarchy | 6 methods (name, isDetached, page, parentFrame, childFrames, frameElement) |
| Locator factory | 10 methods (locator, frameLocator, getByRole, getByText, getByLabel, getByPlaceholder, getByAltText, getByTitle, getByTestId) |
| JavaScript execution | 2 methods (evaluate, evaluateHandle) |
| Script/style injection | 2 methods (addScriptTag, addStyleTag) |
| Element interactions | 12 methods (click, dblclick, check, uncheck, fill, focus, hover, tap, press, type, selectOption, setInputFiles, dispatchEvent, dragAndDrop) |
| Element content & state | 11 methods (getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible, selectText) |
| Waiting/sync | 4 methods (waitForLoadState, waitForNavigation, waitForURL, waitForFunction, waitForSelector) |
| Legacy Selector API | 4 methods ($, $$, $eval, $$eval) |

**Total: ~56 methods/properties**

**Summary:** `Frame` largely mirrors the `Page` API, but applies specifically to a single
iframe context. Modern Playwright tests should prefer `page.frameLocator()` with locator-based
methods. Working with `Frame` directly is mainly relevant for complex multi-frame scenarios and
`evaluate()` executions in the iframe context.

---

**Source:** https://playwright.dev/docs/api/class-frame
