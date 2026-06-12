# Playwright API: ElectronApplication

> **EXPERIMENTAL** — ElectronApplication is part of Playwright's experimental Electron support.
> Requires Electron v12.2.0+, v13.4.0+, or v14+.

`ElectronApplication` represents a running Electron app. It is returned by `electron.launch()`.
Through this object you can:
- Access and automate individual `BrowserWindow` instances as Playwright `Page` objects
- Evaluate code in the **Electron main process** (access to `app`, `ipcMain`, `BrowserWindow`, etc.)
- Intercept network via `context()`
- Listen for window lifecycle events

```js
const { _electron: electron } = require('playwright');

const app = await electron.launch({ args: ['main.js'] });
const window = await app.firstWindow();
console.log(await window.title());
await app.close();
```

---

## Events

### electronApplication.on('close')

Emitted when the Electron application process exits.

**Event data:** none

**Added:** v1.9

**Signature:**
```js
electronApplication.on('close', () => { /* ... */ });
```

**Example:**
```js
app.on('close', () => console.log('Electron app exited'));
```

---

### electronApplication.on('console')

Emitted when a `console` method (`log`, `warn`, `error`, `dir`, etc.) is called
in the Electron **main process**.

**Event data:** `ConsoleMessage`

The `ConsoleMessage` object exposes:
- `message.text()` — the text of the message
- `message.type()` — the console method name (`'log'`, `'warn'`, `'error'`, …)
- `message.args()` — array of `JSHandle` objects for each argument

**Added:** v1.42

**Signature:**
```js
electronApplication.on('console', (message) => { /* ... */ });
```

**Example:**
```js
app.on('console', (msg) => {
  console.log(`[main:${msg.type()}]`, msg.text());
});
```

---

### electronApplication.on('window')

Emitted each time a new `BrowserWindow` is created and fully loaded in Electron.

**Event data:** `Page` — a Playwright Page object for the new window

**Added:** v1.9

**Signature:**
```js
electronApplication.on('window', (page) => { /* ... */ });
```

**Example:**
```js
app.on('window', async (page) => {
  console.log('New window:', await page.title());
});
```

---

## Methods

### electronApplication.browserWindow(page)

Returns a `JSHandle` pointing to the Electron `BrowserWindow` object
that corresponds to the given Playwright `page`.

Use `evaluate()` on the returned handle to call Electron BrowserWindow methods
(e.g. `setSize`, `maximize`, `setAlwaysOnTop`, …).

**Signature:**
```js
await electronApplication.browserWindow(page);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `page` | Page | yes | — | Playwright Page object whose corresponding BrowserWindow is requested |

**Returns:** `Promise<JSHandle>`

**Added:** v1.11

**Example:**
```js
const window = await app.firstWindow();
const bwHandle = await app.browserWindow(window);

// Call Electron BrowserWindow methods via evaluate
await bwHandle.evaluate((bw) => bw.setSize(1200, 800));
await bwHandle.evaluate((bw) => bw.maximize());

const isMaximized = await bwHandle.evaluate((bw) => bw.isMaximized());
console.log('Maximized:', isMaximized);
```

---

### electronApplication.close()

Terminates the Electron application and frees all resources.
After calling this method the `ElectronApplication` instance must not be used.

**Signature:**
```js
await electronApplication.close();
```

**Parameters:** none

**Returns:** `Promise<void>`

**Added:** v1.9

**Example:**
```js
await app.close();
```

---

### electronApplication.context()

Returns the `BrowserContext` that contains all `Page` objects for this application.
Use this to configure context-wide route handling (e.g. `context.route()`),
or to access cookies, storage state, etc.

**Signature:**
```js
electronApplication.context();
```

**Parameters:** none

**Returns:** `BrowserContext`

**Added:** v1.9

**Example:**
```js
const context = app.context();

// Mock all API calls in all Electron windows
await context.route('**/api/**', (route) => {
  route.fulfill({ json: { status: 'ok' } });
});
```

---

### electronApplication.evaluate(pageFunction, arg?)

Runs a function in the Electron **main process** and returns its serialized result.
The function receives the Electron module as its first argument, giving access to
`app`, `ipcMain`, `BrowserWindow`, `shell`, `dialog`, and all other main-process APIs.

**Signature:**
```js
await electronApplication.evaluate(pageFunction, arg?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | function \| string | yes | — | Function (or stringified function) to run in the main process. Receives the Electron module as first parameter and `arg` as second |
| `arg` | EvaluationArgument | no | — | Serializable value passed as the second argument to `pageFunction` |

**Returns:** `Promise<Serializable>`

The return value must be JSON-serializable. For non-serializable return values use `evaluateHandle()`.

**Added:** v1.9

**Example:**
```js
// Get the app path
const appPath = await app.evaluate(async ({ app }) => app.getAppPath());
console.log('App path:', appPath);

// Interact with ipcMain
await app.evaluate(({ ipcMain }) => {
  ipcMain.emit('custom-event', {}, { payload: 'test' });
});

// Pass a custom argument
const result = await app.evaluate(
  ({ app }, userDataPath) => app.setPath('userData', userDataPath),
  '/tmp/test-user-data'
);
```

---

### electronApplication.evaluateHandle(pageFunction, arg?)

Runs a function in the Electron **main process** and returns a `JSHandle` pointing
to the result. Unlike `evaluate()`, the return value does not need to be serializable.
Use this to hold references to Electron objects (e.g. a specific `BrowserWindow` instance).

**Signature:**
```js
await electronApplication.evaluateHandle(pageFunction, arg?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `pageFunction` | function \| string | yes | — | Function to run in the main process. Receives the Electron module as first parameter and `arg` as second |
| `arg` | EvaluationArgument | no | — | Serializable value passed as the second argument |

**Returns:** `Promise<JSHandle>`

**Added:** v1.9

**Example:**
```js
// Get a handle to the first BrowserWindow
const bwHandle = await app.evaluateHandle(({ BrowserWindow }) => {
  return BrowserWindow.getAllWindows()[0];
});

// Now call methods on the handle
const size = await bwHandle.evaluate((bw) => bw.getSize());
console.log('Window size:', size);
```

---

### electronApplication.firstWindow(options?)

Waits for and returns the first application window (`Page`) to open.
If a window is already open at the time of the call it is returned immediately.

**Signature:**
```js
await electronApplication.firstWindow(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | |
| `options.timeout` | number | no | `30000` | Maximum time (ms) to wait for the first window; `0` disables the timeout |

**Returns:** `Promise<Page>`

**Added:** v1.9

**Example:**
```js
const window = await app.firstWindow({ timeout: 10_000 });
console.log('Title:', await window.title());
await window.screenshot({ path: 'first-window.png' });
```

---

### electronApplication.process()

Returns the Node.js `ChildProcess` object for the Electron main process.
Useful for sending signals, monitoring stdout/stderr, or reading the PID.

**Signature:**
```js
electronApplication.process();
```

**Parameters:** none

**Returns:** `ChildProcess`

**Added:** v1.21

**Example:**
```js
const proc = app.process();
console.log('Electron PID:', proc.pid);
proc.stdout?.on('data', (d) => console.log('[stdout]', d.toString()));
proc.stderr?.on('data', (d) => console.error('[stderr]', d.toString()));
```

---

### electronApplication.waitForEvent(event, optionsOrPredicate?)

Waits for a named event to be emitted and returns its data.
Optionally filters events using a predicate function.

**Signature:**
```js
await electronApplication.waitForEvent(event, optionsOrPredicate?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `event` | string | yes | — | Event name (e.g. `'window'`, `'close'`, `'console'`) |
| `optionsOrPredicate` | function \| Object | no | — | Predicate function or options object |
| `optionsOrPredicate` (as function) | (data: any) => boolean | no | — | Called with event data; event is accepted when this returns truthy |
| `optionsOrPredicate.predicate` | function | no | — | Same as above when passing an object |
| `optionsOrPredicate.timeout` | number | no | `30000` | Maximum wait time (ms); `0` disables timeout |

**Returns:** `Promise<Object>`

**Added:** v1.9

**Example:**
```js
// Wait for a specific window to open
const settingsPage = await app.waitForEvent('window', {
  predicate: async (page) => (await page.title()) === 'Settings',
  timeout: 15_000,
});

// Wait for any console message containing 'ready'
const msg = await app.waitForEvent('console', {
  predicate: (m) => m.text().includes('ready'),
});
```

---

### electronApplication.windows()

Returns all currently open application windows as Playwright `Page` objects.

**Signature:**
```js
electronApplication.windows();
```

**Parameters:** none

**Returns:** `Array<Page>`

**Added:** v1.9

**Example:**
```js
const pages = app.windows();
console.log(`${pages.length} window(s) open`);
for (const page of pages) {
  console.log(' -', await page.title());
}
```

---

## Full Integration Example

```js
const { _electron: electron } = require('playwright');
const { test, expect } = require('@playwright/test');

test('Electron app smoke test', async () => {
  const app = await electron.launch({
    args: ['dist/main.js'],
    env: { ...process.env, NODE_ENV: 'test' },
  });

  // Capture main-process console output
  app.on('console', (msg) => console.log('[electron]', msg.text()));

  // Get the main window
  const window = await app.firstWindow();
  await expect(window).toHaveTitle('My App');

  // Access Electron main-process APIs
  const version = await app.evaluate(({ app }) => app.getVersion());
  expect(version).toMatch(/^\d+\.\d+\.\d+$/);

  // Interact via BrowserWindow handle
  const bw = await app.browserWindow(window);
  await bw.evaluate((win) => win.setSize(1280, 800));

  // Route all network requests
  const ctx = app.context();
  await ctx.route('**/api/status', (route) =>
    route.fulfill({ json: { online: true } })
  );

  await window.click('button#refresh');
  await expect(window.locator('#status')).toHaveText('online');

  // Check all open windows
  expect(app.windows().length).toBe(1);

  await app.close();
});
```

---

## Notes

- `ElectronApplication` has **no properties** — `context()`, `process()`, and `windows()` are methods.
- `evaluate()` / `evaluateHandle()` run in the **main process**, not in a renderer window.
  To run code in a renderer, use `page.evaluate()` on the `Page` returned by `firstWindow()`.
- `context()` returns a single shared `BrowserContext`; changes to routing or permissions
  apply to all windows.
- The `'window'` event fires for every new `BrowserWindow` that loads; use `waitForEvent('window')`
  together with a title/URL predicate to wait for a specific window.

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 8 (`browserWindow`, `close`, `context`, `evaluate`, `evaluateHandle`, `firstWindow`, `process`, `waitForEvent`, `windows`) |
| Properties | 0 |
| Events | 3 (`close`, `console`, `window`) |

**Fazit:** `ElectronApplication` ist das zentrale Objekt fuer Electron-Testing. Die Methoden
`evaluate()` / `evaluateHandle()` geben Zugriff auf alle Electron-Main-Process-APIs.
`browserWindow(page)` verbindet Playwright-Pages mit ihren nativen BrowserWindow-Objekten.
`context()` ermoeg licht kontextweites Routing ueber alle Fenster hinweg.

---

Source: https://playwright.dev/docs/api/class-electronapplication
