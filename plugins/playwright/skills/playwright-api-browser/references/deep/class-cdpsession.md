# class-cdpsession

`CDPSession` ermoeglicht die direkte Kommunikation ueber das Chrome DevTools Protocol (CDP). Damit koennen rohe CDP-Befehle gesendet und CDP-Events abonniert werden, die nicht Teil der hoeheren Playwright-API sind.

Erstellt via: `browser.newBrowserCDPSession()`, `browserContext.newCDPSession(page)`, `page.context().newCDPSession(page)`.

**Hinweis:** Nur Chromium-basierte Browser (Chrome, Edge) unterstuetzen CDP.

Methoden: 2 | Properties: 0 | Events: 2

---

## Methods

### cdpSession.detach()

```ts
await cdpSession.detach(): Promise<void>
```

Trennt die CDP-Session vom Ziel. Nach dem Trennen werden keine weiteren Events mehr emittiert und Methoden-Aufrufe werfen Exceptions.

**Returns:** `Promise<void>`

```js
await cdpSession.detach();
```

---

### cdpSession.send(method[, params])

```ts
await cdpSession.send(method[, params]): Promise<Object>
```

Sendet einen CDP-Befehl und gibt die Antwort als Objekt zurueck.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `method` | string | Yes | — | CDP-Methodenname, z.B. `"Network.enable"`, `"DOM.getDocument"` |
| `params` | Object | No | — | Methodenspezifische Parameter gemaess CDP-Spezifikation |

**Returns:** `Promise<Object>` — Antwort-Objekt gemaess CDP-Spezifikation

```js
// CDP-Session an einer Page erstellen
const client = await page.context().newCDPSession(page);

// Network-Monitoring aktivieren
await client.send('Network.enable');

// Performance-Metriken abrufen
const { metrics } = await client.send('Performance.getMetrics');
console.log(metrics);

// Animationsrate abfragen
const { currentPlaybackRate } = await client.send('Animation.getPlaybackRate');

// Coverage aktivieren
await client.send('CSS.startRuleUsageTracking');
// ... Seite navigieren ...
const { ruleUsage } = await client.send('CSS.stopRuleUsageTracking');

// DOM-Dokument abrufen
const { root } = await client.send('DOM.getDocument', { depth: 1 });

// Emulation: Netzwerk-Bedingungen setzen
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

Wird ausgeloest wenn die CDP-Session geschlossen wird, entweder durch das Schliessen des Ziels oder durch expliziten `detach()`-Aufruf.

**Event data:** `CDPSession` — die Session selbst

```js
cdpSession.on('close', (session) => {
  console.log('CDP Session geschlossen');
});
```

---

### event: 'event'

Wird fuer alle eingehenden CDP-Events ausgeloest. Ermoeglicht das generische Abonnieren ohne explizite Event-Namen zu kennen.

**Event data:** Object mit:

| Field | Type | Description |
|-------|------|-------------|
| `method` | string | CDP-Event-Bezeichner, z.B. `"Network.requestWillBeSent"` |
| `params` | Object | Event-spezifische Daten |

```js
cdpSession.on('event', ({ method, params }) => {
  console.log('CDP Event:', method, params);
});
```

---

## Typische CDP-Anwendungsfaelle

```js
// Browser-Level Session (kein Page-Target)
const browserSession = await browser.newBrowserCDPSession();
const { browserContextIds } = await browserSession.send('Target.getBrowserContexts');
console.log('Contexts:', browserContextIds);

// Network-Events abhoeren
const client = await page.context().newCDPSession(page);
await client.send('Network.enable');
client.on('event', ({ method, params }) => {
  if (method === 'Network.responseReceived') {
    console.log('Response:', params.response.url, params.response.status);
  }
});

// JavaScript-Profiling
await client.send('Profiler.enable');
await client.send('Profiler.start');
await page.goto('https://example.com');
const { profile } = await client.send('Profiler.stop');
require('fs').writeFileSync('profile.json', JSON.stringify(profile));

// Aufraumen
await client.detach();
```

---

## CDP-Ressourcen

Die vollstaendige CDP-API-Dokumentation (alle Domaenen und Methoden):
- Chrome: https://chromedevtools.github.io/devtools-protocol/
- Domänen: `Animation`, `Browser`, `CSS`, `DOM`, `Debugger`, `Emulation`, `Input`, `Network`, `Page`, `Performance`, `Profiler`, `Runtime`, `Security`, `ServiceWorker`, `Storage`, `Target`, `Tracing`, u.v.m.

---

## Manifest

| Category | Count |
|----------|-------|
| Methods | 2 |
| Properties | 0 |
| Events | 2 |

**Fazit:** `CDPSession` ist ein Low-Level-Escape-Hatch fuer Chromium-spezifische Funktionen, die Playwright nicht nativ abdeckt. `send()` ist die einzige relevante Methode; die CDP-Methodennamen kommen aus der Chrome DevTools Protocol-Spezifikation. Fuer Standard-Tests sollten immer die hoeheren Playwright-Abstraktionen bevorzugt werden.

---

Source: https://playwright.dev/docs/api/class-cdpsession
