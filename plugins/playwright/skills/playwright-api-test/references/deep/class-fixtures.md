# class-fixtures — Playwright Built-in Test Fixtures

Fixtures are the dependency-injection mechanism of Playwright Test. They are declared as
parameters of test functions and hooks, and Playwright sets them up and tears them down
automatically.

Built-in fixtures are available in every test without configuration. Custom fixtures are added
via `test.extend()`.

---

## Built-in Fixtures

### `browser`

| Type | Scope | Description |
|------|-------|-------------|
| `Browser` | worker | Shared `Browser` instance for the entire worker process |

One browser is launched per worker. All tests in that worker share it but each gets its own
`BrowserContext`.

```ts
test.beforeAll(async ({ browser }) => {
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.close();
});
```

---

### `browserName`

| Type | Scope | Description |
|------|-------|-------------|
| `"chromium" \| "firefox" \| "webkit"` | worker | Browser engine currently executing the tests |

Useful for conditionally skipping or adjusting tests.

```ts
test('skip on Firefox', async ({ browserName }) => {
  test.skip(browserName === 'firefox', 'Not yet implemented for Firefox');
  // rest of test runs on chromium and webkit only
});
```

---

### `context`

| Type | Scope | Description |
|------|-------|-------------|
| `BrowserContext` | test | Isolated browser context created fresh for each test |

Provides a clean session (cookies, localStorage) for every test. The `page` fixture belongs
to this context.

```ts
test('block analytics', async ({ context }) => {
  await context.route('**/analytics.js', route => route.abort());
  const page = await context.newPage();
  await page.goto('/');
});
```

---

### `page`

| Type | Scope | Description |
|------|-------|-------------|
| `Page` | test | Isolated `Page` created fresh for each test within its own `context` |

The most commonly used fixture. Provides a blank tab inside the test's `BrowserContext`.

```ts
test('form submission', async ({ page }) => {
  await page.goto('/contact');
  await page.getByLabel('Name').fill('Alice');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(page.getByText('Thank you')).toBeVisible();
});
```

---

### `request`

| Type | Scope | Description |
|------|-------|-------------|
| `APIRequestContext` | test | Isolated `APIRequestContext` for HTTP API requests |

Independent of the browser page; useful for seeding data or calling REST APIs.

```ts
test('API smoke test', async ({ request }) => {
  const response = await request.get('/api/health');
  expect(response.ok()).toBeTruthy();
});

test('create via API then check UI', async ({ page, request }) => {
  await request.post('/api/items', { data: { name: 'Widget' } });
  await page.goto('/items');
  await expect(page.getByText('Widget')).toBeVisible();
});
```

---

## Custom Fixtures with `test.extend()`

Custom fixtures follow the same convention: a function that calls `use()` to provide the
value, with optional setup before and teardown after.

### Fixture definition syntax

```ts
import { test as base } from '@playwright/test';

type MyFixtures = {
  loggedInPage: Page;
  apiToken: string;
};

export const test = base.extend<MyFixtures>({
  // Test-scoped fixture
  loggedInPage: async ({ page }, use) => {
    await page.goto('/login');
    await page.fill('#user', 'admin');
    await page.fill('#pass', 'secret');
    await page.click('[type=submit]');
    await use(page);                    // provide fixture value
    // teardown runs here (if any)
  },

  // Option fixture (overridable via test.use)
  apiToken: ['default-token', { option: true }],
});
```

### Fixture scopes

| Scope | Declaration | Description |
|-------|-------------|-------------|
| `'test'` (default) | `myFixture: async ({}, use) => {}` | Fresh instance per test |
| `'worker'` | `[async ({}, use) => {}, { scope: 'worker' }]` | Shared across all tests in a worker |
| auto | `[async ({}, use) => {}, { auto: true }]` | Always set up, not declared in parameters |

### Worker-scoped fixture example

```ts
type WorkerFixtures = { dbConnection: DbConnection };

export const test = base.extend<{}, WorkerFixtures>({
  dbConnection: [async ({}, use) => {
    const db = await DbConnection.create(process.env.DATABASE_URL!);
    await use(db);
    await db.close();
  }, { scope: 'worker' }],
});
```

### Auto fixture example

```ts
export const test = base.extend<{ mockDate: void }>({
  mockDate: [async ({ page }, use) => {
    await page.addInitScript(() => {
      Date.now = () => new Date('2025-01-01').getTime();
    });
    await use();
  }, { auto: true }],
});
```

---

## Fixture Composition

Fixtures can depend on other fixtures:

```ts
export const test = base.extend<{ todoPage: TodoPage }>({
  todoPage: async ({ page, apiToken }, use) => {
    // apiToken is another custom fixture, page is built-in
    const tp = new TodoPage(page, apiToken);
    await tp.init();
    await use(tp);
    await tp.cleanup();
  },
});
```

---

## Manifest

| Category | Count |
|----------|-------|
| Built-in fixtures | 5 (`browser`, `browserName`, `context`, `page`, `request`) |
| Fixture scopes | 3 (test, worker, auto) |

**Fazit:** Fixtures sind das Herzstuck der Testarchitektur. Die fuenf Built-ins decken Browser-,
Kontext-, Seiten- und API-Zugang ab. Mit `test.extend()` lassen sich saubere,
wiederverwendbare Setup/Teardown-Bausteine mit beliebiger Scope erstellen.

---

Source: https://playwright.dev/docs/api/class-fixtures
