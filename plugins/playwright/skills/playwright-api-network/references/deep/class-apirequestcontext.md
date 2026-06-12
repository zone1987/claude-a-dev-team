# class-apirequestcontext

`APIRequestContext` ist der HTTP-Client von Playwright fuer Web-API-Tests. Instanzen werden via `apiRequest.newContext()`, `browserContext.request` oder `page.request` erhalten. Jede Instanz verwaltet eigenstaendige Cookies und konfigurierbare Einstellungen.

Methoden: 8 | Properties: 1 | Events: 0

---

## Standard-Request-Optionen

Die folgenden Optionen gelten fuer alle HTTP-Methoden (`get`, `post`, `put`, `patch`, `delete`, `head`, `fetch`):

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `data` | string \| Buffer \| Serializable | No | — | Request-Body; wird als JSON serialisiert wenn Objekt/Array, als String/Buffer direkt |
| `failOnStatusCode` | boolean | No | false | Wirft Exception bei Non-2xx/3xx Status |
| `form` | Object \| FormData | No | — | URL-kodierte Form-Daten (`application/x-www-form-urlencoded`) |
| `headers` | Object<string,string> | No | — | Anfragespezifische Header (ergaenzen Context-Header) |
| `ignoreHTTPSErrors` | boolean | No | false | TLS-Fehler ignorieren |
| `maxRedirects` | number | No | 20 | Max. automatische Redirects; `0` = keine Redirects |
| `maxRetries` | number | No | 0 | Wiederholungen bei Netzwerkfehlern |
| `multipart` | FormData \| Object | No | — | Multipart-Formulardaten (`multipart/form-data`); unterstuetzt File-Uploads |
| `params` | Object \| URLSearchParams \| string | No | — | Query-Parameter (werden an URL angehaengt) |
| `timeout` | number | No | 30000 | Request-Timeout in ms |

**`multipart`-Objekt-Format:**
```js
{
  fieldName: string | number | boolean | ReadStream | Buffer | {
    name: string,      // Dateiname
    mimeType: string,  // MIME-Typ
    buffer: Buffer,    // Dateiinhalt
  }
}
```

---

## Methods

### apiRequestContext.delete(url[, options])

```ts
await apiRequestContext.delete(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-DELETE-Request.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL (absolut oder relativ zu `baseURL`) |
| `options` | Object | No | — | Standard-Request-Optionen (s. oben) |

**Returns:** `Promise<APIResponse>`

```js
const response = await request.delete('/api/users/42');
expect(response.status()).toBe(204);
```

---

### apiRequestContext.dispose([options])

```ts
await apiRequestContext.dispose([options]): Promise<void>
```

Gibt alle Ressourcen des Contexts frei (Cookies, gecachte Responses, Verbindungen). Alle nachfolgenden Aufrufe werfen Exceptions. Muss nach Abschluss aller Tests aufgerufen werden wenn der Context nicht von Playwright verwaltet wird.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.reason` | string | No | — | Grund fuer die Freigabe (fuer Logging/Debugging) |

**Returns:** `Promise<void>`

```js
const context = await request.newContext({ baseURL: 'https://api.example.com' });
try {
  // Tests durchfuehren
} finally {
  await context.dispose();
}
```

---

### apiRequestContext.fetch(urlOrRequest[, options])

```ts
await apiRequestContext.fetch(urlOrRequest[, options]): Promise<APIResponse>
```

Sendet einen HTTP-Request mit freier Methodenwahl. Akzeptiert eine URL-String oder eine bestehende `Request`-Instanz.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `urlOrRequest` | string \| Request | Yes | — | Ziel-URL oder Request-Objekt |
| `options` | Object | No | — | Standard-Request-Optionen plus: |
| `options.method` | string | No | `"GET"` | HTTP-Methode (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, etc.) |

**Returns:** `Promise<APIResponse>`

```js
// Mit Methoden-Override
const response = await request.fetch('https://api.example.com/books', {
  method: 'POST',
  data: { title: 'Playwright Testing', author: 'Alice' },
});

// Multipart-Upload
const form = new FormData();
form.append('file', new File(['content'], 'report.pdf', { type: 'application/pdf' }));
form.append('description', 'Monthly report');
const uploadResponse = await request.fetch('/api/upload', {
  method: 'POST',
  multipart: form,
});
```

---

### apiRequestContext.get(url[, options])

```ts
await apiRequestContext.get(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-GET-Request mit optionalen Query-Parametern.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL |
| `options` | Object | No | — | Standard-Request-Optionen |

**Returns:** `Promise<APIResponse>`

```js
// Einfacher GET
const response = await request.get('https://api.example.com/users');
expect(response.ok()).toBeTruthy();

// Mit Query-Parametern als Objekt
const response = await request.get('/api/products', {
  params: { category: 'electronics', page: 2, limit: 20 },
});

// Mit URLSearchParams
const params = new URLSearchParams({ isbn: '9783161484100', page: '1' });
const response = await request.get('/api/books', { params });

// Mit String-Query
const response = await request.get('/api/search', { params: 'q=playwright&lang=de' });
```

---

### apiRequestContext.head(url[, options])

```ts
await apiRequestContext.head(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-HEAD-Request. Gibt nur Header zurueck, keinen Body.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL |
| `options` | Object | No | — | Standard-Request-Optionen |

**Returns:** `Promise<APIResponse>`

```js
// Ressource-Existenz pruefen
const response = await request.head('/api/users/42');
expect(response.status()).toBe(200);

// Content-Length ohne Download abrufen
const headers = response.headers();
console.log('Content-Length:', headers['content-length']);
```

---

### apiRequestContext.patch(url[, options])

```ts
await apiRequestContext.patch(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-PATCH-Request fuer partielle Ressourcen-Updates.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL |
| `options` | Object | No | — | Standard-Request-Optionen |

**Returns:** `Promise<APIResponse>`

```js
const response = await request.patch('/api/users/42', {
  data: { email: 'newemail@example.com' },
});
expect(response.status()).toBe(200);
```

---

### apiRequestContext.post(url[, options])

```ts
await apiRequestContext.post(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-POST-Request. Unterstuetzt JSON, Form-Daten und Multipart.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL |
| `options` | Object | No | — | Standard-Request-Optionen |

**Returns:** `Promise<APIResponse>`

```js
// JSON-Body
const response = await request.post('/api/users', {
  data: { name: 'Alice', email: 'alice@example.com', role: 'admin' },
});
const user = await response.json();
expect(user.id).toBeDefined();

// URL-kodierte Form
const loginResponse = await request.post('/auth/login', {
  form: { username: 'alice', password: 'secret' },
});

// Multipart mit Datei-Upload
const fileContent = Buffer.from('column1,column2\nvalue1,value2');
const importResponse = await request.post('/api/import', {
  multipart: {
    file: {
      name: 'data.csv',
      mimeType: 'text/csv',
      buffer: fileContent,
    },
    type: 'csv',
  },
});
```

---

### apiRequestContext.put(url[, options])

```ts
await apiRequestContext.put(url[, options]): Promise<APIResponse>
```

Sendet einen HTTP-PUT-Request fuer vollstaendiges Ersetzen einer Ressource.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Ziel-URL |
| `options` | Object | No | — | Standard-Request-Optionen |

**Returns:** `Promise<APIResponse>`

```js
const response = await request.put('/api/users/42', {
  data: {
    id: 42,
    name: 'Alice Updated',
    email: 'alice@example.com',
    role: 'admin',
  },
});
expect(response.ok()).toBeTruthy();
```

---

### apiRequestContext.storageState([options])

```ts
await apiRequestContext.storageState([options]): Promise<StorageState>
```

Gibt den aktuellen Storage-State des Contexts zurueck (Cookies und LocalStorage). Kann fuer spaetere Wiederverwendung gespeichert werden.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.indexedDB` | boolean | No | false | IndexedDB in Snapshot einschliessen |
| `options.path` | string | No | — | Dateipfad zum Speichern (relativ zu cwd) |

**Returns:** `Promise<StorageState>` mit Struktur:
```ts
{
  cookies: Array<{
    name: string,
    value: string,
    domain: string,
    path: string,
    expires: number,    // Unix-Timestamp
    httpOnly: boolean,
    secure: boolean,
    sameSite: "Strict" | "Lax" | "None"
  }>,
  origins: Array<{
    origin: string,
    localStorage: Array<{
      name: string,
      value: string
    }>
  }>
}
```

```js
// Login via API, dann State fuer Browser-Tests speichern
const loginResponse = await request.post('/auth/login', {
  data: { username: 'admin', password: 'secret' },
});
expect(loginResponse.ok()).toBeTruthy();

// Cookies fuer spaetere Browser-Context-Verwendung speichern
await request.storageState({ path: 'playwright/.auth/admin.json' });
```

---

## Properties

### apiRequestContext.tracing

**Type:** `Tracing`

Bietet Zugriff auf Playwright Tracing fuer diesen Request-Context. Ermoeglicht das Aufzeichnen von API-Request-Traces zur Fehleranalyse.

```js
await context.tracing.start({ snapshots: true });
await context.get('/api/users');
await context.tracing.stop({ path: 'api-trace.zip' });
```

---

## Vollstaendiges Nutzungsbeispiel (Setup + Tests)

```js
// playwright.config.ts - Global Setup fuer Auth
import { defineConfig } from '@playwright/test';

export default defineConfig({
  globalSetup: './global-setup.ts',
  use: {
    storageState: 'playwright/.auth/user.json',
  },
});

// global-setup.ts
import { request } from '@playwright/test';

export default async function setup() {
  const context = await request.newContext({
    baseURL: 'https://api.example.com',
  });

  const response = await context.post('/auth/login', {
    data: { username: 'testuser', password: 'testpass' },
  });

  if (!response.ok()) throw new Error('Login fehlgeschlagen');

  await context.storageState({ path: 'playwright/.auth/user.json' });
  await context.dispose();
}

// user.spec.ts - Tests mit authentifiziertem Request
import { test, expect } from '@playwright/test';

test('Benutzerprofil abrufen', async ({ request }) => {
  const response = await request.get('/api/profile');
  expect(response.ok()).toBeTruthy();

  const profile = await response.json();
  expect(profile.username).toBe('testuser');
});

test('Benutzer erstellen und loeschen', async ({ request }) => {
  // Erstellen
  const createResponse = await request.post('/api/users', {
    data: { name: 'Test User', email: 'test@example.com' },
  });
  expect(createResponse.status()).toBe(201);
  const { id } = await createResponse.json();

  // Loeschen
  const deleteResponse = await request.delete(`/api/users/${id}`);
  expect(deleteResponse.status()).toBe(204);
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 8 |
| Properties | 1 |
| Events | 0 |

**Fazit:** `APIRequestContext` ist der vollstaendige HTTP-Client fuer Playwright API-Tests. `post()` mit `data` (JSON), `form` (URL-encoded) oder `multipart` (Datei-Upload) deckt alle gaengigen Content-Types ab. `storageState()` ist der Schluesselmechanismus fuer den Auth-State-Transfer zwischen API-Setup und Browser-Tests.

---

Source: https://playwright.dev/docs/api/class-apirequestcontext
