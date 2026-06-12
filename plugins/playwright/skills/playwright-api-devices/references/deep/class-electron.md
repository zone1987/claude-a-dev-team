# Playwright API: Electron

> **EXPERIMENTAL** — The Electron class is part of Playwright's experimental Electron application testing support.
> Requires Electron v12.2.0+, v13.4.0+, or v14+.

The `Electron` class is the entry point for testing Electron desktop applications.
It is exposed as `playwright.electron` (or `require('playwright')._electron` in legacy imports).

```js
const { _electron: electron } = require('playwright');
const app = await electron.launch({ args: ['main.js'] });
```

---

## Methods

### electron.launch(options?)

Launches an Electron application and returns an `ElectronApplication` instance.

**Signature:**
```js
await electron.launch(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | Launch options |
| `options.acceptDownloads` | boolean | no | `true` | Automatically download all attachments |
| `options.args` | Array\<string\> | no | — | Additional arguments passed to the Electron process. Typically you pass the main script path here (e.g. `['main.js']`) |
| `options.artifactsDir` | string | no | — | Directory where artifacts (traces, videos, HAR, downloads) are saved |
| `options.bypassCSP` | boolean | no | `false` | Bypass Content-Security-Policy in all pages |
| `options.chromiumSandbox` | boolean | no | `false` | Enable Chromium sandboxing |
| `options.colorScheme` | `null` \| `"light"` \| `"dark"` \| `"no-preference"` | no | `'light'` | Emulate `prefers-color-scheme` media feature |
| `options.cwd` | string | no | — | Working directory for the Electron process |
| `options.env` | Object\<string, string\> | no | `process.env` | Environment variables visible to Electron; merged with or replaces `process.env` |
| `options.executablePath` | string | no | — | Path to the Electron binary to launch. Required if the Electron executable is not at the default location |
| `options.extraHTTPHeaders` | Object\<string, string\> | no | — | Additional HTTP headers sent with every network request |
| `options.geolocation` | Object | no | — | Geolocation override |
| `options.geolocation.latitude` | number | yes (if set) | — | Latitude: −90 to 90 |
| `options.geolocation.longitude` | number | yes (if set) | — | Longitude: −180 to 180 |
| `options.geolocation.accuracy` | number | no | `0` | Non-negative accuracy in meters |
| `options.httpCredentials` | Object | no | — | Credentials for HTTP authentication |
| `options.httpCredentials.username` | string | yes (if set) | — | Username |
| `options.httpCredentials.password` | string | yes (if set) | — | Password |
| `options.httpCredentials.origin` | string | no | — | Restrict to this origin only |
| `options.httpCredentials.send` | `"unauthorized"` \| `"always"` | no | `'unauthorized'` | When to send credentials |
| `options.ignoreHTTPSErrors` | boolean | no | `false` | Ignore HTTPS errors when sending network requests |
| `options.locale` | string | no | — | BCP 47 user locale, e.g. `'de-DE'` |
| `options.offline` | boolean | no | `false` | Emulate network offline |
| `options.recordHar` | Object | no | — | HAR recording |
| `options.recordHar.path` | string | yes (if set) | — | Path to write the HAR file |
| `options.recordHar.omitContent` | boolean | no | `false` | Omit request bodies |
| `options.recordHar.content` | `"omit"` \| `"embed"` \| `"attach"` | no | — | How to handle request content |
| `options.recordHar.mode` | `"full"` \| `"minimal"` | no | `'full'` | Recording detail |
| `options.recordHar.urlFilter` | string \| RegExp | no | — | Filter requests to record |
| `options.recordVideo` | Object | no | — | Video recording |
| `options.recordVideo.dir` | string | no | — | Directory for video files |
| `options.recordVideo.size` | Object | no | — | Frame dimensions |
| `options.recordVideo.size.width` | number | yes (if set) | — | Video width in pixels |
| `options.recordVideo.size.height` | number | yes (if set) | — | Video height in pixels |
| `options.recordVideo.showActions` | Object | no | — | Overlay action annotations |
| `options.recordVideo.showActions.duration` | number | no | `500` | Annotation display duration (ms) |
| `options.recordVideo.showActions.position` | `"top-left"` \| `"top"` \| `"top-right"` \| `"bottom-left"` \| `"bottom"` \| `"bottom-right"` | no | `'top-right'` | Position of the annotation overlay |
| `options.recordVideo.showActions.fontSize` | number | no | `24` | Font size in pixels |
| `options.timeout` | number | no | `30000` | Maximum time (ms) to wait for the application to start and be ready |
| `options.timezoneId` | string | no | — | ICU timezone ID, e.g. `'Europe/Berlin'` |
| `options.tracesDir` | string | no | — | Directory to store trace files |

**Returns:** `Promise<ElectronApplication>`

**Example:**
```js
const { _electron: electron } = require('playwright');

(async () => {
  const app = await electron.launch({
    args: ['main.js'],
    cwd: '/path/to/electron/app',
    env: { ...process.env, NODE_ENV: 'test' },
    timeout: 60_000,
  });

  // Get the main window
  const window = await app.firstWindow();
  console.log('Title:', await window.title());

  // Take a screenshot
  await window.screenshot({ path: 'app-screenshot.png' });

  // Interact with the window
  await window.click('text=File');

  await app.close();
})();
```

---

## Notes

- `Electron` has **no properties** and **no events** of its own.
- The class is obtained via `playwright.electron` (stable import name) or
  `require('playwright')._electron` (legacy, still works).
- Playwright integrates with Electron by injecting a helper into the main process.
  The `executablePath` option must point to the Electron binary, not the app's package directory.
- Supported Electron versions: 12.2.0+, 13.4.0+, 14+. Older versions may work but are not tested.
- Unlike browser testing, Electron testing allows evaluating code in the **main process** via
  `ElectronApplication.evaluate()`, giving access to `app`, `ipcMain`, `BrowserWindow`, etc.

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 1 (`launch`) |
| Properties | 0 |
| Events | 0 |

**Fazit:** `Electron` ist das minimale Factory-Objekt — seine einzige Aufgabe ist der Launch
der Electron-Applikation via `launch()`. Alle weiteren Interaktionen finden ueber das zurueckgegebene
`ElectronApplication`-Objekt statt. Die zahlreichen Launch-Optionen decken Netzwerk-, Video-,
HAR- und Tracing-Konfiguration ab.

---

Source: https://playwright.dev/docs/api/class-electron
