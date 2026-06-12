# Playwright class-elementhandle: Vollstaendige API-Referenz

`ElementHandle` repraesentiert ein DOM-Element-Handle. Es ist ein spezielles `JSHandle` mit
zusaetzlichen DOM-spezifischen Methoden. **Wichtig:** Die Playwright-Dokumentation empfiehlt
ausdruecklich, `ElementHandle` NICHT mehr direkt zu verwenden und stattdessen `Locator`-Objekte
und web-first assertions zu nutzen. Alle Interaktionsmethoden von ElementHandle sind als
"deprecated" (entmutigt) markiert.

Ausnahmen: `boundingBox()`, `contentFrame()`, `ownerFrame()` und `waitForElementState()`
gelten als nicht deprecated und koennen weiterhin verwendet werden wenn ein ElementHandle
bereits vorhanden ist (z.B. aus `page.waitForSelector()`).

ElementHandle erbt alle Methoden von [JSHandle](class-jshandle.md).

---

## Inhaltsverzeichnis

1. [Nicht-deprecated Methoden](#1-nicht-deprecated-methoden)
2. [Deprecated: Selektor-Methoden](#2-deprecated-selektor-methoden)
3. [Deprecated: Interaktionsmethoden](#3-deprecated-interaktionsmethoden)
4. [Deprecated: Inhalts-/Zustandsmethoden](#4-deprecated-inhaltszustandsmethoden)
5. [Deprecated: Hilfsmethoden](#5-deprecated-hilfsmethoden)
6. [Geerbte JSHandle-Methoden](#6-geerbte-jshandle-methoden)
7. [Manifest](#7-manifest)

---

## 1. Nicht-deprecated Methoden

### elementHandle.boundingBox()

```typescript
elementHandle.boundingBox(): Promise<null | {
  x: number,
  y: number,
  width: number,
  height: number
}>
```

**Parameter:** Keine

**Rueckgabe:** Promise mit Bounding-Box-Objekt oder `null` wenn Element nicht sichtbar ist.

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `number` | X-Koordinate der linken oberen Ecke (relativ zum Viewport) |
| `y` | `number` | Y-Koordinate der linken oberen Ecke |
| `width` | `number` | Breite des Elements in Pixel |
| `height` | `number` | Hoehe des Elements in Pixel |

Gibt `null` zurueck wenn das Element nicht sichtbar ist (z.B. `display: none`).

```typescript
const handle = await page.waitForSelector('.my-element');
const box = await handle?.boundingBox();
if (box) {
  console.log(`Element bei (${box.x}, ${box.y}), ${box.width}x${box.height}px`);
  // Manuelle Mausbewegung zur Element-Mitte
  await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
}
```

---

### elementHandle.contentFrame()

```typescript
elementHandle.contentFrame(): Promise<null | Frame>
```

**Parameter:** Keine

**Rueckgabe:** Promise mit Frame-Objekt oder `null`.

Gibt den Frame-Inhalt eines `<iframe>`-Elements zurueck. Gibt `null` zurueck wenn das Element
kein `<iframe>` ist.

```typescript
const iframeHandle = await page.$('iframe#my-frame');
const frame = await iframeHandle?.contentFrame();
if (frame) {
  await frame.getByRole('button', { name: 'Absenden' }).click();
}
```

---

### elementHandle.ownerFrame()

```typescript
elementHandle.ownerFrame(): Promise<null | Frame>
```

**Parameter:** Keine

**Rueckgabe:** Promise mit Frame-Objekt oder `null`.

Gibt den Frame zurueck, der dieses Element enthaelt. `null` wenn der Frame nicht mehr existiert
oder abgehaengt wurde.

```typescript
const handle = await page.$('h1');
const frame = await handle?.ownerFrame();
console.log('Element gehoert zu Frame:', frame?.url());
```

---

### elementHandle.waitForElementState()

```typescript
elementHandle.waitForElementState(
  state: 'visible' | 'hidden' | 'stable' | 'enabled' | 'disabled' | 'editable',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `state` | `string` | ja | — | Gewuenschter Zustand des Elements |
| `options.timeout` | `number` | nein | `0` (kein Timeout) | Max. Wartezeit in ms |

**Zustaende:**

| Zustand | Beschreibung |
|---|---|
| `'visible'` | Element hat nicht-leere Bounding Box, kein `visibility:hidden`, kein `opacity:0` |
| `'hidden'` | Gegenteil von `visible` (oder Element existiert nicht im DOM) |
| `'stable'` | Element bewegt sich nicht und ist sichtbar |
| `'enabled'` | Nicht deaktiviert (`disabled`-Attribut abwesend) |
| `'disabled'` | Hat `disabled`-Attribut oder `aria-disabled` |
| `'editable'` | Weder `disabled` noch `readonly` |

```typescript
const spinnerHandle = await page.$('.spinner');
// Warten bis Spinner verschwindet
await spinnerHandle?.waitForElementState('hidden');

const buttonHandle = await page.$('button#save');
// Warten bis Button klickbar
await buttonHandle?.waitForElementState('enabled', { timeout: 5000 });

// Warten bis animiertes Element zur Ruhe kommt
const animHandle = await page.$('.animated-card');
await animHandle?.waitForElementState('stable');
```

---

## 2. Deprecated: Selektor-Methoden

**Empfehlung:** Verwende `locator.locator()` stattdessen.

### elementHandle.$()

```typescript
elementHandle.$(selector: string): Promise<null | ElementHandle>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `selector` | `string` | ja | CSS/XPath-Selektor |

Sucht das erste Element, das dem Selektor im Kontext dieses Elements entspricht.

```typescript
const row = await page.$('tr.selected');
const cell = await row?.$('td.price');
const text = await cell?.textContent();
```

---

### elementHandle.$$()

```typescript
elementHandle.$$(selector: string): Promise<Array<ElementHandle>>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `selector` | `string` | ja | CSS/XPath-Selektor |

Sucht alle Elemente, die dem Selektor im Kontext dieses Elements entsprechen.

```typescript
const list = await page.$('ul.items');
const items = await list?.$$('li') ?? [];
for (const item of items) {
  console.log(await item.textContent());
}
```

---

### elementHandle.$eval()

```typescript
elementHandle.$eval<T>(
  selector: string,
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `selector` | `string` | ja | CSS-Selektor relativ zu diesem Element |
| `pageFunction` | `Function\|string` | ja | Im Browser ausgefuehrte Funktion |
| `arg` | `Serializable\|JSHandle` | nein | Argument |

Fuehrt Funktion auf dem ersten gematchten Kind-Element aus.

```typescript
const form = await page.$('form#login');
const emailValue = await form?.$eval('input[name=email]', el => (el as HTMLInputElement).value);
```

---

### elementHandle.$$eval()

```typescript
elementHandle.$$eval<T>(
  selector: string,
  pageFunction: (elements: Element[], arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

Fuehrt Funktion auf ALLEN gematchten Kind-Elementen aus.

```typescript
const table = await page.$('table');
const cellTexts = await table?.$$eval('td', cells => cells.map(c => c.textContent));
```

---

## 3. Deprecated: Interaktionsmethoden

**Empfehlung:** Verwende `page.locator().click()`, `locator.fill()` etc.

### elementHandle.click()

```typescript
elementHandle.click(options?: {
  button?: 'left' | 'right' | 'middle',
  clickCount?: number,
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  steps?: number,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `button` | `string` | `'left'` | Maustaste |
| `clickCount` | `number` | `1` | Anzahl Klicks |
| `delay` | `number` | `0` | Ms zwischen mousedown und mouseup |
| `force` | `boolean` | `false` | Actionability-Checks ueberspringen |
| `modifiers` | `string[]` | `[]` | Tasten waehrend Klick |
| `position` | `{x,y}` | Element-Mitte | Klick-Position relativ zum Element |
| `steps` | `number` | `1` | Bewegungsschritte zur Klick-Position |
| `timeout` | `number` | `0` | Max. Wartezeit |
| `trial` | `boolean` | `false` | Nur pruefen ohne auszufuehren |

```typescript
const button = await page.$('button.submit');
await button?.click();
await button?.click({ button: 'right' });
await button?.click({ position: { x: 5, y: 5 } });
```

---

### elementHandle.dblclick()

```typescript
elementHandle.dblclick(options?: {
  button?: 'left' | 'right' | 'middle',
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  steps?: number,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Doppelklick.

```typescript
const cell = await page.$('.editable-cell');
await cell?.dblclick();
```

---

### elementHandle.check()

```typescript
elementHandle.check(options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Aktiviert Checkbox oder Radio-Button.

```typescript
const checkbox = await page.$('#accept-terms');
await checkbox?.check();
await checkbox?.check({ force: true });
```

---

### elementHandle.uncheck()

```typescript
elementHandle.uncheck(options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Deaktiviert Checkbox.

```typescript
const checkbox = await page.$('#newsletter');
await checkbox?.uncheck();
```

---

### elementHandle.setChecked()

```typescript
elementHandle.setChecked(checked: boolean, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `checked` | `boolean` | ja | `true` = ankracken, `false` = abwaehlen |

```typescript
const checkbox = await page.$('#newsletter');
await checkbox?.setChecked(true);
await checkbox?.setChecked(false);
```

---

### elementHandle.fill()

```typescript
elementHandle.fill(value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `value` | `string` | ja | Einzufuegender Text |

Loescht bestehenden Wert und fuellt Eingabefeld neu.

```typescript
const input = await page.$('input[name=email]');
await input?.fill('test@example.com');
```

---

### elementHandle.focus()

```typescript
elementHandle.focus(): Promise<void>
```

Setzt Fokus auf das Element.

```typescript
const input = await page.$('input[autofocus]');
await input?.focus();
```

---

### elementHandle.hover()

```typescript
elementHandle.hover(options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Bewegt Maus ueber Element.

```typescript
const trigger = await page.$('.dropdown-trigger');
await trigger?.hover();
```

---

### elementHandle.tap()

```typescript
elementHandle.tap(options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch-Tap (Touchscreen-Emulation erforderlich).

```typescript
const button = await page.$('.mobile-btn');
await button?.tap();
```

---

### elementHandle.press()

```typescript
elementHandle.press(key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `key` | `string` | ja | — | Taste oder Kombination (z.B. `'Enter'`, `'Control+a'`) |
| `options.delay` | `number` | nein | `0` | Ms zwischen keydown und keyup |

```typescript
const input = await page.$('input[type=search]');
await input?.press('Enter');
await input?.press('Control+a');
```

---

### elementHandle.type()

```typescript
elementHandle.type(text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated.** Simuliert echte Tastatureingaben ohne bestehenden Wert zu loeschen.

```typescript
const input = await page.$('input');
await input?.type('Hallo Welt', { delay: 50 });
```

---

### elementHandle.dispatchEvent()

```typescript
elementHandle.dispatchEvent(
  type: string,
  eventInit?: EvaluationArgument
): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `type` | `string` | ja | DOM-Event-Typ |
| `eventInit` | `EvaluationArgument` | nein | Event-Initialisierungsobjekt |

```typescript
const button = await page.$('button');
await button?.dispatchEvent('click');
await button?.dispatchEvent('mouseover', { bubbles: true });
```

---

### elementHandle.selectOption()

```typescript
elementHandle.selectOption(
  values: null | string | ElementHandle | string[] | SelectOptionObject | ElementHandle[] | SelectOptionObject[],
  options?: {
    force?: boolean,
    noWaitAfter?: boolean,
    timeout?: number
  }
): Promise<string[]>
```

| `values` Varianten | Beschreibung |
|---|---|
| `'value'` | Option nach value-Attribut |
| `{ label: 'Text' }` | Option nach sichtbarem Label |
| `{ index: 2 }` | Option nach Index (0-basiert) |
| `['val1', 'val2']` | Mehrfachauswahl |
| `null` | Selektion aufheben |

```typescript
const select = await page.$('select#country');
await select?.selectOption('de');
await select?.selectOption({ label: 'Deutschland' });
await select?.selectOption(null); // Auswahl aufheben
```

---

### elementHandle.selectText()

```typescript
elementHandle.selectText(options?: {
  force?: boolean,
  timeout?: number
}): Promise<void>
```

Selektiert den gesamten Text des Eingabefelds.

```typescript
const input = await page.$('input[name=title]');
await input?.selectText();
```

---

### elementHandle.setInputFiles()

```typescript
elementHandle.setInputFiles(
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    timeout?: number
  }
): Promise<void>
```

| `files` Varianten | Beschreibung |
|---|---|
| `'path/to/file'` | Einzelne Datei |
| `['file1', 'file2']` | Mehrere Dateien |
| `{ name, mimeType, buffer }` | Datei im Speicher |
| `[]` | Alle Dateien entfernen |

```typescript
const fileInput = await page.$('input[type=file]');
await fileInput?.setInputFiles('/path/to/test.pdf');
await fileInput?.setInputFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Hallo')
});
```

---

## 4. Deprecated: Inhalts-/Zustandsmethoden

### elementHandle.getAttribute()

```typescript
elementHandle.getAttribute(name: string): Promise<null | string>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Attribut-Name |

```typescript
const link = await page.$('a.nav-link');
const href = await link?.getAttribute('href');
const className = await link?.getAttribute('class');
```

---

### elementHandle.innerHTML()

```typescript
elementHandle.innerHTML(): Promise<string>
```

Gibt den inneren HTML-Inhalt zurueck.

```typescript
const div = await page.$('.content');
const html = await div?.innerHTML();
```

---

### elementHandle.innerText()

```typescript
elementHandle.innerText(): Promise<string>
```

Gibt den sichtbaren Textinhalt zurueck (respektiert CSS `display`, `visibility`).

```typescript
const h1 = await page.$('h1');
const text = await h1?.innerText();
```

---

### elementHandle.textContent()

```typescript
elementHandle.textContent(): Promise<null | string>
```

Gibt den `textContent` zurueck (inkl. versteckter Elemente). `null` wenn nicht vorhanden.

```typescript
const el = await page.$('#description');
const text = await el?.textContent();
```

---

### elementHandle.inputValue()

```typescript
elementHandle.inputValue(options?: { timeout?: number }): Promise<string>
```

Gibt den aktuellen Wert von `<input>`, `<textarea>` oder `<select>` zurueck.

```typescript
const input = await page.$('input[name=email]');
const value = await input?.inputValue();
```

---

### elementHandle.isChecked()

```typescript
elementHandle.isChecked(): Promise<boolean>
```

Gibt `true` wenn Checkbox/Radio angehakt ist.

```typescript
const checkbox = await page.$('#terms');
const checked = await checkbox?.isChecked();
```

---

### elementHandle.isDisabled()

```typescript
elementHandle.isDisabled(): Promise<boolean>
```

Gibt `true` wenn Element deaktiviert ist.

```typescript
const button = await page.$('button[type=submit]');
const disabled = await button?.isDisabled();
```

---

### elementHandle.isEditable()

```typescript
elementHandle.isEditable(): Promise<boolean>
```

Gibt `true` wenn Element editierbar ist (weder `disabled` noch `readonly`).

```typescript
const input = await page.$('input[name=username]');
const editable = await input?.isEditable();
```

---

### elementHandle.isEnabled()

```typescript
elementHandle.isEnabled(): Promise<boolean>
```

Gegenteil von `isDisabled()`.

```typescript
const submit = await page.$('button[type=submit]');
const enabled = await submit?.isEnabled();
```

---

### elementHandle.isHidden()

```typescript
elementHandle.isHidden(): Promise<boolean>
```

Gibt `true` wenn Element nicht sichtbar ist.

```typescript
const spinner = await page.$('.loading-spinner');
const hidden = await spinner?.isHidden();
```

---

### elementHandle.isVisible()

```typescript
elementHandle.isVisible(): Promise<boolean>
```

Gibt `true` wenn Element sichtbar ist.

```typescript
const modal = await page.$('.modal');
const visible = await modal?.isVisible();
```

---

## 5. Deprecated: Hilfsmethoden

### elementHandle.screenshot()

```typescript
elementHandle.screenshot(options?: {
  animations?: 'disabled' | 'allow',
  caret?: 'hide' | 'initial',
  mask?: Locator[],
  maskColor?: string,
  omitBackground?: boolean,
  path?: string,
  quality?: number,
  scale?: 'css' | 'device',
  style?: string,
  timeout?: number,
  type?: 'png' | 'jpeg'
}): Promise<Buffer>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `animations` | `string` | `'allow'` | CSS-Animationen deaktivieren fuer Screenshot |
| `caret` | `string` | `'hide'` | Text-Cursor verstecken |
| `mask` | `Locator[]` | — | Bereiche mit Farbe ueberdecken |
| `maskColor` | `string` | `'#FF00FF'` | Masken-Farbe |
| `omitBackground` | `boolean` | `false` | Transparenz (nur PNG) |
| `path` | `string` | — | Speicherpfad |
| `quality` | `number` | — | JPEG-Qualitaet 0–100 |
| `scale` | `string` | `'device'` | CSS oder Device-Pixel |
| `type` | `string` | `'png'` | Bildformat |

Macht Screenshot des Elements (nur der Bounding Box des Elements).

```typescript
const card = await page.$('.product-card');
await card?.screenshot({ path: 'card.png' });
const buffer = await card?.screenshot({ type: 'jpeg', quality: 80 });
```

---

### elementHandle.scrollIntoViewIfNeeded()

```typescript
elementHandle.scrollIntoViewIfNeeded(options?: {
  timeout?: number
}): Promise<void>
```

Scrollt das Element in den sichtbaren Bereich, falls noetig.

```typescript
const element = await page.$('#footer-element');
await element?.scrollIntoViewIfNeeded();
// Jetzt sichtbar und interagierbar
await element?.click();
```

---

### elementHandle.waitForSelector()

```typescript
elementHandle.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<null | ElementHandle>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `state` | `string` | `'visible'` | Gewuenschter Zustand |
| `strict` | `boolean` | `false` | Fehler bei mehreren Matches |
| `timeout` | `number` | `0` | Max. Wartezeit in ms |

**Deprecated** — Wartet auf ein Kind-Element im Kontext dieses Elements.

```typescript
const form = await page.$('form');
const submitBtn = await form?.waitForSelector('button[type=submit]', {
  state: 'visible'
});
```

---

## 6. Geerbte JSHandle-Methoden

ElementHandle erbt alle Methoden von `JSHandle`:

### elementHandle.asElement()

```typescript
elementHandle.asElement(): ElementHandle
```

Gibt sich selbst zurueck (da ElementHandle bereits ein ElementHandle ist).

```typescript
const handle = await page.$('h1');
const el = handle?.asElement(); // identisch mit handle
```

---

### elementHandle.dispose()

```typescript
elementHandle.dispose(): Promise<void>
```

Gibt das Element-Handle-Objekt frei. Nach `dispose()` sind keine Operationen mehr moeglich.

```typescript
const handle = await page.$('.temp-element');
// Arbeit mit handle...
await handle?.dispose();
```

---

### elementHandle.evaluate()

```typescript
elementHandle.evaluate<T>(
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pageFunction` | `Function\|string` | ja | Funktion mit diesem Element als erstem Argument |
| `arg` | `Serializable\|JSHandle` | nein | Zusaetzliches Argument |

```typescript
const el = await page.$('input');
const value = await el?.evaluate(input => (input as HTMLInputElement).value);
const len = await el?.evaluate((el, attr) => el.getAttribute(attr)?.length ?? 0, 'class');
```

---

### elementHandle.evaluateHandle()

```typescript
elementHandle.evaluateHandle<T>(
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<JSHandle<T>>
```

Wie `evaluate()`, gibt aber ein `JSHandle` zurueck.

```typescript
const el = await page.$('ul');
const firstChild = await el?.evaluateHandle(ul => ul.firstElementChild);
```

---

### elementHandle.getProperties()

```typescript
elementHandle.getProperties(): Promise<Map<string, JSHandle>>
```

Gibt alle eigenen Eigenschaften als Map von JSHandles zurueck.

```typescript
const el = await page.$('a');
const props = await el?.getProperties();
const hrefHandle = props?.get('href');
const href = await hrefHandle?.jsonValue();
```

---

### elementHandle.getProperty()

```typescript
elementHandle.getProperty(propertyName: string): Promise<JSHandle>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `propertyName` | `string` | ja | Name der Eigenschaft |

```typescript
const input = await page.$('input[type=text]');
const valueHandle = await input?.getProperty('value');
const value = await valueHandle?.jsonValue();
```

---

### elementHandle.jsonValue()

```typescript
elementHandle.jsonValue(): Promise<Serializable>
```

Gibt eine JSON-Repraesentation zurueck. Bei DOM-Elementen ist das Ergebnis ein leeres Objekt `{}`.

```typescript
const handle = await page.$('input');
const json = await handle?.jsonValue(); // {}
```

---

## 7. Manifest

| Kategorie | Dokumentierte Methoden |
|---|---|
| Nicht-deprecated | 4 (boundingBox, contentFrame, ownerFrame, waitForElementState) |
| Deprecated: Selektor | 4 ($, $$, $eval, $$eval) |
| Deprecated: Interaktion | 14 (click, dblclick, check, uncheck, setChecked, fill, focus, hover, tap, press, type, dispatchEvent, selectOption, selectText, setInputFiles) |
| Deprecated: Inhalte/Zustand | 11 (getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible) |
| Deprecated: Hilfe | 3 (screenshot, scrollIntoViewIfNeeded, waitForSelector) |
| Von JSHandle geerbt | 6 (asElement, dispose, evaluate, evaluateHandle, getProperties, getProperty, jsonValue) |

**Gesamt: ~42 Methoden**

**Fazit:** `ElementHandle` ist die Legacy-API fuer DOM-Element-Interaktionen in Playwright.
Alle Interaktionsmethoden sind offiziell als "discouraged" markiert. Fuer neue Tests sollten
ausschliesslich Locator-basierte Methoden verwendet werden. Die drei nicht-deprecated Methoden
(`boundingBox`, `contentFrame`, `waitForElementState`) sind nuetzlich wenn ein ElementHandle
bereits aus Legacy-Code oder `waitForSelector()` vorliegt.

---

**Quelle:** https://playwright.dev/docs/api/class-elementhandle
