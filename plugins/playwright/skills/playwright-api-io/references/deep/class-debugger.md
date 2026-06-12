# Playwright — class: Debugger

> **Manifest:** 5 Methoden, 0 Properties, 1 Event.
> Erlaubt programmatisches Pausieren und Kontrollieren der Playwright-Test-Ausfuehrung.
> Hinzugefuegt: v1.59. Zugriff: `test.info().debugger` oder via `@playwright/test`-API.

---

## Uebersicht

`Debugger` bietet eine programmatische Schnittstelle zum Debuggen von
Playwright-Tests — aehnlich wie Browser-DevTools-Breakpoints, aber auf
Playwright-Aktions-Ebene. Der Debugger pausiert *vor* der naechsten
Playwright-Aktion (nicht im JavaScript-Interpreter).

Alle Methoden wurden in v1.59 eingefuehrt.

---

## Methoden

### debugger.next()

Setzt die Ausfuehrung fort und pausiert vor der naechsten Aktion.
Wirft einen Fehler, wenn der Debugger nicht pausiert ist.

**Signatur:**
```typescript
debugger.next(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.59

**Beispiel:**
```javascript
// Schritt fuer Schritt durch Aktionen gehen
await debugger.next(); // eine Aktion vorwaerts
await debugger.next(); // naechste Aktion
```

---

### debugger.pausedDetails()

Gibt Informationen ueber den aktuellen Pause-Zustand zurueck.
Gibt `null` zurueck, wenn der Debugger nicht pausiert ist.

**Signatur:**
```typescript
debugger.pausedDetails(): null | {
  location: {
    file: string;
    line?: number;
    column?: number;
  };
  title: string;
}
```

**Parameter:** Keine

**Rueckgabe:** `null | Object` mit:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `location` | `Object` | Quellcode-Ort der naechsten Aktion |
| `location.file` | `string` | Quelldatei-Pfad |
| `location.line` | `number` (optional) | Zeilennummer |
| `location.column` | `number` (optional) | Spaltennummer |
| `title` | `string` | Beschreibung der naechsten Aktion |

**Hinzugefuegt:** v1.59

**Beispiel:**
```javascript
const details = debugger.pausedDetails();
if (details) {
  console.log(`Pausiert bei: "${details.title}"`);
  console.log(`Ort: ${details.location.file}:${details.location.line}`);
}
```

---

### debugger.requestPause()

Konfiguriert den Debugger, vor der naechsten Aktion zu pausieren.
Wirft einen Fehler, wenn bereits pausiert.

**Signatur:**
```typescript
debugger.requestPause(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.59

**Unterschied zu `page.pause()`:**
- `page.pause()`: Pausiert *sofort* an der aktuellen Stelle.
- `debugger.requestPause()`: Setzt einen Breakpoint fuer die *naechste* Aktion.

**Beispiel:**
```javascript
await debugger.requestPause();
// Naechste Playwright-Aktion wird jetzt pausieren
await page.click('#button'); // pausiert hier
```

---

### debugger.resume()

Setzt die Ausfuehrung vom pausierten Zustand fort.
Wirft einen Fehler, wenn nicht pausiert.

**Signatur:**
```typescript
debugger.resume(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.59

**Beispiel:**
```javascript
// Debugger laeuft bis zum naechsten requestPause() oder runTo()
await debugger.resume();
```

---

### debugger.runTo(location)

Setzt die Ausfuehrung fort und pausiert, wenn eine Aktion vom angegebenen
Quellcode-Ort ausgeloest wird. Wirft einen Fehler, wenn nicht pausiert.

**Signatur:**
```typescript
debugger.runTo(location: {
  file: string;
  line?: number;
  column?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `location` | `Object` | ja | — | Ziel-Quellortobjekt |
| `location.file` | `string` | ja | — | Pfad zur Zieldatei |
| `location.line` | `number` | nein | — | Zeilennummer des Breakpoints |
| `location.column` | `number` | nein | — | Spaltennummer des Breakpoints |

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.59

**Beispiel:**
```javascript
// Ausfuehren bis Zeile 55 in der Testdatei
await debugger.runTo({
  file: '/tests/checkout.spec.ts',
  line: 55
});
```

---

## Events

### debugger.on('pausedstatechanged')

Wird gefeuert, wenn der Debugger pausiert oder fortgesetzt wird.

**Hinzugefuegt:** v1.59

**Signatur:**
```javascript
debugger.on('pausedstatechanged', (data) => {
  // data: Payload (Typ nicht spezifiziert in Dokumentation)
});
```

**Beispiel:**
```javascript
debugger.on('pausedstatechanged', () => {
  const details = debugger.pausedDetails();
  if (details) {
    console.log(`Debugger pausiert: "${details.title}"`);
  } else {
    console.log('Debugger fortgesetzt');
  }
});
```

---

## Vollstaendiges Beispiel

```javascript
// Programmatischer Debugger-Workflow
test('checkout flow', async ({ page, debugger: dbg }) => {
  // Auf naechste Aktion warten
  await dbg.requestPause();

  await page.goto('/checkout');

  // Details der aktuellen Pause pruefen
  const details = dbg.pausedDetails();
  console.log('Pausiert bei:', details?.title);

  // Schritt fuer Schritt
  await dbg.next();
  await dbg.next();

  // Bis zu einem bestimmten Ort laufen
  await dbg.runTo({
    file: 'checkout.spec.ts',
    line: 42
  });

  // Weiterlaufen lassen
  await dbg.resume();
});
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 5      |
| Properties | 0     |
| Events    | 1 ('pausedstatechanged') |

**Fazit:** Der `Debugger` ist ein programmatischer Breakpoint-Mechanismus auf
Playwright-Aktions-Ebene. `requestPause()` + `next()` ermoeglicht Step-Debugging.
`runTo()` ist das Aequivalent zu "Run to Cursor" in IDEs. Das
`pausedstatechanged`-Event ermoeglicht reaktive Debug-UIs oder Reporter-
Integrationen.

---

*Quelle: https://playwright.dev/docs/api/class-debugger*
