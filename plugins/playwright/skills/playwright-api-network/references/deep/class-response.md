# class-response

`Response` repraesentiert eine HTTP-Antwort auf eine Playwright-Anfrage. Instanzen werden ueber Page/Context-Events (`on('response')`) oder via `request.response()` erhalten. Das Objekt ist read-only.

Methoden: 15 | Properties: 0 | Events: 0

---

## Methods

### response.allHeaders()

```ts
await response.allHeaders(): Promise<Object<string, string>>
```

Gibt alle Response-Header als Objekt zurueck (lowercase Keys). Enthaelt auch sicherheitsrelevante Header, die von `headers()` ausgelassen werden. Multi-Value-Headers werden mit Komma zusammengefuehrt.

**Returns:** `Promise<Object<string, string>>`

```js
const headers = await response.allHeaders();
console.log(headers['content-type']);
```

---

### response.body()

```ts
await response.body(): Promise<Buffer>
```

Gibt den vollstaendigen Response-Body als binaeren `Buffer` zurueck.

**Returns:** `Promise<Buffer>`

```js
const buffer = await response.body();
require('fs').writeFileSync('response.bin', buffer);
```

---

### response.finished()

```ts
await response.finished(): Promise<null | Error>
```

Wartet bis die Response vollstaendig heruntergeladen wurde. Gibt immer `null` zurueck bei Erfolg.

**Returns:** `Promise<null | Error>` — `null` bei Erfolg, `Error` bei Fehler

```js
const err = await response.finished();
if (err) console.error('Download fehlgeschlagen:', err.message);
```

---

### response.frame()

```ts
response.frame(): Frame
```

Gibt den `Frame` zurueck, der diese Response ausgeloest hat.

**Returns:** `Frame`

---

### response.fromServiceWorker()

```ts
response.fromServiceWorker(): boolean
```

Gibt `true` zurueck wenn diese Response von einem Service Worker Fetch Handler bedient wurde.

**Returns:** `boolean`

---

### response.headerValue(name)

```ts
await response.headerValue(name): Promise<string | null>
```

Gibt den Wert eines einzelnen Response-Headers zurueck. Bei mehrfach vorkommenden Headers werden die Werte kommasepariert zusammengefuehrt.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header-Name (case-insensitive) |

**Returns:** `Promise<string | null>`

```js
const contentType = await response.headerValue('content-type');
```

---

### response.headerValues(name)

```ts
await response.headerValues(name): Promise<Array<string>>
```

Gibt alle Werte eines Headers als Array zurueck. Besonders nuetzlich fuer `Set-Cookie`, der mehrfach vorkommen kann.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header-Name (case-insensitive) |

**Returns:** `Promise<Array<string>>`

```js
const cookies = await response.headerValues('set-cookie');
cookies.forEach(c => console.log('Cookie:', c));
```

---

### response.headers()

```ts
response.headers(): Object<string, string>
```

Gibt Response-Header synchron als Objekt zurueck (lowercase Keys). Schliesst einige sicherheitsrelevante Headers aus. Fuer alle Headers `allHeaders()` verwenden.

**Returns:** `Object<string, string>`

---

### response.headersArray()

```ts
await response.headersArray(): Promise<Array<{name: string, value: string}>>
```

Gibt alle Response-Header als Array von Name/Wert-Objekten zurueck. Behaelt Original-Casing bei; Multi-Value-Headers erscheinen als separate Eintraege.

**Returns:** `Promise<Array<{name: string, value: string}>>`

```js
const headers = await response.headersArray();
headers.forEach(h => console.log(`${h.name}: ${h.value}`));
```

---

### response.httpVersion()

```ts
await response.httpVersion(): Promise<string>
```

Gibt die HTTP-Version zurueck, die fuer diese Response verwendet wurde.

**Returns:** `Promise<string>` — z.B. `"HTTP/1.1"`, `"HTTP/2.0"`, `"HTTP/3.0"`

```js
const version = await response.httpVersion();
console.log('HTTP Version:', version);
```

---

### response.json()

```ts
await response.json(): Promise<Serializable>
```

Gibt den Response-Body als geparste JavaScript-Objekt zurueck. Wirft eine Exception wenn der Body kein gueltiges JSON ist.

**Returns:** `Promise<Serializable>`

```js
const data = await response.json();
console.log(data.users[0].name);
```

---

### response.ok()

```ts
response.ok(): boolean
```

Gibt `true` zurueck wenn der Status-Code im Bereich 200-299 liegt.

**Returns:** `boolean`

```js
expect(response.ok()).toBeTruthy();
```

---

### response.request()

```ts
response.request(): Request
```

Gibt die zugehoerige `Request`-Instanz zurueck.

**Returns:** `Request`

```js
const req = response.request();
console.log('Methode:', req.method(), 'URL:', req.url());
```

---

### response.securityDetails()

```ts
await response.securityDetails(): Promise<null | Object>
```

Gibt SSL/TLS-Sicherheitsinformationen zurueck. `null` fuer unsichere (HTTP) Verbindungen.

**Returns:** `Promise<null | Object>` mit:

| Field | Type | Description |
|-------|------|-------------|
| `issuer` | string | Zertifikat-Aussteller (Common Name) |
| `protocol` | string | TLS-Protokollversion |
| `subjectName` | string | Zertifikat-Subject (Common Name) |
| `validFrom` | number | Gueltigkeitsbeginn (Unix-Timestamp) |
| `validTo` | number | Gueltigkeitsende (Unix-Timestamp) |

```js
const details = await response.securityDetails();
if (details) {
  console.log(`TLS: ${details.protocol}, Issuer: ${details.issuer}`);
  console.log(`Valid until: ${new Date(details.validTo * 1000).toISOString()}`);
}
```

---

### response.serverAddr()

```ts
await response.serverAddr(): Promise<null | {ipAddress: string, port: number}>
```

Gibt IP-Adresse und Port des Servers zurueck, der die Response gesendet hat.

**Returns:** `Promise<null | {ipAddress: string, port: number}>`

```js
const addr = await response.serverAddr();
if (addr) {
  console.log(`Server: ${addr.ipAddress}:${addr.port}`);
}
```

---

### response.status()

```ts
response.status(): number
```

Gibt den numerischen HTTP-Status-Code zurueck.

**Returns:** `number` — z.B. `200`, `201`, `301`, `404`, `500`

```js
expect(response.status()).toBe(200);
```

---

### response.statusText()

```ts
response.statusText(): string
```

Gibt den HTTP-Status-Text zurueck.

**Returns:** `string` — z.B. `"OK"`, `"Not Found"`, `"Internal Server Error"`

---

### response.text()

```ts
await response.text(): Promise<string>
```

Gibt den Response-Body als String zurueck (UTF-8-Dekodierung).

**Returns:** `Promise<string>`

```js
const html = await response.text();
console.log(html.includes('<title>'));
```

---

### response.url()

```ts
response.url(): string
```

Gibt die URL der Response zurueck (kann nach Redirects von der urspruenglichen Request-URL abweichen).

**Returns:** `string`

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 15 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `Response` ist ein read-only Datenobjekt fuer HTTP-Antworten. Fuer API-Tests sind `status()`, `ok()`, `json()` und `text()` die am haeufigsten verwendeten Methoden. `headerValues()` ist wichtig fuer `Set-Cookie`-Analyse. `securityDetails()` und `serverAddr()` decken TLS- und Infrastruktur-Pruefungen ab.

---

Source: https://playwright.dev/docs/api/class-response
