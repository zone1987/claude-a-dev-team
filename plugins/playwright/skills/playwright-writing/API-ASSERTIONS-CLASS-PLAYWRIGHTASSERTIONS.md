# class-playwrightassertions — Playwright API Reference

`PlaywrightAssertions` is the factory class that provides the `expect()` function. It is overloaded and returns the matching assertion class depending on the type of the argument passed. All overloads implement "web-first assertions" that retry automatically until the condition holds or the timeout expires.

Default timeout: 5000 ms (configurable via `TestConfig.expect.timeout`).

Method count: 4 overloads of `expect()`

---

## Contents

- [expect(response)](#expectresponse)
- [expect(value)](#expectvalue)
- [expect(locator)](#expectlocator)
- [expect(page)](#expectpage)
- [Return types by argument](#return-types-by-argument)
- [Soft Assertions](#soft-assertions)
- [expect.poll()](#expectpoll)
- [expect.toPass()](#expecttopass)
- [expect.extend()](#expectextend)

## expect(response)

```typescript
expect(response: APIResponse): APIResponseAssertions
```

Creates assertion utilities for an `APIResponse` object.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `response` | `APIResponse` | yes | — | Response object from `request.get()`, `request.post()` etc. |

**Returns:** `APIResponseAssertions`

```typescript
import { test, expect } from '@playwright/test';

test('API endpoint responds successfully', async ({ request }) => {
  const response = await request.get('/api/health');
  await expect(response).toBeOK();
});
```

**Available assertions:** All methods of `APIResponseAssertions` — in particular `toBeOK()`.

---

## expect(value)

```typescript
expect(value: unknown): GenericAssertions
```

Creates assertion utilities for arbitrary JavaScript values. No auto-retry.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `value` | `unknown` | yes | — | Value to check (primitives, objects, arrays, promises, functions) |

**Returns:** `GenericAssertions`

```typescript
expect(42).toBe(42);
expect([1, 2, 3]).toHaveLength(3);
expect(user).toMatchObject({ role: 'admin' });
await expect(Promise.resolve('ok')).resolves.toBe('ok');
expect(() => JSON.parse('{bad}')).toThrow(SyntaxError);
```

**Available assertions:** All methods of `GenericAssertions`.

---

## expect(locator)

```typescript
expect(locator: Locator): LocatorAssertions
```

Creates assertion utilities for a `Locator`. All assertions retry automatically.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `locator` | `Locator` | yes | — | Playwright locator for the element to check |

**Returns:** `LocatorAssertions`

```typescript
await expect(page.getByRole('button', { name: 'Senden' })).toBeEnabled();
await expect(page.locator('.success-message')).toBeVisible();
await expect(page.getByLabel('Name')).toHaveValue('Max');
await expect(page.getByRole('listitem')).toHaveCount(3);
```

**Available assertions:** All 29 matchers of `LocatorAssertions` + `not`.

---

## expect(page)

```typescript
expect(page: Page): PageAssertions
```

Creates assertion utilities for a `Page` object. All assertions retry automatically.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `page` | `Page` | yes | — | Playwright page instance |

**Returns:** `PageAssertions`

```typescript
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveTitle('My App');
await expect(page).toHaveScreenshot('baseline.png');
```

**Available assertions:** All 6 matchers of `PageAssertions` + `not`.

---

## Return types by argument

| Argument type | Return type | Auto-retry |
|---|---|---|
| `APIResponse` | `APIResponseAssertions` | no |
| any value | `GenericAssertions` | no |
| `Locator` | `LocatorAssertions` | yes |
| `Page` | `PageAssertions` | yes |

---

## Soft Assertions

`expect.soft()` marks failed assertions but does not abort the test immediately. All errors are reported collectively at the end of the test.

```typescript
// Fails, but continues the test:
await expect.soft(page.locator('.title')).toHaveText('Erwarteter Titel');
await expect.soft(page.locator('.count')).toHaveText('5');
// Only here is it thrown, if soft assertions have failed:
```

---

## expect.poll()

Runs a function repeatedly and checks the result with a GenericAssertion matcher. Useful for non-Playwright state.

```typescript
await expect.poll(async () => {
  const response = await fetch('/api/status');
  return (await response.json()).state;
}, {
  intervals: [1000, 2000, 5000],
  timeout: 15_000,
}).toBe('complete');
```

---

## expect.toPass()

Runs a block repeatedly until it completes without an error.

```typescript
await expect(async () => {
  const items = await page.getByRole('listitem').all();
  expect(items.length).toBeGreaterThan(2);
}).toPass({ timeout: 10_000 });
```

---

## expect.extend()

Registers custom matchers.

```typescript
expect.extend({
  async toBeLoggedIn(page: Page) {
    const isLoggedIn = await page.locator('.user-menu').isVisible();
    return {
      message: () => `Erwartet, dass Benutzer ${isLoggedIn ? '' : 'nicht '}eingeloggt ist`,
      pass: isLoggedIn,
    };
  },
});

// Usage:
await expect(page).toBeLoggedIn();
```

---

Source: https://playwright.dev/docs/api/class-playwrightassertions
