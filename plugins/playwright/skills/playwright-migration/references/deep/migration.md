# Migration zu Playwright

## Von Puppeteer migrieren

### Kernprinzipien

1. Die meisten Puppeteer-APIs koennen unveraendert uebernommen werden
2. `ElementHandle` nicht mehr verwenden; Locators und Web-First-Assertions bevorzugen
3. Playwright unterstuetzt Cross-Browser-Automation (Chrome, Firefox, WebKit)
4. Explizite `waitFor*`-Aufrufe entfallen durch Auto-Waiting

### API-Vergleichstabelle

| Puppeteer | Playwright |
|-----------|-----------|
| `puppeteer.launch()` | `playwright.chromium.launch()` (Browser-Engine explizit angeben) |
| `{ product: 'firefox' }` | `playwright.firefox.launch()` |
| — | `playwright.webkit.launch()` (in Puppeteer nicht verfuegbar) |
| `createIncognitoBrowserContext()` | `browser.newContext()` |
| `page.setViewport({ width, height })` | `page.setViewportSize({ width, height })` |
| `page.waitForXPath()` | `page.waitForSelector()` (XPath weiterhin unterstuetzt) |
| `page.waitForNetworkIdle()` | `page.waitForLoadState('networkidle')` |
| `page.$eval()` | Assertions / Locators (Web-First bevorzugen) |
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

### Automations-Script: Vorher/Nachher

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

**Playwright (aequivalent):**
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

Wesentliche Aenderungen:
- `setViewport` -> `setViewportSize`
- `networkidle2` -> `networkidle`
- Explizite Browser-Engine (`chromium`)

### Test-Framework: Puppeteer+Jest -> Playwright Test

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

**Playwright Test (modernisiert):**
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

Wesentliche Unterschiede:
- Import aus `@playwright/test`
- `page` wird als Test-Fixture injiziert
- Kein `beforeAll`/`afterAll`-Boilerplate
- Locators ersetzen `$eval()`
- Web-First-Assertions

### Locator-Strictness

Locators sind strikt: Alle Operationen werfen eine Exception, wenn mehr als ein Element den Selector trifft.

---

## Von Protractor migrieren

### Kernprinzipien

1. Kein `webdriver-manager` / Selenium mehr noetig
2. Protractors `ElementFinder` -> Playwright Test Locators
3. `waitForAngular` wird durch Auto-Waiting ersetzt
4. Alle Playwright-Operationen benoetigen `await`

### API-Vergleichstabelle

| Protractor | Playwright Test |
|-----------|----------------|
| `element(by.buttonText('...'))` | `page.locator('button, input[type="button"]').filter({ hasText: '...' })` |
| `element(by.css('...'))` | `page.locator('...')` |
| `element(by.cssContainingText('..1..', '..2..'))` | `page.locator('..1..').filter({ hasText: '..2..' })` |
| `element(by.id('...'))` | `page.locator('#...')` |
| `element(by.model('...'))` | `page.locator('[ng-model="..."]')` |
| `element(by.repeater('...'))` | `page.locator('[ng-repeat="..."]')` |
| `element(by.xpath('...'))` | `page.locator('xpath=...')` |
| `element.all` | `page.locator(...)` (Liste von Elementen) |
| `browser.get(url)` | `await page.goto(url)` |
| `browser.getCurrentUrl()` | `page.url()` |

### Test-Migration: Vorher/Nachher

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

### `waitForAngular`-Ersatz

Playwright wartet automatisch auf DOM-Bereitschaft. In Sonderfaellen (aeltere Angular-Apps):

**Option 1 - Protractor-Client-Skripte:**
```javascript
async function waitForAngular(page) {
  const clientSideScripts = require('protractor/built/clientsidescripts.js');
  await page.evaluate(clientSideScripts.waitForAngular, '');
}
```

**Option 2 - Angular 2+ (empfohlen):**
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

## Selenium Grid anbinden

### Funktionsprinzip

Playwright verbindet sich per Chrome DevTools Protocol (CDP) mit Selenium Grid 4.
Der eigentliche Code aendert sich **nicht** — nur Umgebungsvariablen setzen.

### Umgebungsvariablen

| Variable | Beschreibung |
|----------|-------------|
| `SELENIUM_REMOTE_URL` | Zeigt auf den Selenium Grid Hub (z.B. `http://selenium-hub:4444`) |
| `SELENIUM_REMOTE_CAPABILITIES` | Zusaetzliche Grid-Capabilities als JSON |
| `SELENIUM_REMOTE_HEADERS` | Custom-Headers fuer Authentifizierung / Cloud-Services als JSON |
| `SE_NODE_GRID_URL` | Hub-URL fuer Selenium-Nodes in verteilten Setups |
| `DEBUG` | `pw:browser*` fuer detailliertes Logging |

### Verwendung

```bash
# Hub-URL setzen, dann wie gewohnt testen
SELENIUM_REMOTE_URL=http://localhost:4444 npx playwright test
```

Mit zusaetzlichen Capabilities:
```bash
SELENIUM_REMOTE_URL=http://selenium-hub:4444 \
SELENIUM_REMOTE_CAPABILITIES='{"mygrid:options":{"os":"windows","username":"John","password":"secure"}}' \
npx playwright test
```

### Docker: Standalone-Modus

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

### Docker: Hub + Node-Modus

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

### Einschraenkungen

- Nur Google Chrome und Microsoft Edge werden unterstuetzt
- Feature als **experimentell** markiert
- Selenium 3: Best-Effort mit direktem Node-Zugriff
- Selenium Grid 4 empfohlen (CDP-Unterstuetzung)

---

## Vorteile nach der Migration

- Zero-Config TypeScript-Unterstuetzung
- Multi-Browser (Chrome, Firefox, Safari) ohne zusaetzliche Konfiguration
- Parallel-Ausfuehrung und Test-Isolation
- Integriertes Artifact-Collection (Traces, Videos, Screenshots)
- Playwright Inspector, Code-Generierung, Tracing

---

## Quellen

- https://playwright.dev/docs/puppeteer
- https://playwright.dev/docs/protractor
- https://playwright.dev/docs/selenium-grid
