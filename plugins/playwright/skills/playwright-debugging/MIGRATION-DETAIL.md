# Migrating to Playwright

## Contents

- [Migrating from Puppeteer](#migrating-from-puppeteer)
- [Migrating from Protractor](#migrating-from-protractor)
- [Connecting to Selenium Grid](#connecting-to-selenium-grid)
- [Advantages after the migration](#advantages-after-the-migration)
- [Sources](#sources)

## Migrating from Puppeteer

### Core principles

1. Most Puppeteer APIs can be carried over unchanged
2. Stop using `ElementHandle`; prefer locators and web-first assertions
3. Playwright supports cross-browser automation (Chrome, Firefox, WebKit)
4. Explicit `waitFor*` calls become unnecessary thanks to auto-waiting

### API comparison table

| Puppeteer | Playwright |
|-----------|-----------|
| `puppeteer.launch()` | `playwright.chromium.launch()` (specify the browser engine explicitly) |
| `{ product: 'firefox' }` | `playwright.firefox.launch()` |
| — | `playwright.webkit.launch()` (not available in Puppeteer) |
| `createIncognitoBrowserContext()` | `browser.newContext()` |
| `page.setViewport({ width, height })` | `page.setViewportSize({ width, height })` |
| `page.waitForXPath()` | `page.waitForSelector()` (XPath is still supported) |
| `page.waitForNetworkIdle()` | `page.waitForLoadState('networkidle')` |
| `page.$eval()` | Assertions / locators (prefer web-first) |
| `page.$()` | `page.locator()` |
| `page.$x()` | `page.locator('xpath=...')` |
| — | `locator.check()` / `locator.uncheck()` |
| `element.click()` | `locator.click()` |
| `element.focus()` | `locator.focus()` |
| `element.hover()` | `locator.hover()` |
| `element.select()` | `locator.selectOption()` |
| `element.tap()` | `locator.tap()` |
| `element.type()` | `locator.fill()` |
| `page.waitForFileChooser()` + `uploadFile()` | `locator.setInputFiles()` |
| `page.cookies()` | `browserContext.cookies()` |
| `page.deleteCookie()` | `browserContext.clearCookies()` |
| `page.setCookie()` | `browserContext.addCookies()` |

### Automation script: before/after

**Puppeteer:**
```javascript
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('https://playwright.dev/', { waitUntil: 'networkidle2' });
  await page.screenshot({ path: 'example.png' });
  await browser.close();
})();
```

**Playwright (equivalent):**
```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto('https://playwright.dev/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'example.png' });
  await browser.close();
})();
```

Key changes:
- `setViewport` -> `setViewportSize`
- `networkidle2` -> `networkidle`
- Explicit browser engine (`chromium`)

### Test framework: Puppeteer+Jest -> Playwright Test

**Puppeteer + Jest:**
```javascript
import puppeteer from 'puppeteer';

describe('Playwright homepage', () => {
  let browser, page;
  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
  });
  it('contains hero title', async () => {
    await page.goto('https://playwright.dev/');
    await page.waitForSelector('.hero__title');
    const text = await page.$eval('.hero__title', e => e.textContent);
    expect(text).toContain('Playwright enables reliable end-to-end testing');
  });
  afterAll(() => browser.close());
});
```

**Playwright Test (modernized):**
```javascript
import { test, expect } from '@playwright/test';

test.describe('Playwright homepage', () => {
  test('contains hero title', async ({ page }) => {
    await page.goto('https://playwright.dev/');
    const titleLocator = page.locator('.hero__title');
    await expect(titleLocator).toContainText(
      'Playwright enables reliable end-to-end testing'
    );
  });
});
```

Key differences:
- Import from `@playwright/test`
- `page` is injected as a test fixture
- No `beforeAll`/`afterAll` boilerplate
- Locators replace `$eval()`
- Web-first assertions

### Locator strictness

Locators are strict: all operations throw an exception if more than one element matches the selector.

---

## Migrating from Protractor

### Core principles

1. No more `webdriver-manager` / Selenium needed
2. Protractor's `ElementFinder` -> Playwright Test locators
3. `waitForAngular` is replaced by auto-waiting
4. All Playwright operations require `await`

### API comparison table

| Protractor | Playwright Test |
|-----------|----------------|
| `element(by.buttonText('...'))` | `page.locator('button, input[type="button"]').filter({ hasText: '...' })` |
| `element(by.css('...'))` | `page.locator('...')` |
| `element(by.cssContainingText('..1..', '..2..'))` | `page.locator('..1..').filter({ hasText: '..2..' })` |
| `element(by.id('...'))` | `page.locator('#...')` |
| `element(by.model('...'))` | `page.locator('[ng-model="..."]')` |
| `element(by.repeater('...'))` | `page.locator('[ng-repeat="..."]')` |
| `element(by.xpath('...'))` | `page.locator('xpath=...')` |
| `element.all` | `page.locator(...)` (list of elements) |
| `browser.get(url)` | `await page.goto(url)` |
| `browser.getCurrentUrl()` | `page.url()` |

### Test migration: before/after

**Protractor:**
```javascript
describe('angularjs homepage todo list', function() {
  it('should add a todo', function() {
    browser.get('https://angularjs.org');
    element(by.model('todoList.todoText')).sendKeys('first test');
    element(by.css('[value="add"]')).click();
    const todoList = element.all(by.repeater('todo in todoList.todos'));
    expect(todoList.count()).toEqual(3);
  });
});
```

**Playwright Test:**
```javascript
const { test, expect } = require('@playwright/test');

test.describe('angularjs homepage todo list', () => {
  test('should add a todo', async ({ page }) => {
    await page.goto('https://angularjs.org');
    await page.locator('[ng-model="todoList.todoText"]').fill('first test');
    await page.locator('[value="add"]').click();
    const todoList = page.locator('[ng-repeat="todo in todoList.todos"]');
    await expect(todoList).toHaveCount(3);
  });
});
```

### `waitForAngular` replacement

Playwright waits for DOM readiness automatically. In special cases (older Angular apps):

**Option 1 - Protractor client scripts:**
```javascript
async function waitForAngular(page) {
  const clientSideScripts = require('protractor/built/clientsidescripts.js');
  await page.evaluate(clientSideScripts.waitForAngular, '');
}
```

**Option 2 - Angular 2+ (recommended):**
```javascript
async function waitForAngular(page) {
  await page.evaluate(async () => {
    if (window.getAllAngularTestabilities) {
      const whenStable = (testability) =>
        new Promise((resolve) => testability.whenStable(resolve));
      await Promise.all(
        window.getAllAngularTestabilities().map(whenStable)
      );
    }
  });
}
```

---

## Connecting to Selenium Grid

### How it works

Playwright connects to Selenium Grid 4 via the Chrome DevTools Protocol (CDP).
The actual code does **not** change — just set environment variables.

### Environment variables

| Variable | Description |
|----------|-------------|
| `SELENIUM_REMOTE_URL` | Points at the Selenium Grid hub (e.g. `http://selenium-hub:4444`) |
| `SELENIUM_REMOTE_CAPABILITIES` | Additional grid capabilities as JSON |
| `SELENIUM_REMOTE_HEADERS` | Custom headers for authentication / cloud services as JSON |
| `SE_NODE_GRID_URL` | Hub URL for Selenium nodes in distributed setups |
| `DEBUG` | `pw:browser*` for detailed logging |

### Usage

```bash
# Set the hub URL, then test as usual
SELENIUM_REMOTE_URL=http://localhost:4444 npx playwright test
```

With additional capabilities:
```bash
SELENIUM_REMOTE_URL=http://selenium-hub:4444 \
SELENIUM_REMOTE_CAPABILITIES='{"mygrid:options":{"os":"windows","username":"John","password":"secure"}}' \
npx playwright test
```

### Docker: standalone mode

```yaml
# docker-compose.yml
services:
  selenium:
    image: selenium/standalone-chrome:latest
    ports:
      - "4444:4444"
    shm_size: '2gb'
```

```bash
SELENIUM_REMOTE_URL=http://localhost:4444 npx playwright test
```

### Docker: hub + node mode

```yaml
services:
  selenium-hub:
    image: selenium/hub:latest
    ports:
      - "4442-4444:4442-4444"

  chrome-node:
    image: selenium/node-chrome:latest
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
      - SE_NODE_GRID_URL=http://selenium-hub:4444
```

### Limitations

- Only Google Chrome and Microsoft Edge are supported
- Feature marked as **experimental**
- Selenium 3: best effort with direct node access
- Selenium Grid 4 recommended (CDP support)

---

## Advantages after the migration

- Zero-config TypeScript support
- Multi-browser (Chrome, Firefox, Safari) without additional configuration
- Parallel execution and test isolation
- Built-in artifact collection (traces, videos, screenshots)
- Playwright Inspector, code generation, tracing

---

## Sources

- https://playwright.dev/docs/puppeteer
- https://playwright.dev/docs/protractor
- https://playwright.dev/docs/selenium-grid
