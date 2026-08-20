# class-request

`Request` repraesentiert eine HTTP-Anfrage, die von einer Playwright-Page initiiert wurde. Instanzen werden ueber Page/Context-Events (`on('request')`) oder als Parameter von Route-Handlern erhalten. Das Objekt ist read-only.

Methoden: 15 | Properties: 0 | Events: 0

---

## Methods

### request.allHeaders()

```ts
await request.allHeaders(): Promise<Object<string, string>>
```

Gibt alle HTTP-Request-Header als Objekt zurueck. Header-Namen sind lowercase. Enthaelt auch sicherheitsrelevante Header (`cookie`, etc.), die von `headers()` ausgelassen werden.

**Returns:** `Promise<Object<string, string>>`

```js
const headers = await request.allHeaders();
console.log(headers['content-type']);
```

---

### request.existingResponse()

```ts
request.existingResponse(): Response | null
```

Gibt die Response sofort zurueck, wenn sie bereits empfangen wurde — ohne zu warten. Gibt `null` zurueck wenn noch keine Response vorliegt.

**Returns:** `Response | null`

```js
const response = request.existingResponse();
if (response) {
  console.log('Status:', response.status());
}
```

---

### request.failure()

```ts
request.failure(): { errorText: string } | null
```

Gibt ein Objekt mit dem Fehlertext zurueck wenn die Anfrage fehlgeschlagen ist. Gibt `null` zurueck fuer erfolgreiche Anfragen. Wird typischerweise in `requestfailed`-Events verwendet.

**Returns:** `{ errorText: string } | null`

```js
page.on('requestfailed', request => {
  console.log(request.url(), request.failure()?.errorText);
});
```

---

### request.frame()

```ts
request.frame(): Frame
```

Gibt den `Frame` zurueck, der diese Anfrage initiiert hat.

**Returns:** `Frame`

**Hinweis:** Wirft eine Exception wenn der Frame nicht verfuegbar ist (z.B. bei Service Worker-Anfragen oder sehr fruehen Navigationsanfragen).

```js
const frame = request.frame();
console.log('Frame URL:', frame.url());
```

---

### request.headerValue(name)

```ts
await request.headerValue(name): Promise<string | null>
```

Gibt den Wert eines einzelnen Request-Headers zurueck (case-insensitive).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header-Name (Gross-/Kleinschreibung irrelevant) |

**Returns:** `Promise<string | null>` — `null` wenn Header nicht vorhanden

```js
const contentType = await request.headerValue('Content-Type');
```

---

### request.headers()

```ts
request.headers(): Object<string, string>
```

Gibt Request-Header als Objekt zurueck (synchron). Schliesst sicherheitsrelevante Headers wie `cookie` und internale Playwright-Headers aus. Fuer vollstaendige Headers `allHeaders()` verwenden.

**Returns:** `Object<string, string>`

---

### request.headersArray()

```ts
await request.headersArray(): Promise<Array<{name: string, value: string}>>
```

Gibt alle Request-Header als Array von Name/Wert-Objekten zurueck. Behaelt Original-Casing bei und enthaelt mehrfache Eintraege fuer Multi-Value-Headers.

**Returns:** `Promise<Array<{name: string, value: string}>>`

```js
const headers = await request.headersArray();
headers.forEach(h => console.log(`${h.name}: ${h.value}`));
```

---

### request.isNavigationRequest()

```ts
request.isNavigationRequest(): boolean
```

Gibt `true` zurueck wenn diese Anfrage eine Frame-Navigation antreibt.

**Returns:** `boolean`

---

### request.method()

```ts
request.method(): string
```

Gibt die HTTP-Methode der Anfrage zurueck.

**Returns:** `string` — z.B. `"GET"`, `"POST"`, `"PUT"`, `"DELETE"`

---

### request.postData()

```ts
request.postData(): string | null
```

Gibt den Request-Body als String zurueck. `null` wenn kein Body vorhanden (z.B. GET-Anfragen).

**Returns:** `string | null`

---

### request.postDataBuffer()

```ts
request.postDataBuffer(): Buffer | null
```

Gibt den Request-Body als binaeren `Buffer` zurueck. `null` wenn kein Body vorhanden.

**Returns:** `Buffer | null`

---

### request.postDataJSON()

```ts
request.postDataJSON(): Serializable | null
```

Gibt den Request-Body als geparste JavaScript-Objekt zurueck. Unterstuetzt `application/json` und `application/x-www-form-urlencoded`. Gibt `null` zurueck wenn Body nicht parsbar ist.

**Returns:** `Serializable | null`

```js
const body = request.postDataJSON();
console.log(body?.userId);
```

---

### request.redirectedFrom()

```ts
request.redirectedFrom(): Request | null
```

Gibt die vorherige `Request`-Instanz zurueck, die zu dieser Anfrage weitergeleitet hat. Bildet die Redirect-Kette rueckwaerts ab.

**Returns:** `Request | null`

```js
// Redirect-Chain durchlaufen
let req = request;
while (req.redirectedFrom()) {
  req = req.redirectedFrom();
  console.log('Redirect von:', req.url());
}
```

---

### request.redirectedTo()

```ts
request.redirectedTo(): Request | null
```

Gibt die nachfolgende `Request`-Instanz zurueck, die durch einen Server-Redirect erstellt wurde. Gegenteil von `redirectedFrom()`.

**Returns:** `Request | null`

---

### request.resourceType()

```ts
request.resourceType(): string
```

Gibt den Ressourcentyp der Anfrage zurueck.

**Returns:** `string` — Moegliche Werte: `"document"`, `"stylesheet"`, `"image"`, `"media"`, `"font"`, `"script"`, `"texttrack"`, `"xhr"`, `"fetch"`, `"eventsource"`, `"websocket"`, `"manifest"`, `"other"`

```js
page.on('request', req => {
  if (req.resourceType() === 'image') {
    console.log('Image request:', req.url());
  }
});
```

---

### request.response()

```ts
await request.response(): Promise<Response | null>
```

Wartet auf die Response zu dieser Anfrage und gibt sie zurueck. `null` wenn keine Response empfangen wurde (z.B. bei abgebrochenen Anfragen).

**Returns:** `Promise<Response | null>`

```js
page.on('requestfinished', async request => {
  const response = await request.response();
  console.log(response?.status());
});
```

---

### request.serviceWorker()

```ts
request.serviceWorker(): Worker | null
```

Gibt den Service Worker zurueck, der diese Anfrage ausfuehrt. `null` wenn kein Service Worker beteiligt ist. **Nur Chromium; auf anderen Browsern immer `null`.**

**Returns:** `Worker | null`

---

### request.sizes()

```ts
await request.sizes(): Promise<{requestBodySize: number, requestHeadersSize: number, responseBodySize: number, responseHeadersSize: number}>
```

Gibt Groesseninformationen zur Anfrage und Antwort zurueck (in Bytes).

**Returns:** `Promise<Object>` mit:

| Field | Type | Description |
|-------|------|-------------|
| `requestBodySize` | number | Groesse des Request-Bodys |
| `requestHeadersSize` | number | Groesse der Request-Header |
| `responseBodySize` | number | Groesse des Response-Bodys |
| `responseHeadersSize` | number | Groesse der Response-Header |

```js
const sizes = await request.sizes();
console.log(`Response: ${sizes.responseBodySize} bytes`);
```

---

### request.timing()

```ts
request.timing(): Object
```

Gibt Timing-Informationen zur Anfrage zurueck (aehnlich Resource Timing API).

**Returns:** `Object` mit:

| Field | Type | Description |
|-------|------|-------------|
| `startTime` | number | Request-Startzeitpunkt (ms seit Epoch) |
| `domainLookupStart` | number | DNS-Lookup-Beginn (ms seit startTime) |
| `domainLookupEnd` | number | DNS-Lookup-Ende |
| `connectStart` | number | TCP-Verbindungsaufbau-Beginn |
| `secureConnectionStart` | number | TLS-Handshake-Beginn |
| `connectEnd` | number | TCP-Verbindungsaufbau-Ende |
| `requestStart` | number | Erster Byte gesendet |
| `responseStart` | number | Erster Byte empfangen (TTFB) |
| `responseEnd` | number | Letzter Byte empfangen |

```js
const timing = request.timing();
const ttfb = timing.responseStart - timing.requestStart;
console.log(`TTFB: ${ttfb}ms`);
```

---

### request.url()

```ts
request.url(): string
```

Gibt die vollstaendige URL der Anfrage zurueck.

**Returns:** `string`

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 15 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `Request` ist ein read-only Datenobjekt. Die wichtigsten Methoden fuer Tests sind `url()`, `method()`, `postData()`/`postDataJSON()` und `resourceType()`. Fuer vollstaendige Header-Infos (inkl. Cookies) muss `allHeaders()` statt `headers()` verwendet werden.

---

Source: https://playwright.dev/docs/api/class-request
