# class-framelocator — Playwright API Reference

A `FrameLocator` represents a view onto an `iframe` element on the page. It enables interaction with elements inside the frame. All `getBy*` and `locator()` methods behave identically to their counterparts in `Locator`, but operate in the context of the addressed frame.

Method count: 11 (3 of them deprecated)

---

## Contents

- [frameLocator()](#framelocator)
- [getByAltText()](#getbyalttext)
- [getByLabel()](#getbylabel)
- [getByPlaceholder()](#getbyplaceholder)
- [getByRole()](#getbyrole)
- [getByTestId()](#getbytestid)
- [getByText()](#getbytext)
- [getByTitle()](#getbytitle)
- [locator()](#locator)
- [owner()](#owner)
- [Deprecated Methods](#deprecated-methods)
- [Method Overview](#method-overview)

## frameLocator()

```typescript
frameLocator(selector: string): FrameLocator
```

Navigates into a nested iframe within this frame.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | `string` | yes | — | CSS/Playwright selector for the nested iframe |

**Returns:** `FrameLocator`

```typescript
const outer = page.frameLocator('#outer');
const inner = outer.frameLocator('#inner');
await inner.getByRole('button').click();
```

---

## getByAltText()

```typescript
getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements in the frame by their `alt` text.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Alt text |
| `options.exact` | `boolean` | no | `false` | Exact comparison (case-sensitive + full string) |

**Returns:** `Locator`

```typescript
await page.frameLocator('#widget').getByAltText('Logo').click();
```

---

## getByLabel()

```typescript
getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds form elements in the frame by their label.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Label text |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.frameLocator('#editor').getByLabel('Title').fill('Test');
```

---

## getByPlaceholder()

```typescript
getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds `<input>` elements in the frame by their `placeholder` text.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Placeholder text |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.frameLocator('#form-frame').getByPlaceholder('Email').fill('user@test.com');
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

Finds elements in the frame by ARIA role and optional attributes.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `role` | `AriaRole` | yes | — | ARIA role, e.g. `'button'`, `'textbox'` |
| `options.checked` | `boolean` | no | — | Filters by `aria-checked` |
| `options.description` | `string \| RegExp` | no | — | Accessible description |
| `options.disabled` | `boolean` | no | — | Filters by `aria-disabled` |
| `options.exact` | `boolean` | no | `false` | Exact name/description comparison |
| `options.expanded` | `boolean` | no | — | Filters by `aria-expanded` |
| `options.includeHidden` | `boolean` | no | `false` | Include hidden elements |
| `options.level` | `number` | no | — | Filters by `aria-level` |
| `options.name` | `string \| RegExp` | no | — | Accessible name |
| `options.pressed` | `boolean` | no | — | Filters by `aria-pressed` |
| `options.selected` | `boolean` | no | — | Filters by `aria-selected` |

**Returns:** `Locator`

```typescript
await page.frameLocator('#checkout').getByRole('button', { name: 'Buy' }).click();
```

---

## getByTestId()

```typescript
getByTestId(testId: string | RegExp): Locator
```

Finds elements in the frame by their test ID attribute.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `testId` | `string \| RegExp` | yes | — | Value of the test ID attribute |

**Returns:** `Locator`

```typescript
await page.frameLocator('#app').getByTestId('confirm-btn').click();
```

---

## getByText()

```typescript
getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements in the frame that contain the given text.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Text to search for |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.frameLocator('#preview').getByText('Confirm').click();
```

---

## getByTitle()

```typescript
getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Finds elements in the frame by their `title` attribute.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | `string \| RegExp` | yes | — | Title text |
| `options.exact` | `boolean` | no | `false` | Exact comparison |

**Returns:** `Locator`

```typescript
await page.frameLocator('#map').getByTitle('Fullscreen').click();
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

Creates a locator within the frame.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `selectorOrLocator` | `string \| Locator` | yes | — | Selector or locator |
| `options.has` | `Locator` | no | — | Contains this locator |
| `options.hasNot` | `Locator` | no | — | Does not contain this locator |
| `options.hasNotText` | `string \| RegExp` | no | — | Does not contain this text |
| `options.hasText` | `string \| RegExp` | no | — | Contains this text |

**Returns:** `Locator`

```typescript
const frame = page.frameLocator('#app');
await frame.locator('.submit-btn').click();
```

---

## owner()

```typescript
owner(): Locator
```

Converts the `FrameLocator` into a `Locator` pointing at the same iframe element.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Locator`

```typescript
const frame = page.frameLocator('#app');
await expect(frame.owner()).toBeVisible();
```

---

## Deprecated Methods

These methods are deprecated. Use `locator().nth(n).contentFrame()` etc. instead.

### first() — DEPRECATED

```typescript
first(): FrameLocator
```

Returns a FrameLocator for the first matching iframe.
**Replacement:** `locator('iframe').first().contentFrame()`

### last() — DEPRECATED

```typescript
last(): FrameLocator
```

Returns a FrameLocator for the last matching iframe.
**Replacement:** `locator('iframe').last().contentFrame()`

### nth() — DEPRECATED

```typescript
nth(index: number): FrameLocator
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `index` | `number` | yes | — | Zero-based index |

Returns a FrameLocator for the nth matching iframe.
**Replacement:** `locator('iframe').nth(n).contentFrame()`

---

## Method Overview

| Category | Methods |
|---|---|
| Conversion | `owner()` |
| Nesting | `frameLocator()` |
| Factory methods (getBy*) | `getByAltText`, `getByLabel`, `getByPlaceholder`, `getByRole`, `getByTestId`, `getByText`, `getByTitle` |
| General locators | `locator()` |
| Deprecated | `first()`, `last()`, `nth()` |

---

Source: https://playwright.dev/docs/api/class-framelocator
