# class-apiresponse

`APIResponse` repraesentiert die HTTP-Antwort auf eine Anfrage ueber `APIRequestContext`. Im Gegensatz zu `Response` (Browser-Requests) muss `APIResponse` explizit via `dispose()` freigegeben werden, wenn der Body nicht benoetigt wird, um Speicherlecks zu vermeiden.

Methoden: 10 | Properties: 0 | Events: 0

---

## Methods

### apiResponse.body()

```ts
await apiResponse.body(): Promise<Buffer>
```

Gibt den vollstaendigen Response-Body als binaeren `Buffer` zurueck.

**Returns:** `Promise<Buffer>`

```js
const buffer = await response.body();
require('fs').writeFileSync('download.pdf', buffer);
```

---

### apiResponse.dispose()

```ts
await apiResponse.dispose(): Promise<void>
```

Gibt den Response-Body aus dem Speicher frei. Sollte aufgerufen werden wenn der Body nicht benoetigt wird (z.B. bei Status-Only-Checks). Andernfalls bleibt der Body im Speicher bis der Context geschlossen wird.

**Returns:** `Promise<void>`

```js
// Status pruefen ohne Body zu lesen
const response = await request.get('/api/health');
expect(response.status()).toBe(200);
await response.dispose(); // Speicher freigeben
```

---

### apiResponse.headers()

```ts
apiResponse.headers(): Object<string, string>
```

Gibt alle Response-Header als Objekt zurueck. Multi-Value-Headers werden kommasepariert zusammengefuehrt.

**Returns:** `Object<string, string>`

```js
const headers = response.headers();
console.log('Content-Type:', headers['content-type']);
console.log('Cache-Control:', headers['cache-control']);
```

---

### apiResponse.headersArray()

```ts
apiResponse.headersArray(): Array<{name: string, value: string}>
```

Gibt alle Response-Header als Array zurueck. Behaelt Original-Casing bei; Multi-Value-Headers (z.B. `Set-Cookie`) erscheinen als separate Eintraege.

**Returns:** `Array<{name: string, value: string}>` — Synchron, kein `await` noetig

```js
const headers = apiResponse.headersArray();
const setCookies = headers
  .filter(h => h.name.toLowerCase() === 'set-cookie')
  .map(h => h.value);
```

---

### apiResponse.json()

```ts
await apiResponse.json(): Promise<Serializable>
```

Gibt den Response-Body als geparste JavaScript-Objekt zurueck. Wirft eine Exception wenn der Body kein gueltiges JSON ist.

**Returns:** `Promise<Serializable>`

```js
const data = await response.json();
expect(data.users).toHaveLength(10);
expect(data.users[0]).toMatchObject({
  id: expect.any(Number),
  name: expect.any(String),
});
```

---

### apiResponse.ok()

```ts
apiResponse.ok(): boolean
```

Gibt `true` zurueck wenn der HTTP-Status-Code im Bereich 200-299 liegt.

**Returns:** `boolean`

```js
const response = await request.post('/api/users', { data: userData });
expect(response.ok()).toBeTruthy();
```

---

### apiResponse.status()

```ts
apiResponse.status(): number
```

Gibt den numerischen HTTP-Status-Code zurueck.

**Returns:** `number`

```js
const response = await request.get('/api/users/99999');
expect(response.status()).toBe(404);
```

---

### apiResponse.statusText()

```ts
apiResponse.statusText(): string
```

Gibt den HTTP-Status-Text zurueck.

**Returns:** `string` — z.B. `"OK"`, `"Created"`, `"Not Found"`, `"Internal Server Error"`

```js
console.log(response.status(), response.statusText());
// z.B. "201 Created"
```

---

### apiResponse.text()

```ts
await apiResponse.text(): Promise<string>
```

Gibt den Response-Body als UTF-8-String zurueck.

**Returns:** `Promise<string>`

```js
const html = await response.text();
expect(html).toContain('<html');

const csv = await response.text();
const rows = csv.split('\n').map(r => r.split(','));
```

---

### apiResponse.url()

```ts
apiResponse.url(): string
```

Gibt die URL zurueck, auf die diese Response antwortet (nach Redirects: finale URL).

**Returns:** `string`

```js
console.log('Final URL:', response.url());
// Bei Redirects: URL nach dem letzten Redirect
```

---

## Nutzungsmuster

### Pattern 1: Vollstaendige JSON-API-Tests

```js
test('CRUD-Zyklus', async ({ request }) => {
  // Create
  const createResp = await request.post('/api/items', {
    data: { name: 'Test Item', price: 9.99 },
  });
  expect(createResp.status()).toBe(201);
  const { id } = await createResp.json();

  // Read
  const readResp = await request.get(`/api/items/${id}`);
  expect(readResp.ok()).toBeTruthy();
  const item = await readResp.json();
  expect(item.name).toBe('Test Item');

  // Update
  const updateResp = await request.put(`/api/items/${id}`, {
    data: { name: 'Updated Item', price: 19.99 },
  });
  expect(updateResp.ok()).toBeTruthy();

  // Delete
  const deleteResp = await request.delete(`/api/items/${id}`);
  expect(deleteResp.status()).toBe(204);
  await deleteResp.dispose(); // kein Body erwartet
});
```

### Pattern 2: Fehlerbehandlung

```js
test('Fehler-Responses pruefen', async ({ request }) => {
  const response = await request.post('/api/users', {
    data: { name: '' }, // invalide Daten
  });

  expect(response.status()).toBe(422);
  const error = await response.json();
  expect(error.errors).toContainEqual(
    expect.objectContaining({ field: 'name' })
  );
});
```

### Pattern 3: Header-Pruefung

```js
test('CORS-Header pruefen', async ({ request }) => {
  const response = await request.get('/api/public', {
    headers: { 'Origin': 'https://trusted.example.com' },
  });

  const headers = response.headers();
  expect(headers['access-control-allow-origin']).toBe('https://trusted.example.com');
  expect(headers['content-type']).toContain('application/json');

  await response.dispose();
});
```

### Pattern 4: Datei-Download

```js
test('PDF-Export herunterladen', async ({ request }) => {
  const response = await request.get('/api/report.pdf');
  expect(response.ok()).toBeTruthy();
  expect(response.headers()['content-type']).toBe('application/pdf');

  const buffer = await response.body();
  expect(buffer.length).toBeGreaterThan(0);
  // PDF-Magic-Bytes pruefen
  expect(buffer.slice(0, 4).toString()).toBe('%PDF');
});
```

---

## Unterschied zu class-response

| Aspekt | `APIResponse` | `Response` |
|--------|---------------|------------|
| Herkunft | `APIRequestContext` | Browser/Page-Netzwerk |
| `dispose()` | Erforderlich | Nicht noetig |
| `headersArray()` | Synchron | Asynchron (await) |
| `allHeaders()` | Nicht vorhanden | Vorhanden |
| `fromServiceWorker()` | Nicht vorhanden | Vorhanden |
| `securityDetails()` | Nicht vorhanden | Vorhanden |
| `serverAddr()` | Nicht vorhanden | Vorhanden |

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 10 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `APIResponse` ist das leichtgewichtige Response-Objekt fuer API-Tests. `ok()`, `status()` und `json()` sind die haeufigsten Methoden. `dispose()` muss aufgerufen werden wenn kein Body gelesen wird, um Speicherlecks zu vermeiden. `headersArray()` ist (im Gegensatz zu `class-response`) synchron.

---

Source: https://playwright.dev/docs/api/class-apiresponse
