# Playwright — class: Credentials (HTTPCredentials)

> **Manifest:** 0 methods, 2-4 properties (interface), 0 events.
> Not a standalone class object — `Credentials` / `HTTPCredentials` is a
> configuration interface for HTTP basic authentication in BrowserContext.

---

## Contents

- [Status](#status)
- [HTTPCredentials interface](#httpcredentials-interface)
- [Usage](#usage)
- [Deprecated: browserContext.setHTTPCredentials()](#deprecated-browsercontextsethttpcredentials)
- [In playwright.config.ts](#in-playwrightconfigts)
- [Complete example](#complete-example)
- [Manifest](#manifest)

## Status

`Credentials` / `HTTPCredentials` is not a Playwright class object of its own with
instance methods, but a configuration interface that is passed as an option when
creating a `BrowserContext`.

The page `https://playwright.dev/docs/api/class-credentials` does not exist in
the current Playwright docs. HTTP credentials are documented as an interface type in
`BrowserContext.newPage()` / `browser.newContext()`.

---

## HTTPCredentials interface

```typescript
interface HTTPCredentials {
  username: string;
  password: string;
  origin?: string;
  send?: 'always' | 'unauthorized';
}
```

### Properties

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `username` | `string` | yes | — | HTTP basic auth user name |
| `password` | `string` | yes | — | HTTP basic auth password |
| `origin` | `string` | no | — | Restriction to a particular origin (e.g. `'https://example.com'`). When specified, credentials are only sent for this origin. |
| `send` | `'always' \| 'unauthorized'` | no | `'unauthorized'` | `'always'`: send credentials with every request. `'unauthorized'`: only on HTTP 401 responses. |

---

## Usage

### On context creation

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'admin',
    password: 'secretpassword'
  }
});
```

### With origin restriction

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'user',
    password: 'pass',
    origin: 'https://staging.example.com'
  }
});
```

### Always send (pre-emptive auth)

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'api-user',
    password: 'token123',
    send: 'always'
  }
});
```

---

## Deprecated: browserContext.setHTTPCredentials()

The method `browserContext.setHTTPCredentials()` is deprecated:

```javascript
// DO NOT USE ANY MORE:
await context.setHTTPCredentials({ username: 'user', password: 'pass' });

// Instead: create a new context
const context = await browser.newContext({
  httpCredentials: { username: 'user', password: 'pass' }
});
```

**Note:** Browsers may cache credentials after successful authentication.
Playwright therefore recommends creating a
new BrowserContext for each test that uses different credentials.

---

## In playwright.config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    httpCredentials: {
      username: process.env.AUTH_USER!,
      password: process.env.AUTH_PASSWORD!
    }
  }
});
```

---

## Complete example

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();

// Context with HTTP basic auth for all requests
const context = await browser.newContext({
  httpCredentials: {
    username: 'testuser',
    password: 's3cr3t',
    origin: 'https://protected.example.com',
    send: 'always'
  }
});

const page = await context.newPage();
await page.goto('https://protected.example.com/dashboard');
// Page should load without a login dialog

await context.close();
await browser.close();
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 0 (interface, not a class object) |
| Properties | 4 (username, password, origin, send) |
| Events    | 0      |

**Conclusion:** `HTTPCredentials` is a pure configuration interface for
HTTP basic auth — not a class with instance methods. Configuration happens
once when creating the BrowserContext. For advanced authentication
(OAuth, cookie-based, session storage) Playwright offers the `storageState`
option as an alternative.

---

*Note: https://playwright.dev/docs/api/class-credentials does not exist in
the current stable Playwright docs. Reference: https://playwright.dev/docs/api/class-browser#browser-new-context*
