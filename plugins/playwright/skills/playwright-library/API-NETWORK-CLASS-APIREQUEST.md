# class-apirequest

`APIRequest` is a singleton class accessible via `playwright.request` (in standalone operation) or `test.request` (in the test framework). It serves as a factory for `APIRequestContext` instances.

Methods: 1 | Properties: 0 | Events: 0

---

## Contents

- [Methods](#methods)
- [Relationship to BrowserContext.request](#relationship-to-browsercontextrequest)
- [Manifest](#manifest)

## Methods

### apiRequest.newContext([options])

```ts
await apiRequest.newContext([options]): Promise<APIRequestContext>
```

Creates a new, isolated `APIRequestContext` instance for HTTP API tests. The instance manages its own cookies and has no relation to a browser context.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | Context configuration |
| `options.baseURL` | string | No | — | Base URL for relative request paths (uses Node.js URL constructor rules) |
| `options.clientCertificates` | Array<Object> | No | — | TLS client certificates: `{ origin, certPath?, cert?, keyPath?, key?, pfxPath?, pfx?, passphrase? }` |
| `options.extraHTTPHeaders` | Object<string,string> | No | — | Additional headers sent with every request |
| `options.failOnStatusCode` | boolean | No | false | Throws an exception on non-2xx/3xx status codes |
| `options.httpCredentials` | Object | No | — | HTTP basic/digest auth: `{ username, password, origin?, send? }` |
| `options.ignoreHTTPSErrors` | boolean | No | false | Ignore TLS/SSL certificate errors |
| `options.maxRedirects` | number | No | 20 | Maximum number of automatic redirects; `0` = no redirects |
| `options.proxy` | Object | No | — | Proxy: `{ server, bypass?, username?, password? }` |
| `options.storageState` | string \| Object | No | — | Load the initial context state from a file or object (cookies + local storage) |
| `options.timeout` | number | No | 30000 | Default response timeout in milliseconds |
| `options.userAgent` | string | No | — | Custom user agent string |

**Returns:** `Promise<APIRequestContext>`

```js
// Standalone API test (outside of @playwright/test)
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
// Inside the @playwright/test framework
import { test, expect } from '@playwright/test';

test('API test', async ({ request }) => {
  // request is a preconfigured APIRequestContext instance
  const response = await request.post('/auth/login', {
    data: { username: 'user', password: 'pass' },
  });
  expect(response.ok()).toBeTruthy();
});
```

```js
// Configuration in playwright.config.ts
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

## Relationship to BrowserContext.request

Every `BrowserContext` automatically has an `APIRequestContext` instance under `context.request` (or `page.request`). It shares cookies with the browser context — logins in the browser also apply to API requests and vice versa.

`apiRequest.newContext()` creates an **independent** context with no connection to a browser.

```js
// Share cookies between browser and API (via browserContext.request)
await page.goto('https://example.com/login');
await page.fill('#username', 'user');
await page.fill('#password', 'pass');
await page.click('[type=submit]');

// Use the same session for API tests
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

**Conclusion:** `APIRequest` is a lean factory object with a single method. `newContext()` creates isolated HTTP clients with full configuration for base URL, auth, TLS, proxies and timeouts. In the `@playwright/test` framework, the `request` fixture is provided automatically.

---

Source: https://playwright.dev/docs/api/class-apirequest
