# Playwright — class: Clock

> **Manifest:** 7 methods, 0 properties, 0 events.
> Controls time APIs in the browser: Date, setTimeout, setInterval, requestAnimationFrame, performance.
> Applies to the entire BrowserContext. Access: `page.clock` or `browserContext.clock`.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Typical usage patterns](#typical-usage-patterns)
- [Manifest](#manifest)

## Overview

`Clock` replaces the native browser time APIs with fake implementations
to enable deterministic time control in tests. Affected are:
`Date`, `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`,
`requestAnimationFrame`, `cancelAnimationFrame`, `requestIdleCallback`,
`cancelIdleCallback` and `performance`.

Important: the Clock API affects the entire BrowserContext — all pages
and iframes.

---

## Methods

### clock.fastForward(ticks)

Jumps time forward without triggering all timers repeatedly.
Every due timer fires at most once.

**Signature:**
```typescript
clock.fastForward(ticks: number | string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `ticks` | `number \| string` | yes | — | Number of milliseconds as a number or as a readable string: `"08"` = 8s, `"01:00"` = 1min, `"02:34:10"` = 2h34m10s |

**Returns:** `Promise<void>`

**Example:**
```javascript
// Numeric
await page.clock.fastForward(1000);        // 1 second
await page.clock.fastForward(3600 * 1000); // 1 hour

// Readable
await page.clock.fastForward('30:00');     // 30 minutes
await page.clock.fastForward('01:00:00'); // 1 hour
```

---

### clock.install(options?)

Installs fake time implementations. Must be called before the page
interaction under test.

**Signature:**
```typescript
clock.install(options?: {
  time?: number | string | Date;
}): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.time` | `number \| string \| Date` | no | current system date | Start time of the fake clock. Number = Unix timestamp (ms), string = ISO date string, Date object |

**Returns:** `Promise<void>`

**Example:**
```javascript
// With a fixed starting point (useful for reproducible tests)
await page.clock.install({ time: new Date('2024-01-15T10:00:00Z') });

// Without the option: current system date
await page.clock.install();
```

---

### clock.pauseAt(time)

Jumps to the given time and pauses the clock. After this call
no more timers fire until `runFor()`, `fastForward()`,
`pauseAt()` or `resume()` are called.

**Signature:**
```typescript
clock.pauseAt(time: number | string | Date): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | yes | — | Target time: Unix timestamp (ms), ISO string or Date object |

**Returns:** `Promise<void>`

**Example:**
```javascript
// Freeze at a specific date
await page.clock.pauseAt(new Date('2020-02-02'));
await page.clock.pauseAt('2020-02-02');
await page.clock.pauseAt(1580601600000);

// Typical use: load the page, then freeze at a specific time
await page.clock.install({ time: new Date('2024-01-01') });
await page.goto('https://example.com');
await page.clock.pauseAt(new Date('2024-01-15T09:00:00'));
// The page is now frozen — ideal for screenshot tests
```

---

### clock.resume()

Resumes the fake clock. Time runs again, timers fire normally.

**Signature:**
```typescript
clock.resume(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
await page.clock.pauseAt(new Date('2024-01-15'));
// ... assertions ...
await page.clock.resume(); // time continues to run
```

---

### clock.runFor(ticks)

Advances time by `ticks` and fires ALL due timers along the way
(in contrast to `fastForward()`, which triggers a timer only once).

**Signature:**
```typescript
clock.runFor(ticks: number | string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `ticks` | `number \| string` | yes | — | Milliseconds as a number or a readable string (same formats as `fastForward`) |

**Returns:** `Promise<void>`

**Difference from `fastForward()`:**
- `runFor()`: fires *all* timers that come due within the time window (including recursive timers).
- `fastForward()`: fires each timer at most *once*.

**Example:**
```javascript
// Run all timers within the next 5 seconds
await page.clock.runFor(5000);
await page.clock.runFor('05:00'); // 5 minutes
```

---

### clock.setFixedTime(time)

Sets `Date.now()` and `new Date()` to a fixed value. Timers keep
running normally — only the returned time is frozen.

**Signature:**
```typescript
clock.setFixedTime(time: number | string | Date): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | yes | — | Fixed time value for all Date calls |

**Returns:** `Promise<void>`

**Note:** No prior `install()` call needed — `setFixedTime()` can be
used directly without affecting other time APIs.

**Example:**
```javascript
// Freeze the date for "today is 2024-12-31" tests
await page.clock.setFixedTime(new Date('2024-12-31'));
await page.goto('https://example.com');
// Date.now() and new Date() now always return 2024-12-31
```

---

### clock.setSystemTime(time)

Sets the system time without triggering timers. Serves to test the
behaviour of the page across time jumps.

**Signature:**
```typescript
clock.setSystemTime(time: number | string | Date): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | yes | — | New system time |

**Returns:** `Promise<void>`

**Difference from `setFixedTime()`:**
- `setFixedTime()`: time stays frozen.
- `setSystemTime()`: time is set, but then continues to run normally.

**Example:**
```javascript
// Set the system time without affecting timers
await page.clock.setSystemTime(new Date('2023-06-01'));
```

---

## Typical usage patterns

### Pattern 1: testing a specific date (date only)

```javascript
// Fake only Date.now(), leave timers untouched
await page.clock.setFixedTime(new Date('2024-12-31T23:59:59'));
await page.goto('https://myapp.com/countdown');
await expect(page.getByText('1 second until new year')).toBeVisible();
```

### Pattern 2: testing timer behaviour

```javascript
await page.clock.install();
await page.goto('https://myapp.com/auto-refresh');
// The page refreshes every 30 seconds
await page.clock.runFor(30000);
await expect(page.getByText('Refreshed')).toBeVisible();
```

### Pattern 3: freeze a specific date + screenshot

```javascript
await page.clock.install({ time: new Date('2024-01-01') });
await page.goto('https://myapp.com/dashboard');
await page.clock.pauseAt(new Date('2024-06-15T14:30:00'));
await page.screenshot({ path: 'dashboard-june.png' });
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods   | 7      |
| Properties | 0     |
| Events    | 0      |

**Summary:** `setFixedTime()` is the fastest option for simple date tests.
`install()` + `pauseAt()` + `resume()` enables precise control over
timer behaviour. `runFor()` vs. `fastForward()` differ in how they
handle recursive timers — prefer `runFor()` for polling logic.

---

*Source: https://playwright.dev/docs/api/class-clock*
