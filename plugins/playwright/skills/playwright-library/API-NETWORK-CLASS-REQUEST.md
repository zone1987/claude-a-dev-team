# class-request

`Request` represents an HTTP request initiated by a Playwright page. Instances are obtained through page/context events (`on('request')`) or as parameters of route handlers. The object is read-only.

Methods: 15 | Properties: 0 | Events: 0

---

## Methods

### request.allHeaders()

```ts
await request.allHeaders(): Promise<Object<string, string>>
```

Returns all HTTP request headers as an object. Header names are lowercase. Also includes security-relevant headers (`cookie`, etc.) that are omitted by `headers()`.

**Returns:** `Promise<Object<string, string>>`

```js
const headers = await request.allHeaders();
console.log(headers['content-type']);
```

---

### request.existingResponse()

```ts
request.existingResponse(): Response | null
```

Returns the response immediately if it has already been received — without waiting. Returns `null` when no response is available yet.

**Returns:** `Response | null`

```js
const response = request.existingResponse();
if (response) {
  console.log('Status:', response.status());
}
```

---

### request.failure()

```ts
request.failure(): { errorText: string } | null
```

Returns an object with the error text when the request has failed. Returns `null` for successful requests. Typically used in `requestfailed` events.

**Returns:** `{ errorText: string } | null`

```js
page.on('requestfailed', request => {
  console.log(request.url(), request.failure()?.errorText);
});
```

---

### request.frame()

```ts
request.frame(): Frame
```

Returns the `Frame` that initiated this request.

**Returns:** `Frame`

**Note:** Throws an exception when the frame is not available (e.g. for service worker requests or very early navigation requests).

```js
const frame = request.frame();
console.log('Frame URL:', frame.url());
```

---

### request.headerValue(name)

```ts
await request.headerValue(name): Promise<string | null>
```

Returns the value of a single request header (case-insensitive).

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header name (capitalization irrelevant) |

**Returns:** `Promise<string | null>` — `null` when the header is absent

```js
const contentType = await request.headerValue('Content-Type');
```

---

### request.headers()

```ts
request.headers(): Object<string, string>
```

Returns request headers as an object (synchronously). Excludes security-relevant headers such as `cookie` and internal Playwright headers. Use `allHeaders()` for complete headers.

**Returns:** `Object<string, string>`

---

### request.headersArray()

```ts
await request.headersArray(): Promise<Array<{name: string, value: string}>>
```

Returns all request headers as an array of name/value objects. Preserves the original casing and contains multiple entries for multi-value headers.

**Returns:** `Promise<Array<{name: string, value: string}>>`

```js
const headers = await request.headersArray();
headers.forEach(h => console.log(`${h.name}: ${h.value}`));
```

---

### request.isNavigationRequest()

```ts
request.isNavigationRequest(): boolean
```

Returns `true` when this request drives a frame navigation.

**Returns:** `boolean`

---

### request.method()

```ts
request.method(): string
```

Returns the HTTP method of the request.

**Returns:** `string` — e.g. `"GET"`, `"POST"`, `"PUT"`, `"DELETE"`

---

### request.postData()

```ts
request.postData(): string | null
```

Returns the request body as a string. `null` when no body is present (e.g. GET requests).

**Returns:** `string | null`

---

### request.postDataBuffer()

```ts
request.postDataBuffer(): Buffer | null
```

Returns the request body as a binary `Buffer`. `null` when no body is present.

**Returns:** `Buffer | null`

---

### request.postDataJSON()

```ts
request.postDataJSON(): Serializable | null
```

Returns the request body as a parsed JavaScript object. Supports `application/json` and `application/x-www-form-urlencoded`. Returns `null` when the body is not parsable.

**Returns:** `Serializable | null`

```js
const body = request.postDataJSON();
console.log(body?.userId);
```

---

### request.redirectedFrom()

```ts
request.redirectedFrom(): Request | null
```

Returns the previous `Request` instance that redirected to this request. Maps the redirect chain backwards.

**Returns:** `Request | null`

```js
// Walk through the redirect chain
let req = request;
while (req.redirectedFrom()) {
  req = req.redirectedFrom();
  console.log('Redirect from:', req.url());
}
```

---

### request.redirectedTo()

```ts
request.redirectedTo(): Request | null
```

Returns the subsequent `Request` instance created by a server redirect. The opposite of `redirectedFrom()`.

**Returns:** `Request | null`

---

### request.resourceType()

```ts
request.resourceType(): string
```

Returns the resource type of the request.

**Returns:** `string` — possible values: `"document"`, `"stylesheet"`, `"image"`, `"media"`, `"font"`, `"script"`, `"texttrack"`, `"xhr"`, `"fetch"`, `"eventsource"`, `"websocket"`, `"manifest"`, `"other"`

```js
page.on('request', req => {
  if (req.resourceType() === 'image') {
    console.log('Image request:', req.url());
  }
});
```

---

### request.response()

```ts
await request.response(): Promise<Response | null>
```

Waits for the response to this request and returns it. `null` when no response was received (e.g. for aborted requests).

**Returns:** `Promise<Response | null>`

```js
page.on('requestfinished', async request => {
  const response = await request.response();
  console.log(response?.status());
});
```

---

### request.serviceWorker()

```ts
request.serviceWorker(): Worker | null
```

Returns the service worker that performs this request. `null` when no service worker is involved. **Chromium only; always `null` on other browsers.**

**Returns:** `Worker | null`

---

### request.sizes()

```ts
await request.sizes(): Promise<{requestBodySize: number, requestHeadersSize: number, responseBodySize: number, responseHeadersSize: number}>
```

Returns size information about the request and response (in bytes).

**Returns:** `Promise<Object>` with:

| Field | Type | Description |
|-------|------|-------------|
| `requestBodySize` | number | Size of the request body |
| `requestHeadersSize` | number | Size of the request headers |
| `responseBodySize` | number | Size of the response body |
| `responseHeadersSize` | number | Size of the response headers |

```js
const sizes = await request.sizes();
console.log(`Response: ${sizes.responseBodySize} bytes`);
```

---

### request.timing()

```ts
request.timing(): Object
```

Returns timing information about the request (similar to the Resource Timing API).

**Returns:** `Object` with:

| Field | Type | Description |
|-------|------|-------------|
| `startTime` | number | Request start time (ms since epoch) |
| `domainLookupStart` | number | DNS lookup start (ms since startTime) |
| `domainLookupEnd` | number | DNS lookup end |
| `connectStart` | number | TCP connection setup start |
| `secureConnectionStart` | number | TLS handshake start |
| `connectEnd` | number | TCP connection setup end |
| `requestStart` | number | First byte sent |
| `responseStart` | number | First byte received (TTFB) |
| `responseEnd` | number | Last byte received |

```js
const timing = request.timing();
const ttfb = timing.responseStart - timing.requestStart;
console.log(`TTFB: ${ttfb}ms`);
```

---

### request.url()

```ts
request.url(): string
```

Returns the complete URL of the request.

**Returns:** `string`

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 15 |
| Properties | 0 |
| Events | 0 |

**Conclusion:** `Request` is a read-only data object. The most important methods for tests are `url()`, `method()`, `postData()`/`postDataJSON()` and `resourceType()`. For complete header information (including cookies) `allHeaders()` must be used instead of `headers()`.

---

Source: https://playwright.dev/docs/api/class-request
