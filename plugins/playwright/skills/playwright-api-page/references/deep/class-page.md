# Playwright class-page: Vollstaendige API-Referenz

Die `Page`-Klasse repraesentiert eine einzelne Browser-Seite (Tab). Sie ist die zentrale
Einstiegsklasse fuer nahezu alle Playwright-Operationen: Navigation, Interaktion, Evaluation,
Netzwerk-Routing, Screenshot/PDF und Event-Handling.

---

## Inhaltsverzeichnis

1. [Navigation](#1-navigation)
2. [Seiteninhalte lesen/setzen](#2-seiteninhalte-lesensetzen)
3. [Locator-Fabrik-Methoden](#3-locator-fabrik-methoden)
4. [Frame-Verwaltung](#4-frame-verwaltung)
5. [Elementinteraktionen (Selector-basiert, deprecated)](#5-elementinteraktionen-selector-basiert-deprecated)
6. [JavaScript-Ausfuehrung](#6-javascript-ausfuehrung)
7. [Skript- und Style-Injektion](#7-skript--und-style-injektion)
8. [Netzwerk / Routing](#8-netzwerk--routing)
9. [Warten / Synchronisation](#9-warten--synchronisation)
10. [Screenshots & PDF](#10-screenshots--pdf)
11. [Browser-Konfiguration](#11-browser-konfiguration)
12. [Event-Handling / Listener](#12-event-handling--listener)
13. [Diverse Hilfsmethoden](#13-diverse-hilfsmethoden)
14. [Properties](#14-properties)
15. [Events](#15-events)
16. [Manifest](#16-manifest)

---

## 1. Navigation

### page.goto()

```typescript
page.goto(url: string, options?: {
  referer?: string,
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `url` | `string` | ja | — | Ziel-URL (absolut, data:, about:blank erlaubt) |
| `options.referer` | `string` | nein | — | HTTP-Referer-Header |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms (0 = unbegrenzt) |
| `options.waitUntil` | `string` | nein | `'load'` | `'load'`: wartet auf load-Event; `'domcontentloaded'`: DOMContentLoaded; `'networkidle'`: keine offenen Netzwerk-Verbindungen seit 500ms; `'commit'`: nur Netzwerkantwort empfangen |

Gibt die Haupt-Ressourcen-Antwort zurueck. `null` bei Navigation zu `about:blank` oder gleicher URL mit anderem Hash.

```typescript
const response = await page.goto('https://example.com');
console.log(response?.status()); // 200

await page.goto('https://example.com', {
  waitUntil: 'networkidle',
  timeout: 30000
});
```

---

### page.goBack()

```typescript
page.goBack(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Navigation als abgeschlossen gilt |

Navigiert eine Seite zurueck in der Browser-History. `null` wenn kein vorheriger Eintrag existiert.

```typescript
await page.goBack();
await page.goBack({ waitUntil: 'domcontentloaded' });
```

---

### page.goForward()

```typescript
page.goForward(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Navigation als abgeschlossen gilt |

Navigiert vorwaerts in der Browser-History. `null` wenn kein naechster Eintrag existiert.

```typescript
await page.goForward();
```

---

### page.reload()

```typescript
page.reload(options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Reload als abgeschlossen gilt |

Laedt die aktuelle Seite neu (entspricht `Ctrl+R`/`F5`).

```typescript
await page.reload();
await page.reload({ waitUntil: 'networkidle' });
```

---

### page.url()

```typescript
page.url(): string
```

Gibt die aktuelle URL der Seite zurueck (synchron, kein Promise).

```typescript
console.log(page.url()); // 'https://example.com/path'
```

---

### page.title()

```typescript
page.title(): Promise<string>
```

Gibt den Titel (`<title>`-Element) der Seite zurueck.

```typescript
const title = await page.title();
expect(title).toBe('Meine Seite');
```

---

## 2. Seiteninhalte lesen/setzen

### page.content()

```typescript
page.content(): Promise<string>
```

Gibt den vollstaendigen HTML-Inhalt der Seite zurueck, einschliesslich Doctype.

```typescript
const html = await page.content();
console.log(html.includes('<title>'));
```

---

### page.setContent()

```typescript
page.setContent(html: string, options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `html` | `string` | ja | — | Vollstaendiger HTML-String |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Setzen als abgeschlossen gilt |

```typescript
await page.setContent('<h1>Hallo Welt</h1>');
await page.setContent('<html><body><p>Test</p></body></html>', {
  waitUntil: 'domcontentloaded'
});
```

---

### page.getAttribute()

```typescript
page.getAttribute(selector: string, name: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | CSS/XPath-Selektor |
| `name` | `string` | ja | — | Attribut-Name |
| `options.strict` | `boolean` | nein | `false` | Fehler wenn mehr als ein Element gefunden |
| `options.timeout` | `number` | nein | `defaultTimeout` | Max. Wartezeit in ms |

```typescript
const href = await page.getAttribute('a', 'href');
const checked = await page.getAttribute('input[type=checkbox]', 'checked');
```

---

### page.innerHTML()

```typescript
page.innerHTML(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Gibt das innere HTML des ersten gematchten Elements zurueck.

```typescript
const content = await page.innerHTML('.article-body');
```

---

### page.innerText()

```typescript
page.innerText(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Gibt den sichtbaren Text (wie `HTMLElement.innerText`) zurueck; ignoriert versteckte Elemente.

```typescript
const text = await page.innerText('h1');
```

---

### page.textContent()

```typescript
page.textContent(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

Gibt den `textContent`-Wert zurueck (inkl. versteckter Elemente). `null` wenn kein Element gefunden.

```typescript
const text = await page.textContent('#description');
```

---

### page.inputValue()

```typescript
page.inputValue(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

Gibt den aktuellen Wert von `<input>`, `<textarea>` oder `<select>` zurueck.

```typescript
const value = await page.inputValue('input[name=email]');
```

---

### page.isChecked()

```typescript
page.isChecked(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Prueft ob Checkbox oder Radio-Button angehakt ist.

```typescript
const checked = await page.isChecked('#terms');
```

---

### page.isDisabled()

```typescript
page.isDisabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Prueft ob Element deaktiviert ist (`disabled`-Attribut oder `aria-disabled`).

```typescript
if (await page.isDisabled('button[type=submit]')) { /* ... */ }
```

---

### page.isEditable()

```typescript
page.isEditable(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Prueft ob Element editierbar ist (weder `disabled` noch `readonly`).

```typescript
const editable = await page.isEditable('input[name=username]');
```

---

### page.isEnabled()

```typescript
page.isEnabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Gegenteil von `isDisabled()`.

```typescript
await expect(page.locator('button')).toBeEnabled();
```

---

### page.isHidden()

```typescript
page.isHidden(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Gibt `true` wenn Element versteckt ist ODER kein Element gefunden wurde.

```typescript
const hidden = await page.isHidden('.spinner');
```

---

### page.isVisible()

```typescript
page.isVisible(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

Gibt `true` wenn Element sichtbar ist (nicht `display:none`, nicht `visibility:hidden`, nicht `opacity:0`).

```typescript
const visible = await page.isVisible('.success-message');
```

---

## 3. Locator-Fabrik-Methoden

### page.locator()

```typescript
page.locator(selector: string, options?: {
  has?: Locator,
  hasNot?: Locator,
  hasText?: string | RegExp,
  hasNotText?: string | RegExp
}): Locator
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | CSS, XPath, text=, role=, etc. |
| `options.has` | `Locator` | nein | — | Element muss diesen Sub-Locator enthalten |
| `options.hasNot` | `Locator` | nein | — | Element darf diesen Sub-Locator NICHT enthalten |
| `options.hasText` | `string\|RegExp` | nein | — | Element muss diesen Text (Teilstring) enthalten |
| `options.hasNotText` | `string\|RegExp` | nein | — | Element darf diesen Text NICHT enthalten |

Erstellt einen Locator. **Empfohlene Methode** gegenueber direkten Selector-basierten Methoden.

```typescript
const button = page.locator('button.primary');
await button.click();

// Mit Filter
const row = page.locator('tr', { hasText: 'Max Mustermann' });
await row.locator('td.actions button').click();

// Kombiniert
const item = page.locator('.list-item', {
  has: page.locator('.badge'),
  hasNotText: 'archived'
});
```

---

### page.getByRole()

```typescript
page.getByRole(role: AriaRole, options?: {
  checked?: boolean,
  description?: string | RegExp,
  disabled?: boolean,
  exact?: boolean,
  expanded?: boolean,
  includeHidden?: boolean,
  level?: number,
  name?: string | RegExp,
  pressed?: boolean,
  selected?: boolean
}): Locator
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `role` | `AriaRole` | — | ARIA-Rolle (button, link, textbox, checkbox, ...) |
| `name` | `string\|RegExp` | — | Zugaenglicher Name (case-insensitiv, Teilstring) |
| `exact` | `boolean` | `false` | Exaktes Matching fuer `name` |
| `checked` | `boolean` | — | `aria-checked` |
| `disabled` | `boolean` | — | `aria-disabled` oder `disabled` |
| `expanded` | `boolean` | — | `aria-expanded` |
| `includeHidden` | `boolean` | `false` | ARIA-versteckte Elemente einschliessen |
| `level` | `number` | — | Fuer headings: 1–6 |
| `pressed` | `boolean` | — | `aria-pressed` |
| `selected` | `boolean` | — | `aria-selected` |
| `description` | `string\|RegExp` | — | Zugaengliche Beschreibung |

```typescript
await page.getByRole('button', { name: 'Absenden' }).click();
await page.getByRole('heading', { name: /willkommen/i, level: 1 });
await page.getByRole('checkbox', { name: 'Newsletter' }).check();
await page.getByRole('textbox', { name: 'E-Mail' }).fill('test@example.com');
```

---

### page.getByText()

```typescript
page.getByText(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string\|RegExp` | ja | — | Suchtext (Teilstring bei String, case-insensitiv) |
| `options.exact` | `boolean` | nein | `false` | Exaktes, case-sensitives Matching |

```typescript
page.getByText('Anmelden');
page.getByText(/anmelden/i);
page.getByText('Anmelden', { exact: true });
```

---

### page.getByLabel()

```typescript
page.getByLabel(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Findet Formular-Elemente, die mit einem `<label>`-Element (via `for`/`aria-labelledby`/`aria-label`) verbunden sind.

```typescript
await page.getByLabel('Passwort').fill('geheim123');
await page.getByLabel(/e-mail/i).fill('test@example.com');
```

---

### page.getByPlaceholder()

```typescript
page.getByPlaceholder(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Findet Inputs/Textareas mit passendem `placeholder`-Attribut.

```typescript
await page.getByPlaceholder('Benutzername').fill('admin');
await page.getByPlaceholder(/suche/i).fill('Playwright');
```

---

### page.getByAltText()

```typescript
page.getByAltText(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Findet Elemente (meist `<img>`) mit passendem `alt`-Attribut.

```typescript
await page.getByAltText('Firmenlogo').click();
await expect(page.getByAltText('Produktbild')).toBeVisible();
```

---

### page.getByTitle()

```typescript
page.getByTitle(text: string | RegExp, options?: {
  exact?: boolean
}): Locator
```

Findet Elemente mit passendem `title`-Attribut.

```typescript
await page.getByTitle('Schliessen').click();
await page.getByTitle(/tooltip/i);
```

---

### page.getByTestId()

```typescript
page.getByTestId(testId: string | RegExp): Locator
```

Findet Elemente anhand des `data-testid`-Attributs (konfigurierbar via `playwright.config.ts`).

```typescript
await page.getByTestId('submit-button').click();
await page.getByTestId(/user-row-\d+/).first();
```

---

### page.frameLocator()

```typescript
page.frameLocator(selector: string): FrameLocator
```

Erstellt einen Locator fuer Inhalte innerhalb eines `<iframe>`. Alle weiteren Methoden werden auf den iframe-Inhalt angewendet.

```typescript
const frame = page.frameLocator('#my-iframe');
await frame.getByRole('button', { name: 'Submit' }).click();

// Verschachtelte iframes
const nested = page.frameLocator('.outer').frameLocator('.inner');
await nested.getByText('Hallo').click();
```

---

## 4. Frame-Verwaltung

### page.frames()

```typescript
page.frames(): Frame[]
```

Gibt alle Frames der Seite zurueck (inkl. Haupt-Frame und iframes).

```typescript
const frames = page.frames();
console.log(frames.length);
```

---

### page.frame()

```typescript
page.frame(frameSelector: string | {
  name?: string,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean)
}): Frame | null
```

| Parameter | Typ | Beschreibung |
|---|---|---|
| `frameSelector` | `string` | Frame-Name als String |
| `frameSelector.name` | `string` | Name-Attribut des iframes |
| `frameSelector.url` | `string\|RegExp\|...` | URL des Frames (Match) |

```typescript
const frame = page.frame({ url: /my-frame/ });
const namedFrame = page.frame('my-frame-name');
```

---

### page.mainFrame()

```typescript
page.mainFrame(): Frame
```

Gibt den Haupt-Frame der Seite zurueck.

```typescript
const main = page.mainFrame();
```

---

## 5. Elementinteraktionen (Selector-basiert, deprecated)

**Hinweis:** Diese Methoden akzeptieren direkte CSS-/XPath-Selektoren. Laut Playwright-Dokumentation
sollte stattdessen `page.locator()` + `locator.click()` etc. verwendet werden.
Sie werden aber weiterhin unterstuetzt.

### page.click()

```typescript
page.click(selector: string, options?: {
  button?: 'left' | 'right' | 'middle',
  clickCount?: number,
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `selector` | `string` | — | CSS/XPath-Selektor |
| `button` | `string` | `'left'` | Maustaste |
| `clickCount` | `number` | `1` | Anzahl Klicks |
| `delay` | `number` | `0` | Ms zwischen mousedown und mouseup |
| `force` | `boolean` | `false` | Actionability-Checks ueberspringen |
| `modifiers` | `string[]` | `[]` | Zusaetzliche Tasten halten |
| `noWaitAfter` | `boolean` | `false` | Nicht auf Navigationen warten |
| `position` | `{x,y}` | Element-Mitte | Klick-Position relativ zum Element |
| `strict` | `boolean` | `false` | Fehler wenn mehrere Elemente gefunden |
| `timeout` | `number` | `defaultTimeout` | Max. Wartezeit in ms |
| `trial` | `boolean` | `false` | Nur pruefen ohne auszufuehren |

```typescript
await page.click('button.submit');
await page.click('#menu-item', { button: 'right' });
await page.click('a', { modifiers: ['Control'] }); // Ctrl+Click
await page.click('.target', { position: { x: 10, y: 5 } });
```

---

### page.dblclick()

```typescript
page.dblclick(selector: string, options?: {
  button?: 'left' | 'right' | 'middle',
  delay?: number,
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Doppelklick auf Element. Parameter identisch mit `click()` (ohne `clickCount`).

```typescript
await page.dblclick('.editable-cell');
```

---

### page.check()

```typescript
page.check(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Aktiviert eine Checkbox oder einen Radio-Button (kein Fehler wenn bereits gecheckt).

```typescript
await page.check('#accept-terms');
await page.check('input[name=newsletter]', { force: true });
```

---

### page.uncheck()

```typescript
page.uncheck(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Deaktiviert eine Checkbox (kein Fehler wenn bereits unchecked).

```typescript
await page.uncheck('#newsletter');
```

---

### page.setChecked()

```typescript
page.setChecked(selector: string, checked: boolean, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `selector` | `string` | ja | CSS/XPath-Selektor |
| `checked` | `boolean` | ja | `true` = ankracken, `false` = abwählen |

```typescript
await page.setChecked('#newsletter', true);
await page.setChecked('#terms', false);
```

---

### page.fill()

```typescript
page.fill(selector: string, value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `selector` | `string` | ja | Input/Textarea-Selektor |
| `value` | `string` | ja | Einzufuegender Text (ersetzt vorhandenen Wert) |

Lscht bestehenden Wert und fuellt Feld. Fuer `<input type=file>` stattdessen `setInputFiles()` verwenden.

```typescript
await page.fill('input[name=email]', 'test@example.com');
await page.fill('textarea', 'Mein Kommentar');
```

---

### page.focus()

```typescript
page.focus(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Setzt Fokus auf Element.

```typescript
await page.focus('input[name=search]');
```

---

### page.hover()

```typescript
page.hover(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Bewegt Maus ueber Element (loest `mouseenter`/`mousemove` aus).

```typescript
await page.hover('.dropdown-trigger');
await page.hover('canvas', { position: { x: 100, y: 200 } });
```

---

### page.press()

```typescript
page.press(selector: string, key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | Zu fokussierendes Element |
| `key` | `string` | ja | — | Tastenkombination (z.B. `'Enter'`, `'Tab'`, `'Control+a'`, `'F5'`) |
| `options.delay` | `number` | nein | `0` | Ms zwischen keydown und keyup |

```typescript
await page.press('input', 'Enter');
await page.press('body', 'Control+a');
await page.press('[contenteditable]', 'Shift+End');
```

---

### page.type()

```typescript
page.type(selector: string, text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated** — Verwende `page.locator().pressSequentially()`. Simuliert echte Tastatureingaben
(einen Buchstaben nach dem anderen), ohne bestehenden Inhalt zu lschen.

```typescript
await page.type('input', 'Hallo', { delay: 50 });
```

---

### page.tap()

```typescript
page.tap(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch-Tap auf Element (Touchscreen-Simulation erforderlich).

```typescript
await page.tap('.mobile-menu-button');
```

---

### page.selectOption()

```typescript
page.selectOption(
  selector: string,
  values: null | string | ElementHandle | string[] | SelectOptionObject | ElementHandle[] | SelectOptionObject[],
  options?: {
    force?: boolean,
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<string[]>
```

| `values` Varianten | Beschreibung |
|---|---|
| `'value'` | Option nach value-Attribut |
| `{ label: 'Text' }` | Option nach sichtbarem Text |
| `{ index: 2 }` | Option nach Index |
| `['val1', 'val2']` | Mehrfachauswahl |
| `null` | Selektion aufheben |

Gibt Array der ausgewaehlten `value`-Attribute zurueck.

```typescript
await page.selectOption('select', 'de');
await page.selectOption('select', { label: 'Deutschland' });
await page.selectOption('select[multiple]', ['de', 'at', 'ch']);
```

---

### page.setInputFiles()

```typescript
page.setInputFiles(
  selector: string,
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

| `files` Varianten | Beschreibung |
|---|---|
| `'path/to/file.pdf'` | Einzelne Datei per Pfad |
| `['file1.pdf', 'file2.pdf']` | Mehrere Dateien per Pfad |
| `{ name, mimeType, buffer }` | Datei im Speicher (kein Dateisystem noetig) |
| `[]` | Alle Dateien entfernen |

```typescript
await page.setInputFiles('input[type=file]', 'test.pdf');
await page.setInputFiles('input', ['file1.pdf', 'file2.jpg']);
await page.setInputFiles('input', {
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Hallo')
});
await page.setInputFiles('input', []); // Reset
```

---

### page.dispatchEvent()

```typescript
page.dispatchEvent(
  selector: string,
  type: string,
  eventInit?: EvaluationArgument,
  options?: {
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Loest ein DOM-Event auf dem Element aus (z.B. `'click'`, `'input'`, `'change'`, Custom Events).

```typescript
await page.dispatchEvent('button', 'click');
await page.dispatchEvent('#field', 'input', { data: 'neuer Wert' });
await page.dispatchEvent('.el', 'custom:event', { detail: { key: 'value' } });
```

---

### page.dragAndDrop()

```typescript
page.dragAndDrop(source: string, target: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  sourcePosition?: { x: number, y: number },
  steps?: number,
  strict?: boolean,
  targetPosition?: { x: number, y: number },
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `source` | `string` | ja | — | Selektor des zu ziehenden Elements |
| `target` | `string` | ja | — | Selektor des Zielelements |
| `sourcePosition` | `{x,y}` | nein | Element-Mitte | Startposition |
| `targetPosition` | `{x,y}` | nein | Element-Mitte | Zielposition |
| `steps` | `number` | nein | `1` | Anzahl Bewegungsschritte |

```typescript
await page.dragAndDrop('#source', '#target');
await page.dragAndDrop('.card', '.dropzone', { steps: 10 });
```

---

### page.selectText()

```typescript
page.selectText(selector: string, options?: {
  force?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Selektiert den Text eines Input- oder Textarea-Elements (`select()`).

```typescript
await page.selectText('input[name=title]');
// Danach: Ctrl+C oder Typing ueberschreibt den Inhalt
```

---

## 6. JavaScript-Ausfuehrung

### page.evaluate()

```typescript
page.evaluate<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pageFunction` | `function\|string` | ja | Funktion oder JS-Code-String, der im Browser ausgefuehrt wird |
| `arg` | `Serializable\|JSHandle` | nein | Argument wird in die Funktion uebergeben |

Gibt serialisierten Rueckgabewert zurueck (JSON-faehig). Nicht-serialisierbare Werte werden `undefined`.

```typescript
const url = await page.evaluate(() => window.location.href);
const title = await page.evaluate('document.title');

const result = await page.evaluate(({ a, b }) => a + b, { a: 1, b: 2 });

// Mit DOM-Manipulation
const count = await page.evaluate(() => document.querySelectorAll('li').length);

// Elementhandle uebergeben
const el = await page.locator('h1').elementHandle();
const text = await page.evaluate(el => el.textContent, el);
```

---

### page.evaluateHandle()

```typescript
page.evaluateHandle<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

Wie `evaluate()`, gibt aber ein `JSHandle` zurueck (kein JSON-Serialisierungs-Overhead). Nuetzlich
fuer komplexe Browser-Objekte.

```typescript
const arrayHandle = await page.evaluateHandle(() => Array.from(document.querySelectorAll('a')));
const len = await page.evaluate(arr => arr.length, arrayHandle);
await arrayHandle.dispose();
```

---

### page.exposeFunction()

```typescript
page.exposeFunction(name: string, callback: Function): Promise<Disposable>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Funktionsname auf `window` |
| `callback` | `Function` | ja | Node.js-Funktion, die im Browser aufrufbar ist |

Macht eine Node.js-Funktion unter `window[name]` im Browser aufrufbar. Seiten-Reloads behalten die Exposition.

```typescript
await page.exposeFunction('sha256', async (text: string) => {
  const { createHash } = require('crypto');
  return createHash('sha256').update(text).digest('hex');
});
const hash = await page.evaluate(() => (window as any).sha256('Hallo'));
```

---

### page.exposeBinding()

```typescript
page.exposeBinding(
  name: string,
  callback: (source: BindingSource, ...args: any[]) => any,
  options?: { handle?: boolean }
): Promise<Disposable>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Funktionsname auf `window` |
| `callback` | `Function` | ja | Callback mit Kontext-Objekt als erstem Argument |
| `options.handle` | `boolean` | nein | Wenn `true`: Argumente als JSHandles uebergeben |

Wie `exposeFunction()`, der Callback erhaelt zusaetzlich ein `source`-Objekt mit `{browserContext, page, frame}`.

```typescript
await page.exposeBinding('openBrowser', async (source, url) => {
  console.log(`Aufgerufen von ${source.frame.url()}`);
  await source.page.goto(url);
});
```

---

### page.addInitScript()

```typescript
page.addInitScript(
  script: Function | string | { path?: string, content?: string },
  arg?: Serializable
): Promise<Disposable>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `script` | `Function\|string\|{path?,content?}` | ja | Skript, das VOR jedem Seitenlade-Vorgang ausgefuehrt wird |
| `arg` | `Serializable` | nein | Argument fuer die Funktion |

Wird bei jedem Navigation-Event erneut ausgefuehrt (auch nach `reload()`).

```typescript
// Globale Variable setzen bevor Seite laedt
await page.addInitScript(() => {
  (window as any).__TEST_MODE__ = true;
});

// Mit Argument
await page.addInitScript(({ key, value }) => {
  (window as any)[key] = value;
}, { key: 'API_BASE', value: 'http://mock-server' });

// Aus Datei
await page.addInitScript({ path: './preload.js' });
```

Gibt ein `Disposable` zurueck — `await script[Symbol.asyncDispose]()` entfernt das Skript.

---

## 7. Skript- und Style-Injektion

### page.addScriptTag()

```typescript
page.addScriptTag(options?: {
  content?: string,
  path?: string,
  type?: string,
  url?: string
}): Promise<ElementHandle>
```

| Option | Typ | Beschreibung |
|---|---|---|
| `content` | `string` | Inline-JS-Code |
| `path` | `string` | Lokaler Dateipfad (automatisch base64-kodiert) |
| `type` | `string` | Script-type-Attribut (z.B. `'module'`) |
| `url` | `string` | Externe URL |

Fuegt ein `<script>`-Tag in den `<head>` der Seite ein.

```typescript
await page.addScriptTag({ url: 'https://cdn.example.com/lib.js' });
await page.addScriptTag({ content: 'window.__LOADED = true;' });
await page.addScriptTag({ path: './fixtures/helper.js', type: 'module' });
```

---

### page.addStyleTag()

```typescript
page.addStyleTag(options?: {
  content?: string,
  path?: string,
  url?: string
}): Promise<ElementHandle>
```

Fuegt ein `<style>`-Tag oder `<link rel=stylesheet>` ein.

```typescript
await page.addStyleTag({ content: 'body { display: none }' });
await page.addStyleTag({ url: 'https://cdn.example.com/style.css' });
await page.addStyleTag({ path: './fixtures/test.css' });
```

---

## 8. Netzwerk / Routing

### page.route()

```typescript
page.route(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  handler: (route: Route, request: Request) => void | Promise<void>,
  options?: { times?: number }
): Promise<Disposable>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `url` | `string\|RegExp\|URLPattern\|Function` | ja | URL-Pattern oder Filterfunktion |
| `handler` | `Function` | ja | Callback fuer jede gematchte Anfrage |
| `options.times` | `number` | nein | Max. Anzahl Aufrufe des Handlers |

Interseptiert Netzwerkanfragen. Innerhalb des Handlers muss `route.fulfill()`, `route.abort()` oder
`route.continue()` aufgerufen werden.

```typescript
// Anfrage abbrechen
await page.route('**/*.png', route => route.abort());

// Mocken
await page.route('**/api/users', route => route.fulfill({
  status: 200,
  contentType: 'application/json',
  body: JSON.stringify([{ id: 1, name: 'Test' }])
}));

// Modifizieren
await page.route('**/api/**', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.extra = 'hinzugefuegt';
  await route.fulfill({ response, json });
});

// Nur einmal
await page.route('**/api/data', route => route.fulfill({ body: '[]' }), { times: 1 });
```

---

### page.unroute()

```typescript
page.unroute(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  handler?: Function
): Promise<void>
```

Entfernt Route-Handler. Ohne `handler` werden alle Handler fuer die URL entfernt.

```typescript
await page.unroute('**/*.png');
await page.unroute('**/api/**', specificHandler);
```

---

### page.unrouteAll()

```typescript
page.unrouteAll(options?: {
  behavior?: 'wait' | 'ignoreErrors' | 'default'
}): Promise<void>
```

Entfernt alle Route-Handler.

```typescript
await page.unrouteAll();
await page.unrouteAll({ behavior: 'wait' });
```

---

### page.routeFromHAR()

```typescript
page.routeFromHAR(har: string, options?: {
  content?: 'omit' | 'embed' | 'attach',
  fallback?: 'abort' | 'continue',
  notFound?: 'abort' | 'fallback',
  update?: boolean,
  updateContent?: 'embed' | 'attach',
  updateMode?: 'full' | 'minimal',
  url?: string | RegExp
}): Promise<Disposable>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `har` | `string` | — | Pfad zur HAR-Datei |
| `fallback` | `string` | `'abort'` | Was tun wenn kein Match: `'abort'` oder `'continue'` |
| `notFound` | `string` | `'abort'` | Was tun wenn HAR keinen Eintrag hat |
| `update` | `boolean` | `false` | HAR-Datei automatisch aktualisieren |
| `url` | `string\|RegExp` | — | Nur Anfragen an diese URL(s) |

```typescript
await page.routeFromHAR('./tests/fixtures/api.har');
await page.routeFromHAR('./api.har', { fallback: 'continue', url: '**/api/**' });
```

---

### page.requests()

```typescript
page.requests(): Promise<Request[]>
```

Gibt bis zu 100 neueste Netzwerkanfragen zurueck.

```typescript
const requests = await page.requests();
const apiRequests = requests.filter(r => r.url().includes('/api/'));
```

---

### page.setExtraHTTPHeaders()

```typescript
page.setExtraHTTPHeaders(headers: { [key: string]: string }): Promise<void>
```

Setzt zusaetzliche HTTP-Header fuer alle Anfragen der Seite.

```typescript
await page.setExtraHTTPHeaders({
  'Authorization': 'Bearer my-token',
  'X-Custom-Header': 'value'
});
```

---

## 9. Warten / Synchronisation

### page.waitForLoadState()

```typescript
page.waitForLoadState(
  state?: 'load' | 'domcontentloaded' | 'networkidle',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `state` | `string` | nein | `'load'` | Gewuenschter Lade-Zustand |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |

```typescript
await page.waitForLoadState('networkidle');
await page.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

---

### page.waitForNavigation()

```typescript
page.waitForNavigation(options?: {
  timeout?: number,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean),
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

**Deprecated** — Verwende `page.waitForURL()` oder `page.goto()` mit `waitUntil`.
Wartet auf die naechste Navigation.

```typescript
await Promise.all([
  page.waitForNavigation(),
  page.click('a.nav-link')
]);
```

---

### page.waitForURL()

```typescript
page.waitForURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    timeout?: number,
    waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
  }
): Promise<void>
```

Wartet bis die Seiten-URL mit dem Muster uebereinstimmt.

```typescript
await page.waitForURL('**/dashboard');
await page.waitForURL(/profile/, { waitUntil: 'networkidle' });
await page.waitForURL(url => url.searchParams.get('tab') === 'settings');
```

---

### page.waitForFunction()

```typescript
page.waitForFunction<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg,
  options?: {
    polling?: number | 'raf',
    timeout?: number
  }
): Promise<JSHandle<T>>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `pageFunction` | `Function\|string` | ja | — | Funktion im Browser-Kontext, muss truthy zurueckgeben |
| `arg` | `any` | nein | — | Argument fuer die Funktion |
| `options.polling` | `number\|'raf'` | nein | `'raf'` | Polling-Intervall in ms oder `'raf'` |
| `options.timeout` | `number` | nein | `defaultTimeout` | Max. Wartezeit in ms |

```typescript
await page.waitForFunction(() => document.readyState === 'complete');
await page.waitForFunction(n => window.scrollY > n, 200, { polling: 100 });

const handle = await page.waitForFunction('window.__APP_READY === true');
await handle.dispose();
```

---

### page.waitForSelector()

```typescript
page.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<ElementHandle | null>
```

**Deprecated** — Verwende `page.locator().waitFor()`.

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `state` | `string` | `'visible'` | Gewuenschter Zustand |
| `strict` | `boolean` | `false` | Fehler bei mehreren Elementen |
| `timeout` | `number` | `defaultTimeout` | Max. Wartezeit in ms |

```typescript
const el = await page.waitForSelector('.success-message');
await page.waitForSelector('.spinner', { state: 'hidden' });
```

---

### page.waitForRequest()

```typescript
page.waitForRequest(
  urlOrPredicate: string | RegExp | ((request: Request) => boolean | Promise<boolean>),
  options?: { timeout?: number }
): Promise<Request>
```

Wartet auf eine eingehende Netzwerkanfrage.

```typescript
const request = await page.waitForRequest('**/api/login');
const postRequest = await page.waitForRequest(
  req => req.url().includes('/api/') && req.method() === 'POST'
);
```

---

### page.waitForResponse()

```typescript
page.waitForResponse(
  urlOrPredicate: string | RegExp | ((response: Response) => boolean | Promise<boolean>),
  options?: { timeout?: number }
): Promise<Response>
```

Wartet auf eine Netzwerkantwort.

```typescript
const response = await page.waitForResponse('**/api/data');
const [response2] = await Promise.all([
  page.waitForResponse(r => r.url().includes('/api/save') && r.status() === 200),
  page.click('#save-button')
]);
const json = await response2.json();
```

---

### page.waitForEvent()

```typescript
page.waitForEvent(event: string, optionsOrPredicate?: {
  predicate?: Function,
  timeout?: number
} | Function): Promise<any>
```

Wartet auf ein Page-Event.

```typescript
const popup = await page.waitForEvent('popup');
const download = await page.waitForEvent('download');

// Mit Predicate
const dialog = await page.waitForEvent('dialog', {
  predicate: d => d.type() === 'confirm'
});

// Mit Timeout
const frame = await page.waitForEvent('frameattached', { timeout: 5000 });
```

---

### page.waitForPopup()

```typescript
page.waitForPopup(
  callback: () => Promise<void>,
  options?: { timeout?: number }
): Promise<Page>
```

Wartet auf ein Popup das durch `callback` ausgeloest wird.

```typescript
const popup = await page.waitForPopup(async () => {
  await page.click('a[target=_blank]');
});
await popup.waitForLoadState();
```

---

## 10. Screenshots & PDF

### page.screenshot()

```typescript
page.screenshot(options?: {
  animations?: 'disabled' | 'allow',
  caret?: 'hide' | 'initial',
  clip?: { x: number, y: number, width: number, height: number },
  fullPage?: boolean,
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
| `animations` | `string` | `'allow'` | CSS-Animationen deaktivieren |
| `caret` | `string` | `'hide'` | Text-Cursor verstecken |
| `clip` | `object` | — | Nur diesen Bereich aufnehmen |
| `fullPage` | `boolean` | `false` | Ganze Seite (auch nicht-sichtbarer Bereich) |
| `mask` | `Locator[]` | — | Diese Elemente mit `maskColor` ueberdecken |
| `maskColor` | `string` | `'#FF00FF'` | Farbe fuer maskierte Bereiche |
| `omitBackground` | `boolean` | `false` | Transparenter Hintergrund (nur PNG) |
| `path` | `string` | — | Speicherpfad |
| `quality` | `number` | `100` (PNG) | JPEG-Qualitaet 0–100 |
| `scale` | `string` | `'device'` | `'device'` respektiert devicePixelRatio |
| `type` | `string` | `'png'` | Bildformat |

```typescript
await page.screenshot({ path: 'screenshot.png' });
await page.screenshot({ fullPage: true, path: 'full.png' });
const buffer = await page.screenshot({ type: 'jpeg', quality: 80 });

// Bereiche ausblenden
await page.screenshot({
  mask: [page.locator('.user-avatar')],
  maskColor: '#aabbcc'
});

// Nur Viewport-Ausschnitt
await page.screenshot({
  clip: { x: 0, y: 0, width: 800, height: 600 }
});
```

---

### page.pdf()

```typescript
page.pdf(options?: {
  displayHeaderFooter?: boolean,
  footerTemplate?: string,
  format?: string,
  headerTemplate?: string,
  height?: string | number,
  landscape?: boolean,
  margin?: {
    top?: string | number,
    right?: string | number,
    bottom?: string | number,
    left?: string | number
  },
  outline?: boolean,
  pageRanges?: string,
  path?: string,
  preferCSSPageSize?: boolean,
  printBackground?: boolean,
  scale?: number,
  tagged?: boolean,
  width?: string | number
}): Promise<Buffer>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `format` | `string` | `'Letter'` | Papierformat: `'A4'`, `'Letter'`, `'A3'`, etc. |
| `landscape` | `boolean` | `false` | Querformat |
| `printBackground` | `boolean` | `false` | Hintergrundfarben/-bilder |
| `displayHeaderFooter` | `boolean` | `false` | Kopf-/Fusszeile anzeigen |
| `headerTemplate` | `string` | — | HTML-Template fuer Header |
| `footerTemplate` | `string` | — | HTML-Template fuer Footer |
| `margin` | `object` | — | Seitenraender |
| `scale` | `number` | `1` | Skalierung (0.1–2) |
| `pageRanges` | `string` | — | z.B. `'1-5'`, `'8,10-12'` |
| `path` | `string` | — | Speicherpfad |
| `tagged` | `boolean` | `false` | Getaggtes PDF (Accessibility) |
| `outline` | `boolean` | `false` | PDF-Outline aus Headings |

Nur fuer Chromium verfuegbar.

```typescript
await page.pdf({ path: 'output.pdf', format: 'A4' });
await page.pdf({
  format: 'A4',
  landscape: true,
  printBackground: true,
  margin: { top: '20mm', right: '20mm', bottom: '20mm', left: '20mm' }
});

const pdfBuffer = await page.pdf({ format: 'A4' });
```

---

## 11. Browser-Konfiguration

### page.setViewportSize()

```typescript
page.setViewportSize(viewportSize: {
  width: number,
  height: number
}): Promise<void>
```

```typescript
await page.setViewportSize({ width: 1280, height: 720 });
await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
```

---

### page.viewportSize()

```typescript
page.viewportSize(): { width: number, height: number } | null
```

Gibt aktuelle Viewport-Groesse zurueck (`null` wenn nicht gesetzt).

```typescript
const viewport = page.viewportSize();
console.log(viewport?.width); // 1280
```

---

### page.emulateMedia()

```typescript
page.emulateMedia(options?: {
  colorScheme?: null | 'light' | 'dark' | 'no-preference',
  contrast?: null | 'no-preference' | 'more',
  forcedColors?: null | 'active' | 'none',
  media?: null | 'screen' | 'print',
  reducedMotion?: null | 'reduce' | 'no-preference'
}): Promise<void>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `colorScheme` | `string\|null` | — | Farbschema-Emulation; `null` = reset |
| `contrast` | `string\|null` | — | Kontrastpraeferenz |
| `forcedColors` | `string\|null` | — | Windows Forced Colors Mode |
| `media` | `string\|null` | — | CSS-Medientyp; `null` = reset |
| `reducedMotion` | `string\|null` | — | Bewegungsreduzierung |

```typescript
await page.emulateMedia({ colorScheme: 'dark' });
await page.emulateMedia({ media: 'print' });
await page.emulateMedia({ colorScheme: null }); // Reset
```

---

### page.setDefaultTimeout()

```typescript
page.setDefaultTimeout(timeout: number): void
```

Setzt Standard-Timeout fuer alle Aktionen UND Assertions (in ms). `0` = unbegrenzt.

```typescript
page.setDefaultTimeout(10000); // 10 Sekunden
```

---

### page.setDefaultNavigationTimeout()

```typescript
page.setDefaultNavigationTimeout(timeout: number): void
```

Setzt Standard-Timeout nur fuer Navigations-Methoden (`goto`, `goBack`, etc.).

```typescript
page.setDefaultNavigationTimeout(30000);
```

---

## 12. Event-Handling / Listener

### page.on()

```typescript
page.on(event: string, listener: Function): Page
```

Registriert dauerhaften Event-Listener. Gibt `Page` zurueck (chainable).

```typescript
page.on('console', msg => console.log('Browser:', msg.text()));
page.on('pageerror', err => console.error('Seiten-Fehler:', err.message));
page.on('dialog', async dialog => {
  console.log(dialog.message());
  await dialog.accept();
});
page.on('download', download => {
  console.log('Download gestartet:', download.suggestedFilename());
});
page.on('request', request => {
  if (request.url().includes('/api/')) {
    console.log(`API-Anfrage: ${request.method()} ${request.url()}`);
  }
});
```

---

### page.once()

```typescript
page.once(event: string, listener: Function): Page
```

Wie `on()`, wird aber nach dem ersten Aufruf automatisch entfernt.

```typescript
page.once('dialog', dialog => dialog.accept());
```

---

### page.off()

```typescript
page.off(event: string, listener: Function): Page
```

Entfernt einen spezifischen Event-Listener.

```typescript
const handler = (msg: ConsoleMessage) => console.log(msg.text());
page.on('console', handler);
// ...
page.off('console', handler);
```

---

### page.removeAllListeners()

```typescript
page.removeAllListeners(type?: string, options?: {
  behavior?: 'wait' | 'ignoreErrors' | 'default'
}): Promise<void>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `type` | `string` | nein | Event-Typ; ohne = alle entfernen |
| `options.behavior` | `string` | nein | `'wait'`: auf laufende Handler warten; `'ignoreErrors'`: Fehler ignorieren |

```typescript
await page.removeAllListeners('console');
await page.removeAllListeners(); // Alle
```

---

## 13. Diverse Hilfsmethoden

### page.context()

```typescript
page.context(): BrowserContext
```

Gibt den `BrowserContext` zurueck, zu dem diese Seite gehoert.

```typescript
const context = page.context();
await context.clearCookies();
```

---

### page.opener()

```typescript
page.opener(): Promise<Page | null>
```

Gibt die Seite zurueck, die dieses Popup geoeffnet hat. `null` fuer normale Seiten.

```typescript
const opener = await page.opener();
if (opener) {
  console.log('Geoeffnet von:', opener.url());
}
```

---

### page.isClosed()

```typescript
page.isClosed(): boolean
```

Gibt `true` wenn die Seite geschlossen wurde.

```typescript
if (!page.isClosed()) {
  await page.close();
}
```

---

### page.close()

```typescript
page.close(options?: {
  reason?: string,
  runBeforeUnload?: boolean
}): Promise<void>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `reason` | `string` | — | Grund fuer Schliessung (bei kuenftigen Aktionen gemeldet) |
| `runBeforeUnload` | `boolean` | `false` | `beforeunload`-Handler ausfuehren |

```typescript
await page.close();
await page.close({ runBeforeUnload: true });
await page.close({ reason: 'Test abgeschlossen' });
```

---

### page.bringToFront()

```typescript
page.bringToFront(): Promise<void>
```

Bringt die Seite (Tab) in den Vordergrund.

```typescript
await page.bringToFront();
```

---

### page.pause()

```typescript
page.pause(): Promise<void>
```

Haelt die Test-Ausfuehrung an und oeffnet den Playwright-Inspector (nur im headed-Modus).

```typescript
await page.pause(); // Fuer Debugging
```

---

### page.ariaSnapshot()

```typescript
page.ariaSnapshot(options?: {
  boxes?: boolean,
  depth?: number,
  mode?: 'ai' | 'default',
  timeout?: number
}): Promise<string>
```

Erstellt einen ARIA-Accessibility-Tree-Snapshot als YAML-String.

```typescript
const snapshot = await page.ariaSnapshot();
expect(snapshot).toContain('button "Absenden"');

await page.ariaSnapshot({ mode: 'ai' });
```

---

### page.consoleMessages()

```typescript
page.consoleMessages(options?: {
  filter?: 'all' | 'since-navigation'
}): Promise<ConsoleMessage[]>
```

Gibt bis zu 200 zuletzt empfangene Konsolen-Nachrichten zurueck.

```typescript
const messages = await page.consoleMessages();
const errors = messages.filter(m => m.type() === 'error');
```

---

### page.pageErrors()

```typescript
page.pageErrors(options?: {
  filter?: 'all' | 'since-navigation'
}): Promise<Error[]>
```

Gibt bis zu 200 zuletzt erfasste ungefangene Fehler zurueck.

```typescript
const errors = await page.pageErrors();
if (errors.length > 0) {
  console.error('Seiten-Fehler gefunden:', errors[0].message);
}
```

---

### page.clearConsoleMessages()

```typescript
page.clearConsoleMessages(): Promise<void>
```

Leert den gespeicherten Konsolen-Nachrichten-Puffer.

```typescript
await page.clearConsoleMessages();
```

---

### page.clearPageErrors()

```typescript
page.clearPageErrors(): Promise<void>
```

Leert den gespeicherten Seiten-Fehler-Puffer.

```typescript
await page.clearPageErrors();
```

---

### page.addLocatorHandler()

```typescript
page.addLocatorHandler(
  locator: Locator,
  handler: (locator: Locator) => void | Promise<void>,
  options?: {
    noWaitAfter?: boolean,
    times?: number
  }
): Promise<Disposable>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `locator` | `Locator` | ja | Locator des Overlays/Popups |
| `handler` | `Function` | ja | Wird aufgerufen wenn Overlay erscheint und Actionability blockiert |
| `options.noWaitAfter` | `boolean` | nein | Nicht auf Verschwinden warten |
| `options.times` | `number` | nein | Max. Aufrufe (dann automatisch entfernt) |

Registriert Handler fuer Cookie-Banner, Modals etc. die Actionability-Checks blockieren.

```typescript
await page.addLocatorHandler(
  page.getByText('Cookie-Einstellungen'),
  async () => {
    await page.getByRole('button', { name: 'Alle akzeptieren' }).click();
  }
);
```

---

### page.removeLocatorHandler()

```typescript
page.removeLocatorHandler(locator: Locator): Promise<void>
```

Entfernt Handler fuer einen bestimmten Locator.

```typescript
await page.removeLocatorHandler(page.getByText('Cookie-Einstellungen'));
```

---

### page.pickLocator()

```typescript
page.pickLocator(): Promise<Locator>
```

Startet den interaktiven Locator-Picker (Playwright Inspector). Gibt den ausgewaehlten Locator zurueck.

```typescript
const locator = await page.pickLocator();
console.log(locator); // Locator-Objekt
```

---

### page.cancelPickLocator()

```typescript
page.cancelPickLocator(): Promise<void>
```

Bricht den Locator-Picker ab.

```typescript
await page.cancelPickLocator();
```

---

### page.hideHighlight()

```typescript
page.hideHighlight(): Promise<void>
```

Versteckt alle aktiven Locator-Highlight-Overlays.

```typescript
await page.hideHighlight();
```

---

### page.requestGC()

```typescript
page.requestGC(): Promise<void>
```

Fordert Garbage Collection im Browser an (experimentell, hilfreich fuer Memory-Leak-Tests).

```typescript
await page.requestGC();
```

---

## 14. Properties

### page.keyboard

```typescript
page.keyboard: Keyboard
```

Zugriff auf `Keyboard`-Objekt fuer Low-Level-Tastatureingaben.

```typescript
await page.keyboard.press('Enter');
await page.keyboard.type('Hallo Welt');
await page.keyboard.down('Shift');
await page.keyboard.up('Shift');
await page.keyboard.insertText('Unicode: é');
```

---

### page.mouse

```typescript
page.mouse: Mouse
```

Zugriff auf `Mouse`-Objekt fuer Low-Level-Mausoperationen.

```typescript
await page.mouse.move(100, 200);
await page.mouse.down();
await page.mouse.up();
await page.mouse.click(100, 200);
await page.mouse.dblclick(100, 200);
await page.mouse.wheel(0, 300); // Scrollen
```

---

### page.touchscreen

```typescript
page.touchscreen: Touchscreen
```

Zugriff auf `Touchscreen`-Objekt fuer Touch-Events.

```typescript
await page.touchscreen.tap(150, 250);
```

---

## 15. Events

Events werden mit `page.on(event, listener)` abonniert.

| Event | Payload-Typ | Beschreibung |
|---|---|---|
| `'close'` | `Page` | Seite wurde geschlossen |
| `'console'` | `ConsoleMessage` | Browser-Konsolen-Nachricht (log, warn, error, dir, ...) |
| `'crash'` | `Page` | Seite ist abgestuerzt (z.B. OOM) |
| `'dialog'` | `Dialog` | `alert()`, `confirm()`, `prompt()` oder `beforeunload` |
| `'download'` | `Download` | Download wird gestartet |
| `'error'` | `Error` | Ungefangene Ausnahme in der Seite |
| `'filechooser'` | `FileChooser` | Dateiauswahl-Dialog erscheint |
| `'frameattached'` | `Frame` | Neuer Frame wurde angehaengt |
| `'framedetached'` | `Frame` | Frame wurde entfernt |
| `'framenavigated'` | `Frame` | Frame hat navigiert |
| `'load'` | `Page` | `load`-Event der Seite |
| `'pageerror'` | `Error` | Ungefangener Fehler in Seite (wie `window.onerror`) |
| `'popup'` | `Page` | Popup-Seite wurde geoeffnet |
| `'request'` | `Request` | Netzwerkanfrage wurde gesendet |
| `'requestfailed'` | `Request` | Netzwerkanfrage ist fehlgeschlagen |
| `'requestfinished'` | `Request` | Netzwerkanfrage abgeschlossen |
| `'response'` | `Response` | Netzwerkantwort erhalten |
| `'websocket'` | `WebSocket` | Neues WebSocket-Objekt erstellt |
| `'worker'` | `Worker` | Web Worker wurde erstellt |
| `'domcontentloaded'` | `Page` | `DOMContentLoaded`-Event |

### Event-Beispiele

```typescript
// Console-Ausgaben abfangen
page.on('console', msg => {
  const type = msg.type();
  if (type === 'error') console.error('[BROWSER ERROR]', msg.text());
});

// Dialoge automatisch behandeln
page.on('dialog', async dialog => {
  if (dialog.type() === 'confirm') {
    await dialog.accept();
  } else {
    await dialog.dismiss();
  }
});

// Datei-Downloads
page.on('download', async download => {
  await download.saveAs('/tmp/' + download.suggestedFilename());
});

// Popups behandeln
page.on('popup', async popup => {
  await popup.waitForLoadState();
  console.log('Popup URL:', popup.url());
});

// Netzwerk-Monitoring
page.on('response', response => {
  if (!response.ok()) {
    console.warn(`HTTP ${response.status()} fuer ${response.url()}`);
  }
});

// File Chooser
page.on('filechooser', async fileChooser => {
  await fileChooser.setFiles('/path/to/file.pdf');
});

// Web Worker
page.on('worker', worker => {
  console.log('Worker erstellt:', worker.url());
});
```

---

## 16. Manifest

| Kategorie | Anzahl dokumentierter Mitglieder |
|---|---|
| Navigation | 6 Methoden (goto, goBack, goForward, reload, url, title) |
| Seiteninhalte | 9 Methoden (content, setContent, getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible) |
| Locator-Fabrik | 10 Methoden (locator, getByRole, getByText, getByLabel, getByPlaceholder, getByAltText, getByTitle, getByTestId, frameLocator) |
| Frame-Verwaltung | 3 Methoden (frames, frame, mainFrame) |
| Element-Interaktion | 16 Methoden (click, dblclick, check, uncheck, setChecked, fill, focus, hover, press, type, tap, selectOption, setInputFiles, dispatchEvent, dragAndDrop, selectText) |
| JavaScript | 5 Methoden (evaluate, evaluateHandle, exposeFunction, exposeBinding, addInitScript) |
| Skript/Style-Injektion | 2 Methoden (addScriptTag, addStyleTag) |
| Netzwerk/Routing | 5 Methoden (route, unroute, unrouteAll, routeFromHAR, requests, setExtraHTTPHeaders) |
| Warten/Sync | 8 Methoden (waitForLoadState, waitForNavigation, waitForURL, waitForFunction, waitForSelector, waitForRequest, waitForResponse, waitForEvent, waitForPopup) |
| Screenshots/PDF | 2 Methoden (screenshot, pdf) |
| Browser-Konfiguration | 5 Methoden (setViewportSize, viewportSize, emulateMedia, setDefaultTimeout, setDefaultNavigationTimeout) |
| Event-Handling | 4 Methoden (on, once, off, removeAllListeners) |
| Diverse | 14 Methoden (context, opener, isClosed, close, bringToFront, pause, ariaSnapshot, consoleMessages, pageErrors, clearConsoleMessages, clearPageErrors, addLocatorHandler, removeLocatorHandler, pickLocator, cancelPickLocator, hideHighlight, requestGC) |
| Properties | 3 (keyboard, mouse, touchscreen) |
| Events | 17 Events |

**Gesamt: ~102 Methoden/Properties + 17 Events**

**Fazit:** Die `Page`-Klasse ist das Herzst der Playwright-API. Sie vereint Navigation, Elementinteraktion
(via Selector und Locator), JavaScript-Evaluation, Netzwerk-Interception, Konfiguration und Event-Handling
in einer einzigen Klasse. Fuer neue Tests sollten Locator-basierte Methoden (`page.locator()`, `getBy*()`)
den veralteten direkten Selector-Methoden vorgezogen werden.

---

**Quelle:** https://playwright.dev/docs/api/class-page
