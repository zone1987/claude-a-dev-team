# Playwright class-jshandle: Complete API reference

`JSHandle` represents a reference to a JavaScript object in the browser context.
It provides access to JavaScript objects that are not JSON-serializable
(e.g. `window`, DOM elements, complex objects).

`JSHandle` is returned by:
- `page.evaluateHandle()`
- `frame.evaluateHandle()`
- `jsHandle.evaluateHandle()`
- `jsHandle.getProperty()`
- `jsHandle.getProperties()` (map values)
- `page.waitForFunction()`
- `frame.waitForFunction()`

`ElementHandle` is a subclass of `JSHandle` and inherits all methods documented here.

---

## Contents

- [Table of contents](#table-of-contents)
- [1. asElement()](#1-aselement)
- [2. dispose()](#2-dispose)
- [3. evaluate()](#3-evaluate)
- [4. evaluateHandle()](#4-evaluatehandle)
- [5. getProperties()](#5-getproperties)
- [6. getProperty()](#6-getproperty)
- [7. jsonValue()](#7-jsonvalue)
- [8. Typical usage scenarios](#8-typical-usage-scenarios)
- [9. Manifest](#9-manifest)

## Table of contents

1. [asElement()](#1-aselement)
2. [dispose()](#2-dispose)
3. [evaluate()](#3-evaluate)
4. [evaluateHandle()](#4-evaluatehandle)
5. [getProperties()](#5-getproperties)
6. [getProperty()](#6-getproperty)
7. [jsonValue()](#7-jsonvalue)
8. [Typical usage scenarios](#8-typical-usage-scenarios)
9. [Manifest](#9-manifest)

---

## 1. asElement()

```typescript
jsHandle.asElement(): null | ElementHandle
```

**Parameters:** None

**Returns:** `ElementHandle` if the handle represents a DOM element, otherwise `null`.

Allows safe casting of a `JSHandle` to `ElementHandle`.

```typescript
// Check a handle obtained from evaluateHandle
const handle = await page.evaluateHandle(() => document.querySelector('h1'));
const elementHandle = handle.asElement();

if (elementHandle) {
  // Is a DOM element
  const text = await elementHandle.textContent();
  console.log('Title:', text);
  const box = await elementHandle.boundingBox();
  console.log('Position:', box);
} else {
  // Not a DOM element (e.g. primitive value or complex object)
  const value = await handle.jsonValue();
  console.log('Value:', value);
}

// Difference to ElementHandle.asElement():
// ElementHandle.asElement() always returns itself
// JSHandle.asElement() returns null if not a DOM element
```

---

## 2. dispose()

```typescript
jsHandle.dispose(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

Releases the JavaScript object handle. The browser-side object is no longer referenced by
Playwright and can be cleaned up by the garbage collector. After `dispose()` no
further operations on the handle are possible — they throw an error.

```typescript
const handle = await page.evaluateHandle(() => window);
// Work with handle...
const userAgent = await handle.evaluate(win => win.navigator.userAgent);
console.log(userAgent);
// Release the handle when no longer needed
await handle.dispose();

// Also clean up handles in arrays/maps
const propsMap = await handle.getProperties();
for (const [key, propHandle] of propsMap) {
  await propHandle.dispose();
}
```

---

## 3. evaluate()

```typescript
jsHandle.evaluate<T>(
  pageFunction: ((handle: Handle, arg?: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pageFunction` | `Function\|string` | yes | Function executed in the browser; the handle is passed as the first argument |
| `arg` | `Serializable\|JSHandle` | no | Optional second argument |

**Returns:** `Promise<T>` — serialized JSON value. Non-JSON-capable values become `undefined`.

Executes a function in the browser context and passes the handle as the first argument.
Ideal for operations on JavaScript objects that are not directly serializable.

```typescript
// Analyze the window object
const windowHandle = await page.evaluateHandle(() => window);
const url = await windowHandle.evaluate(win => win.location.href);
const scrollY = await windowHandle.evaluate(win => win.scrollY);

// Evaluate an array handle
const arrayHandle = await page.evaluateHandle(() =>
  Array.from(document.querySelectorAll('a'))
);
const count = await arrayHandle.evaluate(arr => arr.length);
const firstHref = await arrayHandle.evaluate(arr => arr[0]?.getAttribute('href'));

// With an additional argument
const threshold = 5;
const longLinks = await arrayHandle.evaluate(
  (links, minLen) => links.filter(a => a.textContent!.length > minLen).length,
  threshold
);

// Map object
const mapHandle = await page.evaluateHandle(() => new Map([['key', 'value']]));
const hasKey = await mapHandle.evaluate(m => m.has('key'));
```

---

## 4. evaluateHandle()

```typescript
jsHandle.evaluateHandle<T>(
  pageFunction: ((handle: Handle, arg?: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pageFunction` | `Function\|string` | yes | Function executed in the browser; the handle as the first argument |
| `arg` | `Serializable\|JSHandle` | no | Optional second argument |

**Returns:** `Promise<JSHandle<T>>` — a new handle to the returned object.

Like `evaluate()`, but returns a `JSHandle` instead of a serialized value.
Useful when the return value itself is complex/non-serializable, or for chaining.

```typescript
// Extract an element from an array handle
const listHandle = await page.evaluateHandle(() =>
  document.querySelectorAll('li')
);
// First element as a new handle
const firstHandle = await listHandle.evaluateHandle(list => list[0]);
const elementHandle = firstHandle.asElement();
if (elementHandle) {
  const text = await elementHandle.textContent();
}

// Traverse child elements
const bodyHandle = await page.evaluateHandle(() => document.body);
const headerHandle = await bodyHandle.evaluateHandle(body => body.querySelector('header'));
const headerEl = headerHandle.asElement();

// Navigate window.history and keep it as a handle
const historyHandle = await page.evaluateHandle(() => window.history);
const stateHandle = await historyHandle.evaluateHandle(h => h.state);

// Clean up properly
await listHandle.dispose();
await firstHandle.dispose();
await bodyHandle.dispose();
await headerHandle.dispose();
await historyHandle.dispose();
await stateHandle.dispose();
```

---

## 5. getProperties()

```typescript
jsHandle.getProperties(): Promise<Map<string, JSHandle>>
```

**Parameters:** None

**Returns:** `Promise<Map<string, JSHandle>>` — map with property names as keys
and JSHandle instances as values.

Returns all **own** (non-inherited) properties of the referenced object.
Each property is itself a JSHandle.

```typescript
// All own properties of an object
const handle = await page.evaluateHandle(() => ({ name: 'Max', age: 30, active: true }));
const props = await handle.getProperties();

for (const [key, valueHandle] of props) {
  const value = await valueHandle.jsonValue();
  console.log(`${key}: ${value}`);
  await valueHandle.dispose();
}
await handle.dispose();
// Output:
// name: Max
// age: 30
// active: true

// DOM element properties
const inputHandle = await page.evaluateHandle(() => document.querySelector('input'));
const inputProps = await inputHandle.getProperties();
const valueHandle = inputProps.get('value');
if (valueHandle) {
  const value = await valueHandle.jsonValue();
  console.log('Input value:', value);
  await valueHandle.dispose();
}

// Own properties only (no prototype properties)
const arrayHandle = await page.evaluateHandle(() => [1, 2, 3]);
const arrayProps = await arrayHandle.getProperties();
// Contains '0', '1', '2', 'length' — but NOT Array.prototype methods
```

---

## 6. getProperty()

```typescript
jsHandle.getProperty(propertyName: string): Promise<JSHandle>
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `propertyName` | `string` | yes | Name of the property to retrieve |

**Returns:** `Promise<JSHandle>` — handle to the property value.

Retrieves a single property without loading all properties.
More efficient than `getProperties()` when only one property is needed.

```typescript
// Simple property
const handle = await page.evaluateHandle(() => ({
  name: 'Max',
  address: { city: 'Berlin' }
}));

const nameHandle = await handle.getProperty('name');
const name = await nameHandle.jsonValue();
console.log('Name:', name); // 'Max'
await nameHandle.dispose();

// Nested property (yields a handle to an object)
const addressHandle = await handle.getProperty('address');
const cityHandle = await addressHandle.getProperty('city');
const city = await cityHandle.jsonValue();
console.log('City:', city); // 'Berlin'
await cityHandle.dispose();
await addressHandle.dispose();

await handle.dispose();

// Read an input value
const inputHandle = await page.evaluateHandle(() =>
  document.querySelector('input[name=email]')
);
const valueHandle = await inputHandle.getProperty('value');
const value = await valueHandle.jsonValue();
console.log('E-mail:', value);

// Checked state of a checkbox
const checkboxHandle = await page.evaluateHandle(() =>
  document.querySelector('input[type=checkbox]')
);
const checkedHandle = await checkboxHandle.getProperty('checked');
const checked = await checkedHandle.jsonValue();
console.log('Checked:', checked);

await valueHandle.dispose();
await inputHandle.dispose();
await checkedHandle.dispose();
await checkboxHandle.dispose();
```

---

## 7. jsonValue()

```typescript
jsHandle.jsonValue<T>(): Promise<T>
```

**Parameters:** None

**Returns:** `Promise<T>` — JSON representation of the referenced object.

Serializes the referenced JavaScript object as JSON. If the object has a `toJSON()`
method, it is **not** called. Circular references and non-serializable
values (e.g. `undefined`, functions, symbols) are ignored/removed.

For DOM elements, `jsonValue()` returns an empty object `{}` — in that case
use `evaluate()` or `ElementHandle` methods.

```typescript
// Primitive values
const numHandle = await page.evaluateHandle(() => 42);
const num = await numHandle.jsonValue();
console.log(num); // 42

const strHandle = await page.evaluateHandle(() => 'Hello');
const str = await strHandle.jsonValue();
console.log(str); // 'Hello'

// Arrays
const arrHandle = await page.evaluateHandle(() => [1, 2, 3, 'four']);
const arr = await arrHandle.jsonValue();
console.log(arr); // [1, 2, 3, 'four']

// Objects
const objHandle = await page.evaluateHandle(() => ({
  user: 'Max',
  scores: [10, 20],
  active: true
}));
const obj = await objHandle.jsonValue();
console.log(obj.user); // 'Max'

// DOM element — returns {}
const elHandle = await page.evaluateHandle(() => document.body);
const elJson = await elHandle.jsonValue();
console.log(elJson); // {}
// Instead: elHandle.asElement()?.textContent()

// Non-serializable values
const fnHandle = await page.evaluateHandle(() => function test() {});
const fnJson = await fnHandle.jsonValue();
console.log(fnJson); // undefined

// Clean up
await numHandle.dispose();
await strHandle.dispose();
await arrHandle.dispose();
await objHandle.dispose();
await elHandle.dispose();
await fnHandle.dispose();
```

---

## 8. Typical usage scenarios

### Scenario 1: Inspect the window object

```typescript
const windowHandle = await page.evaluateHandle(() => window);

// Read properties
const location = await windowHandle.evaluate(w => ({
  href: w.location.href,
  pathname: w.location.pathname,
  search: w.location.search
}));
console.log(location);

// Check a global variable
const appState = await windowHandle.evaluate(w => (w as any).__APP_STATE__);

await windowHandle.dispose();
```

---

### Scenario 2: Process a NodeList / HTMLCollection

```typescript
// All links as a handle
const linksHandle = await page.evaluateHandle(() =>
  document.querySelectorAll('a[href]')
);

// Count
const count = await linksHandle.evaluate(links => links.length);

// All HREFs
const hrefs = await linksHandle.evaluate(links =>
  Array.from(links).map(a => (a as HTMLAnchorElement).href)
);

await linksHandle.dispose();
```

---

### Scenario 3: Complex return values from evaluate

```typescript
// When evaluate is not enough (object not JSON-capable)
const setHandle = await page.evaluateHandle(() => new Set(['a', 'b', 'c']));
const size = await setHandle.evaluate(s => s.size);
const hasA = await setHandle.evaluate(s => s.has('a'));
const asArray = await setHandle.evaluate(s => Array.from(s));
console.log(asArray); // ['a', 'b', 'c']

await setHandle.dispose();
```

---

### Scenario 4: Handle chaining

```typescript
// Without chaining (inefficient — multiple evaluate calls)
const formHandle = await page.evaluateHandle(() =>
  document.querySelector('form#checkout')
);
const inputHandle = await formHandle.evaluateHandle(form =>
  form.querySelector('input[name=card]')
);
const inputEl = inputHandle.asElement();
if (inputEl) {
  await inputEl.fill('4111111111111111');
}

// Clean up properly
await inputHandle.dispose();
await formHandle.dispose();
```

---

### Scenario 5: Memory-safe usage with using

```typescript
// TypeScript 5+ Symbol.asyncDispose (if the Playwright version supports it)
{
  const handle = await page.evaluateHandle(() => window);
  try {
    const title = await handle.evaluate(w => w.document.title);
    console.log(title);
  } finally {
    await handle.dispose(); // Always clean up
  }
}
```

---

## 9. Manifest

| Method | Returns | Description |
|---|---|---|
| `asElement()` | `null \| ElementHandle` | Cast to ElementHandle |
| `dispose()` | `Promise<void>` | Release the handle |
| `evaluate(fn, arg?)` | `Promise<T>` | Run a function with the handle, return the serialized value |
| `evaluateHandle(fn, arg?)` | `Promise<JSHandle>` | Run a function with the handle, return a handle |
| `getProperties()` | `Promise<Map<string, JSHandle>>` | All own properties as a map |
| `getProperty(name)` | `Promise<JSHandle>` | Single property as a handle |
| `jsonValue()` | `Promise<T>` | JSON serialization of the referenced object |

**Total: 7 methods** (no properties, no events)

**Summary:** `JSHandle` is the base class for all browser object handles in Playwright.
It enables safe work with non-serializable JavaScript values in the browser.
Important: always release handles with `dispose()` to avoid memory leaks.
In practice, `JSHandle` is mostly used indirectly through `ElementHandle` and `page.evaluateHandle()`
— working with `JSHandle` directly is mainly necessary for complex browser objects
(sets, maps, window, complex classes).

---

**Source:** https://playwright.dev/docs/api/class-jshandle
