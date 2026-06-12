# Playwright Aktionen und Actionability

Alle Aktionen fuehren vor der Ausfuehrung Actionability-Checks durch und warten
automatisch, bis die Bedingungen erfuellt sind (Auto-Waiting).

---

## Actionability-Checks

### Die fuenf Pruefungen

| Pruefung | Kriterium |
|---|---|
| **Visible** | Element hat eine nicht-leere Bounding Box UND hat KEIN `visibility:hidden`. Elemente mit `display:none` oder Groesse 0 schlagen fehl. `opacity:0` besteht die Pruefung. |
| **Stable** | Element hat dieselbe Bounding Box in mindestens zwei aufeinanderfolgenden Animations-Frames (kein laufende Animation). |
| **Receives Events** | Am Aktions-Koordinatenpunkt empfaengt das Zielelement Pointer-Events (kein Overlay darueber). |
| **Enabled** | Element ist NICHT deaktiviert. Deaktiviert durch: `[disabled]`-Attribut (button/select/input/textarea/option/optgroup), deaktiviertes Fieldset-Vorfahre, `[aria-disabled=true]`-Vorfahre. |
| **Editable** | Element ist Enabled UND hat KEIN `[readonly]`- oder `[aria-readonly=true]`-Attribut. |

### Welche Aktion prueft was

| Aktion | Visible | Stable | Receives Events | Enabled | Editable |
|---|---|---|---|---|---|
| `click`, `check`, `tap` | Ja | Ja | Ja | Ja | — |
| `hover`, `dragTo` | Ja | Ja | Ja | — | — |
| `fill`, `clear` | Ja | — | — | Ja | Ja |
| `screenshot` | Ja | Ja | — | — | — |
| `blur`, `focus`, `press`, `dispatchEvent` | — | — | — | — | — |

### force: true — Pruefungen ueberspringen

```typescript
await page.getByRole('button').click({ force: true });
// Ueberspringt Receives-Events-Pruefung; sonstige Pruefungen bleiben
```

### trial: true — Nur Pruefungen, keine Ausfuehrung

```typescript
await page.getByRole('button').click({ trial: true });
// Fuehrt alle Actionability-Checks durch, fuehrt aber die Aktion NICHT aus
// Nuetzlich um vorab zu pruefen ob ein Element klickbar ist
```

### Timeout-Verhalten

Wenn Actionability-Checks nicht innerhalb des Timeouts bestehen: `TimeoutError`.
Default-Timeout: `0` (kein Timeout) — kann ueberschrieben werden mit `timeout`-Option
oder `page.setDefaultTimeout()` / `browserContext.setDefaultTimeout()`.

---

## click()

```typescript
await locator.click(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `button` | `'left' \| 'right' \| 'middle'` | `'left'` | Maustaste |
| `clickCount` | `number` | `1` | Anzahl der Klicks |
| `delay` | `number` | `0` | Verzoegerung in ms zwischen mousedown und mouseup |
| `force` | `boolean` | `false` | Actionability-Checks ueberspringen |
| `modifiers` | `Array<'Alt' \| 'Control' \| 'ControlOrMeta' \| 'Meta' \| 'Shift'>` | — | Modifier-Tasten |
| `noWaitAfter` | `boolean` | `false` | **Veraltet**, hat keine Wirkung mehr |
| `position` | `{ x: number; y: number }` | Mittelpunkt | Position relativ zur Padding Box |
| `steps` | `number` | `1` | Interpolierte Mausbewegungsschritte |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks, Aktion nicht ausfuehren |

```typescript
// Einfacher Klick
await page.getByRole('button', { name: 'Absenden' }).click();

// Rechtsklick
await page.getByRole('button').click({ button: 'right' });

// Doppelklick (Alternative zu dblclick)
await page.getByRole('button').click({ clickCount: 2 });

// Mit Modifier
await page.getByRole('link').click({ modifiers: ['Shift'] });

// Prazise Position
await page.getByRole('button').click({ position: { x: 10, y: 5 } });

// Ctrl+Klick (macOS: Meta)
await page.getByRole('link').click({ modifiers: ['ControlOrMeta'] });
```

---

## dblclick()

```typescript
await locator.dblclick(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `button` | `'left' \| 'right' \| 'middle'` | `'left'` | Maustaste |
| `delay` | `number` | `0` | Verzoegerung zwischen Klicks in ms |
| `force` | `boolean` | `false` | Checks ueberspringen |
| `modifiers` | `Array<...>` | — | Modifier-Tasten |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `position` | `{ x: number; y: number }` | Mittelpunkt | Position |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks |

```typescript
await page.getByRole('listitem').dblclick();
```

---

## fill()

Loescht den vorhandenen Wert und gibt neuen Text ein. Fuer `<input>`, `<textarea>` und
`contenteditable`-Elemente.

```typescript
await locator.fill(value: string, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `value` | `string` | — | **Pflicht** — einzugebender Text |
| `force` | `boolean` | `false` | Checks ueberspringen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
await page.getByLabel('E-Mail').fill('user@example.com');
await page.getByPlaceholder('Passwort').fill('geheim');

// Inhalt loeschen (leerer String)
await page.getByRole('textbox').fill('');
```

---

## clear()

Loescht den Inhalt eines Input-Felds.

```typescript
await locator.clear(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
await page.getByRole('textbox').clear();
```

---

## pressSequentially()

Gibt Text Zeichen fuer Zeichen ein (loest Tastaturereignisse aus). Nuetzlich fuer
Felder mit Autocomplete oder zeichenweise Validierung.

```typescript
await locator.pressSequentially(text: string, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `text` | `string` | — | **Pflicht** — einzugebender Text |
| `delay` | `number` | `0` | Verzoegerung in ms zwischen Tastenanschlaegen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
// Mit Tipp-Verzoegerung fuer realistischere Simulation
await page.getByRole('textbox').pressSequentially('Hallo Welt', { delay: 50 });
```

---

## press()

Drueckt eine einzelne Taste oder Tastenkombination.

```typescript
await locator.press(key: string, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `key` | `string` | — | **Pflicht** — Taste oder Kombination |
| `delay` | `number` | `0` | Zeit in ms zwischen keydown und keyup |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

### Taste-Format

- Einzelne Taste: `'Enter'`, `'Tab'`, `'Escape'`, `'Space'`, `'Backspace'`
- Kombination: `'Control+A'`, `'Shift+Tab'`, `'Control+ArrowRight'`
- Plattform-uebergreifend: `'ControlOrMeta+A'` (Control auf Windows/Linux, Meta auf macOS)

```typescript
await page.getByRole('textbox').press('Enter');
await page.getByRole('textbox').press('Control+A');
await page.getByRole('textbox').press('Shift+Tab');
await page.keyboard.press('Escape');    // Globaler Tastendruck
```

---

## hover()

Bewegt die Maus ueber ein Element.

```typescript
await locator.hover(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `modifiers` | `Array<'Alt' \| 'Control' \| 'ControlOrMeta' \| 'Meta' \| 'Shift'>` | — | Modifier-Tasten |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `position` | `{ x: number; y: number }` | Mittelpunkt | Position relativ zur Padding Box |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks |

```typescript
await page.getByRole('button').hover();
await page.locator('.menu-item').hover({ position: { x: 5, y: 5 } });
```

---

## check() und uncheck()

```typescript
await locator.check(options?)
await locator.uncheck(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `position` | `{ x: number; y: number }` | Mittelpunkt | Position |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks |

```typescript
await page.getByRole('checkbox', { name: 'AGB akzeptieren' }).check();
await page.getByRole('checkbox').uncheck();
await expect(page.getByRole('checkbox')).toBeChecked();
```

### setChecked() — kombiniert check/uncheck

```typescript
await locator.setChecked(checked: boolean, options?)
```

```typescript
await page.getByRole('checkbox').setChecked(true);
await page.getByRole('checkbox').setChecked(false);
```

---

## selectOption()

Waehlt eine oder mehrere Optionen in einem `<select>`-Element.

```typescript
await locator.selectOption(values, options?)
```

### values-Parameter

| Format | Beschreibung | Beispiel |
|---|---|---|
| `string` | Einzelner Wert | `'option-value'` |
| `string[]` | Mehrere Werte | `['val1', 'val2']` |
| `{ value?: string }` | Objekt mit Wert | `{ value: 'rot' }` |
| `{ label?: string }` | Objekt mit Label | `{ label: 'Rot' }` |
| `{ index?: number }` | Objekt mit Index | `{ index: 0 }` |
| Kombinierte Arrays | Mehrere Objekte | `[{ label: 'Rot' }, { value: 'blau' }]` |

### Options-Parameter

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
// Nach Wert auswaehlen
await page.getByRole('combobox').selectOption('farbe-rot');

// Nach Label auswaehlen
await page.getByRole('combobox').selectOption({ label: 'Rot' });

// Nach Index auswaehlen
await page.getByRole('combobox').selectOption({ index: 2 });

// Mehrere Optionen (Multi-Select)
await page.getByRole('listbox').selectOption(['rot', 'blau', 'gruen']);

// Gemischt
await page.getByRole('listbox').selectOption([
  { label: 'Rot' },
  { value: 'blau' },
]);
```

---

## setInputFiles()

Setzt Dateien fuer `<input type="file">`-Elemente.

```typescript
await locator.setInputFiles(files, options?)
```

### files-Parameter

| Format | Beschreibung |
|---|---|
| `string` | Einzelner Dateipfad |
| `string[]` | Mehrere Dateipfade |
| `FilePayload` | Datei-Objekt (kein Dateisystem noetig) |
| `FilePayload[]` | Mehrere Datei-Objekte |
| `[]` | Leeres Array = Auswahl loeschen |

### FilePayload-Objekt

```typescript
interface FilePayload {
  name: string;       // Dateiname
  mimeType: string;   // MIME-Typ, z.B. 'image/png'
  buffer: Buffer;     // Dateiinhalt als Buffer
}
```

### Options

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
// Einzelne Datei
await page.getByLabel('Datei hochladen').setInputFiles('/pfad/zur/datei.pdf');

// Mehrere Dateien
await page.getByLabel('Bilder').setInputFiles([
  '/pfad/bild1.png',
  '/pfad/bild2.jpg',
]);

// Aus Buffer (kein Dateisystem)
await page.getByLabel('Upload').setInputFiles({
  name: 'dokument.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Dateiinhalt'),
});

// Auswahl loeschen
await page.getByLabel('Upload').setInputFiles([]);
```

---

## dragTo()

Zieht ein Element zu einem anderen Locator.

```typescript
await locator.dragTo(target: Locator, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `sourcePosition` | `{ x: number; y: number }` | Mittelpunkt | Startpunkt relativ zur Padding Box |
| `targetPosition` | `{ x: number; y: number }` | Mittelpunkt | Zielpunkt relativ zur Padding Box |
| `steps` | `number` | `1` | Interpolierte Mausbewegungsschritte |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks |

```typescript
// Einfaches Drag & Drop
await page.getByText('Aufgabe 1').dragTo(page.getByText('Erledigt'));

// Mit Positionierung
await page.locator('#element').dragTo(page.locator('#ziel'), {
  sourcePosition: { x: 10, y: 10 },
  targetPosition: { x: 5, y: 5 },
});
```

### Manuelles Drag & Drop mit Mouse-API

```typescript
await page.mouse.move(startX, startY);
await page.mouse.down();
await page.mouse.move(zielX, zielY, { steps: 10 });
await page.mouse.up();
```

---

## tap()

Tippt auf ein Element (Touch-Geste). Erfordert `hasTouch: true` in den Context-Optionen.

```typescript
await locator.tap(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `modifiers` | `Array<...>` | — | Modifier-Tasten |
| `noWaitAfter` | `boolean` | `false` | Veraltet |
| `position` | `{ x: number; y: number }` | Mittelpunkt | Position |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur Checks |

```typescript
const context = await browser.newContext({ hasTouch: true });
const page = await context.newPage();
await page.getByRole('button').tap();
```

---

## focus() und blur()

```typescript
await locator.focus(options?)
await locator.blur(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
await page.getByRole('textbox').focus();
await page.getByRole('textbox').blur();
```

---

## dispatchEvent()

Loest ein DOM-Event programmatisch aus (ignoriert Actionability-Checks).

```typescript
await locator.dispatchEvent(type: string, eventInit?, options?)
```

| Parameter | Typ | Beschreibung |
|---|---|---|
| `type` | `string` | Event-Typ, z.B. `'click'`, `'input'`, `'change'` |
| `eventInit` | `object` | Event-Initialisierungsobjekt |
| `timeout` | `number` | Max. Wartezeit in ms |

```typescript
await page.getByRole('button').dispatchEvent('click');
await page.locator('#datepicker').dispatchEvent('change', {
  bubbles: true,
});
```

---

## scrollIntoViewIfNeeded()

Scrollt das Element in den sichtbaren Bereich.

```typescript
await locator.scrollIntoViewIfNeeded(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
await page.getByRole('button').scrollIntoViewIfNeeded();
```

### Mausrad

```typescript
await page.mouse.wheel(deltaX, deltaY);
// deltaX: horizontales Scrollen, deltaY: vertikales Scrollen
await page.mouse.wheel(0, 500);  // 500px nach unten scrollen
```

---

## evaluate() und evaluateAll()

Fuehrt JavaScript im Browser-Kontext aus.

```typescript
// Auf einem Element
const result = await locator.evaluate(fn, arg?, options?)

// Auf allen passenden Elementen
const results = await locator.evaluateAll(fn, arg?)
```

```typescript
// Element-Eigenschaft lesen
const value = await page.getByRole('textbox').evaluate(el => el.value);

// Alle Element-Texte sammeln
const texte = await page.getByRole('listitem').evaluateAll(
  items => items.map(el => el.textContent?.trim())
);
```

---

## Zustandsabfrage-Methoden

```typescript
await locator.getAttribute(name: string, options?): Promise<string | null>
await locator.innerHTML(options?):  Promise<string>
await locator.innerText(options?):  Promise<string>
await locator.inputValue(options?): Promise<string>
await locator.textContent(options?): Promise<string | null>
await locator.isChecked(options?):  Promise<boolean>
await locator.isDisabled(options?): Promise<boolean>
await locator.isEditable(options?): Promise<boolean>
await locator.isEnabled(options?):  Promise<boolean>
await locator.isHidden(options?):   Promise<boolean>
await locator.isVisible(options?):  Promise<boolean>
```

Alle akzeptieren `{ timeout?: number }`.

```typescript
const titel = await page.getByRole('heading').innerText();
const wert = await page.getByRole('textbox').inputValue();
const istAktiv = await page.getByRole('checkbox').isChecked();
const html = await page.locator('.container').innerHTML();
```

---

## waitFor()

Wartet bis ein Element in einem bestimmten Zustand ist.

```typescript
await locator.waitFor(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `state` | `'attached' \| 'detached' \| 'visible' \| 'hidden'` | `'visible'` | Erwarteter Zustand |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

```typescript
await page.getByText('Laden...').waitFor({ state: 'hidden' });
await page.getByRole('dialog').waitFor({ state: 'visible' });
await page.getByRole('button').waitFor({ state: 'attached' });
```

---

## selectText()

Markiert den Text-Inhalt eines Elements.

```typescript
await locator.selectText(options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `force` | `boolean` | `false` | Checks ueberspringen |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

---

## Vollstaendiges Interaktions-Beispiel

```typescript
import { test, expect } from '@playwright/test';

test('Bestellformular ausfullen', async ({ page }) => {
  await page.goto('https://shop.example.com/checkout');

  // Texteingabe
  await page.getByLabel('Vorname').fill('Anna');
  await page.getByLabel('Nachname').fill('Muster');
  await page.getByLabel('E-Mail').fill('anna@example.com');

  // Dropdown
  await page.getByLabel('Land').selectOption({ label: 'Deutschland' });

  // Checkbox
  await page.getByRole('checkbox', { name: 'Expresszustellung' }).check();

  // Radio-Button
  await page.getByRole('radio', { name: 'Kreditkarte' }).check();

  // Datei-Upload
  await page.getByLabel('Rechnung hochladen').setInputFiles('/pfad/rechnung.pdf');

  // Absenden
  await page.getByRole('button', { name: 'Bestellen' }).click();

  // Ergebnis pruefen
  await expect(page.getByRole('heading', { name: 'Bestellung erfolgreich' }))
    .toBeVisible({ timeout: 10000 });
});
```

<!-- Quellen:
https://playwright.dev/docs/input
https://playwright.dev/docs/actionability
https://playwright.dev/docs/api/class-locator
-->
