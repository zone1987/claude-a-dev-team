# Playwright class-jshandle: Vollstaendige API-Referenz

`JSHandle` repraesentiert einen Verweis auf ein JavaScript-Objekt im Browser-Kontext.
Es ermoeglicht den Zugriff auf JavaScript-Objekte, die nicht JSON-serialisierbar sind
(z.B. `window`, DOM-Elemente, komplexe Objekte).

`JSHandle` wird zurueckgegeben von:
- `page.evaluateHandle()`
- `frame.evaluateHandle()`
- `jsHandle.evaluateHandle()`
- `jsHandle.getProperty()`
- `jsHandle.getProperties()` (Map-Werte)
- `page.waitForFunction()`
- `frame.waitForFunction()`

`ElementHandle` ist eine Unterklasse von `JSHandle` und erbt alle hier dokumentierten Methoden.

---

## Inhaltsverzeichnis

1. [asElement()](#1-aselement)
2. [dispose()](#2-dispose)
3. [evaluate()](#3-evaluate)
4. [evaluateHandle()](#4-evaluatehandle)
5. [getProperties()](#5-getproperties)
6. [getProperty()](#6-getproperty)
7. [jsonValue()](#7-jsonvalue)
8. [Typische Verwendungsszenarien](#8-typische-verwendungsszenarien)
9. [Manifest](#9-manifest)

---

## 1. asElement()

```typescript
jsHandle.asElement(): null | ElementHandle
```

**Parameter:** Keine

**Rueckgabe:** `ElementHandle` wenn das Handle ein DOM-Element repraesentiert, sonst `null`.

Ermoeglicht sicheres Casting eines `JSHandle` zu `ElementHandle`.

```typescript
// Aus evaluateHandle gewonnenes Handle pruefen
const handle = await page.evaluateHandle(() => document.querySelector('h1'));
const elementHandle = handle.asElement();

if (elementHandle) {
  // Ist ein DOM-Element
  const text = await elementHandle.textContent();
  console.log('Titel:', text);
  const box = await elementHandle.boundingBox();
  console.log('Position:', box);
} else {
  // Kein DOM-Element (z.B. primitiver Wert oder komplexes Objekt)
  const value = await handle.jsonValue();
  console.log('Wert:', value);
}

// Unterschied zu ElementHandle.asElement():
// ElementHandle.asElement() gibt immer sich selbst zurueck
// JSHandle.asElement() gibt null zurueck wenn kein DOM-Element
```

---

## 2. dispose()

```typescript
jsHandle.dispose(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

Gibt das JavaScript-Objekt-Handle frei. Das Browser-seitige Objekt wird nicht mehr von Playwright
referenziert und kann vom Garbage Collector abgeraeumt werden. Nach `dispose()` sind keine
weiteren Operationen auf dem Handle moeglich — sie wuerfeln einen Fehler.

```typescript
const handle = await page.evaluateHandle(() => window);
// Arbeit mit handle...
const userAgent = await handle.evaluate(win => win.navigator.userAgent);
console.log(userAgent);
// Handle freigeben wenn nicht mehr benoetigt
await handle.dispose();

// Handles in Arrays/Maps ebenfalls bereinigen
const propsMap = await handle.getProperties();
for (const [key, propHandle] of propsMap) {
  await propHandle.dispose();
}
```

---

## 3. evaluate()

```typescript
jsHandle.evaluate<T>(
  pageFunction: ((handle: Handle, arg?: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pageFunction` | `Function\|string` | ja | Funktion die im Browser ausgefuehrt wird; das Handle wird als erstes Argument uebergeben |
| `arg` | `Serializable\|JSHandle` | nein | Optionales zweites Argument |

**Rueckgabe:** `Promise<T>` — serialisierter JSON-Wert. Nicht-JSON-faehige Werte werden zu `undefined`.

Fuehrt eine Funktion im Browser-Kontext aus und uebergibt das Handle als erstes Argument.
Ideal fuer Operationen auf JavaScript-Objekten, die nicht direkt serialisierbar sind.

```typescript
// window-Objekt analysieren
const windowHandle = await page.evaluateHandle(() => window);
const url = await windowHandle.evaluate(win => win.location.href);
const scrollY = await windowHandle.evaluate(win => win.scrollY);

// Array-Handle auswerten
const arrayHandle = await page.evaluateHandle(() =>
  Array.from(document.querySelectorAll('a'))
);
const count = await arrayHandle.evaluate(arr => arr.length);
const firstHref = await arrayHandle.evaluate(arr => arr[0]?.getAttribute('href'));

// Mit Zusatz-Argument
const threshold = 5;
const longLinks = await arrayHandle.evaluate(
  (links, minLen) => links.filter(a => a.textContent!.length > minLen).length,
  threshold
);

// Map-Objekt
const mapHandle = await page.evaluateHandle(() => new Map([['key', 'value']]));
const hasKey = await mapHandle.evaluate(m => m.has('key'));
```

---

## 4. evaluateHandle()

```typescript
jsHandle.evaluateHandle<T>(
  pageFunction: ((handle: Handle, arg?: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pageFunction` | `Function\|string` | ja | Funktion die im Browser ausgefuehrt wird; das Handle als erstes Argument |
| `arg` | `Serializable\|JSHandle` | nein | Optionales zweites Argument |

**Rueckgabe:** `Promise<JSHandle<T>>` — ein neues Handle auf das Rueckgabe-Objekt.

Wie `evaluate()`, aber gibt ein `JSHandle` statt eines serialisierten Werts zurueck.
Nuetzlich wenn der Rueckgabewert selbst komplex/nicht-serialisierbar ist oder fuer Chaining.

```typescript
// Element aus Array-Handle extrahieren
const listHandle = await page.evaluateHandle(() =>
  document.querySelectorAll('li')
);
// Erstes Element als neues Handle
const firstHandle = await listHandle.evaluateHandle(list => list[0]);
const elementHandle = firstHandle.asElement();
if (elementHandle) {
  const text = await elementHandle.textContent();
}

// Kindelement traversieren
const bodyHandle = await page.evaluateHandle(() => document.body);
const headerHandle = await bodyHandle.evaluateHandle(body => body.querySelector('header'));
const headerEl = headerHandle.asElement();

// window.history navigieren und als Handle behalten
const historyHandle = await page.evaluateHandle(() => window.history);
const stateHandle = await historyHandle.evaluateHandle(h => h.state);

// Sauber aufraumen
await listHandle.dispose();
await firstHandle.dispose();
await bodyHandle.dispose();
await headerHandle.dispose();
await historyHandle.dispose();
await stateHandle.dispose();
```

---

## 5. getProperties()

```typescript
jsHandle.getProperties(): Promise<Map<string, JSHandle>>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<Map<string, JSHandle>>` — Map mit Eigenschaftsnamen als Schluesseln
und JSHandle-Instanzen als Werten.

Gibt alle **eigenen** (nicht-vererbten) Eigenschaften des referenzierten Objekts zurueck.
Jede Eigenschaft ist selbst ein JSHandle.

```typescript
// Alle eigenen Eigenschaften eines Objekts
const handle = await page.evaluateHandle(() => ({ name: 'Max', age: 30, active: true }));
const props = await handle.getProperties();

for (const [key, valueHandle] of props) {
  const value = await valueHandle.jsonValue();
  console.log(`${key}: ${value}`);
  await valueHandle.dispose();
}
await handle.dispose();
// Ausgabe:
// name: Max
// age: 30
// active: true

// DOM-Element-Eigenschaften
const inputHandle = await page.evaluateHandle(() => document.querySelector('input'));
const inputProps = await inputHandle.getProperties();
const valueHandle = inputProps.get('value');
if (valueHandle) {
  const value = await valueHandle.jsonValue();
  console.log('Input value:', value);
  await valueHandle.dispose();
}

// Nur eigene Eigenschaften (keine Prototype-Eigenschaften)
const arrayHandle = await page.evaluateHandle(() => [1, 2, 3]);
const arrayProps = await arrayHandle.getProperties();
// Enthaelt '0', '1', '2', 'length' — aber NICHT Array.prototype-Methoden
```

---

## 6. getProperty()

```typescript
jsHandle.getProperty(propertyName: string): Promise<JSHandle>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `propertyName` | `string` | ja | Name der abzurufenden Eigenschaft |

**Rueckgabe:** `Promise<JSHandle>` — Handle auf den Eigenschaftswert.

Ruft eine einzelne Eigenschaft ab, ohne alle Eigenschaften zu laden.
Effizienter als `getProperties()` wenn nur eine Eigenschaft benoetigt wird.

```typescript
// Einfache Eigenschaft
const handle = await page.evaluateHandle(() => ({
  name: 'Max',
  address: { city: 'Berlin' }
}));

const nameHandle = await handle.getProperty('name');
const name = await nameHandle.jsonValue();
console.log('Name:', name); // 'Max'
await nameHandle.dispose();

// Verschachtelte Eigenschaft (ergibt Handle auf Objekt)
const addressHandle = await handle.getProperty('address');
const cityHandle = await addressHandle.getProperty('city');
const city = await cityHandle.jsonValue();
console.log('Stadt:', city); // 'Berlin'
await cityHandle.dispose();
await addressHandle.dispose();

await handle.dispose();

// Input-Wert lesen
const inputHandle = await page.evaluateHandle(() =>
  document.querySelector('input[name=email]')
);
const valueHandle = await inputHandle.getProperty('value');
const value = await valueHandle.jsonValue();
console.log('E-Mail:', value);

// Checked-Zustand einer Checkbox
const checkboxHandle = await page.evaluateHandle(() =>
  document.querySelector('input[type=checkbox]')
);
const checkedHandle = await checkboxHandle.getProperty('checked');
const checked = await checkedHandle.jsonValue();
console.log('Angehakt:', checked);

await valueHandle.dispose();
await inputHandle.dispose();
await checkedHandle.dispose();
await checkboxHandle.dispose();
```

---

## 7. jsonValue()

```typescript
jsHandle.jsonValue<T>(): Promise<T>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<T>` — JSON-Repraesentation des referenzierten Objekts.

Serialisiert das referenzierte JavaScript-Objekt als JSON. Wenn das Objekt eine `toJSON()`-
Methode hat, wird diese **nicht** aufgerufen. Zirkulaere Referenzen und nicht-serialisierbare
Werte (z.B. `undefined`, Funktionen, Symbols) werden ignoriert/entfernt.

Fuer DOM-Elemente gibt `jsonValue()` ein leeres Objekt `{}` zurueck — in diesem Fall
`evaluate()` oder `ElementHandle`-Methoden verwenden.

```typescript
// Primitive Werte
const numHandle = await page.evaluateHandle(() => 42);
const num = await numHandle.jsonValue();
console.log(num); // 42

const strHandle = await page.evaluateHandle(() => 'Hallo');
const str = await strHandle.jsonValue();
console.log(str); // 'Hallo'

// Arrays
const arrHandle = await page.evaluateHandle(() => [1, 2, 3, 'vier']);
const arr = await arrHandle.jsonValue();
console.log(arr); // [1, 2, 3, 'vier']

// Objekte
const objHandle = await page.evaluateHandle(() => ({
  user: 'Max',
  scores: [10, 20],
  active: true
}));
const obj = await objHandle.jsonValue();
console.log(obj.user); // 'Max'

// DOM-Element — gibt {} zurueck
const elHandle = await page.evaluateHandle(() => document.body);
const elJson = await elHandle.jsonValue();
console.log(elJson); // {}
// Stattdessen: elHandle.asElement()?.textContent()

// Nicht-serialisierbare Werte
const fnHandle = await page.evaluateHandle(() => function test() {});
const fnJson = await fnHandle.jsonValue();
console.log(fnJson); // undefined

// Aufraumen
await numHandle.dispose();
await strHandle.dispose();
await arrHandle.dispose();
await objHandle.dispose();
await elHandle.dispose();
await fnHandle.dispose();
```

---

## 8. Typische Verwendungsszenarien

### Szenario 1: Window-Objekt inspizieren

```typescript
const windowHandle = await page.evaluateHandle(() => window);

// Eigenschaften auslesen
const location = await windowHandle.evaluate(w => ({
  href: w.location.href,
  pathname: w.location.pathname,
  search: w.location.search
}));
console.log(location);

// Globale Variable pruefen
const appState = await windowHandle.evaluate(w => (w as any).__APP_STATE__);

await windowHandle.dispose();
```

---

### Szenario 2: NodeList / HTMLCollection verarbeiten

```typescript
// Alle Links als Handle
const linksHandle = await page.evaluateHandle(() =>
  document.querySelectorAll('a[href]')
);

// Anzahl
const count = await linksHandle.evaluate(links => links.length);

// Alle HREFs
const hrefs = await linksHandle.evaluate(links =>
  Array.from(links).map(a => (a as HTMLAnchorElement).href)
);

await linksHandle.dispose();
```

---

### Szenario 3: Komplexe Rueckgabewerte aus evaluate

```typescript
// Wenn evaluate nicht ausreicht (Objekt nicht JSON-faehig)
const setHandle = await page.evaluateHandle(() => new Set(['a', 'b', 'c']));
const size = await setHandle.evaluate(s => s.size);
const hasA = await setHandle.evaluate(s => s.has('a'));
const asArray = await setHandle.evaluate(s => Array.from(s));
console.log(asArray); // ['a', 'b', 'c']

await setHandle.dispose();
```

---

### Szenario 4: Handle-Chaining

```typescript
// Ohne Chaining (ineffizient — mehrere evaluate-Aufrufe)
const formHandle = await page.evaluateHandle(() =>
  document.querySelector('form#checkout')
);
const inputHandle = await formHandle.evaluateHandle(form =>
  form.querySelector('input[name=card]')
);
const inputEl = inputHandle.asElement();
if (inputEl) {
  await inputEl.fill('4111111111111111');
}

// Sauber aufraumen
await inputHandle.dispose();
await formHandle.dispose();
```

---

### Szenario 5: Memory-sichere Verwendung mit using

```typescript
// TypeScript 5+ Symbol.asyncDispose (falls Playwright-Version unterstuetzt)
{
  const handle = await page.evaluateHandle(() => window);
  try {
    const title = await handle.evaluate(w => w.document.title);
    console.log(title);
  } finally {
    await handle.dispose(); // Immer aufraumen
  }
}
```

---

## 9. Manifest

| Methode | Rueckgabe | Beschreibung |
|---|---|---|
| `asElement()` | `null \| ElementHandle` | Cast zu ElementHandle |
| `dispose()` | `Promise<void>` | Handle freigeben |
| `evaluate(fn, arg?)` | `Promise<T>` | Funktion mit Handle ausfuehren, serialisierten Wert zurueckgeben |
| `evaluateHandle(fn, arg?)` | `Promise<JSHandle>` | Funktion mit Handle ausfuehren, Handle zurueckgeben |
| `getProperties()` | `Promise<Map<string, JSHandle>>` | Alle eigenen Eigenschaften als Map |
| `getProperty(name)` | `Promise<JSHandle>` | Einzelne Eigenschaft als Handle |
| `jsonValue()` | `Promise<T>` | JSON-Serialisierung des referenzierten Objekts |

**Gesamt: 7 Methoden** (keine Properties, keine Events)

**Fazit:** `JSHandle` ist die Basis-Klasse fuer alle Browser-Objekt-Handles in Playwright.
Sie ermoeglicht das sichere Arbeiten mit nicht-serialisierbaren JavaScript-Werten im Browser.
Wichtig: Handles immer mit `dispose()` freigeben, um Memory-Leaks zu vermeiden.
In der Praxis wird `JSHandle` meist indirekt ueber `ElementHandle` und `page.evaluateHandle()`
verwendet — direktes `JSHandle`-Arbeiten ist vor allem bei komplexen Browser-Objekten
(Sets, Maps, Window, komplexe Klassen) notwendig.

---

**Quelle:** https://playwright.dev/docs/api/class-jshandle
