# Playwright — class: Debugger

> **Manifest:** 5 methods, 0 properties, 1 event.
> Allows pausing and controlling Playwright test execution programmatically.
> Added: v1.59. Access: `test.info().debugger` or via the `@playwright/test` API.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Events](#events)
- [Complete example](#complete-example)
- [Manifest](#manifest)

## Overview

`Debugger` provides a programmatic interface for debugging
Playwright tests — similar to browser DevTools breakpoints, but at the
Playwright action level. The debugger pauses *before* the next
Playwright action (not inside the JavaScript interpreter).

All methods were introduced in v1.59.

---

## Methods

### debugger.next()

Resumes execution and pauses before the next action.
Throws an error if the debugger is not paused.

**Signature:**
```typescript
debugger.next(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.59

**Example:**
```javascript
// Step through actions one at a time
await debugger.next(); // one action forward
await debugger.next(); // next action
```

---

### debugger.pausedDetails()

Returns information about the current paused state.
Returns `null` if the debugger is not paused.

**Signature:**
```typescript
debugger.pausedDetails(): null | {
  location: {
    file: string;
    line?: number;
    column?: number;
  };
  title: string;
}
```

**Parameters:** None

**Returns:** `null | Object` with:

| Field | Type | Description |
|------|-----|--------------|
| `location` | `Object` | Source code location of the next action |
| `location.file` | `string` | Source file path |
| `location.line` | `number` (optional) | Line number |
| `location.column` | `number` (optional) | Column number |
| `title` | `string` | Description of the next action |

**Added:** v1.59

**Example:**
```javascript
const details = debugger.pausedDetails();
if (details) {
  console.log(`Paused at: "${details.title}"`);
  console.log(`Location: ${details.location.file}:${details.location.line}`);
}
```

---

### debugger.requestPause()

Configures the debugger to pause before the next action.
Throws an error if already paused.

**Signature:**
```typescript
debugger.requestPause(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.59

**Difference from `page.pause()`:**
- `page.pause()`: Pauses *immediately* at the current position.
- `debugger.requestPause()`: Sets a breakpoint for the *next* action.

**Example:**
```javascript
await debugger.requestPause();
// The next Playwright action will now pause
await page.click('#button'); // pauses here
```

---

### debugger.resume()

Resumes execution from the paused state.
Throws an error if not paused.

**Signature:**
```typescript
debugger.resume(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Added:** v1.59

**Example:**
```javascript
// The debugger runs until the next requestPause() or runTo()
await debugger.resume();
```

---

### debugger.runTo(location)

Resumes execution and pauses when an action is triggered from the given
source code location. Throws an error if not paused.

**Signature:**
```typescript
debugger.runTo(location: {
  file: string;
  line?: number;
  column?: number;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `location` | `Object` | yes | — | Target source location object |
| `location.file` | `string` | yes | — | Path to the target file |
| `location.line` | `number` | no | — | Line number of the breakpoint |
| `location.column` | `number` | no | — | Column number of the breakpoint |

**Returns:** `Promise<void>`

**Added:** v1.59

**Example:**
```javascript
// Run until line 55 in the test file
await debugger.runTo({
  file: '/tests/checkout.spec.ts',
  line: 55
});
```

---

## Events

### debugger.on('pausedstatechanged')

Fired when the debugger pauses or resumes.

**Added:** v1.59

**Signature:**
```javascript
debugger.on('pausedstatechanged', (data) => {
  // data: payload (type not specified in the documentation)
});
```

**Example:**
```javascript
debugger.on('pausedstatechanged', () => {
  const details = debugger.pausedDetails();
  if (details) {
    console.log(`Debugger paused: "${details.title}"`);
  } else {
    console.log('Debugger resumed');
  }
});
```

---

## Complete example

```javascript
// Programmatic debugger workflow
test('checkout flow', async ({ page, debugger: dbg }) => {
  // Wait for the next action
  await dbg.requestPause();

  await page.goto('/checkout');

  // Inspect the details of the current pause
  const details = dbg.pausedDetails();
  console.log('Paused at:', details?.title);

  // Step by step
  await dbg.next();
  await dbg.next();

  // Run to a specific location
  await dbg.runTo({
    file: 'checkout.spec.ts',
    line: 42
  });

  // Let it continue
  await dbg.resume();
});
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 5      |
| Properties | 0     |
| Events    | 1 ('pausedstatechanged') |

**Summary:** The `Debugger` is a programmatic breakpoint mechanism at the
Playwright action level. `requestPause()` + `next()` enables step debugging.
`runTo()` is the equivalent of "Run to Cursor" in IDEs. The
`pausedstatechanged` event enables reactive debug UIs or reporter
integrations.

---

*Source: https://playwright.dev/docs/api/class-debugger*
