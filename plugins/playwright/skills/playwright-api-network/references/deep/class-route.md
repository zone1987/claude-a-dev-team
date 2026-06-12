# class-route

`Route` repraesentiert eine abgefangene Netzwerkanfrage im Kontext eines Route-Handlers (registriert via `page.route()`, `browserContext.route()`). Jede Route muss exakt einmal mit `fulfill()`, `continue()`, `abort()` oder `fallback()` behandelt werden.

Methoden: 6 | Properties: 0 | Events: 0

---

## Methods

### route.abort([errorCode])

```ts
await route.abort([errorCode]): Promise<void>
```

Bricht die Anfrage ab. Der Browser erhaelt einen Netzwerkfehler.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `errorCode` | string | No | `"failed"` | Art des Fehlers |

**Moegliche Fehlercodes:**

| Code | Beschreibung |
|------|-------------|
| `"aborted"` | Operation wurde abgebrochen |
| `"accessdenied"` | Zugriff verweigert |
| `"addressunreachable"` | Adresse nicht erreichbar |
| `"blockedbyclient"` | Durch Client blockiert |
| `"blockedbyresponse"` | Durch Response blockiert |
| `"connectionaborted"` | Verbindung abgebrochen |
| `"connectionclosed"` | Verbindung geschlossen |
| `"connectionfailed"` | Verbindung fehlgeschlagen |
| `"connectionrefused"` | Verbindung abgelehnt |
| `"connectionreset"` | Verbindung zurueckgesetzt |
| `"internetdisconnected"` | Keine Internetverbindung |
| `"namenotresolved"` | DNS-Aufloesung fehlgeschlagen |
| `"timedout"` | Timeout |
| `"failed"` | Generischer Fehler (Default) |

**Returns:** `Promise<void>`

```js
// Alle Tracker blockieren
await page.route('**tracking**', route => route.abort());

// Bilder mit spezifischem Fehler blockieren
await page.route('**/*.{png,jpg,gif}', route => route.abort('blockedbyclient'));
```

---

### route.continue([options])

```ts
await route.continue([options]): Promise<void>
```

Leitet die Anfrage unveraendert oder modifiziert an das Netzwerk weiter. Die Anfrage wird tatsaechlich ausgefuehrt.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | HTTP-Header ueberschreiben (gilt fuer Original- und Redirect-Anfragen) |
| `options.method` | string | No | — | HTTP-Methode ueberschreiben (nur Original-Anfrage) |
| `options.postData` | string \| Buffer \| Serializable | No | — | Request-Body ueberschreiben (nur Original-Anfrage) |
| `options.url` | string | No | — | URL ueberschreiben (muss gleiches Protokoll behalten; nur Original-Anfrage) |

**Returns:** `Promise<void>`

```js
// Anfrage unveraendert durchlassen
await page.route('**', route => route.continue());

// Authorization-Header hinzufuegen
await page.route('**/api/**', route => route.continue({
  headers: {
    ...route.request().headers(),
    'Authorization': 'Bearer token123',
  },
}));

// Methode und Body aendern
await page.route('**/search', route => route.continue({
  method: 'POST',
  postData: JSON.stringify({ q: 'playwright' }),
  headers: { 'Content-Type': 'application/json' },
}));
```

---

### route.fallback([options])

```ts
await route.fallback([options]): Promise<void>
```

Gibt die Kontrolle an den naechsten passenden Route-Handler ab (wenn mehrere Handler fuer die gleiche URL registriert sind). Wenn kein weiterer Handler existiert, wird die Anfrage an das Netzwerk weitergeleitet. Akzeptiert die gleichen Optionen wie `continue()` zur Modifikation.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | Header-Overrides |
| `options.method` | string | No | — | Methoden-Override |
| `options.postData` | string \| Buffer \| Serializable | No | — | Body-Override |
| `options.url` | string | No | — | URL-Override |

**Returns:** `Promise<void>`

```js
// Erster Handler: Logging
await context.route('**', route => {
  console.log('Request:', route.request().url());
  route.fallback(); // naechsten Handler aufrufen
});

// Zweiter Handler: Spezifisches Mocking
await page.route('**/api/users', route => route.fulfill({
  json: [{ id: 1, name: 'Alice' }],
}));
```

---

### route.fetch([options])

```ts
await route.fetch([options]): Promise<APIResponse>
```

Fuehrt die Anfrage aus und gibt die Response zurueck, ohne die Route abzuschliessen. Ermoeglicht das Lesen und/oder Modifizieren der echten Response vor dem Zurueckgeben an den Browser.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | Header-Overrides fuer die ausgefuehrte Anfrage |
| `options.maxRedirects` | number | No | 20 | Maximale Anzahl automatischer Redirects |
| `options.maxRetries` | number | No | 0 | Wiederholungen bei Netzwerkfehlern |
| `options.method` | string | No | — | HTTP-Methoden-Override |
| `options.postData` | string \| Buffer \| Serializable | No | — | Body-Override |
| `options.timeout` | number | No | 30000 | Timeout in ms |
| `options.url` | string | No | — | URL-Override |

**Returns:** `Promise<APIResponse>`

**Wichtig:** Nach `route.fetch()` muss die Route noch mit `fulfill()`, `continue()` oder `abort()` abgeschlossen werden.

```js
// Response modifizieren
await page.route('**/api/users', async route => {
  const response = await route.fetch();
  const json = await response.json();

  // Daten manipulieren
  json.push({ id: 99, name: 'Test User' });

  await route.fulfill({
    response, // Original-Response als Basis (Status, Headers)
    json,     // Modifizierter Body
  });
});
```

---

### route.fulfill([options])

```ts
await route.fulfill([options]): Promise<void>
```

Antwortet auf die abgefangene Anfrage mit einer Mock-Response. Beendet das Routing.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.body` | string \| Buffer | No | — | Response-Body als String oder Buffer |
| `options.contentType` | string | No | — | `Content-Type`-Header (automatisch gesetzt fuer `json` und `path`) |
| `options.headers` | Object<string,string> | No | — | Response-Header |
| `options.json` | Serializable | No | — | JSON-Objekt als Body; setzt `Content-Type: application/json` automatisch |
| `options.path` | string | No | — | Pfad zu einer Datei, die als Response-Body dient |
| `options.response` | APIResponse | No | — | Basis-Response (Overrides einzelner Felder moeglich) |
| `options.status` | number | No | 200 | HTTP-Status-Code |

**Returns:** `Promise<void>`

```js
// Einfaches JSON-Mock
await page.route('**/api/user', route => route.fulfill({
  status: 200,
  json: { id: 1, name: 'Alice', role: 'admin' },
}));

// Fehler simulieren
await page.route('**/api/orders', route => route.fulfill({
  status: 500,
  body: 'Internal Server Error',
  contentType: 'text/plain',
}));

// Datei als Response
await page.route('**/data.json', route => route.fulfill({
  path: 'fixtures/data.json',
}));

// Echte Response als Basis + Modifikation
await page.route('**/api/**', async route => {
  const response = await route.fetch();
  await route.fulfill({
    response,
    headers: { ...response.headers(), 'X-Modified': 'true' },
  });
});
```

---

### route.request()

```ts
route.request(): Request
```

Gibt die `Request`-Instanz der abgefangenen Anfrage zurueck.

**Returns:** `Request`

```js
await page.route('**', route => {
  const req = route.request();
  console.log('Intercepted:', req.method(), req.url());
  route.continue();
});
```

---

## Typische Verwendungsmuster

```js
// Pattern 1: Alle Anfragen loggen + durchlassen
await context.route('**', route => {
  console.log(route.request().url());
  route.continue();
});

// Pattern 2: Offline-Verhalten testen
await page.route('**/api/**', route => route.abort('internetdisconnected'));

// Pattern 3: Schnelle Tests ohne echte Netzwerkanfragen
await page.route('**/graphql', route => route.fulfill({
  json: { data: { products: [] } },
}));

// Pattern 4: Response-Modifikation (Spy + Transform)
await page.route('**/prices', async route => {
  const response = await route.fetch();
  const prices = await response.json();
  const doubled = prices.map(p => ({ ...p, price: p.price * 2 }));
  await route.fulfill({ response, json: doubled });
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 6 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `Route` ist das zentrale Objekt fuer Netzwerk-Interception und -Mocking. `fulfill()` ist fuer vollstaendiges Mocking, `continue()` fuer passthrough mit optionaler Modifikation, `fetch()` fuer Response-Transformation und `abort()` fuer das Blockieren von Anfragen. Jede Route-Handler-Funktion MUSS die Route genau einmal behandeln.

---

Source: https://playwright.dev/docs/api/class-route
