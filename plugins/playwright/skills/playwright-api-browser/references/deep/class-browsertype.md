# class-browsertype

`BrowserType` repraesentiert eine Browserfamilie (`chromium`, `firefox`, `webkit`). Ueber dieses Objekt werden Browser-Instanzen gestartet oder mit bestehenden Instanzen verbunden.

Methoden: 6 | Properties: 0 | Events: 0

---

## Methods

### browserType.connect(endpoint[, options])

```ts
await browserType.connect(endpoint[, options]): Promise<Browser>
```

Verbindet Playwright mit einer bestehenden Browser-Instanz, die via `browserType.launchServer()` gestartet wurde.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `endpoint` | string | Yes | — | WebSocket-Endpoint aus `browserServer.wsEndpoint()` |
| `options.exposeNetwork` | string | No | — | Netzwerk-Exposition (z.B. `"<loopback>"`, Hostnamen, IP-Bereiche) |
| `options.headers` | Object<string,string> | No | — | Zusaetzliche HTTP-Header fuer die WebSocket-Verbindung |
| `options.slowMo` | number | No | 0 | Verzoegerung fuer jede Operation in ms |
| `options.timeout` | number | No | 30000 | Maximale Wartezeit fuer Verbindungsaufbau in ms |

**Returns:** `Promise<Browser>`

**Hinweis:** Client und Server muessen kompatible Playwright-Versionen verwenden (gleiche Minor-Version, z.B. 1.2.x).

```js
const browser = await chromium.connect('ws://localhost:9222/playwright');
const page = await browser.newPage();
```

---

### browserType.connectOverCDP(endpointURL[, options])

```ts
await browserType.connectOverCDP(endpointURL[, options]): Promise<Browser>
```

Verbindet via Chrome DevTools Protocol (CDP) mit einem laufenden Browser. Niedriger Funktionsumfang als das native Playwright-Protokoll. **Nur Chromium-basierte Browser.**

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `endpointURL` | string | Yes | — | CDP-WebSocket- oder HTTP-URL (z.B. `http://localhost:9222/`) |
| `options.headers` | Object<string,string> | No | — | Zusaetzliche HTTP-Header |
| `options.isLocal` | boolean | No | false | Optimierungen fuer lokale Verbindungen aktivieren |
| `options.noDefaults` | boolean | No | false | Playwright-eigene Overrides auf bestehenden Contexten verhindern |
| `options.slowMo` | number | No | 0 | Verzoegerung in ms |
| `options.timeout` | number | No | 30000 | Maximale Wartezeit in ms |

**Returns:** `Promise<Browser>`

```js
// Chrome mit --remote-debugging-port=9222 starten, dann:
const browser = await chromium.connectOverCDP('http://localhost:9222');
const [context] = browser.contexts();
```

---

### browserType.executablePath()

```ts
browserType.executablePath(): string
```

Gibt den Dateipfad zum mitgelieferten Browser-Executable zurueck.

**Returns:** `string`

```js
console.log(chromium.executablePath());
// z.B. "/home/user/.cache/ms-playwright/chromium-1084/chrome-linux/chrome"
```

---

### browserType.launch([options])

```ts
await browserType.launch([options]): Promise<Browser>
```

Startet eine neue Browser-Instanz.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options.args` | Array<string> | No | — | Zusaetzliche Kommandozeilen-Argumente fuer den Browser |
| `options.artifactsDir` | string | No | — | Verzeichnis fuer Traces, Videos, Downloads |
| `options.channel` | string | No | — | Browser-Kanal: `"chromium"`, `"chrome"`, `"chrome-beta"`, `"chrome-dev"`, `"chrome-canary"`, `"msedge"`, `"msedge-beta"`, `"msedge-dev"`, `"msedge-canary"`, `"firefox"`, `"webkit"` |
| `options.chromiumSandbox` | boolean | No | false | Chromium-Sandbox aktivieren |
| `options.downloadsPath` | string | No | tmpdir | Verzeichnis fuer akzeptierte Downloads |
| `options.env` | Object<string,string\|number\|boolean> | No | — | Umgebungsvariablen fuer den Browser-Prozess |
| `options.executablePath` | string | No | — | Pfad zu einem eigenen Browser-Executable |
| `options.firefoxUserPrefs` | Object | No | — | Firefox-Preferences (user.js) |
| `options.handleSIGHUP` | boolean | No | true | SIGHUP-Signal abfangen und Browser schliessen |
| `options.handleSIGINT` | boolean | No | true | SIGINT (Ctrl+C) abfangen und Browser schliessen |
| `options.handleSIGTERM` | boolean | No | true | SIGTERM abfangen und Browser schliessen |
| `options.headless` | boolean | No | true | Im Headless-Modus starten |
| `options.ignoreDefaultArgs` | boolean \| Array<string> | No | false | Standard-Argumente ignorieren (alle oder Liste) |
| `options.logger` | Logger | No | — | Logging-Sink (veraltet) |
| `options.proxy` | Object | No | — | Proxy-Konfiguration: `{ server, bypass?, username?, password? }` |
| `options.slowMo` | number | No | 0 | Jede Operation um X ms verzoegern (Debugging) |
| `options.timeout` | number | No | 30000 | Max. Startzeit in ms; `0` = kein Timeout |
| `options.tracesDir` | string | No | — | Verzeichnis fuer Trace-Dateien |

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

Startet einen Browser mit persistentem Benutzerprofil und gibt einen einzigen verwalteten `BrowserContext` zurueck. Schliessung des Contexts schliesst den Browser automatisch. Wird fuer Chrome-Extensions und echte User-Profile benoetigt.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `userDataDir` | string | Yes | — | Pfad zum Benutzerprofilverzeichnis (wird erstellt wenn nicht vorhanden) |
| `options` | Object | No | — | Kombination aus `launch()`-Optionen und Context-Optionen |
| `options.acceptDownloads` | boolean | No | true | |
| `options.baseURL` | string | No | — | |
| `options.bypassCSP` | boolean | No | false | |
| `options.clientCertificates` | Array<Object> | No | — | TLS-Client-Zertifikate: `{ origin, certPath?, cert?, keyPath?, key?, pfxPath?, pfx?, passphrase? }` |
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
| `options.locale` | string | No | — | z.B. `"en-GB"`, `"de-DE"` |
| `options.offline` | boolean | No | false | |
| `options.permissions` | Array<string> | No | — | |
| `options.recordHar` | Object | No | — | `{ path, omitContent?, content?, mode?, urlFilter? }` |
| `options.recordVideo` | Object | No | — | `{ dir, size?, showActions? }` |
| `options.reducedMotion` | `"reduce"` \| `"no-preference"` \| null | No | — | |
| `options.screen` | Object | No | — | `{ width, height }` in Pixeln |
| `options.serviceWorkers` | `"allow"` \| `"block"` | No | `"allow"` | |
| `options.strictSelectors` | boolean | No | false | |
| `options.timezoneId` | string | No | — | ICU-Timezone-ID |
| `options.userAgent` | string | No | — | |
| `options.viewport` | Object \| null | No | `{width:1280,height:720}` | `null` deaktiviert Viewport-Emulation |
| _alle `launch()`-Optionen_ | | No | | `args`, `channel`, `executablePath`, `headless`, etc. |

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

Startet einen Browser-Server, mit dem sich Playwright-Clients via `browserType.connect()` verbinden koennen.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `options` | Object | No | — | Alle `launch()`-Optionen plus: |
| `options.host` | string | No | `"localhost"` | WebSocket-Host |
| `options.port` | number | No | 0 | WebSocket-Port (0 = beliebiger freier Port) |
| `options.wsPath` | string | No | — | Server-Pfad (sicherheitsrelevant: unguessable Token verwenden) |

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

Gibt den Namen des Browsers zurueck.

**Returns:** `string` — `"chromium"`, `"webkit"` oder `"firefox"`

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

**Fazit:** `BrowserType` ist der Factory-Einstiegspunkt fuer alle Browser-Instanzen. `launch()` und `launchPersistentContext()` sind die haeufigstem Methoden im Test-Code. `launchServer()` + `connect()` ermoeglichen Remote-Browser-Setups fuer verteilte Test-Infrastrukturen.

---

Source: https://playwright.dev/docs/api/class-browsertype
