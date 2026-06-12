# Playwright class-frame: Vollstaendige API-Referenz

`Frame` repraesentiert einen einzelnen Frame (Haupt-Frame oder iframe) innerhalb einer Seite.
Viele Methoden der `Page`-Klasse delegieren intern an den Haupt-Frame (`page.mainFrame()`).
Beim direkten Arbeiten mit iframes erhaelt man ein `Frame`-Objekt via `page.frame()`,
`page.frames()`, oder als Ergebnis von `frameattached`-Events.

---

## Inhaltsverzeichnis

1. [Navigation & Inhalt](#1-navigation--inhalt)
2. [Frame-Eigenschaften & Hierarchie](#2-frame-eigenschaften--hierarchie)
3. [Locator-Fabrik-Methoden](#3-locator-fabrik-methoden)
4. [JavaScript-Ausfuehrung](#4-javascript-ausfuehrung)
5. [Skript- und Style-Injektion](#5-skript--und-style-injektion)
6. [Elementinteraktionen (Selector-basiert, deprecated)](#6-elementinteraktionen-selector-basiert-deprecated)
7. [Element-Inhalte & Zustand (Selector-basiert, deprecated)](#7-element-inhalte--zustand-selector-basiert-deprecated)
8. [Warten / Synchronisation](#8-warten--synchronisation)
9. [Legacy Selector API (deprecated)](#9-legacy-selector-api-deprecated)
10. [Manifest](#10-manifest)

---

## 1. Navigation & Inhalt

### frame.goto()

```typescript
frame.goto(url: string, options?: {
  referer?: string,
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `url` | `string` | ja | — | Ziel-URL |
| `options.referer` | `string` | nein | — | HTTP-Referer-Header |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Navigation abgeschlossen gilt |

Navigiert den Frame zur angegebenen URL.

```typescript
// Haupt-Frame navigieren (entspricht page.goto)
await page.mainFrame().goto('https://example.com');

// iframe navigieren
const frame = page.frame({ name: 'my-frame' });
await frame?.goto('https://other-domain.com');
```

---

### frame.content()

```typescript
frame.content(): Promise<string>
```

Gibt den vollstaendigen HTML-Inhalt des Frames zurueck (inkl. Doctype).

```typescript
const html = await frame.content();
expect(html).toContain('<h1>');
```

---

### frame.setContent()

```typescript
frame.setContent(html: string, options?: {
  timeout?: number,
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `html` | `string` | ja | — | Vollstaendiger HTML-String |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |
| `options.waitUntil` | `string` | nein | `'load'` | Wann Setzen abgeschlossen gilt |

```typescript
await frame.setContent('<h1>Test</h1><p>Inhalt</p>');
await frame.setContent(htmlString, { waitUntil: 'domcontentloaded' });
```

---

### frame.title()

```typescript
frame.title(): Promise<string>
```

Gibt den Seitentitel des Frames zurueck.

```typescript
const title = await frame.title();
```

---

### frame.url()

```typescript
frame.url(): string
```

Gibt die aktuelle URL des Frames zurueck (synchron).

```typescript
console.log(frame.url()); // 'https://example.com/path'
```

---

## 2. Frame-Eigenschaften & Hierarchie

### frame.name()

```typescript
frame.name(): string
```

Gibt das `name`-Attribut des `<iframe>`-Tags zurueck. Leerer String fuer den Haupt-Frame.

```typescript
const name = frame.name(); // 'my-frame' oder ''
```

---

### frame.isDetached()

```typescript
frame.isDetached(): boolean
```

Gibt `true` zurueck wenn der Frame vom DOM entfernt wurde.

```typescript
if (!frame.isDetached()) {
  await frame.locator('button').click();
}
```

---

### frame.page()

```typescript
frame.page(): Page
```

Gibt die `Page`-Instanz zurueck, zu der dieser Frame gehoert.

```typescript
const page = frame.page();
await page.screenshot();
```

---

### frame.parentFrame()

```typescript
frame.parentFrame(): Frame | null
```

Gibt den uebergeordneten Frame zurueck. `null` fuer den Haupt-Frame und abgehaengte Frames.

```typescript
const parent = frame.parentFrame();
if (parent) {
  console.log('Parent-URL:', parent.url());
}
```

---

### frame.childFrames()

```typescript
frame.childFrames(): Frame[]
```

Gibt alle direkt untergeordneten Frames zurueck.

```typescript
const children = frame.childFrames();
for (const child of children) {
  console.log('Child-Frame:', child.url());
}
```

---

### frame.frameElement()

```typescript
frame.frameElement(): Promise<ElementHandle>
```

Gibt das `<iframe>`- oder `<frame>`-DOM-Element zurueck, das diesem Frame entspricht.

```typescript
const frameElement = await frame.frameElement();
const src = await frameElement.getAttribute('src');
console.log('iframe src:', src);
```

---

## 3. Locator-Fabrik-Methoden

Alle Locator-Methoden des Frames entsprechen 1:1 den gleichnamigen Methoden auf `Page`.
Sie operieren aber im Kontext dieses spezifischen Frames.

### frame.locator()

```typescript
frame.locator(selector: string, options?: {
  has?: Locator,
  hasNot?: Locator,
  hasText?: string | RegExp,
  hasNotText?: string | RegExp
}): Locator
```

Erstellt einen Locator relativ zum Frame.

```typescript
const iframe = page.frame({ name: 'payment' });
await iframe?.locator('input[name=card]').fill('4111111111111111');
```

---

### frame.frameLocator()

```typescript
frame.frameLocator(selector: string): FrameLocator
```

Erstellt einen Locator fuer verschachtelte iframes.

```typescript
const outerFrame = page.frame('outer');
const innerLocator = outerFrame?.frameLocator('#inner-iframe');
await innerLocator?.getByRole('button').click();
```

---

### frame.getByRole()

```typescript
frame.getByRole(role: AriaRole, options?: {
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

Findet Elemente nach ARIA-Rolle im Frame-Kontext.

```typescript
const frame = page.frame('login-frame');
await frame?.getByRole('button', { name: 'Anmelden' }).click();
await frame?.getByRole('textbox', { name: 'Passwort' }).fill('geheim');
```

---

### frame.getByText()

```typescript
frame.getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
const frame = page.frame('content');
await frame?.getByText('Willkommen').click();
```

---

### frame.getByLabel()

```typescript
frame.getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByLabel('E-Mail').fill('test@example.com');
```

---

### frame.getByPlaceholder()

```typescript
frame.getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByPlaceholder('Suchbegriff').fill('Playwright');
```

---

### frame.getByAltText()

```typescript
frame.getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByAltText('Logo').click();
```

---

### frame.getByTitle()

```typescript
frame.getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

```typescript
await frame?.getByTitle('Schliessen').click();
```

---

### frame.getByTestId()

```typescript
frame.getByTestId(testId: string | RegExp): Locator
```

```typescript
await frame?.getByTestId('submit-btn').click();
```

---

## 4. JavaScript-Ausfuehrung

### frame.evaluate()

```typescript
frame.evaluate<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<T>
```

| Parameter | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pageFunction` | `Function\|string` | ja | Funktion die im Frame-Kontext ausgefuehrt wird |
| `arg` | `Serializable\|JSHandle` | nein | Argument (serialisierbar oder JSHandle) |

Gibt serialisierten JSON-Wert zurueck.

```typescript
const url = await frame.evaluate(() => window.location.href);
const sum = await frame.evaluate(({ a, b }) => a + b, { a: 5, b: 3 });
const title = await frame.evaluate('document.title');

// DOM-Manipulation
await frame.evaluate(() => {
  document.querySelector('.overlay')?.remove();
});
```

---

### frame.evaluateHandle()

```typescript
frame.evaluateHandle<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg
): Promise<JSHandle<T>>
```

Wie `evaluate()`, gibt aber ein `JSHandle` zurueck (kein JSON-Serialisierungs-Overhead).

```typescript
const bodyHandle = await frame.evaluateHandle(() => document.body);
const children = await frame.evaluate(body => body.children.length, bodyHandle);
await bodyHandle.dispose();
```

---

## 5. Skript- und Style-Injektion

### frame.addScriptTag()

```typescript
frame.addScriptTag(options?: {
  content?: string,
  path?: string,
  type?: string,
  url?: string
}): Promise<ElementHandle>
```

| Option | Typ | Beschreibung |
|---|---|---|
| `content` | `string` | Inline-JS-Code |
| `path` | `string` | Lokaler Dateipfad |
| `type` | `string` | Script-type-Attribut (z.B. `'module'`) |
| `url` | `string` | Externe URL |

Fuegt ein `<script>`-Tag in den Frame ein.

```typescript
await frame.addScriptTag({ url: 'https://cdn.example.com/lib.js' });
await frame.addScriptTag({ content: 'window.__FRAME_LOADED = true;' });
await frame.addScriptTag({ path: './helper.js', type: 'module' });
```

---

### frame.addStyleTag()

```typescript
frame.addStyleTag(options?: {
  content?: string,
  path?: string,
  url?: string
}): Promise<ElementHandle>
```

Fuegt ein `<style>`-Tag oder `<link rel=stylesheet>` in den Frame ein.

```typescript
await frame.addStyleTag({ content: '.highlight { background: yellow; }' });
await frame.addStyleTag({ url: 'https://cdn.example.com/style.css' });
```

---

## 6. Elementinteraktionen (Selector-basiert, deprecated)

**Hinweis:** Bevorzuge `frame.locator().click()` etc. gegenueber diesen direkten Selector-Methoden.

### frame.click()

```typescript
frame.click(selector: string, options?: {
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

Klickt auf das erste Element, das dem Selektor entspricht.

```typescript
await frame.click('button[type=submit]');
await frame.click('#menu-item', { button: 'right' });
await frame.click('a', { modifiers: ['Control'] });
```

---

### frame.dblclick()

```typescript
frame.dblclick(selector: string, options?: {
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

Doppelklick.

```typescript
await frame.dblclick('.editable');
```

---

### frame.check()

```typescript
frame.check(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Aktiviert Checkbox oder Radio.

```typescript
await frame.check('#accept-terms');
```

---

### frame.uncheck()

```typescript
frame.uncheck(selector: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Deaktiviert Checkbox.

```typescript
await frame.uncheck('#newsletter');
```

---

### frame.fill()

```typescript
frame.fill(selector: string, value: string, options?: {
  force?: boolean,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Loescht bestehenden Wert und fuellt Eingabefeld.

```typescript
await frame.fill('input[name=email]', 'test@example.com');
await frame.fill('textarea#comment', 'Mein Kommentar');
```

---

### frame.focus()

```typescript
frame.focus(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Setzt Fokus auf Element.

```typescript
await frame.focus('input[autofocus]');
```

---

### frame.hover()

```typescript
frame.hover(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Bewegt Maus ueber Element.

```typescript
await frame.hover('.tooltip-trigger');
```

---

### frame.tap()

```typescript
frame.tap(selector: string, options?: {
  force?: boolean,
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>,
  noWaitAfter?: boolean,
  position?: { x: number, y: number },
  strict?: boolean,
  timeout?: number,
  trial?: boolean
}): Promise<void>
```

Touch-Tap (Touchscreen-Emulation erforderlich).

```typescript
await frame.tap('.mobile-button');
```

---

### frame.press()

```typescript
frame.press(selector: string, key: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | Zu fokussierendes Element |
| `key` | `string` | ja | — | Tastenkombination |
| `options.delay` | `number` | nein | `0` | Ms zwischen keydown und keyup |

```typescript
await frame.press('input', 'Enter');
await frame.press('body', 'Escape');
```

---

### frame.type()

```typescript
frame.type(selector: string, text: string, options?: {
  delay?: number,
  noWaitAfter?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

**Deprecated.** Simuliert echte Tastatureingaben ohne bestehenden Inhalt zu loeschen.

```typescript
await frame.type('input', 'Hallo', { delay: 50 });
```

---

### frame.selectOption()

```typescript
frame.selectOption(
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

Waehlt Optionen in einem `<select>`-Element aus.

```typescript
await frame.selectOption('select#country', 'de');
await frame.selectOption('select', { label: 'Deutschland' });
await frame.selectOption('select[multiple]', ['de', 'at']);
```

---

### frame.setInputFiles()

```typescript
frame.setInputFiles(
  selector: string,
  files: string | string[] | { name: string, mimeType: string, buffer: Buffer } | Array<...>,
  options?: {
    noWaitAfter?: boolean,
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Setzt Dateien fuer ein `<input type=file>`.

```typescript
await frame.setInputFiles('input[type=file]', '/path/to/file.pdf');
await frame.setInputFiles('input', [], { }); // Reset
```

---

### frame.dispatchEvent()

```typescript
frame.dispatchEvent(
  selector: string,
  type: string,
  eventInit?: EvaluationArgument,
  options?: {
    strict?: boolean,
    timeout?: number
  }
): Promise<void>
```

Loest ein DOM-Event aus.

```typescript
await frame.dispatchEvent('button', 'click');
await frame.dispatchEvent('#field', 'input', { bubbles: true });
```

---

### frame.dragAndDrop()

```typescript
frame.dragAndDrop(source: string, target: string, options?: {
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

Drag-and-Drop innerhalb des Frames.

```typescript
await frame.dragAndDrop('#source', '#target');
await frame.dragAndDrop('.card', '.dropzone', { steps: 5 });
```

---

## 7. Element-Inhalte & Zustand (Selector-basiert, deprecated)

### frame.getAttribute()

```typescript
frame.getAttribute(selector: string, name: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

```typescript
const href = await frame.getAttribute('a.link', 'href');
```

---

### frame.innerHTML()

```typescript
frame.innerHTML(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const content = await frame.innerHTML('.article-body');
```

---

### frame.innerText()

```typescript
frame.innerText(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const text = await frame.innerText('h1');
```

---

### frame.textContent()

```typescript
frame.textContent(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string | null>
```

```typescript
const text = await frame.textContent('#description');
```

---

### frame.inputValue()

```typescript
frame.inputValue(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<string>
```

```typescript
const value = await frame.inputValue('input[name=email]');
```

---

### frame.isChecked()

```typescript
frame.isChecked(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const checked = await frame.isChecked('#terms');
```

---

### frame.isDisabled()

```typescript
frame.isDisabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const disabled = await frame.isDisabled('button[type=submit]');
```

---

### frame.isEditable()

```typescript
frame.isEditable(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const editable = await frame.isEditable('input[name=username]');
```

---

### frame.isEnabled()

```typescript
frame.isEnabled(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const enabled = await frame.isEnabled('.submit-btn');
```

---

### frame.isHidden()

```typescript
frame.isHidden(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const hidden = await frame.isHidden('.spinner');
```

---

### frame.isVisible()

```typescript
frame.isVisible(selector: string, options?: {
  strict?: boolean,
  timeout?: number
}): Promise<boolean>
```

```typescript
const visible = await frame.isVisible('.success-message');
```

---

### frame.selectText()

```typescript
frame.selectText(selector: string, options?: {
  force?: boolean,
  strict?: boolean,
  timeout?: number
}): Promise<void>
```

Selektiert Text eines Eingabefelds.

```typescript
await frame.selectText('input[name=title]');
```

---

## 8. Warten / Synchronisation

### frame.waitForLoadState()

```typescript
frame.waitForLoadState(
  state?: 'load' | 'domcontentloaded' | 'networkidle',
  options?: { timeout?: number }
): Promise<void>
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `state` | `string` | nein | `'load'` | Gewuenschter Lade-Zustand |
| `options.timeout` | `number` | nein | `defaultNavigationTimeout` | Max. Wartezeit in ms |

```typescript
await frame.waitForLoadState('networkidle');
await frame.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

---

### frame.waitForNavigation()

```typescript
frame.waitForNavigation(options?: {
  timeout?: number,
  url?: string | RegExp | URLPattern | ((url: URL) => boolean),
  waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
}): Promise<Response | null>
```

**Deprecated** — Verwende `frame.waitForURL()`. Wartet auf Navigation im Frame.

```typescript
await Promise.all([
  frame.waitForNavigation(),
  frame.click('a.navigate')
]);
```

---

### frame.waitForURL()

```typescript
frame.waitForURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    timeout?: number,
    waitUntil?: 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
  }
): Promise<void>
```

Wartet bis die Frame-URL mit dem Muster uebereinstimmt.

```typescript
await frame.waitForURL('**/dashboard');
await frame.waitForURL(/profile/, { waitUntil: 'networkidle' });
```

---

### frame.waitForFunction()

```typescript
frame.waitForFunction<T>(
  pageFunction: ((arg: Arg) => T | Promise<T>) | string,
  arg?: Arg,
  options?: {
    polling?: number | 'raf',
    timeout?: number
  }
): Promise<JSHandle<T>>
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `polling` | `number\|'raf'` | `'raf'` | Polling-Intervall |
| `timeout` | `number` | `defaultTimeout` | Max. Wartezeit |

Wartet bis Funktion im Frame-Kontext truthy zurueckgibt.

```typescript
await frame.waitForFunction(() => document.readyState === 'complete');
await frame.waitForFunction(count => window.itemCount >= count, 10);
```

---

### frame.waitForSelector()

```typescript
frame.waitForSelector(selector: string, options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden',
  strict?: boolean,
  timeout?: number
}): Promise<ElementHandle | null>
```

**Deprecated** — Verwende `frame.locator().waitFor()`.

```typescript
await frame.waitForSelector('.content', { state: 'visible' });
const handle = await frame.waitForSelector('.result');
```

---

## 9. Legacy Selector API (deprecated)

### frame.$()

```typescript
frame.$(selector: string, options?: { strict?: boolean }): Promise<ElementHandle | null>
```

Gibt das erste Element zurueck, das dem Selektor entspricht. `null` wenn nicht gefunden.

```typescript
const el = await frame.$('h1');
if (el) {
  const text = await el.textContent();
}
```

---

### frame.$$()

```typescript
frame.$$(selector: string): Promise<ElementHandle[]>
```

Gibt alle Elemente zurueck, die dem Selektor entsprechen.

```typescript
const items = await frame.$$('li.item');
for (const item of items) {
  console.log(await item.textContent());
}
```

---

### frame.$eval()

```typescript
frame.$eval<T>(
  selector: string,
  pageFunction: (element: Element, arg?: Arg) => T | Promise<T>,
  arg?: Arg,
  options?: { strict?: boolean }
): Promise<T>
```

Fuehrt Funktion auf dem ersten gematchten Element aus.

```typescript
const text = await frame.$eval('h1', el => el.textContent);
const href = await frame.$eval('a.link', el => el.getAttribute('href'));
```

---

### frame.$$eval()

```typescript
frame.$$eval<T>(
  selector: string,
  pageFunction: (elements: Element[], arg?: Arg) => T | Promise<T>,
  arg?: Arg
): Promise<T>
```

Fuehrt Funktion auf ALLEN gematchten Elementen aus.

```typescript
const texts = await frame.$$eval('li', els => els.map(el => el.textContent));
const count = await frame.$$eval('.item', els => els.length);
```

---

## 10. Manifest

| Kategorie | Dokumentierte Mitglieder |
|---|---|
| Navigation & Inhalt | 5 Methoden (goto, content, setContent, title, url) |
| Frame-Eigenschaften & Hierarchie | 6 Methoden (name, isDetached, page, parentFrame, childFrames, frameElement) |
| Locator-Fabrik | 10 Methoden (locator, frameLocator, getByRole, getByText, getByLabel, getByPlaceholder, getByAltText, getByTitle, getByTestId) |
| JavaScript-Ausfuehrung | 2 Methoden (evaluate, evaluateHandle) |
| Skript/Style-Injektion | 2 Methoden (addScriptTag, addStyleTag) |
| Elementinteraktionen | 12 Methoden (click, dblclick, check, uncheck, fill, focus, hover, tap, press, type, selectOption, setInputFiles, dispatchEvent, dragAndDrop) |
| Element-Inhalte & Zustand | 11 Methoden (getAttribute, innerHTML, innerText, textContent, inputValue, isChecked, isDisabled, isEditable, isEnabled, isHidden, isVisible, selectText) |
| Warten/Sync | 4 Methoden (waitForLoadState, waitForNavigation, waitForURL, waitForFunction, waitForSelector) |
| Legacy Selector API | 4 Methoden ($, $$, $eval, $$eval) |

**Gesamt: ~56 Methoden/Properties**

**Fazit:** `Frame` spiegelt weitgehend die `Page`-API wider, gilt aber spezifisch fuer einen einzelnen
iframe-Kontext. Moderne Playwright-Tests sollten `page.frameLocator()` mit Locator-basierten Methoden
bevorzugen. Direktes `Frame`-Arbeiten ist vor allem bei komplexen Multi-Frame-Szenarien und
`evaluate()`-Ausfuehrungen im iframe-Kontext relevant.

---

**Quelle:** https://playwright.dev/docs/api/class-frame
