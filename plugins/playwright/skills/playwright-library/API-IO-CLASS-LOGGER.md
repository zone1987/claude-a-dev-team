# Playwright — class: Logger

> **Manifest:** 2 methods, 0 properties, 0 events.
> **DEPRECATED** — Playwright recommends using `Tracing` instead.
> Interface for forwarding Playwright-internal logs to custom log handlers.

---

## Contents

- [Overview](#overview)
- [Interface methods](#interface-methods)
- [Usage](#usage)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Logger` is an interface (not a concrete object) that can be passed in the
`logger` option when creating the browser. It allows
intercepting and forwarding internal Playwright logs to your own log systems.

**Deprecation note:** "The logs pumped through this class are incomplete.
Please use tracing instead." — Playwright recommends using
`context.tracing` for complete diagnostics.

---

## Interface methods

### logger.isEnabled(name, severity)

Checks whether the logger sink is interested in logs from a particular logger with
the given severity. Playwright calls this method
before the actual `log()` call — if it returns `false`,
`log()` is not called.

**Signature:**
```typescript
logger.isEnabled(
  name: string,
  severity: 'verbose' | 'info' | 'warning' | 'error'
): boolean
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `name` | `string` | yes | — | Name of the logger (e.g. `'api'`, `'browser'`, `'context'`) |
| `severity` | `'verbose' \| 'info' \| 'warning' \| 'error'` | yes | — | Severity of the log entry |

**Returns:** `boolean` — `true` if the logger should process this entry

**Example:**
```javascript
const myLogger = {
  isEnabled: (name, severity) => {
    // Only API logs at error level
    return name === 'api' && severity === 'error';
  },
  log: (name, severity, message, args) => {
    console.error(`[${name}] ${message}`);
  }
};
```

---

### logger.log(name, severity, message, args, hints)

Processes a log entry. Only called when `isEnabled()`
has returned `true`.

**Signature:**
```typescript
logger.log(
  name: string,
  severity: 'verbose' | 'info' | 'warning' | 'error',
  message: string | Error,
  args: Array<Object>,
  hints: {
    color?: string;
  }
): void
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `name` | `string` | yes | — | Logger name |
| `severity` | `'verbose' \| 'info' \| 'warning' \| 'error'` | yes | — | Severity |
| `message` | `string \| Error` | yes | — | Log message as string or Error object |
| `args` | `Array<Object>` | yes | — | Arguments for string formatting |
| `hints` | `Object` | no | `{}` | Formatting hints |
| `hints.color` | `string` | no | — | Preferred color for display (e.g. `'red'`, `'green'`) |

**Returns:** `void` (synchronous)

---

## Usage

The Logger interface is passed as an option to `chromium.launch()` / `chromium.connect()` /
`firefox.launch()` / `webkit.launch()`:

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch({
  logger: {
    isEnabled: (name, severity) => name === 'api',
    log: (name, severity, message, args) => {
      const formatted = typeof message === 'string'
        ? message
        : message.message;
      console.log(`[Playwright/${name}/${severity}] ${formatted}`);
    }
  }
});
```

### Record all logs

```javascript
const logs: string[] = [];

const browser = await chromium.launch({
  logger: {
    isEnabled: () => true,
    log: (name, severity, message) => {
      logs.push(`[${severity}][${name}] ${message}`);
    }
  }
});

// ... test actions ...

// Display on failure
if (testFailed) {
  console.log(logs.join('\n'));
}
```

---

## Properties

No public properties — purely interface-based.

## Events

No events.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 2      |
| Properties | 0     |
| Events    | 0      |

**Conclusion:** Logger is deprecated and should no longer be used in new
code. For complete diagnostics and debug information,
`context.tracing` offers a far superior alternative with visual
presentation in the Trace Viewer. Should Logger still be needed: implement `isEnabled()`
as a gating function in order to minimize performance overhead through selective
logging.

---

*Source: https://playwright.dev/docs/api/class-logger*
