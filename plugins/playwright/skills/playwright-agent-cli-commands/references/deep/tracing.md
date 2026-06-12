# Playwright Agent CLI — Tracing

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `tracing-start` | Trace-Aufnahme starten |
| `tracing-stop` | Trace-Aufnahme beenden und speichern |

---

## tracing-start

```bash
playwright-cli tracing-start
```

Keine Argumente. Startet die Aufzeichnung aller Aktionen, DOM-Snapshots, Netzwerk-Anfragen
und Timing-Informationen.

---

## tracing-stop

```bash
playwright-cli tracing-stop
# Trace saved to .playwright-cli/trace.zip
```

Keine Argumente. Beendet die Aufnahme und speichert als ZIP-Datei.

---

## Trace anzeigen

```bash
npx playwright show-trace .playwright-cli/trace.zip
```

Der Trace Viewer zeigt:

| Information | Beschreibung |
|-------------|-------------|
| Aktions-Timeline | Chronologische Liste aller ausgefuehrten Aktionen |
| DOM-Snapshots | Seitenzustand vor und nach jeder Aktion |
| Screenshots | Visuelle Referenz fuer jeden Schritt |
| Netzwerk-Anfragen | Alle HTTP-Anfragen und Antworten |
| Console-Nachrichten | Browser-Console-Output |
| Timing-Informationen | Dauer jeder Aktion |

---

## Basis-Workflow

```bash
playwright-cli tracing-start
playwright-cli goto https://example.com
playwright-cli click e5
playwright-cli fill e3 "test"
playwright-cli tracing-stop
# Trace saved to .playwright-cli/trace.zip

npx playwright show-trace .playwright-cli/trace.zip
```

---

## Debugging-Workflow

```bash
playwright-cli tracing-start
playwright-cli goto https://store.example.com/checkout
playwright-cli fill e10 "4111111111111111"
playwright-cli click e15
playwright-cli snapshot
playwright-cli console error
playwright-cli tracing-stop
# Trace fuer Team-Analyse bereitstellen
```

---

## Automatische Session-Aufnahme

Sessions ohne manuelle Befehle automatisch tracen:

```bash
playwright-cli --save-session
```

Zeichnet automatisch Traces fuer jede Session auf ohne manuellen Eingriff.

---

## Wann Tracing nutzen

- Nicht-reproduzierbare Fehler debuggen
- Ausfuehrungskontext fuer Team-Analyse erfassen
- Timing-Probleme diagnostizieren
- Netzwerk-Anfragen bei Fehlern dokumentieren
- CI-Fehler in Playwright-Tests analysieren

---

Quelle: https://playwright.dev/agent-cli/commands/tracing
