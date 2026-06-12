# Playwright — class: WebError

> **Manifest:** 3 Methoden, 0 Properties, 0 Events (1 externer Context-Event).
> Repraesentiert einen unbehandelten JavaScript-Fehler (uncaught exception) in einer Seite.
> Instanzen werden ueber `browserContext.on('weberror')` erhalten.

---

## Uebersicht

`WebError` kapselt unbehandelte Ausnahmen, die im Browser-Kontext auftreten
(d.h. Fehler, die nicht per `try/catch` oder `window.onerror` abgefangen
wurden). Dies unterscheidet sich von `page.on('pageerror')`, das den gleichen
Zweck hat, aber auf eine einzelne Seite beschraenkt ist.

```javascript
// Auf Context-Ebene
context.on('weberror', webError => {
  console.error('Uncaught exception:', webError.error());
  console.error('In Seite:', webError.page()?.url());
});
```

---

## Methoden

### webError.error()

Gibt das zugrunde liegende JavaScript-Error-Objekt zurueck.

**Signatur:**
```typescript
webError.error(): Error
```

**Parameter:** Keine

**Rueckgabe:** `Error` — das JavaScript Error-Objekt mit `message`, `stack`
und ggf. weiteren Properties.

**Hinzugefuegt:** v1.38

**Beispiel:**
```javascript
context.on('weberror', webError => {
  const err = webError.error();
  console.error('Fehler:', err.message);
  console.error('Stack:', err.stack);
});
```

---

### webError.location()

Gibt den Quellcode-Ort des Fehlers zurueck.

**Signatur:**
```typescript
webError.location(): {
  url: string;
  line: number;
  column: number;
}
```

**Parameter:** Keine

**Rueckgabe:** Objekt mit:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `url` | `string` | URL der Ressource, in der der Fehler aufgetreten ist |
| `line` | `number` | 0-basierte Zeilennummer |
| `column` | `number` | 0-basierte Spaltennummer |

**Hinzugefuegt:** v1.60

**Beispiel:**
```javascript
context.on('weberror', webError => {
  const loc = webError.location();
  console.error(`Fehler bei ${loc.url}:${loc.line}:${loc.column}`);
});
```

---

### webError.page()

Gibt die Seite zurueck, in der der unbehandelte Fehler aufgetreten ist.

**Signatur:**
```typescript
webError.page(): Page | null
```

**Parameter:** Keine

**Rueckgabe:** `Page | null` — die Seite oder `null`, wenn der Fehler
nicht einer Seite zugeordnet werden konnte (z.B. in einem Service Worker)

**Hinzugefuegt:** v1.38

**Beispiel:**
```javascript
context.on('weberror', webError => {
  const p = webError.page();
  if (p) {
    console.error('Fehler auf Seite:', p.url());
  } else {
    console.error('Fehler in unbekanntem Kontext');
  }
});
```

---

## Context-Event: 'weberror'

Das Event wird auf dem `BrowserContext` registriert:

```javascript
context.on('weberror', (webError) => {
  // webError: WebError
});
```

Fuer seitenspezifische Fehler gibt es auch `page.on('pageerror')`:

```javascript
page.on('pageerror', (error) => {
  // error: Error (direkt, kein WebError-Wrapper)
  console.error(error.message);
});
```

---

## Vollstaendiges Beispiel: Fehler-Sammlung

```javascript
const errors: string[] = [];

context.on('weberror', webError => {
  const err = webError.error();
  const loc = webError.location();
  errors.push(`${err.message} (${loc.url}:${loc.line}:${loc.column})`);
});

await page.goto('https://example.com');
// ... Testschritte ...

if (errors.length > 0) {
  throw new Error(`Unbehandelte Browser-Fehler:\n${errors.join('\n')}`);
}
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 3      |
| Properties | 0     |
| Events    | 0 (1 Context-Event: 'weberror') |

**Fazit:** `error()` liefert den eigentlichen Fehler inkl. Stack-Trace.
`location()` (ab v1.60) ist essentiell fuer die Quellortkartierung in
Source-Map-Szenarien. `page()` hilft dabei, Fehler im Multi-Page-Kontext
der richtigen Seite zuzuordnen.

---

*Quelle: https://playwright.dev/docs/api/class-weberror*
