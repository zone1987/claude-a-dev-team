# class-cdpsession

`CDPSession` enables direct communication over the Chrome DevTools Protocol (CDP). It allows sending raw CDP commands and subscribing to CDP events that are not part of the higher-level Playwright API.

Created via: `browser.newBrowserCDPSession()`, `browserContext.newCDPSession(page)`, `page.context().newCDPSession(page)`.

**Note:** Only Chromium-based browsers (Chrome, Edge) support CDP.

Methods: 2 | Properties: 0 | Events: 2

---

## Contents

- [Methods](#methods)
- [Events](#events)
- [Typical CDP Use Cases](#typical-cdp-use-cases)
- [CDP Resources](#cdp-resources)
- [Manifest](#manifest)

## Methods

### cdpSession.detach()

```ts
await cdpSession.detach(): Promise<void>
```

Detaches the CDP session from the target. After detaching, no further events are emitted and method calls throw exceptions.

**Returns:** `Promise<void>`

```js
await cdpSession.detach();
```

---

### cdpSession.send(method[, params])

```ts
await cdpSession.send(method[, params]): Promise<Object>
```

Sends a CDP command and returns the response as an object.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `method` | string | Yes | — | CDP method name, e.g. `"Network.enable"`, `"DOM.getDocument"` |
| `params` | Object | No | — | Method-specific parameters according to the CDP specification |

**Returns:** `Promise<Object>` — response object according to the CDP specification

```js
// Create a CDP session on a page
const client = await page.context().newCDPSession(page);

// Enable network monitoring
await client.send('Network.enable');

// Retrieve performance metrics
const { metrics } = await client.send('Performance.getMetrics');
console.log(metrics);

// Query the animation rate
const { currentPlaybackRate } = await client.send('Animation.getPlaybackRate');

// Enable coverage
await client.send('CSS.startRuleUsageTracking');
// ... navigate the page ...
const { ruleUsage } = await client.send('CSS.stopRuleUsageTracking');

// Retrieve the DOM document
const { root } = await client.send('DOM.getDocument', { depth: 1 });

// Emulation: set network conditions
await client.send('Network.emulateNetworkConditions', {
  offline: false,
  downloadThroughput: (1.5 * 1024 * 1024) / 8,
  uploadThroughput: (750 * 1024) / 8,
  latency: 40,
});
```

---

## Events

### event: 'close'

Emitted when the CDP session is closed, either by closing the target or by an explicit `detach()` call.

**Event data:** `CDPSession` — the session itself

```js
cdpSession.on('close', (session) => {
  console.log('CDP Session closed');
});
```

---

### event: 'event'

Emitted for all incoming CDP events. Allows generic subscription without knowing explicit event names.

**Event data:** Object with:

| Field | Type | Description |
|-------|------|-------------|
| `method` | string | CDP event identifier, e.g. `"Network.requestWillBeSent"` |
| `params` | Object | Event-specific data |

```js
cdpSession.on('event', ({ method, params }) => {
  console.log('CDP Event:', method, params);
});
```

---

## Typical CDP Use Cases

```js
// Browser-level session (no page target)
const browserSession = await browser.newBrowserCDPSession();
const { browserContextIds } = await browserSession.send('Target.getBrowserContexts');
console.log('Contexts:', browserContextIds);

// Listen to network events
const client = await page.context().newCDPSession(page);
await client.send('Network.enable');
client.on('event', ({ method, params }) => {
  if (method === 'Network.responseReceived') {
    console.log('Response:', params.response.url, params.response.status);
  }
});

// JavaScript profiling
await client.send('Profiler.enable');
await client.send('Profiler.start');
await page.goto('https://example.com');
const { profile } = await client.send('Profiler.stop');
require('fs').writeFileSync('profile.json', JSON.stringify(profile));

// Clean up
await client.detach();
```

---

## CDP Resources

The complete CDP API documentation (all domains and methods):
- Chrome: https://chromedevtools.github.io/devtools-protocol/
- Domains: `Animation`, `Browser`, `CSS`, `DOM`, `Debugger`, `Emulation`, `Input`, `Network`, `Page`, `Performance`, `Profiler`, `Runtime`, `Security`, `ServiceWorker`, `Storage`, `Target`, `Tracing`, and many more.

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 2 |
| Properties | 0 |
| Events | 2 |

**Conclusion:** `CDPSession` is a low-level escape hatch for Chromium-specific features that Playwright does not cover natively. `send()` is the only relevant method; the CDP method names come from the Chrome DevTools Protocol specification. For standard tests, the higher-level Playwright abstractions should always be preferred.

---

Source: https://playwright.dev/docs/api/class-cdpsession
