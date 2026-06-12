# class-websocketroute

`WebSocketRoute` ermoeglicht das aktive Intercepten, Modifizieren und Mocken von WebSocket-Verbindungen. Instanzen werden als Parameter an Handler uebergeben, die via `page.routeWebSocket()` oder `browserContext.routeWebSocket()` registriert wurden.

Jede `WebSocketRoute`-Instanz repraesentiert die **Seite der Page** (Browser-seitig). Wird `connectToServer()` aufgerufen, entsteht eine zweite Instanz fuer die **Server-Seite**.

Methoden: 6 | Properties: 0 | Events: 0

---

## Methods

### webSocketRoute.close([options])

```ts
webSocketRoute.close([options]): Promise<void>
```

Schliesst eine Seite der WebSocket-Verbindung (Page-seitig oder Server-seitig, je nachdem auf welcher Instanz aufgerufen).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.code` | number | No | — | Close-Code gemaess WebSocket-Standard (z.B. 1000 = normal closure, 1001 = going away) |
| `options.reason` | string | No | — | Schliessungsgrund als String |

**Returns:** `Promise<void>`

```js
await page.routeWebSocket('**/ws', ws => {
  // Verbindung sofort schliessen
  ws.close({ code: 1001, reason: 'Maintenance' });
});
```

---

### webSocketRoute.connectToServer()

```ts
webSocketRoute.connectToServer(): WebSocketRoute
```

Verbindet sich mit dem echten WebSocket-Server. Gibt eine neue `WebSocketRoute`-Instanz zurueck, die die **Server-Seite** repraesentiert.

Wenn diese Methode aufgerufen wird, werden Nachrichten automatisch zwischen Page und Server weitergeleitet, es sei denn, es werden `onMessage()`-Handler fuer Interception registriert.

**Returns:** `WebSocketRoute` — Server-seitige Route-Instanz

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();

  // Nachrichten von der Page zum Server intercepten
  ws.onMessage(msg => {
    console.log('Page -> Server:', msg);
    server.send(msg); // manuell weiterleiten
  });

  // Nachrichten vom Server zur Page intercepten
  server.onMessage(msg => {
    const data = JSON.parse(msg);
    data.modified = true; // modifizieren
    ws.send(JSON.stringify(data)); // an Page senden
  });
});
```

---

### webSocketRoute.onClose(handler)

```ts
webSocketRoute.onClose(handler): void
```

Registriert einen Handler fuer das Schliessen der WebSocket-Verbindung. Wenn ein Handler gesetzt wird, wird das Standard-Weiterleitungsverhalten fuer Close-Events deaktiviert.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `handler` | Function | Yes | — | Erhaelt optionalen Close-Code (number) und Reason (string) |

**Returns:** `void`

```js
ws.onClose((code, reason) => {
  console.log(`Geschlossen: Code=${code}, Reason=${reason}`);
  // Manuell auf Server-Seite schliessen wenn noetig:
  // serverWs.close({ code, reason });
});
```

---

### webSocketRoute.onMessage(handler)

```ts
webSocketRoute.onMessage(handler): void
```

Registriert einen Handler fuer eingehende Nachrichten. Deaktiviert das automatische Weiterleiten von Nachrichten — der Handler muss selbst entscheiden, ob und wie die Nachricht weitergeleitet wird.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `handler` | Function | Yes | — | Erhaelt die Nachricht als `string` (Text-Frame) oder `Buffer` (Binaer-Frame) |

**Returns:** `void`

```js
// Auf Page-seitiger Route: Nachrichten von der Page
ws.onMessage(msg => {
  const data = JSON.parse(msg);
  if (data.type === 'ping') {
    ws.send(JSON.stringify({ type: 'pong' })); // direkte Antwort
  } else {
    server.send(msg); // weiterleiten
  }
});

// Auf Server-seitiger Route: Nachrichten vom Server
server.onMessage(msg => {
  ws.send(msg); // unmodifiziert an Page
});
```

---

### webSocketRoute.protocols()

```ts
webSocketRoute.protocols(): Array<string>
```

Gibt die angeforderten WebSocket-Subprotokolle zurueck (entspricht dem `Sec-WebSocket-Protocol`-Header).

**Returns:** `Array<string>` — Leeres Array wenn keine Protokolle angefordert

```js
const protocols = ws.protocols();
if (protocols.includes('chat.v2')) {
  // v2-Protokoll-Handling
} else {
  // Fallback auf v1
}
```

---

### webSocketRoute.send(message)

```ts
webSocketRoute.send(message): void
```

Sendet eine Nachricht ueber die WebSocket-Verbindung. Auf der **Page-seitigen** Route: Nachricht wird an die Page gesendet. Auf der **Server-seitigen** Route: Nachricht wird an den echten Server gesendet.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `message` | string \| Buffer | Yes | — | Zu sendende Nachricht; String fuer Text-Frame, Buffer fuer Binaer-Frame |

**Returns:** `void`

```js
// Text-Nachricht
ws.send(JSON.stringify({ type: 'update', data: { count: 42 } }));

// Binaer-Nachricht
ws.send(Buffer.from([0x01, 0x02, 0x03]));
```

---

### webSocketRoute.url()

```ts
webSocketRoute.url(): string
```

Gibt die URL des WebSocket zurueck, der in der Page erstellt wurde.

**Returns:** `string`

```js
console.log('WebSocket URL:', ws.url());
```

---

## Verwendungsmuster

### Pattern 1: Vollstaendiges Mocken (kein echter Server)

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

### Pattern 2: Transparent Intercepten (echter Server)

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();
  // Ohne onMessage: automatisches Durchleiten in beide Richtungen
});
```

### Pattern 3: Server-Nachrichten modifizieren

```js
await page.routeWebSocket('**/ws', ws => {
  const server = ws.connectToServer();

  server.onMessage(msg => {
    const data = JSON.parse(msg);
    // Sensible Felder maskieren
    if (data.creditCard) {
      data.creditCard = '****';
    }
    ws.send(JSON.stringify(data));
  });
});
```

### Pattern 4: Server-Push simulieren

```js
let wsRoute;
await page.routeWebSocket('**/ws', ws => {
  wsRoute = ws;
  ws.connectToServer();
});

await page.goto('/dashboard');

// Von aussen eine Nachricht injecten
await page.evaluate(() => {}); // sicherstellen dass WS verbunden ist
wsRoute.send(JSON.stringify({ type: 'notification', message: 'New order!' }));
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 6 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `WebSocketRoute` ist das maechtigue Werkzeug fuer WebSocket-Tests. `connectToServer()` aktiviert Transparent-Mode mit optionaler Interception via `onMessage()`. Ohne `connectToServer()` wird die Page komplett gemockt — kein echter Server wird kontaktiert. `send()` ist die zentrale Methode zum Einschleusen von Nachrichten von aussen.

---

Source: https://playwright.dev/docs/api/class-websocketroute
