# Playwright API Testing - Complete Reference

Playwright enables complete API testing without a browser via
`APIRequestContext`. No browser launch required.

---

## Contents

- [1. Basic Configuration](#1-basic-configuration)
- [2. request Fixture](#2-request-fixture)
- [3. APIRequestContext - All Methods](#3-apirequestcontext---all-methods)
- [4. APIResponse - All Methods](#4-apiresponse---all-methods)
- [5. Manual Context](#5-manual-context)
- [6. Context-bound vs. Isolated Request](#6-context-bound-vs-isolated-request)
- [7. Combining UI + API](#7-combining-ui-api)
- [8. Lifecycle Hooks](#8-lifecycle-hooks)
- [9. Reusing Auth State](#9-reusing-auth-state)

## 1. Basic Configuration

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
    // Proxy for all API requests
    proxy: {
      server: 'http://my-proxy:8080',
      username: 'user',
      password: 'secret',
    },
    // Ignore HTTPS errors
    ignoreHTTPSErrors: true,
  },
});
```

---

## 2. request Fixture

The `request` fixture is available in every test and respects `baseURL`
and `extraHTTPHeaders` from the configuration.

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

## 3. APIRequestContext - All Methods

### Common Options (for all HTTP methods)

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `data` | `string \| Buffer \| Serializable` | - | Request body; objects become JSON (Content-Type: application/json) |
| `failOnStatusCode` | `boolean` | `false` | Throw an exception on non-2xx/3xx responses |
| `form` | `Object \| FormData` | - | URL-encoded form data (application/x-www-form-urlencoded) |
| `headers` | `Object<string, string>` | - | Additional/overriding HTTP headers |
| `ignoreHTTPSErrors` | `boolean` | `false` | Ignore TLS errors |
| `maxRedirects` | `number` | `20` | Max. automatic redirects (0 = disabled) |
| `maxRetries` | `number` | `0` | Retries on network errors |
| `multipart` | `FormData \| Object` | - | Multipart form data (multipart/form-data) |
| `params` | `Object \| URLSearchParams \| string` | - | Query parameters (appended to the URL) |
| `timeout` | `number` | `30000` | Timeout in ms (0 = no timeout) |

---

### request.get(url, options?)

```typescript
// Simple GET
const response = await request.get('/users');

// With query parameters (Object)
const response = await request.get('/search', {
  params: { q: 'playwright', page: 1, per_page: 20 },
});

// With query parameters (URLSearchParams)
const params = new URLSearchParams();
params.set('q', 'playwright');
params.append('page', '1');
const response = await request.get('/search', { params });

// With query parameters (String)
const response = await request.get('/search', { params: 'q=playwright&page=1' });

// With headers
const response = await request.get('/protected', {
  headers: { 'Authorization': `Bearer ${token}` },
});
```

---

### request.post(url, options?)

```typescript
// JSON body (object is serialized automatically)
const response = await request.post('/users', {
  data: { name: 'Alice', email: 'alice@example.com' },
});

// URL-encoded form
const response = await request.post('/login', {
  form: { username: 'alice', password: 'secret' },
});

// Multipart with file upload (native FormData)
const form = new FormData();
form.set('name', 'Alice');
form.append('avatar', new File(['<svg>...</svg>'], 'avatar.svg', { type: 'image/svg+xml' }));
const response = await request.post('/upload', { multipart: form });

// Multipart as an object
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

// Raw string body
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
// No body with HEAD
```

---

### request.fetch(urlOrRequest, options?)

Generic method; accepts a URL or an existing `Request` object (e.g.
from `route.request()`).

| Extra option | Type | Description |
|--------------|-----|--------------|
| `method` | `string` | HTTP verb (default: GET if not specified) |

```typescript
// Arbitrary method
const response = await request.fetch('/api/data', { method: 'OPTIONS' });

// Reuse the Request object (inside a route handler)
await page.route('**/api/**', async route => {
  const response = await request.fetch(route.request());
  await route.fulfill({ response });
});
```

---

### request.storageState(options?)

Stores or returns the current auth state (cookies, local storage).

| Option | Type | Description |
|--------|-----|--------------|
| `path` | `string` | File path to save to (relative to cwd) |
| `indexedDB` | `boolean` | Include an IndexedDB snapshot (default: false, from v1.51) |

```typescript
// Save the state after login
await request.post('/login', { data: { user: 'alice', password: 'secret' } });
await request.storageState({ path: 'playwright/.auth/alice.json' });

// Return the state without saving
const state = await request.storageState();
console.log(state.cookies);
```

---

### request.dispose(options?)

Releases all stored responses (memory management).

```typescript
// Always call this after a manually created context
await apiContext.dispose();

// With a reason (from v1.45)
await apiContext.dispose({ reason: 'Test finished' });
```

---

## 4. APIResponse - All Methods

| Method | Returns | Description |
|---------|-----------|--------------|
| `response.ok()` | `boolean` | Status 200-299 |
| `response.status()` | `number` | HTTP status code |
| `response.statusText()` | `string` | HTTP status text |
| `response.url()` | `string` | Final URL (after redirects) |
| `response.headers()` | `Object<string, string>` | Headers (lowercase) |
| `response.headersArray()` | `Promise<Array<{name,value}>>` | Headers as an array |
| `response.headerValue(name)` | `Promise<string \| null>` | Single header |
| `response.headerValues(name)` | `Promise<string[]>` | All values for one header |
| `response.body()` | `Promise<Buffer>` | Body as a Buffer |
| `response.text()` | `Promise<string>` | Body as a string |
| `response.json()` | `Promise<any>` | Body as parsed JSON |
| `response.dispose()` | `Promise<void>` | Release memory |

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

## 5. Manual Context

For advanced configuration or isolated cookie management.

```typescript
import { request } from '@playwright/test';

test.beforeAll(async () => {
  apiContext = await request.newContext({
    baseURL: 'https://api.github.com',
    extraHTTPHeaders: {
      'Authorization': `token ${process.env.TOKEN}`,
    },
    // Certificate configuration
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

## 6. Context-bound vs. Isolated Request

### Context-bound (shares cookies with the browser)

Accessed via `page.request` or `context.request`.

```typescript
test('shared cookies', async ({ page, context }) => {
  // Cookies from the browser context are sent automatically
  const response = await page.request.get('/api/profile');
  expect(response.ok()).toBeTruthy();
});
```

### Isolated (own cookie management)

Created via `playwright.request.newContext()`.

```typescript
test('isolated cookies', async ({ playwright, browser }) => {
  const apiRequest = await playwright.request.newContext();

  // Cookies stay isolated within apiRequest
  await apiRequest.get('/api/login');

  // Explicitly transfer to the browser context if needed
  const state = await apiRequest.storageState();
  const browserContext = await browser.newContext({ storageState: state });

  await apiRequest.dispose();
  await browserContext.close();
});
```

---

## 7. Combining UI + API

### Set up preconditions via the API

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
  // Prepare the server state via the API
  const issue = await apiContext.post('/repos/owner/repo/issues', {
    data: { title: '[Feature] My new feature' },
  });
  const { number } = await issue.json();

  // Validate the UI
  await page.goto('https://github.com/owner/repo/issues');
  await expect(page.locator('a[data-hovercard-type="issue"]').first())
    .toHaveText('[Feature] My new feature');

  // Clean up
  await apiContext.delete(`/repos/owner/repo/issues/${number}`);
});
```

### Validate postconditions via the API

```typescript
test('ui action creates server state', async ({ page, request }) => {
  await page.goto('https://github.com/owner/repo/issues');
  await page.getByText('New Issue').click();
  await page.getByLabel('Title').fill('Bug: Something broken');
  await page.getByText('Submit new issue').click();
  await page.waitForURL(/\/issues\/\d+/);

  const issueNumber = page.url().split('/').pop();

  // Check the server state via the API
  const response = await request.get(`/repos/owner/repo/issues/${issueNumber}`);
  expect(response.ok()).toBeTruthy();
  const issue = await response.json();
  expect(issue.title).toBe('Bug: Something broken');
});
```

---

## 8. Lifecycle Hooks

```typescript
test.beforeAll(async ({ request }) => {
  // Prepare the server state globally
  await request.post('/test/seed', { data: { scenario: 'default' } });
});

test.afterAll(async ({ request }) => {
  // Clean up
  await request.delete('/test/cleanup');
});

test.beforeEach(async ({ request }) => {
  // Per-test state
  await request.post('/test/reset');
});
```

---

## 9. Reusing Auth State

```typescript
// 1. Log in via the API, save the state
const context = await request.newContext();
await context.post('https://example.com/api/login', {
  data: { username: 'admin', password: 'secret' },
});
await context.storageState({ path: 'playwright/.auth/admin.json' });
await context.dispose();

// 2. Browser context with the saved state
const browserCtx = await browser.newContext({
  storageState: 'playwright/.auth/admin.json',
});
```

---

Source: https://playwright.dev/docs/api-testing | https://playwright.dev/docs/api/class-apirequestcontext
