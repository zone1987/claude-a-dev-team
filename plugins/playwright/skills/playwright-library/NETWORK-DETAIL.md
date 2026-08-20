# Playwright Network - Complete Reference

Playwright allows complete control over HTTP/HTTPS, XHR, fetch and
WebSocket traffic. Interception is enabled via `page.route()` or
`context.route()` - without any further configuration.

---

## Contents

- [1. URL Pattern Matching](#1-url-pattern-matching)
- [2. page.route() / context.route()](#2-pageroute-contextroute)
- [3. Route Methods (complete)](#3-route-methods-complete)
- [4. Request Object (complete methods)](#4-request-object-complete-methods)
- [5. Response Object (complete methods)](#5-response-object-complete-methods)
- [6. Network Events on page](#6-network-events-on-page)
- [7. HAR Replay with routeFromHAR](#7-har-replay-with-routefromhar)
- [8. WebSocket Routing](#8-websocket-routing)
- [9. Mocking Browser APIs (addInitScript)](#9-mocking-browser-apis-addinitscript)
- [10. Service Workers](#10-service-workers)
- [11. HTTP Auth and Proxy](#11-http-auth-and-proxy)
- [12. Typical Patterns](#12-typical-patterns)

## 1. URL Pattern Matching

All route methods accept a `url` parameter as a glob, RegExp or
predicate function.

### Glob rules

| Character | Meaning |
|---------|-----------|
| `*`     | Any characters except `/` |
| `**`    | Any characters including `/` |
| `?`     | Literal question mark (NOT a single character) |
| `{a,b}` | Alternatives |
| `\`     | Escape character |

```typescript
// All JS files on one domain
await page.route('https://example.com/*.js', route => route.abort());

// All images, any domain
await page.route('**/*.{png,jpg,jpeg,gif,webp}', route => route.abort());

// RegExp
await page.route(/\/api\/v\d+\//, handler);

// Predicate
await page.route(url => url.hostname === 'cdn.example.com', handler);
```

---

## 2. page.route() / context.route()

```typescript
await page.route(url, handler, options?)
await context.route(url, handler, options?)
```

| Parameter | Type | Description |
|-----------|-----|--------------|
| `url` | `string \| RegExp \| (url: URL) => boolean` | URL pattern |
| `handler` | `(route: Route, request: Request) => void` | Callback |
| `options.times` | `number` | How often the handler applies (default: unlimited) |

Context routes also apply to popups and newly opened pages.
Multiple handlers are invoked in reverse registration order.

```typescript
// One-time route (times: 1)
await page.route('**/api/data', route => route.fulfill({ json: [] }), { times: 1 });

// Deregister a route
const handler = route => route.continue();
await page.route('**/*', handler);
await page.unroute('**/*', handler);

// Remove all routes
await page.unrouteAll({ behavior: 'ignoreErrors' });
```

---

## 3. Route Methods (complete)

### route.abort(errorCode?)

Aborts the request with an error code.

| Parameter | Type | Default | Description |
|-----------|-----|---------|--------------|
| `errorCode` | `string` | `'failed'` | Error code |

Allowed error codes:
`aborted`, `accessdenied`, `addressunreachable`, `blockedbyclient`,
`blockedbyresponse`, `connectionaborted`, `connectionclosed`,
`connectionfailed`, `connectionrefused`, `connectionreset`,
`internetdisconnected`, `namenotresolved`, `timedout`, `failed`

```typescript
// Block CSS files
await page.route('**/*.css', route => route.abort());

// With a specific error
await page.route('**/tracking/**', route => route.abort('blockedbyclient'));
```

---

### route.continue(options?)

Forwards the request to the server with optional modifications.

| Option | Type | Description |
|--------|-----|--------------|
| `headers` | `Object<string, string>` | Replaced/additional headers (undefined removes a header) |
| `method` | `string` | New HTTP verb |
| `postData` | `string \| Buffer \| Serializable` | New request body |
| `url` | `string` | New URL (same protocol required) |

Note: Sends immediately - subsequent handlers are skipped.
Certain headers (Cookie, Host, Content-Length) cannot be overridden.

```typescript
// Add a header
await page.route('**/*', async route => {
  const headers = { ...route.request().headers(), 'X-Custom': 'value' };
  await route.continue({ headers });
});

// Remove a header
await page.route('**/*', async route => {
  const headers = route.request().headers();
  delete headers['X-Secret'];
  await route.continue({ headers });
});

// Change method and body
await page.route('**/submit', route => route.continue({ method: 'POST', postData: '{}' }));
```

---

### route.fallback(options?)

Passes the request to the next matching handler (not to the server).
Accepts the same options as `continue()`.

```typescript
// Handler chain: first handler modifies, second one handles it
await page.route('**/*', async route => {
  // Runs first (reverse order)
  await route.fallback({ headers: { ...route.request().headers(), 'X-Auth': token } });
});
await page.route('**/*', async route => {
  // Called after fallback
  await route.continue();
});
```

---

### route.fetch(options?)

Performs the original request and returns the response without forwarding it to the
browser.

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `headers` | `Object<string, string>` | - | Modified headers |
| `maxRedirects` | `number` | `20` | Max. redirects (0 = disabled) |
| `maxRetries` | `number` | `0` | Retries on network errors |
| `method` | `string` | - | Modified HTTP verb |
| `postData` | `string \| Buffer \| Serializable` | - | Modified body |
| `timeout` | `number` | `30000` | Timeout in ms (0 = no timeout) |
| `url` | `string` | - | Modified URL |

**Returns:** `Promise<APIResponse>`

```typescript
// Fetch and modify the response
await page.route('**/api/products', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.push({ id: 999, name: 'Extra Product' });
  await route.fulfill({ response, json });
});

// With timeout
await page.route('**/slow-api', async route => {
  const response = await route.fetch({ timeout: 5000 });
  await route.fulfill({ response });
});
```

---

### route.fulfill(options?)

Responds to the request with custom data.

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `body` | `string \| Buffer` | - | Response body |
| `contentType` | `string` | - | Content-Type header |
| `headers` | `Object<string, string>` | - | Response headers |
| `json` | `Serializable` | - | JSON response (sets Content-Type: application/json) |
| `path` | `string` | - | File path as the response (Content-Type from extension) |
| `response` | `APIResponse` | - | Base response (fields can be overridden) |
| `status` | `number` | `200` | HTTP status code |

```typescript
// JSON mock
await page.route('**/api/users', route => route.fulfill({
  json: [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }],
}));

// Error response
await page.route('**/api/secret', route => route.fulfill({
  status: 403,
  body: 'Forbidden',
}));

// File from disk
await page.route('**/api/data', route => route.fulfill({
  path: './fixtures/data.json',
}));

// Original response with modification
await page.route('**/api/config', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.featureFlag = true;
  await route.fulfill({ response, json });
});

// HTML as a string
await page.route('**/page', route => route.fulfill({
  contentType: 'text/html',
  body: '<h1>Mock Page</h1>',
}));
```

---

### route.request()

Returns the associated `Request` object.

```typescript
await page.route('**/*', async route => {
  const req = route.request();
  console.log(req.method(), req.url());
  await route.continue();
});
```

---

## 4. Request Object (complete methods)

| Method | Returns | Description |
|---------|-----------|--------------|
| `request.url()` | `string` | Complete URL |
| `request.method()` | `string` | HTTP verb (GET, POST, ...) |
| `request.headers()` | `Object<string, string>` | Headers (lowercase, without security headers) |
| `request.allHeaders()` | `Promise<Object<string, string>>` | All headers including security ones (async) |
| `request.headersArray()` | `Promise<Array<{name,value}>>` | Headers as an array (letter case preserved) |
| `request.headerValue(name)` | `Promise<string \| null>` | Single header value (case-insensitive) |
| `request.postData()` | `string \| null` | Request body as a string |
| `request.postDataBuffer()` | `Buffer \| null` | Request body as a buffer |
| `request.postDataJSON()` | `Serializable \| null` | Request body as parsed JSON/form data |
| `request.resourceType()` | `string` | `document`, `stylesheet`, `image`, `script`, `xhr`, `fetch`, `websocket`, ... |
| `request.isNavigationRequest()` | `boolean` | Is this a navigation request? |
| `request.frame()` | `Frame` | Triggering frame |
| `request.serviceWorker()` | `Worker \| null` | Service worker (Chromium only) |
| `request.redirectedFrom()` | `Request \| null` | Previous request on a redirect |
| `request.redirectedTo()` | `Request \| null` | Subsequent request on a redirect |
| `request.response()` | `Promise<Response \| null>` | Matching response (waits) |
| `request.existingResponse()` | `Response \| null` | Response if already received, otherwise null |
| `request.failure()` | `{errorText: string} \| null` | Error object for a failed request |
| `request.timing()` | `Object` | Resource timing data (startTime, domainLookup, connect, ...) |
| `request.sizes()` | `Promise<Object>` | Byte sizes (requestBody, requestHeaders, responseBody, responseHeaders) |

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

## 5. Response Object (complete methods)

| Method | Returns | Description |
|---------|-----------|--------------|
| `response.url()` | `string` | Response URL |
| `response.status()` | `number` | HTTP status code |
| `response.statusText()` | `string` | HTTP status text |
| `response.ok()` | `boolean` | true when status is 200-299 |
| `response.headers()` | `Object<string, string>` | Headers (lowercase) |
| `response.allHeaders()` | `Promise<Object<string, string>>` | All headers (async) |
| `response.headersArray()` | `Promise<Array<{name,value}>>` | Headers as an array |
| `response.headerValue(name)` | `Promise<string \| null>` | Single header (multiple: comma-separated) |
| `response.headerValues(name)` | `Promise<string[]>` | All values for one header (e.g. set-cookie) |
| `response.body()` | `Promise<Buffer>` | Body as a buffer |
| `response.text()` | `Promise<string>` | Body as a string |
| `response.json()` | `Promise<Serializable>` | Body as parsed JSON |
| `response.request()` | `Request` | Associated request |
| `response.frame()` | `Frame` | Triggering frame |
| `response.fromServiceWorker()` | `boolean` | Answered by the service worker? |
| `response.finished()` | `Promise<null \| Error>` | Waits for completion |
| `response.securityDetails()` | `Promise<Object \| null>` | SSL info (issuer, protocol, subjectName, validFrom, validTo) |
| `response.serverAddr()` | `Promise<{ipAddress, port} \| null>` | Server IP and port |
| `response.httpVersion()` | `Promise<string>` | HTTP protocol version |

---

## 6. Network Events on page

```typescript
// Every request
page.on('request', (request: Request) => {
  console.log(request.method(), request.url());
});

// Every response
page.on('response', (response: Response) => {
  console.log(response.status(), response.url());
});

// Completed requests
page.on('requestfinished', (request: Request) => {
  // request.response() is now available
});

// Failed requests
page.on('requestfailed', (request: Request) => {
  console.log(request.failure()?.errorText);
});

// Waiting for a specific request/response
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

## 7. HAR Replay with routeFromHAR

### Recording a HAR (CLI)

```bash
npx playwright open --save-har=recording.har --save-har-glob="**/api/**" https://example.com
```

### Recording a HAR (code)

```typescript
// Record inside the Playwright context
const context = await browser.newContext();
await context.recordHar({ path: 'recording.har', urlFilter: '**/api/**' });
// ... run tests ...
await context.close(); // Writes the HAR file

// Or via config
use: {
  recordHar: { path: 'recording.har', mode: 'minimal' }
}
```

### Replaying a HAR

```typescript
// page level
await page.routeFromHAR('./hars/recording.har', {
  url: '**/api/**',      // Optional: serve only these URLs from the HAR
  update: false,         // false = replay, true = update
  updateMode: 'minimal', // 'full' or 'minimal'
  notFound: 'abort',     // 'abort' (default) or 'fallback'
  lazyUpdateCSP: false,  // Adjust the Content-Security-Policy (default: false)
});

// context level (for all pages)
await context.routeFromHAR('./hars/recording.har', { url: '**/api/**' });
```

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `url` | `string \| RegExp` | - | Serve only these URLs from the HAR |
| `update` | `boolean` | `false` | true = update the HAR file instead of replaying |
| `updateMode` | `'minimal' \| 'full'` | `'minimal'` | On update: minimal only new ones, full all |
| `notFound` | `'abort' \| 'fallback'` | `'abort'` | What happens for unmatched URLs |
| `lazyUpdateCSP` | `boolean` | `false` | Adjust CSP for HAR content |

Matching: URL + HTTP method; for POST also the payload (strict).

---

## 8. WebSocket Routing

```typescript
// Intercept a WebSocket
await page.routeWebSocket('wss://example.com/ws', ws => {
  ws.onMessage(message => {
    if (message === 'ping') ws.send('pong');
  });
});

// Pass-through with modification
await page.routeWebSocket('wss://api.example.com/stream', ws => {
  const server = ws.connectToServer();

  // Client -> Server
  ws.onMessage(message => {
    const data = JSON.parse(message as string);
    server.send(JSON.stringify({ ...data, authenticated: true }));
  });

  // Server -> Client
  server.onMessage(message => {
    ws.send(message); // forward unchanged
  });
});
```

### WebSocketRoute methods

| Method | Description |
|---------|--------------|
| `ws.onMessage(handler)` | Receives messages from the client |
| `ws.send(message)` | Sends a message to the client |
| `ws.connectToServer()` | Connects to the real server, returns a `WebSocketRoute` |
| `ws.close(options?)` | Closes the WebSocket connection |

### WebSocket events on page

```typescript
page.on('websocket', ws => {
  console.log('WebSocket opened:', ws.url());

  ws.on('framesent', event => console.log('Sent:', event.payload));
  ws.on('framereceived', event => console.log('Received:', event.payload));
  ws.on('close', () => console.log('WebSocket closed'));
});
```

---

## 9. Mocking Browser APIs (addInitScript)

```typescript
// Mock the geolocation API
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

// Mock the Battery API (example from the docs)
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

// Change the mock state
await page.evaluate(() => (window as any).__mockBattery._setLevel(0.1));
```

---

## 10. Service Workers

Service workers can intercept network requests and thereby bypass
`page.route()`.

```typescript
// Disable service workers (recommended for clean network tests)
const context = await browser.newContext({ serviceWorkers: 'block' });

// Observe a service worker (Chromium only)
context.on('serviceworker', worker => {
  console.log('Service Worker:', worker.url());
});
```

### Configuration options

| Option | Values | Default | Description |
|--------|-------|---------|--------------|
| `serviceWorkers` | `'allow' \| 'block'` | `'allow'` | Allow/block service workers |

---

## 11. HTTP Auth and Proxy

### HTTP auth

```typescript
// Global configuration (playwright.config.ts)
use: {
  httpCredentials: {
    username: 'user',
    password: 'secret',
  },
}

// Per context
const context = await browser.newContext({
  httpCredentials: { username: 'user', password: 'secret' },
});
```

### Proxy

```typescript
use: {
  proxy: {
    server: 'http://myproxy:8080',   // Required field
    username: 'proxyuser',            // Optional
    password: 'proxysecret',          // Optional
    bypass: 'localhost,127.0.0.1',    // Comma-separated hosts
  },
}
```

---

## 12. Typical Patterns

### Block all images

```typescript
await context.route(/\.(png|jpg|jpeg|gif|webp|svg)$/i, route => route.abort());
```

### Log API requests

```typescript
page.on('request', req => {
  if (req.url().includes('/api/')) {
    console.log(`${req.method()} ${req.url()}`);
  }
});
```

### Simulate network errors

```typescript
await page.route('**/api/unreliable', async route => {
  if (Math.random() < 0.5) {
    await route.abort('connectionreset');
  } else {
    await route.continue();
  }
});
```

### Simulate response latency

```typescript
await page.route('**/api/**', async route => {
  await new Promise(resolve => setTimeout(resolve, 1000));
  await route.continue();
});
```

---

Source: https://playwright.dev/docs/network | https://playwright.dev/docs/mock | https://playwright.dev/docs/mock-browser-apis | https://playwright.dev/docs/api/class-route | https://playwright.dev/docs/api/class-request | https://playwright.dev/docs/api/class-response
