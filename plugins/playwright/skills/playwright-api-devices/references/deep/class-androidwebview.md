# Playwright API: AndroidWebView

> **EXPERIMENTAL** — AndroidWebView is part of Playwright's experimental Android (ADB) support.

`AndroidWebView` represents a WebView instance running inside an Android application.
Once a WebView is obtained, you can call `page()` to get a full Playwright `Page` object
and use the entire Playwright page API (navigation, locators, assertions, screenshots, etc.)
against the embedded web content.

Instances are obtained via:
- `androidDevice.webView(selector, options?)` — wait for a specific WebView
- `androidDevice.webViews()` — list all currently open WebViews
- The `'webview'` event on `AndroidDevice`

```js
const wv = await device.webView({ pkg: 'com.example.app' });
const page = await wv.page();
await page.goto('https://example.com');
console.log(await page.title());
```

---

## Events

### androidWebView.on('close')

Emitted when the WebView is closed (the hosting activity was destroyed or the app exited).

**Event data:** none

**Signature:**
```js
androidWebView.on('close', () => { /* ... */ });
```

**Example:**
```js
wv.on('close', () => console.log('WebView closed'));
```

---

## Methods

### androidWebView.page()

Connects to the WebView and returns a Playwright `Page` object for full automation.
If the WebView is not yet ready, this method waits until it becomes available.

**Signature:**
```js
await androidWebView.page();
```

**Parameters:** none

**Returns:** `Promise<Page>`

The returned `Page` supports the full Playwright `Page` API:
navigation, locators, evaluation, screenshots, network interception, assertions, etc.

**Example:**
```js
const page = await wv.page();
await page.goto('https://playwright.dev');
await page.locator('text=Get started').click();
await page.screenshot({ path: 'webview.png' });
```

---

### androidWebView.pid()

Returns the OS process ID (PID) of the process hosting this WebView.

**Signature:**
```js
androidWebView.pid();
```

**Parameters:** none

**Returns:** `number`

**Example:**
```js
console.log('WebView PID:', wv.pid()); // e.g. 12345
```

---

### androidWebView.pkg()

Returns the Android package name of the application that owns this WebView.

**Signature:**
```js
androidWebView.pkg();
```

**Parameters:** none

**Returns:** `string`

**Example:**
```js
console.log('Package:', wv.pkg()); // e.g. "com.example.myapp"
```

---

## Full Usage Example

```js
const { android } = require('playwright');

(async () => {
  const [device] = await android.devices();

  // Wait until the app's WebView is open
  const wv = await device.webView({ pkg: 'com.example.myapp' }, { timeout: 10_000 });

  console.log(`WebView in ${wv.pkg()} (pid ${wv.pid()})`);

  // Get a full Playwright page handle
  const page = await wv.page();

  // Use the complete Playwright Page API
  console.log('URL:', page.url());
  await page.locator('#login-btn').click();
  await page.screenshot({ path: 'login.png' });

  await device.close();
})();
```

---

## Notes

- `AndroidWebView` has **no properties** (pid and pkg are methods, not properties).
- The `page()` method can be called multiple times — it returns the same `Page` instance.
- WebViews must have remote debugging enabled in the Android app
  (`WebView.setWebContentsDebuggingEnabled(true)`) for Playwright to connect to them.
- The `'close'` event fires when the WebView is destroyed; after that the `Page` obtained
  from `page()` will also be closed.

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 3 (`page`, `pid`, `pkg`) |
| Properties | 0 |
| Events | 1 (`close`) |

**Fazit:** `AndroidWebView` ist das Bindeglied zwischen nativer Android-Automatisierung und
der vollstaendigen Playwright-Page-API. Die zentrale Methode ist `page()`, die einen
Standard-`Page`-Handle zurueckgibt. `pid()` und `pkg()` sind nuetzlich zum Identifizieren
der richtigen WebView-Instanz bei Mehrfach-App-Szenarien.

---

Source: https://playwright.dev/docs/api/class-androidwebview
