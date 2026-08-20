# class-response

`Response` represents an HTTP response to a Playwright request. Instances are obtained through page/context events (`on('response')`) or via `request.response()`. The object is read-only.

Methods: 15 | Properties: 0 | Events: 0

---

## Methods

### response.allHeaders()

```ts
await response.allHeaders(): Promise<Object<string, string>>
```

Returns all response headers as an object (lowercase keys). Also includes security-relevant headers that are omitted by `headers()`. Multi-value headers are joined with a comma.

**Returns:** `Promise<Object<string, string>>`

```js
const headers = await response.allHeaders();
console.log(headers['content-type']);
```

---

### response.body()

```ts
await response.body(): Promise<Buffer>
```

Returns the complete response body as a binary `Buffer`.

**Returns:** `Promise<Buffer>`

```js
const buffer = await response.body();
require('fs').writeFileSync('response.bin', buffer);
```

---

### response.finished()

```ts
await response.finished(): Promise<null | Error>
```

Waits until the response has been downloaded completely. Always returns `null` on success.

**Returns:** `Promise<null | Error>` — `null` on success, `Error` on failure

```js
const err = await response.finished();
if (err) console.error('Download failed:', err.message);
```

---

### response.frame()

```ts
response.frame(): Frame
```

Returns the `Frame` that triggered this response.

**Returns:** `Frame`

---

### response.fromServiceWorker()

```ts
response.fromServiceWorker(): boolean
```

Returns `true` when this response was served by a service worker fetch handler.

**Returns:** `boolean`

---

### response.headerValue(name)

```ts
await response.headerValue(name): Promise<string | null>
```

Returns the value of a single response header. For headers that occur multiple times, the values are joined comma-separated.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header name (case-insensitive) |

**Returns:** `Promise<string | null>`

```js
const contentType = await response.headerValue('content-type');
```

---

### response.headerValues(name)

```ts
await response.headerValues(name): Promise<Array<string>>
```

Returns all values of a header as an array. Especially useful for `Set-Cookie`, which can occur multiple times.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | string | Yes | — | Header name (case-insensitive) |

**Returns:** `Promise<Array<string>>`

```js
const cookies = await response.headerValues('set-cookie');
cookies.forEach(c => console.log('Cookie:', c));
```

---

### response.headers()

```ts
response.headers(): Object<string, string>
```

Returns response headers synchronously as an object (lowercase keys). Excludes some security-relevant headers. Use `allHeaders()` for all headers.

**Returns:** `Object<string, string>`

---

### response.headersArray()

```ts
await response.headersArray(): Promise<Array<{name: string, value: string}>>
```

Returns all response headers as an array of name/value objects. Preserves the original casing; multi-value headers appear as separate entries.

**Returns:** `Promise<Array<{name: string, value: string}>>`

```js
const headers = await response.headersArray();
headers.forEach(h => console.log(`${h.name}: ${h.value}`));
```

---

### response.httpVersion()

```ts
await response.httpVersion(): Promise<string>
```

Returns the HTTP version that was used for this response.

**Returns:** `Promise<string>` — e.g. `"HTTP/1.1"`, `"HTTP/2.0"`, `"HTTP/3.0"`

```js
const version = await response.httpVersion();
console.log('HTTP Version:', version);
```

---

### response.json()

```ts
await response.json(): Promise<Serializable>
```

Returns the response body as a parsed JavaScript object. Throws an exception when the body is not valid JSON.

**Returns:** `Promise<Serializable>`

```js
const data = await response.json();
console.log(data.users[0].name);
```

---

### response.ok()

```ts
response.ok(): boolean
```

Returns `true` when the status code is in the range 200-299.

**Returns:** `boolean`

```js
expect(response.ok()).toBeTruthy();
```

---

### response.request()

```ts
response.request(): Request
```

Returns the associated `Request` instance.

**Returns:** `Request`

```js
const req = response.request();
console.log('Method:', req.method(), 'URL:', req.url());
```

---

### response.securityDetails()

```ts
await response.securityDetails(): Promise<null | Object>
```

Returns SSL/TLS security information. `null` for insecure (HTTP) connections.

**Returns:** `Promise<null | Object>` with:

| Field | Type | Description |
|-------|------|-------------|
| `issuer` | string | Certificate issuer (common name) |
| `protocol` | string | TLS protocol version |
| `subjectName` | string | Certificate subject (common name) |
| `validFrom` | number | Start of validity (Unix timestamp) |
| `validTo` | number | End of validity (Unix timestamp) |

```js
const details = await response.securityDetails();
if (details) {
  console.log(`TLS: ${details.protocol}, Issuer: ${details.issuer}`);
  console.log(`Valid until: ${new Date(details.validTo * 1000).toISOString()}`);
}
```

---

### response.serverAddr()

```ts
await response.serverAddr(): Promise<null | {ipAddress: string, port: number}>
```

Returns the IP address and port of the server that sent the response.

**Returns:** `Promise<null | {ipAddress: string, port: number}>`

```js
const addr = await response.serverAddr();
if (addr) {
  console.log(`Server: ${addr.ipAddress}:${addr.port}`);
}
```

---

### response.status()

```ts
response.status(): number
```

Returns the numeric HTTP status code.

**Returns:** `number` — e.g. `200`, `201`, `301`, `404`, `500`

```js
expect(response.status()).toBe(200);
```

---

### response.statusText()

```ts
response.statusText(): string
```

Returns the HTTP status text.

**Returns:** `string` — e.g. `"OK"`, `"Not Found"`, `"Internal Server Error"`

---

### response.text()

```ts
await response.text(): Promise<string>
```

Returns the response body as a string (UTF-8 decoding).

**Returns:** `Promise<string>`

```js
const html = await response.text();
console.log(html.includes('<title>'));
```

---

### response.url()

```ts
response.url(): string
```

Returns the URL of the response (may differ from the original request URL after redirects).

**Returns:** `string`

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 15 |
| Properties | 0 |
| Events | 0 |

**Conclusion:** `Response` is a read-only data object for HTTP responses. For API tests, `status()`, `ok()`, `json()` and `text()` are the most frequently used methods. `headerValues()` is important for `Set-Cookie` analysis. `securityDetails()` and `serverAddr()` cover TLS and infrastructure checks.

---

Source: https://playwright.dev/docs/api/class-response
