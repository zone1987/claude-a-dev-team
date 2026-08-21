# Playwright Fixtures — Complete Reference

## Contents

- [Built-in fixtures](#built-in-fixtures)
- [Custom fixtures with `test.extend()`](#custom-fixtures-with-testextend)
- [Fixture scopes](#fixture-scopes)
- [Automatic fixtures (auto)](#automatic-fixtures-auto)
- [Option fixtures (configurable)](#option-fixtures-configurable)
- [Overriding built-in fixtures](#overriding-built-in-fixtures)
- [Fixture composition (dependencies)](#fixture-composition-dependencies)
- [Merging fixtures](#merging-fixtures)
- [Fixture options](#fixture-options)
- [Complete fixture signature](#complete-fixture-signature)
- [Global Setup/Teardown](#global-setupteardown)
- [Parametrization](#parametrization)

## Built-in fixtures

| Fixture | Type | Scope | Description |
|---|---|---|---|
| `page` | `Page` | test | Isolated page for each test |
| `context` | `BrowserContext` | test | Isolated browser context; `page` belongs to it |
| `browser` | `Browser` | worker | Shared browser instance (resource-efficient) |
| `browserName` | `string` | worker | Current browser: `'chromium'`, `'firefox'`, `'webkit'` |
| `request` | `APIRequestContext` | test | Isolated API request instance |

---

## Custom fixtures with `test.extend()`

```typescript
import { test as base } from '@playwright/test';

type MyFixtures = {
  todoPage: TodoPage;
  adminPage: AdminPage;
};

export const test = base.extend<MyFixtures>({
  todoPage: async ({ page }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.goto();
    await todoPage.addToDo('item1');

    await use(todoPage);           // <-- Teardown begins after use()

    await todoPage.removeAll();
  },

  adminPage: async ({ page }, use) => {
    await use(new AdminPage(page));
  },
});

export { expect } from '@playwright/test';
```

**Pattern:** setup → `await use(value)` → teardown

---

## Fixture scopes

### Test scope (default)

```typescript
export const test = base.extend<{ myFixture: string }>({
  myFixture: async ({}, use) => {
    await use('hello');
  },
  // Implicitly: { scope: 'test' }
});
```

Is set up and torn down anew for every test.

### Worker scope

```typescript
type WorkerFixtures = { sharedDB: Database };

export const test = base.extend<{}, WorkerFixtures>({
  sharedDB: [async ({ browser }, use, workerInfo) => {
    const db = await Database.connect(`db-${workerInfo.workerIndex}`);
    await use(db);
    await db.close();
  }, { scope: 'worker' }],
});
```

Runs once per worker process; shared across all tests.
`workerInfo.workerIndex` enables data isolation.

---

## Automatic fixtures (auto)

Are executed for every test without the test requesting them explicitly:

```typescript
// Behaves like beforeEach/afterEach
forEachTest: [async ({ page }, use, testInfo) => {
  await page.goto('http://localhost:8000');
  await use();
  // Always executed, even on failure:
  if (testInfo.status !== testInfo.expectedStatus) {
    console.log('Test failed, saving logs...');
    testInfo.attachments.push({
      name: 'logs',
      contentType: 'text/plain',
      body: Buffer.from('error log'),
    });
  }
}, { auto: true }],

// Behaves like beforeAll/afterAll (worker-scoped auto)
forEachWorker: [async ({}, use, workerInfo) => {
  console.log(`Worker ${workerInfo.workerIndex} starting`);
  await use();
  console.log('Worker finished');
}, { scope: 'worker', auto: true }],
```

---

## Option fixtures (configurable)

Allow configuration via `playwright.config.ts` / `use`:

```typescript
// fixtures.ts
type MyOptions = {
  defaultItem: string;
  apiUrl: string;
};

export const test = base.extend<MyOptions & MyFixtures>({
  // Option fixture with a default
  defaultItem: ['Something nice', { option: true }],
  apiUrl: ['http://localhost:3000', { option: true }],

  // Depends on an option fixture
  todoPage: async ({ page, defaultItem }, use) => {
    const p = new TodoPage(page);
    await p.goto();
    await p.addToDo(defaultItem);
    await use(p);
  },
});
```

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';
import type { MyOptions } from './fixtures';

export default defineConfig<MyOptions>({
  projects: [
    { name: 'shopping', use: { defaultItem: 'Buy milk', apiUrl: 'http://localhost:4000' } },
    { name: 'default',  use: { defaultItem: 'Something nice' } },
  ],
});
```

---

## Overriding built-in fixtures

```typescript
export const test = base.extend({
  // All tests start on baseURL
  page: async ({ baseURL, page }, use) => {
    await page.goto(baseURL!);
    await use(page);
  },
});

// Reset an individual option:
test.use({ baseURL: undefined });
```

---

## Fixture composition (dependencies)

```typescript
export const test = base.extend({
  // userFixture depends on dbFixture
  dbFixture: async ({}, use) => {
    const db = await openDB();
    await use(db);
    await db.close();               // teardown after userFixture
  },

  userFixture: async ({ dbFixture }, use) => {
    const user = await dbFixture.createUser();
    await use(user);
    await dbFixture.deleteUser(user.id);
  },
});
```

Setup order: `dbFixture` → `userFixture`
Teardown order: `userFixture` → `dbFixture` (reversed)

---

## Merging fixtures

```typescript
import { mergeTests } from '@playwright/test';
import { test as dbTest } from './database-fixtures';
import { test as a11yTest } from './a11y-fixtures';

export const test = mergeTests(dbTest, a11yTest);
```

---

## Fixture options

| Option | Type | Default | Description |
|---|---|---|---|
| `scope` | `'test' \| 'worker'` | `'test'` | Lifetime of the fixture |
| `auto` | `boolean` | `false` | Execute automatically for every test |
| `option` | `boolean` | `false` | Overridable via config/use |
| `timeout` | `number` | (test timeout) | Dedicated timeout for this fixture in ms |
| `box` | `boolean` | `false` | Hide from test reports |
| `title` | `string` | (fixture name) | Displayed name in reports |

```typescript
// Fixture with its own timeout (for slow operations)
slowFixture: [async ({}, use) => {
  await someSlowOperation();
  await use('result');
}, { timeout: 120_000, scope: 'worker' }],

// Hide a fixture from reports
helperFixture: [async ({}, use) => {
  await use('helper');
}, { box: true }],
```

---

## Complete fixture signature

```typescript
fixtureFunction: async (
  fixtures: BuiltInFixtures & MyFixtures,  // all available fixtures
  use: (value: T) => Promise<void>,        // provide the value
  testInfo: TestInfo,                      // test info (status, title, …)
) => Promise<void>
```

`TestInfo` properties (selection):

| Property | Type | Description |
|---|---|---|
| `title` | `string` | Test title |
| `file` | `string` | File path |
| `line` | `number` | Line number |
| `status` | `'passed' \| 'failed' \| 'timedOut' \| 'skipped' \| 'interrupted'` | Test result |
| `expectedStatus` | `'passed' \| 'failed' \| 'skipped'` | Expected result |
| `retry` | `number` | Current retry attempt (0 = first) |
| `workerIndex` | `number` | Worker index |
| `parallelIndex` | `number` | Parallel index |
| `timeout` | `number` | Test timeout in ms |
| `attachments` | `Attachment[]` | Test attachments |
| `annotations` | `Annotation[]` | Test annotations |
| `snapshotDir` | `string` | Snapshot directory |
| `outputDir` | `string` | Output directory for this test |
| `outputPath(...pathSegments)` | `string` | Output path helper |
| `snapshotPath(...pathSegments)` | `string` | Snapshot path helper |
| `setTimeout(timeout)` | `void` | Change the test timeout |

---

## Global Setup/Teardown

### Recommended approach: project dependencies

```typescript
// playwright.config.ts
projects: [
  {
    name: 'setup db',
    testMatch: /global\.setup\.ts/,
    teardown: 'cleanup db',
  },
  {
    name: 'cleanup db',
    testMatch: /global\.teardown\.ts/,
  },
  {
    name: 'chromium',
    use: { ...devices['Desktop Chrome'] },
    dependencies: ['setup db'],
  },
],
```

```typescript
// tests/global.setup.ts
import { test as setup } from '@playwright/test';

setup('create new database', async ({ request }) => {
  // Playwright fixtures are available here
  await request.post('/api/create-db');
});
```

**Advantages over `globalSetup`:**
- Appears in the HTML report
- Trace recording supported
- Playwright fixtures available
- Retries/parallelism respected

### globalSetup/globalTeardown (legacy)

```typescript
// playwright.config.ts
export default defineConfig({
  globalSetup: require.resolve('./global-setup'),
  globalTeardown: require.resolve('./global-teardown'),
});
```

```typescript
// global-setup.ts
import { chromium, type FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
  const { baseURL, storageState } = config.projects[0].use;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(baseURL!);
  await page.getByLabel('User Name').fill('user');
  await page.getByLabel('Password').fill('password');
  await page.getByText('Sign in').click();
  await page.context().storageState({ path: storageState as string });
  await browser.close();
}

export default globalSetup;
```

**Passing data to tests:**

```typescript
// In globalSetup:
process.env.DB_URL = 'postgres://localhost/test';
process.env.API_TOKEN = JSON.stringify({ token: 'secret' });

// In tests:
test('example', async ({ page }) => {
  const { token } = JSON.parse(process.env.API_TOKEN!);
});
```

---

## Parametrization

### Simple parametrization with forEach

```typescript
const datasets = [
  { name: 'Alice', expected: 'Hello, Alice!' },
  { name: 'Bob',   expected: 'Hello, Bob!' },
];

datasets.forEach(({ name, expected }) => {
  test(`greeting for ${name}`, async ({ page }) => {
    await page.goto(`/greet?name=${name}`);
    await expect(page.getByRole('heading')).toHaveText(expected);
  });
});
```

Keep hooks outside the loop so they are only called once.

### Parametrized projects (option fixtures)

```typescript
// my-test.ts
type PersonOption = { person: string };
export const test = base.extend<PersonOption>({
  person: ['John', { option: true }],
});

// test.spec.ts
test('greeting', async ({ page, person }) => {
  await expect(page.getByText(`Hello, ${person}`)).toBeVisible();
});
```

```typescript
// playwright.config.ts
projects: [
  { name: 'alice', use: { person: 'Alice' } },
  { name: 'bob',   use: { person: 'Bob' } },
],
```

### CSV-based tests

```typescript
import { parse } from 'csv-parse/sync';
import * as fs from 'fs';

const records = parse(fs.readFileSync('testdata.csv'), {
  columns: true,
  skip_empty_lines: true,
});

for (const record of records) {
  test(`${record.test_case}`, async ({ page }) => {
    await page.goto(record.url);
    await expect(page.getByTestId('result')).toHaveText(record.expected);
  });
}
```

---

Source: https://playwright.dev/docs/test-fixtures | https://playwright.dev/docs/test-global-setup-teardown | https://playwright.dev/docs/test-parameterize
