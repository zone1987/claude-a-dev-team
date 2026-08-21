# Playwright Evaluating, Handles and Events - Complete Reference

---

## Contents

- [1. page.evaluate()](#1-pageevaluate)
- [2. page.evaluateHandle()](#2-pageevaluatehandle)
- [3. Passing arguments to evaluate](#3-passing-arguments-to-evaluate)
- [4. JSHandle](#4-jshandle)
- [5. ElementHandle](#5-elementhandle)
- [6. addInitScript](#6-addinitscript)
- [7. page.exposeFunction](#7-pageexposefunction)
- [8. Events](#8-events)
- [9. Available page events](#9-available-page-events)
- [10. context.exposeFunction](#10-contextexposefunction)
- [11. Locator vs. ElementHandle](#11-locator-vs-elementhandle)

## 1. page.evaluate()

Runs a function in the browser context and returns the serialized result
to the test context.

```typescript
evaluate(pageFunction: Function | string, arg?: any): Promise<any>
```

| Parameter | Type | Description |
|-----------|-----|--------------|
| `pageFunction` | `Function \| string` | Function or JS string to run in the browser |
| `arg` | `Serializable \| JSHandle` | Single argument value (complex data as an object/array) |

**Important:** Promises are resolved automatically. The function runs in the
browser process, not in the test process - variables from the test scope are
NOT directly accessible.

```typescript
// Simple access to browser APIs
const href = await page.evaluate(() => document.location.href);
const title = await page.evaluate(() => document.title);

// Async function
const status = await page.evaluate(async () => {
  const response = await fetch('/api/health');
  return response.status;
});

// Pass an argument (serializable value)
const doubled = await page.evaluate(n => n * 2, 21); // 42

// Object argument
const result = await page.evaluate(({ a, b }) => a + b, { a: 10, b: 20 });

// Array argument
const sum = await page.evaluate(([a, b]) => a + b, [10, 20]);

// DOM manipulation
await page.evaluate(() => {
  document.querySelector('#banner')?.remove();
});
```

---

## 2. page.evaluateHandle()

Like `evaluate()`, but returns a `JSHandle` instead of the serialized
value. Useful when the result is not serializable or is to be passed on
directly.

```typescript
evaluateHandle(pageFunction: Function | string, arg?: any): Promise<JSHandle>
```

```typescript
// Window object as a handle
const windowHandle = await page.evaluateHandle('window');

// DOM element as a handle
const bodyHandle = await page.evaluateHandle(() => document.body);

// Complex object (Map, Set, etc.)
const mapHandle = await page.evaluateHandle(() => new Map([['a', 1], ['b', 2]]));
```

---

## 3. Passing arguments to evaluate

Only one argument is supported. For multiple values: use an object or array.

### Supported types

| Type | Example |
|-----|---------|
| Primitives | `42`, `'string'`, `true`, `null` |
| Arrays | `[1, 2, 3]` |
| Plain objects | `{ key: 'value' }` |
| `JSHandle` | Returned by `evaluateHandle()` |
| Mixed | Object/array of primitives + handles |

```typescript
// WRONG: a variable from the test scope is not visible
const value = 42;
const result = await page.evaluate(() => value); // ReferenceError!

// RIGHT: pass it as an argument
const result = await page.evaluate(v => v, value);

// Handle as an argument
const buttonHandle = await page.evaluateHandle(() => document.querySelector('button'));
const text = await page.evaluate(btn => btn.textContent, buttonHandle);
await buttonHandle.dispose();

// Multiple handles in an object
const btn1 = await page.evaluateHandle(() => document.getElementById('btn1'));
const btn2 = await page.evaluateHandle(() => document.getElementById('btn2'));
const combined = await page.evaluate(
  ({ b1, b2 }) => b1.textContent + ' | ' + b2.textContent,
  { b1: btn1, b2: btn2 }
);
await btn1.dispose();
await btn2.dispose();

// Handle with its own evaluate
const text = await buttonHandle.evaluate(
  (el, from) => el.textContent?.substring(from),
  5
);
```

---

## 4. JSHandle

Reference to a JavaScript object in the browser process.

### Methods

| Method | Returns | Description |
|---------|-----------|--------------|
| `jsHandle.evaluate(fn, arg?)` | `Promise<any>` | Run a function with the handle as the first arg |
| `jsHandle.evaluateHandle(fn, arg?)` | `Promise<JSHandle>` | Like evaluate, returns a handle |
| `jsHandle.getProperties()` | `Promise<Map<string, JSHandle>>` | All properties as a map of handles |
| `jsHandle.getProperty(name)` | `Promise<JSHandle>` | Single property as a handle |
| `jsHandle.jsonValue()` | `Promise<any>` | Get the serialized value of the handle |
| `jsHandle.asElement()` | `ElementHandle \| null` | As an ElementHandle (if a DOM element) |
| `jsHandle.dispose()` | `Promise<void>` | Release the handle and the referenced object |

```typescript
// Check the array size without serialization
const arrayHandle = await page.evaluateHandle(() => {
  window.myArray = [1, 2, 3];
  return window.myArray;
});
const length = await page.evaluate(arr => arr.length, arrayHandle);

// Element manipulation via the handle
await page.evaluate(arr => arr.push(4), arrayHandle);

// Iterate the properties of an object
const propsMap = await arrayHandle.getProperties();
for (const [key, prop] of propsMap) {
  console.log(key, await prop.jsonValue());
  await prop.dispose();
}

await arrayHandle.dispose();
```

---

## 5. ElementHandle

Specialized `JSHandle` for DOM elements. **Recommendation:** prefer locators
- an ElementHandle goes stale after navigations.

### Methods

| Method | Returns | Description |
|---------|-----------|--------------|
| `elementHandle.boundingBox()` | `Promise<{x,y,width,height} \| null>` | Position and size |
| `elementHandle.getAttribute(name)` | `Promise<string \| null>` | Attribute value |
| `elementHandle.innerHTML()` | `Promise<string>` | Inner HTML |
| `elementHandle.innerText()` | `Promise<string>` | Inner text |
| `elementHandle.textContent()` | `Promise<string \| null>` | Text content |
| `elementHandle.inputValue()` | `Promise<string>` | Value of input/select/textarea |
| `elementHandle.isVisible()` | `Promise<boolean>` | Visibility |
| `elementHandle.isEnabled()` | `Promise<boolean>` | Enabled state |
| `elementHandle.isChecked()` | `Promise<boolean>` | Checkbox state |
| `elementHandle.click(options?)` | `Promise<void>` | Trigger a click |
| `elementHandle.fill(value)` | `Promise<void>` | Requires a form field |
| `elementHandle.$(selector)` | `Promise<ElementHandle \| null>` | Find a child element |
| `elementHandle.$$(selector)` | `Promise<ElementHandle[]>` | Find child elements |
| `elementHandle.$eval(selector, fn)` | `Promise<any>` | Evaluate a child |
| `elementHandle.$$eval(selector, fn)` | `Promise<any>` | Evaluate children |
| `elementHandle.waitForSelector(sel, opts?)` | `Promise<ElementHandle>` | Wait for a child |
| `elementHandle.asElement()` | `ElementHandle` | Return itself |
| `elementHandle.dispose()` | `Promise<void>` | Release |

```typescript
// Create an ElementHandle (only when really necessary)
const el = await page.waitForSelector('#container');
const box = await el.boundingBox();
console.log(`Position: ${box?.x}, ${box?.y}`);

// With evaluate
const text = await el.evaluate(node => node.textContent);

// Locator preferred
const locator = page.locator('#container');
await expect(locator).toBeVisible();
```

---

## 6. addInitScript

Runs code before every page load (also after navigations).

### page.addInitScript(script, arg?)

| Parameter | Type | Description |
|-----------|-----|--------------|
| `script` | `Function \| string \| {path: string, content: string}` | Script to run |
| `arg` | `Serializable` | Argument for the script function |

```typescript
// Function with an argument
await page.addInitScript(seed => {
  Math.random = () => seed;
}, 0.42);

// Load from a file
await page.addInitScript({ path: './mocks/preload.js' });

// As a string
await page.addInitScript('window.__TEST__ = true;');

// Typical beforeEach pattern
test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => {
    // Set global mock variables
    (window as any).__MOCK_USER__ = { id: 1, role: 'admin' };
  });
});
```

### context.addInitScript(script, arg?)

Applies to all pages in the context (including newly opened ones).

```typescript
await context.addInitScript(() => {
  // Applies to all pages of this context
  window.__ENV__ = 'test';
});
```

---

## 7. page.exposeFunction

Makes a Node.js function callable in the browser context.

```typescript
exposeFunction(name: string, callback: Function): Promise<void>
```

```typescript
// Expose a function
await page.exposeFunction('sha256', async (text: string) => {
  const { createHash } = await import('crypto');
  return createHash('sha256').update(text).digest('hex');
});

// Callable in the browser
const hash = await page.evaluate(async () => {
  return await window.sha256('hello world');
});

// Typical use: routing browser logs to the test
const logs: string[] = [];
await page.exposeFunction('recordLog', (msg: string) => {
  logs.push(msg);
});
await page.evaluate(() => {
  console.log = (msg: string) => window.recordLog(msg);
});
```

---

## 8. Events

### page.waitForEvent(event, options?)

Waits for a single occurrence of an event.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `event` | `string` | Event name |
| `optionOrPredicate` | `Function \| {predicate?, timeout?}` | Filter function or options object |

```typescript
// Catch a popup
const popupPromise = page.waitForEvent('popup');
await page.click('#open-popup');
const popup = await popupPromise;
await popup.waitForLoadState();

// With a predicate
const downloadPromise = page.waitForEvent('download', {
  predicate: download => download.suggestedFilename().endsWith('.pdf'),
  timeout: 10000,
});
await page.click('#export-pdf');
const download = await downloadPromise;

// Wait for navigation and an event at the same time
const [response, request] = await Promise.all([
  page.waitForEvent('response'),
  page.waitForRequest(/\/api\//),
  page.click('#submit'),
]);
```

### page.on(event, handler)

Persistent event listening.

```typescript
// Log requests/responses
page.on('request', (request) => {
  console.log(`>> ${request.method()} ${request.url()}`);
});
page.on('response', (response) => {
  console.log(`<< ${response.status()} ${response.url()}`);
});

// Catch errors
page.on('pageerror', (err) => {
  console.error('Page error:', err.message);
});
page.on('console', (msg) => {
  if (msg.type() === 'error') console.error('Console error:', msg.text());
});

// Worker events
page.on('worker', (worker) => {
  console.log('Worker created:', worker.url());
});
```

### page.once(event, handler)

One-off handler (removed automatically after the first occurrence).

```typescript
// Accept a dialog once
page.once('dialog', dialog => dialog.accept('test input'));
await page.evaluate("prompt('Name:')");

// Catch the next request
page.once('request', request => {
  console.log('Next request:', request.url());
});
```

### page.off(event, handler)

Remove a handler.

```typescript
const handler = (request: Request) => console.log(request.url());
page.on('request', handler);
await page.goto('/some-page');
page.off('request', handler); // No longer active
```

---

## 9. Available page events

| Event | Callback parameter | Description |
|-------|--------------------|--------------|
| `'close'` | `Page` | Page closed |
| `'console'` | `ConsoleMessage` | console.* call |
| `'crash'` | `Page` | Page crashed |
| `'dialog'` | `Dialog` | alert/confirm/prompt |
| `'domcontentloaded'` | `Page` | DOMContentLoaded |
| `'download'` | `Download` | Download started |
| `'filechooser'` | `FileChooser` | File dialog opened |
| `'frameattached'` | `Frame` | Frame added |
| `'framedetached'` | `Frame` | Frame removed |
| `'framenavigated'` | `Frame` | Frame navigated |
| `'load'` | `Page` | Load event |
| `'pageerror'` | `Error` | Uncaught exception |
| `'popup'` | `Page` | Popup opened |
| `'request'` | `Request` | Request sent |
| `'requestfailed'` | `Request` | Request failed |
| `'requestfinished'` | `Request` | Request finished |
| `'response'` | `Response` | Response received |
| `'websocket'` | `WebSocket` | WebSocket opened |
| `'worker'` | `Worker` | Worker created |

---

## 10. context.exposeFunction

Like `page.exposeFunction`, applies to all pages in the context.

```typescript
await context.exposeFunction('testHelper', () => ({
  mockDate: new Date('2024-01-01'),
  userId: 42,
}));
```

---

## 11. Locator vs. ElementHandle

| Aspect | Locator | ElementHandle |
|--------|---------|---------------|
| Reference | Lazy (re-resolved on every use) | Fixed (goes stale after navigation) |
| Navigation | Safe | Can go stale |
| Auto-wait | Yes | No |
| Recommendation | Prefer | Only in exceptions |

```typescript
// PREFERRED: locator
const button = page.locator('#submit');
await expect(button).toBeVisible();
await button.click();

// ONLY when necessary: ElementHandle
const handle = await page.waitForSelector('#lazy-element');
const bbox = await handle.boundingBox();
await handle.dispose();
```

---

Source: https://playwright.dev/docs/evaluating | https://playwright.dev/docs/handles | https://playwright.dev/docs/events
