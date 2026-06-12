# Playwright — class: Worker

> **Manifest:** 4 Methoden, 0 Properties, 2 Events.
> Repraesentiert einen Web Worker oder Service Worker einer Seite.
> Instanzen werden ueber `page.on('worker')` oder `page.workers()` erhalten.

---

## Uebersicht

`Worker` bildet einen dedizierten Web Worker ab. Service Workers koennen
ueber `browserContext.serviceWorkers()` abgerufen werden. Worker-Instanzen
erlauben die Ausfuehrung von Code innerhalb des Worker-Kontexts sowie
das Abfragen der Worker-URL.

```javascript
page.on('worker', worker => {
  console.log('Worker gestartet:', worker.url());
});

page.on('workerdestroyed', worker => {
  console.log('Worker beendet:', worker.url());
});
```

---

## Methoden

### worker.evaluate(pageFunction, arg?)

Fuehrt eine Funktion im Worker-Kontext aus und gibt das Ergebnis als
serialisierten Wert zurueck.

**Signatur:**
```typescript
worker.evaluate<R>(
  pageFunction: Function | string,
  arg?: any
): Promise<R>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `pageFunction` | `Function \| string` | ja | — | Funktion oder JS-String, der im Worker-Kontext ausgefuehrt wird |
| `arg` | `EvaluationArgument` | nein | — | Optionales Argument, das an `pageFunction` uebergeben wird. Muss JSON-serialisierbar sein oder ein JSHandle. |

**Rueckgabe:** `Promise<R>` — serialisierter Rueckgabewert (JSON-kompatible Typen)

**Besondere Werte:** `NaN`, `Infinity`, `-0` und `undefined` werden korrekt
behandelt.

**Beispiel:**
```javascript
const workerValue = await worker.evaluate(() => {
  return { workerType: 'dedicated', navigator: navigator.userAgent };
});
console.log(workerValue);
```

---

### worker.evaluateHandle(pageFunction, arg?)

Wie `evaluate()`, gibt aber ein `JSHandle` statt eines serialisierten Werts
zurueck. Geeignet fuer nicht-serialisierbare Worker-Objekte.

**Signatur:**
```typescript
worker.evaluateHandle<R>(
  pageFunction: Function | string,
  arg?: any
): Promise<JSHandle<R>>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `pageFunction` | `Function \| string` | ja | — | Funktion oder JS-String |
| `arg` | `EvaluationArgument` | nein | — | Optionales Argument |

**Rueckgabe:** `Promise<JSHandle>` — Handle auf den Worker-Wert

**Beispiel:**
```javascript
const handle = await worker.evaluateHandle(() => globalThis);
const keys = await handle.getProperties();
```

---

### worker.url()

Gibt die URL des Worker-Skripts zurueck.

**Signatur:**
```typescript
worker.url(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — vollstaendige URL des Worker-Skripts

**Beispiel:**
```javascript
console.log('Worker-URL:', worker.url());
// z.B. "https://example.com/workers/background.js"
```

---

### worker.waitForEvent(event, optionsOrPredicate?)

Wartet darauf, dass ein bestimmtes Event auf dem Worker-Objekt gefeuert wird.

**Signatur:**
```typescript
worker.waitForEvent(
  event: string,
  optionsOrPredicate?: Function | {
    predicate?: Function;
    timeout?: number;
  }
): Promise<any>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `event` | `string` | ja | — | Event-Name (z.B. `'close'`, `'console'`) |
| `optionsOrPredicate` | `Function \| Object` | nein | — | Filterfunktion oder Options-Objekt |
| `optionsOrPredicate.predicate` | `Function` | nein | — | Filtert Events; gibt `true` zurueck wenn das Event akzeptiert werden soll |
| `optionsOrPredicate.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms (`0` = kein Timeout) |

**Rueckgabe:** `Promise<any>` — der Event-Payload

**Beispiel:**
```javascript
const closeEvent = await worker.waitForEvent('close');
console.log('Worker geschlossen');
```

---

## Events

### worker.on('close')

Wird gefeuert, wenn dieser dedizierte Web Worker beendet wird.

**Event-Payload:** `Worker` — das Worker-Objekt selbst

**Beispiel:**
```javascript
worker.on('close', (w) => {
  console.log('Worker beendet:', w.url());
});
```

---

### worker.on('console')

Wird gefeuert, wenn JavaScript im Worker `console`-API-Methoden aufruft
(z.B. `console.log`, `console.dir`).

**Event-Payload:** `ConsoleMessage`

**Hinzugefuegt:** v1.57

**Beispiel:**
```javascript
worker.on('console', msg => {
  console.log(`[Worker ${worker.url()}] [${msg.type()}] ${msg.text()}`);
});
```

---

## Worker-Zugriff ueber Page

```javascript
// Alle aktiven Worker einer Seite abrufen
const workers = page.workers();
for (const w of workers) {
  console.log(w.url());
}

// Auf neuen Worker warten
const workerPromise = page.waitForEvent('worker');
await page.goto('https://example.com'); // laedt Worker
const worker = await workerPromise;

// Service Workers (ueber BrowserContext)
const serviceWorkers = context.serviceWorkers();
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 4      |
| Properties | 0     |
| Events    | 2 ('close', 'console') |

**Fazit:** `evaluate()` ist die primaere Methode, um Code im Worker-Kontext
auszufuehren und Ergebnisse abzurufen. `url()` identifiziert Worker eindeutig.
Das `console`-Event ermoeglicht vollstaendiges Logging auch von Worker-
Aktivitaeten, was besonders wichtig fuer Debugging in Service-Worker-
Umgebungen ist.

---

*Quelle: https://playwright.dev/docs/api/class-worker*
