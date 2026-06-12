# class-browsercontext

`BrowserContext` bietet eine isolierte Browser-Sitzung mit eigenem Cookie-Speicher, LocalStorage, Berechtigungen und Netzwerk-Routing. Jede Testdatei sollte einen eigenen Context verwenden, um Seiteneffekte zu vermeiden.

Methoden: 25 | Properties: 4 | Events: 16

---

## Methods

### browserContext.addCookies(cookies)

```ts
await browserContext.addCookies(cookies): Promise<void>
```

Fuegt Cookies zum Context hinzu. Felder `url` oder beide `domain` + `path` sind erforderlich.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `cookies` | Array<Object> | Yes | — | Array von Cookie-Objekten |
| `cookies[].name` | string | Yes | — | Cookie-Name |
| `cookies[].value` | string | Yes | — | Cookie-Wert |
| `cookies[].url` | string | No* | — | Cookie-URL (alternativ: domain+path) |
| `cookies[].domain` | string | No* | — | Domain; mit `.` prefix fuer Subdomains |
| `cookies[].path` | string | No* | — | Pfad |
| `cookies[].expires` | number | No | — | Ablaufzeitpunkt als Unix-Timestamp (Sekunden) |
| `cookies[].httpOnly` | boolean | No | — | HttpOnly-Flag |
| `cookies[].secure` | boolean | No | — | Secure-Flag |
| `cookies[].sameSite` | `"Strict"` \| `"Lax"` \| `"None"` | No | — | SameSite-Attribut |
| `cookies[].partitionKey` | string | No | — | CHIPS partition key (Top-Level-Site) |

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

Fuegt ein Script hinzu, das in jedem Frame jeder Page dieses Contexts vor dem Seiten-Script ausgefuehrt wird. Wird auch nach Navigationen erneut ausgefuehrt.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `script` | Function \| string \| Object | Yes | — | Funktion, Script-String oder `{ path?, content? }` |
| `script.path` | string | No | — | Pfad zur Script-Datei (relativ zu cwd) |
| `script.content` | string | No | — | Script-Inhalt als String |
| `arg` | Serializable | No | — | Argument, das an die Funktion uebergeben wird (nur bei Funktionen) |

**Returns:** `Promise<Disposable>` — Aufruf von `.dispose()` entfernt das Script

```js
// Math.random fuer alle Pages ueberschreiben
await context.addInitScript(() => {
  Math.random = () => 0.42;
});

// Mit Argument
await context.addInitScript(({ seed }) => {
  Math.random = () => seed;
}, { seed: 0.5 });
```

---

### browserContext.browser()

```ts
browserContext.browser(): Browser | null
```

Gibt den `Browser` zurueck, dem dieser Context gehoert. Gibt `null` zurueck fuer den persistenten Context (von `launchPersistentContext()`).

**Returns:** `Browser | null`

---

### browserContext.clearCookies([options])

```ts
await browserContext.clearCookies([options]): Promise<void>
```

Loescht Cookies des Contexts, optional gefiltert.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.domain` | string \| RegExp | No | — | Nur Cookies dieser Domain loeschen |
| `options.name` | string \| RegExp | No | — | Nur Cookies mit diesem Namen |
| `options.path` | string \| RegExp | No | — | Nur Cookies mit diesem Pfad |

**Returns:** `Promise<void>`

```js
await context.clearCookies(); // alle loeschen
await context.clearCookies({ name: /session.*/ }); // gefiltert
```

---

### browserContext.clearPermissions()

```ts
await browserContext.clearPermissions(): Promise<void>
```

Widerruft alle zuvor erteilten Berechtigungen.

**Returns:** `Promise<void>`

---

### browserContext.close([options])

```ts
await browserContext.close([options]): Promise<void>
```

Schliesst den Context und alle darin enthaltenen Pages. Der Default-BrowserContext kann nicht geschlossen werden.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.reason` | string | No | — | Grund, der unterbrochenen Operationen gemeldet wird |

**Returns:** `Promise<void>`

---

### browserContext.cookies([urls])

```ts
await browserContext.cookies([urls]): Promise<Array<Cookie>>
```

Gibt Cookies des Contexts zurueck, optional gefiltert nach URLs.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `urls` | string \| Array<string> | No | — | URL(s) zum Filtern |

**Returns:** `Promise<Array<Cookie>>` mit Feldern: `name`, `value`, `domain`, `path` (strings), `expires` (number), `httpOnly`, `secure` (booleans), `sameSite` (`"Strict"` \| `"Lax"` \| `"None"`), `partitionKey?` (string)

```js
const cookies = await context.cookies('https://example.com');
```

---

### browserContext.exposeBinding(name, callback[, options])

```ts
await browserContext.exposeBinding(name, callback[, options]): Promise<Disposable>
```

Stellt eine Funktion unter `window[name]` in allen Frames aller Pages bereit. Der Callback wird im Playwright-Prozess ausgefuehrt und erhaelt als erstes Argument ein Source-Objekt `{ browserContext, page, frame }`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Funktionsname auf dem `window`-Objekt |
| `callback` | Function | Yes | — | Callback-Funktion; erstes Argument ist `{ browserContext, page, frame }` |
| `options.handle` | boolean | No | false | Wenn `true`, erhaelt der Callback ein JSHandle statt des deserialisierten Werts |

**Returns:** `Promise<Disposable>`

```js
await context.exposeBinding('pageURL', ({ page }) => page.url());
// Im Browser: const url = await window.pageURL();
```

---

### browserContext.exposeFunction(name, callback)

```ts
await browserContext.exposeFunction(name, callback): Promise<Disposable>
```

Stellt eine Funktion unter `window[name]` bereit (ohne Source-Argument, einfachere Variante von `exposeBinding`).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Funktionsname |
| `callback` | Function | Yes | — | Wird mit den Argumenten des Browser-Aufrufs aufgerufen |

**Returns:** `Promise<Disposable>`

```js
const crypto = require('crypto');
await context.exposeFunction('sha256', (text) =>
  crypto.createHash('sha256').update(text).digest('hex')
);
// Im Browser: const hash = await window.sha256('hello');
```

---

### browserContext.grantPermissions(permissions[, options])

```ts
await browserContext.grantPermissions(permissions[, options]): Promise<void>
```

Erteilt Berechtigungen fuer den Context (optional eingeschraenkt auf einen Origin).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `permissions` | Array<string> | Yes | — | Zu erteilende Berechtigungen |
| `options.origin` | string | No | — | Nur fuer diesen Origin erteilen |

**Moegliche Berechtigungen:** `"accelerometer"`, `"ambient-light-sensor"`, `"background-sync"`, `"camera"`, `"clipboard-read"`, `"clipboard-write"`, `"geolocation"`, `"gyroscope"`, `"local-fonts"`, `"local-network-access"`, `"magnetometer"`, `"microphone"`, `"midi"`, `"midi-sysex"`, `"notifications"`, `"payment-handler"`, `"storage-access"`, `"screen-wake-lock"`

**Returns:** `Promise<void>`

```js
await context.grantPermissions(['geolocation'], { origin: 'https://example.com' });
```

---

### browserContext.isClosed()

```ts
browserContext.isClosed(): boolean
```

Gibt `true` zurueck wenn der Context geschlossen wurde.

**Returns:** `boolean`

---

### browserContext.newCDPSession(page)

```ts
await browserContext.newCDPSession(page): Promise<CDPSession>
```

Erstellt eine neue CDP-Session fuer eine Page oder einen Frame. **Nur Chromium.**

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `page` | Page \| Frame | Yes | — | Ziel der CDP-Session |

**Returns:** `Promise<CDPSession>`

---

### browserContext.newPage()

```ts
await browserContext.newPage(): Promise<Page>
```

Erstellt eine neue Page in diesem Context.

**Returns:** `Promise<Page>`

---

### browserContext.pages()

```ts
browserContext.pages(): Array<Page>
```

Gibt alle offenen Pages in diesem Context zurueck.

**Returns:** `Array<Page>`

---

### browserContext.removeAllListeners([type, options])

```ts
await browserContext.removeAllListeners([type, options]): Promise<void>
```

Entfernt Event-Listener.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `type` | string | No | — | Event-Typ |
| `options.behavior` | `"wait"` \| `"ignoreErrors"` \| `"default"` | No | `"default"` | Umgang mit laufenden Handlern |

**Returns:** `Promise<void>`

---

### browserContext.route(url, handler[, options])

```ts
await browserContext.route(url, handler[, options]): Promise<Disposable>
```

Registriert einen Netzwerk-Handler fuer alle Pages in diesem Context. Handler wird fuer jede Anfrage aufgerufen, die `url` matcht.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| URLPattern \| Function(URL):boolean | Yes | — | URL-Muster oder Praedikat |
| `handler` | Function(Route, Request) | Yes | — | Handler-Funktion; muss `route.fulfill()`, `route.continue()`, `route.abort()` oder `route.fallback()` aufrufen |
| `options.times` | number | No | — | Wie oft der Handler angewendet wird (danach entfernt) |

**Returns:** `Promise<Disposable>`

```js
// Alle Bilder blockieren
await context.route('**/*.{png,jpg,jpeg}', route => route.abort());

// API-Anfragen mocken
await context.route(/api\/users/, async route => {
  await route.fulfill({ json: [{ id: 1, name: 'Alice' }] });
});
```

---

### browserContext.routeFromHAR(har[, options])

```ts
await browserContext.routeFromHAR(har[, options]): Promise<void>
```

Bedient Netzwerkanfragen aus einer HAR-Datei (HTTP Archive).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `har` | string | Yes | — | Pfad zur HAR-Datei |
| `options.notFound` | `"abort"` \| `"fallback"` | No | `"abort"` | Verhalten fuer nicht gematchte Anfragen |
| `options.update` | boolean | No | false | HAR mit echten Daten aktualisieren |
| `options.updateContent` | `"embed"` \| `"attach"` | No | — | Content-Speichermodus beim Update |
| `options.updateMode` | `"full"` \| `"minimal"` | No | `"minimal"` | Update-Umfang |
| `options.url` | string \| RegExp | No | — | Nur Anfragen fuer dieses Muster aus HAR bedienen |

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

Registriert einen Handler fuer WebSocket-Verbindungen in allen Pages dieses Contexts.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| Function(URL):boolean | Yes | — | WebSocket-URL-Muster |
| `handler` | Function(WebSocketRoute) | Yes | — | Handler-Funktion |

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

Gibt alle aktiven Service Workers in diesem Context zurueck. **Nur Chromium.**

**Returns:** `Array<Worker>`

---

### browserContext.setDefaultNavigationTimeout(timeout)

```ts
browserContext.setDefaultNavigationTimeout(timeout): void
```

Setzt das Standard-Timeout fuer Navigationsoperationen (`goto`, `goBack`, `goForward`, `reload`, `setContent`, `waitForNavigation`).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `timeout` | number | Yes | — | Timeout in Millisekunden |

---

### browserContext.setDefaultTimeout(timeout)

```ts
browserContext.setDefaultTimeout(timeout): void
```

Setzt das Standard-Timeout fuer alle Operationen (ausser Navigation).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `timeout` | number | Yes | — | Timeout in Millisekunden; `0` = kein Timeout |

---

### browserContext.setExtraHTTPHeaders(headers)

```ts
await browserContext.setExtraHTTPHeaders(headers): Promise<void>
```

Setzt zusaetzliche HTTP-Header, die bei jeder Anfrage aller Pages gesendet werden.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `headers` | Object<string,string> | Yes | — | Header-Name/-Wert-Paare |

**Returns:** `Promise<void>`

```js
await context.setExtraHTTPHeaders({ 'X-Custom-Header': 'value' });
```

---

### browserContext.setGeolocation(geolocation)

```ts
await browserContext.setGeolocation(geolocation): Promise<void>
```

Setzt oder aendert die Geolocation-Emulation. Erfordert zuvor `grantPermissions(['geolocation'])`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `geolocation` | Object \| null | Yes | — | `null` loescht die Emulation |
| `geolocation.latitude` | number | Yes | — | Breitengrad (-90 bis 90) |
| `geolocation.longitude` | number | Yes | — | Laengengrad (-180 bis 180) |
| `geolocation.accuracy` | number | No | 0 | Genauigkeit in Metern (>= 0) |

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

Aktiviert oder deaktiviert die Offline-Netzwerkemulation.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `offline` | boolean | Yes | — | `true` = offline emulieren |

**Returns:** `Promise<void>`

---

### browserContext.setStorageState(storageState)

```ts
await browserContext.setStorageState(storageState): Promise<void>
```

Setzt Cookies und LocalStorage des Contexts (loescht zuvor vorhandene Daten).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `storageState` | string \| Object | Yes | — | Dateipfad oder State-Objekt mit `cookies` und `origins` |

**Returns:** `Promise<void>`

---

### browserContext.storageState([options])

```ts
await browserContext.storageState([options]): Promise<StorageState>
```

Gibt den aktuellen Storage-State (Cookies + LocalStorage) als serialisierbares Objekt zurueck.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.indexedDB` | boolean | No | false | IndexedDB-Snapshot einschliessen |
| `options.path` | string | No | — | Dateipfad zum Speichern |

**Returns:** `Promise<StorageState>` mit Feldern `cookies` (Array) und `origins` (Array mit `localStorage`)

```js
// Nach dem Login speichern
await page.locator('#login').click();
await context.storageState({ path: 'auth.json' });
```

---

### browserContext.unroute(url[, handler])

```ts
await browserContext.unroute(url[, handler]): Promise<void>
```

Entfernt einen zuvor registrierten Route-Handler.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string \| RegExp \| URLPattern \| Function | Yes | — | Zu entfernendes URL-Muster |
| `handler` | Function | No | — | Bestimmten Handler entfernen (sonst alle fuer `url`) |

**Returns:** `Promise<void>`

---

### browserContext.unrouteAll([options])

```ts
await browserContext.unrouteAll([options]): Promise<void>
```

Entfernt alle Route-Handler.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.behavior` | `"wait"` \| `"ignoreErrors"` \| `"default"` | No | `"default"` | Umgang mit laufenden Handlern |

**Returns:** `Promise<void>`

---

### browserContext.waitForEvent(event[, optionsOrPredicate])

```ts
await browserContext.waitForEvent(event[, optionsOrPredicate]): Promise<Object>
```

Wartet auf ein Event und gibt dessen Daten zurueck.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `event` | string | Yes | — | Event-Name (z.B. `"page"`, `"request"`) |
| `optionsOrPredicate` | Function \| Object | No | — | Praedikat oder Options-Objekt |
| `optionsOrPredicate.predicate` | Function | No | — | Gibt `true` zurueck wenn das Event akzeptiert werden soll |
| `optionsOrPredicate.timeout` | number | No | 30000 | Timeout in Millisekunden |

**Returns:** `Promise<Object>` — Event-Daten

```js
const pagePromise = context.waitForEvent('page');
await page.locator('a[target=_blank]').click();
const newPage = await pagePromise;
```

---

## Properties

### browserContext.clock

**Type:** `Clock`

Erlaubt die Steuerung der Zeit (Mock-Clock). Ermoeglicht das Vorspulen von Timern, Dates und Intervallen.

```js
await context.clock.setFixedTime(new Date('2024-01-01'));
```

---

### browserContext.debugger

**Type:** `Debugger`

Ermoeglicht das Pausieren und Fortsetzen der Ausfuehrung waehrend des Debuggings.

---

### browserContext.request

**Type:** `APIRequestContext`

API-Testing-Helfer, der die Cookies des Contexts teilt. Verwendet fuer HTTP-Anfragen ausserhalb des Browsers.

```js
const response = await context.request.get('https://api.example.com/users');
```

---

### browserContext.tracing

**Type:** `Tracing`

Playwright Tracing-Unterstuetzung fuer diesen Context.

```js
await context.tracing.start({ screenshots: true, snapshots: true });
// ... Test durchfuehren ...
await context.tracing.stop({ path: 'trace.zip' });
```

---

## Events

### event: 'close'

Wird ausgeloest wenn der Context geschlossen wird.

**Event data:** `BrowserContext`

---

### event: 'console'

Wird ausgeloest wenn `console.log()`, `console.error()` o.ae. in einer Page aufgerufen wird.

**Event data:** `ConsoleMessage`

```js
context.on('console', msg => console.log(msg.text()));
```

---

### event: 'dialog'

Wird ausgeloest wenn ein JavaScript-Dialog erscheint (`alert`, `prompt`, `confirm`, `beforeunload`). Dialog muss mit `dialog.accept()` oder `dialog.dismiss()` behandelt werden.

**Event data:** `Dialog`

---

### event: 'download'

Wird ausgeloest wenn ein Datei-Download in einer Page des Contexts beginnt.

**Event data:** `Download`

---

### event: 'frameattached'

Wird ausgeloest wenn ein Frame in einer Page des Contexts hinzugefuegt wird.

**Event data:** `Frame`

---

### event: 'framedetached'

Wird ausgeloest wenn ein Frame aus einer Page des Contexts entfernt wird.

**Event data:** `Frame`

---

### event: 'framenavigated'

Wird ausgeloest wenn ein Frame zu einer neuen URL navigiert.

**Event data:** `Frame`

---

### event: 'page'

Wird ausgeloest wenn eine neue Page im Context erstellt wird (z.B. durch Popup oder `context.newPage()`).

**Event data:** `Page`

```js
context.on('page', async page => {
  await page.waitForLoadState();
  console.log(page.url());
});
```

---

### event: 'pageclose'

Wird ausgeloest wenn eine Page im Context geschlossen wird.

**Event data:** `Page`

---

### event: 'pageload'

Wird ausgeloest wenn das JavaScript-`load`-Event einer Page im Context dispatched wird.

**Event data:** `Page`

---

### event: 'request'

Wird ausgeloest wenn eine Netzwerk-Anfrage von einer Page des Contexts initiiert wird.

**Event data:** `Request`

---

### event: 'requestfailed'

Wird ausgeloest wenn eine Anfrage fehlschlaegt (Timeout, Abbruch, o.ae.).

**Event data:** `Request`

---

### event: 'requestfinished'

Wird ausgeloest wenn eine Anfrage abgeschlossen ist (Response vollstaendig heruntergeladen).

**Event data:** `Request`

---

### event: 'response'

Wird ausgeloest wenn Status-Code und Header einer Antwort empfangen wurden.

**Event data:** `Response`

---

### event: 'serviceworker'

Wird ausgeloest wenn ein neuer Service Worker im Context registriert wird. **Nur Chromium.**

**Event data:** `Worker`

---

### event: 'weberror'

Wird ausgeloest wenn eine unbehandelte Exception in einer Page des Contexts auftritt.

**Event data:** `WebError` mit `error()` und `page()`

```js
context.on('weberror', err => console.error(err.error().message));
```

---

## Deprecated

### browserContext.setHTTPCredentials(httpCredentials) [DEPRECATED]

Veraltet. Browser cachen Credentials; stattdessen neuen Context mit `httpCredentials`-Option erstellen.

### backgroundPages() [DEPRECATED]

Veraltet (Chromium Manifest V3). Gibt immer leeres Array zurueck.

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 25 |
| Properties | 4 |
| Events | 16 |

**Fazit:** `BrowserContext` ist die zentrale Isolationseinheit in Playwright. Die wichtigsten Features sind Netzwerk-Routing (`route`, `routeFromHAR`), Cookie/Storage-Management (`addCookies`, `storageState`, `setStorageState`) und Berechtigungen (`grantPermissions`). Fuer End-to-End-Authentication-Flows ist `storageState()` unverzichtbar.

---

Source: https://playwright.dev/docs/api/class-browsercontext
