# Playwright Authentication - Complete Reference

---

## Contents

- [1. Basic principle](#1-basic-principle)
- [2. Strategy 1: Shared account (recommended for stateless tests)](#2-strategy-1-shared-account-recommended-for-stateless-tests)
- [3. Strategy 2: One account per worker (for state-modifying tests)](#3-strategy-2-one-account-per-worker-for-state-modifying-tests)
- [4. Strategy 3: Login via API](#4-strategy-3-login-via-api)
- [5. Multiple roles](#5-multiple-roles)
- [6. Both roles in one test](#6-both-roles-in-one-test)
- [7. Page Object Model with role fixtures](#7-page-object-model-with-role-fixtures)
- [8. Session Storage](#8-session-storage)
- [9. Tests without authentication](#9-tests-without-authentication)
- [10. storageState API reference](#10-storagestate-api-reference)
- [11. Auth expiry and refresh](#11-auth-expiry-and-refresh)

## 1. Basic principle

Playwright stores the entire authentication state (cookies,
LocalStorage, SessionStorage) in a JSON file (`storageState`). This
file is created once and then reused by all tests.

### Directory setup

```bash
mkdir -p playwright/.auth
echo "playwright/.auth/" >> .gitignore
```

**Security note:** Storage state files contain real cookies and
auth tokens. Never commit them to Git.

---

## 2. Strategy 1: Shared account (recommended for stateless tests)

Ideal for tests that do not modify server-side state and can run in
parallel.

### Setup file: tests/auth.setup.ts

```typescript
import { test as setup, expect } from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

setup('authenticate', async ({ page }) => {
  // Open the login page
  await page.goto('https://example.com/login');

  // Enter credentials
  await page.getByLabel('Email').fill(process.env.TEST_EMAIL!);
  await page.getByLabel('Password').fill(process.env.TEST_PASSWORD!);
  await page.getByRole('button', { name: 'Sign in' }).click();

  // Wait for a successful login
  await page.waitForURL('https://example.com/dashboard');
  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();

  // Save the state
  await page.context().storageState({ path: authFile });
});
```

### playwright.config.ts

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // Setup runs first
    {
      name: 'setup',
      testMatch: /.*\.setup\.ts/,
    },
    // Chromium tests use the saved state
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        storageState: 'playwright/.auth/user.json',
      },
      dependencies: ['setup'],
    },
    // Firefox tests use the same state
    {
      name: 'firefox',
      use: {
        ...devices['Desktop Firefox'],
        storageState: 'playwright/.auth/user.json',
      },
      dependencies: ['setup'],
    },
  ],
});
```

### Test (authenticated automatically)

```typescript
import { test, expect } from '@playwright/test';

test('authenticated page', async ({ page }) => {
  // page is already logged in - no login code needed
  await page.goto('https://example.com/dashboard');
  await expect(page.getByText('Welcome')).toBeVisible();
});
```

**UI Mode:** Run the setup file manually when the auth session expires
(triangle button in the UI mode filters).

---

## 3. Strategy 2: One account per worker (for state-modifying tests)

When tests change server-side state and run in parallel, every
worker needs its own account.

### playwright/fixtures.ts

```typescript
import { test as baseTest, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';

// Account pool (from a database, env variables, etc.)
async function acquireAccount(parallelIndex: number) {
  const accounts = [
    { username: 'user1@test.com', password: 'pass1' },
    { username: 'user2@test.com', password: 'pass2' },
    { username: 'user3@test.com', password: 'pass3' },
  ];
  return accounts[parallelIndex % accounts.length];
}

export * from '@playwright/test';

export const test = baseTest.extend<{}, { workerStorageState: string }>({
  // storageState is replaced by the worker state
  storageState: ({ workerStorageState }, use) => use(workerStorageState),

  workerStorageState: [async ({ browser }, use) => {
    const id = test.info().parallelIndex;
    const fileName = path.resolve(
      test.info().project.outputDir,
      `.auth/worker-${id}.json`
    );

    // State already saved: reuse it
    if (fs.existsSync(fileName)) {
      await use(fileName);
      return;
    }

    // Log in again
    const page = await browser.newPage({ storageState: undefined });
    const account = await acquireAccount(id);

    await page.goto('https://example.com/login');
    await page.getByLabel('Username').fill(account.username);
    await page.getByLabel('Password').fill(account.password);
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('https://example.com/');
    await expect(page.getByRole('button', { name: 'Account' })).toBeVisible();

    await page.context().storageState({ path: fileName });
    await page.close();
    await use(fileName);
  }, { scope: 'worker' }],
});
```

### Test with the worker fixture

```typescript
// IMPORTANT: import the fixture file, not @playwright/test
import { test, expect } from '../playwright/fixtures';

test('isolated state test', async ({ page }) => {
  // Every worker uses its own account
  await page.goto('/my-orders');
  await expect(page.locator('.order-count')).toBeVisible();
});
```

---

## 4. Strategy 3: Login via API

Faster than a UI login when an API endpoint is available.

### Setup via the request fixture

```typescript
import { test as setup } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('authenticate via API', async ({ request }) => {
  // POST to the login endpoint
  const response = await request.post('https://example.com/api/login', {
    data: {
      username: process.env.TEST_USER,
      password: process.env.TEST_PASSWORD,
    },
  });
  expect(response.ok()).toBeTruthy();

  // Save cookies and LocalStorage
  await request.storageState({ path: authFile });
});
```

### Worker fixture with API login

```typescript
workerStorageState: [async ({}, use) => {
  const id = test.info().parallelIndex;
  const fileName = path.resolve(test.info().project.outputDir, `.auth/${id}.json`);

  if (fs.existsSync(fileName)) {
    await use(fileName);
    return;
  }

  const account = await acquireAccount(id);
  const context = await request.newContext({ storageState: undefined });

  await context.post('https://example.com/api/login', {
    form: { user: account.username, password: account.password },
  });

  await context.storageState({ path: fileName });
  await context.dispose();
  await use(fileName);
}, { scope: 'worker' }],
```

---

## 5. Multiple roles

### Multiple setup tests

```typescript
// tests/auth.setup.ts
import { test as setup, expect } from '@playwright/test';

setup('authenticate as admin', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', process.env.ADMIN_EMAIL!);
  await page.fill('#password', process.env.ADMIN_PASSWORD!);
  await page.click('[type="submit"]');
  await page.waitForURL('/admin/dashboard');
  await page.context().storageState({ path: 'playwright/.auth/admin.json' });
});

setup('authenticate as user', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', process.env.USER_EMAIL!);
  await page.fill('#password', process.env.USER_PASSWORD!);
  await page.click('[type="submit"]');
  await page.waitForURL('/dashboard');
  await page.context().storageState({ path: 'playwright/.auth/user.json' });
});
```

### Switching roles in a test

```typescript
import { test, expect } from '@playwright/test';

// All tests in this file: admin
test.use({ storageState: 'playwright/.auth/admin.json' });

test('admin can see user list', async ({ page }) => {
  await page.goto('/admin/users');
  await expect(page.locator('table')).toBeVisible();
});

// Group with a different role
test.describe('user permissions', () => {
  test.use({ storageState: 'playwright/.auth/user.json' });

  test('user cannot access admin', async ({ page }) => {
    await page.goto('/admin');
    await expect(page).toHaveURL('/403');
  });
});
```

---

## 6. Both roles in one test

```typescript
test('admin sees user content', async ({ browser }) => {
  // Admin context
  const adminContext = await browser.newContext({
    storageState: 'playwright/.auth/admin.json',
  });
  const adminPage = await adminContext.newPage();

  // User context
  const userContext = await browser.newContext({
    storageState: 'playwright/.auth/user.json',
  });
  const userPage = await userContext.newPage();

  // Interactions
  await adminPage.goto('/admin/posts');
  await adminPage.getByRole('button', { name: 'New Post' }).click();
  await adminPage.fill('#title', 'Test Post');
  await adminPage.click('#publish');

  await userPage.goto('/feed');
  await expect(userPage.getByText('Test Post')).toBeVisible();

  // Clean up
  await adminContext.close();
  await userContext.close();
});
```

---

## 7. Page Object Model with role fixtures

```typescript
// playwright/fixtures.ts
import { test as base, type Page, type Locator } from '@playwright/test';

class AdminPage {
  constructor(public readonly page: Page) {}
  readonly userList = this.page.locator('table.users');
  async goto() { await this.page.goto('/admin'); }
}

class UserPage {
  constructor(public readonly page: Page) {}
  readonly dashboard = this.page.locator('#dashboard');
  async goto() { await this.page.goto('/dashboard'); }
}

export const test = base.extend<{
  adminPage: AdminPage;
  userPage: UserPage;
}>({
  adminPage: async ({ browser }, use) => {
    const ctx = await browser.newContext({ storageState: 'playwright/.auth/admin.json' });
    await use(new AdminPage(await ctx.newPage()));
    await ctx.close();
  },
  userPage: async ({ browser }, use) => {
    const ctx = await browser.newContext({ storageState: 'playwright/.auth/user.json' });
    await use(new UserPage(await ctx.newPage()));
    await ctx.close();
  },
});

// Test
import { test, expect } from '../playwright/fixtures';
test('multi-role interaction', async ({ adminPage, userPage }) => {
  await adminPage.goto();
  await expect(adminPage.userList).toBeVisible();

  await userPage.goto();
  await expect(userPage.dashboard).toBeVisible();
});
```

---

## 8. Session Storage

Not included in `storageState` (only LocalStorage + cookies). Manage it
manually:

```typescript
// Save
const sessionData = await page.evaluate(() => JSON.stringify(sessionStorage));
fs.writeFileSync('playwright/.auth/session.json', sessionData, 'utf-8');

// Restore (before navigating)
const sessionData = JSON.parse(fs.readFileSync('playwright/.auth/session.json', 'utf-8'));
await context.addInitScript(storage => {
  if (window.location.hostname === 'example.com') {
    for (const [key, value] of Object.entries(storage)) {
      window.sessionStorage.setItem(key, value as string);
    }
  }
}, sessionData);

await page.goto('https://example.com'); // Session storage is now populated
```

---

## 9. Tests without authentication

```typescript
// not-signed-in.spec.ts
import { test, expect } from '@playwright/test';

// Set an empty storage state
test.use({ storageState: { cookies: [], origins: [] } });

test('public page without login', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('link', { name: 'Login' })).toBeVisible();
});

test('redirect to login when accessing protected page', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveURL('/login');
});
```

---

## 10. storageState API reference

### context.storageState(options?)

| Option | Type | Description |
|--------|-----|--------------|
| `path` | `string` | File path to save to (relative to cwd) |
| `indexedDB` | `boolean` | Include IndexedDB (default: false, from v1.51) |

```typescript
// Save after login
await page.context().storageState({ path: 'playwright/.auth/user.json' });

// Return the value
const state = await page.context().storageState();
console.log(state.cookies);   // Array of cookie objects
console.log(state.origins);   // Array of {origin, localStorage[{name, value}]}

// With IndexedDB
await page.context().storageState({
  path: 'playwright/.auth/full-state.json',
  indexedDB: true,
});
```

### Storage state format

```json
{
  "cookies": [
    {
      "name": "session",
      "value": "abc123",
      "domain": "example.com",
      "path": "/",
      "expires": 1735689600,
      "httpOnly": true,
      "secure": true,
      "sameSite": "Lax"
    }
  ],
  "origins": [
    {
      "origin": "https://example.com",
      "localStorage": [
        { "name": "auth_token", "value": "eyJhbGc..." }
      ]
    }
  ]
}
```

### request.storageState(options?)

Same options as context.storageState(). For API-based auth.

```typescript
await request.post('/login', { data: { username: 'alice', password: 'secret' } });
await request.storageState({ path: 'playwright/.auth/alice.json' });
```

---

## 11. Auth expiry and refresh

### Detecting auth expiry

```typescript
// In setup: check whether still logged in
setup('conditionally authenticate', async ({ page }) => {
  const authFile = 'playwright/.auth/user.json';

  // Load the saved state
  if (fs.existsSync(authFile)) {
    const context = await browser.newContext({ storageState: authFile });
    const page = await context.newPage();
    await page.goto('/dashboard');

    // Check whether still logged in
    if (await page.locator('#user-menu').isVisible()) {
      await context.close();
      return; // Still valid
    }
    await context.close();
  }

  // Log in again
  await page.goto('/login');
  // ... login ...
  await page.context().storageState({ path: authFile });
});
```

### Configuration for multiple browser projects

```typescript
export default defineConfig({
  projects: [
    { name: 'setup', testMatch: /auth\.setup\.ts/ },
    { name: 'admin-setup', testMatch: /admin\.auth\.setup\.ts/ },
    {
      name: 'tests:user',
      use: { storageState: 'playwright/.auth/user.json' },
      dependencies: ['setup'],
    },
    {
      name: 'tests:admin',
      use: { storageState: 'playwright/.auth/admin.json' },
      dependencies: ['admin-setup'],
    },
  ],
});
```

---

Source: https://playwright.dev/docs/auth
