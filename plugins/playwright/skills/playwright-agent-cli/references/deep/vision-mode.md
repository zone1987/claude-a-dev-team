# Playwright Agent CLI — Vision Mode

## Uebersicht

Vision Mode ermoeglicht die Interaktion mit Seitenelementen ueber Koordinaten und Screenshots —
fuer Elemente, die nicht im Accessibility-Tree sichtbar sind.

**Grundregel:** Fuer die meisten Webanwendungen ist der Standard-Snapshot-Ansatz
zuverlaessiger und token-effizienter. Vision Mode nur nutzen, wenn der Accessibility-Tree
den Anwendungsfall nicht abdeckt.

---

## Vision-Befehle

| Befehl | Typ | Beschreibung |
|--------|-----|-------------|
| `mousemove <x> <y>` | Pflicht: x (number), y (number) | Maus zu Pixel-Koordinaten bewegen |
| `mousedown [button]` | Optional: `left` (Standard), `right`, `middle` | Maustaste druecken |
| `mouseup [button]` | Optional: `left` (Standard), `right`, `middle` | Maustaste loslassen |
| `mousewheel <dx> <dy>` | Pflicht: dx (number), dy (number) | Scrollen (dx=horizontal, dy=vertikal) |
| `screenshot` | — | Viewport erfassen fuer Koordinaten-Referenz |

---

## Anwendungsfaelle

| Szenario | Empfohlener Ansatz |
|----------|-------------------|
| Buttons, Links, Formularelemente klicken | `click`, `fill`, ref-basierte Befehle |
| Canvas-/WebGL-Applikationen | Maus-Befehle mit Koordinaten |
| Karten-Interaktion (Pan/Zoom) | Maus-Befehle mit Koordinaten |
| Bild-Bearbeitungs-Tools | Maus-Befehle mit Koordinaten |
| Diagramm-/Graph-Interaktion | Maus-Befehle mit Koordinaten |
| Benutzerdefinierte Widgets ohne ARIA | Maus-Befehle mit Koordinaten |
| Pixel-praezise Drag-Interaktionen | Maus-Befehle mit Koordinaten |

---

## Workflow 1: Canvas-App

```bash
# Screenshot fuer visuelle Referenz aufnehmen
playwright-cli screenshot

# Koordinaten aus Screenshot identifizieren, dann interagieren
playwright-cli mousemove 100 200
playwright-cli mousedown
playwright-cli mousemove 300 400
playwright-cli mouseup

# Ergebnis pruefen
playwright-cli screenshot --filename=after-draw.png
```

## Workflow 2: Icon ohne barrierefreien Namen klicken

```bash
# Screenshot aufnehmen um Koordinaten zu identifizieren
playwright-cli screenshot --filename=reference.png

# Koordinatenbasiert klicken
playwright-cli mousemove 450 320
playwright-cli mousedown
playwright-cli mouseup

# Ergebnis pruefen
playwright-cli screenshot --filename=after-click.png
```

## Workflow 3: Rechtsklick-Kontextmenue

```bash
playwright-cli screenshot
playwright-cli mousemove 300 400
playwright-cli mousedown right
playwright-cli mouseup right
playwright-cli snapshot
```

## Workflow 4: Scrollen

```bash
# Nach unten scrollen (500 Pixel)
playwright-cli mousewheel 0 500

# Nach rechts scrollen (200 Pixel)
playwright-cli mousewheel 200 0

# Nach oben scrollen
playwright-cli mousewheel 0 -300
```

---

## Koordinaten ermitteln

1. `playwright-cli screenshot --filename=ref.png` ausfuehren
2. Bild analysieren (visuell oder per Bildanalyse-Tool)
3. x/y-Koordinaten des Zielelements bestimmen
4. `playwright-cli mousemove <x> <y>` ausfuehren
5. Maus-Down/Up oder weitere Aktionen ausfuehren
6. Ergebnis per Screenshot pruefen

---

Quelle: https://playwright.dev/agent-cli/vision-mode
