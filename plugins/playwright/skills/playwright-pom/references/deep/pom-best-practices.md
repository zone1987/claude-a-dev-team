# Playwright Page Object Model & Best Practices

## Page Object Model (POM)

### Zweck

Page Objects erfullen zwei Aufgaben:
1. **Authoring vereinfachen**: Hoehere API, die zur Anwendung passt
2. **Wartung vereinfachen**: Selektoren an einem Ort zentralisieren und Code wiederverwenden

### Struktur

```typescript
// pages/PlaywrightDevPage.ts
import { type Page, type Locator, expect } from '@playwright/test';

export class PlaywrightDevPage {
  readonly page: Page;

  // Locators als readonly Properties (lazy evaluation)
  readonly getStartedLink: Locator;
  readonly gettingStartedHeader: Locator;
  readonly pomLink: Locator;
  readonly tocList: Locator;

  constructor(page: Page) {
    this.page = page;
    this.getStartedLink  = page.getByRole('link', { name: 'Get started' });
    this.gettingStartedHeader = page.getByRole('heading', { name: 'Installation' });
    this.pomLink  = page.getByRole('listitem').filter({ hasText: 'Page Object Model' });
    this.tocList  = page.locator('article').getByRole('listitem');
  }

  async goto() {
    await this.page.goto('https://playwright.dev');
  }

  async getStarted() {
    await this.getStartedLink.first().click();
    await expect(this.gettingStartedHeader).toBeVisible();
  }

  async pageObjectModel() {
    await this.getStarted();
    await this.pomLink.click();
  }
}
```

### Verwendung in Tests

```typescript
// tests/playwright-dev.spec.ts
import { test, expect } from '@playwright/test';
import { PlaywrightDevPage } from '../pages/PlaywrightDevPage';

test.describe('playwright.dev', () => {
  test('has title', async ({ page }) => {
    const playwrightDev = new PlaywrightDevPage(page);
    await playwrightDev.goto();
    await expect(page).toHaveTitle(/Playwright/);
  });

  test('get started link', async ({ page }) => {
    const playwrightDev = new PlaywrightDevPage(page);
    await playwrightDev.getStarted();
  });

  test('page object model', async ({ page }) => {
    const playwrightDev = new PlaywrightDevPage(page);
    await playwrightDev.pageObjectModel();
    await expect(playwrightDev.tocList).toHaveText([
      'Introduction',
      'Before you begin',
      // ...
    ]);
  });
});
```

### POM mit Fixtures kombinieren

```typescript
// fixtures.ts
import { test as base } from '@playwright/test';
import { PlaywrightDevPage } from './pages/PlaywrightDevPage';

type Fixtures = {
  playwrightDev: PlaywrightDevPage;
};

export const test = base.extend<Fixtures>({
  playwrightDev: async ({ page }, use) => {
    const p = new PlaywrightDevPage(page);
    await p.goto();
    await use(p);
  },
});
```

---

## Best Practices

### 1. Nutzerverhalten testen, nicht Implementierung

```typescript
// GUT: testet was der Nutzer sieht und tut
await page.getByRole('button', { name: 'Submit' }).click();
await expect(page.getByText('Thank you!')).toBeVisible();

// SCHLECHT: testet Implementierungsdetails
await page.click('.submit-btn-v2');
expect(await page.evaluate(() => window._formSubmitted)).toBe(true);
```

### 2. Test-Isolation

Jeder Test sollte vollstaendig isoliert sein (eigene Cookies, Storage, Daten):

```typescript
test.beforeEach(async ({ page }) => {
  // State zuruecksetzen
  await page.goto('/');
});

// Isolation durch Fixtures (besser):
export const test = base.extend({
  isolatedPage: async ({ browser }, use) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await use(page);
    await context.close();
  },
});
```

### 3. Bevorzugte Locatoren (Prioritaet)

| Prioritaet | Locator | Beispiel |
|---|---|---|
| 1 (beste) | Rollen-basiert | `getByRole('button', { name: 'Submit' })` |
| 2 | Label | `getByLabel('Email address')` |
| 3 | Placeholder | `getByPlaceholder('user@example.com')` |
| 4 | Text | `getByText('Sign in')` |
| 5 | Alt-Text | `getByAltText('Playwright logo')` |
| 6 | Title | `getByTitle('Close dialog')` |
| 7 | Test-ID | `getByTestId('submit-btn')` |
| 8 (vermeiden) | CSS-Klasse | `locator('.btn-submit')` |
| 9 (vermeiden) | XPath | `locator('//button')` |

```typescript
// GUT: resilient gegen DOM-Aenderungen
page.getByRole('button', { name: 'submit' });
page.getByLabel('Password');
page.getByTestId('checkout-btn');

// SCHLECHT: bruechig
page.locator('button.buttonIcon.episode-actions-later');
page.locator('#main > div:nth-child(2) > button');
```

### 4. Locatoren verketten und filtern

```typescript
// Auf Kontext einengen
await page
  .getByRole('listitem')
  .filter({ hasText: 'Product 2' })
  .getByRole('button', { name: 'Add to cart' })
  .click();

// within-Aequivalent
const dialog = page.getByRole('dialog');
await dialog.getByRole('button', { name: 'Confirm' }).click();
```

### 5. Web-First-Assertions verwenden

```typescript
// GUT: wartet und wiederholt automatisch
await expect(page.getByText('Welcome')).toBeVisible();

// SCHLECHT: sofortige Auswertung, kein Auto-Wait
expect(await page.getByText('Welcome').isVisible()).toBe(true);
```

### 6. Drittanbieter-Abhaengigkeiten mocken

```typescript
await page.route('**/api/external-service', route =>
  route.fulfill({ status: 200, body: JSON.stringify({ data: 'mocked' }) })
);
```

### 7. Keine harten Wartezeiten

```typescript
// SCHLECHT
await page.waitForTimeout(2000);

// GUT: auf Bedingung warten
await page.waitForSelector('[data-loaded]');
await expect(page.getByRole('status')).toHaveText('Ready');
```

### 8. Test-Daten kontrollieren

- Staging-Umgebung mit bekannten Daten verwenden
- Kein Testen gegen echte externe APIs in E2E-Tests
- Konsistente Betriebssysteme fuer visuelle Regression

---

## Debugging

### Lokal

```bash
# Playwright Inspector (Schritt-fuer-Schritt)
npx playwright test --debug
npx playwright test example.spec.ts --debug
npx playwright test example.spec.ts:10 --debug

# Headed-Modus (Browser sichtbar)
npx playwright test --headed

# VS Code Extension
# "Run test" und "Debug test" direkt im Editor
```

### CI-Debugging mit Trace Viewer

```typescript
// playwright.config.ts
use: { trace: 'on-first-retry' }
```

```bash
npx playwright show-report
# Im HTML-Report auf fehlgeschlagenen Test klicken -> Trace oeffnen
```

Trace Viewer zeigt: Timeline, DOM-Snapshots, Netzwerk-Requests, Console-Log.

### Locatoren testen

```bash
# Codegen: interaktiv Locatoren aufzeichnen
npx playwright codegen https://example.com
```

Im UI-Modus: Locator-Picker zum Verifizieren von Selektoren.

---

## Test-Organisation

### Mehrere Browser (Projects)

```typescript
projects: [
  { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit',   use: { ...devices['Desktop Safari'] } },
],
```

### Parallelisierung nutzen

```typescript
// Global
export default defineConfig({ fullyParallel: true });

// Per Datei
test.describe.configure({ mode: 'parallel' });
```

### Sharding fuer grosse Suites

```bash
npx playwright test --shard=1/4   # auf 4 Maschinen verteilt
```

### Datei-Benennung fuer sequenzielle Ausfuehrung (ohne fullyParallel)

```
001-setup.spec.ts
002-login.spec.ts
003-checkout.spec.ts
```

---

## CI-Optimierung

```bash
# Nur noetige Browser installieren
npx playwright install chromium --with-deps

# Auf CI: 2 Worker, Retries aktivieren
export default defineConfig({
  workers: process.env.CI ? 2 : undefined,
  retries: process.env.CI ? 2 : 0,
  reporter: process.env.CI ? 'blob' : 'html',
});
```

```typescript
// GitHub Actions
- name: Run Playwright tests
  run: npx playwright test
- uses: actions/upload-artifact@v4
  if: ${{ !cancelled() }}
  with:
    name: playwright-report
    path: playwright-report/
```

### Abhängigkeiten aktuell halten

```bash
npm install -D @playwright/test@latest
npx playwright install   # neue Browser-Versionen
npx playwright --version
```

### TypeScript + ESLint

```json
// .eslintrc
{
  "rules": {
    "@typescript-eslint/no-floating-promises": "error"
  }
}
```

Fangen fehlende `await` vor Playwright-Aufrufen ab.

---

Source: https://playwright.dev/docs/pom | https://playwright.dev/docs/best-practices
