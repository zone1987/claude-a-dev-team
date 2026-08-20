# class-websocket

`WebSocket` represents a WebSocket connection opened by a page. Instances are obtained through the `page.on('websocket')` event. The object is read-only and allows observing WebSocket messages.

For actively mocking/intercepting WebSocket connections: use `page.routeWebSocket()` (returns `WebSocketRoute`).

Methods: 3 | Properties: 0 | Events: 4

---

## Contents

- [Methods](#methods)
- [Events](#events)
- [Complete observing example](#complete-observing-example)
- [Manifest](#manifest)

## Methods

### webSocket.isClosed()

```ts
webSocket.isClosed(): boolean
```

Returns `true` when the WebSocket connection has been closed.

**Returns:** `boolean`

```js
if (webSocket.isClosed()) {
  console.log('WebSocket is closed');
}
```

---

### webSocket.url()

```ts
webSocket.url(): string
```

Returns the URL of the WebSocket server.

**Returns:** `string`

```js
console.log('WebSocket URL:', webSocket.url());
// e.g. "wss://example.com/socket"
```

---

### webSocket.waitForEvent(event[, optionsOrPredicate])

```ts
await webSocket.waitForEvent(event[, optionsOrPredicate]): Promise<Object>
```

Waits for an event and returns its data. Useful for handling WebSocket events synchronously in tests.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `event` | string | Yes | — | Event name (`"framereceived"`, `"framesent"`, `"close"`, `"socketerror"`) |
| `optionsOrPredicate` | Function \| Object | No | — | Predicate function or options object |
| `optionsOrPredicate.predicate` | Function | No | — | Evaluates event data; keeps waiting when `false` |
| `optionsOrPredicate.timeout` | number | No | 0 | Timeout in ms; `0` = no timeout |

**Returns:** `Promise<Object>` — event data

```js
// Wait for a specific message
const wsPromise = page.waitForEvent('websocket');
await page.goto('/chat');
const ws = await wsPromise;

const { payload } = await ws.waitForEvent('framereceived', {
  predicate: ({ payload }) => payload.includes('connected'),
  timeout: 5000,
});
console.log('Received:', payload);
```

---

## Events

### event: 'close'

Fired when the WebSocket connection is closed.

**Event data:** `WebSocket` — the WebSocket instance itself

```js
ws.on('close', (ws) => {
  console.log('WebSocket closed:', ws.url());
});
```

---

### event: 'framereceived'

Fired when the WebSocket receives an incoming message.

**Event data:** object with:

| Field | Type | Description |
|-------|------|-------------|
| `payload` | string \| Buffer | Message content; string for text frames, buffer for binary frames |

```js
ws.on('framereceived', ({ payload }) => {
  if (typeof payload === 'string') {
    const data = JSON.parse(payload);
    console.log('Received:', data);
  }
});
```

---

### event: 'framesent'

Fired when the WebSocket sends an outgoing message.

**Event data:** object with:

| Field | Type | Description |
|-------|------|-------------|
| `payload` | string \| Buffer | Sent message content |

```js
ws.on('framesent', ({ payload }) => {
  console.log('Sent:', payload);
});
```

---

### event: 'socketerror'

Fired when an error occurs in the WebSocket.

**Event data:** `string` — error message

```js
ws.on('socketerror', (error) => {
  console.error('WebSocket error:', error);
});
```

---

## Complete observing example

```js
test('observe WebSocket communication', async ({ page }) => {
  const messages = [];

  // Intercept the WebSocket
  page.on('websocket', ws => {
    console.log('WebSocket opened:', ws.url());

    ws.on('framereceived', ({ payload }) => {
      messages.push({ direction: 'in', payload });
    });
    ws.on('framesent', ({ payload }) => {
      messages.push({ direction: 'out', payload });
    });
    ws.on('socketerror', error => {
      console.error('WS Error:', error);
    });
    ws.on('close', () => {
      console.log('WS closed. Messages:', messages.length);
    });
  });

  await page.goto('/chat');
  await page.locator('#message').fill('Hello');
  await page.locator('#send').click();

  // Wait for the answer
  const ws = await page.waitForEvent('websocket');
  await ws.waitForEvent('framereceived', {
    predicate: ({ payload }) => payload.includes('echo'),
  });

  expect(messages).toHaveLength(2); // sent + received
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 3 |
| Properties | 0 |
| Events | 4 |

**Summary:** `WebSocket` is a read-only observer for WebSocket connections. The events `framereceived` and `framesent` are the core tools for monitoring. For actively intercepting and modifying WebSocket connections, `WebSocketRoute` (via `page.routeWebSocket()`) must be used.

---

Source: https://playwright.dev/docs/api/class-websocket
