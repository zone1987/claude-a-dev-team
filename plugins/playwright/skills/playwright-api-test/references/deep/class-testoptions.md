# class-testoptions — Playwright Test Use-Options Reference

`TestOptions` is the type of the `use` object in `TestConfig`, `TestProject`, or `test.use()`.
It combines Playwright browser/context options with test-runner-specific settings.

```ts
// playwright.config.ts
export default defineConfig({
  use: { /* TestOptions */ },
  projects: [{ use: { /* TestOptions */ } }],
});

// per-file or per-describe
test.use({ locale: 'de-DE' });
```

---

## All Properties

### `acceptDownloads`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `true` | Automatically accept file downloads |

---

### `actionTimeout`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `0` | Default timeout (ms) for individual actions like `click`, `fill`; 0 = no timeout |

---

### `baseURL`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Base URL prepended to relative paths in `page.goto()`, `page.route()`, etc. |

```ts
baseURL: 'http://localhost:3000'
// then: await page.goto('/login') navigates to http://localhost:3000/login
```

---

### `browserName`

| Type | Default | Description |
|------|---------|-------------|
| `"chromium" \| "firefox" \| "webkit"` | `"chromium"` | Browser engine for this test or project |

---

### `bypassCSP`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Bypass Content-Security-Policy headers |

---

### `channel`

| Type | Default | Description |
|------|---------|-------------|
| `string` | — | Browser distribution channel: `"chrome"`, `"chrome-beta"`, `"msedge"`, `"msedge-dev"`, etc. |

```ts
channel: 'chrome'
```

---

### `clientCertificates`

| Type | Default | Description |
|------|---------|-------------|
| `Array<Object>` | — | TLS client certificates sent to matching origins |

Certificate object fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `origin` | `string` | yes | Origin URL (scheme + host + port) |
| `certPath` | `string` | no | Path to PEM certificate file |
| `keyPath` | `string` | no | Path to PEM private key file |
| `pfxPath` | `string` | no | Path to PFX/PKCS12 bundle |
| `passphrase` | `string` | no | Passphrase for encrypted private key or PFX |

---

### `colorScheme`

| Type | Default | Description |
|------|---------|-------------|
| `null \| "light" \| "dark" \| "no-preference"` | `"light"` | Emulates `prefers-color-scheme` CSS media feature |

---

### `connectOptions`

| Type | Default | Description |
|------|---------|-------------|
| `Object \| void` | — | Connect to a remote browser via WebSocket |

Sub-fields:

| Field | Type | Description |
|-------|------|-------------|
| `wsEndpoint` | `string` | WebSocket URL of the remote browser |
| `headers` | `Object<string,string>` | Additional HTTP headers for the WS handshake |
| `timeout` | `number` | Connection timeout in ms |
| `exposeNetwork` | `string` | Expose host network to remote browser (e.g. `'*'`) |
| `slowMo` | `number` | Slow down all operations by N ms |

---

### `contextOptions`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Raw `browser.newContext()` options; merged with other `use` settings |

Use for options not directly exposed by `TestOptions`.

---

### `deviceScaleFactor`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `1` | Device pixel ratio; `2` simulates a Retina display |

---

### `extraHTTPHeaders`

| Type | Default | Description |
|------|---------|-------------|
| `Object<string, string>` | — | Additional HTTP headers sent with every request |

```ts
extraHTTPHeaders: { 'X-API-Key': process.env.API_KEY! }
```

---

### `geolocation`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Emulate geographic location |

Sub-fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `latitude` | `number` | yes | Latitude in degrees (−90 to 90) |
| `longitude` | `number` | yes | Longitude in degrees (−180 to 180) |
| `accuracy` | `number` | no | Accuracy in metres |

---

### `hasTouch`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Viewport supports touch events |

---

### `headless`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `true` | Run browser without a GUI |

---

### `httpCredentials`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | HTTP Basic / Digest authentication credentials |

Sub-fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `username` | `string` | yes | Auth username |
| `password` | `string` | yes | Auth password |
| `origin` | `string` | no | Restrict credentials to this origin |
| `send` | `"unauthorized" \| "always"` | no | When to send credentials (default: `"unauthorized"`) |

---

### `ignoreHTTPSErrors`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Ignore TLS certificate errors |

---

### `isMobile`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Emulate mobile device (touch, viewport, meta viewport) |

---

### `javaScriptEnabled`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `true` | Enable JavaScript execution in the page |

---

### `launchOptions`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Raw `browserType.launch()` options; merged with other `use` settings |

Use for options not directly exposed by `TestOptions` (e.g. `executablePath`, `args`).

---

### `locale`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `"en-US"` | Browser locale affecting `navigator.language`, date/number formatting |

```ts
locale: 'de-DE'
```

---

### `navigationTimeout`

| Type | Default | Description |
|------|---------|-------------|
| `number` | `0` | Timeout (ms) for navigation operations (`goto`, `waitForNavigation`); 0 = no timeout |

---

### `offline`

| Type | Default | Description |
|------|---------|-------------|
| `boolean` | `false` | Emulate network being offline |

---

### `permissions`

| Type | Default | Description |
|------|---------|-------------|
| `Array<string>` | — | Browser permissions granted to all pages in the context |

Common values: `'geolocation'`, `'notifications'`, `'microphone'`, `'camera'`, `'clipboard-read'`

```ts
permissions: ['geolocation']
```

---

### `proxy`

| Type | Default | Description |
|------|---------|-------------|
| `Object` | — | Network proxy configuration |

Sub-fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `server` | `string` | yes | Proxy URL (e.g. `'http://myproxy.com:3128'`) |
| `bypass` | `string` | no | Comma-separated hosts to bypass |
| `username` | `string` | no | Proxy auth username |
| `password` | `string` | no | Proxy auth password |

---

### `screenshot`

| Type | Default | Description |
|------|---------|-------------|
| `"off" \| "on" \| "only-on-failure" \| "on-first-failure" \| Object` | `"off"` | Automatic screenshot capture mode |

When using an object:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | `"off" \| "on" \| "only-on-failure" \| "on-first-failure"` | `"off"` | Capture mode |
| `fullPage` | `boolean` | `false` | Capture full scrollable page |
| `omitBackground` | `boolean` | `false` | Make background transparent (PNG only) |

---

### `serviceWorkers`

| Type | Default | Description |
|------|---------|-------------|
| `"allow" \| "block"` | `"allow"` | Whether service worker registration is permitted |

---

### `storageState`

| Type | Default | Description |
|------|---------|-------------|
| `string \| Object` | — | Pre-populate cookies and localStorage (e.g. saved authentication state) |

```ts
storageState: 'playwright/.auth/user.json'
```

---

### `testIdAttribute`

| Type | Default | Description |
|------|---------|-------------|
| `string` | `"data-testid"` | HTML attribute used by `page.getByTestId()` |

```ts
testIdAttribute: 'data-pw'
```

---

### `timezoneId`

| Type | Default | Description |
|------|---------|-------------|
| `string` | system timezone | IANA timezone identifier (e.g. `'Europe/Berlin'`) |

---

### `trace`

| Type | Default | Description |
|------|---------|-------------|
| `"off" \| "on" \| "retain-on-failure" \| "on-first-retry" \| "retain-on-first-failure" \| "retain-on-failure-and-retries" \| Object` | `"off"` | Trace recording mode |

When using an object:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | one of the string values above | `"off"` | When to record |
| `attachments` | `boolean` | `true` | Include attachments in trace |
| `screenshots` | `boolean` | `true` | Include screenshots |
| `snapshots` | `boolean` | `true` | Include DOM snapshots |
| `sources` | `boolean` | `true` | Include source files |

```ts
trace: process.env.CI ? 'on-first-retry' : 'retain-on-failure'
```

---

### `userAgent`

| Type | Default | Description |
|------|---------|-------------|
| `string` | browser default | Custom `User-Agent` string |

---

### `video`

| Type | Default | Description |
|------|---------|-------------|
| `"off" \| "on" \| "retain-on-failure" \| "on-first-retry" \| Object` | `"off"` | Video recording mode |

When using an object:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | one of the string values | `"off"` | When to record |
| `size` | `{ width: number, height: number }` | viewport size | Recording resolution |
| `dir` | `string` | `outputDir` | Output directory for video files |

---

### `viewport`

| Type | Default | Description |
|------|---------|-------------|
| `null \| { width: number, height: number }` | `{ width: 1280, height: 720 }` | Browser viewport size; `null` disables fixed viewport |

```ts
viewport: { width: 1920, height: 1080 }
```

---

## Manifest

| Category | Count |
|----------|-------|
| Direct option properties | 35 |
| Properties with sub-fields | 10 |

**Fazit:** `TestOptions` steuert den gesamten Browser- und Kontext-Lebenszyklus pro Test.
Die haeufigsten Einstellungen sind `baseURL`, `trace`, `screenshot`, `storageState` und
`viewport`. `launchOptions` und `contextOptions` bieten Escape-Hatch-Zugang zu allen
nativen Playwright-Optionen.

---

Source: https://playwright.dev/docs/api/class-testoptions
