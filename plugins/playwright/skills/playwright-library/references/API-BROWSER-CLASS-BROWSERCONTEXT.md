# class-browsercontext

`BrowserContext` provides an isolated browser session with its own cookie storage, LocalStorage, permissions and network routing. Each test file should use its own context to avoid side effects.

Methods: 25 | Properties: 4 | Events: 16

---

## Contents

- [Methods](#methods)
- [Properties](#properties)
- [Events](#events)
- [Deprecated](#deprecated)
- [Manifest](#manifest)

## Methods

### browserContext.addCookies(cookies)

```ts
await browserContext.addCookies(cookies): Promise<void>
```

Adds cookies to the context. Either the `url` field or both `domain` + `path` are required.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `cookies` | Array<Object> | Yes | — | Array of cookie objects |
| `cookies[].name` | string | Yes | — | Cookie name |
| `cookies[].value` | string | Yes | — | Cookie value |
| `cookies[].url` | string | No* | — | Cookie URL (alternatively: domain+path) |
| `cookies[].domain` | string | No* | — | Domain; with a `.` prefix for subdomains |
| `cookies[].path` | string | No* | — | Path |
| `cookies[].expires` | number | No | — | Expiry time as a Unix timestamp (seconds) |
| `cookies[].httpOnly` | boolean | No | — | HttpOnly flag |
| `cookies[].secure` | boolean | No | — | Secure flag |
| `cookies[].sameSite` | `"Strict"` \| `"Lax"` \| `"None"` | No | — | SameSite attribute |
| `cookies[].partitionKey` | string | No | — | CHIPS partition key (top-level site) |

**Returns:** `Promise<void>`

```js
await context.addCookies([{
  name: 'session',
  value: 'abc123',
  domain: 'example.com',
  path: '/',
  httpOnly: true,
  secure: true,
}]);
```

---

### browserContext.addInitScript(script[, arg])

```ts
await browserContext.addInitScript(script[, arg]): Promise<Disposable>
```

Adds a script that is executed in every frame of every page of this context before the page script. It is also re-executed after navigations.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `script` | Function \| string \| Object | Yes | — | Function, script string or `{ path?, content? }` |
| `script.path` | string | No | — | Path to the script file (relative to cwd) |
| `script.content` | string | No | — | Script content as a string |
| `arg` | Serializable | No | — | Argument passed to the function (only for functions) |

**Returns:** `Promise<Disposable>` — calling `.dispose()` removes the script

```js
// Override Math.random for all pages
await context.addInitScript(() => {
  Math.random = () => 0.42;
});

// With an argument
await context.addInitScript(({ seed }) => {
  Math.random = () => seed;
}, { seed: 0.5 });
```

---

### browserContext.browser()

```ts
browserContext.browser(): Browser | null
```

Returns the `Browser` that owns this context. Returns `null` for the persistent context (from `launchPersistentContext()`).

**Returns:** `Browser | null`

---

### browserContext.clearCookies([options])

```ts
await browserContext.clearCookies([options]): Promise<void>
```

Deletes the context's cookies, optionally filtered.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.domain` | string \| RegExp | No | — | Only delete cookies of this domain |
| `options.name` | string \| RegExp | No | — | Only cookies with this name |
| `options.path` | string \| RegExp | No | — | Only cookies with this path |

**Returns:** `Promise<void>`

```js
await context.clearCookies(); // delete all
await context.clearCookies({ name: /session.*/ }); // filtered
```

---

### browserContext.clearPermissions()

```ts
await browserContext.clearPermissions(): Promise<void>
```

Revokes all previously granted permissions.

**Returns:** `Promise<void>`

---

### browserContext.close([options])

```ts
await browserContext.close([options]): Promise<void>
```

Closes the context and all pages it contains. The default BrowserContext cannot be closed.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.reason` | string | No | — | Reason reported to interrupted operations |

**Returns:** `Promise<void>`

---

### browserContext.cookies([urls])

```ts
await browserContext.cookies([urls]): Promise<Array<Cookie>>
```

Returns the context's cookies, optionally filtered by URLs.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `urls` | string \| Array<string> | No | — | URL(s) to filter by |

**Returns:** `Promise<Array<Cookie>>` with fields: `name`, `value`, `domain`, `path` (strings), `expires` (number), `httpOnly`, `secure` (booleans), `sameSite` (`"Strict"` \| `"Lax"` \| `"None"`), `partitionKey?` (string)

```js
const cookies = await context.cookies('https://example.com');
```

---

### browserContext.exposeBinding(name, callback[, options])

```ts
await browserContext.exposeBinding(name, callback[, options]): Promise<Disposable>
```

Exposes a function under `window[name]` in all frames of all pages. The callback runs in the Playwright process and receives a source object `{ browserContext, page, frame }` as its first argument.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Function name on the `window` object |
| `callback` | Function | Yes | — | Callback function; the first argument is `{ browserContext, page, frame }` |
| `options.handle` | boolean | No | false | If `true`, the callback receives a JSHandle instead of the deserialized value |

**Returns:** `Promise<Disposable>`

```js
await context.exposeBinding('pageURL', ({ page }) => page.url());
// In the browser: const url = await window.pageURL();
```

---

### browserContext.exposeFunction(name, callback)

```ts
await browserContext.exposeFunction(name, callback): Promise<Disposable>
```

Exposes a function under `window[name]` (without a source argument, a simpler variant of `exposeBinding`).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Function name |
| `callback` | Function | Yes | — | Called with the arguments of the browser-side call |

**Returns:** `Promise<Disposable>`

```js
const crypto = require('crypto');
await context.exposeFunction('sha256', (text) =>
  crypto.createHash('sha256').update(text).digest('hex')
);
// In the browser: const hash = await window.sha256('hello');
```

---

### browserContext.grantPermissions(permissions[, options])

```ts
await browserContext.grantPermissions(permissions[, options]): Promise<void>
```

Grants permissions for the context (optionally restricted to one origin).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `permissions` | Array<string> | Yes | — | Permissions to grant |
| `options.origin` | string | No | — | Grant only for this origin |

**Possible permissions:** `"accelerometer"`, `"ambient-light-sensor"`, `"background-sync"`, `"camera"`, `"clipboard-read"`, `"clipboard-write"`, `"geolocation"`, `"gyroscope"`, `"local-fonts"`, `"local-network-access"`, `"magnetometer"`, `"microphone"`, `"midi"`, `"midi-sysex"`, `"notifications"`, `"payment-handler"`, `"storage-access"`, `"screen-wake-lock"`

**Returns:** `Promise<void>`

```js
await context.grantPermissions(['geolocation'], { origin: 'https://example.com' });
```

---

### browserContext.isClosed()

```ts
browserContext.isClosed(): boolean
```

Returns `true` if the context has been closed.

**Returns:** `boolean`

---

### browserContext.newCDPSession(page)

```ts
await browserContext.newCDPSession(page): Promise<CDPSession>
```

Creates a new CDP session for a page or a frame. **Chromium only.**

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `page` | Page \| Frame | Yes | — | Target of the CDP session |

**Returns:** `Promise<CDPSession>`

---

### browserContext.newPage()

```ts
await browserContext.newPage(): Promise<Page>
```

Creates a new page in this context.

**Returns:** `Promise<Page>`

---

### browserContext.pages()

```ts
browserContext.pages(): Array<Page>
```

Returns all open pages in this context.

**Returns:** `Array<Page>`

---

### browserContext.removeAllListeners([type, options])

```ts
await browserContext.removeAllListeners([type, options]): Promise<void>
```

Removes event listeners.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `type` | string | No | — | Event type |
| `options.behavior` | `"wait"` \| `"ignoreErrors"` \| `"default"` | No | `"default"` | How to handle running handlers |

**Returns:** `Promise<void>`

---

### browserContext.route(url, handler[, options])

```ts
await browserContext.route(url, handler[, options]): Promise<Disposable>
```

Registers a network handler for all pages in this context. The handler is called for every request matching `url`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| URLPattern \| Function(URL):boolean | Yes | — | URL pattern or predicate |
| `handler` | Function(Route, Request) | Yes | — | Handler function; must call `route.fulfill()`, `route.continue()`, `route.abort()` or `route.fallback()` |
| `options.times` | number | No | — | How many times the handler is applied (removed afterwards) |

**Returns:** `Promise<Disposable>`

```js
// Block all images
await context.route('**/*.{png,jpg,jpeg}', route => route.abort());

// Mock API requests
await context.route(/api\/users/, async route => {
  await route.fulfill({ json: [{ id: 1, name: 'Alice' }] });
});
```

---

### browserContext.routeFromHAR(har[, options])

```ts
await browserContext.routeFromHAR(har[, options]): Promise<void>
```

Serves network requests from a HAR file (HTTP Archive).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `har` | string | Yes | — | Path to the HAR file |
| `options.notFound` | `"abort"` \| `"fallback"` | No | `"abort"` | Behavior for unmatched requests |
| `options.update` | boolean | No | false | Update the HAR with real data |
| `options.updateContent` | `"embed"` \| `"attach"` | No | — | Content storage mode when updating |
| `options.updateMode` | `"full"` \| `"minimal"` | No | `"minimal"` | Update scope |
| `options.url` | string \| RegExp | No | — | Serve only requests matching this pattern from the HAR |

**Returns:** `Promise<void>`

```js
await context.routeFromHAR('fixtures/api.har', {
  url: /api\//,
  notFound: 'fallback',
});
```

---

### browserContext.routeWebSocket(url, handler)

```ts
await browserContext.routeWebSocket(url, handler): Promise<void>
```

Registers a handler for WebSocket connections in all pages of this context.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| Function(URL):boolean | Yes | — | WebSocket URL pattern |
| `handler` | Function(WebSocketRoute) | Yes | — | Handler function |

**Returns:** `Promise<void>`

```js
await context.routeWebSocket(/ws\.example\.com/, ws => {
  ws.onMessage(msg => {
    ws.send('mocked response');
  });
});
```

---

### browserContext.serviceWorkers()

```ts
browserContext.serviceWorkers(): Array<Worker>
```

Returns all active service workers in this context. **Chromium only.**

**Returns:** `Array<Worker>`

---

### browserContext.setDefaultNavigationTimeout(timeout)

```ts
browserContext.setDefaultNavigationTimeout(timeout): void
```

Sets the default timeout for navigation operations (`goto`, `goBack`, `goForward`, `reload`, `setContent`, `waitForNavigation`).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `timeout` | number | Yes | — | Timeout in milliseconds |

---

### browserContext.setDefaultTimeout(timeout)

```ts
browserContext.setDefaultTimeout(timeout): void
```

Sets the default timeout for all operations (except navigation).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `timeout` | number | Yes | — | Timeout in milliseconds; `0` = no timeout |

---

### browserContext.setExtraHTTPHeaders(headers)

```ts
await browserContext.setExtraHTTPHeaders(headers): Promise<void>
```

Sets additional HTTP headers that are sent with every request of all pages.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `headers` | Object<string,string> | Yes | — | Header name/value pairs |

**Returns:** `Promise<void>`

```js
await context.setExtraHTTPHeaders({ 'X-Custom-Header': 'value' });
```

---

### browserContext.setGeolocation(geolocation)

```ts
await browserContext.setGeolocation(geolocation): Promise<void>
```

Sets or changes the geolocation emulation. Requires a prior `grantPermissions(['geolocation'])`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `geolocation` | Object \| null | Yes | — | `null` clears the emulation |
| `geolocation.latitude` | number | Yes | — | Latitude (-90 to 90) |
| `geolocation.longitude` | number | Yes | — | Longitude (-180 to 180) |
| `geolocation.accuracy` | number | No | 0 | Accuracy in meters (>= 0) |

**Returns:** `Promise<void>`

```js
await context.grantPermissions(['geolocation']);
await context.setGeolocation({ latitude: 52.52, longitude: 13.405 });
```

---

### browserContext.setOffline(offline)

```ts
await browserContext.setOffline(offline): Promise<void>
```

Enables or disables offline network emulation.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `offline` | boolean | Yes | — | `true` = emulate offline |

**Returns:** `Promise<void>`

---

### browserContext.setStorageState(storageState)

```ts
await browserContext.setStorageState(storageState): Promise<void>
```

Sets the context's cookies and LocalStorage (clearing any previously existing data).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `storageState` | string \| Object | Yes | — | File path or state object with `cookies` and `origins` |

**Returns:** `Promise<void>`

---

### browserContext.storageState([options])

```ts
await browserContext.storageState([options]): Promise<StorageState>
```

Returns the current storage state (cookies + LocalStorage) as a serializable object.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.indexedDB` | boolean | No | false | Include an IndexedDB snapshot |
| `options.path` | string | No | — | File path to save to |

**Returns:** `Promise<StorageState>` with the fields `cookies` (array) and `origins` (array containing `localStorage`)

```js
// Save after logging in
await page.locator('#login').click();
await context.storageState({ path: 'auth.json' });
```

---

### browserContext.unroute(url[, handler])

```ts
await browserContext.unroute(url[, handler]): Promise<void>
```

Removes a previously registered route handler.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| URLPattern \| Function | Yes | — | URL pattern to remove |
| `handler` | Function | No | — | Remove a specific handler (otherwise all for `url`) |

**Returns:** `Promise<void>`

---

### browserContext.unrouteAll([options])

```ts
await browserContext.unrouteAll([options]): Promise<void>
```

Removes all route handlers.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.behavior` | `"wait"` \| `"ignoreErrors"` \| `"default"` | No | `"default"` | How to handle running handlers |

**Returns:** `Promise<void>`

---

### browserContext.waitForEvent(event[, optionsOrPredicate])

```ts
await browserContext.waitForEvent(event[, optionsOrPredicate]): Promise<Object>
```

Waits for an event and returns its data.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `event` | string | Yes | — | Event name (e.g. `"page"`, `"request"`) |
| `optionsOrPredicate` | Function \| Object | No | — | Predicate or options object |
| `optionsOrPredicate.predicate` | Function | No | — | Returns `true` if the event should be accepted |
| `optionsOrPredicate.timeout` | number | No | 30000 | Timeout in milliseconds |

**Returns:** `Promise<Object>` — event data

```js
const pagePromise = context.waitForEvent('page');
await page.locator('a[target=_blank]').click();
const newPage = await pagePromise;
```

---

## Properties

### browserContext.clock

**Type:** `Clock`

Allows controlling time (mock clock). Enables fast-forwarding timers, dates and intervals.

```js
await context.clock.setFixedTime(new Date('2024-01-01'));
```

---

### browserContext.debugger

**Type:** `Debugger`

Allows pausing and resuming execution while debugging.

---

### browserContext.request

**Type:** `APIRequestContext`

API testing helper that shares the context's cookies. Used for HTTP requests outside the browser.

```js
const response = await context.request.get('https://api.example.com/users');
```

---

### browserContext.tracing

**Type:** `Tracing`

Playwright tracing support for this context.

```js
await context.tracing.start({ screenshots: true, snapshots: true });
// ... run the test ...
await context.tracing.stop({ path: 'trace.zip' });
```

---

## Events

### event: 'close'

Emitted when the context is closed.

**Event data:** `BrowserContext`

---

### event: 'console'

Emitted when `console.log()`, `console.error()` or similar is called in a page.

**Event data:** `ConsoleMessage`

```js
context.on('console', msg => console.log(msg.text()));
```

---

### event: 'dialog'

Emitted when a JavaScript dialog appears (`alert`, `prompt`, `confirm`, `beforeunload`). The dialog must be handled with `dialog.accept()` or `dialog.dismiss()`.

**Event data:** `Dialog`

---

### event: 'download'

Emitted when a file download starts in a page of the context.

**Event data:** `Download`

---

### event: 'frameattached'

Emitted when a frame is added in a page of the context.

**Event data:** `Frame`

---

### event: 'framedetached'

Emitted when a frame is removed from a page of the context.

**Event data:** `Frame`

---

### event: 'framenavigated'

Emitted when a frame navigates to a new URL.

**Event data:** `Frame`

---

### event: 'page'

Emitted when a new page is created in the context (e.g. by a popup or `context.newPage()`).

**Event data:** `Page`

```js
context.on('page', async page => {
  await page.waitForLoadState();
  console.log(page.url());
});
```

---

### event: 'pageclose'

Emitted when a page in the context is closed.

**Event data:** `Page`

---

### event: 'pageload'

Emitted when the JavaScript `load` event of a page in the context is dispatched.

**Event data:** `Page`

---

### event: 'request'

Emitted when a network request is initiated by a page of the context.

**Event data:** `Request`

---

### event: 'requestfailed'

Emitted when a request fails (timeout, abort, or similar).

**Event data:** `Request`

---

### event: 'requestfinished'

Emitted when a request has completed (response fully downloaded).

**Event data:** `Request`

---

### event: 'response'

Emitted when the status code and headers of a response have been received.

**Event data:** `Response`

---

### event: 'serviceworker'

Emitted when a new service worker is registered in the context. **Chromium only.**

**Event data:** `Worker`

---

### event: 'weberror'

Emitted when an unhandled exception occurs in a page of the context.

**Event data:** `WebError` with `error()` and `page()`

```js
context.on('weberror', err => console.error(err.error().message));
```

---

## Deprecated

### browserContext.setHTTPCredentials(httpCredentials) [DEPRECATED]

Deprecated. Browsers cache credentials; create a new context with the `httpCredentials` option instead.

### backgroundPages() [DEPRECATED]

Deprecated (Chromium Manifest V3). Always returns an empty array.

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 25 |
| Properties | 4 |
| Events | 16 |

**Summary:** `BrowserContext` is the central isolation unit in Playwright. The most important features are network routing (`route`, `routeFromHAR`), cookie/storage management (`addCookies`, `storageState`, `setStorageState`) and permissions (`grantPermissions`). For end-to-end authentication flows, `storageState()` is indispensable.

---

Source: https://playwright.dev/docs/api/class-browsercontext
