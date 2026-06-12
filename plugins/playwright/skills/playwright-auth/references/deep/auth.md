# Playwright Authentication - Vollstaendige Referenz

---

## 1. Grundprinzip

Playwright speichert den gesamten Authentifizierungszustand (Cookies,
LocalStorage, SessionStorage) in einer JSON-Datei (`storageState`). Diese
Datei wird einmalig erzeugt und dann von allen Tests wiederverwendet.

### Verzeichnis-Setup

```bash
mkdir -p playwright/.auth
echo "playwright/.auth/" >> .gitignore
```

**Sicherheitshinweis:** Storage-State-Dateien enthalten echte Cookies und
Auth-Token. Niemals in Git committen.

---

## 2. Strategie 1: Geteilter Account (Empfohlen fuer statuslose Tests)

Ideal fuer Tests, die keinen serverseitigen Zustand modifizieren und parallel
laufen koennen.

### Setup-Datei: tests/auth.setup.ts

```typescript
import { test as setup, expect } from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

setup('authenticate', async ({ page }) => {
  // Login-Seite aufrufen
  await page.goto('https://example.com/login');

  // Credentials eingeben
  await page.getByLabel('Email').fill(process.env.TEST_EMAIL!);
  await page.getByLabel('Password').fill(process.env.TEST_PASSWORD!);
  await page.getByRole('button', { name: 'Sign in' }).click();

  // Auf erfolgreichen Login warten
  await page.waitForURL('https://example.com/dashboard');
  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();

  // Zustand speichern
  await page.context().storageState({ path: authFile });
});
```

### playwright.config.ts

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // Setup laeuft zuerst
    {
      name: 'setup',
      testMatch: /.*\.setup\.ts/,
    },
    // Chromium-Tests nutzen gespeicherten Zustand
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        storageState: 'playwright/.auth/user.json',
      },
      dependencies: ['setup'],
    },
    // Firefox-Tests nutzen denselben Zustand
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

### Test (automatisch authentifiziert)

```typescript
import { test, expect } from '@playwright/test';

test('authenticated page', async ({ page }) => {
  // page ist bereits eingeloggt - kein Login-Code noetig
  await page.goto('https://example.com/dashboard');
  await expect(page.getByText('Willkommen')).toBeVisible();
});
```

**UI Mode:** Setup-Datei manuell ausfuehren wenn die Auth-Session ablaeuft
(Dreieck-Button in den Filtern des UI-Mode).

---

## 3. Strategie 2: Ein Account pro Worker (Fuer state-modifizierende Tests)

Wenn Tests serverseitigen Zustand aendern und parallel laufen, braucht jeder
Worker einen eigenen Account.

### playwright/fixtures.ts

```typescript
import { test as baseTest, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';

// Account-Pool (aus Datenbank, Env-Variablen etc.)
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
  // storageState wird durch Worker-State ersetzt
  storageState: ({ workerStorageState }, use) => use(workerStorageState),

  workerStorageState: [async ({ browser }, use) => {
    const id = test.info().parallelIndex;
    const fileName = path.resolve(
      test.info().project.outputDir,
      `.auth/worker-${id}.json`
    );

    // Bereits gespeicherter Zustand: wiederverwenden
    if (fs.existsSync(fileName)) {
      await use(fileName);
      return;
    }

    // Neu einloggen
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

### Test mit Worker-Fixture

```typescript
// WICHTIG: Fixture-File importieren, nicht @playwright/test
import { test, expect } from '../playwright/fixtures';

test('isolated state test', async ({ page }) => {
  // Jeder Worker nutzt seinen eigenen Account
  await page.goto('/my-orders');
  await expect(page.locator('.order-count')).toBeVisible();
});
```

---

## 4. Strategie 3: Login per API

Schneller als UI-Login, wenn ein API-Endpoint verfuegbar ist.

### Setup via request-Fixture

```typescript
import { test as setup } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('authenticate via API', async ({ request }) => {
  // POST zum Login-Endpoint
  const response = await request.post('https://example.com/api/login', {
    data: {
      username: process.env.TEST_USER,
      password: process.env.TEST_PASSWORD,
    },
  });
  expect(response.ok()).toBeTruthy();

  // Cookies und LocalStorage speichern
  await request.storageState({ path: authFile });
});
```

### Worker-Fixture mit API-Login

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

## 5. Mehrere Rollen

### Mehrere Setup-Tests

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

### Rollen im Test wechseln

```typescript
import { test, expect } from '@playwright/test';

// Alle Tests in dieser Datei: Admin
test.use({ storageState: 'playwright/.auth/admin.json' });

test('admin can see user list', async ({ page }) => {
  await page.goto('/admin/users');
  await expect(page.locator('table')).toBeVisible();
});

// Gruppe mit anderer Rolle
test.describe('user permissions', () => {
  test.use({ storageState: 'playwright/.auth/user.json' });

  test('user cannot access admin', async ({ page }) => {
    await page.goto('/admin');
    await expect(page).toHaveURL('/403');
  });
});
```

---

## 6. Beide Rollen in einem Test

```typescript
test('admin sees user content', async ({ browser }) => {
  // Admin-Context
  const adminContext = await browser.newContext({
    storageState: 'playwright/.auth/admin.json',
  });
  const adminPage = await adminContext.newPage();

  // User-Context
  const userContext = await browser.newContext({
    storageState: 'playwright/.auth/user.json',
  });
  const userPage = await userContext.newPage();

  // Interaktionen
  await adminPage.goto('/admin/posts');
  await adminPage.getByRole('button', { name: 'New Post' }).click();
  await adminPage.fill('#title', 'Test Post');
  await adminPage.click('#publish');

  await userPage.goto('/feed');
  await expect(userPage.getByText('Test Post')).toBeVisible();

  // Aufraeumen
  await adminContext.close();
  await userContext.close();
});
```

---

## 7. Page Object Model mit Rollen-Fixtures

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

Nicht in `storageState` enthalten (nur LocalStorage + Cookies). Manuell
verwalten:

```typescript
// Speichern
const sessionData = await page.evaluate(() => JSON.stringify(sessionStorage));
fs.writeFileSync('playwright/.auth/session.json', sessionData, 'utf-8');

// Wiederherstellen (vor Navigation)
const sessionData = JSON.parse(fs.readFileSync('playwright/.auth/session.json', 'utf-8'));
await context.addInitScript(storage => {
  if (window.location.hostname === 'example.com') {
    for (const [key, value] of Object.entries(storage)) {
      window.sessionStorage.setItem(key, value as string);
    }
  }
}, sessionData);

await page.goto('https://example.com'); // Session-Storage ist jetzt gefuellt
```

---

## 9. Tests ohne Authentifizierung

```typescript
// not-signed-in.spec.ts
import { test, expect } from '@playwright/test';

// Leeren Storage-State setzen
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

## 10. storageState API-Referenz

### context.storageState(options?)

| Option | Typ | Beschreibung |
|--------|-----|--------------|
| `path` | `string` | Dateipfad zum Speichern (relativ zu cwd) |
| `indexedDB` | `boolean` | IndexedDB einschliessen (default: false, ab v1.51) |

```typescript
// Speichern nach Login
await page.context().storageState({ path: 'playwright/.auth/user.json' });

// Wert zurueckgeben
const state = await page.context().storageState();
console.log(state.cookies);   // Array von Cookie-Objekten
console.log(state.origins);   // Array von {origin, localStorage[{name, value}]}

// Mit IndexedDB
await page.context().storageState({
  path: 'playwright/.auth/full-state.json',
  indexedDB: true,
});
```

### Storage-State-Format

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

Gleiche Optionen wie context.storageState(). Fuer API-basierte Auth.

```typescript
await request.post('/login', { data: { username: 'alice', password: 'secret' } });
await request.storageState({ path: 'playwright/.auth/alice.json' });
```

---

## 11. Auth-Ablauf und Refresh

### Auth-Ablauf erkennen

```typescript
// In setup: pruefen ob noch eingeloggt
setup('conditionally authenticate', async ({ page }) => {
  const authFile = 'playwright/.auth/user.json';

  // Gespeicherten State laden
  if (fs.existsSync(authFile)) {
    const context = await browser.newContext({ storageState: authFile });
    const page = await context.newPage();
    await page.goto('/dashboard');

    // Pruefen ob noch eingeloggt
    if (await page.locator('#user-menu').isVisible()) {
      await context.close();
      return; // Noch gueltig
    }
    await context.close();
  }

  // Neu einloggen
  await page.goto('/login');
  // ... login ...
  await page.context().storageState({ path: authFile });
});
```

### Konfiguration fuer mehrere Browserprojekte

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

Quelle: https://playwright.dev/docs/auth
