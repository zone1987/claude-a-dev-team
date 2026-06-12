# Playwright Agent CLI — Screenshots & PDF

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `screenshot` | Screenshot des sichtbaren Viewports |
| `screenshot [ref]` | Screenshot eines spezifischen Elements |
| `screenshot --filename=<name>` | Screenshot mit benutzerdefiniertem Dateinamen |
| `screenshot --full-page` | Screenshot der gesamten scrollbaren Seite |
| `pdf` | Seite als PDF exportieren |
| `pdf --filename=<name>` | PDF mit benutzerdefiniertem Dateinamen |
| `snapshot` | Accessibility-Tree erfassen (kein visuelles Bild) |

---

## screenshot

```bash
playwright-cli screenshot
# Gespeichert unter: .playwright-cli/screenshot-2026-03-15.png

playwright-cli screenshot e15
# Screenshot von Element e15

playwright-cli screenshot "#main"
# Screenshot des Elements mit ID 'main'

playwright-cli screenshot --filename=login-page.png
# Benutzerdefinierter Dateiname

playwright-cli screenshot --full-page --filename=full-page.png
# Komplette scrollbare Seite
```

### screenshot-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `[ref]` | string | Nein | — | Element-Ref oder CSS-Selektor fuer Element-Screenshot |
| `--filename=<name>` | string | Nein | Zeitstempel | Dateiname fuer den Screenshot |
| `--full-page` | flag | Nein | false | Gesamte scrollbare Seite erfassen |

Standard-Speicherort: `.playwright-cli/screenshot-<timestamp>.png`

---

## pdf

```bash
playwright-cli pdf
# Gespeichert unter: .playwright-cli/page-<timestamp>.pdf

playwright-cli pdf --filename=report.pdf
# Benutzerdefinierter Dateiname
```

### pdf-Optionen

| Option | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|---------|-------------|
| `--filename=<name>` | string | Nein | Zeitstempel | Dateiname fuer das PDF |

Standard-Speicherort: `.playwright-cli/page-<timestamp>.pdf`

---

## snapshot (Accessibility-Tree)

Im Gegensatz zu `screenshot` (visuell) erfasst `snapshot` den Accessibility-Tree.

```bash
playwright-cli snapshot                     # Ganze Seite
playwright-cli snapshot --filename=f.yaml   # Benutzerdefinierter Dateiname
playwright-cli snapshot e34                 # Element-Scope per Ref
playwright-cli snapshot "#main"             # Element-Scope per CSS-Selektor
playwright-cli snapshot --depth=4           # Baum-Tiefe begrenzen
playwright-cli snapshot --raw               # Nur Ausgabe, ohne Seiteninformationen
```

---

## Wann welches Tool verwenden

| Anwendungsfall | Empfohlenes Tool |
|----------------|-----------------|
| Visuelles Layout pruefen | `screenshot` |
| Canvas-/Diagramm-Inhalt erfassen | `screenshot` |
| Bug dokumentieren | `screenshot` |
| Ganze Seite als Bild | `screenshot --full-page` |
| Seite als Dokument exportieren | `pdf` |
| Elemente fuer Interaktion finden | `snapshot` (Accessibility-Tree) |
| Seitenstruktur verstehen | `snapshot` |
| Textinhalt lesen | `snapshot` |
| Element-Refs fuer Befehle ermitteln | `snapshot` |

---

## Typischer Workflow

```bash
# Seite laden
playwright-cli open https://app.example.com --headed

# Strukturellen Snapshot nehmen
playwright-cli snapshot

# Interagieren
playwright-cli click e15
playwright-cli fill e3 "test@example.com"

# Visuellen Beweis nehmen
playwright-cli screenshot --filename=state-after-fill.png

# Bug-Dokumentation
playwright-cli screenshot --full-page --filename=full-bug-report.png
playwright-cli pdf --filename=bug-report.pdf
```

---

Quelle: https://playwright.dev/agent-cli/commands/screenshots-pdf
