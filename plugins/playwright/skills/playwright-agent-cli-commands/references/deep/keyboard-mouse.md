# Playwright Agent CLI — Keyboard & Mouse

## Tastatur-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `press <key>` | Taste druecken und loslassen |
| `keydown <key>` | Taste niederdruecken (haelt gehalten) |
| `keyup <key>` | Taste loslassen |

---

## press

```bash
playwright-cli press Enter
playwright-cli press Tab
playwright-cli press Escape
playwright-cli press ArrowDown
playwright-cli press Control+a
playwright-cli press Control+c
playwright-cli press Control+v
playwright-cli press Shift+Tab
playwright-cli press Alt+Enter
```

### press-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<key>` | string | Ja | Taste oder Tastenkombination (z. B. `Enter`, `Control+a`) |

### Haeufige Tasten

| Taste | Beschreibung |
|-------|-------------|
| `Enter` | Bestaetigen / Formular absenden |
| `Tab` | Naechstes Feld fokussieren |
| `Shift+Tab` | Vorheriges Feld fokussieren |
| `Escape` | Abbrechen / Schliessen |
| `Backspace` | Zeichen loeschen (rueckwaerts) |
| `Delete` | Zeichen loeschen (vorwaerts) |
| `Space` | Leerzeichen / Checkbox umschalten |
| `ArrowUp` | Aufwaerts navigieren |
| `ArrowDown` | Abwaerts navigieren |
| `ArrowLeft` | Links navigieren |
| `ArrowRight` | Rechts navigieren |
| `Home` | Zum Anfang springen |
| `End` | Zum Ende springen |
| `PageUp` | Seite aufwaerts blaettern |
| `PageDown` | Seite abwaerts blaettern |
| `Control+a` | Alles auswaehlen |
| `Control+c` | Kopieren |
| `Control+v` | Einfuegen |
| `Control+x` | Ausschneiden |
| `Control+z` | Rueckgaengig |
| `Control+y` | Wiederherstellen |
| `F1` bis `F12` | Funktionstasten |

### Tastaturnavigation (Beispiel)

```bash
playwright-cli press Tab                # Naechstes Feld
playwright-cli press ArrowDown          # Dropdown-Navigation
playwright-cli press Enter              # Option auswaehlen
playwright-cli press Shift+Tab          # Zurueck
```

---

## keydown / keyup

Fuer modifizierte Interaktionen (z. B. gehalten halten waehrend Klick):

```bash
playwright-cli keydown Shift
playwright-cli click e15               # Shift+Klick
playwright-cli keyup Shift
```

### keydown/keyup-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<key>` | string | Ja | Zu haltende Taste (z. B. `Shift`, `Control`, `Alt`) |

---

## Maus-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `mousemove <x> <y>` | Maus zu Koordinaten bewegen |
| `mousedown [button]` | Maustaste niederdruecken |
| `mouseup [button]` | Maustaste loslassen |
| `mousewheel <dx> <dy>` | Mit Mausrad scrollen |

---

## mousemove

```bash
playwright-cli mousemove 100 200
playwright-cli mousemove 450 320
```

### mousemove-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<x>` | number | Ja | Horizontale Koordinate in Pixeln |
| `<y>` | number | Ja | Vertikale Koordinate in Pixeln |

---

## mousedown / mouseup

```bash
# Linksklick bei Koordinaten
playwright-cli mousemove 100 200
playwright-cli mousedown
playwright-cli mouseup

# Rechtsklick
playwright-cli mousemove 300 400
playwright-cli mousedown right
playwright-cli mouseup right

# Mittelklick
playwright-cli mousemove 500 300
playwright-cli mousedown middle
playwright-cli mouseup middle
```

### mousedown/mouseup-Argumente

| Argument | Typ | Pflicht | Standard | Beschreibung |
|----------|-----|---------|---------|-------------|
| `[button]` | string | Nein | `left` | Taste: `left`, `right`, `middle` |

---

## mousewheel

```bash
playwright-cli mousewheel 0 500        # 500px nach unten scrollen
playwright-cli mousewheel 0 -300       # 300px nach oben scrollen
playwright-cli mousewheel 200 0        # 200px nach rechts scrollen
playwright-cli mousewheel -100 0       # 100px nach links scrollen
playwright-cli mousewheel 0 1000       # Schnell nach unten scrollen
```

### mousewheel-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<dx>` | number | Ja | Horizontaler Scroll-Wert in Pixeln (negativ = links) |
| `<dy>` | number | Ja | Vertikaler Scroll-Wert in Pixeln (negativ = oben) |

---

## Wann welchen Ansatz verwenden

| Szenario | Empfohlener Ansatz |
|----------|-------------------|
| Buttons, Links, Formularfelder klicken | `click`, `fill`, ref-basierte Befehle |
| Canvas-Anwendungen (Zeichnen, Karten) | Maus-Befehle mit Koordinaten |
| Benutzerdefinierte UI-Steuerelemente ohne Accessibility | Maus-Befehle mit Koordinaten |
| Drag-Interaktionen auf pixel-praezisen Zielen | Maus-Befehle mit Koordinaten |
| Tastaturkuerzel | `press` mit Modifier+Taste |
| Modifier waehrend Mausklick halten | `keydown` / `keyup` um `click` herum |

---

Quelle: https://playwright.dev/agent-cli/commands/keyboard-mouse
