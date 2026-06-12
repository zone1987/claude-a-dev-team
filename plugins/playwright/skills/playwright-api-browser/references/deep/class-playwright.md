# class-playwright

Das `Playwright`-Objekt ist der Root-Einstiegspunkt der Playwright-API. Es wird durch `require('playwright')` oder den Test-Runner bereitgestellt und enthaelt die Browser-Typen sowie globale Hilfsobjekte.

Methoden: 0 | Properties: 6 | Events: 0

---

## Properties

### playwright.chromium

**Type:** `BrowserType`

Objekt zum Starten oder Verbinden mit Chromium-Browser-Instanzen (einschliesslich Chrome und Edge ueber `channel`-Option).

```js
const { chromium } = require('playwright');
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();
```

---

### playwright.firefox

**Type:** `BrowserType`

Objekt zum Starten oder Verbinden mit Firefox-Browser-Instanzen.

```js
const { firefox } = require('playwright');
const browser = await firefox.launch();
```

---

### playwright.webkit

**Type:** `BrowserType`

Objekt zum Starten oder Verbinden mit WebKit-Browser-Instanzen (Safari-Engine).

```js
const { webkit } = require('playwright');
const browser = await webkit.launch();
```

---

### playwright.devices

**Type:** `Object`

Woerterbuch mit vordefinierten Geraete-Deskriptoren fuer mobile Emulation. Kann mit `browser.newContext()` oder `browser.newPage()` verwendet werden (Spread-Operator).

**Verfuegbare Geraete:** Alle in den [Playwright-Devicedescriptors](https://playwright.dev/docs/emulation#devices) aufgefuehrten Geraete, z.B. `"iPhone 15"`, `"Pixel 7"`, `"Galaxy S9+"`, etc.

Jeder Eintrag enthaelt: `userAgent`, `viewport`, `deviceScaleFactor`, `isMobile`, `hasTouch`, `defaultBrowserType`.

```js
const { webkit, devices } = require('playwright');
const iPhone = devices['iPhone 15'];

const browser = await webkit.launch();
const context = await browser.newContext({
  ...iPhone,
  locale: 'de-DE',
});
const page = await context.newPage();
await page.goto('https://example.com');
```

---

### playwright.request

**Type:** `APIRequest`

Singleton-Instanz der `APIRequest`-Klasse fuer das Erstellen unabhaengiger `APIRequestContext`-Instanzen (ohne Browser-Context).

```js
const { request } = require('playwright');
const context = await request.newContext({
  baseURL: 'https://api.example.com',
  extraHTTPHeaders: { 'Authorization': 'Bearer token123' },
});
const response = await context.get('/users');
console.log(await response.json());
await context.dispose();
```

---

### playwright.selectors

**Type:** `Selectors`

Ermoeglicht die Installation eigener Selector-Engines (z.B. Datenbindungs-Selektoren fuer spezifische Frameworks).

```js
const { selectors, chromium } = require('playwright');

// Selector-Engine registrieren
await selectors.register('tag', {
  query(root, selector) {
    return root.querySelector(selector);
  },
  queryAll(root, selector) {
    return Array.from(root.querySelectorAll(selector));
  },
});

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
const element = await page.locator('tag=h1');
```

---

### playwright.errors

**Type:** `Object`

Enthaelt Fehlerklassen, die von Playwright-Methoden geworfen werden.

**Sub-properties:**

| Property | Type | Description |
|----------|------|-------------|
| `TimeoutError` | Function | Wird geworfen wenn ein Timeout ablaeuft |

```js
const { errors } = require('playwright');

try {
  await page.locator('.nonexistent').waitFor({ timeout: 1000 });
} catch (e) {
  if (e instanceof errors.TimeoutError) {
    console.log('Element nicht gefunden innerhalb des Timeouts');
  }
}
```

---

## Import-Patterns

```js
// CommonJS
const { chromium, firefox, webkit, devices, request, selectors } = require('playwright');

// ES Modules
import { chromium, firefox, webkit, devices } from 'playwright';

// Im Playwright Test-Framework (automatisch injiziert)
import { test, expect } from '@playwright/test';
// browserType via test.use({ browserName: 'chromium' })
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 0 |
| Properties | 6 |
| Events | 0 |

**Fazit:** Das `Playwright`-Objekt ist ein reiner Namespace ohne eigene Methoden. Die drei BrowserType-Properties (`chromium`, `firefox`, `webkit`) sind der Startpunkt jeder Browser-Interaktion. `devices` und `request` sind globale Hilfsobjekte fuer Geraete-Emulation bzw. standalone API-Tests.

---

Source: https://playwright.dev/docs/api/class-playwright
