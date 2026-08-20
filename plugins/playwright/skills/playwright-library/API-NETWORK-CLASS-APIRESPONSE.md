# class-apiresponse

`APIResponse` represents the HTTP response to a request made via `APIRequestContext`. Unlike `Response` (browser requests), `APIResponse` must be released explicitly via `dispose()` when the body is not needed, in order to avoid memory leaks.

Methods: 10 | Properties: 0 | Events: 0

---

## Contents

- [Methods](#methods)
- [Usage patterns](#usage-patterns)
- [Difference from class-response](#difference-from-class-response)
- [Manifest](#manifest)

## Methods

### apiResponse.body()

```ts
await apiResponse.body(): Promise<Buffer>
```

Returns the complete response body as a binary `Buffer`.

**Returns:** `Promise<Buffer>`

```js
const buffer = await response.body();
require('fs').writeFileSync('download.pdf', buffer);
```

---

### apiResponse.dispose()

```ts
await apiResponse.dispose(): Promise<void>
```

Releases the response body from memory. Should be called when the body is not needed (e.g. for status-only checks). Otherwise the body stays in memory until the context is closed.

**Returns:** `Promise<void>`

```js
// Check status without reading the body
const response = await request.get('/api/health');
expect(response.status()).toBe(200);
await response.dispose(); // free memory
```

---

### apiResponse.headers()

```ts
apiResponse.headers(): Object<string, string>
```

Returns all response headers as an object. Multi-value headers are joined with commas.

**Returns:** `Object<string, string>`

```js
const headers = response.headers();
console.log('Content-Type:', headers['content-type']);
console.log('Cache-Control:', headers['cache-control']);
```

---

### apiResponse.headersArray()

```ts
apiResponse.headersArray(): Array<{name: string, value: string}>
```

Returns all response headers as an array. Preserves the original casing; multi-value headers (e.g. `Set-Cookie`) appear as separate entries.

**Returns:** `Array<{name: string, value: string}>` — synchronous, no `await` needed

```js
const headers = apiResponse.headersArray();
const setCookies = headers
  .filter(h => h.name.toLowerCase() === 'set-cookie')
  .map(h => h.value);
```

---

### apiResponse.json()

```ts
await apiResponse.json(): Promise<Serializable>
```

Returns the response body as a parsed JavaScript object. Throws an exception if the body is not valid JSON.

**Returns:** `Promise<Serializable>`

```js
const data = await response.json();
expect(data.users).toHaveLength(10);
expect(data.users[0]).toMatchObject({
  id: expect.any(Number),
  name: expect.any(String),
});
```

---

### apiResponse.ok()

```ts
apiResponse.ok(): boolean
```

Returns `true` if the HTTP status code is in the range 200-299.

**Returns:** `boolean`

```js
const response = await request.post('/api/users', { data: userData });
expect(response.ok()).toBeTruthy();
```

---

### apiResponse.status()

```ts
apiResponse.status(): number
```

Returns the numeric HTTP status code.

**Returns:** `number`

```js
const response = await request.get('/api/users/99999');
expect(response.status()).toBe(404);
```

---

### apiResponse.statusText()

```ts
apiResponse.statusText(): string
```

Returns the HTTP status text.

**Returns:** `string` — e.g. `"OK"`, `"Created"`, `"Not Found"`, `"Internal Server Error"`

```js
console.log(response.status(), response.statusText());
// e.g. "201 Created"
```

---

### apiResponse.text()

```ts
await apiResponse.text(): Promise<string>
```

Returns the response body as a UTF-8 string.

**Returns:** `Promise<string>`

```js
const html = await response.text();
expect(html).toContain('<html');

const csv = await response.text();
const rows = csv.split('\n').map(r => r.split(','));
```

---

### apiResponse.url()

```ts
apiResponse.url(): string
```

Returns the URL this response answers (after redirects: the final URL).

**Returns:** `string`

```js
console.log('Final URL:', response.url());
// With redirects: URL after the last redirect
```

---

## Usage patterns

### Pattern 1: Complete JSON API tests

```js
test('CRUD cycle', async ({ request }) => {
  // Create
  const createResp = await request.post('/api/items', {
    data: { name: 'Test Item', price: 9.99 },
  });
  expect(createResp.status()).toBe(201);
  const { id } = await createResp.json();

  // Read
  const readResp = await request.get(`/api/items/${id}`);
  expect(readResp.ok()).toBeTruthy();
  const item = await readResp.json();
  expect(item.name).toBe('Test Item');

  // Update
  const updateResp = await request.put(`/api/items/${id}`, {
    data: { name: 'Updated Item', price: 19.99 },
  });
  expect(updateResp.ok()).toBeTruthy();

  // Delete
  const deleteResp = await request.delete(`/api/items/${id}`);
  expect(deleteResp.status()).toBe(204);
  await deleteResp.dispose(); // no body expected
});
```

### Pattern 2: Error handling

```js
test('check error responses', async ({ request }) => {
  const response = await request.post('/api/users', {
    data: { name: '' }, // invalid data
  });

  expect(response.status()).toBe(422);
  const error = await response.json();
  expect(error.errors).toContainEqual(
    expect.objectContaining({ field: 'name' })
  );
});
```

### Pattern 3: Header check

```js
test('check CORS headers', async ({ request }) => {
  const response = await request.get('/api/public', {
    headers: { 'Origin': 'https://trusted.example.com' },
  });

  const headers = response.headers();
  expect(headers['access-control-allow-origin']).toBe('https://trusted.example.com');
  expect(headers['content-type']).toContain('application/json');

  await response.dispose();
});
```

### Pattern 4: File download

```js
test('download PDF export', async ({ request }) => {
  const response = await request.get('/api/report.pdf');
  expect(response.ok()).toBeTruthy();
  expect(response.headers()['content-type']).toBe('application/pdf');

  const buffer = await response.body();
  expect(buffer.length).toBeGreaterThan(0);
  // check PDF magic bytes
  expect(buffer.slice(0, 4).toString()).toBe('%PDF');
});
```

---

## Difference from class-response

| Aspect | `APIResponse` | `Response` |
|--------|---------------|------------|
| Origin | `APIRequestContext` | Browser/page network |
| `dispose()` | Required | Not needed |
| `headersArray()` | Synchronous | Asynchronous (await) |
| `allHeaders()` | Not available | Available |
| `fromServiceWorker()` | Not available | Available |
| `securityDetails()` | Not available | Available |
| `serverAddr()` | Not available | Available |

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 10 |
| Properties | 0 |
| Events | 0 |

**Conclusion:** `APIResponse` is the lightweight response object for API tests. `ok()`, `status()` and `json()` are the most common methods. `dispose()` must be called when no body is read, in order to avoid memory leaks. `headersArray()` is (unlike in `class-response`) synchronous.

---

Source: https://playwright.dev/docs/api/class-apiresponse
