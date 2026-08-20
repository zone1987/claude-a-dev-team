# class-websocketroute

`WebSocketRoute` allows actively intercepting, modifying and mocking WebSocket connections. Instances are passed as parameters to handlers registered via `page.routeWebSocket()` or `browserContext.routeWebSocket()`.

Every `WebSocketRoute` instance represents the **page side** (browser side). When `connectToServer()` is called, a second instance is created for the **server side**.

Methods: 6 | Properties: 0 | Events: 0

---

## Contents

- [Methods](#methods)
- [Usage patterns](#usage-patterns)
- [Manifest](#manifest)

## Methods

### webSocketRoute.close([options])

```ts
webSocketRoute.close([options]): Promise<void>
```

Closes one side of the WebSocket connection (page side or server side, depending on which instance it is called on).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.code` | number | No | — | Close code according to the WebSocket standard (e.g. 1000 = normal closure, 1001 = going away) |
| `options.reason` | string | No | — | Reason for closing, as a string |

**Returns:** `Promise<void>`

```js
await page.routeWebSocket('**/ws', ws => {
  // Close the connection immediately
  ws.close({ code: 1001, reason: 'Maintenance' });
});
```

---

### webSocketRoute.connectToServer()

```ts
webSocketRoute.connectToServer(): WebSocketRoute
```

Connects to the real WebSocket server. Returns a new `WebSocketRoute` instance representing the **server side**.

When this method is called, messages are forwarded automatically between page and server, unless `onMessage()` handlers are registered for interception.

**Returns:** `WebSocketRoute` — server-side route instance

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();

  // Intercept messages from the page to the server
  ws.onMessage(msg => {
    console.log('Page -> Server:', msg);
    server.send(msg); // forward manually
  });

  // Intercept messages from the server to the page
  server.onMessage(msg => {
    const data = JSON.parse(msg);
    data.modified = true; // modify
    ws.send(JSON.stringify(data)); // send to the page
  });
});
```

---

### webSocketRoute.onClose(handler)

```ts
webSocketRoute.onClose(handler): void
```

Registers a handler for the closing of the WebSocket connection. When a handler is set, the default forwarding behavior for close events is disabled.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `handler` | Function | Yes | — | Receives an optional close code (number) and reason (string) |

**Returns:** `void`

```js
ws.onClose((code, reason) => {
  console.log(`Closed: code=${code}, reason=${reason}`);
  // Close the server side manually if needed:
  // serverWs.close({ code, reason });
});
```

---

### webSocketRoute.onMessage(handler)

```ts
webSocketRoute.onMessage(handler): void
```

Registers a handler for incoming messages. Disables automatic forwarding of messages — the handler itself must decide whether and how the message is forwarded.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `handler` | Function | Yes | — | Receives the message as a `string` (text frame) or `Buffer` (binary frame) |

**Returns:** `void`

```js
// On the page-side route: messages from the page
ws.onMessage(msg => {
  const data = JSON.parse(msg);
  if (data.type === 'ping') {
    ws.send(JSON.stringify({ type: 'pong' })); // direct answer
  } else {
    server.send(msg); // forward
  }
});

// On the server-side route: messages from the server
server.onMessage(msg => {
  ws.send(msg); // unmodified to the page
});
```

---

### webSocketRoute.protocols()

```ts
webSocketRoute.protocols(): Array<string>
```

Returns the requested WebSocket subprotocols (corresponds to the `Sec-WebSocket-Protocol` header).

**Returns:** `Array<string>` — empty array when no protocols are requested

```js
const protocols = ws.protocols();
if (protocols.includes('chat.v2')) {
  // v2 protocol handling
} else {
  // fall back to v1
}
```

---

### webSocketRoute.send(message)

```ts
webSocketRoute.send(message): void
```

Sends a message over the WebSocket connection. On the **page-side** route: the message is sent to the page. On the **server-side** route: the message is sent to the real server.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `message` | string \| Buffer | Yes | — | Message to send; string for a text frame, buffer for a binary frame |

**Returns:** `void`

```js
// Text message
ws.send(JSON.stringify({ type: 'update', data: { count: 42 } }));

// Binary message
ws.send(Buffer.from([0x01, 0x02, 0x03]));
```

---

### webSocketRoute.url()

```ts
webSocketRoute.url(): string
```

Returns the URL of the WebSocket that was created in the page.

**Returns:** `string`

```js
console.log('WebSocket URL:', ws.url());
```

---

## Usage patterns

### Pattern 1: Complete mocking (no real server)

```js
await page.routeWebSocket('**/ws', ws => {
  ws.onMessage(msg => {
    const { type, id } = JSON.parse(msg);
    if (type === 'subscribe') {
      ws.send(JSON.stringify({ type: 'subscribed', id }));
    }
  });
});
```

### Pattern 2: Transparent interception (real server)

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();
  // Without onMessage: automatic passthrough in both directions
});
```

### Pattern 3: Modify server messages

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();

  server.onMessage(msg => {
    const data = JSON.parse(msg);
    // Mask sensitive fields
    if (data.creditCard) {
      data.creditCard = '****';
    }
    ws.send(JSON.stringify(data));
  });
});
```

### Pattern 4: Simulate server push

```js
let wsRoute;
await page.routeWebSocket('**/ws', ws => {
  wsRoute = ws;
  ws.connectToServer();
});

await page.goto('/dashboard');

// Inject a message from the outside
await page.evaluate(() => {}); // make sure the WS is connected
wsRoute.send(JSON.stringify({ type: 'notification', message: 'New order!' }));
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 6 |
| Properties | 0 |
| Events | 0 |

**Summary:** `WebSocketRoute` is the powerful tool for WebSocket tests. `connectToServer()` activates transparent mode with optional interception via `onMessage()`. Without `connectToServer()`, the page is mocked completely — no real server is contacted. `send()` is the central method for injecting messages from the outside.

---

Source: https://playwright.dev/docs/api/class-websocketroute
