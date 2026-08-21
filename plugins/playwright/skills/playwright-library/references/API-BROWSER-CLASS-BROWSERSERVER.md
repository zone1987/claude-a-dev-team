# class-browserserver

`BrowserServer` represents a running browser server instance that was started via `browserType.launchServer()`. Clients can connect using `browserType.connect(wsEndpoint)`.

Methods: 4 | Properties: 0 | Events: 1

---

## Contents

- [Methods](#methods)
- [Events](#events)
- [Typical Usage Pattern](#typical-usage-pattern)
- [Manifest](#manifest)

## Methods

### browserServer.close()

```ts
await browserServer.close(): Promise<void>
```

Closes the browser server gracefully and waits until the process has terminated.

**Returns:** `Promise<void>`

```js
await browserServer.close();
```

---

### browserServer.kill()

```ts
await browserServer.kill(): Promise<void>
```

Terminates the browser process immediately (kill) and waits until the process has terminated. Unlike `close()`, without a graceful shutdown.

**Returns:** `Promise<void>`

```js
await browserServer.kill();
```

---

### browserServer.process()

```ts
browserServer.process(): ChildProcess
```

Returns the Node.js `ChildProcess` of the launched browser process.

**Returns:** `ChildProcess`

```js
const proc = browserServer.process();
console.log('PID:', proc.pid);
proc.stderr.pipe(process.stderr);
```

---

### browserServer.wsEndpoint()

```ts
browserServer.wsEndpoint(): string
```

Returns the WebSocket endpoint that can be used as the argument for `browserType.connect()`.

**Returns:** `string` — WebSocket URL

```js
const endpoint = browserServer.wsEndpoint();
// e.g. "ws://localhost:9222/secret-token"

// Another process connects:
const browser = await chromium.connect(endpoint);
```

---

## Events

### event: 'close'

Emitted when the browser server is closed.

**Event data:** no data

```js
browserServer.on('close', () => {
  console.log('BrowserServer closed');
});
```

---

## Typical Usage Pattern

```js
// Server process:
const { chromium } = require('playwright');
const server = await chromium.launchServer({
  port: 9222,
  wsPath: 'my-secret-token',
});
console.log('Endpoint:', server.wsEndpoint());
// Pass the endpoint securely to the client...

// Client process:
const browser = await chromium.connect('ws://localhost:9222/my-secret-token');
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();

// Shut down the server:
await server.close();
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 4 |
| Properties | 0 |
| Events | 1 |

**Summary:** `BrowserServer` is a lightweight handle for remote browser instances. `wsEndpoint()` is the crucial method for passing the connection point to clients. For production setups, `wsPath` should contain an unpredictable token to prevent unauthorized access.

---

Source: https://playwright.dev/docs/api/class-browserserver
