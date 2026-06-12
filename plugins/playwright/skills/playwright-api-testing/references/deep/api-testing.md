# Playwright API Testing - Vollstaendige Referenz

Playwright ermoeglicht vollstaendiges API-Testing ohne Browser ueber
`APIRequestContext`. Kein Browser-Launch erforderlich.

---

## 1. Grundkonfiguration

### playwright.config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    baseURL: 'https://api.github.com',
    extraHTTPHeaders: {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': `token ${process.env.API_TOKEN}`,
    },
    // Proxy fuer alle API-Anfragen
    proxy: {
      server: 'http://my-proxy:8080',
      username: 'user',
      password: 'secret',
    },
    // HTTPS-Fehler ignorieren
    ignoreHTTPSErrors: true,
  },
});
```

---

## 2. request-Fixture

Das `request`-Fixture ist in jedem Test verfuegbar und respektiert `baseURL`
und `extraHTTPHeaders` aus der Konfiguration.

```typescript
import { test, expect } from '@playwright/test';

test('create and verify issue', async ({ request }) => {
  const created = await request.post('/repos/owner/repo/issues', {
    data: { title: 'Bug report', body: 'Details here' },
  });
  expect(created.ok()).toBeTruthy();
  expect(created.status()).toBe(201);

  const list = await request.get('/repos/owner/repo/issues');
  const issues = await list.json();
  expect(issues).toContainEqual(expect.objectContaining({ title: 'Bug report' }));
});
```

---

## 3. APIRequestContext - Alle Methoden

### Gemeinsame Optionen (fuer alle HTTP-Methoden)

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `data` | `string \| Buffer \| Serializable` | - | Request-Body; Objekte werden zu JSON (Content-Type: application/json) |
| `failOnStatusCode` | `boolean` | `false` | Exception bei non-2xx/3xx Antworten |
| `form` | `Object \| FormData` | - | URL-kodierte Formulardaten (application/x-www-form-urlencoded) |
| `headers` | `Object<string, string>` | - | Zusaetzliche/ueberschreibende HTTP-Header |
| `ignoreHTTPSErrors` | `boolean` | `false` | TLS-Fehler ignorieren |
| `maxRedirects` | `number` | `20` | Max. automatische Weiterleitungen (0 = deaktiviert) |
| `maxRetries` | `number` | `0` | Wiederholungen bei Netzwerkfehlern |
| `multipart` | `FormData \| Object` | - | Multipart-Formulardaten (multipart/form-data) |
| `params` | `Object \| URLSearchParams \| string` | - | Query-Parameter (werden an URL angehaengt) |
| `timeout` | `number` | `30000` | Timeout in ms (0 = kein Timeout) |

---

### request.get(url, options?)

```typescript
// Einfaches GET
const response = await request.get('/users');

// Mit Query-Parametern (Object)
const response = await request.get('/search', {
  params: { q: 'playwright', page: 1, per_page: 20 },
});

// Mit Query-Parametern (URLSearchParams)
const params = new URLSearchParams();
params.set('q', 'playwright');
params.append('page', '1');
const response = await request.get('/search', { params });

// Mit Query-Parametern (String)
const response = await request.get('/search', { params: 'q=playwright&page=1' });

// Mit Headern
const response = await request.get('/protected', {
  headers: { 'Authorization': `Bearer ${token}` },
});
```

---

### request.post(url, options?)

```typescript
// JSON-Body (Objekt wird automatisch serialisiert)
const response = await request.post('/users', {
  data: { name: 'Alice', email: 'alice@example.com' },
});

// URL-encoded Form
const response = await request.post('/login', {
  form: { username: 'alice', password: 'secret' },
});

// Multipart mit Datei-Upload (native FormData)
const form = new FormData();
form.set('name', 'Alice');
form.append('avatar', new File(['<svg>...</svg>'], 'avatar.svg', { type: 'image/svg+xml' }));
const response = await request.post('/upload', { multipart: form });

// Multipart als Objekt
const response = await request.post('/upload', {
  multipart: {
    name: 'Alice',
    file: {
      name: 'data.csv',
      mimeType: 'text/csv',
      buffer: Buffer.from('a,b,c\n1,2,3'),
    },
  },
});

// Raw-String-Body
const response = await request.post('/raw', {
  data: 'plain text body',
  headers: { 'Content-Type': 'text/plain' },
});
```

---

### request.put(url, options?)

```typescript
const response = await request.put(`/users/${id}`, {
  data: { name: 'Updated Name' },
});
expect(response.ok()).toBeTruthy();
```

---

### request.patch(url, options?)

```typescript
const response = await request.patch(`/users/${id}`, {
  data: { email: 'new@example.com' },
});
```

---

### request.delete(url, options?)

```typescript
const response = await request.delete(`/users/${id}`);
expect(response.status()).toBe(204);
```

---

### request.head(url, options?)

```typescript
const response = await request.head('/health');
expect(response.ok()).toBeTruthy();
// Kein Body bei HEAD
```

---

### request.fetch(urlOrRequest, options?)

Generische Methode; akzeptiert URL oder bestehendes `Request`-Objekt (z.B.
aus `route.request()`).

| Zusatzoption | Typ | Beschreibung |
|--------------|-----|--------------|
| `method` | `string` | HTTP-Verb (Default: GET wenn nicht angegeben) |

```typescript
// Beliebige Methode
const response = await request.fetch('/api/data', { method: 'OPTIONS' });

// Request-Objekt weiterverwenden (in Route-Handler)
await page.route('**/api/**', async route => {
  const response = await request.fetch(route.request());
  await route.fulfill({ response });
});
```

---

### request.storageState(options?)

Speichert oder gibt den aktuellen Auth-Zustand (Cookies, LocalStorage) zurueck.

| Option | Typ | Beschreibung |
|--------|-----|--------------|
| `path` | `string` | Dateipfad zum Speichern (relativ zu cwd) |
| `indexedDB` | `boolean` | IndexedDB-Snapshot einschliessen (default: false, ab v1.51) |

```typescript
// Zustand nach Login speichern
await request.post('/login', { data: { user: 'alice', password: 'secret' } });
await request.storageState({ path: 'playwright/.auth/alice.json' });

// Zustand zurueckgeben ohne Speichern
const state = await request.storageState();
console.log(state.cookies);
```

---

### request.dispose(options?)

Gibt alle gespeicherten Responses frei (Speicher-Management).

```typescript
// Nach manuell erstelltem Context immer aufrufen
await apiContext.dispose();

// Mit Grund (ab v1.45)
await apiContext.dispose({ reason: 'Test beendet' });
```

---

## 4. APIResponse - Alle Methoden

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `response.ok()` | `boolean` | Status 200-299 |
| `response.status()` | `number` | HTTP-Statuscode |
| `response.statusText()` | `string` | HTTP-Statustext |
| `response.url()` | `string` | Finale URL (nach Redirects) |
| `response.headers()` | `Object<string, string>` | Headers (lowercase) |
| `response.headersArray()` | `Promise<Array<{name,value}>>` | Headers als Array |
| `response.headerValue(name)` | `Promise<string \| null>` | Einzelner Header |
| `response.headerValues(name)` | `Promise<string[]>` | Alle Werte fuer einen Header |
| `response.body()` | `Promise<Buffer>` | Body als Buffer |
| `response.text()` | `Promise<string>` | Body als String |
| `response.json()` | `Promise<any>` | Body als geparste JSON |
| `response.dispose()` | `Promise<void>` | Speicher freigeben |

```typescript
const response = await request.post('/users', { data: { name: 'Alice' } });

expect(response.ok()).toBeTruthy();
expect(response.status()).toBe(201);

const user = await response.json();
expect(user.id).toBeDefined();
expect(user.name).toBe('Alice');

const location = await response.headerValue('location');
expect(location).toMatch(/\/users\/\d+/);
```

---

## 5. Manueller Context

Fuer erweiterte Konfiguration oder isolierte Cookie-Verwaltung.

```typescript
import { request } from '@playwright/test';

test.beforeAll(async () => {
  apiContext = await request.newContext({
    baseURL: 'https://api.github.com',
    extraHTTPHeaders: {
      'Authorization': `token ${process.env.TOKEN}`,
    },
    // Zertifikat-Konfiguration
    clientCertificates: [{
      origin: 'https://api.example.com',
      certPath: './cert.pem',
      keyPath: './key.pem',
    }],
  });
});

test.afterAll(async () => {
  await apiContext.dispose();
});
```

---

## 6. Kontext-gebundener vs. isolierter Request

### Kontext-gebunden (teilt Cookies mit Browser)

Zugriff ueber `page.request` oder `context.request`.

```typescript
test('shared cookies', async ({ page, context }) => {
  // Cookies aus dem Browser-Kontext werden automatisch mitgesendet
  const response = await page.request.get('/api/profile');
  expect(response.ok()).toBeTruthy();
});
```

### Isoliert (eigene Cookie-Verwaltung)

Erstellt ueber `playwright.request.newContext()`.

```typescript
test('isolated cookies', async ({ playwright, browser }) => {
  const apiRequest = await playwright.request.newContext();

  // Cookies bleiben in apiRequest isoliert
  await apiRequest.get('/api/login');

  // Explizit in Browser-Kontext uebertragen wenn noetig
  const state = await apiRequest.storageState();
  const browserContext = await browser.newContext({ storageState: state });

  await apiRequest.dispose();
  await browserContext.close();
});
```

---

## 7. UI + API kombinieren

### Vorbedingungen per API setzen

```typescript
let apiContext: APIRequestContext;

test.beforeAll(async ({ playwright }) => {
  apiContext = await playwright.request.newContext({
    baseURL: 'https://api.github.com',
    extraHTTPHeaders: { 'Authorization': `token ${process.env.TOKEN}` },
  });
});

test.afterAll(async () => {
  await apiContext.dispose();
});

test('newest issue first in list', async ({ page }) => {
  // Server-Zustand per API vorbereiten
  const issue = await apiContext.post('/repos/owner/repo/issues', {
    data: { title: '[Feature] My new feature' },
  });
  const { number } = await issue.json();

  // UI validieren
  await page.goto('https://github.com/owner/repo/issues');
  await expect(page.locator('a[data-hovercard-type="issue"]').first())
    .toHaveText('[Feature] My new feature');

  // Aufraumen
  await apiContext.delete(`/repos/owner/repo/issues/${number}`);
});
```

### Nachbedingungen per API validieren

```typescript
test('ui action creates server state', async ({ page, request }) => {
  await page.goto('https://github.com/owner/repo/issues');
  await page.getByText('New Issue').click();
  await page.getByLabel('Title').fill('Bug: Something broken');
  await page.getByText('Submit new issue').click();
  await page.waitForURL(/\/issues\/\d+/);

  const issueNumber = page.url().split('/').pop();

  // Server-Zustand per API pruefen
  const response = await request.get(`/repos/owner/repo/issues/${issueNumber}`);
  expect(response.ok()).toBeTruthy();
  const issue = await response.json();
  expect(issue.title).toBe('Bug: Something broken');
});
```

---

## 8. Lifecycle-Hooks

```typescript
test.beforeAll(async ({ request }) => {
  // Server-Zustand global vorbereiten
  await request.post('/test/seed', { data: { scenario: 'default' } });
});

test.afterAll(async ({ request }) => {
  // Aufraumen
  await request.delete('/test/cleanup');
});

test.beforeEach(async ({ request }) => {
  // Pro-Test-Zustand
  await request.post('/test/reset');
});
```

---

## 9. Auth-Zustand wiederverwenden

```typescript
// 1. Login per API, Zustand speichern
const context = await request.newContext();
await context.post('https://example.com/api/login', {
  data: { username: 'admin', password: 'secret' },
});
await context.storageState({ path: 'playwright/.auth/admin.json' });
await context.dispose();

// 2. Browser-Kontext mit gespeichertem Zustand
const browserCtx = await browser.newContext({
  storageState: 'playwright/.auth/admin.json',
});
```

---

Quelle: https://playwright.dev/docs/api-testing | https://playwright.dev/docs/api/class-apirequestcontext
