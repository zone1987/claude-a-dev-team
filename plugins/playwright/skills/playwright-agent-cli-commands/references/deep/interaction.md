# Playwright Agent CLI — Interaction

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `click <ref> [button]` | Element klicken (links, rechts oder Mitte) |
| `dblclick <ref> [button]` | Element doppelklicken |
| `fill <ref> <text>` | Text-Feld leeren und befuellen |
| `fill <ref> <text> --submit` | Befuellen und Enter druecken |
| `type <text>` | Text in fokussiertes Element eingeben |
| `select <ref> <value>` | Dropdown-Option auswaehlen |
| `check <ref>` | Checkbox oder Radio-Button anklicken (aktivieren) |
| `uncheck <ref>` | Checkbox deaktivieren |
| `hover <ref>` | Ueber ein Element hovern |
| `drag <startRef> <endRef>` | Drag & Drop |
| `upload <file>` | Datei hochladen |
| `resize <width> <height>` | Browser-Fenster anpassen |

---

## Elemente ansprechen

### Drei unterstuetzte Methoden

**Refs aus Snapshots (empfohlen):**

```bash
playwright-cli snapshot
playwright-cli click e15
playwright-cli fill e3 "hello"
```

**CSS-Selektoren:**

```bash
playwright-cli click "#main > button.submit"
playwright-cli fill "#email" "test@example.com"
playwright-cli click "[data-testid='submit']"
```

**Playwright-Locators:**

```bash
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli fill "getByLabel('Email')" "test@example.com"
playwright-cli click "getByTestId('submit-button')"
playwright-cli click "getByText('Login')"
```

---

## click

```bash
playwright-cli click e15
playwright-cli click e15 right        # Rechtsklick
playwright-cli click e15 middle       # Mittelklick
playwright-cli click "#submit-btn"
playwright-cli click "getByRole('button', { name: 'Save' })"
```

### click-Argumente

| Argument | Typ | Pflicht | Standard | Beschreibung |
|----------|-----|---------|---------|-------------|
| `<ref>` | string | Ja | — | Element-Ref, CSS-Selektor oder Playwright-Locator |
| `[button]` | string | Nein | `left` | Maustaste: `left`, `right`, `middle` |

---

## dblclick

```bash
playwright-cli dblclick e15
playwright-cli dblclick "#my-element"
```

### dblclick-Argumente

| Argument | Typ | Pflicht | Standard | Beschreibung |
|----------|-----|---------|---------|-------------|
| `<ref>` | string | Ja | — | Element-Ref, CSS-Selektor oder Playwright-Locator |
| `[button]` | string | Nein | `left` | Maustaste: `left`, `right`, `middle` |

---

## fill

```bash
playwright-cli fill e3 "hello@example.com"
playwright-cli fill e3 "test input" --submit
playwright-cli fill "#search" "playwright"
playwright-cli fill "getByLabel('Email')" "user@example.com"
```

### fill-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `<ref>` | string | Ja | — | Element-Ref, CSS-Selektor oder Playwright-Locator |
| `<text>` | string | Ja | — | Einzugebender Text (ersetzt vorhandenen Inhalt) |
| `--submit` | flag | Nein | false | Enter nach dem Befuellen druecken |

---

## type

```bash
playwright-cli type "Buy groceries"
playwright-cli type "Water flowers"
```

### type-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<text>` | string | Ja | In das aktuell fokussierte Element einzugebender Text |

Unterschied zu `fill`: `type` simuliert echte Tastatureingaben zeichenweise,
`fill` setzt den Wert direkt und loescht vorher.

---

## select

```bash
playwright-cli select e8 "Germany"
playwright-cli select "#country" "US"
playwright-cli select "getByLabel('Country')" "France"
```

### select-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<ref>` | string | Ja | Element-Ref, CSS-Selektor oder Playwright-Locator des `<select>`-Elements |
| `<value>` | string | Ja | Wert (`value`-Attribut) oder sichtbarer Text der Option |

---

## check / uncheck

```bash
playwright-cli check e21
playwright-cli uncheck e21
playwright-cli check "[name='agree']"
```

### check/uncheck-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<ref>` | string | Ja | Element-Ref, CSS-Selektor oder Playwright-Locator der Checkbox/Radio |

---

## hover

```bash
playwright-cli hover e20
playwright-cli hover "#menu-trigger"
playwright-cli hover "getByText('Hover me')"
```

### hover-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<ref>` | string | Ja | Element-Ref, CSS-Selektor oder Playwright-Locator |

---

## drag

```bash
playwright-cli drag e10 e20
playwright-cli drag "#draggable" "#droptarget"
```

### drag-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<startRef>` | string | Ja | Quell-Element-Ref, CSS-Selektor oder Playwright-Locator |
| `<endRef>` | string | Ja | Ziel-Element-Ref, CSS-Selektor oder Playwright-Locator |

---

## upload

```bash
playwright-cli upload ./document.pdf
playwright-cli upload ./image.png
```

### upload-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<file>` | string (Pfad) | Ja | Pfad zur hochzuladenden Datei |

Der Datei-Eingabe-Dialog muss vorher durch Klick geoeffnet worden sein.

---

## resize

```bash
playwright-cli resize 1280 720
playwright-cli resize 375 812          # iPhone-Groesse
playwright-cli resize 1920 1080        # Full-HD Desktop
```

### resize-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<width>` | number | Ja | Fensterbreite in Pixeln |
| `<height>` | number | Ja | Fensterhoehe in Pixeln |

---

## Login-Workflow (Beispiel)

```bash
playwright-cli open https://app.example.com/login
playwright-cli snapshot
playwright-cli fill e3 "user@example.com"
playwright-cli fill e5 "password123" --submit
playwright-cli snapshot
playwright-cli screenshot --filename=after-login.png
```

---

Quelle: https://playwright.dev/agent-cli/commands/interaction
