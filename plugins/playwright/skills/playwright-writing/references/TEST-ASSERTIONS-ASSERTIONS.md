# Playwright Assertions — Complete Reference

## Contents

- [Basic principle](#basic-principle)
- [Locator assertions (auto-retrying)](#locator-assertions-auto-retrying)
- [Page assertions (auto-retrying)](#page-assertions-auto-retrying)
- [APIResponse assertions (auto-retrying)](#apiresponse-assertions-auto-retrying)
- [Generic assertions (NOT auto-retrying)](#generic-assertions-not-auto-retrying)
- [Snapshot assertions](#snapshot-assertions)
- [Negation](#negation)
- [Soft Assertions](#soft-assertions)
- [Custom error message](#custom-error-message)
- [`expect.configure()`](#expectconfigure)
- [`expect.poll()`](#expectpoll)
- [`expect.toPass()`](#expecttopass)
- [Asymmetric matchers](#asymmetric-matchers)
- [`expect.extend()` — Custom matchers](#expectextend--custom-matchers)

## Basic principle

```typescript
import { test, expect } from '@playwright/test';

test('example', async ({ page }) => {
  await page.goto('/');

  // Auto-retrying: waits until the condition is met or timeout
  await expect(page.getByRole('heading')).toBeVisible();

  // Generic (not retrying): immediate evaluation
  expect(42).toBe(42);
});
```

**Default timeout for assertions:** 5000 ms (configurable via `expect.timeout` in the config).

---

## Locator assertions (auto-retrying)

All locator assertions repeat the check until the condition is met or the timeout expires.

| Assertion | Parameter | Description |
|---|---|---|
| `toBeAttached(options?)` | `options?: { attached?: boolean, timeout?: number }` | Element is attached to the DOM |
| `toBeChecked(options?)` | `options?: { checked?: boolean, timeout?: number }` | Checkbox/radio is checked |
| `toBeDisabled(options?)` | `options?: { timeout?: number }` | Element is disabled |
| `toBeEditable(options?)` | `options?: { editable?: boolean, timeout?: number }` | Element is editable |
| `toBeEmpty(options?)` | `options?: { timeout?: number }` | Container is empty (no text/children) |
| `toBeEnabled(options?)` | `options?: { timeout?: number }` | Element is enabled |
| `toBeFocused(options?)` | `options?: { timeout?: number }` | Element has focus |
| `toBeHidden(options?)` | `options?: { timeout?: number }` | Element is not visible |
| `toBeInViewport(options?)` | `options?: { ratio?: number, timeout?: number }` | Element intersects the viewport |
| `toBeVisible(options?)` | `options?: { visible?: boolean, timeout?: number }` | Element is visible |
| `toContainText(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { ignoreCase?, normalizeWhitespace?, useInnerText?, timeout? }` | Element contains text |
| `toContainClass(expected, options?)` | `expected: string \| string[]`, `options?: { timeout? }` | Element has (at least) these CSS classes |
| `toHaveAccessibleDescription(description?, options?)` | `description?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | Associated ARIA description value |
| `toHaveAccessibleName(name?, options?)` | `name?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | Associated ARIA name |
| `toHaveAttribute(name, value?, options?)` | `name: string`, `value?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | HTML attribute (and value) present |
| `toHaveClass(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { timeout? }` | CSS class property |
| `toHaveCount(count, options?)` | `count: number`, `options?: { timeout? }` | Locator list has exactly N entries |
| `toHaveCSS(name, value, options?)` | `name: string`, `value: string \| RegExp`, `options?: { timeout? }` | CSS property has value |
| `toHaveId(id, options?)` | `id: string \| RegExp`, `options?: { timeout? }` | Element has ID |
| `toHaveJSProperty(name, value, options?)` | `name: string`, `value: any`, `options?: { timeout? }` | JS property has value |
| `toHaveRole(role, options?)` | `role: AriaRole`, `options?: { timeout? }` | Element has ARIA role |
| `toHaveScreenshot(name?, options?)` | See snapshot section | Screenshot comparison |
| `toHaveText(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { ignoreCase?, normalizeWhitespace?, useInnerText?, timeout? }` | Exact text match |
| `toHaveValue(value, options?)` | `value: string \| RegExp`, `options?: { timeout? }` | Input value |
| `toHaveValues(values, options?)` | `values: (string \| RegExp)[]`, `options?: { timeout? }` | Select multi-selection |
| `toMatchAriaSnapshot(expected?, options?)` | `expected?: string`, `options?: { timeout? }` | ARIA snapshot comparison |

### Examples

```typescript
// Text
await expect(page.getByRole('heading')).toHaveText('Welcome');
await expect(page.locator('.status')).toContainText(/error/i);

// Form
await expect(page.getByRole('checkbox')).toBeChecked();
await expect(page.getByRole('textbox')).toHaveValue('John');
await expect(page.getByRole('combobox')).toHaveValues(['option1', 'option2']);

// Attributes
await expect(page.getByRole('img')).toHaveAttribute('alt', 'Logo');
await expect(page.getByRole('button')).toBeEnabled();

// List
await expect(page.getByRole('listitem')).toHaveCount(3);

// CSS
await expect(page.locator('.box')).toHaveCSS('color', 'rgb(0, 0, 0)');

// Visibility
await expect(page.getByText('Error')).toBeHidden();
await expect(page.getByText('Success')).toBeVisible();
```

---

## Page assertions (auto-retrying)

| Assertion | Parameter | Description |
|---|---|---|
| `toHaveTitle(title, options?)` | `title: string \| RegExp`, `options?: { timeout? }` | Page title |
| `toHaveURL(url, options?)` | `url: string \| RegExp`, `options?: { timeout? }` | Current URL |
| `toHaveScreenshot(name?, options?)` | See snapshot section | Page screenshot |
| `toMatchAriaSnapshot(expected?, options?)` | `expected?: string`, `options?: { timeout? }` | ARIA snapshot |

```typescript
await expect(page).toHaveTitle(/Playwright/);
await expect(page).toHaveURL('https://example.com/dashboard');
```

---

## APIResponse assertions (auto-retrying)

| Assertion | Parameter | Description |
|---|---|---|
| `toBeOK(options?)` | `options?: { timeout? }` | Status is 2xx |

```typescript
const response = await page.request.get('/api/users');
await expect(response).toBeOK();
```

---

## Generic assertions (NOT auto-retrying)

Immediate evaluation — not suitable for asynchronous scenarios.

| Assertion | Parameter | Description |
|---|---|---|
| `toBe(value)` | `value: any` | Reference equality (`===`) |
| `toBeCloseTo(value, digits?)` | `value: number`, `digits?: number` | Approximate equality |
| `toBeDefined()` | — | Value is not `undefined` |
| `toBeFalsy()` | — | Falsy (false, 0, '', null, undefined, NaN) |
| `toBeGreaterThan(value)` | `value: number \| bigint` | Greater than |
| `toBeGreaterThanOrEqual(value)` | `value: number \| bigint` | Greater than or equal |
| `toBeInstanceOf(cls)` | `cls: Function` | Instance of a class |
| `toBeLessThan(value)` | `value: number \| bigint` | Less than |
| `toBeLessThanOrEqual(value)` | `value: number \| bigint` | Less than or equal |
| `toBeNaN()` | — | Value is NaN |
| `toBeNull()` | — | Value is null |
| `toBeTruthy()` | — | Truthy |
| `toBeUndefined()` | — | Value is undefined |
| `toContain(value)` | `value: string \| any` | String/array/set contains element |
| `toContainEqual(value)` | `value: any` | Array/set contains a similar element |
| `toEqual(value)` | `value: any` | Deep equality |
| `toHaveLength(length)` | `length: number` | Array/string length |
| `toHaveProperty(path, value?)` | `path: string \| string[]`, `value?: any` | Object property |
| `toMatch(regexp)` | `regexp: RegExp \| string` | String matches regex |
| `toMatchObject(object)` | `object: object` | Object contains subset |
| `toStrictEqual(value)` | `value: any` | Strict equality including types |
| `toThrow(error?)` | `error?: string \| RegExp \| Error \| Function` | Function throws an error |

```typescript
expect(result).toEqual({ id: 1, name: 'Alice' });
expect(items).toHaveLength(3);
expect(fn).toThrow(/invalid/);
expect(value).toBeGreaterThan(0);
```

---

## Snapshot assertions

### `toHaveScreenshot()`

```typescript
// Page
await expect(page).toHaveScreenshot('landing.png');
await expect(page).toHaveScreenshot(['subdir', 'landing.png']);

// Element
await expect(page.getByRole('main')).toHaveScreenshot('main-content.png');
```

**Options:**

| Option | Type | Default | Description |
|---|---|---|---|
| `name` | `string \| string[]` | auto | Snapshot file name (segment array = subdirectory) |
| `maxDiffPixels` | `number` | — | Max. differing pixels |
| `maxDiffPixelRatio` | `number` | — | Max. ratio of differing pixels (0-1) |
| `threshold` | `number` | `0.2` | Pixelmatch threshold (0-1) |
| `animations` | `'disabled' \| 'allow'` | `'disabled'` | CSS animations |
| `caret` | `'hide' \| 'initial'` | `'hide'` | Text cursor |
| `scale` | `'css' \| 'device'` | `'css'` | Scaling mode |
| `stylePath` | `string \| string[]` | — | CSS for overlaying volatile elements |
| `timeout` | `number` | (expect timeout) | Max. wait time |
| `clip` | `{ x, y, width, height }` | — | Crop region |
| `mask` | `Locator[]` | — | Mask regions |
| `maskColor` | `string` | `'#FF00FF'` | Color for masks |
| `fullPage` | `boolean` | `false` | Full-page screenshot |
| `omitBackground` | `boolean` | `false` | Transparent background |

**Naming:** `{testName}-{browser}-{platform}.png`
**Directory:** `{testfile}-snapshots/`

**Global configuration:**

```typescript
expect: {
  toHaveScreenshot: {
    maxDiffPixels: 100,
    stylePath: './screenshot.css',
  },
}
```

### `toMatchSnapshot()`

For text and binary data:

```typescript
expect(await page.textContent('.hero')).toMatchSnapshot('hero.txt');
expect(buffer).toMatchSnapshot('data.bin');
```

**Options:**

| Option | Type | Description |
|---|---|---|
| `name` | `string \| string[]` | Snapshot file name |
| `maxDiffPixels` | `number` | Max. pixel differences (images) |
| `maxDiffPixelRatio` | `number` | Max. ratio (images) |
| `threshold` | `number` | Threshold (images) |

**Updating snapshots:**

```bash
npx playwright test --update-snapshots
npx playwright test --update-snapshots=changed   # only changed ones
npx playwright test --update-snapshots=missing   # only missing ones (default)
```

---

## Negation

```typescript
await expect(page.getByText('Error')).not.toBeVisible();
expect(value).not.toEqual(0);
```

---

## Soft Assertions

Failed assertions do NOT abort the test; the test is marked as failed at the end.

```typescript
// Individually
await expect.soft(page.getByTestId('status')).toHaveText('Success');
await expect.soft(page.getByTestId('count')).toHaveText('3');

// With a custom message
expect.soft(value, 'should be positive').toBeGreaterThan(0);

// Check errors manually
expect(test.info().errors).toHaveLength(0);
```

---

## Custom error message

```typescript
await expect(
  page.getByRole('button'),
  'Submit-Button sollte sichtbar sein'
).toBeVisible();
```

---

## `expect.configure()`

Pre-configured expect instance:

```typescript
const slowExpect = expect.configure({ timeout: 30_000 });
const softExpect = expect.configure({ soft: true });

await slowExpect(locator).toBeVisible();
await softExpect(locator).toHaveText('hello');
```

Parameters: `timeout: number`, `soft: boolean`

---

## `expect.poll()`

Poll a synchronous expect function asynchronously:

```typescript
await expect.poll(async () => {
  const response = await page.request.get('/api/status');
  return response.status();
}, {
  message: 'API sollte 200 zurueckgeben',
  timeout: 10_000,
  intervals: [100, 250, 500, 1000],   // ms between attempts
}).toBe(200);
```

Combinable with soft: `expect.configure({ soft: true }).poll(fn).toBe(x)`

---

## `expect.toPass()`

Repeat a code block until it succeeds:

```typescript
await expect(async () => {
  const response = await page.request.get('/api/data');
  expect(response.status()).toBe(200);
  expect(await response.json()).toHaveProperty('items');
}).toPass({
  intervals: [100, 250, 500, 1000],
  timeout: 10_000,                    // Default: 0 (no timeout)
});
```

---

## Asymmetric matchers

Inside other assertions for flexible checks:

| Matcher | Description |
|---|---|
| `expect.any(Class)` | Any instance of the class/primitive |
| `expect.anything()` | Any value (not null/undefined) |
| `expect.arrayContaining([...])` | Array contains all listed elements |
| `expect.arrayOf(type)` | Array of elements of the type |
| `expect.closeTo(num, digits?)` | Approximate number |
| `expect.objectContaining({...})` | Object contains certain properties |
| `expect.stringContaining(str)` | String contains substring |
| `expect.stringMatching(re)` | String matches regex |

```typescript
expect(obj).toEqual({
  id: expect.any(Number),
  name: expect.stringMatching(/^Alice/),
  tags: expect.arrayContaining(['admin']),
});
```

---

## `expect.extend()` — Custom matchers

```typescript
import { expect as baseExpect } from '@playwright/test';
import type { Locator } from '@playwright/test';

export const expect = baseExpect.extend({
  async toHaveAmount(locator: Locator, expected: number, options?: { timeout?: number }) {
    const assertionName = 'toHaveAmount';
    let pass: boolean;
    let matcherResult: any;

    try {
      await baseExpect(locator).toHaveText(
        String(expected),
        { timeout: options?.timeout ?? 1000 }
      );
      pass = true;
    } catch (e: any) {
      matcherResult = e.matcherResult;
      pass = false;
    }

    const message = pass
      ? () => `${this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot })}\n\nExpected: not ${expected}`
      : () => `${this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot })}\n\nExpected: ${expected}\nReceived: ${matcherResult?.actual}`;

    return { message, pass, name: assertionName, expected, actual: matcherResult?.actual };
  },
});
```

Merging several custom expects:

```typescript
import { mergeExpects } from '@playwright/test';
export const expect = mergeExpects(dbExpect, a11yExpect);
```

---

Source: https://playwright.dev/docs/test-assertions | https://playwright.dev/docs/test-snapshots
