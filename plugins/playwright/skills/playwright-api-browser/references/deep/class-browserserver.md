# class-browserserver

`BrowserServer` repraesentiert eine laufende Browser-Server-Instanz, die via `browserType.launchServer()` gestartet wurde. Clients koennen sich per `browserType.connect(wsEndpoint)` verbinden.

Methoden: 4 | Properties: 0 | Events: 1

---

## Methods

### browserServer.close()

```ts
await browserServer.close(): Promise<void>
```

Schliesst den Browser-Server gracefully und wartet, bis der Prozess beendet ist.

**Returns:** `Promise<void>`

```js
await browserServer.close();
```

---

### browserServer.kill()

```ts
await browserServer.kill(): Promise<void>
```

Beendet den Browser-Prozess sofort (kill) und wartet bis der Prozess terminiert ist. Im Gegensatz zu `close()` ohne graceful shutdown.

**Returns:** `Promise<void>`

```js
await browserServer.kill();
```

---

### browserServer.process()

```ts
browserServer.process(): ChildProcess
```

Gibt den Node.js `ChildProcess` des gestarteten Browser-Prozesses zurueck.

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

Gibt den WebSocket-Endpoint zurueck, der als Argument fuer `browserType.connect()` verwendet werden kann.

**Returns:** `string` — WebSocket-URL

```js
const endpoint = browserServer.wsEndpoint();
// z.B. "ws://localhost:9222/secret-token"

// Anderer Prozess verbindet sich:
const browser = await chromium.connect(endpoint);
```

---

## Events

### event: 'close'

Wird ausgeloest wenn der Browser-Server geschlossen wird.

**Event data:** keine Daten

```js
browserServer.on('close', () => {
  console.log('BrowserServer closed');
});
```

---

## Typisches Usage-Pattern

```js
// Server-Prozess:
const { chromium } = require('playwright');
const server = await chromium.launchServer({
  port: 9222,
  wsPath: 'my-secret-token',
});
console.log('Endpoint:', server.wsEndpoint());
// Endpoint sicher an Client weitergeben...

// Client-Prozess:
const browser = await chromium.connect('ws://localhost:9222/my-secret-token');
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();

// Server herunterfahren:
await server.close();
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 4 |
| Properties | 0 |
| Events | 1 |

**Fazit:** `BrowserServer` ist ein schlankes Handle fuer Remote-Browser-Instanzen. `wsEndpoint()` ist die entscheidende Methode, um den Verbindungspunkt an Clients weiterzugeben. Fuer Produktions-Setups sollte `wsPath` ein unvorhersehbares Token enthalten, um unautorisierten Zugriff zu verhindern.

---

Source: https://playwright.dev/docs/api/class-browserserver
