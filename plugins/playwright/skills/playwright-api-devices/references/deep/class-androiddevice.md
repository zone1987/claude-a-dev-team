# Playwright API: AndroidDevice

> **EXPERIMENTAL** — AndroidDevice is part of Playwright's experimental Android (ADB) support.

`AndroidDevice` represents a single connected Android device. Instances are obtained from
`android.devices()` or `android.connect()`. The device exposes both UI-automation methods
(tap, swipe, fill, …) and lower-level shell/file operations.

---

## Events

### androidDevice.on('close')

Emitted when the device connection is closed.

**Event data:** `AndroidDevice` (the device instance)

```js
device.on('close', () => console.log('Device disconnected'));
```

---

### androidDevice.on('webview')

Emitted when a new WebView instance is opened on the device.

**Event data:** `AndroidWebView`

```js
device.on('webview', (webview) => {
  console.log('New WebView from package', webview.pkg());
});
```

---

## Properties

### androidDevice.input

**Type:** `AndroidInput`

Provides raw, coordinate-based input methods (tap, drag, swipe, press key, type text).

```js
await device.input.tap({ x: 100, y: 200 });
```

---

## Methods

### androidDevice.close()

Closes the connection to the device. After calling this the device object must not be used.

**Signature:**
```js
await androidDevice.close();
```

**Parameters:** none

**Returns:** `Promise<void>`

**Example:**
```js
await device.close();
```

---

### androidDevice.drag(selector, dest, options?)

Drags the widget matched by `selector` to the destination point.

**Signature:**
```js
await androidDevice.drag(selector, dest, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to drag (see AndroidSelector type) |
| `dest` | Object | yes | — | Destination coordinates |
| `dest.x` | number | yes | — | X coordinate in device pixels |
| `dest.y` | number | yes | — | Y coordinate in device pixels |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Drag speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms) to wait for the widget; `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.drag({ text: 'Item' }, { x: 500, y: 800 }, { speed: 1000 });
```

---

### androidDevice.fill(selector, text, options?)

Fills the text input matched by `selector` with `text`.
Clears any existing content before typing.

**Signature:**
```js
await androidDevice.fill(selector, text, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Input widget to fill |
| `text` | string | yes | — | Text to enter |
| `options` | Object | no | — | |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.fill({ res: 'com.example.app:id/search' }, 'Playwright');
```

---

### androidDevice.fling(selector, direction, options?)

Flings (fast-scroll) the widget matched by `selector` in the given direction.

**Signature:**
```js
await androidDevice.fling(selector, direction, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to fling |
| `direction` | `"down"` \| `"up"` \| `"left"` \| `"right"` | yes | — | Fling direction |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Fling speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.fling({ clazz: 'androidx.recyclerview.widget.RecyclerView' }, 'up');
```

---

### androidDevice.info(selector)

Returns detailed information about the widget matched by `selector`.

**Signature:**
```js
await androidDevice.info(selector);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to inspect |

**Returns:** `Promise<AndroidElementInfo>`

`AndroidElementInfo` has the following shape:
```ts
{
  bounds: { x: number; y: number; width: number; height: number };
  checkable: boolean;
  checked: boolean;
  clazz: string;
  clickable: boolean;
  desc: string;
  enabled: boolean;
  focusable: boolean;
  focused: boolean;
  longClickable: boolean;
  pkg: string;
  res: string;
  scrollable: boolean;
  selected: boolean;
  text: string;
}
```

**Example:**
```js
const info = await device.info({ res: 'com.example:id/btn_ok' });
console.log(info.bounds, info.text);
```

---

### androidDevice.installApk(file, options?)

Installs an APK on the device.

**Signature:**
```js
await androidDevice.installApk(file, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `file` | string \| Buffer | yes | — | Path to the APK file or its contents as a Buffer |
| `options` | Object | no | — | |
| `options.args` | Array\<string\> | no | `['-r', '-t', '-S']` | Extra arguments passed to `adb install` |

**Returns:** `Promise<void>`

**Example:**
```js
await device.installApk('./app-debug.apk');
await device.installApk('./app-debug.apk', { args: ['-r', '-t', '-d', '-S'] });
```

---

### androidDevice.launchBrowser(options?)

Launches Chrome on the device and returns a Playwright `BrowserContext`
representing a persistent browser context. Use this to run normal Playwright
page automation inside Chrome on Android.

**Signature:**
```js
await androidDevice.launchBrowser(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | |
| `options.acceptDownloads` | boolean | no | `true` | Whether to automatically download attachments |
| `options.args` | Array\<string\> | no | — | Additional Chromium command-line flags |
| `options.baseURL` | string | no | — | Base URL for relative navigations |
| `options.bypassCSP` | boolean | no | `false` | Bypass Content-Security-Policy |
| `options.colorScheme` | `null` \| `"light"` \| `"dark"` \| `"no-preference"` | no | `'light'` | Emulated color scheme |
| `options.contrast` | `null` \| `"no-preference"` \| `"more"` | no | `'no-preference'` | Emulated contrast preference |
| `options.deviceScaleFactor` | number | no | `1` | Device pixel ratio |
| `options.extraHTTPHeaders` | Object\<string, string\> | no | — | Extra headers sent with every request |
| `options.forcedColors` | `null` \| `"active"` \| `"none"` | no | `'none'` | Emulate forced-colors media feature |
| `options.geolocation` | Object | no | — | |
| `options.geolocation.latitude` | number | yes (if set) | — | Latitude: −90 to 90 |
| `options.geolocation.longitude` | number | yes (if set) | — | Longitude: −180 to 180 |
| `options.geolocation.accuracy` | number | no | `0` | Non-negative accuracy value in meters |
| `options.hasTouch` | boolean | no | `false` | Emulate touch events |
| `options.httpCredentials` | Object | no | — | HTTP authentication credentials |
| `options.httpCredentials.username` | string | yes (if set) | — | |
| `options.httpCredentials.password` | string | yes (if set) | — | |
| `options.httpCredentials.origin` | string | no | — | Restrict credentials to this origin |
| `options.httpCredentials.send` | `"unauthorized"` \| `"always"` | no | `'unauthorized'` | When to send credentials |
| `options.ignoreHTTPSErrors` | boolean | no | `false` | Ignore HTTPS errors |
| `options.isMobile` | boolean | no | `false` | Mobile viewport emulation |
| `options.javaScriptEnabled` | boolean | no | `true` | Enable/disable JavaScript |
| `options.locale` | string | no | — | BCP 47 locale tag, e.g. `'de-DE'` |
| `options.offline` | boolean | no | `false` | Emulate offline network |
| `options.permissions` | Array\<string\> | no | — | Granted browser permissions |
| `options.pkg` | string | no | — | Custom browser package name on device (default: Chrome) |
| `options.proxy` | Object | no | — | Proxy settings |
| `options.proxy.server` | string | yes (if set) | — | Proxy server URL |
| `options.proxy.bypass` | string | no | — | Comma-separated domains to bypass |
| `options.proxy.username` | string | no | — | Proxy auth username |
| `options.proxy.password` | string | no | — | Proxy auth password |
| `options.recordHar` | Object | no | — | HAR recording options |
| `options.recordHar.path` | string | yes (if set) | — | Path to save the HAR file |
| `options.recordHar.omitContent` | boolean | no | `false` | Omit request bodies |
| `options.recordHar.content` | `"omit"` \| `"embed"` \| `"attach"` | no | — | How to store request content |
| `options.recordHar.mode` | `"full"` \| `"minimal"` | no | `'full'` | Recording detail level |
| `options.recordHar.urlFilter` | string \| RegExp | no | — | Filter recorded URLs |
| `options.recordVideo` | Object | no | — | Video recording options |
| `options.recordVideo.dir` | string | no | — | Directory to save videos |
| `options.recordVideo.size` | Object | no | — | Video frame dimensions |
| `options.recordVideo.size.width` | number | yes (if set) | — | Frame width in pixels |
| `options.recordVideo.size.height` | number | yes (if set) | — | Frame height in pixels |
| `options.reducedMotion` | `null` \| `"reduce"` \| `"no-preference"` | no | `'no-preference'` | Emulate reduced-motion preference |
| `options.screen` | Object | no | — | Screen dimensions (independent of viewport) |
| `options.screen.width` | number | yes (if set) | — | Screen width in pixels |
| `options.screen.height` | number | yes (if set) | — | Screen height in pixels |
| `options.serviceWorkers` | `"allow"` \| `"block"` | no | `'allow'` | Service worker handling |
| `options.strictSelectors` | boolean | no | `false` | Throw on ambiguous selectors |
| `options.timezoneId` | string | no | — | ICU timezone ID, e.g. `'Europe/Berlin'` |
| `options.userAgent` | string | no | — | Custom user-agent string |
| `options.viewport` | null \| Object | no | 1280×720 | Viewport size; `null` disables emulation |
| `options.viewport.width` | number | yes (if set) | — | Viewport width in pixels |
| `options.viewport.height` | number | yes (if set) | — | Viewport height in pixels |

**Returns:** `Promise<BrowserContext>`

**Example:**
```js
const context = await device.launchBrowser({ locale: 'de-DE' });
const page = await context.newPage();
await page.goto('https://playwright.dev');
await page.screenshot({ path: 'android-pw.png' });
await context.close();
```

---

### androidDevice.longTap(selector, options?)

Performs a long press on the widget matched by `selector`.

**Signature:**
```js
await androidDevice.longTap(selector, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to long-press |
| `options` | Object | no | — | |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.longTap({ text: 'Hold me' });
```

---

### androidDevice.model()

Returns the device model identifier string (e.g. `'Pixel 4'`).

**Signature:**
```js
androidDevice.model();
```

**Parameters:** none

**Returns:** `string`

**Example:**
```js
console.log(device.model()); // "sdk_gphone64_arm64"
```

---

### androidDevice.open(command)

Launches a process on the device via the given shell command and returns an
`AndroidSocket` for bidirectional communication with that process.

**Signature:**
```js
await androidDevice.open(command);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `command` | string | yes | — | Shell command to execute on the device |

**Returns:** `Promise<AndroidSocket>`

**Example:**
```js
const socket = await device.open('logcat -T 1');
socket.on('data', (buf) => process.stdout.write(buf.toString()));
await new Promise((r) => setTimeout(r, 3000));
await socket.close();
```

---

### androidDevice.pinchClose(selector, percent, options?)

Performs a pinch-close (zoom out) gesture on the widget.

**Signature:**
```js
await androidDevice.pinchClose(selector, percent, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to pinch |
| `percent` | number | yes | — | Pinch amount as a fraction of the widget's size (e.g. `0.5` for 50 %) |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.pinchClose({ clazz: 'android.webkit.WebView' }, 0.5);
```

---

### androidDevice.pinchOpen(selector, percent, options?)

Performs a pinch-open (zoom in) gesture on the widget.

**Signature:**
```js
await androidDevice.pinchOpen(selector, percent, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to pinch |
| `percent` | number | yes | — | Pinch amount as a fraction of the widget's size |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.pinchOpen({ clazz: 'android.webkit.WebView' }, 0.5);
```

---

### androidDevice.press(selector, key, options?)

Presses a hardware key while the widget matched by `selector` is focused.

**Signature:**
```js
await androidDevice.press(selector, key, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to focus before pressing |
| `key` | AndroidKey | yes | — | Key code to press (enum exported from Playwright, e.g. `AndroidKey.Back`) |
| `options` | Object | no | — | |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
const { AndroidKey } = require('playwright');
await device.press({ res: 'com.example:id/input' }, AndroidKey.Enter);
```

---

### androidDevice.push(file, path, options?)

Copies a file to the device.

**Signature:**
```js
await androidDevice.push(file, path, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `file` | string \| Buffer | yes | — | Local file path or file content as Buffer |
| `path` | string | yes | — | Absolute destination path on the device |
| `options` | Object | no | — | |
| `options.mode` | number | no | `644` | Unix file permissions as an octal number |

**Returns:** `Promise<void>`

**Example:**
```js
await device.push('./test-data.json', '/sdcard/Download/test-data.json');
```

---

### androidDevice.screenshot(options?)

Captures the current device screen and returns it as a PNG buffer.

**Signature:**
```js
await androidDevice.screenshot(options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `options` | Object | no | — | |
| `options.path` | string | no | — | If provided, saves the screenshot to this file path |

**Returns:** `Promise<Buffer>`

**Example:**
```js
const buf = await device.screenshot({ path: 'screen.png' });
```

---

### androidDevice.scroll(selector, direction, percent, options?)

Scrolls the widget matched by `selector` in the given direction by `percent` of the widget's size.

**Signature:**
```js
await androidDevice.scroll(selector, direction, percent, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to scroll |
| `direction` | `"down"` \| `"up"` \| `"left"` \| `"right"` | yes | — | Scroll direction |
| `percent` | number | yes | — | Scroll distance as fraction of widget size |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Scroll speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.scroll({ clazz: 'android.widget.ListView' }, 'down', 0.5);
```

---

### androidDevice.serial()

Returns the ADB serial number of the device.

**Signature:**
```js
androidDevice.serial();
```

**Parameters:** none

**Returns:** `string`

**Example:**
```js
console.log(device.serial()); // "emulator-5554"
```

---

### androidDevice.setDefaultTimeout(timeout)

Overrides the default timeout for all methods on this device instance that accept a `timeout` option.

**Signature:**
```js
androidDevice.setDefaultTimeout(timeout);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `timeout` | number | yes | — | New default timeout in milliseconds; `0` disables all timeouts |

**Returns:** `void`

**Example:**
```js
device.setDefaultTimeout(60_000);
```

---

### androidDevice.shell(command)

Executes a shell command on the device and returns the combined stdout/stderr as a Buffer.

**Signature:**
```js
await androidDevice.shell(command);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `command` | string | yes | — | ADB shell command string |

**Returns:** `Promise<Buffer>`

**Example:**
```js
const out = await device.shell('pm list packages -3');
console.log(out.toString());
```

---

### androidDevice.swipe(selector, direction, percent, options?)

Performs a swipe gesture on the widget matched by `selector`.

**Signature:**
```js
await androidDevice.swipe(selector, direction, percent, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to swipe |
| `direction` | `"down"` \| `"up"` \| `"left"` \| `"right"` | yes | — | Swipe direction |
| `percent` | number | yes | — | Swipe distance as fraction of widget size |
| `options` | Object | no | — | |
| `options.speed` | number | no | — | Swipe speed in pixels/second |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.swipe({ clazz: 'androidx.viewpager.widget.ViewPager' }, 'left', 1.0);
```

---

### androidDevice.tap(selector, options?)

Taps on the widget matched by `selector`.

**Signature:**
```js
await androidDevice.tap(selector, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget to tap |
| `options` | Object | no | — | |
| `options.duration` | number | no | — | Duration of the tap in milliseconds (for long-press effect) |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.tap({ text: 'Sign in' });
await device.tap({ res: 'com.example:id/btn_ok' }, { duration: 500 });
```

---

### androidDevice.wait(selector, options?)

Waits until the widget matched by `selector` appears (default) or disappears.

**Signature:**
```js
await androidDevice.wait(selector, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | AndroidSelector | yes | — | Widget selector |
| `options` | Object | no | — | |
| `options.state` | `"gone"` | no | — | If set to `"gone"`, waits for the widget to disappear instead of appear |
| `options.timeout` | number | no | `30000` | Maximum time (ms); `0` disables timeout |

**Returns:** `Promise<void>`

**Example:**
```js
await device.wait({ text: 'Loading' }, { state: 'gone' });
await device.wait({ res: 'com.example:id/main_content' });
```

---

### androidDevice.waitForEvent(event, optionsOrPredicate?)

Waits for a named event and returns its data. Optionally filters using a predicate function.

**Signature:**
```js
await androidDevice.waitForEvent(event, optionsOrPredicate?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `event` | string | yes | — | Event name (e.g. `'webview'`, `'close'`) |
| `optionsOrPredicate` | function \| Object | no | — | Predicate or options object |
| `optionsOrPredicate` (as function) | (data: any) => boolean | no | — | Called with event data; resolves when returning truthy |
| `optionsOrPredicate.predicate` | function | no | — | Same as above when passing an object |
| `optionsOrPredicate.timeout` | number | no | `30000` | Maximum wait time (ms); `0` disables timeout |

**Returns:** `Promise<Object>`

**Example:**
```js
const webview = await device.waitForEvent('webview', {
  predicate: (wv) => wv.pkg() === 'com.example.app',
  timeout: 15_000,
});
```

---

### androidDevice.webView(selector, options?)

Returns an existing WebView matching `selector`, or waits for one to appear.

**Signature:**
```js
await androidDevice.webView(selector, options?);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `selector` | Object | yes | — | |
| `selector.pkg` | string | no | — | Package name of the application hosting the WebView |
| `selector.socketName` | string | no | — | WebView socket name (from `adb shell cat /proc/net/unix`) |
| `options` | Object | no | — | |
| `options.timeout` | number | no | `30000` | Maximum wait time (ms); `0` disables timeout |

**Returns:** `Promise<AndroidWebView>`

**Example:**
```js
const wv = await device.webView({ pkg: 'com.example.app' });
const page = await wv.page();
await page.goto('https://example.com');
```

---

### androidDevice.webViews()

Returns all currently open WebView instances on the device.

**Signature:**
```js
androidDevice.webViews();
```

**Parameters:** none

**Returns:** `Array<AndroidWebView>`

**Example:**
```js
const views = device.webViews();
for (const wv of views) {
  console.log(wv.pkg(), wv.pid());
}
```

---

## AndroidSelector Type Reference

`AndroidSelector` is a plain object — all fields are optional and combined as AND-conditions:

| Field | Type | Description |
|---|---|---|
| `checkable` | boolean | Widget is checkable |
| `checked` | boolean | Widget is checked |
| `clazz` | string \| RegExp | Full Java class name (e.g. `'android.widget.Button'`) |
| `clickable` | boolean | Widget is clickable |
| `depth` | number | UI tree depth |
| `desc` | string \| RegExp | Content description (`android:contentDescription`) |
| `enabled` | boolean | Widget is enabled |
| `focusable` | boolean | Widget is focusable |
| `focused` | boolean | Widget currently has focus |
| `hasChild` | Object | Must have a direct child matching this sub-selector |
| `hasDescendant` | Object | Must have a descendant matching this sub-selector |
| `longClickable` | boolean | Widget supports long-click |
| `pkg` | string | Package name of the owning application |
| `res` | string | Resource ID (e.g. `'com.example:id/submit'`) |
| `scrollable` | boolean | Widget is scrollable |
| `selected` | boolean | Widget is selected |
| `text` | string \| RegExp | Widget text label |

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 22 (`close`, `drag`, `fill`, `fling`, `info`, `installApk`, `launchBrowser`, `longTap`, `model`, `open`, `pinchClose`, `pinchOpen`, `press`, `push`, `screenshot`, `scroll`, `serial`, `setDefaultTimeout`, `shell`, `swipe`, `tap`, `wait`, `waitForEvent`, `webView`, `webViews`) |
| Properties | 1 (`input`) |
| Events | 2 (`close`, `webview`) |

**Fazit:** `AndroidDevice` ist die Kern-API fuer Android-Automatisierung. Sie deckt saemlichte
UI-Gesten (Tap, Swipe, Fling, Pinch, Drag), Datei-/Shell-Operationen und WebView-Integration ab.
Die Methode `launchBrowser()` gibt einen Standard-Playwright-`BrowserContext` zurueck und ermoeglicht
damit die volle Page-API auf Android-Chrome.

---

Source: https://playwright.dev/docs/api/class-androiddevice
