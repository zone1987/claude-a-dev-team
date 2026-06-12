# Playwright Fixtures — Vollstaendige Referenz

## Eingebaute Fixtures

| Fixture | Typ | Scope | Beschreibung |
|---|---|---|---|
| `page` | `Page` | test | Isolierte Seite fuer jeden Test |
| `context` | `BrowserContext` | test | Isolierter Browser-Kontext; `page` gehoert dazu |
| `browser` | `Browser` | worker | Gemeinsame Browser-Instanz (ressourceneffizient) |
| `browserName` | `string` | worker | Aktueller Browser: `'chromium'`, `'firefox'`, `'webkit'` |
| `request` | `APIRequestContext` | test | Isolierte API-Request-Instanz |

---

## Eigene Fixtures mit `test.extend()`

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

    await use(todoPage);           // <-- Teardown beginnt nach use()

    await todoPage.removeAll();
  },

  adminPage: async ({ page }, use) => {
    await use(new AdminPage(page));
  },
});

export { expect } from '@playwright/test';
```

**Muster:** Setup → `await use(value)` → Teardown

---

## Fixture-Scopes

### Test-Scope (Standard)

```typescript
export const test = base.extend<{ myFixture: string }>({
  myFixture: async ({}, use) => {
    await use('hello');
  },
  // Implizit: { scope: 'test' }
});
```

Wird fuer jeden Test neu aufgebaut und abgebaut.

### Worker-Scope

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

Laeuft einmal pro Worker-Prozess; wird ueber alle Tests geteilt.
`workerInfo.workerIndex` ermoeglicht Datenisolation.

---

## Automatische Fixtures (auto)

Werden fuer jeden Test ausgefuehrt, ohne dass der Test sie explizit anfordert:

```typescript
// Verhalt sich wie beforeEach/afterEach
forEachTest: [async ({ page }, use, testInfo) => {
  await page.goto('http://localhost:8000');
  await use();
  // Immer ausgefuehrt, auch bei Fehlschlag:
  if (testInfo.status !== testInfo.expectedStatus) {
    console.log('Test failed, saving logs...');
    testInfo.attachments.push({
      name: 'logs',
      contentType: 'text/plain',
      body: Buffer.from('error log'),
    });
  }
}, { auto: true }],

// Verhalt sich wie beforeAll/afterAll (worker-scoped auto)
forEachWorker: [async ({}, use, workerInfo) => {
  console.log(`Worker ${workerInfo.workerIndex} startet`);
  await use();
  console.log('Worker beendet');
}, { scope: 'worker', auto: true }],
```

---

## Option-Fixtures (konfigurierbar)

Erlauben Konfiguration ueber `playwright.config.ts` / `use`:

```typescript
// fixtures.ts
type MyOptions = {
  defaultItem: string;
  apiUrl: string;
};

export const test = base.extend<MyOptions & MyFixtures>({
  // Option-Fixture mit Default
  defaultItem: ['Something nice', { option: true }],
  apiUrl: ['http://localhost:3000', { option: true }],

  // Abhaengig von Option-Fixture
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

## Eingebaute Fixtures ueberschreiben

```typescript
export const test = base.extend({
  // Alle Tests starten auf baseURL
  page: async ({ baseURL, page }, use) => {
    await page.goto(baseURL!);
    await use(page);
  },
});

// Einzelne Option zuruecksetzen:
test.use({ baseURL: undefined });
```

---

## Fixture-Komposition (Abhaengigkeiten)

```typescript
export const test = base.extend({
  // userFixture haengt von dbFixture ab
  dbFixture: async ({}, use) => {
    const db = await openDB();
    await use(db);
    await db.close();               // teardown nach userFixture
  },

  userFixture: async ({ dbFixture }, use) => {
    const user = await dbFixture.createUser();
    await use(user);
    await dbFixture.deleteUser(user.id);
  },
});
```

Setup-Reihenfolge: `dbFixture` → `userFixture`
Teardown-Reihenfolge: `userFixture` → `dbFixture` (umgekehrt)

---

## Fixtures zusammenfuehren

```typescript
import { mergeTests } from '@playwright/test';
import { test as dbTest } from './database-fixtures';
import { test as a11yTest } from './a11y-fixtures';

export const test = mergeTests(dbTest, a11yTest);
```

---

## Fixture-Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `scope` | `'test' \| 'worker'` | `'test'` | Lebensdauer des Fixtures |
| `auto` | `boolean` | `false` | Automatisch fuer jeden Test ausfuehren |
| `option` | `boolean` | `false` | Per Konfig/use ueberschreibbar |
| `timeout` | `number` | (test timeout) | Eigener Timeout fuer dieses Fixture in ms |
| `box` | `boolean` | `false` | Aus Test-Berichten ausblenden |
| `title` | `string` | (Fixture-Name) | Angezeigter Name in Reports |

```typescript
// Fixture mit eigenem Timeout (fuer langsame Operationen)
slowFixture: [async ({}, use) => {
  await someSlowOperation();
  await use('result');
}, { timeout: 120_000, scope: 'worker' }],

// Fixture aus Reports ausblenden
helperFixture: [async ({}, use) => {
  await use('helper');
}, { box: true }],
```

---

## Fixture-Signatur vollstaendig

```typescript
fixtureFunction: async (
  fixtures: BuiltInFixtures & MyFixtures,  // alle verfuegbaren Fixtures
  use: (value: T) => Promise<void>,        // Wert bereitstellen
  testInfo: TestInfo,                      // Testinfos (Status, Title, …)
) => Promise<void>
```

`TestInfo`-Properties (Auswahl):

| Property | Typ | Beschreibung |
|---|---|---|
| `title` | `string` | Test-Titel |
| `file` | `string` | Dateipfad |
| `line` | `number` | Zeilennummer |
| `status` | `'passed' \| 'failed' \| 'timedOut' \| 'skipped' \| 'interrupted'` | Test-Ergebnis |
| `expectedStatus` | `'passed' \| 'failed' \| 'skipped'` | Erwartetes Ergebnis |
| `retry` | `number` | Aktueller Wiederholungsversuch (0 = erster) |
| `workerIndex` | `number` | Worker-Index |
| `parallelIndex` | `number` | Paralleler Index |
| `timeout` | `number` | Test-Timeout in ms |
| `attachments` | `Attachment[]` | Test-Anhaenge |
| `annotations` | `Annotation[]` | Test-Annotationen |
| `snapshotDir` | `string` | Snapshot-Verzeichnis |
| `outputDir` | `string` | Ausgabeverzeichnis fuer diesen Test |
| `outputPath(...pathSegments)` | `string` | Ausgabepfad-Helper |
| `snapshotPath(...pathSegments)` | `string` | Snapshot-Pfad-Helper |
| `setTimeout(timeout)` | `void` | Test-Timeout aendern |

---

## Global Setup/Teardown

### Empfohlener Weg: Project Dependencies

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
  // Playwright-Fixtures sind hier verfuegbar
  await request.post('/api/create-db');
});
```

**Vorteile gegenueber `globalSetup`:**
- Erscheint im HTML-Report
- Trace-Aufnahme unterstuetzt
- Playwright-Fixtures verfuegbar
- Retry/Parallelismus respektiert

### globalSetup/globalTeardown (Legacy)

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

**Daten an Tests weitergeben:**

```typescript
// In globalSetup:
process.env.DB_URL = 'postgres://localhost/test';
process.env.API_TOKEN = JSON.stringify({ token: 'secret' });

// In Tests:
test('example', async ({ page }) => {
  const { token } = JSON.parse(process.env.API_TOKEN!);
});
```

---

## Parametrisierung

### Einfache Parametrisierung mit forEach

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

Hooks ausserhalb der Schleife, damit sie nur einmal aufgerufen werden.

### Parametrisierte Projekte (Option-Fixtures)

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

### CSV-basierte Tests

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
