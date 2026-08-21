# Playwright — class: WebError

> **Manifest:** 3 methods, 0 properties, 0 events (1 external context event).
> Represents an unhandled JavaScript error (uncaught exception) in a page.
> Instances are received via `browserContext.on('weberror')`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Context event: 'weberror'](#context-event-weberror)
- [Complete example: error collection](#complete-example-error-collection)
- [Manifest](#manifest)

## Overview

`WebError` encapsulates unhandled exceptions that occur in the browser context
(i.e. errors that were not caught by `try/catch` or `window.onerror`).
This differs from `page.on('pageerror')`, which serves the same
purpose but is limited to a single page.

```javascript
// At context level
context.on('weberror', webError => {
  console.error('Uncaught exception:', webError.error());
  console.error('In page:', webError.page()?.url());
});
```

---

## Methods

### webError.error()

Returns the underlying JavaScript Error object.

**Signature:**
```typescript
webError.error(): Error
```

**Parameters:** None

**Returns:** `Error` — the JavaScript Error object with `message`, `stack`
and possibly further properties.

**Added:** v1.38

**Example:**
```javascript
context.on('weberror', webError => {
  const err = webError.error();
  console.error('Error:', err.message);
  console.error('Stack:', err.stack);
});
```

---

### webError.location()

Returns the source code location of the error.

**Signature:**
```typescript
webError.location(): {
  url: string;
  line: number;
  column: number;
}
```

**Parameters:** None

**Returns:** Object with:

| Field | Type | Description |
|------|-----|--------------|
| `url` | `string` | URL of the resource in which the error occurred |
| `line` | `number` | 0-based line number |
| `column` | `number` | 0-based column number |

**Added:** v1.60

**Example:**
```javascript
context.on('weberror', webError => {
  const loc = webError.location();
  console.error(`Error at ${loc.url}:${loc.line}:${loc.column}`);
});
```

---

### webError.page()

Returns the page in which the unhandled error occurred.

**Signature:**
```typescript
webError.page(): Page | null
```

**Parameters:** None

**Returns:** `Page | null` — the page, or `null` if the error
could not be associated with a page (e.g. in a service worker)

**Added:** v1.38

**Example:**
```javascript
context.on('weberror', webError => {
  const p = webError.page();
  if (p) {
    console.error('Error on page:', p.url());
  } else {
    console.error('Error in unknown context');
  }
});
```

---

## Context event: 'weberror'

The event is registered on the `BrowserContext`:

```javascript
context.on('weberror', (webError) => {
  // webError: WebError
});
```

For page-specific errors there is also `page.on('pageerror')`:

```javascript
page.on('pageerror', (error) => {
  // error: Error (directly, no WebError wrapper)
  console.error(error.message);
});
```

---

## Complete example: error collection

```javascript
const errors: string[] = [];

context.on('weberror', webError => {
  const err = webError.error();
  const loc = webError.location();
  errors.push(`${err.message} (${loc.url}:${loc.line}:${loc.column})`);
});

await page.goto('https://example.com');
// ... test steps ...

if (errors.length > 0) {
  throw new Error(`Unhandled browser errors:\n${errors.join('\n')}`);
}
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 3      |
| Properties | 0     |
| Events    | 0 (1 context event: 'weberror') |

**Summary:** `error()` provides the actual error including the stack trace.
`location()` (from v1.60) is essential for source location mapping in
source map scenarios. `page()` helps to attribute errors in a multi-page context
to the correct page.

---

*Source: https://playwright.dev/docs/api/class-weberror*
