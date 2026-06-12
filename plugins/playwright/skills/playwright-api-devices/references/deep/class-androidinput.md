# Playwright API: AndroidInput

> **EXPERIMENTAL** — AndroidInput is part of Playwright's experimental Android (ADB) support.

`AndroidInput` provides raw, coordinate-based input methods for an Android device.
It is accessed through the `input` property of an `AndroidDevice` instance — there is no constructor.

```js
const device = (await android.devices())[0];
// Use via:
await device.input.tap({ x: 200, y: 400 });
```

---

## Methods

### androidInput.drag(from, to, steps)

Performs a drag gesture from one screen coordinate to another.
Each step takes approximately 5 ms, so the total duration is `steps * 5 ms`.

**Signature:**
```js
await androidDevice.input.drag(from, to, steps);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `from` | Object | yes | — | Starting screen coordinate |
| `from.x` | number | yes | — | X coordinate in device pixels |
| `from.y` | number | yes | — | Y coordinate in device pixels |
| `to` | Object | yes | — | Ending screen coordinate |
| `to.x` | number | yes | — | X coordinate in device pixels |
| `to.y` | number | yes | — | Y coordinate in device pixels |
| `steps` | number | yes | — | Number of intermediate steps; each step = 5 ms |

**Returns:** `Promise<void>`

**Example:**
```js
// Drag from (100, 200) to (500, 200) over ~500 ms (100 steps)
await device.input.drag({ x: 100, y: 200 }, { x: 500, y: 200 }, 100);
```

---

### androidInput.press(key)

Presses a hardware key on the device.
Use the `AndroidKey` enum exported from the `playwright` package for key values.

**Signature:**
```js
await androidDevice.input.press(key);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | AndroidKey | yes | — | Key code to press |

**Returns:** `Promise<void>`

**Common AndroidKey values:**

| Key name | Description |
|---|---|
| `AndroidKey.Back` | Back button |
| `AndroidKey.Home` | Home button |
| `AndroidKey.Menu` | Menu button |
| `AndroidKey.Enter` | Enter / Confirm |
| `AndroidKey.Tab` | Tab |
| `AndroidKey.VolumeUp` | Volume up |
| `AndroidKey.VolumeDown` | Volume down |
| `AndroidKey.Power` | Power button |
| `AndroidKey.Search` | Search button |
| `AndroidKey.Del` | Backspace / Delete |

**Example:**
```js
const { AndroidKey } = require('playwright');
await device.input.press(AndroidKey.Back);
await device.input.press(AndroidKey.Home);
```

---

### androidInput.swipe(from, segments, steps)

Performs a multi-segment swipe gesture. The gesture starts at `from`, then follows
each point in `segments` sequentially. Each step per segment takes approximately 5 ms.

**Signature:**
```js
await androidDevice.input.swipe(from, segments, steps);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `from` | Object | yes | — | Starting screen coordinate |
| `from.x` | number | yes | — | X coordinate in device pixels |
| `from.y` | number | — | — | Y coordinate in device pixels |
| `segments` | Array\<Object\> | yes | — | Array of waypoints after the starting point |
| `segments[n].x` | number | yes | — | X coordinate of waypoint n |
| `segments[n].y` | number | yes | — | Y coordinate of waypoint n |
| `steps` | number | yes | — | Steps per segment; each step = 5 ms (e.g. 100 steps ≈ 0.5 s per segment) |

**Returns:** `Promise<void>`

**Example:**
```js
// Swipe right across the screen in two steps
await device.input.swipe(
  { x: 100, y: 400 },
  [{ x: 400, y: 400 }, { x: 700, y: 400 }],
  50
);
```

---

### androidInput.tap(point)

Taps at the specified screen coordinate.

**Signature:**
```js
await androidDevice.input.tap(point);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `point` | Object | yes | — | Screen coordinate to tap |
| `point.x` | number | yes | — | X coordinate in device pixels |
| `point.y` | number | yes | — | Y coordinate in device pixels |

**Returns:** `Promise<void>`

**Example:**
```js
// Tap at the center of a 1080x1920 screen
await device.input.tap({ x: 540, y: 960 });
```

---

### androidInput.type(text)

Types text into the currently focused widget using keyboard events.
The widget must already be focused (e.g. via a preceding `device.tap()`).

**Signature:**
```js
await androidDevice.input.type(text);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | string | yes | — | Text to type into the focused widget |

**Returns:** `Promise<void>`

**Example:**
```js
await device.tap({ res: 'com.example:id/email_field' });
await device.input.type('user@example.com');
await device.input.press(AndroidKey.Tab);
await device.input.type('password123');
await device.input.press(AndroidKey.Enter);
```

---

## Notes

- `AndroidInput` has **no properties** and **no events**.
- All coordinate-based methods use **device pixels** (not CSS pixels or DP), so you may need to
  account for the device's density (DPR). Use `device.shell('wm size')` to retrieve screen dimensions.
- `AndroidInput` methods bypass the widget-selector system — they operate on raw screen coordinates.
  For higher-level UI automation prefer the selector-based methods on `AndroidDevice`
  (e.g. `device.tap(selector)`, `device.fill(selector, text)`).

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 5 (`drag`, `press`, `swipe`, `tap`, `type`) |
| Properties | 0 |
| Events | 0 |

**Fazit:** `AndroidInput` ist die Low-Level-Schicht fuer koordinatenbasierte Eingaben.
`drag` und `swipe` verwenden Steps als Zeiteinheit (1 Step = 5 ms), was genaue
Geschwindigkeitskontrolle ermoeglicht. `swipe` unterstuetzt Multi-Segment-Pfade.
Fuer die meisten Anwendungsfaelle sind die Selector-basierten Methoden auf `AndroidDevice` vorzuziehen.

---

Source: https://playwright.dev/docs/api/class-androidinput
