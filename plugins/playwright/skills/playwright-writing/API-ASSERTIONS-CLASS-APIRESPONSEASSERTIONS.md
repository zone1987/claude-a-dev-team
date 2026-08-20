# class-apiresponseassertions — Playwright API Reference

`APIResponseAssertions` is the assertion class for `APIResponse` objects from Playwright API tests. It offers a single matcher for HTTP status checks.

Accessed via `expect(response).*`.

Matcher count: 1 matcher + property `not`

---

## not

```typescript
not: APIResponseAssertions
```

Inverts the following assertion.

```typescript
await expect(response).not.toBeOK();
```

---

## toBeOK()

```typescript
toBeOK(): Promise<void>
```

Checks whether the response's HTTP status code lies in the success range `200..299`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| — | — | — | — | No parameters |

**Returns:** `Promise<void>`

```typescript
import { test, expect } from '@playwright/test';

test('API returns success response', async ({ request }) => {
  const response = await request.get('/api/products');
  await expect(response).toBeOK();
});

test('Deleted resource is no longer available', async ({ request }) => {
  const response = await request.get('/api/products/geloescht');
  await expect(response).not.toBeOK();
  // Example: status 404 would make the test pass
});
```

---

## Practical notes

`toBeOK()` is deliberately kept simple. For more precise status checks, check the status code directly:

```typescript
const response = await request.post('/api/orders', { data: payload });
await expect(response).toBeOK(); // Only checks 2xx

// Explicit status check:
expect(response.status()).toBe(201);
expect(response.ok()).toBe(true);
```

---

## Matcher overview (1 matcher)

| Matcher | Checks |
|---|---|
| `toBeOK` | HTTP status code in the range 200-299 |

---

Source: https://playwright.dev/docs/api/class-apiresponseassertions
