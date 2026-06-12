# Playwright — class: Location

> **Manifest:** 0 Methoden, 3 Properties, 0 Events.
> Repraesentiert einen Quellcode-Ort (Datei, Zeile, Spalte) in Playwright Test.
> Wird als Rueckgabetyp und Parameter in verschiedenen APIs verwendet.

---

## Uebersicht

`Location` ist ein einfaches Daten-Interface ohne Methoden. Es beschreibt,
wo eine Testdatei, eine Test-Suite oder ein Testfall im Quellcode definiert
ist. Es erscheint als Property auf `TestCase`, `Suite`, `TestResult` sowie
als Parameter in Tracing-APIs.

---

## Properties

### location.file

Pfad zur Quelldatei.

**Typ:** `string`

**Hinzugefuegt:** v1.10

**Beispiel:**
```javascript
console.log(testCase.location.file);
// z.B. "/home/user/tests/login.spec.ts"
```

---

### location.line

Zeilennummer in der Quelldatei.

**Typ:** `number`

**Hinzugefuegt:** v1.10

**Hinweis:** 1-basiert in den meisten Kontexten, aber in einigen APIs
(z.B. `ConsoleMessage.location()`) 0-basiert. Kontext pruefen.

**Beispiel:**
```javascript
console.log(testCase.location.line); // z.B. 42
```

---

### location.column

Spaltennummer in der Quelldatei.

**Typ:** `number`

**Hinzugefuegt:** v1.10

**Hinweis:** Wie `line` — Indexierung haengt vom aufrufenden Kontext ab.

**Beispiel:**
```javascript
console.log(testCase.location.column); // z.B. 5
```

---

## Verwendung als Interface

`Location` taucht in folgenden APIs auf:

### Als Property:
- `TestCase.location` — wo der Test definiert ist
- `Suite.location` — wo die Suite definiert ist

### Als Rueckgabetyp:
- `ConsoleMessage.location()` — Ort des `console.*()`-Aufrufs (0-basiert)
- `WebError.location()` — Ort des unbehandelten Fehlers (0-basiert)
- `Debugger.pausedDetails()` — aktueller Pause-Ort

### Als Parameter:
- `tracing.group(name, { location })` — Quellortzuordnung fuer Trace-Gruppe
- `debugger.runTo(location)` — Zielort fuer bedingtes Pausieren

---

## Vollstaendiges Beispiel

```javascript
// In einem Reporter
class MyReporter {
  onTestBegin(test) {
    const loc = test.location;
    console.log(`Test "${test.title}" in ${loc.file}:${loc.line}:${loc.column}`);
  }
}

// In Tracing
await context.tracing.group('Mein Schritt', {
  location: {
    file: '/tests/login.spec.ts',
    line: 45,
    column: 3
  }
});
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 0      |
| Properties | 3 (file, line, column) |
| Events    | 0      |

**Fazit:** `Location` ist ein reines Daten-Transfer-Objekt ohne Logik.
Es verbindet Laufzeit-Informationen mit Quellcode-Positionen und ist
zentral fuer Reporter, Tracing und Debugger-Integrationen. Die Indexierung
(0- vs. 1-basiert) variiert je nach API-Kontext — immer die jeweilige
API-Dokumentation pruefen.

---

*Quelle: https://playwright.dev/docs/api/class-location*
