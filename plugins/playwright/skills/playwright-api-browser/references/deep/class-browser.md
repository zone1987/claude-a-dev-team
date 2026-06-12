# class-browser

Playwright `Browser` represents a browser instance launched via `BrowserType.launch()` or connected via `BrowserType.connect()`. A single `Browser` may own multiple `BrowserContext` instances.

Methoden: 12 | Properties: 0 | Events: 2

---

## Methods

### browser.browserType()

```ts
browser.browserType(): BrowserType
```

Returns the `BrowserType` object this browser belongs to (`chromium`, `firefox`, or `webkit`).

**Returns:** `BrowserType`

```js
const type = browser.browserType();
console.log(type.name()); // "chromium"
```

---

### browser.close([options])

```ts
await browser.close([options])
```

Closes the browser and all associated pages and contexts. Equivalent to a force-quit.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | Options object |
| `options.reason` | string | No | — | Human-readable reason reported to interrupted operations |

**Returns:** `Promise<void>`

```js
await browser.close();
await browser.close({ reason: 'Test finished' });
```

---

### browser.contexts()

```ts
browser.contexts(): Array<BrowserContext>
```

Returns an array of all open browser contexts.

**Returns:** `Array<BrowserContext>`

```js
const contexts = browser.contexts();
console.log(contexts.length); // number of open contexts
```

---

### browser.isConnected()

```ts
browser.isConnected(): boolean
```

Indicates whether the browser is still connected to the Playwright process.

**Returns:** `boolean`

```js
if (!browser.isConnected()) {
  console.log('Browser disconnected');
}
```

---

### browser.newBrowserCDPSession()

```ts
await browser.newBrowserCDPSession(): Promise<CDPSession>
```

Creates a new CDP (Chrome DevTools Protocol) session attached to the browser itself (not a page). **Chromium-based browsers only.**

**Returns:** `Promise<CDPSession>`

```js
const session = await browser.newBrowserCDPSession();
const { browserContextIds } = await session.send('Target.getBrowserContexts');
```

---

### browser.newContext([options])

```ts
await browser.newContext([options]): Promise<BrowserContext>
```

Creates a new isolated browser context. Each context has its own cookies, storage, and network state.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | Context configuration |
| `options.acceptDownloads` | boolean | No | true | Whether to auto-accept file downloads |
| `options.baseURL` | string | No | — | Base URL for relative navigations via `page.goto('/')` |
| `options.bypassCSP` | boolean | No | false | Bypass Content Security Policy |
| `options.clientCertificates` | Array<Object> | No | — | TLS client certificates (origin, certPath/cert, keyPath/key, pfxPath/pfx, passphrase) |
| `options.colorScheme` | `"light"` \| `"dark"` \| `"no-preference"` \| `null` | No | `"light"` | Emulates `prefers-color-scheme` media feature |
| `options.contrast` | `"no-preference"` \| `"more"` \| `null` | No | — | Emulates `prefers-contrast` |
| `options.deviceScaleFactor` | number | No | 1 | Device pixel ratio (DPR) |
| `options.extraHTTPHeaders` | Object<string,string> | No | — | Additional HTTP headers sent with every request |
| `options.forcedColors` | `"active"` \| `"none"` \| `null` | No | — | Emulates `forced-colors` CSS media feature |
| `options.geolocation` | Object | No | — | `{ latitude, longitude, accuracy? }` |
| `options.hasTouch` | boolean | No | false | Enables touch event simulation |
| `options.httpCredentials` | Object | No | — | HTTP Basic/Digest auth: `{ username, password, origin?, send? }` |
| `options.ignoreHTTPSErrors` | boolean | No | false | Ignore TLS/SSL certificate errors |
| `options.isMobile` | boolean | No | false | Enables mobile viewport and meta viewport tag |
| `options.javaScriptEnabled` | boolean | No | true | Enable/disable JavaScript execution |
| `options.locale` | string | No | — | User locale, e.g. `"en-GB"`, `"de-DE"` |
| `options.offline` | boolean | No | false | Simulate offline network |
| `options.permissions` | Array<string> | No | — | Permissions to grant (e.g. `["geolocation", "camera"]`) |
| `options.proxy` | Object | No | — | Proxy config: `{ server, bypass?, username?, password? }` |
| `options.recordHar` | Object | No | — | HAR recording: `{ path, omitContent?, content?, mode?, urlFilter? }` |
| `options.recordVideo` | Object | No | — | Video recording: `{ dir, size?, showActions? }` |
| `options.reducedMotion` | `"reduce"` \| `"no-preference"` \| `null` | No | — | Emulates `prefers-reduced-motion` |
| `options.screen` | Object | No | — | Screen dimensions: `{ width, height }` |
| `options.serviceWorkers` | `"allow"` \| `"block"` | No | `"allow"` | Whether to allow service workers |
| `options.storageState` | string \| Object | No | — | Pre-populate cookies/localStorage from file path or state object |
| `options.strictSelectors` | boolean | No | false | Throw when a selector matches multiple elements |
| `options.timezoneId` | string | No | — | ICU timezone ID, e.g. `"America/New_York"` |
| `options.userAgent` | string | No | — | Custom User-Agent string |
| `options.viewport` | Object \| `null` | No | `{width:1280,height:720}` | Viewport size; `null` disables viewport emulation |

**Returns:** `Promise<BrowserContext>`

```js
const context = await browser.newContext({
  baseURL: 'https://example.com',
  storageState: 'auth.json',
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
});
```

---

### browser.newPage([options])

```ts
await browser.newPage([options]): Promise<Page>
```

Convenience method: creates a new `BrowserContext` and opens a new `Page` in it. Accepts the same options as `browser.newContext()`. The context is closed when the page is closed.

**Returns:** `Promise<Page>`

```js
const page = await browser.newPage({ locale: 'en-US' });
await page.goto('https://example.com');
```

---

### browser.removeAllListeners([type, options])

```ts
await browser.removeAllListeners([type, options]): Promise<void>
```

Removes event listeners. Without `type`, removes all listeners.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `type` | string | No | — | Event type to remove listeners for |
| `options` | Object | No | — | |
| `options.behavior` | `"wait"` \| `"ignoreErrors"` \| `"default"` | No | `"default"` | How to handle in-flight handlers |

**Returns:** `Promise<void>`

---

### browser.startTracing([page, options])

```ts
await browser.startTracing([page, options]): Promise<void>
```

Starts Chromium tracing (low-level performance tracing, not Playwright Trace). **Chromium only.**

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `page` | Page | No | — | If provided, screenshots are captured for this page |
| `options` | Object | No | — | |
| `options.categories` | Array<string> | No | — | Custom trace event categories |
| `options.path` | string | No | — | File path to save the trace |
| `options.screenshots` | boolean | No | false | Capture screenshots during tracing |

**Returns:** `Promise<void>`

```js
await browser.startTracing(page, { path: 'trace.json', screenshots: true });
```

---

### browser.stopTracing()

```ts
await browser.stopTracing(): Promise<Buffer>
```

Stops Chromium tracing and returns the trace data as a `Buffer`. **Chromium only.**

**Returns:** `Promise<Buffer>`

```js
const buffer = await browser.stopTracing();
require('fs').writeFileSync('trace.json', buffer);
```

---

### browser.version()

```ts
browser.version(): string
```

Returns the browser version string.

**Returns:** `string`

```js
console.log(browser.version()); // e.g. "119.0.6045.105"
```

---

### browser.bind(title[, options])

```ts
await browser.bind(title[, options]): Promise<{endpoint: string}>
```

Creates a WebSocket server binding for the browser. Used for advanced remote control scenarios.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `title` | string | Yes | — | Identifier title for the binding |
| `options.host` | string | No | — | Host for the WebSocket server |
| `options.port` | number | No | 0 | Port (0 = OS-assigned) |
| `options.metadata` | Object | No | — | Additional metadata |
| `options.workspaceDir` | string | No | — | Working directory |

**Returns:** `Promise<{endpoint: string}>`

---

### browser.unbind()

```ts
await browser.unbind(): Promise<void>
```

Removes a binding created with `browser.bind()`.

**Returns:** `Promise<void>`

---

## Events

### event: 'disconnected'

Emitted when the browser is disconnected from the Playwright process. This happens when the browser crashes, is closed via `browser.close()`, or the remote connection drops.

**Event data:** `Browser` instance

```js
browser.on('disconnected', (browser) => {
  console.log('Browser disconnected');
});
```

---

### event: 'context'

Emitted when a new `BrowserContext` is created inside this browser.

**Event data:** `BrowserContext` instance

```js
browser.on('context', (context) => {
  console.log('New context created');
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 12 |
| Events | 2 |

**Fazit:** `Browser` ist der Einstiegspunkt fuer alle Kontexte und Seiten. Die wichtigsten Methoden sind `newContext()` (mit umfangreichen Emulations-Optionen), `newPage()` (Convenience-Wrapper) und `close()`. CDP-Zugriff und Chromium-Tracing sind als Low-Level-Erweiterungen verfuegbar.

---

Source: https://playwright.dev/docs/api/class-browser
