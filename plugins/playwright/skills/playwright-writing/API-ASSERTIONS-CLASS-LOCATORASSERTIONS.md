# class-locatorassertions — Playwright API Reference

`LocatorAssertions` is the assertion class for `Locator` objects. All matchers retry automatically until the test succeeds or the timeout is reached. Default timeout: value from `TestConfig.expect` (default 5000 ms).

Accessed via `expect(locator).*`.

Matcher count: 29 matchers + property `not`

---

## Contents

- [Overview: timeout pattern](#overview-timeout-pattern)
- [not](#not)
- [toBeAttached()](#tobeattached)
- [toBeChecked()](#tobechecked)
- [toBeDisabled()](#tobedisabled)
- [toBeEditable()](#tobeeditable)
- [toBeEmpty()](#tobeempty)
- [toBeEnabled()](#tobeenabled)
- [toBeFocused()](#tobefocused)
- [toBeHidden()](#tobehidden)
- [toBeInViewport()](#tobeinviewport)
- [toBeVisible()](#tobevisible)
- [toContainClass()](#tocontainclass)
- [toContainText()](#tocontaintext)
- [toHaveAccessibleDescription()](#tohaveaccessibledescription)
- [toHaveAccessibleErrorMessage()](#tohaveaccessibleerrormessage)
- [toHaveAccessibleName()](#tohaveaccessiblename)
- [toHaveAttribute() — with value](#tohaveattribute-with-value)
- [toHaveAttribute() — existence only](#tohaveattribute-existence-only)
- [toHaveClass()](#tohaveclass)
- [toHaveCount()](#tohavecount)
- [toHaveCSS()](#tohavecss)
- [toHaveId()](#tohaveid)
- [toHaveJSProperty()](#tohavejsproperty)
- [toHaveRole()](#tohaverole)
- [toHaveScreenshot() — with name](#tohavescreenshot-with-name)
- [toHaveScreenshot() — automatic](#tohavescreenshot-automatic)
- [toHaveText()](#tohavetext)
- [toHaveValue()](#tohavevalue)
- [toHaveValues()](#tohavevalues)
- [toMatchAriaSnapshot() — inline](#tomatchariasnapshot-inline)
- [toMatchAriaSnapshot() — stored](#tomatchariasnapshot-stored)
- [Matcher overview (29 matchers)](#matcher-overview-29-matchers)

## Overview: timeout pattern

Every matcher optionally accepts `{ timeout?: number }` as the last options object. The timeout value overrides `TestConfig.expect.timeout` for this single call.

```typescript
await expect(locator).toBeVisible({ timeout: 10_000 });
```

---

## not

```typescript
not: LocatorAssertions
```

Inverts the assertion — checks the opposite of the following assertion.

```typescript
await expect(page.locator('.error')).not.toBeVisible();
await expect(page.getByRole('button')).not.toBeDisabled();
```

---

## toBeAttached()

```typescript
toBeAttached(options?: {
  attached?: boolean;
  timeout?: number;
}): Promise<void>
```

Checks whether the element is connected to the DOM (attached to a `Document` or `ShadowRoot`).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.attached` | `boolean` | no | `true` | `true` = must be attached; `false` = must not be attached |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('#modal')).toBeAttached();
await expect(page.locator('#removed')).toBeAttached({ attached: false });
```

---

## toBeChecked()

```typescript
toBeChecked(options?: {
  checked?: boolean;
  indeterminate?: boolean;
  timeout?: number;
}): Promise<void>
```

Checks the checked state of a checkbox, a radio button or an `aria-checked` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.checked` | `boolean` | no | `true` | Expected state |
| `options.indeterminate` | `boolean` | no | `false` | Checks for the indeterminate state (`indeterminate`) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('AGB akzeptieren')).toBeChecked();
await expect(page.getByLabel('Option')).toBeChecked({ checked: false });
```

---

## toBeDisabled()

```typescript
toBeDisabled(options?: { timeout?: number }): Promise<void>
```

Checks whether the element is disabled (via the `disabled` attribute or `aria-disabled`).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('button', { name: 'Senden' })).toBeDisabled();
```

---

## toBeEditable()

```typescript
toBeEditable(options?: {
  editable?: boolean;
  timeout?: number;
}): Promise<void>
```

Checks whether the element is editable.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.editable` | `boolean` | no | `true` | Expected state |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('Kommentar')).toBeEditable();
await expect(page.getByLabel('Readonly')).toBeEditable({ editable: false });
```

---

## toBeEmpty()

```typescript
toBeEmpty(options?: { timeout?: number }): Promise<void>
```

Checks whether an editable element or DOM node contains no text.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('textbox')).toBeEmpty();
```

---

## toBeEnabled()

```typescript
toBeEnabled(options?: {
  enabled?: boolean;
  timeout?: number;
}): Promise<void>
```

Checks whether the element is enabled (not disabled).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.enabled` | `boolean` | no | `true` | Expected state |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('button', { name: 'Submit' })).toBeEnabled();
```

---

## toBeFocused()

```typescript
toBeFocused(options?: { timeout?: number }): Promise<void>
```

Checks whether the element has keyboard focus.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('Suche')).toBeFocused();
```

---

## toBeHidden()

```typescript
toBeHidden(options?: { timeout?: number }): Promise<void>
```

Checks whether the element is hidden or not visible.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.loading-spinner')).toBeHidden();
```

---

## toBeInViewport()

```typescript
toBeInViewport(options?: {
  ratio?: number;
  timeout?: number;
}): Promise<void>
```

Checks whether the element intersects the viewport (Intersection Observer API).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.ratio` | `number` | no | 0 | Minimum proportion of the element inside the viewport (0-1) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('#cta')).toBeInViewport();
await expect(page.locator('#hero')).toBeInViewport({ ratio: 0.5 });
```

---

## toBeVisible()

```typescript
toBeVisible(options?: {
  timeout?: number;
  visible?: boolean;
}): Promise<void>
```

Checks whether the element is attached to the DOM and visible.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |
| `options.visible` | `boolean` | no | `true` | `false` is equivalent to `.not.toBeVisible()` |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.toast')).toBeVisible();
await expect(page.locator('#overlay')).toBeVisible({ visible: false });
```

---

## toContainClass()

```typescript
toContainClass(
  expected: string | string[],
  options?: { timeout?: number }
): Promise<void>
```

Checks whether the element contains the given CSS classes (not necessarily all of them).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| string[]` | yes | — | Expected class(es); space-separated or as an array |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.btn')).toContainClass('active');
await expect(page.locator('.item')).toContainClass(['selected', 'highlighted']);
```

---

## toContainText()

```typescript
toContainText(
  expected: string | RegExp | Array<string | RegExp>,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
    useInnerText?: boolean;
  }
): Promise<void>
```

Checks whether the element contains the given text (substring or regex match).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | yes | — | Expected text; with an array the elements are checked sequentially |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |
| `options.useInnerText` | `boolean` | no | `false` | Use `innerText` instead of `textContent` |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.message')).toContainText('Erfolg');
await expect(page.locator('.list')).toContainText(['Eintrag 1', 'Eintrag 2']);
```

---

## toHaveAccessibleDescription()

```typescript
toHaveAccessibleDescription(
  description: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Checks the element's accessible description according to the W3C specification.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `description` | `string \| RegExp` | yes | — | Expected description |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('img')).toHaveAccessibleDescription('Produktfoto');
```

---

## toHaveAccessibleErrorMessage()

```typescript
toHaveAccessibleErrorMessage(
  errorMessage: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Checks the value of the `aria-errormessage` attribute.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `errorMessage` | `string \| RegExp` | yes | — | Expected error message |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('Email')).toHaveAccessibleErrorMessage('Invalid email');
```

---

## toHaveAccessibleName()

```typescript
toHaveAccessibleName(
  name: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Checks the element's accessible name according to the W3C specification.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string \| RegExp` | yes | — | Expected name |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('button')).toHaveAccessibleName('Sign in');
```

---

## toHaveAttribute() — with value

```typescript
toHaveAttribute(
  name: string,
  value: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Checks whether the element has a certain attribute with a certain value.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | Attribute name |
| `value` | `string \| RegExp` | yes | — | Expected attribute value |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('link')).toHaveAttribute('href', '/dashboard');
await expect(page.locator('img')).toHaveAttribute('src', /\.webp$/);
```

---

## toHaveAttribute() — existence only

```typescript
toHaveAttribute(
  name: string,
  options?: { timeout?: number }
): Promise<void>
```

Checks only the existence of the attribute, regardless of its value.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | Attribute name |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('video')).toHaveAttribute('controls');
```

---

## toHaveClass()

```typescript
toHaveClass(
  expected: string | RegExp | Array<string | RegExp>,
  options?: { timeout?: number }
): Promise<void>
```

Checks the element's complete `class` property (exact match or regex).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | yes | — | Complete expected class string; with an array: one element per list entry |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
// Single element: exact class attribute comparison
await expect(page.locator('.btn')).toHaveClass('btn btn-primary');
// List of elements (array form)
await expect(page.getByRole('listitem')).toHaveClass(['active', 'inactive', 'active']);
```

---

## toHaveCount()

```typescript
toHaveCount(
  count: number,
  options?: { timeout?: number }
): Promise<void>
```

Checks whether the locator resolves to exactly the given number of DOM nodes.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `count` | `number` | yes | — | Expected number of elements |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByRole('listitem')).toHaveCount(5);
```

---

## toHaveCSS()

```typescript
toHaveCSS(
  name: string,
  value: string | RegExp,
  options?: {
    pseudo?: 'before' | 'after';
    timeout?: number;
  }
): Promise<void>
```

Checks a computed CSS property value.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | CSS property name (e.g. `'display'`, `'color'`) |
| `value` | `string \| RegExp` | yes | — | Expected value |
| `options.pseudo` | `'before' \| 'after'` | no | — | Check the pseudo element |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.badge')).toHaveCSS('display', 'flex');
await expect(page.locator('.icon')).toHaveCSS('content', '"*"', { pseudo: 'before' });
```

---

## toHaveId()

```typescript
toHaveId(
  id: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Checks the element's DOM `id` property.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `id` | `string \| RegExp` | yes | — | Expected ID value |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('input').first()).toHaveId('username');
```

---

## toHaveJSProperty()

```typescript
toHaveJSProperty(
  name: string,
  value: unknown,
  options?: { timeout?: number }
): Promise<void>
```

Checks a JavaScript property of the DOM element (not just attributes).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | Property name |
| `value` | `unknown` | yes | — | Expected value (primitive or serializable object) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('input[type=checkbox]')).toHaveJSProperty('indeterminate', true);
```

---

## toHaveRole()

```typescript
toHaveRole(
  role: AriaRole,
  options?: { timeout?: number }
): Promise<void>
```

Checks the element's ARIA role according to the W3C specification (exact string comparison).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `role` | `AriaRole` | yes | — | Expected ARIA role e.g. `'button'`, `'dialog'` |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.modal')).toHaveRole('dialog');
```

---

## toHaveScreenshot() — with name

```typescript
toHaveScreenshot(
  name: string | string[],
  options?: {
    animations?: 'disabled' | 'allow';
    caret?: 'hide' | 'initial';
    mask?: Locator[];
    maskColor?: string;
    maxDiffPixelRatio?: number;
    maxDiffPixels?: number;
    omitBackground?: boolean;
    scale?: 'css' | 'device';
    stylePath?: string | string[];
    threshold?: number;
    timeout?: number;
  }
): Promise<void>
```

Compares an element screenshot with a stored snapshot (named mode). Only available in the test runner.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string \| string[]` | yes | — | File name or path segments for the snapshot |
| `options.animations` | `'disabled' \| 'allow'` | no | `'disabled'` | How to handle CSS animations during the screenshot |
| `options.caret` | `'hide' \| 'initial'` | no | `'hide'` | Text cursor visibility |
| `options.mask` | `Locator[]` | no | `[]` | Elements to mask (magenta rectangle) |
| `options.maskColor` | `string` | no | `'#FF00FF'` | Color of the mask |
| `options.maxDiffPixelRatio` | `number` | no | from config | Maximum proportion of differing pixels (0-1) |
| `options.maxDiffPixels` | `number` | no | from config | Maximum number of differing pixels |
| `options.omitBackground` | `boolean` | no | `false` | Transparent background (PNG only) |
| `options.scale` | `'css' \| 'device'` | no | `'css'` | Pixel unit |
| `options.stylePath` | `string \| string[]` | no | — | Additional CSS files for the screenshot |
| `options.threshold` | `number` | no | `0.2` | Color difference threshold (YIQ, 0-1) |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('.chart')).toHaveScreenshot('chart-baseline.png');
await expect(page.locator('.header')).toHaveScreenshot('header.png', {
  maxDiffPixelRatio: 0.01,
  mask: [page.locator('.dynamic-date')],
});
```

---

## toHaveScreenshot() — automatic

```typescript
toHaveScreenshot(options?: {
  animations?: 'disabled' | 'allow';
  caret?: 'hide' | 'initial';
  mask?: Locator[];
  maskColor?: string;
  maxDiffPixelRatio?: number;
  maxDiffPixels?: number;
  omitBackground?: boolean;
  scale?: 'css' | 'device';
  stylePath?: string | string[];
  threshold?: number;
  timeout?: number;
}): Promise<void>
```

Same as above, but the name is generated automatically from the test name + counter.

```typescript
await expect(page.locator('.widget')).toHaveScreenshot();
```

---

## toHaveText()

```typescript
toHaveText(
  expected: string | RegExp | Array<string | RegExp>,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
    useInnerText?: boolean;
  }
): Promise<void>
```

Checks the element's complete text (whitespace-normalized for strings).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | yes | — | Expected text; with an array: one element per list entry |
| `options.ignoreCase` | `boolean` | no | `false` | Ignore case |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |
| `options.useInnerText` | `boolean` | no | `false` | Use `innerText` instead of `textContent` |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('h1')).toHaveText('Welcome');
await expect(page.getByRole('listitem')).toHaveText(['Eins', 'Zwei', 'Drei']);
```

---

## toHaveValue()

```typescript
toHaveValue(
  value: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Checks the current value of an `<input>`, `<textarea>` or `<select>` element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `value` | `string \| RegExp` | yes | — | Expected value |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('Name')).toHaveValue('John Doe');
```

---

## toHaveValues()

```typescript
toHaveValues(
  values: Array<string | RegExp>,
  options?: { timeout?: number }
): Promise<void>
```

Checks the selected values of a multi-select or combobox element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `values` | `Array<string \| RegExp>` | yes | — | Expected selected values |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.getByLabel('Sprachen')).toHaveValues(['de', 'en']);
```

---

## toMatchAriaSnapshot() — inline

```typescript
toMatchAriaSnapshot(
  expected: string,
  options?: { timeout?: number }
): Promise<void>
```

Checks whether the element matches an inline ARIA snapshot.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string` | yes | — | ARIA snapshot as a YAML string |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('nav')).toMatchAriaSnapshot(`
  - navigation:
    - link "Home"
    - link "Produkte"
`);
```

---

## toMatchAriaSnapshot() — stored

```typescript
toMatchAriaSnapshot(options?: {
  name?: string;
  timeout?: number;
}): Promise<void>
```

Compares against a stored `.aria.yml` snapshot file.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `options.name` | `string` | no | auto | File name of the stored snapshot |
| `options.timeout` | `number` | no | `TestConfig.expect` | Maximum wait time in ms |

**Returns:** `Promise<void>`

```typescript
await expect(page.locator('main')).toMatchAriaSnapshot({ name: 'main-content.aria.yml' });
```

---

## Matcher overview (29 matchers)

| Category | Matcher |
|---|---|
| Visibility / DOM state | `toBeAttached`, `toBeHidden`, `toBeVisible`, `toBeInViewport` |
| Enablement / interaction | `toBeChecked`, `toBeDisabled`, `toBeEditable`, `toBeEmpty`, `toBeEnabled`, `toBeFocused` |
| Text | `toContainText`, `toHaveText`, `toHaveValue`, `toHaveValues` |
| CSS / layout | `toContainClass`, `toHaveClass`, `toHaveCSS` |
| Attributes / properties | `toHaveAttribute`, `toHaveId`, `toHaveJSProperty`, `toHaveRole` |
| Accessibility | `toHaveAccessibleDescription`, `toHaveAccessibleErrorMessage`, `toHaveAccessibleName` |
| Count | `toHaveCount` |
| Screenshots | `toHaveScreenshot` (2 overloads) |
| ARIA snapshots | `toMatchAriaSnapshot` (2 overloads) |

---

Source: https://playwright.dev/docs/api/class-locatorassertions
