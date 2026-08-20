# class-route

`Route` represents an intercepted network request in the context of a route handler (registered via `page.route()`, `browserContext.route()`). Every route must be handled exactly once with `fulfill()`, `continue()`, `abort()` or `fallback()`.

Methods: 6 | Properties: 0 | Events: 0

---

## Contents

- [Methods](#methods)
- [Typical usage patterns](#typical-usage-patterns)
- [Manifest](#manifest)

## Methods

### route.abort([errorCode])

```ts
await route.abort([errorCode]): Promise<void>
```

Aborts the request. The browser receives a network error.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `errorCode` | string | No | `"failed"` | Kind of error |

**Possible error codes:**

| Code | Description |
|------|-------------|
| `"aborted"` | Operation was aborted |
| `"accessdenied"` | Access denied |
| `"addressunreachable"` | Address unreachable |
| `"blockedbyclient"` | Blocked by the client |
| `"blockedbyresponse"` | Blocked by the response |
| `"connectionaborted"` | Connection aborted |
| `"connectionclosed"` | Connection closed |
| `"connectionfailed"` | Connection failed |
| `"connectionrefused"` | Connection refused |
| `"connectionreset"` | Connection reset |
| `"internetdisconnected"` | No internet connection |
| `"namenotresolved"` | DNS resolution failed |
| `"timedout"` | Timeout |
| `"failed"` | Generic error (default) |

**Returns:** `Promise<void>`

```js
// Block all trackers
await page.route('**tracking**', route => route.abort());

// Block images with a specific error
await page.route('**/*.{png,jpg,gif}', route => route.abort('blockedbyclient'));
```

---

### route.continue([options])

```ts
await route.continue([options]): Promise<void>
```

Forwards the request to the network, unchanged or modified. The request is actually executed.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | Override HTTP headers (applies to the original and to redirect requests) |
| `options.method` | string | No | — | Override the HTTP method (original request only) |
| `options.postData` | string \| Buffer \| Serializable | No | — | Override the request body (original request only) |
| `options.url` | string | No | — | Override the URL (must keep the same protocol; original request only) |

**Returns:** `Promise<void>`

```js
// Let the request pass through unchanged
await page.route('**', route => route.continue());

// Add an Authorization header
await page.route('**/api/**', route => route.continue({
  headers: {
    ...route.request().headers(),
    'Authorization': 'Bearer token123',
  },
}));

// Change method and body
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

Hands control over to the next matching route handler (when several handlers are registered for the same URL). If no further handler exists, the request is forwarded to the network. Accepts the same options as `continue()` for modification.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | Header overrides |
| `options.method` | string | No | — | Method override |
| `options.postData` | string \| Buffer \| Serializable | No | — | Body override |
| `options.url` | string | No | — | URL override |

**Returns:** `Promise<void>`

```js
// First handler: logging
await context.route('**', route => {
  console.log('Request:', route.request().url());
  route.fallback(); // call the next handler
});

// Second handler: specific mocking
await page.route('**/api/users', route => route.fulfill({
  json: [{ id: 1, name: 'Alice' }],
}));
```

---

### route.fetch([options])

```ts
await route.fetch([options]): Promise<APIResponse>
```

Executes the request and returns the response without completing the route. Allows reading and/or modifying the real response before returning it to the browser.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.headers` | Object<string,string> | No | — | Header overrides for the executed request |
| `options.maxRedirects` | number | No | 20 | Maximum number of automatic redirects |
| `options.maxRetries` | number | No | 0 | Retries on network errors |
| `options.method` | string | No | — | HTTP method override |
| `options.postData` | string \| Buffer \| Serializable | No | — | Body override |
| `options.timeout` | number | No | 30000 | Timeout in ms |
| `options.url` | string | No | — | URL override |

**Returns:** `Promise<APIResponse>`

**Important:** After `route.fetch()`, the route must still be completed with `fulfill()`, `continue()` or `abort()`.

```js
// Modify the response
await page.route('**/api/users', async route => {
  const response = await route.fetch();
  const json = await response.json();

  // Manipulate the data
  json.push({ id: 99, name: 'Test User' });

  await route.fulfill({
    response, // original response as the basis (status, headers)
    json,     // modified body
  });
});
```

---

### route.fulfill([options])

```ts
await route.fulfill([options]): Promise<void>
```

Answers the intercepted request with a mock response. Ends the routing.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.body` | string \| Buffer | No | — | Response body as a string or buffer |
| `options.contentType` | string | No | — | `Content-Type` header (set automatically for `json` and `path`) |
| `options.headers` | Object<string,string> | No | — | Response headers |
| `options.json` | Serializable | No | — | JSON object as the body; sets `Content-Type: application/json` automatically |
| `options.path` | string | No | — | Path to a file that serves as the response body |
| `options.response` | APIResponse | No | — | Base response (overrides of individual fields possible) |
| `options.status` | number | No | 200 | HTTP status code |

**Returns:** `Promise<void>`

```js
// Simple JSON mock
await page.route('**/api/user', route => route.fulfill({
  status: 200,
  json: { id: 1, name: 'Alice', role: 'admin' },
}));

// Simulate an error
await page.route('**/api/orders', route => route.fulfill({
  status: 500,
  body: 'Internal Server Error',
  contentType: 'text/plain',
}));

// File as the response
await page.route('**/data.json', route => route.fulfill({
  path: 'fixtures/data.json',
}));

// Real response as basis + modification
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

Returns the `Request` instance of the intercepted request.

**Returns:** `Request`

```js
await page.route('**', route => {
  const req = route.request();
  console.log('Intercepted:', req.method(), req.url());
  route.continue();
});
```

---

## Typical usage patterns

```js
// Pattern 1: log all requests + let them pass
await context.route('**', route => {
  console.log(route.request().url());
  route.continue();
});

// Pattern 2: test offline behavior
await page.route('**/api/**', route => route.abort('internetdisconnected'));

// Pattern 3: fast tests without real network requests
await page.route('**/graphql', route => route.fulfill({
  json: { data: { products: [] } },
}));

// Pattern 4: response modification (spy + transform)
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

**Conclusion:** `Route` is the central object for network interception and mocking. `fulfill()` is for complete mocking, `continue()` for passthrough with optional modification, `fetch()` for response transformation and `abort()` for blocking requests. Every route handler function MUST handle the route exactly once.

---

Source: https://playwright.dev/docs/api/class-route
