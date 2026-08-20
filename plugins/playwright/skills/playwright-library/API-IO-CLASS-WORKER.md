# Playwright — class: Worker

> **Manifest:** 4 methods, 0 properties, 2 events.
> Represents a Web Worker or Service Worker of a page.
> Instances are obtained via `page.on('worker')` or `page.workers()`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Events](#events)
- [Worker access via Page](#worker-access-via-page)
- [Manifest](#manifest)

## Overview

`Worker` represents a dedicated Web Worker. Service Workers can be
retrieved via `browserContext.serviceWorkers()`. Worker instances
allow code to be executed inside the worker context as well as
querying the worker URL.

```javascript
page.on('worker', worker => {
  console.log('Worker started:', worker.url());
});

page.on('workerdestroyed', worker => {
  console.log('Worker terminated:', worker.url());
});
```

---

## Methods

### worker.evaluate(pageFunction, arg?)

Executes a function in the worker context and returns the result as a
serialized value.

**Signature:**
```typescript
worker.evaluate<R>(
  pageFunction: Function | string,
  arg?: any
): Promise<R>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `pageFunction` | `Function \| string` | yes | — | Function or JS string that is executed in the worker context |
| `arg` | `EvaluationArgument` | no | — | Optional argument passed to `pageFunction`. Must be JSON-serializable or a JSHandle. |

**Returns:** `Promise<R>` — serialized return value (JSON-compatible types)

**Special values:** `NaN`, `Infinity`, `-0` and `undefined` are handled
correctly.

**Example:**
```javascript
const workerValue = await worker.evaluate(() => {
  return { workerType: 'dedicated', navigator: navigator.userAgent };
});
console.log(workerValue);
```

---

### worker.evaluateHandle(pageFunction, arg?)

Like `evaluate()`, but returns a `JSHandle` instead of a serialized value.
Suitable for non-serializable worker objects.

**Signature:**
```typescript
worker.evaluateHandle<R>(
  pageFunction: Function | string,
  arg?: any
): Promise<JSHandle<R>>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `pageFunction` | `Function \| string` | yes | — | Function or JS string |
| `arg` | `EvaluationArgument` | no | — | Optional argument |

**Returns:** `Promise<JSHandle>` — handle on the worker value

**Example:**
```javascript
const handle = await worker.evaluateHandle(() => globalThis);
const keys = await handle.getProperties();
```

---

### worker.url()

Returns the URL of the worker script.

**Signature:**
```typescript
worker.url(): string
```

**Parameters:** None

**Returns:** `string` — full URL of the worker script

**Example:**
```javascript
console.log('Worker URL:', worker.url());
// e.g. "https://example.com/workers/background.js"
```

---

### worker.waitForEvent(event, optionsOrPredicate?)

Waits for a specific event to be fired on the worker object.

**Signature:**
```typescript
worker.waitForEvent(
  event: string,
  optionsOrPredicate?: Function | {
    predicate?: Function;
    timeout?: number;
  }
): Promise<any>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `event` | `string` | yes | — | Event name (e.g. `'close'`, `'console'`) |
| `optionsOrPredicate` | `Function \| Object` | no | — | Filter function or options object |
| `optionsOrPredicate.predicate` | `Function` | no | — | Filters events; returns `true` when the event should be accepted |
| `optionsOrPredicate.timeout` | `number` | no | `0` | Maximum wait time in ms (`0` = no timeout) |

**Returns:** `Promise<any>` — the event payload

**Example:**
```javascript
const closeEvent = await worker.waitForEvent('close');
console.log('Worker closed');
```

---

## Events

### worker.on('close')

Fired when this dedicated Web Worker is terminated.

**Event payload:** `Worker` — the worker object itself

**Example:**
```javascript
worker.on('close', (w) => {
  console.log('Worker terminated:', w.url());
});
```

---

### worker.on('console')

Fired when JavaScript in the worker calls `console` API methods
(e.g. `console.log`, `console.dir`).

**Event payload:** `ConsoleMessage`

**Added:** v1.57

**Example:**
```javascript
worker.on('console', msg => {
  console.log(`[Worker ${worker.url()}] [${msg.type()}] ${msg.text()}`);
});
```

---

## Worker access via Page

```javascript
// Retrieve all active workers of a page
const workers = page.workers();
for (const w of workers) {
  console.log(w.url());
}

// Wait for a new worker
const workerPromise = page.waitForEvent('worker');
await page.goto('https://example.com'); // loads worker
const worker = await workerPromise;

// Service Workers (via BrowserContext)
const serviceWorkers = context.serviceWorkers();
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 4      |
| Properties | 0     |
| Events    | 2 ('close', 'console') |

**Summary:** `evaluate()` is the primary method for executing code in the
worker context and retrieving results. `url()` identifies workers uniquely.
The `console` event enables complete logging of worker activity as
well, which is particularly important for debugging in Service-Worker
environments.

---

*Source: https://playwright.dev/docs/api/class-worker*
