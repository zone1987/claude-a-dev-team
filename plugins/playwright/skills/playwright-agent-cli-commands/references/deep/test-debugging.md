# Playwright Agent CLI — Test Debugging

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `pause-at <file>:<line>` | Breakpoint an bestimmter Zeile setzen |
| `resume` | Test-Ausfuehrung fortsetzen |
| `step-over` | Zur naechsten Aktion vorgehen |
| `attach <session-name>` | Mit pausiertem Test verbinden |

---

## Test mit Debug-Modus starten

```bash
npx playwright test --debug=cli
# Output: Session name: pw-debug-session-abc123
```

Startet den Test pausiert und gibt den Session-Namen aus, mit dem die CLI verbunden werden kann.

---

## attach (Test-Debugging-Modus)

```bash
playwright-cli attach pw-debug-session-abc123
```

### attach-Argumente (Test-Modus)

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<session-name>` | string | Ja | Session-Name aus `--debug=cli` Ausgabe |

---

## Seitenzustand erkunden

Nach dem Verbinden stehen alle normalen Befehle zur Verfuegung:

| Befehl | Zweck |
|--------|-------|
| `playwright-cli snapshot` | Aktuellen Seitenzustand ansehen |
| `playwright-cli console error` | Auf Fehler pruefen |
| `playwright-cli eval "() => document.title"` | JavaScript ausfuehren |
| `playwright-cli screenshot --filename=debug-state.png` | Screenshot aufnehmen |
| `playwright-cli network` | Netzwerk-Anfragen pruefen |

---

## Ausfuehrungs-Kontrolle

| Befehl | Typ | Beschreibung |
|--------|-----|-------------|
| `resume` | — | Test-Ausfuehrung fortsetzen |
| `step-over` | — | Zur naechsten Aktion vorgehen |
| `pause-at <datei>:<zeile>` | string | Breakpoint an spezifischer Testdatei-Zeile |

### pause-at-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<file>:<line>` | string | Ja | Dateipfad und Zeilennummer (z. B. `test.ts:42`) |

---

## Vollstaendiger Debugging-Workflow

### 1. Test mit Debug-Flag starten

```bash
npx playwright test --debug=cli tests/checkout.spec.ts
# Output: Connect with: playwright-cli attach pw-debug-abc123
```

### 2. CLI in separatem Terminal verbinden

```bash
playwright-cli attach pw-debug-abc123
```

### 3. Seitenzustand inspizieren

```bash
playwright-cli snapshot
playwright-cli console error
playwright-cli network
```

### 4. Tracing fuer Analyse starten

```bash
playwright-cli tracing-start
```

### 5. Durch Ausfuehrung schreiten

```bash
playwright-cli step-over              # Naechste Aktion
playwright-cli step-over              # Naechste Aktion
playwright-cli snapshot               # Zustand nach Aktionen pruefen
playwright-cli console                # Nachrichten pruefen
```

### 6. Zum Fehler-Punkt navigieren

```bash
playwright-cli pause-at test.ts:42   # Breakpoint setzen
playwright-cli resume                 # Bis dahin ausfuehren
playwright-cli snapshot               # Seitenzustand bei Fehler
playwright-cli screenshot --filename=failure-point.png
```

### 7. Trace speichern

```bash
playwright-cli tracing-stop
npx playwright show-trace .playwright-cli/trace.zip
```

---

## Flaky-Test untersuchen

```bash
# Test mehrfach mit Debug-Flag ausfuehren
npx playwright test --debug=cli --repeat-each=3 tests/flaky.spec.ts

playwright-cli attach <session>
playwright-cli tracing-start
playwright-cli step-over
playwright-cli step-over
playwright-cli console
playwright-cli network
playwright-cli tracing-stop
```

---

Quelle: https://playwright.dev/agent-cli/commands/test-debugging
