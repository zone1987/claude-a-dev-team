# Playwright Network - Vollstaendige Referenz

Playwright erlaubt vollstaendige Kontrolle ueber HTTP/HTTPS-, XHR-, fetch- und
WebSocket-Traffic. Die Interception wird per `page.route()` oder
`context.route()` aktiviert - ohne weitere Konfiguration.

---

## 1. URL-Pattern-Matching

Alle Route-Methoden akzeptieren einen `url`-Parameter als Glob, RegExp oder
Praedikatsfunktion.

### Glob-Regeln

| Zeichen | Bedeutung |
|---------|-----------|
| `*`     | Beliebige Zeichen ausser `/` |
| `**`    | Beliebige Zeichen inkl. `/` |
| `?`     | Fragezeichen literal (NICHT ein Zeichen) |
| `{a,b}` | Alternativen |
| `\`     | Escape-Zeichen |

```typescript
// Alle JS-Dateien auf einer Domain
await page.route('https://example.com/*.js', route => route.abort());

// Alle Bilder, beliebige Domain
await page.route('**/*.{png,jpg,jpeg,gif,webp}', route => route.abort());

// RegExp
await page.route(/\/api\/v\d+\//, handler);

// Praedikat
await page.route(url => url.hostname === 'cdn.example.com', handler);
```

---

## 2. page.route() / context.route()

```typescript
await page.route(url, handler, options?)
await context.route(url, handler, options?)
```

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `url` | `string \| RegExp \| (url: URL) => boolean` | URL-Muster |
| `handler` | `(route: Route, request: Request) => void` | Callback |
| `options.times` | `number` | Wie oft der Handler greift (Standard: unbegrenzt) |

Context-Routes gelten auch fuer Popups und neu geoeffnete Seiten.
Mehrere Handler werden in umgekehrter Registrierungsreihenfolge aufgerufen.

```typescript
// Einmalige Route (times: 1)
await page.route('**/api/data', route => route.fulfill({ json: [] }), { times: 1 });

// Route deregistrieren
const handler = route => route.continue();
await page.route('**/*', handler);
await page.unroute('**/*', handler);

// Alle Routes entfernen
await page.unrouteAll({ behavior: 'ignoreErrors' });
```

---

## 3. Route-Methoden (vollstaendig)

### route.abort(errorCode?)

Bricht die Anfrage mit einem Fehlercode ab.

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `errorCode` | `string` | `'failed'` | Fehlercode |

Erlaubte Fehlercodes:
`aborted`, `accessdenied`, `addressunreachable`, `blockedbyclient`,
`blockedbyresponse`, `connectionaborted`, `connectionclosed`,
`connectionfailed`, `connectionrefused`, `connectionreset`,
`internetdisconnected`, `namenotresolved`, `timedout`, `failed`

```typescript
// CSS-Dateien blockieren
await page.route('**/*.css', route => route.abort());

// Mit spezifischem Fehler
await page.route('**/tracking/**', route => route.abort('blockedbyclient'));
```

---

### route.continue(options?)

Leitet die Anfrage mit optionalen Aenderungen an den Server weiter.

| Option | Typ | Beschreibung |
|--------|-----|--------------|
| `headers` | `Object<string, string>` | Ersetzte/zusaetzliche Header (undefined entfernt Header) |
| `method` | `string` | Neues HTTP-Verb |
| `postData` | `string \| Buffer \| Serializable` | Neuer Request-Body |
| `url` | `string` | Neue URL (gleiches Protokoll erforderlich) |

Hinweis: Sendet sofort - nachfolgende Handler werden uebersprungen.
Bestimmte Header (Cookie, Host, Content-Length) koennen nicht ueberschrieben werden.

```typescript
// Header hinzufuegen
await page.route('**/*', async route => {
  const headers = { ...route.request().headers(), 'X-Custom': 'value' };
  await route.continue({ headers });
});

// Header entfernen
await page.route('**/*', async route => {
  const headers = route.request().headers();
  delete headers['X-Secret'];
  await route.continue({ headers });
});

// Methode und Body aendern
await page.route('**/submit', route => route.continue({ method: 'POST', postData: '{}' }));
```

---

### route.fallback(options?)

Uebergibt die Anfrage an den naechsten passenden Handler (nicht an den Server).
Akzeptiert dieselben Optionen wie `continue()`.

```typescript
// Handler-Kette: erster Handler modifiziert, zweiter bearbeitet
await page.route('**/*', async route => {
  // Wird zuerst ausgefuehrt (umgekehrte Reihenfolge)
  await route.fallback({ headers: { ...route.request().headers(), 'X-Auth': token } });
});
await page.route('**/*', async route => {
  // Wird nach fallback aufgerufen
  await route.continue();
});
```

---

### route.fetch(options?)

Fuehrt die Originalanfrage aus und gibt die Antwort zurueck, ohne sie an den
Browser weiterzuleiten.

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `headers` | `Object<string, string>` | - | Geaenderte Header |
| `maxRedirects` | `number` | `20` | Max. Weiterleitungen (0 = deaktiviert) |
| `maxRetries` | `number` | `0` | Wiederholungen bei Netzwerkfehlern |
| `method` | `string` | - | Geaendertes HTTP-Verb |
| `postData` | `string \| Buffer \| Serializable` | - | Geaenderter Body |
| `timeout` | `number` | `30000` | Timeout in ms (0 = kein Timeout) |
| `url` | `string` | - | Geaenderte URL |

**Gibt zurueck:** `Promise<APIResponse>`

```typescript
// Antwort abrufen und modifizieren
await page.route('**/api/products', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.push({ id: 999, name: 'Extra Product' });
  await route.fulfill({ response, json });
});

// Mit Timeout
await page.route('**/slow-api', async route => {
  const response = await route.fetch({ timeout: 5000 });
  await route.fulfill({ response });
});
```

---

### route.fulfill(options?)

Antwortet auf die Anfrage mit benutzerdefinierten Daten.

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `body` | `string \| Buffer` | - | Response-Body |
| `contentType` | `string` | - | Content-Type-Header |
| `headers` | `Object<string, string>` | - | Response-Header |
| `json` | `Serializable` | - | JSON-Antwort (setzt Content-Type: application/json) |
| `path` | `string` | - | Datei-Pfad als Antwort (Content-Type aus Extension) |
| `response` | `APIResponse` | - | Basis-Response (Felder ueberschreibbar) |
| `status` | `number` | `200` | HTTP-Statuscode |

```typescript
// JSON-Mock
await page.route('**/api/users', route => route.fulfill({
  json: [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }],
}));

// Fehlerantwort
await page.route('**/api/secret', route => route.fulfill({
  status: 403,
  body: 'Forbidden',
}));

// Datei aus Disk
await page.route('**/api/data', route => route.fulfill({
  path: './fixtures/data.json',
}));

// Originale Antwort mit Modifikation
await page.route('**/api/config', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.featureFlag = true;
  await route.fulfill({ response, json });
});

// HTML als String
await page.route('**/page', route => route.fulfill({
  contentType: 'text/html',
  body: '<h1>Mock Page</h1>',
}));
```

---

### route.request()

Gibt das zugehoerige `Request`-Objekt zurueck.

```typescript
await page.route('**/*', async route => {
  const req = route.request();
  console.log(req.method(), req.url());
  await route.continue();
});
```

---

## 4. Request-Objekt (vollstaendige Methoden)

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `request.url()` | `string` | Vollstaendige URL |
| `request.method()` | `string` | HTTP-Verb (GET, POST, ...) |
| `request.headers()` | `Object<string, string>` | Headers (lowercase, ohne Security-Headers) |
| `request.allHeaders()` | `Promise<Object<string, string>>` | Alle Headers inkl. Security (async) |
| `request.headersArray()` | `Promise<Array<{name,value}>>` | Headers als Array (Gross-/Kleinschreibung erhalten) |
| `request.headerValue(name)` | `Promise<string \| null>` | Einzelner Header-Wert (case-insensitive) |
| `request.postData()` | `string \| null` | Request-Body als String |
| `request.postDataBuffer()` | `Buffer \| null` | Request-Body als Buffer |
| `request.postDataJSON()` | `Serializable \| null` | Request-Body als geparste JSON/Form-Daten |
| `request.resourceType()` | `string` | `document`, `stylesheet`, `image`, `script`, `xhr`, `fetch`, `websocket`, ... |
| `request.isNavigationRequest()` | `boolean` | Ist dies eine Navigationsanfrage? |
| `request.frame()` | `Frame` | Ausloesendes Frame |
| `request.serviceWorker()` | `Worker \| null` | Service Worker (nur Chromium) |
| `request.redirectedFrom()` | `Request \| null` | Vorherige Anfrage bei Redirect |
| `request.redirectedTo()` | `Request \| null` | Nachfolgende Anfrage bei Redirect |
| `request.response()` | `Promise<Response \| null>` | Matching Response (wartet) |
| `request.existingResponse()` | `Response \| null` | Response falls bereits erhalten, sonst null |
| `request.failure()` | `{errorText: string} \| null` | Fehlerobjekt bei gescheiterter Anfrage |
| `request.timing()` | `Object` | Resource-Timing-Daten (startTime, domainLookup, connect, ...) |
| `request.sizes()` | `Promise<Object>` | Byte-Groessen (requestBody, requestHeaders, responseBody, responseHeaders) |

```typescript
page.on('requestfailed', request => {
  console.log(request.url(), request.failure()?.errorText);
});

page.on('requestfinished', async request => {
  const timing = request.timing();
  console.log('TTFB:', timing.responseStart - timing.requestStart);
});
```

---

## 5. Response-Objekt (vollstaendige Methoden)

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `response.url()` | `string` | Response-URL |
| `response.status()` | `number` | HTTP-Statuscode |
| `response.statusText()` | `string` | HTTP-Statustext |
| `response.ok()` | `boolean` | true wenn Status 200-299 |
| `response.headers()` | `Object<string, string>` | Headers (lowercase) |
| `response.allHeaders()` | `Promise<Object<string, string>>` | Alle Headers (async) |
| `response.headersArray()` | `Promise<Array<{name,value}>>` | Headers als Array |
| `response.headerValue(name)` | `Promise<string \| null>` | Einzelner Header (mehrere: kommasepariert) |
| `response.headerValues(name)` | `Promise<string[]>` | Alle Werte fuer einen Header (z.B. set-cookie) |
| `response.body()` | `Promise<Buffer>` | Body als Buffer |
| `response.text()` | `Promise<string>` | Body als String |
| `response.json()` | `Promise<Serializable>` | Body als geparste JSON |
| `response.request()` | `Request` | Zugehoerige Anfrage |
| `response.frame()` | `Frame` | Ausloesendes Frame |
| `response.fromServiceWorker()` | `boolean` | Vom Service Worker beantwortet? |
| `response.finished()` | `Promise<null \| Error>` | Wartet auf Abschluss |
| `response.securityDetails()` | `Promise<Object \| null>` | SSL-Infos (issuer, protocol, subjectName, validFrom, validTo) |
| `response.serverAddr()` | `Promise<{ipAddress, port} \| null>` | Server-IP und Port |
| `response.httpVersion()` | `Promise<string>` | HTTP-Protokollversion |

---

## 6. Network-Events auf page

```typescript
// Jede Anfrage
page.on('request', (request: Request) => {
  console.log(request.method(), request.url());
});

// Jede Antwort
page.on('response', (response: Response) => {
  console.log(response.status(), response.url());
});

// Abgeschlossene Anfragen
page.on('requestfinished', (request: Request) => {
  // request.response() ist jetzt verfuegbar
});

// Fehlgeschlagene Anfragen
page.on('requestfailed', (request: Request) => {
  console.log(request.failure()?.errorText);
});

// Warten auf spezifische Anfrage/Antwort
const [request] = await Promise.all([
  page.waitForRequest('**/api/data'),
  page.click('#load'),
]);

const [response] = await Promise.all([
  page.waitForResponse(res => res.url().includes('/api/') && res.status() === 200),
  page.click('#submit'),
]);
```

---

## 7. HAR-Replay mit routeFromHAR

### HAR aufzeichnen (CLI)

```bash
npx playwright open --save-har=recording.har --save-har-glob="**/api/**" https://example.com
```

### HAR aufzeichnen (Code)

```typescript
// Im Playwright-Kontext aufzeichnen
const context = await browser.newContext();
await context.recordHar({ path: 'recording.har', urlFilter: '**/api/**' });
// ... Tests ausfuehren ...
await context.close(); // Schreibt die HAR-Datei

// Oder per Config
use: {
  recordHar: { path: 'recording.har', mode: 'minimal' }
}
```

### HAR wiedergeben

```typescript
// page-Ebene
await page.routeFromHAR('./hars/recording.har', {
  url: '**/api/**',      // Optional: nur diese URLs aus HAR bedienen
  update: false,         // false = Wiedergabe, true = Aktualisierung
  updateMode: 'minimal', // 'full' oder 'minimal'
  notFound: 'abort',     // 'abort' (default) oder 'fallback'
  lazyUpdateCSP: false,  // Content-Security-Policy anpassen (default: false)
});

// context-Ebene (fuer alle Pages)
await context.routeFromHAR('./hars/recording.har', { url: '**/api/**' });
```

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `url` | `string \| RegExp` | - | Nur diese URLs aus HAR bedienen |
| `update` | `boolean` | `false` | true = HAR-Datei aktualisieren statt wiedergeben |
| `updateMode` | `'minimal' \| 'full'` | `'minimal'` | Bei update: minimal nur neue, full alle |
| `notFound` | `'abort' \| 'fallback'` | `'abort'` | Was bei nicht gematchten URLs passiert |
| `lazyUpdateCSP` | `boolean` | `false` | CSP fuer HAR-Inhalte anpassen |

Matching: URL + HTTP-Methode; bei POST auch Payload (strikt).

---

## 8. WebSocket-Routing

```typescript
// WebSocket abfangen
await page.routeWebSocket('wss://example.com/ws', ws => {
  ws.onMessage(message => {
    if (message === 'ping') ws.send('pong');
  });
});

// Pass-Through mit Modifikation
await page.routeWebSocket('wss://api.example.com/stream', ws => {
  const server = ws.connectToServer();

  // Client -> Server
  ws.onMessage(message => {
    const data = JSON.parse(message as string);
    server.send(JSON.stringify({ ...data, authenticated: true }));
  });

  // Server -> Client
  server.onMessage(message => {
    ws.send(message); // unveraendert weiterleiten
  });
});
```

### WebSocketRoute-Methoden

| Methode | Beschreibung |
|---------|--------------|
| `ws.onMessage(handler)` | Empfaengt Nachrichten vom Client |
| `ws.send(message)` | Sendet Nachricht zum Client |
| `ws.connectToServer()` | Verbindet mit dem echten Server, gibt `WebSocketRoute` zurueck |
| `ws.close(options?)` | Schliesst die WebSocket-Verbindung |

### WebSocket-Events auf page

```typescript
page.on('websocket', ws => {
  console.log('WebSocket opened:', ws.url());

  ws.on('framesent', event => console.log('Sent:', event.payload));
  ws.on('framereceived', event => console.log('Received:', event.payload));
  ws.on('close', () => console.log('WebSocket closed'));
});
```

---

## 9. Browser-APIs mocken (addInitScript)

```typescript
// Geolocation-API mocken
await page.addInitScript(() => {
  Object.defineProperty(navigator, 'geolocation', {
    value: {
      getCurrentPosition: (success) => success({
        coords: { latitude: 52.52, longitude: 13.405, accuracy: 1 },
        timestamp: Date.now(),
      }),
    },
  });
});

// Battery API mocken (Beispiel aus Doku)
await page.addInitScript(() => {
  const mockBattery = {
    level: 0.9,
    charging: true,
    chargingTime: 1800,
    dischargingTime: Infinity,
    _listeners: {} as Record<string, Function[]>,
    addEventListener(event: string, cb: Function) {
      (this._listeners[event] ||= []).push(cb);
    },
    removeEventListener(event: string, cb: Function) {
      this._listeners[event] = (this._listeners[event] || []).filter(l => l !== cb);
    },
    _setLevel(level: number) {
      this.level = level;
      (this._listeners['levelchange'] || []).forEach(cb => cb.call(this));
    },
  };
  Object.defineProperty(navigator, 'getBattery', {
    value: () => Promise.resolve(mockBattery),
  });
  (window as any).__mockBattery = mockBattery;
});

// Mock-Zustand aendern
await page.evaluate(() => (window as any).__mockBattery._setLevel(0.1));
```

---

## 10. Service Workers

Service Workers koennen Netzwerkanfragen abfangen und dadurch `page.route()`
umgehen.

```typescript
// Service Workers deaktivieren (empfohlen fuer klare Netzwerk-Tests)
const context = await browser.newContext({ serviceWorkers: 'block' });

// Service Worker beobachten (Chromium-only)
context.on('serviceworker', worker => {
  console.log('Service Worker:', worker.url());
});
```

### Konfigurationsoptionen

| Option | Werte | Default | Beschreibung |
|--------|-------|---------|--------------|
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Service Worker erlauben/blockieren |

---

## 11. HTTP-Auth und Proxy

### HTTP-Auth

```typescript
// Globale Konfiguration (playwright.config.ts)
use: {
  httpCredentials: {
    username: 'user',
    password: 'secret',
  },
}

// Per Context
const context = await browser.newContext({
  httpCredentials: { username: 'user', password: 'secret' },
});
```

### Proxy

```typescript
use: {
  proxy: {
    server: 'http://myproxy:8080',   // Pflichtfeld
    username: 'proxyuser',            // Optional
    password: 'proxysecret',          // Optional
    bypass: 'localhost,127.0.0.1',    // Kommaseparierte Hosts
  },
}
```

---

## 12. Typische Patterns

### Alle Bilder blockieren

```typescript
await context.route(/\.(png|jpg|jpeg|gif|webp|svg)$/i, route => route.abort());
```

### API-Anfragen protokollieren

```typescript
page.on('request', req => {
  if (req.url().includes('/api/')) {
    console.log(`${req.method()} ${req.url()}`);
  }
});
```

### Netzwerk-Fehler simulieren

```typescript
await page.route('**/api/unreliable', async route => {
  if (Math.random() < 0.5) {
    await route.abort('connectionreset');
  } else {
    await route.continue();
  }
});
```

### Antwort-Latenz simulieren

```typescript
await page.route('**/api/**', async route => {
  await new Promise(resolve => setTimeout(resolve, 1000));
  await route.continue();
});
```

---

Quelle: https://playwright.dev/docs/network | https://playwright.dev/docs/mock | https://playwright.dev/docs/mock-browser-apis | https://playwright.dev/docs/api/class-route | https://playwright.dev/docs/api/class-request | https://playwright.dev/docs/api/class-response
