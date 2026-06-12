# Playwright API: Android

> **EXPERIMENTAL** — The Android class is part of Playwright's experimental Android (ADB) support.
> Requires a running ADB (Android Debug Bridge) daemon and the Playwright driver installed on the device.

The `Android` class is the entry point for all Android device automation. It is exposed as `playwright.android`
(or `require('playwright').android` when using `_android` in legacy imports).

---

## Methods

### android.connect(endpoint, options?)

Connects to an already-running Playwright Android server via WebSocket.

**Signature:**
```js
await android.connect(endpoint, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `endpoint` | string | yes | — | WebSocket endpoint URL to connect to (e.g. `ws://localhost:4444/`) |
| `options` | Object | no | — | Additional options |
| `options.headers` | Object\<string, string\> | no | — | Additional HTTP headers sent with the WebSocket upgrade request |
| `options.slowMo` | number | no | `0` | Slows down all Playwright operations by the given number of milliseconds |
| `options.timeout` | number | no | `30000` | Maximum time (ms) to wait for the connection to be established; `0` disables the timeout |

**Returns:** `Promise<AndroidDevice>`

**Example:**
```js
const { android } = require('playwright');

const device = await android.connect('ws://192.168.1.10:4444/');
console.log(device.model());
await device.close();
```

---

### android.devices(options?)

Lists all Android devices connected to the local ADB server.

**Signature:**
```js
await android.devices(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | Additional options |
| `options.host` | string | no | `'127.0.0.1'` | ADB server host address |
| `options.omitDriverInstall` | boolean | no | `false` | If `true`, Playwright will not automatically install the driver APK on the device |
| `options.port` | number | no | `5037` | ADB server port |

**Returns:** `Promise<Array<AndroidDevice>>`

**Example:**
```js
const { android } = require('playwright');

const devices = await android.devices();
for (const device of devices) {
  console.log(device.serial(), device.model());
}
```

---

### android.launchServer(options?)

Launches a Playwright Android server that remote clients can connect to via `android.connect()`.
This is useful for remote-access and CI scenarios.

**Signature:**
```js
await android.launchServer(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | Additional options |
| `options.adbHost` | string | no | `'127.0.0.1'` | ADB server host |
| `options.adbPort` | number | no | `5037` | ADB server port |
| `options.deviceSerialNumber` | string | no | — | If specified, only the device with this serial number is used |
| `options.host` | string | no | `'localhost'` | Host that the WebSocket server listens on |
| `options.omitDriverInstall` | boolean | no | `false` | If `true`, skips automatic driver installation on the device |
| `options.port` | number | no | `0` | Port the WebSocket server listens on; `0` picks a random available port |
| `options.wsPath` | string | no | random | URL path component for the WebSocket endpoint; uses an unguessable random path by default for security |

**Returns:** `Promise<BrowserServer>`

**Example:**
```js
const { android } = require('playwright');

const server = await android.launchServer({ port: 4444 });
console.log('Listening on', server.wsEndpoint());
// Pass the wsEndpoint to android.connect() from another process
```

---

### android.setDefaultTimeout(timeout)

Sets the default timeout for all Android methods that accept a `timeout` option.
Overrides the Playwright default of 30 000 ms.

**Signature:**
```js
android.setDefaultTimeout(timeout);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `timeout` | number | yes | — | New default timeout in milliseconds |

**Returns:** `void`

**Example:**
```js
android.setDefaultTimeout(60_000); // 1 minute
```

---

## Notes

- `Android` has **no properties** and **no events** of its own.
- The class is obtained via `playwright.android` — there is no constructor.
- `AndroidKey` enum values (used by `AndroidDevice.press()`) are exported from the `playwright` package:
  `{ Back, Tab, …, VolumeUp, VolumeDown, Power, … }`. See the Playwright source for the full list.
- `AndroidSelector` is a plain object: `{ checkable?, checked?, clazz?, clickable?, depth?, desc?,
  enabled?, focusable?, focused?, hasChild?, hasDescendant?, longClickable?, pkg?, res?, scrollable?,
  selected?, text? }`. All fields are optional; an empty object matches any widget.

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 4 (`connect`, `devices`, `launchServer`, `setDefaultTimeout`) |
| Properties | 0 |
| Events | 0 |

**Fazit:** `Android` ist ein schlankes Factory-Objekt. Kernmethode ist `devices()` um verbundene Geraete
zu enumerieren; `launchServer()` + `connect()` ermoeglichen verteiltes Testen ueber WebSocket.
`setDefaultTimeout()` setzt den globalen Timeout fuer alle Android-Operationen.

---

Source: https://playwright.dev/docs/api/class-android
