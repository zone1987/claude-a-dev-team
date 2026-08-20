# class-selectors — Playwright API Reference

The `Selectors` class allows registering custom selector engines and configuring the test ID attribute. Both methods must be called **before** creating any pages. Access via `playwright.selectors` (global Playwright instance).

Method count: 2

---

## Contents

- [register()](#register)
- [setTestIdAttribute()](#settestidattribute)
- [Method Overview](#method-overview)

## register()

```typescript
register(
  name: string,
  script: Function | string | { path?: string; content?: string },
  options?: { contentScript?: boolean }
): Promise<void>
```

Registers a custom selector engine. After registration, the selector can be used via the prefix `name=myselector` in all methods that accept selectors.

**Important:** Must be called before pages (`page`) are created.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `name` | `string` | yes | — | Unique identifier (only `[a-zA-Z0-9_]`); used as prefix `name=...` |
| `script` | `Function \| string \| { path?: string; content?: string }` | yes | — | Evaluates to a selector engine instance; executed in the page context |
| `options.contentScript` | `boolean` | no | `false` | Run the engine in an isolated JS environment (has access to the DOM, but not to frame scripts) |

**Returns:** `Promise<void>`

### Selector Engine API

The script must return an object with the following methods:

| Method | Signature | Description |
|---|---|---|
| `query` | `(root: Element, selector: string) => Element \| null` | Finds the first matching element |
| `queryAll` | `(root: Element, selector: string) => Element[]` | Finds all matching elements |

```typescript
// Custom engine: finds elements via the data-qa attribute
await playwright.selectors.register('qa', () => ({
  query(root, selector) {
    return root.querySelector(`[data-qa="${selector}"]`);
  },
  queryAll(root, selector) {
    return Array.from(root.querySelectorAll(`[data-qa="${selector}"]`));
  },
}));

// Usage
await page.locator('qa=submit-button').click();
```

Load from a file:

```typescript
await playwright.selectors.register('myengine', {
  path: './my-selector-engine.js',
});
```

---

## setTestIdAttribute()

```typescript
setTestIdAttribute(attributeName: string): void
```

Sets the HTML attribute used by `getByTestId()`. The default is `data-testid`.

**Important:** Must be called before creating any pages.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `attributeName` | `string` | yes | — | Name of the attribute interpreted as the test ID |

**Returns:** `void`

```typescript
// In playwright.config.ts or a global setup file:
import { selectors } from '@playwright/test';
selectors.setTestIdAttribute('data-cy');

// Afterwards:
await page.getByTestId('login-form').fill('...'); // looks for data-cy="login-form"
```

---

## Method Overview

| Method | Purpose |
|---|---|
| `register()` | Register a custom selector engine |
| `setTestIdAttribute()` | Configure the test ID attribute name |

---

Source: https://playwright.dev/docs/api/class-selectors
