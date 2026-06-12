# Playwright Agent CLI — Video Recording

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `video-start [filename]` | Videoaufnahme starten |
| `video-chapter <title>` | Kapitelmarke einfuegen |
| `video-stop` | Aufnahme beenden und speichern |

---

## video-start

```bash
playwright-cli video-start
# Gespeichert unter: .playwright-cli/<timestamp>.webm

playwright-cli video-start demo.webm
# Benutzerdefinierter Dateiname

playwright-cli video-start recording.webm --size=800x600
# Mit spezifischer Groesse
```

### video-start-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `[filename]` | string | Nein | Zeitstempel | Dateiname fuer die Videoaufnahme (`.webm`) |
| `--size=<WxH>` | string | Nein | Viewport-Groesse | Videoaufloessung z. B. `800x600`, `1280x720` |

---

## video-chapter

```bash
playwright-cli video-chapter "Login"
playwright-cli video-chapter "Checkout" --description="Entering payment details"
playwright-cli video-chapter "Confirmation" --description="Order confirmed" --duration=2000
```

### video-chapter-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `<title>` | string | Ja | — | Kapitel-Bezeichnung |
| `--description=<text>` | string | Nein | — | Zusaetzlicher Beschreibungstext |
| `--duration=<ms>` | number | Nein | — | Millisekunden, die die Kapitelkarte angezeigt wird |

---

## video-stop

```bash
playwright-cli video-stop
```

Keine Argumente. Beendet die Aufnahme und speichert die Datei.

---

## Vollstaendiger Aufnahme-Workflow

```bash
playwright-cli video-start demo.webm

playwright-cli video-chapter "Startseite" --description="Landing page loaded"
playwright-cli goto https://demo.playwright.dev/todomvc/

playwright-cli video-chapter "Todo hinzufuegen"
playwright-cli type "Buy groceries"
playwright-cli press Enter

playwright-cli video-chapter "Abschliessen"
playwright-cli check e21

playwright-cli video-stop
# Saved: .playwright-cli/demo.webm
```

---

## Automatische Aufnahme

Automatisch starten ohne manuelle Befehle:

### Via Konfigurationsdatei

```json
{
  "saveVideo": {
    "width": 800,
    "height": 600
  }
}
```

### Via Umgebungsvariable

```bash
PLAYWRIGHT_MCP_SAVE_VIDEO=800x600 playwright-cli open https://example.com
```

---

## Anwendungsfaelle

| Szenario | Beschreibung |
|----------|-------------|
| Bug-Reproduktion | Fehlerhaftes Verhalten fuer Entwickler aufzeichnen |
| Test-Dokumentation | Manuellen Test-Durchlauf dokumentieren |
| Agent-Monitoring | Automatisierten Agent-Ablauf beobachten |
| Demovideo erstellen | Produktfunktionen demonstrieren |

---

Quelle: https://playwright.dev/agent-cli/commands/video-recording
