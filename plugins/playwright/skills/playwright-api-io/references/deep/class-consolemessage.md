# Playwright — class: ConsoleMessage

> **Manifest:** 6 Methoden, 0 Properties, 0 Events (1 externer Page-Event).
> Repraesentiert eine einzelne Console-Nachricht aus dem Browser-Kontext.
> Instanzen werden ueber `page.on('console')` und `worker.on('console')` erhalten.

---

## Uebersicht

`ConsoleMessage` kapselt alle Informationen zu einem einzelnen Console-API-
Aufruf der Seite (`console.log`, `console.error`, usw.). Jede Instanz
enthaelt den Text, den Typ, den Ursprungs-Ort und ggf. die Argumente.

```javascript
page.on('console', async msg => {
  console.log(`[${msg.type()}] ${msg.text()}`);
  if (msg.type() === 'error') {
    console.error('Browser-Fehler:', msg.text());
  }
});
```

---

## Methoden

### consoleMessage.args()

Gibt alle Argumente zurueck, die der Console-Funktion uebergeben wurden,
als JSHandle-Array.

**Signatur:**
```typescript
consoleMessage.args(): Array<JSHandle>
```

**Parameter:** Keine

**Rueckgabe:** `Array<JSHandle>` — ein Handle pro Argument

**Beispiel:**
```javascript
page.on('console', async msg => {
  for (const arg of msg.args()) {
    console.log(await arg.jsonValue());
  }
});
```

**Hinweis:** `JSHandle.jsonValue()` wirft fuer nicht-serialisierbare Werte.
Fuer DOM-Elemente `asElement()` nutzen.

---

### consoleMessage.location()

Gibt den Quellcode-Ort des Console-Aufrufs zurueck.

**Signatur:**
```typescript
consoleMessage.location(): {
  url: string;
  line: number;
  column: number;
  lineNumber: number;   // deprecated, use line
  columnNumber: number; // deprecated, use column
}
```

**Parameter:** Keine

**Rueckgabe:** Objekt mit:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `url` | `string` | URL der Quell-Ressource |
| `line` | `number` | 0-basierte Zeilennummer |
| `column` | `number` | 0-basierte Spaltennummer |
| `lineNumber` | `number` | Deprecated — `line` verwenden |
| `columnNumber` | `number` | Deprecated — `column` verwenden |

**Beispiel:**
```javascript
page.on('console', msg => {
  const loc = msg.location();
  console.log(`${loc.url}:${loc.line}:${loc.column}`);
});
```

---

### consoleMessage.page()

Gibt die Seite zurueck, die diese Nachricht erzeugt hat.

**Signatur:**
```typescript
consoleMessage.page(): Page | null
```

**Parameter:** Keine

**Rueckgabe:** `Page | null` — die ausloesende Seite oder `null`

**Beispiel:**
```javascript
page.on('console', msg => {
  const p = msg.page();
  if (p) console.log('Seite:', p.url());
});
```

---

### consoleMessage.text()

Gibt den Textinhalt der Console-Nachricht zurueck.

**Signatur:**
```typescript
consoleMessage.text(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — der serialisierte Nachrichtentext

**Beispiel:**
```javascript
page.on('console', msg => {
  console.log('Nachricht:', msg.text());
});
```

---

### consoleMessage.timestamp()

Gibt den Zeitstempel der Nachricht in Millisekunden seit Unix-Epoch zurueck.

**Signatur:**
```typescript
consoleMessage.timestamp(): number
```

**Parameter:** Keine

**Rueckgabe:** `number` — Millisekunden-Timestamp

**Hinzugefuegt:** v1.59

**Beispiel:**
```javascript
page.on('console', msg => {
  const date = new Date(msg.timestamp());
  console.log(`[${date.toISOString()}] ${msg.text()}`);
});
```

---

### consoleMessage.type()

Gibt den Typ der Console-Nachricht zurueck.

**Signatur:**
```typescript
consoleMessage.type(): string
```

**Parameter:** Keine

**Rueckgabe:** Einer der folgenden Strings:

| Wert | Entspricht |
|------|-----------|
| `'log'` | `console.log()` |
| `'debug'` | `console.debug()` |
| `'info'` | `console.info()` |
| `'error'` | `console.error()` |
| `'warning'` | `console.warn()` |
| `'dir'` | `console.dir()` |
| `'dirxml'` | `console.dirxml()` |
| `'table'` | `console.table()` |
| `'trace'` | `console.trace()` |
| `'clear'` | `console.clear()` |
| `'startGroup'` | `console.group()` |
| `'startGroupCollapsed'` | `console.groupCollapsed()` |
| `'endGroup'` | `console.groupEnd()` |
| `'assert'` | `console.assert()` |
| `'profile'` | `console.profile()` |
| `'profileEnd'` | `console.profileEnd()` |
| `'count'` | `console.count()` |
| `'time'` | `console.time()` |
| `'timeEnd'` | `console.timeEnd()` |

**Beispiel:**
```javascript
page.on('console', async msg => {
  if (msg.type() === 'error') {
    console.error(`Browser-Error: "${msg.text()}"`);
  }
});
```

---

### consoleMessage.worker()

Gibt den Web Worker oder Service Worker zurueck, der die Nachricht erzeugt hat.

**Signatur:**
```typescript
consoleMessage.worker(): Worker | null
```

**Parameter:** Keine

**Rueckgabe:** `Worker | null`

**Hinzugefuegt:** v1.57

**Beispiel:**
```javascript
page.on('console', msg => {
  const w = msg.worker();
  if (w) console.log('Von Worker:', w.url());
});
```

---

## Page-Event: 'console'

```javascript
page.on('console', msg => {
  // msg ist ConsoleMessage
  console.log(`[${msg.type()}] ${msg.text()}`);
});
```

Auch verfuegbar auf `Worker`:

```javascript
worker.on('console', msg => { /* ... */ });
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 6 (+1 seit v1.57: worker()) |
| Properties | 0     |
| Events    | 0 (1 Page-Event: 'console', 1 Worker-Event: 'console') |

**Fazit:** `text()` und `type()` reichen fuer einfache Log-Ueberwachung aus.
`args()` wird benoetigt, wenn strukturierte Objekte (Arrays, Objekte) geprueft
werden sollen. `timestamp()` ermaoglicht zeitliche Korrelation von Browser-
Nachrichten mit Test-Schritten.

---

*Quelle: https://playwright.dev/docs/api/class-consolemessage*
