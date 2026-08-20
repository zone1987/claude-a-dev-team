# Playwright Emulation, Clock and Screenshots - Complete Reference

---

## Contents

- [1. Device emulation](#1-device-emulation)
- [2. Viewport](#2-viewport)
- [3. isMobile](#3-ismobile)
- [4. User Agent](#4-user-agent)
- [5. Locale and timezone](#5-locale-and-timezone)
- [6. Geolocation](#6-geolocation)
- [7. Permissions](#7-permissions)
- [8. Color scheme and media](#8-color-scheme-and-media)
- [9. Offline mode and JavaScript](#9-offline-mode-and-javascript)
- [10. Clock API](#10-clock-api)
- [11. Screenshots](#11-screenshots)
- [12. Complete emulation example](#12-complete-emulation-example)

## 1. Device emulation

Playwright ships with a database of predefined device parameters.

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 7'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 15'] },
    },
    {
      name: 'Desktop Chrome',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
```

A device preset automatically sets: `userAgent`, `viewport`, `deviceScaleFactor`,
`isMobile`, `hasTouch`.

```typescript
// Platform-agnostic user agent (override the preset)
test.use({
  ...devices['iPhone 15'],
  userAgent: undefined, // No platform-specific UA
});
```

---

## 2. Viewport

### Configuration

```typescript
// playwright.config.ts
use: {
  viewport: { width: 1280, height: 720 },
}

// Per test
test.use({
  viewport: { width: 1920, height: 1080 },
});

// At runtime
await page.setViewportSize({ width: 375, height: 812 });
```

### Device Scale Factor (HiDPI)

```typescript
const context = await browser.newContext({
  viewport: { width: 2560, height: 1440 },
  deviceScaleFactor: 2, // Retina
});
```

---

## 3. isMobile

Controls whether the meta viewport tag is respected and touch events are enabled.

```typescript
use: { isMobile: true }  // Default for mobile devices: true

// No direct API at runtime - only when creating the context
const context = await browser.newContext({ isMobile: true });
```

---

## 4. User Agent

```typescript
// Configuration
test.use({ userAgent: 'MyTestBot/1.0' });

// Per context
const context = await browser.newContext({
  userAgent: 'Mozilla/5.0 (compatible; TestRunner/1.0)',
});

// Runtime (only via a new page in the context)
```

---

## 5. Locale and timezone

```typescript
// Configuration
use: {
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
}

// Per context
const context = await browser.newContext({
  locale: 'ja-JP',
  timezoneId: 'Asia/Tokyo',
});
```

**Note:** `timezoneId` affects only the browser, not the test runner.
For the test runner: set the `TZ` environment variable.

Valid timezone IDs: IANA format, e.g. `'America/New_York'`, `'UTC'`,
`'Europe/Paris'`, `'Asia/Shanghai'`.

---

## 6. Geolocation

```typescript
// Configuration
use: {
  geolocation: { longitude: 13.405, latitude: 52.52 }, // Berlin
  permissions: ['geolocation'],
}

// Update at runtime (applies to all pages in the context)
await context.setGeolocation({ longitude: 2.349, latitude: 48.864 }); // Paris

// With accuracy
await context.setGeolocation({
  longitude: -0.1276,
  latitude: 51.5074,
  accuracy: 10, // meters
});
```

**Important:** Geolocation can only be changed for the entire context, not
individually per page.

---

## 7. Permissions

### Granting

```typescript
// Configuration (all pages in the project)
use: {
  permissions: ['notifications', 'geolocation'],
}

// Per context
const context = await browser.newContext({
  permissions: ['camera', 'microphone'],
});

// Domain-specific
await context.grantPermissions(['notifications'], {
  origin: 'https://example.com',
});

// Multiple domains
await context.grantPermissions(['geolocation'], { origin: 'https://maps.google.com' });
await context.grantPermissions(['geolocation'], { origin: 'https://openstreetmap.org' });
```

### Resetting

```typescript
await context.clearPermissions(); // Revoke all permissions
```

### Supported permissions

`'accelerometer'`, `'ambient-light-sensor'`, `'background-sync'`,
`'camera'`, `'clipboard-read'`, `'clipboard-write'`, `'geolocation'`,
`'gyroscope'`, `'magnetometer'`, `'microphone'`, `'midi'`,
`'notifications'`, `'payment-handler'`, `'persistent-storage'`,
`'push'`, `'screen-wake-lock'`, `'storage-access'`

---

## 8. Color scheme and media

### Color Scheme

```typescript
// Configuration
use: { colorScheme: 'dark' } // 'light' | 'dark' | 'no-preference'

// At runtime
await page.emulateMedia({ colorScheme: 'dark' });
await page.emulateMedia({ colorScheme: 'light' });
```

### Media Type

```typescript
// Emulate print preview
await page.emulateMedia({ media: 'print' }); // 'screen' | 'print' | null

// Reduced motion
await page.emulateMedia({ reducedMotion: 'reduce' }); // 'reduce' | 'no-preference' | null

// Contrast preference
await page.emulateMedia({ forcedColors: 'active' }); // 'active' | 'none' | null
```

### emulateMedia complete options

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `colorScheme` | `'light' \| 'dark' \| 'no-preference' \| null` | - | Color scheme preference |
| `forcedColors` | `'active' \| 'none' \| null` | - | Forced colors |
| `media` | `'screen' \| 'print' \| null` | - | CSS media type |
| `reducedMotion` | `'reduce' \| 'no-preference' \| null` | - | Animation reduction |

```typescript
// All options together
await page.emulateMedia({
  colorScheme: 'dark',
  media: 'screen',
  reducedMotion: 'reduce',
});
```

---

## 9. Offline mode and JavaScript

```typescript
// Offline
use: { offline: true }

const context = await browser.newContext({ offline: true });
await context.setOffline(true);  // At runtime
await context.setOffline(false);

// Disable JavaScript
test.use({ javaScriptEnabled: false });

const context = await browser.newContext({ javaScriptEnabled: false });
```

---

## 10. Clock API

The Clock API provides complete control over time in the browser.

### Method overview

| Method | Description |
|---------|--------------|
| `page.clock.setFixedTime(time)` | Fixed time for Date.now() and new Date() |
| `page.clock.install(options?)` | Complete clock takeover |
| `page.clock.pauseAt(time)` | Jump to a time and pause |
| `page.clock.fastForward(ticks)` | Fast-forward time (timers fire at most once) |
| `page.clock.runFor(ticks)` | Fast-forward time (fire all timers) |
| `page.clock.resume()` | Let a paused clock continue |
| `page.clock.setSystemTime(time)` | Set the system time without firing timers |

---

### page.clock.setFixedTime(time)

Simplest method: pins `Date.now()` and `new Date()`. Timers keep running.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | Fixed time |

```typescript
// Pin the date
await page.clock.setFixedTime(new Date('2024-02-29T10:00:00'));
await page.goto('http://localhost:3000');
await expect(page.getByTestId('date-display')).toHaveText('Feb 29, 2024');

// As a Unix timestamp (ms)
await page.clock.setFixedTime(1709200000000);

// As an ISO string
await page.clock.setFixedTime('2024-02-29');
```

---

### page.clock.install(options?)

Replaces all native time functions with fakes.

**Overridden globals:**
`Date`, `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`,
`requestAnimationFrame`, `cancelAnimationFrame`, `requestIdleCallback`,
`cancelIdleCallback`, `performance`, `Event.timeStamp`

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `time` | `number \| string \| Date` | System time | Start time |

**Important:** `install()` MUST come before all other clock calls,
if used at all.

```typescript
await page.clock.install({ time: new Date('2024-01-01T09:00:00') });
await page.goto('http://localhost:3000/dashboard');
// All timers and Date calls are now controllable
```

---

### page.clock.pauseAt(time)

Jumps to the given time and pauses all timers.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | Target time |

```typescript
await page.clock.install({ time: new Date('2024-12-10T08:00:00') });
await page.goto('http://localhost:3000');
await page.clock.pauseAt(new Date('2024-12-10T10:00:00'));
// Time is now 10:00, no timers are running

await expect(page.getByTestId('clock')).toHaveText('10:00:00');
```

---

### page.clock.fastForward(ticks)

Jumps forward; every due timer runs at most once.
Simulates e.g. closing a laptop lid.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `ticks` | `number \| string` | Milliseconds or `'HH:MM:SS'` format |

```typescript
// Fast-forward 30 minutes
await page.clock.fastForward('30:00');

// As milliseconds
await page.clock.fastForward(1800000);

// Pattern: install -> navigate -> pause -> fastForward
await page.clock.install({ time: new Date('2024-02-02T08:00:00') });
await page.goto('http://localhost:3000');
await page.clock.pauseAt(new Date('2024-02-02T10:00:00'));
await page.clock.fastForward('30:00'); // Up to 10:30
```

---

### page.clock.runFor(ticks)

Like `fastForward`, but all timers fire in real-time order.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `ticks` | `number \| string` | Milliseconds or `'HH:MM:SS'` format |

```typescript
// Simulate 2 seconds (all timeouts/intervals fire)
await page.clock.runFor(2000);
await page.clock.runFor('00:02'); // 2 seconds

// Interval test
await page.clock.install();
await page.evaluate(() => {
  setInterval(() => document.body.setAttribute('data-tick', String(Date.now())), 1000);
});
await page.clock.runFor(5000); // 5 ticks
```

---

### page.clock.resume()

Resumes a paused clock.

```typescript
await page.clock.install();
await page.clock.pauseAt(new Date('2024-06-15T12:00:00'));
// ... tests at time 12:00 ...
await page.clock.resume(); // Timers run again
```

---

### page.clock.setSystemTime(time)

Sets the system time but does not fire any timers. For timezone-jump tests.

| Parameter | Type | Description |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | New system time |

```typescript
await page.clock.install();
await page.clock.setSystemTime(new Date('2024-12-31T23:59:00'));
// The page reacts to year-change logic
```

---

### Time format for ticks/time

| Format | Example | Meaning |
|--------|---------|-----------|
| `number` | `3600000` | Milliseconds |
| `string HH` | `'30'` | 30 seconds |
| `string HH:MM` | `'01:30'` | 1 minute 30 seconds |
| `string HH:MM:SS` | `'02:30:00'` | 2 hours 30 minutes |
| `Date` | `new Date('2024-01-01')` | Date object |
| ISO string | `'2024-01-01T12:00:00'` | ISO date |

---

## 11. Screenshots

### page.screenshot(options?)

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `path` | `string` | - | Save path (extension determines the format: .png, .jpg) |
| `type` | `'png' \| 'jpeg'` | `'png'` | Image format |
| `quality` | `number` | - | JPEG quality 0-100 (JPEG only) |
| `fullPage` | `boolean` | `false` | Entire scrollable page |
| `clip` | `{x, y, width, height}` | - | Clipping rectangle |
| `omitBackground` | `boolean` | `false` | Transparency instead of a white background (PNG only) |
| `animations` | `'disabled' \| 'allow'` | `'disabled'` | CSS animations |
| `caret` | `'hide' \| 'initial'` | `'hide'` | Caret visibility |
| `scale` | `'css' \| 'device'` | `'device'` | Render scale |
| `mask` | `Locator[]` | - | Mask elements |
| `maskColor` | `string` | `'#FF00FF'` | Masking color |
| `timeout` | `number` | `0` | Timeout in ms |

```typescript
// Simple screenshot
await page.screenshot({ path: 'screenshot.png' });

// Whole page
await page.screenshot({ path: 'full.png', fullPage: true });

// Clipping
await page.screenshot({
  path: 'header.png',
  clip: { x: 0, y: 0, width: 1280, height: 80 },
});

// JPEG with quality
await page.screenshot({
  path: 'preview.jpg',
  type: 'jpeg',
  quality: 80,
});

// Transparent background
await page.screenshot({
  path: 'transparent.png',
  omitBackground: true,
});

// Mask sensitive data
await page.screenshot({
  path: 'masked.png',
  mask: [page.locator('.credit-card'), page.locator('#password')],
  maskColor: '#000000',
});

// Buffer (no file path)
const buffer = await page.screenshot();
const base64 = buffer.toString('base64');
```

### locator.screenshot(options?)

Screenshot of a single element (same options as page.screenshot).

```typescript
await page.locator('.product-card').first().screenshot({ path: 'card.png' });

// Element screenshot into a buffer
const cardBuffer = await page.locator('.hero-image').screenshot();
```

---

## 12. Complete emulation example

```typescript
import { test, expect, devices } from '@playwright/test';

test.use({
  ...devices['iPhone 15 Pro'],
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
  geolocation: { latitude: 48.137, longitude: 11.576 }, // Munich
  permissions: ['geolocation'],
  colorScheme: 'dark',
});

test('mobile dark mode with geolocation', async ({ page, context }) => {
  // Pin the clock
  await page.clock.setFixedTime(new Date('2024-06-21T14:30:00+02:00'));

  await page.goto('http://localhost:3000');

  // Update geolocation at runtime
  await context.setGeolocation({ latitude: 52.52, longitude: 13.405 }); // Berlin
  await page.reload();

  await page.screenshot({
    path: 'test-results/mobile-dark.png',
    fullPage: true,
    mask: [page.locator('.user-data')],
  });
});
```

---

Source: https://playwright.dev/docs/emulation | https://playwright.dev/docs/clock | https://playwright.dev/docs/screenshots | https://playwright.dev/docs/api/class-clock
