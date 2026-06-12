# class-websocket

`WebSocket` repraesentiert eine WebSocket-Verbindung, die von einer Page geoeffnet wurde. Instanzen werden ueber das `page.on('websocket')` Event erhalten. Das Objekt ist read-only und erlaubt das Beobachten von WebSocket-Nachrichten.

Fuer aktives Mocken/Intercepten von WebSocket-Verbindungen: `page.routeWebSocket()` verwenden (liefert `WebSocketRoute`).

Methoden: 3 | Properties: 0 | Events: 4

---

## Methods

### webSocket.isClosed()

```ts
webSocket.isClosed(): boolean
```

Gibt `true` zurueck wenn die WebSocket-Verbindung geschlossen wurde.

**Returns:** `boolean`

```js
if (webSocket.isClosed()) {
  console.log('WebSocket ist geschlossen');
}
```

---

### webSocket.url()

```ts
webSocket.url(): string
```

Gibt die URL des WebSocket-Servers zurueck.

**Returns:** `string`

```js
console.log('WebSocket URL:', webSocket.url());
// z.B. "wss://example.com/socket"
```

---

### webSocket.waitForEvent(event[, optionsOrPredicate])

```ts
await webSocket.waitForEvent(event[, optionsOrPredicate]): Promise<Object>
```

Wartet auf ein Event und gibt dessen Daten zurueck. Nuetzlich fuer die synchrone Behandlung von WebSocket-Ereignissen in Tests.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `event` | string | Yes | — | Event-Name (`"framereceived"`, `"framesent"`, `"close"`, `"socketerror"`) |
| `optionsOrPredicate` | Function \| Object | No | — | Praedikat-Funktion oder Options-Objekt |
| `optionsOrPredicate.predicate` | Function | No | — | Evaluiert Event-Daten; wartet weiter wenn `false` |
| `optionsOrPredicate.timeout` | number | No | 0 | Timeout in ms; `0` = kein Timeout |

**Returns:** `Promise<Object>` — Event-Daten

```js
// Auf spezifische Nachricht warten
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

Wird ausgeloest wenn die WebSocket-Verbindung geschlossen wird.

**Event data:** `WebSocket` — die WebSocket-Instanz selbst

```js
ws.on('close', (ws) => {
  console.log('WebSocket geschlossen:', ws.url());
});
```

---

### event: 'framereceived'

Wird ausgeloest wenn der WebSocket eine eingehende Nachricht empfaengt.

**Event data:** Object mit:

| Field | Type | Description |
|-------|------|-------------|
| `payload` | string \| Buffer | Nachrichteninhalt; String fuer Text-Frames, Buffer fuer Binaer-Frames |

```js
ws.on('framereceived', ({ payload }) => {
  if (typeof payload === 'string') {
    const data = JSON.parse(payload);
    console.log('Empfangen:', data);
  }
});
```

---

### event: 'framesent'

Wird ausgeloest wenn der WebSocket eine ausgehende Nachricht sendet.

**Event data:** Object mit:

| Field | Type | Description |
|-------|------|-------------|
| `payload` | string \| Buffer | Gesendeter Nachrichteninhalt |

```js
ws.on('framesent', ({ payload }) => {
  console.log('Gesendet:', payload);
});
```

---

### event: 'socketerror'

Wird ausgeloest wenn ein Fehler im WebSocket auftritt.

**Event data:** `string` — Fehlermeldung

```js
ws.on('socketerror', (error) => {
  console.error('WebSocket-Fehler:', error);
});
```

---

## Vollstaendiges Observing-Beispiel

```js
test('WebSocket-Kommunikation beobachten', async ({ page }) => {
  const messages = [];

  // WebSocket abfangen
  page.on('websocket', ws => {
    console.log('WebSocket geoeffnet:', ws.url());

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

  // Auf Antwort warten
  const ws = await page.waitForEvent('websocket');
  await ws.waitForEvent('framereceived', {
    predicate: ({ payload }) => payload.includes('echo'),
  });

  expect(messages).toHaveLength(2); // gesendet + empfangen
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 3 |
| Properties | 0 |
| Events | 4 |

**Fazit:** `WebSocket` ist ein read-only Beobachter fuer WebSocket-Verbindungen. Die Events `framereceived` und `framesent` sind die Kern-Werkzeuge fuer das Monitoring. Fuer aktives Intercepten und Modifizieren von WebSocket-Verbindungen muss `WebSocketRoute` (via `page.routeWebSocket()`) verwendet werden.

---

Source: https://playwright.dev/docs/api/class-websocket
