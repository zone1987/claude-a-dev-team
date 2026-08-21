# Playwright Page Object Model & Best Practices

## Contents

- [Page Object Model (POM)](#page-object-model-pom)
- [Best Practices](#best-practices)
- [Debugging](#debugging)
- [Test organization](#test-organization)
- [CI optimization](#ci-optimization)

## Page Object Model (POM)

### Purpose

Page objects serve two purposes:
1. **Simplify authoring**: a higher-level API that matches the application
2. **Simplify maintenance**: centralize selectors in one place and reuse code

### Structure

```typescript
// pages/PlaywrightDevPage.ts
import { type Page, type Locator, expect } from '@playwright/test';

export class PlaywrightDevPage {
  readonly page: Page;

  // Locators as readonly properties (lazy evaluation)
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

### Usage in tests

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

### Combining POM with fixtures

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

### 1. Test user behavior, not implementation

```typescript
// GOOD: tests what the user sees and does
await page.getByRole('button', { name: 'Submit' }).click();
await expect(page.getByText('Thank you!')).toBeVisible();

// BAD: tests implementation details
await page.click('.submit-btn-v2');
expect(await page.evaluate(() => window._formSubmitted)).toBe(true);
```

### 2. Test isolation

Every test should be fully isolated (its own cookies, storage, data):

```typescript
test.beforeEach(async ({ page }) => {
  // Reset state
  await page.goto('/');
});

// Isolation via fixtures (better):
export const test = base.extend({
  isolatedPage: async ({ browser }, use) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await use(page);
    await context.close();
  },
});
```

### 3. Preferred locators (priority)

| Priority | Locator | Example |
|---|---|---|
| 1 (best) | Role-based | `getByRole('button', { name: 'Submit' })` |
| 2 | Label | `getByLabel('Email address')` |
| 3 | Placeholder | `getByPlaceholder('user@example.com')` |
| 4 | Text | `getByText('Sign in')` |
| 5 | Alt text | `getByAltText('Playwright logo')` |
| 6 | Title | `getByTitle('Close dialog')` |
| 7 | Test ID | `getByTestId('submit-btn')` |
| 8 (avoid) | CSS class | `locator('.btn-submit')` |
| 9 (avoid) | XPath | `locator('//button')` |

```typescript
// GOOD: resilient against DOM changes
page.getByRole('button', { name: 'submit' });
page.getByLabel('Password');
page.getByTestId('checkout-btn');

// BAD: brittle
page.locator('button.buttonIcon.episode-actions-later');
page.locator('#main > div:nth-child(2) > button');
```

### 4. Chaining and filtering locators

```typescript
// Narrow down to a context
await page
  .getByRole('listitem')
  .filter({ hasText: 'Product 2' })
  .getByRole('button', { name: 'Add to cart' })
  .click();

// within equivalent
const dialog = page.getByRole('dialog');
await dialog.getByRole('button', { name: 'Confirm' }).click();
```

### 5. Use web-first assertions

```typescript
// GOOD: waits and retries automatically
await expect(page.getByText('Welcome')).toBeVisible();

// BAD: immediate evaluation, no auto-wait
expect(await page.getByText('Welcome').isVisible()).toBe(true);
```

### 6. Mock third-party dependencies

```typescript
await page.route('**/api/external-service', route =>
  route.fulfill({ status: 200, body: JSON.stringify({ data: 'mocked' }) })
);
```

### 7. No hard waits

```typescript
// BAD
await page.waitForTimeout(2000);

// GOOD: wait for a condition
await page.waitForSelector('[data-loaded]');
await expect(page.getByRole('status')).toHaveText('Ready');
```

### 8. Control test data

- Use a staging environment with known data
- Do not test against real external APIs in E2E tests
- Consistent operating systems for visual regression

---

## Debugging

### Locally

```bash
# Playwright Inspector (step by step)
npx playwright test --debug
npx playwright test example.spec.ts --debug
npx playwright test example.spec.ts:10 --debug

# Headed mode (browser visible)
npx playwright test --headed

# VS Code Extension
# "Run test" and "Debug test" directly in the editor
```

### CI debugging with the Trace Viewer

```typescript
// playwright.config.ts
use: { trace: 'on-first-retry' }
```

```bash
npx playwright show-report
# In the HTML report, click the failed test -> open the trace
```

Trace Viewer shows: timeline, DOM snapshots, network requests, console log.

### Testing locators

```bash
# Codegen: record locators interactively
npx playwright codegen https://example.com
```

In UI mode: locator picker for verifying selectors.

---

## Test organization

### Multiple browsers (projects)

```typescript
projects: [
  { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit',   use: { ...devices['Desktop Safari'] } },
],
```

### Use parallelization

```typescript
// Global
export default defineConfig({ fullyParallel: true });

// Per file
test.describe.configure({ mode: 'parallel' });
```

### Sharding for large suites

```bash
npx playwright test --shard=1/4   # distributed across 4 machines
```

### File naming for sequential execution (without fullyParallel)

```
001-setup.spec.ts
002-login.spec.ts
003-checkout.spec.ts
```

---

## CI optimization

```bash
# Install only the required browsers
npx playwright install chromium --with-deps

# On CI: 2 workers, enable retries
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

### Keeping dependencies up to date

```bash
npm install -D @playwright/test@latest
npx playwright install   # new browser versions
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

Catches missing `await` before Playwright calls.

---

Source: https://playwright.dev/docs/pom | https://playwright.dev/docs/best-practices
