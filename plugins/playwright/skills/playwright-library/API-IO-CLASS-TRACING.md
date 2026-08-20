# Playwright — class: Tracing

> **Manifest:** 8 methods, 0 properties, 0 events.
> Creates and manages Playwright traces for the Trace Viewer.
> Access: `browserContext.tracing`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Complete example (Playwright Test)](#complete-example-playwright-test)
- [Manifest](#manifest)

## Overview

`Tracing` records detailed information about network requests,
page actions, screenshots and DOM snapshots. The resulting
`.zip` files can be opened in the Playwright Trace Viewer (`npx playwright show-trace
trace.zip`).

```javascript
// Simple example
await context.tracing.start({ screenshots: true, snapshots: true });
const page = await context.newPage();
await page.goto('https://playwright.dev');
await context.tracing.stop({ path: 'trace.zip' });
```

---

## Methods

### tracing.group(name, options?)

Creates a named group in the trace that bundles all subsequent API calls
up to the next `groupEnd()`.

**Signature:**
```typescript
tracing.group(name: string, options?: {
  location?: {
    file: string;
    line?: number;
    column?: number;
  };
}): Promise<Disposable>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `name` | `string` | yes | — | Label of the group in the Trace Viewer |
| `options.location` | `Object` | no | — | Source code location of the group (for test annotations) |
| `options.location.file` | `string` | no | — | Source file path |
| `options.location.line` | `number` | no | — | Line number |
| `options.location.column` | `number` | no | — | Column number |

**Returns:** `Promise<Disposable>` — on dispose the group is closed

**Example:**
```javascript
await context.tracing.group('Login flow');
await page.fill('#username', 'user');
await page.fill('#password', 'pass');
await page.click('#submit');
await context.tracing.groupEnd();
```

---

### tracing.groupEnd()

Closes the group most recently opened with `group()`.

**Signature:**
```typescript
tracing.groupEnd(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.groupEnd();
```

---

### tracing.start(options?)

Starts trace recording for this BrowserContext.

**Signature:**
```typescript
tracing.start(options?: {
  live?: boolean;
  name?: string;
  screenshots?: boolean;
  snapshots?: boolean;
  sources?: boolean;
  title?: string;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.live` | `boolean` | no | `false` | The trace file is not archived — allows live inspection via `tracesDir` |
| `options.name` | `string` | no | — | Prefix for temporary trace files in `tracesDir` |
| `options.screenshots` | `boolean` | no | `false` | Capture screenshots for the timeline preview |
| `options.snapshots` | `boolean` | no | `false` | Record DOM snapshots and network activity (enables inspect mode in the viewer) |
| `options.sources` | `boolean` | no | `false` | Include source files in the trace |
| `options.title` | `string` | no | — | Name displayed in the Trace Viewer |

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.start({
  screenshots: true,
  snapshots: true,
  sources: true,
  title: 'Checkout flow test'
});
```

---

### tracing.startChunk(options?)

Starts a new trace chunk on the same already running context.
Makes it possible to produce several partial traces from a single test
session.

**Signature:**
```typescript
tracing.startChunk(options?: {
  name?: string;
  title?: string;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.name` | `string` | no | — | Prefix for temporary chunk files |
| `options.title` | `string` | no | — | Name displayed in the Trace Viewer |

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.start({ screenshots: true, snapshots: true });

// First test
await context.tracing.startChunk({ title: 'Test: Login' });
await page.goto('/login');
await context.tracing.stopChunk({ path: 'trace-login.zip' });

// Second test on the same context
await context.tracing.startChunk({ title: 'Test: Checkout' });
await page.goto('/checkout');
await context.tracing.stopChunk({ path: 'trace-checkout.zip' });
```

---

### tracing.startHar(path, options?)

Starts HAR recording of network activity. The file is written when
`stopHar()` is called.

**Signature:**
```typescript
tracing.startHar(path: string, options?: {
  content?: 'omit' | 'embed' | 'attach';
  mode?: 'full' | 'minimal';
  resourcesDir?: string;
  urlFilter?: string | RegExp;
}): Promise<Disposable>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `path` | `string` | yes | — | Target file path for the HAR file (`.zip` is supported) |
| `options.content` | `'omit' \| 'embed' \| 'attach'` | no | — | How response contents are stored: `'omit'` = do not store, `'embed'` = embed in HAR, `'attach'` = as separate files |
| `options.mode` | `'full' \| 'minimal'` | no | — | `'full'` = all details, `'minimal'` = only data needed for routing |
| `options.resourcesDir` | `string` | no | — | Directory for response bodies (with `'attach'`) |
| `options.urlFilter` | `string \| RegExp` | no | — | Record only matching URLs |

**Returns:** `Promise<Disposable>` — on dispose HAR recording is stopped

**Example:**
```javascript
await context.tracing.startHar('network.har', {
  content: 'attach',
  urlFilter: /api\./
});
await page.goto('https://example.com');
await context.tracing.stopHar();
```

---

### tracing.stop(options?)

Ends trace recording and optionally exports it to a file.

**Signature:**
```typescript
tracing.stop(options?: {
  path?: string;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.path` | `string` | no | — | Target file path for the trace (`.zip`). Without it the trace is discarded. |

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.stop({ path: 'trace.zip' });
// Viewer: npx playwright show-trace trace.zip
```

---

### tracing.stopChunk(options?)

Ends the current trace chunk and exports it.

**Signature:**
```typescript
tracing.stopChunk(options?: {
  path?: string;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.path` | `string` | no | — | Target file path for the chunk trace |

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.stopChunk({ path: 'trace-chunk-1.zip' });
```

---

### tracing.stopHar()

Ends HAR recording and writes the file to the path given in
`startHar()`.

**Signature:**
```typescript
tracing.stopHar(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await context.tracing.stopHar();
```

---

## Complete example (Playwright Test)

```typescript
import { test } from '@playwright/test';

test.describe('E-Commerce Flow', () => {
  test.beforeAll(async ({ browser }) => {
    const context = await browser.newContext();
    await context.tracing.start({ screenshots: true, snapshots: true, sources: true });
    // ... setup ...
  });

  test('add to cart', async ({ page, context }) => {
    await context.tracing.startChunk({ title: 'Cart' });
    await page.goto('/shop');
    await page.click('[data-testid="add-to-cart"]');
    await context.tracing.stopChunk({ path: 'trace-cart.zip' });
  });
});
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 8      |
| Properties | 0     |
| Events    | 0      |

**Conclusion:** `start()` + `stop()` cover the standard case. `startChunk()` /
`stopChunk()` enables granular traces per test with a shared context.
`startHar()` is independent of trace recording and serves network
analysis specifically. `group()` / `groupEnd()` improve readability in the Trace
Viewer considerably.

---

*Source: https://playwright.dev/docs/api/class-tracing*
