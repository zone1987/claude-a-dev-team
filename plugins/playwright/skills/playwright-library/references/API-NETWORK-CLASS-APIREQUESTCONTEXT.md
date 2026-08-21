# class-apirequestcontext

`APIRequestContext` is Playwright's HTTP client for web API tests. Instances are obtained via `apiRequest.newContext()`, `browserContext.request` or `page.request`. Each instance manages its own cookies and configurable settings.

Methods: 8 | Properties: 1 | Events: 0

---

## Contents

- [Standard request options](#standard-request-options)
- [Methods](#methods)
- [Properties](#properties)
- [Complete usage example (setup + tests)](#complete-usage-example-setup-tests)
- [Manifest](#manifest)

## Standard request options

The following options apply to all HTTP methods (`get`, `post`, `put`, `patch`, `delete`, `head`, `fetch`):

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `data` | string \| Buffer \| Serializable | No | — | Request body; serialized as JSON when object/array, sent directly as string/buffer |
| `failOnStatusCode` | boolean | No | false | Throws an exception on non-2xx/3xx status |
| `form` | Object \| FormData | No | — | URL-encoded form data (`application/x-www-form-urlencoded`) |
| `headers` | Object<string,string> | No | — | Request-specific headers (add to the context headers) |
| `ignoreHTTPSErrors` | boolean | No | false | Ignore TLS errors |
| `maxRedirects` | number | No | 20 | Max. automatic redirects; `0` = no redirects |
| `maxRetries` | number | No | 0 | Retries on network errors |
| `multipart` | FormData \| Object | No | — | Multipart form data (`multipart/form-data`); supports file uploads |
| `params` | Object \| URLSearchParams \| string | No | — | Query parameters (appended to the URL) |
| `timeout` | number | No | 30000 | Request timeout in ms |

**`multipart` object format:**
```js
{
  fieldName: string | number | boolean | ReadStream | Buffer | {
    name: string,      // File name
    mimeType: string,  // MIME type
    buffer: Buffer,    // File content
  }
}
```

---

## Methods

### apiRequestContext.delete(url[, options])

```ts
await apiRequestContext.delete(url[, options]): Promise<APIResponse>
```

Sends an HTTP DELETE request.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL (absolute or relative to `baseURL`) |
| `options` | Object | No | — | Standard request options (see above) |

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

Releases all resources of the context (cookies, cached responses, connections). All subsequent calls throw exceptions. Must be called after all tests have finished when the context is not managed by Playwright.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.reason` | string | No | — | Reason for the disposal (for logging/debugging) |

**Returns:** `Promise<void>`

```js
const context = await request.newContext({ baseURL: 'https://api.example.com' });
try {
  // Run tests
} finally {
  await context.dispose();
}
```

---

### apiRequestContext.fetch(urlOrRequest[, options])

```ts
await apiRequestContext.fetch(urlOrRequest[, options]): Promise<APIResponse>
```

Sends an HTTP request with a freely chosen method. Accepts a URL string or an existing `Request` instance.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `urlOrRequest` | string \| Request | Yes | — | Target URL or request object |
| `options` | Object | No | — | Standard request options plus: |
| `options.method` | string | No | `"GET"` | HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, etc.) |

**Returns:** `Promise<APIResponse>`

```js
// With method override
const response = await request.fetch('https://api.example.com/books', {
  method: 'POST',
  data: { title: 'Playwright Testing', author: 'Alice' },
});

// Multipart upload
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

Sends an HTTP GET request with optional query parameters.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL |
| `options` | Object | No | — | Standard request options |

**Returns:** `Promise<APIResponse>`

```js
// Simple GET
const response = await request.get('https://api.example.com/users');
expect(response.ok()).toBeTruthy();

// With query parameters as an object
const response = await request.get('/api/products', {
  params: { category: 'electronics', page: 2, limit: 20 },
});

// With URLSearchParams
const params = new URLSearchParams({ isbn: '9783161484100', page: '1' });
const response = await request.get('/api/books', { params });

// With a string query
const response = await request.get('/api/search', { params: 'q=playwright&lang=de' });
```

---

### apiRequestContext.head(url[, options])

```ts
await apiRequestContext.head(url[, options]): Promise<APIResponse>
```

Sends an HTTP HEAD request. Returns headers only, no body.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL |
| `options` | Object | No | — | Standard request options |

**Returns:** `Promise<APIResponse>`

```js
// Check resource existence
const response = await request.head('/api/users/42');
expect(response.status()).toBe(200);

// Retrieve Content-Length without downloading
const headers = response.headers();
console.log('Content-Length:', headers['content-length']);
```

---

### apiRequestContext.patch(url[, options])

```ts
await apiRequestContext.patch(url[, options]): Promise<APIResponse>
```

Sends an HTTP PATCH request for partial resource updates.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL |
| `options` | Object | No | — | Standard request options |

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

Sends an HTTP POST request. Supports JSON, form data and multipart.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL |
| `options` | Object | No | — | Standard request options |

**Returns:** `Promise<APIResponse>`

```js
// JSON body
const response = await request.post('/api/users', {
  data: { name: 'Alice', email: 'alice@example.com', role: 'admin' },
});
const user = await response.json();
expect(user.id).toBeDefined();

// URL-encoded form
const loginResponse = await request.post('/auth/login', {
  form: { username: 'alice', password: 'secret' },
});

// Multipart with file upload
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

Sends an HTTP PUT request for completely replacing a resource.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `url` | string | Yes | — | Target URL |
| `options` | Object | No | — | Standard request options |

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

Returns the current storage state of the context (cookies and local storage). Can be saved for later reuse.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.indexedDB` | boolean | No | false | Include IndexedDB in the snapshot |
| `options.path` | string | No | — | File path for saving (relative to cwd) |

**Returns:** `Promise<StorageState>` with the structure:
```ts
{
  cookies: Array<{
    name: string,
    value: string,
    domain: string,
    path: string,
    expires: number,    // Unix timestamp
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
// Log in via API, then save state for browser tests
const loginResponse = await request.post('/auth/login', {
  data: { username: 'admin', password: 'secret' },
});
expect(loginResponse.ok()).toBeTruthy();

// Save cookies for later browser context use
await request.storageState({ path: 'playwright/.auth/admin.json' });
```

---

## Properties

### apiRequestContext.tracing

**Type:** `Tracing`

Provides access to Playwright tracing for this request context. Enables recording API request traces for error analysis.

```js
await context.tracing.start({ snapshots: true });
await context.get('/api/users');
await context.tracing.stop({ path: 'api-trace.zip' });
```

---

## Complete usage example (setup + tests)

```js
// playwright.config.ts - global setup for auth
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

  if (!response.ok()) throw new Error('Login failed');

  await context.storageState({ path: 'playwright/.auth/user.json' });
  await context.dispose();
}

// user.spec.ts - tests with an authenticated request
import { test, expect } from '@playwright/test';

test('retrieve user profile', async ({ request }) => {
  const response = await request.get('/api/profile');
  expect(response.ok()).toBeTruthy();

  const profile = await response.json();
  expect(profile.username).toBe('testuser');
});

test('create and delete user', async ({ request }) => {
  // Create
  const createResponse = await request.post('/api/users', {
    data: { name: 'Test User', email: 'test@example.com' },
  });
  expect(createResponse.status()).toBe(201);
  const { id } = await createResponse.json();

  // Delete
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

**Summary:** `APIRequestContext` is the complete HTTP client for Playwright API tests. `post()` with `data` (JSON), `form` (URL-encoded) or `multipart` (file upload) covers all common content types. `storageState()` is the key mechanism for transferring auth state between API setup and browser tests.

---

Source: https://playwright.dev/docs/api/class-apirequestcontext
