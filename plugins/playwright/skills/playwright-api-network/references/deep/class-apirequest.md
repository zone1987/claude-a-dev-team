# class-apirequest

`APIRequest` ist eine Singleton-Klasse, die ueber `playwright.request` (im eigenstaendigen Betrieb) oder `test.request` (im Test-Framework) zugaenglich ist. Sie dient als Factory fuer `APIRequestContext`-Instanzen.

Methoden: 1 | Properties: 0 | Events: 0

---

## Methods

### apiRequest.newContext([options])

```ts
await apiRequest.newContext([options]): Promise<APIRequestContext>
```

Erstellt eine neue, isolierte `APIRequestContext`-Instanz fuer HTTP-API-Tests. Die Instanz verwaltet eigenstaendige Cookies und hat keinen Bezug zu einem Browser-Context.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | Context-Konfiguration |
| `options.baseURL` | string | No | — | Basis-URL fuer relative Anfrage-Pfade (verwendet Node.js URL-Konstruktor-Regeln) |
| `options.clientCertificates` | Array<Object> | No | — | TLS-Client-Zertifikate: `{ origin, certPath?, cert?, keyPath?, key?, pfxPath?, pfx?, passphrase? }` |
| `options.extraHTTPHeaders` | Object<string,string> | No | — | Zusaetzliche Header, die bei jeder Anfrage gesendet werden |
| `options.failOnStatusCode` | boolean | No | false | Wirft Exception bei Non-2xx/3xx Status-Codes |
| `options.httpCredentials` | Object | No | — | HTTP-Basic/Digest-Auth: `{ username, password, origin?, send? }` |
| `options.ignoreHTTPSErrors` | boolean | No | false | TLS/SSL-Zertifikatsfehler ignorieren |
| `options.maxRedirects` | number | No | 20 | Maximale Anzahl automatischer Redirects; `0` = keine Redirects |
| `options.proxy` | Object | No | — | Proxy: `{ server, bypass?, username?, password? }` |
| `options.storageState` | string \| Object | No | — | Initialen Context-State aus Datei oder Objekt laden (Cookies + LocalStorage) |
| `options.timeout` | number | No | 30000 | Standard-Response-Timeout in Millisekunden |
| `options.userAgent` | string | No | — | Custom User-Agent-String |

**Returns:** `Promise<APIRequestContext>`

```js
// Eigenstaendiger API-Test (ausserhalb von @playwright/test)
const { request } = require('playwright');

const context = await request.newContext({
  baseURL: 'https://api.example.com',
  extraHTTPHeaders: {
    'Authorization': 'Bearer mytoken123',
    'Accept': 'application/json',
  },
  timeout: 10000,
});

const response = await context.get('/users');
console.log(await response.json());

await context.dispose();
```

```js
// Im @playwright/test Framework
import { test, expect } from '@playwright/test';

test('API-Test', async ({ request }) => {
  // request ist eine vorkonfigurierte APIRequestContext-Instanz
  const response = await request.post('/auth/login', {
    data: { username: 'user', password: 'pass' },
  });
  expect(response.ok()).toBeTruthy();
});
```

```js
// Konfiguration in playwright.config.ts
export default defineConfig({
  use: {
    baseURL: 'https://api.example.com',
    extraHTTPHeaders: {
      'Authorization': `Bearer ${process.env.API_TOKEN}`,
    },
  },
});
```

---

## Beziehung zu BrowserContext.request

Jeder `BrowserContext` hat automatisch eine `APIRequestContext`-Instanz unter `context.request` (bzw. `page.request`). Diese teilt Cookies mit dem Browser-Context — Anmeldungen im Browser gelten auch fuer API-Requests und umgekehrt.

`apiRequest.newContext()` erstellt einen **unabhaengigen** Context ohne Verbindung zu einem Browser.

```js
// Cookies zwischen Browser und API teilen (via browserContext.request)
await page.goto('https://example.com/login');
await page.fill('#username', 'user');
await page.fill('#password', 'pass');
await page.click('[type=submit]');

// Dieselbe Session fuer API-Tests verwenden
const response = await page.request.get('https://example.com/api/profile');
const profile = await response.json();
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 1 |
| Properties | 0 |
| Events | 0 |

**Fazit:** `APIRequest` ist ein schlankes Factory-Objekt mit einer einzigen Methode. `newContext()` erstellt isolierte HTTP-Clients mit voller Konfiguration fuer Basis-URL, Auth, TLS, Proxies und Timeouts. Im `@playwright/test`-Framework wird der `request`-Fixture automatisch bereitgestellt.

---

Source: https://playwright.dev/docs/api/class-apirequest
