# class-locator — Playwright API Reference

Complete method reference for the `Locator` class. A `Locator` represents a way to find one or more elements on the page. It is lazy and performs the actual DOM search only when an action is executed.

Method count: 57 (excluding deprecated aliases)

---

## Contents

- [all()](#all)
- [allInnerTexts()](#allinnertexts)
- [allTextContents()](#alltextcontents)
- [and()](#and)
- [ariaSnapshot()](#ariasnapshot)
- [blur()](#blur)
- [boundingBox()](#boundingbox)
- [check()](#check)
- [clear()](#clear)
- [click()](#click)
- [contentFrame()](#contentframe)
- [count()](#count)
- [dblclick()](#dblclick)
- [describe()](#describe)
- [description()](#description)
- [dispatchEvent()](#dispatchevent)
- [dragTo()](#dragto)
- [drop()](#drop)
- [evaluate()](#evaluate)
- [evaluateAll()](#evaluateall)
- [evaluateHandle()](#evaluatehandle)
- [fill()](#fill)
- [filter()](#filter)
- [first()](#first)
- [focus()](#focus)
- [frameLocator()](#framelocator)
- [getAttribute()](#getattribute)
- [getByAltText()](#getbyalttext)
- [getByLabel()](#getbylabel)
- [getByPlaceholder()](#getbyplaceholder)
- [getByRole()](#getbyrole)
- [getByTestId()](#getbytestid)
- [getByText()](#getbytext)
- [getByTitle()](#getbytitle)
- [hideHighlight()](#hidehighlight)
- [highlight()](#highlight)
- [hover()](#hover)
- [innerHTML()](#innerhtml)
- [innerText()](#innertext)
- [inputValue()](#inputvalue)
- [isChecked()](#ischecked)
- [isDisabled()](#isdisabled)
- [isEditable()](#iseditable)
- [isEnabled()](#isenabled)
- [isHidden()](#ishidden)
- [isVisible()](#isvisible)
- [last()](#last)
- [locator()](#locator)
- [nth()](#nth)
- [or()](#or)
- [press()](#press)
- [pressSequentially()](#presssequentially)
- [screenshot()](#screenshot)
- [scrollIntoViewIfNeeded()](#scrollintoviewifneeded)
- [selectOption()](#selectoption)
- [selectText()](#selecttext)
- [setChecked()](#setchecked)
- [setInputFiles()](#setinputfiles)
- [tap()](#tap)
- [textContent()](#textcontent)
- [uncheck()](#uncheck)
- [waitFor()](#waitfor)
- [Method Overview (57 methods)](#method-overview-57-methods)

## all()

```typescript
all(): Promise<Array<Locator>>
```

Returns all elements matching the locator as an array of individual locators.
Does **not** wait for elements — returns an immediate snapshot.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<Array<Locator>>`

```typescript
const rows = await page.getByRole('row').all();
for (const row of rows) await row.click();
```

---

## allInnerTexts()

```typescript
allInnerTexts(): Promise<Array<string>>
```

Returns the `node.innerText` values of all matching elements.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<Array<string>>`

```typescript
const texts = await page.getByRole('listitem').allInnerTexts();
```

---

## allTextContents()

```typescript
allTextContents(): Promise<Array<string>>
```

Returns the `node.textContent` values of all matching elements.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<Array<string>>`

```typescript
const contents = await page.locator('p').allTextContents();
```

---

## and()

```typescript
and(locator: Locator): Locator
```

Creates a new locator that must satisfy **both** conditions (logical AND).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `locator` | `Locator` | yes | — | Additional locator whose condition must be satisfied |

**Returns:** `Locator`

```typescript
const button = page.getByRole('button').and(page.getByTitle('Save'));
```

---

## ariaSnapshot()

```typescript
ariaSnapshot(options?: {
  boxes?: boolean;
  depth?: number;
  mode?: 'ai' | 'default';
  timeout?: number;
}): Promise<string>
```

Creates an ARIA snapshot of the element for accessibility tests.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.boxes` | `boolean` | no | `false` | Include bounding box information in the snapshot |
| `options.depth` | `number` | no | unlimited | Maximum depth of the snapshot |
| `options.mode` | `'ai' \| 'default'` | no | `'default'` | Snapshot format |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<string>`

```typescript
const snapshot = await page.locator('#nav').ariaSnapshot();
```

---

## blur()

```typescript
blur(options?: { timeout?: number }): Promise<void>
```

Calls `blur()` on the element, thereby removing focus.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('Name').blur();
```

---

## boundingBox()

```typescript
boundingBox(options?: { timeout?: number }): Promise<null | {
  x: number;
  y: number;
  width: number;
  height: number;
}>
```

Returns the bounding box of the element relative to the main viewport, or `null` if it is invisible.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<null | { x: number; y: number; width: number; height: number }>`

```typescript
const box = await page.locator('.tooltip').boundingBox();
if (box) console.log(box.x, box.y, box.width, box.height);
```

---

## check()

```typescript
check(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Puts a checkbox or radio element into the checked state.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability checks |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Click position relative to the padding box |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability, do not click |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('I agree').check();
```

---

## clear()

```typescript
clear(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  timeout?: number;
}): Promise<void>
```

Clears the content of an input field.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability checks |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('textbox').clear();
```

---

## click()

```typescript
click(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
  delay?: number;
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  steps?: number;
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Clicks the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Mouse button |
| `options.clickCount` | `number` | no | `1` | Number of clicks |
| `options.delay` | `number` | no | `0` | Delay between mousedown and mouseup in ms |
| `options.force` | `boolean` | no | `false` | Bypass actionability checks |
| `options.modifiers` | `Array<string>` | no | `[]` | Modifier keys held down simultaneously |
| `options.noWaitAfter` | `boolean` | no | `false` | Do not wait for navigation after the click |
| `options.position` | `{ x: number; y: number }` | no | center | Click coordinates relative to the padding box |
| `options.steps` | `number` | no | `1` | Interpolated mousemove events |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability, do not click |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('button', { name: 'Submit' }).click();
await page.getByText('Options').click({ button: 'right' });
```

---

## contentFrame()

```typescript
contentFrame(): FrameLocator
```

Returns a `FrameLocator` pointing at the iframe element that this locator describes.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `FrameLocator`

```typescript
const frame = page.locator('iframe[title="Editor"]').contentFrame();
await frame.getByRole('textbox').fill('Hello');
```

---

## count()

```typescript
count(): Promise<number>
```

Returns the number of matching elements.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<number>`

```typescript
const n = await page.getByRole('listitem').count();
expect(n).toBe(3);
```

---

## dblclick()

```typescript
dblclick(options?: {
  button?: 'left' | 'right' | 'middle';
  delay?: number;
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  steps?: number;
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Double-clicks the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.button` | `'left' \| 'right' \| 'middle'` | no | `'left'` | Mouse button |
| `options.delay` | `number` | no | `0` | Delay between mousedown/mouseup in ms |
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.modifiers` | `Array<string>` | no | `[]` | Modifier keys |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Click position |
| `options.steps` | `number` | no | `1` | Interpolated mousemove events |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.getByText('Filename').dblclick();
```

---

## describe()

```typescript
describe(description: string): Locator
```

Sets a custom description that is shown in the Trace Viewer. Returns the locator (chainable).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `description` | `string` | yes | — | Description text for the Trace Viewer |

**Returns:** `Locator`

```typescript
const btn = page.getByRole('button').describe('Main CTA');
```

---

## description()

```typescript
description(): null | string
```

Returns the description previously set with `describe()`, or `null`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `null | string`

```typescript
const desc = page.getByRole('button').describe('Save').description();
// => 'Save'
```

---

## dispatchEvent()

```typescript
dispatchEvent(
  type: string,
  eventInit?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<void>
```

Dispatches a DOM event on the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `type` | `string` | yes | — | DOM event type, e.g. `'click'`, `'dragstart'` |
| `eventInit` | `EvaluationArgument` | no | `{}` | Event-specific initialization parameters |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.locator('#drag').dispatchEvent('dragstart');
```

---

## dragTo()

```typescript
dragTo(target: Locator, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  sourcePosition?: { x: number; y: number };
  steps?: number;
  targetPosition?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Drags the element onto a target element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `target` | `Locator` | yes | — | Target locator the element is dragged onto |
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.sourcePosition` | `{ x: number; y: number }` | no | center | Start position within the source element |
| `options.steps` | `number` | no | `1` | Interpolated mousemove events |
| `options.targetPosition` | `{ x: number; y: number }` | no | center | Target position within the target element |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.locator('#item-1').dragTo(page.locator('#target-zone'));
```

---

## drop()

```typescript
drop(payload: {
  files?: string | Array<string> | { name: string; mimeType: string; buffer: Buffer } | Array<{ name: string; mimeType: string; buffer: Buffer }>;
  data?: Record<string, string>;
  position?: { x: number; y: number };
}, options?: { timeout?: number }): Promise<void>
```

Simulates an external drag-and-drop of files or data onto the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `payload.files` | `string \| string[] \| FilePayload \| FilePayload[]` | no | — | File paths or buffer objects |
| `payload.data` | `Record<string, string>` | no | — | MIME type to data map |
| `payload.position` | `{ x: number; y: number }` | no | center | Drop position |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.locator('#dropzone').drop({ files: ['path/to/file.pdf'] });
```

---

## evaluate()

```typescript
evaluate<R>(
  pageFunction: (element: SVGElement | HTMLElement, arg?: unknown) => R,
  arg?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<R>
```

Executes JavaScript in the browser context; the matching element is passed as the first argument.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | yes | — | Code to execute; the first argument is the DOM element |
| `arg` | `EvaluationArgument` | no | — | Serializable value passed as the second argument |
| `options.timeout` | `number` | no | global default | Maximum wait time for the locator in ms |

**Returns:** `Promise<R>`

```typescript
const tagName = await page.locator('h1').evaluate(el => el.tagName);
```

---

## evaluateAll()

```typescript
evaluateAll<R>(
  pageFunction: (elements: Array<SVGElement | HTMLElement>, arg?: unknown) => R,
  arg?: EvaluationArgument
): Promise<R>
```

Executes JavaScript; all matching elements are passed as an array.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | yes | — | Code; the first argument is an array of all DOM elements |
| `arg` | `EvaluationArgument` | no | — | Serializable value |

**Returns:** `Promise<R>`

```typescript
const values = await page.locator('input').evaluateAll(els => els.map(e => e.value));
```

---

## evaluateHandle()

```typescript
evaluateHandle(
  pageFunction: function | string,
  arg?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<JSHandle>
```

Executes JavaScript and returns a `JSHandle` with the result (not serialized).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | yes | — | Code to execute |
| `arg` | `EvaluationArgument` | no | — | Argument |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<JSHandle>`

```typescript
const handle = await page.locator('canvas').evaluateHandle(el => el.getContext('2d'));
```

---

## fill()

```typescript
fill(value: string, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  timeout?: number;
}): Promise<void>
```

Sets the value of an `<input>`, `<textarea>` or `contenteditable` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `value` | `string` | yes | — | Value to insert |
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('Email').fill('user@example.com');
```

---

## filter()

```typescript
filter(options?: {
  has?: Locator;
  hasNot?: Locator;
  hasNotText?: string | RegExp;
  hasText?: string | RegExp;
  visible?: boolean;
}): Locator
```

Filters the matching elements by additional criteria. Returns a new locator.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.has` | `Locator` | no | — | Keep only elements that contain this locator |
| `options.hasNot` | `Locator` | no | — | Exclude elements that contain this locator |
| `options.hasNotText` | `string \| RegExp` | no | — | Exclude elements that contain this text |
| `options.hasText` | `string \| RegExp` | no | — | Keep only elements that contain this text |
| `options.visible` | `boolean` | no | — | Filter by visibility |

**Returns:** `Locator`

```typescript
const items = page.getByRole('listitem').filter({ hasText: 'Active' });
const enabled = page.getByRole('row').filter({ hasNot: page.locator('[disabled]') });
```

---

## first()

```typescript
first(): Locator
```

Returns a locator pointing at the first matching element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Locator`

```typescript
await page.getByRole('button').first().click();
```

---

## focus()

```typescript
focus(options?: { timeout?: number }): Promise<void>
```

Calls `focus()` on the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('textbox').focus();
```

---

## frameLocator()

```typescript
frameLocator(selector: string): FrameLocator
```

Returns a `FrameLocator` for an iframe element inside this locator.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | CSS/Playwright selector for the iframe |

**Returns:** `FrameLocator`

```typescript
const frame = page.locator('.widget').frameLocator('iframe');
await frame.getByRole('button').click();
```

---

## getAttribute()

```typescript
getAttribute(name: string, options?: { timeout?: number }): Promise<null | string>
```

Returns the value of an attribute, or `null` if the attribute does not exist.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | Attribute name |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<null | string>`

```typescript
const href = await page.getByRole('link').getAttribute('href');
```

---

## getByAltText()

```typescript
getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements by their `alt` text (typical for images).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Alt text to search for |
| `options.exact` | `boolean` | no | `false` | Exact comparison (case-sensitive + full string) |

**Returns:** `Locator`

```typescript
await page.getByAltText('Company logo').click();
```

---

## getByLabel()

```typescript
getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds form elements by their label text, `aria-label` or `aria-labelledby`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Label text to search for |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.getByLabel('Password').fill('secret');
```

---

## getByPlaceholder()

```typescript
getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds `<input>` elements by their `placeholder` text.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Placeholder text |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.getByPlaceholder('Search...').fill('Playwright');
```

---

## getByRole()

```typescript
getByRole(role: AriaRole, options?: {
  checked?: boolean;
  description?: string | RegExp;
  disabled?: boolean;
  exact?: boolean;
  expanded?: boolean;
  includeHidden?: boolean;
  level?: number;
  name?: string | RegExp;
  pressed?: boolean;
  selected?: boolean;
}): Locator
```

Finds elements by their ARIA role and optional ARIA attributes.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `role` | `AriaRole` | yes | — | ARIA role, e.g. `'button'`, `'link'`, `'heading'` |
| `options.checked` | `boolean` | no | — | Filters by `aria-checked` or the native `checked` state |
| `options.description` | `string \| RegExp` | no | — | Filters by accessible description |
| `options.disabled` | `boolean` | no | — | Filters by `aria-disabled` or native `disabled` |
| `options.exact` | `boolean` | no | `false` | Exact comparison for `name` and `description` |
| `options.expanded` | `boolean` | no | — | Filters by `aria-expanded` |
| `options.includeHidden` | `boolean` | no | `false` | Include hidden elements |
| `options.level` | `number` | no | — | Filters by `aria-level` (for headings) |
| `options.name` | `string \| RegExp` | no | — | Filters by accessible name |
| `options.pressed` | `boolean` | no | — | Filters by `aria-pressed` |
| `options.selected` | `boolean` | no | — | Filters by `aria-selected` |

**Returns:** `Locator`
```typescript
await page.getByRole('button', { name: 'Sign in' }).click();
await page.getByRole('heading', { level: 2 }).first().click();
```

---

## getByTestId()

```typescript
getByTestId(testId: string | RegExp): Locator
```

Finds elements by their test ID attribute (default: `data-testid`; configurable via `selectors.setTestIdAttribute`).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `testId` | `string \| RegExp` | yes | — | Value of the test ID attribute |

**Returns:** `Locator`

```typescript
await page.getByTestId('submit-button').click();
```

---

## getByText()

```typescript
getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements that contain the given text (whitespace is normalized).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Text to search for |
| `options.exact` | `boolean` | no | `false` | Exact comparison (case-sensitive + full string) |

**Returns:** `Locator`

```typescript
await page.getByText('Order confirmation').click();
await page.getByText(/Welcome/i).waitFor();
```

---

## getByTitle()

```typescript
getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements by their `title` attribute.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Title text |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.getByTitle('Edit profile').click();
```

---

## hideHighlight()

```typescript
hideHighlight(): Promise<void>
```

Hides the element highlight created with `highlight()`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<void>`

```typescript
await page.locator('.box').hideHighlight();
```

---

## highlight()

```typescript
highlight(options?: {
  style?: string | Record<string, string | number>;
}): Promise<Disposable>
```

Highlights the element on screen. Returns a `Disposable`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.style` | `string \| Record<string, string \| number>` | no | default overlay | CSS styles for the highlight overlay |

**Returns:** `Promise<Disposable>`

```typescript
const highlight = await page.locator('button').highlight();
// ... screenshot ...
await highlight[Symbol.dispose]?.();
```

---

## hover()

```typescript
hover(options?: {
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Moves the mouse over the element (hover).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.modifiers` | `Array<string>` | no | `[]` | Modifier keys |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Hover position |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('menuitem', { name: 'File' }).hover();
```

---

## innerHTML()

```typescript
innerHTML(options?: { timeout?: number }): Promise<string>
```

Returns the `innerHTML` value of the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<string>`

```typescript
const html = await page.locator('.content').innerHTML();
```

---

## innerText()

```typescript
innerText(options?: { timeout?: number }): Promise<string>
```

Returns the `innerText` value of the element (visible text, taking CSS rendering into account).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<string>`

```typescript
const text = await page.locator('h1').innerText();
```

---

## inputValue()

```typescript
inputValue(options?: { timeout?: number }): Promise<string>
```

Returns the current value of an `<input>`, `<textarea>` or `<select>` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<string>`

```typescript
const val = await page.getByLabel('Name').inputValue();
```

---

## isChecked()

```typescript
isChecked(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the checkbox or radio element is checked.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
if (await page.getByLabel('Privacy policy').isChecked()) { /* ... */ }
```

---

## isDisabled()

```typescript
isDisabled(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the element is disabled.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
const disabled = await page.getByRole('button').isDisabled();
```

---

## isEditable()

```typescript
isEditable(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the element is editable.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
const editable = await page.getByRole('textbox').isEditable();
```

---

## isEnabled()

```typescript
isEnabled(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the element is enabled (not disabled).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
const enabled = await page.getByRole('button').isEnabled();
```

---

## isHidden()

```typescript
isHidden(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the element is hidden or not visible. A timeout of `0` means no waiting.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
if (await page.locator('.spinner').isHidden()) { /* ... */ }
```

---

## isVisible()

```typescript
isVisible(options?: { timeout?: number }): Promise<boolean>
```

Returns whether the element is visible. A timeout of `0` means no waiting.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `0` | Maximum wait time in ms |

**Returns:** `Promise<boolean>`

```typescript
if (await page.locator('.modal').isVisible()) { /* ... */ }
```

---

## last()

```typescript
last(): Locator
```

Returns a locator pointing at the last matching element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Locator`

```typescript
await page.getByRole('row').last().click();
```

---

## locator()

```typescript
locator(selectorOrLocator: string | Locator, options?: {
  has?: Locator;
  hasNot?: Locator;
  hasNotText?: string | RegExp;
  hasText?: string | RegExp;
}): Locator
```

Creates a child locator — searches within the current locator.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selectorOrLocator` | `string \| Locator` | yes | — | CSS/Playwright selector or another locator |
| `options.has` | `Locator` | no | — | Keep only elements that contain this locator |
| `options.hasNot` | `Locator` | no | — | Exclude elements that contain this locator |
| `options.hasNotText` | `string \| RegExp` | no | — | Exclude by text |
| `options.hasText` | `string \| RegExp` | no | — | Keep by text |

**Returns:** `Locator`

```typescript
const row = page.locator('tr').filter({ hasText: 'Max' });
const cell = row.locator('td:nth-child(2)');
```

---

## nth()

```typescript
nth(index: number): Locator
```

Returns the locator for the nth (zero-based) matching element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `index` | `number` | yes | — | Zero-based index |

**Returns:** `Locator`

```typescript
await page.getByRole('button').nth(2).click(); // third button
```

---

## or()

```typescript
or(locator: Locator): Locator
or(locator: Locator): Locator
```

Creates a locator that matches elements of either locator (logical OR).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `locator` | `Locator` | yes | — | Alternative locator |

**Returns:** `Locator`

```typescript
const el = page.getByRole('button').or(page.getByRole('link'));
```

---

## press()

```typescript
press(key: string, options?: {
  delay?: number;
  timeout?: number;
}): Promise<void>
```

Presses a key on the element (the element must be focused).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `string` | yes | — | Key, e.g. `'Enter'`, `'Tab'`, `'ArrowDown'`, `'Control+A'` |
| `options.delay` | `number` | no | `0` | Delay between keydown and keyup in ms |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('textbox').press('Enter');
await page.locator('#editor').press('Control+A');
```

---

## pressSequentially()

```typescript
pressSequentially(text: string, options?: {
  delay?: number;
  timeout?: number;
}): Promise<void>
```

Types text character by character with an optional delay (simulates human input).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string` | yes | — | Text to type |
| `options.delay` | `number` | no | `0` | Delay between key presses in ms |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('textbox').pressSequentially('Hello', { delay: 50 });
```

---

## screenshot()

```typescript
screenshot(options?: {
  animations?: 'disabled' | 'allow';
  mask?: Array<Locator>;
  maskColor?: string;
  omitBackground?: boolean;
  path?: string;
  quality?: number;
  scale?: 'css' | 'device';
  timeout?: number;
  type?: 'png' | 'jpeg';
}): Promise<Buffer>
```

Takes a screenshot of the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.animations` | `'disabled' \| 'allow'` | no | `'disabled'` | How to handle CSS animations |
| `options.mask` | `Array<Locator>` | no | `[]` | Elements to be masked (obscured) |
| `options.maskColor` | `string` | no | `'#FF00FF'` | Color used for masking |
| `options.omitBackground` | `boolean` | no | `false` | Omit the background (transparent PNG) |
| `options.path` | `string` | no | — | Save path |
| `options.quality` | `number` | no | — | JPEG quality 0-100 |
| `options.scale` | `'css' \| 'device'` | no | `'device'` | CSS pixels or device units |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.type` | `'png' \| 'jpeg'` | no | `'png'` | Image format |

**Returns:** `Promise<Buffer>`

```typescript
const buf = await page.locator('.chart').screenshot({ path: 'chart.png' });
```

---

## scrollIntoViewIfNeeded()

```typescript
scrollIntoViewIfNeeded(options?: { timeout?: number }): Promise<void>
```

Scrolls the element into the visible area if necessary.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.locator('#footer').scrollIntoViewIfNeeded();
```

---

## selectOption()

```typescript
selectOption(
  values: string | string[] | { value?: string; label?: string; index?: number } | Array<{ value?: string; label?: string; index?: number }>,
  options?: {
    force?: boolean;
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<string[]>
```

Selects options in a `<select>` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `values` | `string \| string[] \| SelectOption \| SelectOption[]` | yes | — | Values/labels/indices to select |
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<string[]>` — the selected option values

```typescript
await page.getByLabel('Country').selectOption('DE');
await page.getByLabel('Colors').selectOption(['red', 'blue']);
```

---

## selectText()

```typescript
selectText(options?: {
  force?: boolean;
  timeout?: number;
}): Promise<void>
```

Selects the entire text content of an input or textarea element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('textbox').selectText();
```

---

## setChecked()

```typescript
setChecked(checked: boolean, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Explicitly sets the checked state of a checkbox or radio element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `checked` | `boolean` | yes | — | `true` = checked, `false` = unchecked |
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Click position |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('Newsletter').setChecked(true);
```

---

## setInputFiles()

```typescript
setInputFiles(
  files: string | Array<string> | { name: string; mimeType: string; buffer: Buffer } | Array<{ name: string; mimeType: string; buffer: Buffer }>,
  options?: {
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Sets files for an `<input type="file">` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `files` | `string \| string[] \| FilePayload \| FilePayload[]` | yes | — | File paths or buffer objects with `name`, `mimeType`, `buffer` |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('Upload file').setInputFiles('path/to/file.pdf');
```

---

## tap()

```typescript
tap(options?: {
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Performs a touch tap gesture on the element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.modifiers` | `Array<string>` | no | `[]` | Modifier keys |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Tap position |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.getByRole('button').tap();
```

---

## textContent()

```typescript
textContent(options?: { timeout?: number }): Promise<string | null>
```

Returns the `textContent` value of the element (including invisible children).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<string | null>`

```typescript
const raw = await page.locator('script').textContent();
```

---

## uncheck()

```typescript
uncheck(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Ensures that a checkbox or radio element is not checked.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.force` | `boolean` | no | `false` | Bypass actionability |
| `options.noWaitAfter` | `boolean` | no | — | Deprecated, has no effect |
| `options.position` | `{ x: number; y: number }` | no | center | Click position |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |
| `options.trial` | `boolean` | no | `false` | Only check actionability |

**Returns:** `Promise<void>`

```typescript
await page.getByLabel('Select all').uncheck();
```

---

## waitFor()

```typescript
waitFor(options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden';
  timeout?: number;
}): Promise<void>
```

Waits until the element has reached the desired state.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.state` | `'attached' \| 'detached' \| 'visible' \| 'hidden'` | no | `'visible'` | Desired DOM/visibility state |
| `options.timeout` | `number` | no | global default | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await page.locator('.toast').waitFor({ state: 'visible' });
await page.locator('.spinner').waitFor({ state: 'hidden' });
```

---

## Method Overview (57 methods)

| Category | Methods |
|---|---|
| Iteration/composition | `all`, `and`, `or`, `filter`, `first`, `last`, `nth`, `count` |
| Factory methods (getBy*) | `getByAltText`, `getByLabel`, `getByPlaceholder`, `getByRole`, `getByTestId`, `getByText`, `getByTitle` |
| Child locators | `locator`, `frameLocator`, `contentFrame` |
| Reading (no action) | `allInnerTexts`, `allTextContents`, `getAttribute`, `innerHTML`, `innerText`, `inputValue`, `textContent`, `boundingBox` |
| State checks | `isChecked`, `isDisabled`, `isEditable`, `isEnabled`, `isHidden`, `isVisible` |
| Actions | `check`, `uncheck`, `setChecked`, `click`, `dblclick`, `tap`, `hover`, `fill`, `clear`, `press`, `pressSequentially`, `selectOption`, `selectText`, `setInputFiles`, `focus`, `blur`, `dragTo`, `drop`, `scrollIntoViewIfNeeded` |
| Screenshot/snapshot | `screenshot`, `ariaSnapshot` |
| Eval | `evaluate`, `evaluateAll`, `evaluateHandle`, `dispatchEvent` |
| Waiting | `waitFor` |
| Debugging | `describe`, `description`, `highlight`, `hideHighlight` |

---

Source: https://playwright.dev/docs/api/class-locator
