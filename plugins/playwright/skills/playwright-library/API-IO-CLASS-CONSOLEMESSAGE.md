# Playwright — class: ConsoleMessage

> **Manifest:** 6 methods, 0 properties, 0 events (1 external page event).
> Represents a single console message from the browser context.
> Instances are obtained via `page.on('console')` and `worker.on('console')`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Page event: 'console'](#page-event-console)
- [Manifest](#manifest)

## Overview

`ConsoleMessage` encapsulates all information about a single console API
call made by the page (`console.log`, `console.error`, etc.). Each instance
contains the text, the type, the origin location and possibly the arguments.

```javascript
page.on('console', async msg => {
  console.log(`[${msg.type()}] ${msg.text()}`);
  if (msg.type() === 'error') {
    console.error('Browser error:', msg.text());
  }
});
```

---

## Methods

### consoleMessage.args()

Returns all arguments that were passed to the console function,
as a JSHandle array.

**Signature:**
```typescript
consoleMessage.args(): Array<JSHandle>
```

**Parameters:** None

**Returns:** `Array<JSHandle>` — one handle per argument

**Example:**
```javascript
page.on('console', async msg => {
  for (const arg of msg.args()) {
    console.log(await arg.jsonValue());
  }
});
```

**Note:** `JSHandle.jsonValue()` throws for non-serializable values.
Use `asElement()` for DOM elements.

---

### consoleMessage.location()

Returns the source code location of the console call.

**Signature:**
```typescript
consoleMessage.location(): {
  url: string;
  line: number;
  column: number;
  lineNumber: number;   // deprecated, use line
  columnNumber: number; // deprecated, use column
}
```

**Parameters:** None

**Returns:** Object with:

| Field | Type | Description |
|------|-----|--------------|
| `url` | `string` | URL of the source resource |
| `line` | `number` | 0-based line number |
| `column` | `number` | 0-based column number |
| `lineNumber` | `number` | Deprecated — use `line` |
| `columnNumber` | `number` | Deprecated — use `column` |

**Example:**
```javascript
page.on('console', msg => {
  const loc = msg.location();
  console.log(`${loc.url}:${loc.line}:${loc.column}`);
});
```

---

### consoleMessage.page()

Returns the page that produced this message.

**Signature:**
```typescript
consoleMessage.page(): Page | null
```

**Parameters:** None

**Returns:** `Page | null` — the triggering page or `null`

**Example:**
```javascript
page.on('console', msg => {
  const p = msg.page();
  if (p) console.log('Page:', p.url());
});
```

---

### consoleMessage.text()

Returns the text content of the console message.

**Signature:**
```typescript
consoleMessage.text(): string
```

**Parameters:** None

**Returns:** `string` — the serialized message text

**Example:**
```javascript
page.on('console', msg => {
  console.log('Message:', msg.text());
});
```

---

### consoleMessage.timestamp()

Returns the timestamp of the message in milliseconds since the Unix epoch.

**Signature:**
```typescript
consoleMessage.timestamp(): number
```

**Parameters:** None

**Returns:** `number` — millisecond timestamp

**Added:** v1.59

**Example:**
```javascript
page.on('console', msg => {
  const date = new Date(msg.timestamp());
  console.log(`[${date.toISOString()}] ${msg.text()}`);
});
```

---

### consoleMessage.type()

Returns the type of the console message.

**Signature:**
```typescript
consoleMessage.type(): string
```

**Parameters:** None

**Returns:** One of the following strings:

| Value | Corresponds to |
|------|-----------|
| `'log'` | `console.log()` |
| `'debug'` | `console.debug()` |
| `'info'` | `console.info()` |
| `'error'` | `console.error()` |
| `'warning'` | `console.warn()` |
| `'dir'` | `console.dir()` |
| `'dirxml'` | `console.dirxml()` |
| `'table'` | `console.table()` |
| `'trace'` | `console.trace()` |
| `'clear'` | `console.clear()` |
| `'startGroup'` | `console.group()` |
| `'startGroupCollapsed'` | `console.groupCollapsed()` |
| `'endGroup'` | `console.groupEnd()` |
| `'assert'` | `console.assert()` |
| `'profile'` | `console.profile()` |
| `'profileEnd'` | `console.profileEnd()` |
| `'count'` | `console.count()` |
| `'time'` | `console.time()` |
| `'timeEnd'` | `console.timeEnd()` |

**Example:**
```javascript
page.on('console', async msg => {
  if (msg.type() === 'error') {
    console.error(`Browser-Error: "${msg.text()}"`);
  }
});
```

---

### consoleMessage.worker()

Returns the Web Worker or Service Worker that produced the message.

**Signature:**
```typescript
consoleMessage.worker(): Worker | null
```

**Parameters:** None

**Returns:** `Worker | null`

**Added:** v1.57

**Example:**
```javascript
page.on('console', msg => {
  const w = msg.worker();
  if (w) console.log('From worker:', w.url());
});
```

---

## Page event: 'console'

```javascript
page.on('console', msg => {
  // msg is a ConsoleMessage
  console.log(`[${msg.type()}] ${msg.text()}`);
});
```

Also available on `Worker`:

```javascript
worker.on('console', msg => { /* ... */ });
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 6 (+1 since v1.57: worker()) |
| Properties | 0     |
| Events    | 0 (1 page event: 'console', 1 worker event: 'console') |

**Summary:** `text()` and `type()` are enough for simple log monitoring.
`args()` is required when structured objects (arrays, objects) need to be
inspected. `timestamp()` enables temporal correlation of browser
messages with test steps.

---

*Source: https://playwright.dev/docs/api/class-consolemessage*
