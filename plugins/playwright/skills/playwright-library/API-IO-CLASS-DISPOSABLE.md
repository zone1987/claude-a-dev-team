# Playwright — class: Disposable

> **Manifest:** 1 method, 0 properties, 0 events.
> Allows undoing actions that return a Disposable object.
> Returned by various Playwright methods.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Return context: methods that return Disposable](#return-context-methods-that-return-disposable)
- [Using pattern with `await using` (TypeScript / ECMAScript)](#using-pattern-with-await-using-typescript-ecmascript)
- [Typical usage pattern](#typical-usage-pattern)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Disposable` is a lightweight interface that provides a single `dispose()`
method to revoke an associated resource or action.
It is returned by methods that perform a reversible action
(e.g. `page.addInitScript()`, `browserContext.addInitScript()`,
`tracing.group()`, `screencast.showActions()`, `screencast.showOverlay()`,
`screencast.start()`).

**Added:** v1.59

---

## Methods

### disposable.dispose()

Removes the associated resource or undoes the associated action.

**Signature:**
```typescript
disposable.dispose(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
// Add an init script and remove it later
const disposable = await page.addInitScript(() => {
  window.__testMode = true;
});
// ...
await disposable.dispose(); // init script is now removed
```

---

## Return context: methods that return Disposable

| Method | Effect on dispose |
|---------|---------------------|
| `page.addInitScript()` | Init script is removed |
| `browserContext.addInitScript()` | Init script is removed |
| `tracing.group()` | Trace group is closed |
| `tracing.startHar()` | HAR recording is stopped |
| `screencast.showActions()` | Action annotations are stopped |
| `screencast.showOverlay()` | Overlay is removed |
| `screencast.start()` | Screencast recording is stopped |

---

## Using pattern with `await using` (TypeScript / ECMAScript)

With TypeScript and Symbol.asyncDispose the `Disposable` interface
can be used cleanly with `await using` (provided Playwright implements the
`Symbol.asyncDispose` interface):

```typescript
// Conceptual pattern (TypeScript 5.2+)
{
  await using overlay = await page.screencast.showOverlay('<div>Loading...</div>');
  await performLongOperation();
  // overlay.dispose() is called automatically at the end of the block
}
```

---

## Typical usage pattern

```javascript
// Show a visual hint during a test step
async function withHint(page, label, fn) {
  const overlay = await page.screencast.showOverlay(
    `<div class="hint">${label}</div>`
  );
  try {
    await fn();
  } finally {
    await overlay.dispose();
  }
}

await withHint(page, 'Sign-in', async () => {
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'secret');
  await page.click('#login-button');
});
```

---

## Properties

No public properties.

## Events

No events.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 1      |
| Properties | 0     |
| Events    | 0      |

**Summary:** `Disposable` follows the resource management pattern. The class is
kept minimal — there is only one method. It is important to call `dispose()` in the
`finally` block in order to ensure that resources are released even on
errors. In TypeScript, `await using` can be used from TS 5.2 onwards as an
elegant alternative.

---

*Source: https://playwright.dev/docs/api/class-disposable*
