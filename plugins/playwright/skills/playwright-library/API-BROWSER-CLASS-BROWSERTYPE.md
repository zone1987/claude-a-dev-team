# class-browsertype

`BrowserType` represents a browser family (`chromium`, `firefox`, `webkit`). This object is used to launch browser instances or connect to existing ones.

Methods: 6 | Properties: 0 | Events: 0

---

## Methods

### browserType.connect(endpoint[, options])

```ts
await browserType.connect(endpoint[, options]): Promise<Browser>
```

Connects Playwright to an existing browser instance that was started via `browserType.launchServer()`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `endpoint` | string | Yes | — | WebSocket endpoint from `browserServer.wsEndpoint()` |
| `options.exposeNetwork` | string | No | — | Network exposure (e.g. `"<loopback>"`, hostnames, IP ranges) |
| `options.headers` | Object<string,string> | No | — | Additional HTTP headers for the WebSocket connection |
| `options.slowMo` | number | No | 0 | Delay for each operation in ms |
| `options.timeout` | number | No | 30000 | Maximum wait time for establishing the connection in ms |

**Returns:** `Promise<Browser>`

**Note:** Client and server must use compatible Playwright versions (same minor version, e.g. 1.2.x).

```js
const browser = await chromium.connect('ws://localhost:9222/playwright');
const page = await browser.newPage();
```

---

### browserType.connectOverCDP(endpointURL[, options])

```ts
await browserType.connectOverCDP(endpointURL[, options]): Promise<Browser>
```

Connects to a running browser via the Chrome DevTools Protocol (CDP). Lower feature coverage than the native Playwright protocol. **Chromium-based browsers only.**

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `endpointURL` | string | Yes | — | CDP WebSocket or HTTP URL (e.g. `http://localhost:9222/`) |
| `options.headers` | Object<string,string> | No | — | Additional HTTP headers |
| `options.isLocal` | boolean | No | false | Enable optimizations for local connections |
| `options.noDefaults` | boolean | No | false | Prevent Playwright's own overrides on existing contexts |
| `options.slowMo` | number | No | 0 | Delay in ms |
| `options.timeout` | number | No | 30000 | Maximum wait time in ms |

**Returns:** `Promise<Browser>`

```js
// Start Chrome with --remote-debugging-port=9222, then:
const browser = await chromium.connectOverCDP('http://localhost:9222');
const [context] = browser.contexts();
```

---

### browserType.executablePath()

```ts
browserType.executablePath(): string
```

Returns the file path to the bundled browser executable.

**Returns:** `string`

```js
console.log(chromium.executablePath());
// e.g. "/home/user/.cache/ms-playwright/chromium-1084/chrome-linux/chrome"
```

---

### browserType.launch([options])

```ts
await browserType.launch([options]): Promise<Browser>
```

Launches a new browser instance.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.args` | Array<string> | No | — | Additional command-line arguments for the browser |
| `options.artifactsDir` | string | No | — | Directory for traces, videos, downloads |
| `options.channel` | string | No | — | Browser channel: `"chromium"`, `"chrome"`, `"chrome-beta"`, `"chrome-dev"`, `"chrome-canary"`, `"msedge"`, `"msedge-beta"`, `"msedge-dev"`, `"msedge-canary"`, `"firefox"`, `"webkit"` |
| `options.chromiumSandbox` | boolean | No | false | Enable the Chromium sandbox |
| `options.downloadsPath` | string | No | tmpdir | Directory for accepted downloads |
| `options.env` | Object<string,string\|number\|boolean> | No | — | Environment variables for the browser process |
| `options.executablePath` | string | No | — | Path to a custom browser executable |
| `options.firefoxUserPrefs` | Object | No | — | Firefox preferences (user.js) |
| `options.handleSIGHUP` | boolean | No | true | Intercept the SIGHUP signal and close the browser |
| `options.handleSIGINT` | boolean | No | true | Intercept SIGINT (Ctrl+C) and close the browser |
| `options.handleSIGTERM` | boolean | No | true | Intercept SIGTERM and close the browser |
| `options.headless` | boolean | No | true | Launch in headless mode |
| `options.ignoreDefaultArgs` | boolean \| Array<string> | No | false | Ignore default arguments (all or a list) |
| `options.logger` | Logger | No | — | Logging sink (deprecated) |
| `options.proxy` | Object | No | — | Proxy configuration: `{ server, bypass?, username?, password? }` |
| `options.slowMo` | number | No | 0 | Delay every operation by X ms (debugging) |
| `options.timeout` | number | No | 30000 | Max. startup time in ms; `0` = no timeout |
| `options.tracesDir` | string | No | — | Directory for trace files |

**Returns:** `Promise<Browser>`

```js
const browser = await chromium.launch({
  headless: false,
  slowMo: 50,
  args: ['--no-sandbox'],
});
```

---

### browserType.launchPersistentContext(userDataDir[, options])

```ts
await browserType.launchPersistentContext(userDataDir[, options]): Promise<BrowserContext>
```

Launches a browser with a persistent user profile and returns a single managed `BrowserContext`. Closing the context automatically closes the browser. Required for Chrome extensions and real user profiles.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `userDataDir` | string | Yes | — | Path to the user profile directory (created if it does not exist) |
| `options` | Object | No | — | Combination of `launch()` options and context options |
| `options.acceptDownloads` | boolean | No | true | |
| `options.baseURL` | string | No | — | |
| `options.bypassCSP` | boolean | No | false | |
| `options.clientCertificates` | Array<Object> | No | — | TLS client certificates: `{ origin, certPath?, cert?, keyPath?, key?, pfxPath?, pfx?, passphrase? }` |
| `options.colorScheme` | `"light"` \| `"dark"` \| `"no-preference"` \| null | No | — | |
| `options.contrast` | `"no-preference"` \| `"more"` \| null | No | — | |
| `options.deviceScaleFactor` | number | No | 1 | |
| `options.extraHTTPHeaders` | Object<string,string> | No | — | |
| `options.forcedColors` | `"active"` \| `"none"` \| null | No | — | |
| `options.geolocation` | Object | No | — | `{ latitude, longitude, accuracy? }` |
| `options.hasTouch` | boolean | No | false | |
| `options.httpCredentials` | Object | No | — | `{ username, password, origin?, send? }` |
| `options.ignoreHTTPSErrors` | boolean | No | false | |
| `options.isMobile` | boolean | No | false | |
| `options.javaScriptEnabled` | boolean | No | true | |
| `options.locale` | string | No | — | e.g. `"en-GB"`, `"de-DE"` |
| `options.offline` | boolean | No | false | |
| `options.permissions` | Array<string> | No | — | |
| `options.recordHar` | Object | No | — | `{ path, omitContent?, content?, mode?, urlFilter? }` |
| `options.recordVideo` | Object | No | — | `{ dir, size?, showActions? }` |
| `options.reducedMotion` | `"reduce"` \| `"no-preference"` \| null | No | — | |
| `options.screen` | Object | No | — | `{ width, height }` in pixels |
| `options.serviceWorkers` | `"allow"` \| `"block"` | No | `"allow"` | |
| `options.strictSelectors` | boolean | No | false | |
| `options.timezoneId` | string | No | — | ICU timezone ID |
| `options.userAgent` | string | No | — | |
| `options.viewport` | Object \| null | No | `{width:1280,height:720}` | `null` disables viewport emulation |
| _all `launch()` options_ | | No | | `args`, `channel`, `executablePath`, `headless`, etc. |

**Returns:** `Promise<BrowserContext>`

```js
const context = await chromium.launchPersistentContext('/tmp/user-data', {
  headless: false,
  args: ['--disable-extensions-except=/path/to/ext', '--load-extension=/path/to/ext'],
});
const page = await context.newPage();
```

---

### browserType.launchServer([options])

```ts
await browserType.launchServer([options]): Promise<BrowserServer>
```

Launches a browser server that Playwright clients can connect to via `browserType.connect()`.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | All `launch()` options plus: |
| `options.host` | string | No | `"localhost"` | WebSocket host |
| `options.port` | number | No | 0 | WebSocket port (0 = any free port) |
| `options.wsPath` | string | No | — | Server path (security-relevant: use an unguessable token) |

**Returns:** `Promise<BrowserServer>`

```js
const server = await chromium.launchServer({ port: 9222, wsPath: 'secret-token' });
console.log(server.wsEndpoint()); // ws://localhost:9222/secret-token
```

---

### browserType.name()

```ts
browserType.name(): string
```

Returns the name of the browser.

**Returns:** `string` — `"chromium"`, `"webkit"` or `"firefox"`

```js
console.log(chromium.name()); // "chromium"
```

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 6 |
| Properties | 0 |
| Events | 0 |

**Conclusion:** `BrowserType` is the factory entry point for all browser instances. `launch()` and `launchPersistentContext()` are the most frequently used methods in test code. `launchServer()` + `connect()` enable remote browser setups for distributed test infrastructures.

---

Source: https://playwright.dev/docs/api/class-browsertype
