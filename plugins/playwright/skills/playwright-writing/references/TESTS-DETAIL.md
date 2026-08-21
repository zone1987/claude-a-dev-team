# Playwright: Writing tests, running them, Codegen, VS Code

## Contents

- [Test structure](#test-structure)
- [test() — function](#test-function)
- [test.describe() — grouping](#testdescribe-grouping)
- [Hooks](#hooks)
- [Page navigation](#page-navigation)
- [Interactions (quick reference)](#interactions-quick-reference)
- [expect() — assertions](#expect-assertions)
- [Complete test example](#complete-test-example)
- [CLI: running tests](#cli-running-tests)
- [Codegen: test recorder](#codegen-test-recorder)
- [VS Code extension](#vs-code-extension)

## Test structure

### Minimal test

```typescript
import { test, expect } from '@playwright/test';

test('check page title', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

### Test fixtures

Every test automatically gets isolated fixtures:
- `page` — new page in a fresh `BrowserContext`
- `context` — isolated `BrowserContext`
- `browser` — shared browser process

---

## test() — function

```typescript
test(title: string, fn: (fixtures) => Promise<void>): void
test(title: string, details: TestDetails, fn: (fixtures) => Promise<void>): void
```

Every test runs in a fresh, isolated `BrowserContext` (automatic isolation).

---

## test.describe() — grouping

```typescript
test.describe('Group', () => {
  test('Test 1', async ({ page }) => { /* ... */ });
  test('Test 2', async ({ page }) => { /* ... */ });
});

// Nested
test.describe('Outer group', () => {
  test.describe('Inner group', () => {
    test('deeply nested test', async ({ page }) => { /* ... */ });
  });
});
```

---

## Hooks

```typescript
test.describe('With hooks', () => {
  test.beforeAll(async () => {
    // Once before all tests of the group (no page fixture here)
  });

  test.afterAll(async () => {
    // Once after all tests of the group
  });

  test.beforeEach(async ({ page }) => {
    // Before each test; page fixture available
    await page.goto('https://playwright.dev/');
  });

  test.afterEach(async ({ page }) => {
    // After each test
  });

  test('first test', async ({ page }) => {
    await expect(page).toHaveTitle(/Playwright/);
  });
});
```

---

## Page navigation

```typescript
await page.goto('https://example.com');
// Playwright waits for the load state before continuing
```

---

## Interactions (quick reference)

| Action | Method |
|---|---|
| Click | `await locator.click()` |
| Enter text | `await locator.fill('text')` |
| Check checkbox | `await locator.check()` |
| Uncheck checkbox | `await locator.uncheck()` |
| Hover | `await locator.hover()` |
| Focus | `await locator.focus()` |
| Press key | `await locator.press('Enter')` |
| Upload file | `await locator.setInputFiles('/pfad/datei.pdf')` |
| Select option | `await locator.selectOption('wert')` |

---

## expect() — assertions

### Web-first assertions (with `await` — have auto-retry)

These assertions wait until the condition is met or a timeout occurs.

| Assertion | Checks |
|---|---|
| `await expect(locator).toBeChecked()` | Checkbox is checked |
| `await expect(locator).toBeChecked({ checked: false })` | Checkbox is unchecked |
| `await expect(locator).toBeDisabled()` | Element is disabled |
| `await expect(locator).toBeEditable()` | Element is editable |
| `await expect(locator).toBeEmpty()` | Element has no text / empty input |
| `await expect(locator).toBeEnabled()` | Element is enabled |
| `await expect(locator).toBeFocused()` | Element has focus |
| `await expect(locator).toBeHidden()` | Element is not visible |
| `await expect(locator).toBeInViewport()` | Element is in the viewport |
| `await expect(locator).toBeVisible()` | Element is visible |
| `await expect(locator).toContainText('text')` | Element contains text (substring) |
| `await expect(locator).toContainText(/regex/)` | Element contains text (regex) |
| `await expect(locator).toHaveAttribute('name', 'wert')` | Element has attribute with value |
| `await expect(locator).toHaveClass('klasse')` | Element has CSS class |
| `await expect(locator).toHaveCount(n)` | Number of elements |
| `await expect(locator).toHaveCSS('prop', 'wert')` | Computed CSS |
| `await expect(locator).toHaveId('id')` | Element ID |
| `await expect(locator).toHaveJSProperty('prop', wert)` | JS property |
| `await expect(locator).toHaveRole('button')` | ARIA role |
| `await expect(locator).toHaveText('exakt')` | Exact text |
| `await expect(locator).toHaveText(['a', 'b'])` | Texts of all elements |
| `await expect(locator).toHaveValue('wert')` | Input value |
| `await expect(locator).toHaveValues(['a', 'b'])` | Multi-select values |
| `await expect(page).toHaveTitle('Titel')` | Page title |
| `await expect(page).toHaveTitle(/Regex/)` | Page title via regex |
| `await expect(page).toHaveURL('https://...')` | Page URL |
| `await expect(page).toHaveURL(/regex/)` | Page URL via regex |
| `await expect(response).toBeOK()` | HTTP response is OK (2xx) |

#### Negation

```typescript
await expect(locator).not.toBeVisible();
await expect(page).not.toHaveURL(/error/);
```

#### Options for all web-first assertions

```typescript
await expect(locator).toBeVisible({ timeout: 5000 }); // ms, default: 5000
```

| Option | Type | Default | Description |
|---|---|---|---|
| `timeout` | `number` | `5000` | Max. wait time in ms |
| `message` | `string` | — | Custom error message |

### Synchronous assertions (without `await` — no retry)

```typescript
expect(value).toEqual(erwarteterWert);
expect(array).toContain(element);
expect(value).toBeTruthy();
expect(value).toBeFalsy();
expect(value).toBeNull();
expect(value).toBeDefined();
expect(number).toBeGreaterThan(n);
expect(number).toBeLessThan(n);
expect(string).toMatch(/regex/);
```

### Soft assertions

Collect failures without aborting the test immediately:

```typescript
await expect.soft(locator).toHaveText('erwartet');
await expect.soft(locator2).toBeVisible();
// Test continues even if assertions fail
```

---

## Complete test example

```typescript
import { test, expect } from '@playwright/test';

test.describe('Todo app', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://demo.playwright.dev/todomvc');
  });

  test('add todo', async ({ page }) => {
    await page.getByPlaceholder('What needs to be done?').fill('Einkaufen');
    await page.getByPlaceholder('What needs to be done?').press('Enter');

    await expect(page.getByTestId('todo-title')).toHaveText('Einkaufen');
    await expect(page.getByRole('listitem')).toHaveCount(1);
  });

  test('complete todo', async ({ page }) => {
    await page.getByPlaceholder('What needs to be done?').fill('Aufgabe');
    await page.getByPlaceholder('What needs to be done?').press('Enter');
    await page.getByRole('checkbox').first().check();

    await expect(page.getByRole('checkbox').first()).toBeChecked();
  });
});
```

---

## CLI: running tests

### Basic commands

```bash
npx playwright test                       # All tests headless
npx playwright test --headed              # With visible browser
npx playwright test --ui                  # UI mode (watch + live debug)
npx playwright test --debug               # Inspector debugging
npx playwright show-report                # Show HTML report
```

### Filters and selection

| Flag | Description | Example |
|---|---|---|
| `<datei>` | Run a specific file | `npx playwright test login.spec.ts` |
| `<dir1> <dir2>` | Multiple directories | `npx playwright test tests/auth/ tests/shop/` |
| `<keyword>` | File name contains keyword | `npx playwright test login home` |
| `-g "titel"` | Test title via grep | `npx playwright test -g "add a todo"` |
| `--last-failed` | Only the last failed ones | `npx playwright test --last-failed` |

### Browsers and parallelization

| Flag | Description | Example |
|---|---|---|
| `--project <name>` | Specific browser project | `npx playwright test --project webkit` |
| `--project a --project b` | Multiple projects | `npx playwright test --project webkit --project firefox` |

### Output and reporting

| Flag | Description |
|---|---|
| `--reporter=html` | HTML reporter |
| `--reporter=list` | List reporter |
| `--reporter=dot` | Compact dot reporter |

---

## Codegen: test recorder

### Basic command

```bash
npx playwright codegen [URL]
# URL is optional; it can also be entered in the browser window
```

Opens two windows:
1. Interactive browser for actions
2. Playwright Inspector with the generated code

### All CLI flags

| Flag | Type | Description | Example |
|---|---|---|---|
| `--viewport-size` | `string` | Viewport size | `--viewport-size="800,600"` |
| `--device` | `string` | Device emulation | `--device="iPhone 13"` |
| `--color-scheme` | `string` | `dark` or `light` | `--color-scheme=dark` |
| `--timezone` | `string` | Time zone | `--timezone="Europe/Berlin"` |
| `--geolocation` | `string` | GPS coordinates | `--geolocation="52.52,13.40"` |
| `--lang` | `string` | Language/locale | `--lang="de-DE"` |
| `--save-storage` | `string` | Save auth state | `--save-storage=auth.json` |
| `--load-storage` | `string` | Load auth state | `--load-storage=auth.json` |
| `--user-data-dir` | `string` | Browser profile directory | `--user-data-dir=/pfad/profil` |

### Assertion types in the recorder

| Type | Checks |
|---|---|
| Assert Visibility | Element visible/invisible |
| Assert Text | Specific text content |
| Assert Value | Value of an input |

### Inspector controls

| Button | Function |
|---|---|
| Record | Toggle recording on/off |
| Copy | Copy generated code |
| Clear | Reset code / new recording |
| Pick Locator | Pick an element selector |

### Saving and loading the auth state

```bash
# Record the login and save the auth state
npx playwright codegen github.com/login --save-storage=auth.json

# La	ter, continue with the saved auth state
npx playwright codegen --load-storage=auth.json github.com/dashboard
```

### Codegen in your own context (page.pause())

```typescript
import { chromium } from '@playwright/test';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  // Your own routing/interception logic
  await context.route('**/*', route => route.continue());
  const page = await context.newPage();
  // Opens the Inspector inside your own context
  await page.pause();
})();
```

---

## VS Code extension

### Installation

1. Open Extensions (`Cmd+Shift+X`), search for "Playwright", install the Microsoft extension
2. Command Palette (`Cmd+Shift+P`) → `Test: Install Playwright`
3. Choose browsers (Chromium / Firefox / WebKit), optionally GitHub Actions

### Running tests

| Action | Method |
|---|---|
| Single test | Click the green play icon next to the test |
| Multiple tests | Play icon at file or project level |
| Multi-browser | Select projects in the Playwright sidebar |
| Visible browser window | Enable "Show Browsers" in the sidebar |

### Debugging

| Function | Description |
|---|---|
| Breakpoints | Click the gutter line, then right-click → "Debug Test" |
| Live inspection | With "Show Browsers": click a locator = highlight the element |
| Error details | "expected vs. received" + full call log |
| AI help | Sparkle icon: Copilot suggestions for error causes |
| Trace Viewer | "Show Trace Viewer": timeline + DOM snapshots + network |

### Test recording (CodeGen in VS Code)

| Function | Description |
|---|---|
| Record new | Record a new test → `test-1.spec.ts` |
| Record at cursor | Append actions at the cursor position |
| Pick locator | Click an element → optimal locator in the clipboard |

### Switching configuration

Gear icon in the sidebar: switch between multiple `playwright.config.ts` files.

<!-- Sources:
https://playwright.dev/docs/writing-tests
https://playwright.dev/docs/running-tests
https://playwright.dev/docs/codegen-intro
https://playwright.dev/docs/codegen
https://playwright.dev/docs/getting-started-vscode
-->
