# Playwright Evaluating, Handles und Events - Vollstaendige Referenz

---

## 1. page.evaluate()

Fuehrt eine Funktion im Browser-Kontext aus und gibt das serialisierte Ergebnis
an den Test-Kontext zurueck.

```typescript
evaluate(pageFunction: Function | string, arg?: any): Promise<any>
```

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `pageFunction` | `Function \| string` | Funktion oder JS-String zur Ausfuehrung im Browser |
| `arg` | `Serializable \| JSHandle` | Einziger Argument-Wert (komplexe Daten als Objekt/Array) |

**Wichtig:** Promises werden automatisch aufgeloest. Die Funktion laeuft im
Browser-Prozess, nicht im Test-Prozess - Variablen aus dem Test-Scope sind
NICHT direkt zugaenglich.

```typescript
// Einfacher Zugriff auf Browser-APIs
const href = await page.evaluate(() => document.location.href);
const title = await page.evaluate(() => document.title);

// Async-Funktion
const status = await page.evaluate(async () => {
  const response = await fetch('/api/health');
  return response.status;
});

// Argument uebergeben (serialisierbarer Wert)
const doubled = await page.evaluate(n => n * 2, 21); // 42

// Objekt-Argument
const result = await page.evaluate(({ a, b }) => a + b, { a: 10, b: 20 });

// Array-Argument
const sum = await page.evaluate(([a, b]) => a + b, [10, 20]);

// DOM-Manipulation
await page.evaluate(() => {
  document.querySelector('#banner')?.remove();
});
```

---

## 2. page.evaluateHandle()

Wie `evaluate()`, gibt aber einen `JSHandle` zurueck statt des serialisierten
Werts. Verwendbar wenn das Ergebnis nicht serialisierbar ist oder direkt
weitergegeben werden soll.

```typescript
evaluateHandle(pageFunction: Function | string, arg?: any): Promise<JSHandle>
```

```typescript
// Window-Objekt als Handle
const windowHandle = await page.evaluateHandle('window');

// DOM-Element als Handle
const bodyHandle = await page.evaluateHandle(() => document.body);

// Komplexes Objekt (Map, Set etc.)
const mapHandle = await page.evaluateHandle(() => new Map([['a', 1], ['b', 2]]));
```

---

## 3. Argument-Uebergabe an evaluate

Nur ein Argument wird unterstuetzt. Fuer mehrere Werte: Objekt oder Array nutzen.

### Unterstuetzte Typen

| Typ | Beispiel |
|-----|---------|
| Primitive | `42`, `'string'`, `true`, `null` |
| Arrays | `[1, 2, 3]` |
| Plain Objects | `{ key: 'value' }` |
| `JSHandle` | Von `evaluateHandle()` zurueckgegeben |
| Gemischt | Objekt/Array aus Primitives + Handles |

```typescript
// FALSCH: Variable aus Test-Scope ist nicht sichtbar
const value = 42;
const result = await page.evaluate(() => value); // ReferenceError!

// RICHTIG: Als Argument uebergeben
const result = await page.evaluate(v => v, value);

// Handle als Argument
const buttonHandle = await page.evaluateHandle(() => document.querySelector('button'));
const text = await page.evaluate(btn => btn.textContent, buttonHandle);
await buttonHandle.dispose();

// Mehrere Handles in Objekt
const btn1 = await page.evaluateHandle(() => document.getElementById('btn1'));
const btn2 = await page.evaluateHandle(() => document.getElementById('btn2'));
const combined = await page.evaluate(
  ({ b1, b2 }) => b1.textContent + ' | ' + b2.textContent,
  { b1: btn1, b2: btn2 }
);
await btn1.dispose();
await btn2.dispose();

// Handle mit eigenem evaluate
const text = await buttonHandle.evaluate(
  (el, from) => el.textContent?.substring(from),
  5
);
```

---

## 4. JSHandle

Referenz auf ein JavaScript-Objekt im Browser-Prozess.

### Methoden

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `jsHandle.evaluate(fn, arg?)` | `Promise<any>` | Funktion mit Handle als erstem Arg ausfuehren |
| `jsHandle.evaluateHandle(fn, arg?)` | `Promise<JSHandle>` | Wie evaluate, gibt Handle zurueck |
| `jsHandle.getProperties()` | `Promise<Map<string, JSHandle>>` | Alle Properties als Map von Handles |
| `jsHandle.getProperty(name)` | `Promise<JSHandle>` | Einzelne Property als Handle |
| `jsHandle.jsonValue()` | `Promise<any>` | Serialisierten Wert des Handles holen |
| `jsHandle.asElement()` | `ElementHandle \| null` | Als ElementHandle (wenn DOM-Element) |
| `jsHandle.dispose()` | `Promise<void>` | Handle und referenziertes Objekt freigeben |

```typescript
// Array-Groesse ohne Serialisierung pruefen
const arrayHandle = await page.evaluateHandle(() => {
  window.myArray = [1, 2, 3];
  return window.myArray;
});
const length = await page.evaluate(arr => arr.length, arrayHandle);

// Element-Manipulation ueber Handle
await page.evaluate(arr => arr.push(4), arrayHandle);

// Properties eines Objekts durchgehen
const propsMap = await arrayHandle.getProperties();
for (const [key, prop] of propsMap) {
  console.log(key, await prop.jsonValue());
  await prop.dispose();
}

await arrayHandle.dispose();
```

---

## 5. ElementHandle

Spezialisierter `JSHandle` fuer DOM-Elemente. **Empfehlung:** Locator
bevorzugen - ElementHandle wird nach Navigationen stale.

### Methoden

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `elementHandle.boundingBox()` | `Promise<{x,y,width,height} \| null>` | Position und Groesse |
| `elementHandle.getAttribute(name)` | `Promise<string \| null>` | Attributwert |
| `elementHandle.innerHTML()` | `Promise<string>` | Inner HTML |
| `elementHandle.innerText()` | `Promise<string>` | Inner Text |
| `elementHandle.textContent()` | `Promise<string \| null>` | Text Content |
| `elementHandle.inputValue()` | `Promise<string>` | Wert von input/select/textarea |
| `elementHandle.isVisible()` | `Promise<boolean>` | Sichtbarkeit |
| `elementHandle.isEnabled()` | `Promise<boolean>` | Aktivierungszustand |
| `elementHandle.isChecked()` | `Promise<boolean>` | Checkbox-Zustand |
| `elementHandle.click(options?)` | `Promise<void>` | Klick ausloesen |
| `elementHandle.fill(value)` | `Promise<void>` | Formularfeld benoetigt |
| `elementHandle.$(selector)` | `Promise<ElementHandle \| null>` | Kind-Element finden |
| `elementHandle.$$(selector)` | `Promise<ElementHandle[]>` | Kind-Elemente finden |
| `elementHandle.$eval(selector, fn)` | `Promise<any>` | Kind evaluieren |
| `elementHandle.$$eval(selector, fn)` | `Promise<any>` | Kinder evaluieren |
| `elementHandle.waitForSelector(sel, opts?)` | `Promise<ElementHandle>` | Auf Kind warten |
| `elementHandle.asElement()` | `ElementHandle` | Sich selbst zurueckgeben |
| `elementHandle.dispose()` | `Promise<void>` | Freigeben |

```typescript
// ElementHandle erstellen (nur wenn wirklich noetig)
const el = await page.waitForSelector('#container');
const box = await el.boundingBox();
console.log(`Position: ${box?.x}, ${box?.y}`);

// Mit evaluate
const text = await el.evaluate(node => node.textContent);

// Als Locator bevorzugt
const locator = page.locator('#container');
await expect(locator).toBeVisible();
```

---

## 6. addInitScript

Fuehrt Code vor jedem Page-Load aus (auch nach Navigationen).

### page.addInitScript(script, arg?)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `script` | `Function \| string \| {path: string, content: string}` | Auszufuehrendes Script |
| `arg` | `Serializable` | Argument fuer Script-Funktion |

```typescript
// Funktion mit Argument
await page.addInitScript(seed => {
  Math.random = () => seed;
}, 0.42);

// Aus Datei laden
await page.addInitScript({ path: './mocks/preload.js' });

// Als String
await page.addInitScript('window.__TEST__ = true;');

// beforeEach typisches Pattern
test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => {
    // Globale Mock-Variablen setzen
    (window as any).__MOCK_USER__ = { id: 1, role: 'admin' };
  });
});
```

### context.addInitScript(script, arg?)

Gilt fuer alle Pages im Context (auch neu geoeffnete).

```typescript
await context.addInitScript(() => {
  // Gilt fuer alle Pages dieses Contexts
  window.__ENV__ = 'test';
});
```

---

## 7. page.exposeFunction

Macht eine Node.js-Funktion im Browser-Kontext aufrufbar.

```typescript
exposeFunction(name: string, callback: Function): Promise<void>
```

```typescript
// Funktion exponieren
await page.exposeFunction('sha256', async (text: string) => {
  const { createHash } = await import('crypto');
  return createHash('sha256').update(text).digest('hex');
});

// Im Browser aufrufbar
const hash = await page.evaluate(async () => {
  return await window.sha256('hello world');
});

// Typische Verwendung: Logging aus Browser zum Test leiten
const logs: string[] = [];
await page.exposeFunction('recordLog', (msg: string) => {
  logs.push(msg);
});
await page.evaluate(() => {
  console.log = (msg: string) => window.recordLog(msg);
});
```

---

## 8. Events

### page.waitForEvent(event, options?)

Wartet auf ein einzelnes Event-Vorkommen.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `event` | `string` | Event-Name |
| `optionOrPredicate` | `Function \| {predicate?, timeout?}` | Filterfunktion oder Options-Objekt |

```typescript
// Popup abfangen
const popupPromise = page.waitForEvent('popup');
await page.click('#open-popup');
const popup = await popupPromise;
await popup.waitForLoadState();

// Mit Praedikat
const downloadPromise = page.waitForEvent('download', {
  predicate: download => download.suggestedFilename().endsWith('.pdf'),
  timeout: 10000,
});
await page.click('#export-pdf');
const download = await downloadPromise;

// Gleichzeitig auf Navigation und Event warten
const [response, request] = await Promise.all([
  page.waitForEvent('response'),
  page.waitForRequest(/\/api\//),
  page.click('#submit'),
]);
```

### page.on(event, handler)

Dauerhaftes Event-Listening.

```typescript
// Request/Response protokollieren
page.on('request', (request) => {
  console.log(`>> ${request.method()} ${request.url()}`);
});
page.on('response', (response) => {
  console.log(`<< ${response.status()} ${response.url()}`);
});

// Fehler abfangen
page.on('pageerror', (err) => {
  console.error('Page error:', err.message);
});
page.on('console', (msg) => {
  if (msg.type() === 'error') console.error('Console error:', msg.text());
});

// Worker-Events
page.on('worker', (worker) => {
  console.log('Worker created:', worker.url());
});
```

### page.once(event, handler)

Einmaliger Handler (wird nach erstem Auftreten automatisch entfernt).

```typescript
// Dialog einmalig akzeptieren
page.once('dialog', dialog => dialog.accept('test input'));
await page.evaluate("prompt('Name:')");

// Naechsten Request abfangen
page.once('request', request => {
  console.log('Next request:', request.url());
});
```

### page.off(event, handler)

Handler entfernen.

```typescript
const handler = (request: Request) => console.log(request.url());
page.on('request', handler);
await page.goto('/some-page');
page.off('request', handler); // Nicht mehr aktiv
```

---

## 9. Verfuegbare Page-Events

| Event | Callback-Parameter | Beschreibung |
|-------|--------------------|--------------|
| `'close'` | `Page` | Seite geschlossen |
| `'console'` | `ConsoleMessage` | console.*-Aufruf |
| `'crash'` | `Page` | Seite abgestuerzt |
| `'dialog'` | `Dialog` | alert/confirm/prompt |
| `'domcontentloaded'` | `Page` | DOMContentLoaded |
| `'download'` | `Download` | Download gestartet |
| `'filechooser'` | `FileChooser` | Datei-Dialog geoeffnet |
| `'frameattached'` | `Frame` | Frame hinzugefuegt |
| `'framedetached'` | `Frame` | Frame entfernt |
| `'framenavigated'` | `Frame` | Frame navigiert |
| `'load'` | `Page` | Load-Event |
| `'pageerror'` | `Error` | Uncaught Exception |
| `'popup'` | `Page` | Popup geoeffnet |
| `'request'` | `Request` | Anfrage gesendet |
| `'requestfailed'` | `Request` | Anfrage fehlgeschlagen |
| `'requestfinished'` | `Request` | Anfrage abgeschlossen |
| `'response'` | `Response` | Antwort erhalten |
| `'websocket'` | `WebSocket` | WebSocket geoeffnet |
| `'worker'` | `Worker` | Worker erstellt |

---

## 10. context.exposeFunction

Wie `page.exposeFunction`, gilt fuer alle Pages im Context.

```typescript
await context.exposeFunction('testHelper', () => ({
  mockDate: new Date('2024-01-01'),
  userId: 42,
}));
```

---

## 11. Locator vs. ElementHandle

| Aspekt | Locator | ElementHandle |
|--------|---------|---------------|
| Referenz | Lazy (neu aufgeloest bei jeder Verwendung) | Fest (wird stale nach Navigation) |
| Navigation | Sicher | Kann stale werden |
| Auto-Wait | Ja | Nein |
| Empfehlung | Bevorzugen | Nur in Ausnahmen |

```typescript
// BEVORZUGT: Locator
const button = page.locator('#submit');
await expect(button).toBeVisible();
await button.click();

// NUR wenn noetig: ElementHandle
const handle = await page.waitForSelector('#lazy-element');
const bbox = await handle.boundingBox();
await handle.dispose();
```

---

Quelle: https://playwright.dev/docs/evaluating | https://playwright.dev/docs/handles | https://playwright.dev/docs/events
