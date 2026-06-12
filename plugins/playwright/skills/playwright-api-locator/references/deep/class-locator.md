# class-locator — Playwright API Reference

Vollstaendige Methoden-Referenz der `Locator`-Klasse. Ein `Locator` repraesentiert eine Moeglichkeit, ein oder mehrere Elemente auf der Seite zu finden. Er ist lazy und fuehrt die eigentliche DOM-Suche erst bei Ausfuehrung einer Aktion durch.

Methoden-Anzahl: 57 (ohne veraltete Aliase)

---

## all()

```typescript
all(): Promise<Array<Locator>>
```

Gibt alle Elemente zurueck, die auf den Locator passen, als Array einzelner Locatoren.
Wartet **nicht** auf Elemente — gibt sofort eine Momentaufnahme zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<Array<Locator>>`

```typescript
const rows = await page.getByRole('row').all();
for (const row of rows) await row.click();
```

---

## allInnerTexts()

```typescript
allInnerTexts(): Promise<Array<string>>
```

Gibt `node.innerText`-Werte aller passenden Elemente zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<Array<string>>`

```typescript
const texts = await page.getByRole('listitem').allInnerTexts();
```

---

## allTextContents()

```typescript
allTextContents(): Promise<Array<string>>
```

Gibt `node.textContent`-Werte aller passenden Elemente zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<Array<string>>`

```typescript
const contents = await page.locator('p').allTextContents();
```

---

## and()

```typescript
and(locator: Locator): Locator
```

Erstellt einen neuen Locator, der **beide** Bedingungen erfuellen muss (logisches UND).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `locator` | `Locator` | ja | — | Weiterer Locator, dessen Bedingung erfuellt sein muss |

**Rueckgabe:** `Locator`

```typescript
const button = page.getByRole('button').and(page.getByTitle('Speichern'));
```

---

## ariaSnapshot()

```typescript
ariaSnapshot(options?: {
  boxes?: boolean;
  depth?: number;
  mode?: 'ai' | 'default';
  timeout?: number;
}): Promise<string>
```

Erstellt einen ARIA-Snapshot des Elements fuer Accessibility-Tests.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.boxes` | `boolean` | nein | `false` | Bounding-Box-Informationen in Snapshot aufnehmen |
| `options.depth` | `number` | nein | unbegrenzt | Maximale Tiefe des Snapshots |
| `options.mode` | `'ai' \| 'default'` | nein | `'default'` | Snapshot-Format |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string>`

```typescript
const snapshot = await page.locator('#nav').ariaSnapshot();
```

---

## blur()

```typescript
blur(options?: { timeout?: number }): Promise<void>
```

Ruft `blur()` auf dem Element auf und entfernt damit den Fokus.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('Name').blur();
```

---

## boundingBox()

```typescript
boundingBox(options?: { timeout?: number }): Promise<null | {
  x: number;
  y: number;
  width: number;
  height: number;
}>
```

Gibt die Bounding-Box des Elements relativ zum Haupt-Viewport zurueck, oder `null` wenn unsichtbar.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<null | { x: number; y: number; width: number; height: number }>`

```typescript
const box = await page.locator('.tooltip').boundingBox();
if (box) console.log(box.x, box.y, box.width, box.height);
```

---

## check()

```typescript
check(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Setzt eine Checkbox oder ein Radio-Element in den angehakten Zustand.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability-Pruefungen uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Klickposition relativ zur Padding-Box |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen, nicht klicken |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('Ich stimme zu').check();
```

---

## clear()

```typescript
clear(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  timeout?: number;
}): Promise<void>
```

Leert den Inhalt eines Input-Feldes.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability-Pruefungen uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('textbox').clear();
```

---

## click()

```typescript
click(options?: {
  button?: 'left' | 'right' | 'middle';
  clickCount?: number;
  delay?: number;
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  steps?: number;
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Klickt auf das Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Maus-Taste |
| `options.clickCount` | `number` | nein | `1` | Anzahl Klicks |
| `options.delay` | `number` | nein | `0` | Verzoegerung zwischen mousedown und mouseup in ms |
| `options.force` | `boolean` | nein | `false` | Actionability-Pruefungen uebergehen |
| `options.modifiers` | `Array<string>` | nein | `[]` | Gleichzeitig gedrueckte Modifier-Tasten |
| `options.noWaitAfter` | `boolean` | nein | `false` | Navigation nach Klick nicht abwarten |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Klickkoordinaten relativ zur Padding-Box |
| `options.steps` | `number` | nein | `1` | Interpolierte mousemove-Events |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen, nicht klicken |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('button', { name: 'Absenden' }).click();
await page.getByText('Optionen').click({ button: 'right' });
```

---

## contentFrame()

```typescript
contentFrame(): FrameLocator
```

Gibt einen `FrameLocator` zurueck, der auf das iframe-Element zeigt, das dieser Locator beschreibt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `FrameLocator`

```typescript
const frame = page.locator('iframe[title="Editor"]').contentFrame();
await frame.getByRole('textbox').fill('Hallo');
```

---

## count()

```typescript
count(): Promise<number>
```

Gibt die Anzahl der passenden Elemente zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<number>`

```typescript
const n = await page.getByRole('listitem').count();
expect(n).toBe(3);
```

---

## dblclick()

```typescript
dblclick(options?: {
  button?: 'left' | 'right' | 'middle';
  delay?: number;
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  steps?: number;
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Doppelklickt auf das Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.button` | `'left' \| 'right' \| 'middle'` | nein | `'left'` | Maus-Taste |
| `options.delay` | `number` | nein | `0` | Verzoegerung zwischen mousedown/mouseup in ms |
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.modifiers` | `Array<string>` | nein | `[]` | Modifier-Tasten |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Klickposition |
| `options.steps` | `number` | nein | `1` | Interpolierte mousemove-Events |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByText('Dateiname').dblclick();
```

---

## describe()

```typescript
describe(description: string): Locator
```

Setzt eine benutzerdefinierte Beschreibung, die im Trace Viewer angezeigt wird. Gibt den Locator zurueck (chainable).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `description` | `string` | ja | — | Beschreibungstext fuer den Trace Viewer |

**Rueckgabe:** `Locator`

```typescript
const btn = page.getByRole('button').describe('Haupt-CTA');
```

---

## description()

```typescript
description(): null | string
```

Gibt die zuvor mit `describe()` gesetzte Beschreibung zurueck, oder `null`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `null | string`

```typescript
const desc = page.getByRole('button').describe('Speichern').description();
// => 'Speichern'
```

---

## dispatchEvent()

```typescript
dispatchEvent(
  type: string,
  eventInit?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<void>
```

Sendet ein DOM-Event auf dem Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `type` | `string` | ja | — | DOM-Event-Typ z.B. `'click'`, `'dragstart'` |
| `eventInit` | `EvaluationArgument` | nein | `{}` | Event-spezifische Initialisierungsparameter |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('#drag').dispatchEvent('dragstart');
```

---

## dragTo()

```typescript
dragTo(target: Locator, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  sourcePosition?: { x: number; y: number };
  steps?: number;
  targetPosition?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Zieht das Element auf ein Ziel-Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `target` | `Locator` | ja | — | Ziel-Locator, auf den das Element gezogen wird |
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.sourcePosition` | `{ x: number; y: number }` | nein | Mittelpunkt | Startposition innerhalb des Quellelements |
| `options.steps` | `number` | nein | `1` | Interpolierte mousemove-Events |
| `options.targetPosition` | `{ x: number; y: number }` | nein | Mittelpunkt | Zielposition innerhalb des Zielelements |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('#item-1').dragTo(page.locator('#target-zone'));
```

---

## drop()

```typescript
drop(payload: {
  files?: string | Array<string> | { name: string; mimeType: string; buffer: Buffer } | Array<{ name: string; mimeType: string; buffer: Buffer }>;
  data?: Record<string, string>;
  position?: { x: number; y: number };
}, options?: { timeout?: number }): Promise<void>
```

Simuliert einen externen Drag-and-Drop von Dateien oder Daten auf das Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `payload.files` | `string \| string[] \| FilePayload \| FilePayload[]` | nein | — | Dateipfade oder Buffer-Objekte |
| `payload.data` | `Record<string, string>` | nein | — | MIME-Typ zu Daten-Map |
| `payload.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Drop-Position |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('#dropzone').drop({ files: ['path/to/file.pdf'] });
```

---

## evaluate()

```typescript
evaluate<R>(
  pageFunction: (element: SVGElement | HTMLElement, arg?: unknown) => R,
  arg?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<R>
```

Fuehrt JavaScript im Browser-Kontext aus; das passende Element wird als erstes Argument uebergeben.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | ja | — | Auszufuehrender Code; erstes Argument ist das DOM-Element |
| `arg` | `EvaluationArgument` | nein | — | Serialisierbarer Wert, der als zweites Argument uebergeben wird |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit fuer den Locator in ms |

**Rueckgabe:** `Promise<R>`

```typescript
const tagName = await page.locator('h1').evaluate(el => el.tagName);
```

---

## evaluateAll()

```typescript
evaluateAll<R>(
  pageFunction: (elements: Array<SVGElement | HTMLElement>, arg?: unknown) => R,
  arg?: EvaluationArgument
): Promise<R>
```

Fuehrt JavaScript aus; alle passenden Elemente werden als Array uebergeben.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | ja | — | Code; erstes Argument ist ein Array aller DOM-Elemente |
| `arg` | `EvaluationArgument` | nein | — | Serialisierbarer Wert |

**Rueckgabe:** `Promise<R>`

```typescript
const values = await page.locator('input').evaluateAll(els => els.map(e => e.value));
```

---

## evaluateHandle()

```typescript
evaluateHandle(
  pageFunction: function | string,
  arg?: EvaluationArgument,
  options?: { timeout?: number }
): Promise<JSHandle>
```

Fuehrt JavaScript aus und gibt ein `JSHandle` mit dem Ergebnis zurueck (nicht serialisiert).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `pageFunction` | `function \| string` | ja | — | Auszufuehrender Code |
| `arg` | `EvaluationArgument` | nein | — | Argument |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<JSHandle>`

```typescript
const handle = await page.locator('canvas').evaluateHandle(el => el.getContext('2d'));
```

---

## fill()

```typescript
fill(value: string, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  timeout?: number;
}): Promise<void>
```

Setzt den Wert eines `<input>`, `<textarea>` oder `contenteditable`-Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `value` | `string` | ja | — | Einzufuegender Wert |
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('E-Mail').fill('user@example.com');
```

---

## filter()

```typescript
filter(options?: {
  has?: Locator;
  hasNot?: Locator;
  hasNotText?: string | RegExp;
  hasText?: string | RegExp;
  visible?: boolean;
}): Locator
```

Filtert die passenden Elemente nach weiteren Kriterien. Gibt einen neuen Locator zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.has` | `Locator` | nein | — | Nur Elemente behalten, die diesen Locator enthalten |
| `options.hasNot` | `Locator` | nein | — | Elemente ausschliessen, die diesen Locator enthalten |
| `options.hasNotText` | `string \| RegExp` | nein | — | Elemente ausschliessen, die diesen Text enthalten |
| `options.hasText` | `string \| RegExp` | nein | — | Nur Elemente behalten, die diesen Text enthalten |
| `options.visible` | `boolean` | nein | — | Nach Sichtbarkeit filtern |

**Rueckgabe:** `Locator`

```typescript
const items = page.getByRole('listitem').filter({ hasText: 'Aktiv' });
const enabled = page.getByRole('row').filter({ hasNot: page.locator('[disabled]') });
```

---

## first()

```typescript
first(): Locator
```

Gibt einen Locator zurueck, der auf das erste passende Element zeigt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Locator`

```typescript
await page.getByRole('button').first().click();
```

---

## focus()

```typescript
focus(options?: { timeout?: number }): Promise<void>
```

Ruft `focus()` auf dem Element auf.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('textbox').focus();
```

---

## frameLocator()

```typescript
frameLocator(selector: string): FrameLocator
```

Gibt einen `FrameLocator` fuer ein iframe-Element innerhalb dieses Locators zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | CSS-/Playwright-Selektor fuer das iframe |

**Rueckgabe:** `FrameLocator`

```typescript
const frame = page.locator('.widget').frameLocator('iframe');
await frame.getByRole('button').click();
```

---

## getAttribute()

```typescript
getAttribute(name: string, options?: { timeout?: number }): Promise<null | string>
```

Gibt den Wert eines Attributs zurueck, oder `null` wenn das Attribut nicht existiert.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | Attributname |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<null | string>`

```typescript
const href = await page.getByRole('link').getAttribute('href');
```

---

## getByAltText()

```typescript
getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente ueber ihren `alt`-Text (typisch fuer Bilder).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Alt-Text zum Suchen |
| `options.exact` | `boolean` | nein | `false` | Exakter (Gross-/Kleinschreibung + vollstaendiger String) Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.getByAltText('Firmenlogo').click();
```

---

## getByLabel()

```typescript
getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Formularelemente ueber ihren Label-Text, `aria-label` oder `aria-labelledby`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Label-Text zum Suchen |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.getByLabel('Passwort').fill('geheim');
```

---

## getByPlaceholder()

```typescript
getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet `<input>`-Elemente ueber ihren `placeholder`-Text.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Placeholder-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.getByPlaceholder('Suche...').fill('Playwright');
```

---

## getByRole()

```typescript
getByRole(role: AriaRole, options?: {
  checked?: boolean;
  description?: string | RegExp;
  disabled?: boolean;
  exact?: boolean;
  expanded?: boolean;
  includeHidden?: boolean;
  level?: number;
  name?: string | RegExp;
  pressed?: boolean;
  selected?: boolean;
}): Locator
```

Findet Elemente ueber ihre ARIA-Rolle und optionale ARIA-Attribute.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `role` | `AriaRole` | ja | — | ARIA-Rolle z.B. `'button'`, `'link'`, `'heading'` |
| `options.checked` | `boolean` | nein | — | Filtert nach `aria-checked` oder nativem `checked`-Zustand |
| `options.description` | `string \| RegExp` | nein | — | Filtert nach accessible description |
| `options.disabled` | `boolean` | nein | — | Filtert nach `aria-disabled` oder nativem `disabled` |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich fuer `name` und `description` |
| `options.expanded` | `boolean` | nein | — | Filtert nach `aria-expanded` |
| `options.includeHidden` | `boolean` | nein | `false` | Versteckte Elemente einbeziehen |
| `options.level` | `number` | nein | — | Filtert nach `aria-level` (fuer Headings) |
| `options.name` | `string \| RegExp` | nein | — | Filtert nach accessible name |
| `options.pressed` | `boolean` | nein | — | Filtert nach `aria-pressed` |
| `options.selected` | `boolean` | nein | — | Filtert nach `aria-selected` |

**Rueckgabe:** `Locator`

```typescript
await page.getByRole('button', { name: 'Anmelden' }).click();
await page.getByRole('heading', { level: 2 }).first().click();
```

---

## getByTestId()

```typescript
getByTestId(testId: string | RegExp): Locator
```

Findet Elemente ueber ihr Test-ID-Attribut (Standard: `data-testid`; konfigurierbar via `selectors.setTestIdAttribute`).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `testId` | `string \| RegExp` | ja | — | Wert des Test-ID-Attributs |

**Rueckgabe:** `Locator`

```typescript
await page.getByTestId('submit-button').click();
```

---

## getByText()

```typescript
getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente, die den angegebenen Text enthalten (Whitespace wird normalisiert).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Gesuchter Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich (Gross-/Kleinschreibung + vollstaendiger String) |

**Rueckgabe:** `Locator`

```typescript
await page.getByText('Bestellbestaetigung').click();
await page.getByText(/Willkommen/i).waitFor();
```

---

## getByTitle()

```typescript
getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente ueber ihr `title`-Attribut.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Title-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.getByTitle('Profil bearbeiten').click();
```

---

## hideHighlight()

```typescript
hideHighlight(): Promise<void>
```

Versteckt das Element-Highlight, das mit `highlight()` erzeugt wurde.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('.box').hideHighlight();
```

---

## highlight()

```typescript
highlight(options?: {
  style?: string | Record<string, string | number>;
}): Promise<Disposable>
```

Hebt das Element auf dem Bildschirm hervor. Gibt ein `Disposable` zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.style` | `string \| Record<string, string \| number>` | nein | Standard-Overlay | CSS-Stile fuer das Hervorhebungs-Overlay |

**Rueckgabe:** `Promise<Disposable>`

```typescript
const highlight = await page.locator('button').highlight();
// ... screenshot ...
await highlight[Symbol.dispose]?.();
```

---

## hover()

```typescript
hover(options?: {
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Bewegt die Maus ueber das Element (Hover).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.modifiers` | `Array<string>` | nein | `[]` | Modifier-Tasten |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Hover-Position |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('menuitem', { name: 'Datei' }).hover();
```

---

## innerHTML()

```typescript
innerHTML(options?: { timeout?: number }): Promise<string>
```

Gibt den `innerHTML`-Wert des Elements zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string>`

```typescript
const html = await page.locator('.content').innerHTML();
```

---

## innerText()

```typescript
innerText(options?: { timeout?: number }): Promise<string>
```

Gibt den `innerText`-Wert des Elements zurueck (sichtbarer Text, CSS-Rendering beruecksichtigt).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string>`

```typescript
const text = await page.locator('h1').innerText();
```

---

## inputValue()

```typescript
inputValue(options?: { timeout?: number }): Promise<string>
```

Gibt den aktuellen Wert eines `<input>`, `<textarea>` oder `<select>`-Elements zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string>`

```typescript
const val = await page.getByLabel('Name').inputValue();
```

---

## isChecked()

```typescript
isChecked(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob die Checkbox oder das Radio-Element angehakt ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
if (await page.getByLabel('Datenschutz').isChecked()) { /* ... */ }
```

---

## isDisabled()

```typescript
isDisabled(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob das Element deaktiviert ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
const disabled = await page.getByRole('button').isDisabled();
```

---

## isEditable()

```typescript
isEditable(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob das Element editierbar ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
const editable = await page.getByRole('textbox').isEditable();
```

---

## isEnabled()

```typescript
isEnabled(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob das Element aktiviert (nicht deaktiviert) ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
const enabled = await page.getByRole('button').isEnabled();
```

---

## isHidden()

```typescript
isHidden(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob das Element versteckt oder nicht sichtbar ist. Timeout `0` bedeutet keine Wartezeit.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
if (await page.locator('.spinner').isHidden()) { /* ... */ }
```

---

## isVisible()

```typescript
isVisible(options?: { timeout?: number }): Promise<boolean>
```

Gibt zurueck, ob das Element sichtbar ist. Timeout `0` bedeutet keine Wartezeit.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<boolean>`

```typescript
if (await page.locator('.modal').isVisible()) { /* ... */ }
```

---

## last()

```typescript
last(): Locator
```

Gibt einen Locator zurueck, der auf das letzte passende Element zeigt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Locator`

```typescript
await page.getByRole('row').last().click();
```

---

## locator()

```typescript
locator(selectorOrLocator: string | Locator, options?: {
  has?: Locator;
  hasNot?: Locator;
  hasNotText?: string | RegExp;
  hasText?: string | RegExp;
}): Locator
```

Erstellt einen untergeordneten Locator — sucht innerhalb des aktuellen Locators.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selectorOrLocator` | `string \| Locator` | ja | — | CSS/Playwright-Selektor oder anderer Locator |
| `options.has` | `Locator` | nein | — | Nur Elemente behalten, die diesen Locator enthalten |
| `options.hasNot` | `Locator` | nein | — | Elemente ausschliessen, die diesen Locator enthalten |
| `options.hasNotText` | `string \| RegExp` | nein | — | Ausschliessen nach Text |
| `options.hasText` | `string \| RegExp` | nein | — | Behalten nach Text |

**Rueckgabe:** `Locator`

```typescript
const row = page.locator('tr').filter({ hasText: 'Max' });
const cell = row.locator('td:nth-child(2)');
```

---

## nth()

```typescript
nth(index: number): Locator
```

Gibt den n-ten (nullbasiert) passenden Element-Locator zurueck.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `index` | `number` | ja | — | Nullbasierter Index |

**Rueckgabe:** `Locator`

```typescript
await page.getByRole('button').nth(2).click(); // drittes Button
```

---

## or()

```typescript
or(locator: Locator): Locator
```

Erstellt einen Locator, der Elemente beider Locatoren matched (logisches ODER).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `locator` | `Locator` | ja | — | Alternativer Locator |

**Rueckgabe:** `Locator`

```typescript
const el = page.getByRole('button').or(page.getByRole('link'));
```

---

## press()

```typescript
press(key: string, options?: {
  delay?: number;
  timeout?: number;
}): Promise<void>
```

Drueckt eine Taste auf dem Element (das Element muss fokussiert sein).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `key` | `string` | ja | — | Taste z.B. `'Enter'`, `'Tab'`, `'ArrowDown'`, `'Control+A'` |
| `options.delay` | `number` | nein | `0` | Verzoegerung zwischen keydown und keyup in ms |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('textbox').press('Enter');
await page.locator('#editor').press('Control+A');
```

---

## pressSequentially()

```typescript
pressSequentially(text: string, options?: {
  delay?: number;
  timeout?: number;
}): Promise<void>
```

Tippt Text Zeichen fuer Zeichen mit optionaler Verzoegerung (simuliert menschliche Eingabe).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string` | ja | — | Einzutippender Text |
| `options.delay` | `number` | nein | `0` | Verzoegerung zwischen Tastendrucken in ms |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('textbox').pressSequentially('Hello', { delay: 50 });
```

---

## screenshot()

```typescript
screenshot(options?: {
  animations?: 'disabled' | 'allow';
  mask?: Array<Locator>;
  maskColor?: string;
  omitBackground?: boolean;
  path?: string;
  quality?: number;
  scale?: 'css' | 'device';
  timeout?: number;
  type?: 'png' | 'jpeg';
}): Promise<Buffer>
```

Erstellt einen Screenshot des Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.animations` | `'disabled' \| 'allow'` | nein | `'disabled'` | CSS-Animationen behandeln |
| `options.mask` | `Array<Locator>` | nein | `[]` | Elemente, die maskiert (unkenntlich) werden sollen |
| `options.maskColor` | `string` | nein | `'#FF00FF'` | Farbe fuer Maskierung |
| `options.omitBackground` | `boolean` | nein | `false` | Hintergrund weglassen (PNG transparent) |
| `options.path` | `string` | nein | — | Speicherpfad |
| `options.quality` | `number` | nein | — | JPEG-Qualitaet 0-100 |
| `options.scale` | `'css' \| 'device'` | nein | `'device'` | CSS-Pixel oder Geraetemasseinheit |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.type` | `'png' \| 'jpeg'` | nein | `'png'` | Bildformat |

**Rueckgabe:** `Promise<Buffer>`

```typescript
const buf = await page.locator('.chart').screenshot({ path: 'chart.png' });
```

---

## scrollIntoViewIfNeeded()

```typescript
scrollIntoViewIfNeeded(options?: { timeout?: number }): Promise<void>
```

Scrollt das Element in den sichtbaren Bereich, wenn noetig.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('#footer').scrollIntoViewIfNeeded();
```

---

## selectOption()

```typescript
selectOption(
  values: string | string[] | { value?: string; label?: string; index?: number } | Array<{ value?: string; label?: string; index?: number }>,
  options?: {
    force?: boolean;
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<string[]>
```

Waehlt Optionen in einem `<select>`-Element aus.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `values` | `string \| string[] \| SelectOption \| SelectOption[]` | ja | — | Zu waehlende Werte/Labels/Indizes |
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string[]>` — gewaehlte Optionswerte

```typescript
await page.getByLabel('Land').selectOption('DE');
await page.getByLabel('Farben').selectOption(['rot', 'blau']);
```

---

## selectText()

```typescript
selectText(options?: {
  force?: boolean;
  timeout?: number;
}): Promise<void>
```

Markiert den gesamten Textinhalt eines Input- oder Textarea-Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('textbox').selectText();
```

---

## setChecked()

```typescript
setChecked(checked: boolean, options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Setzt den angehakten Zustand einer Checkbox oder eines Radio-Elements explizit.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `checked` | `boolean` | ja | — | `true` = angehakt, `false` = nicht angehakt |
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Klickposition |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('Newsletter').setChecked(true);
```

---

## setInputFiles()

```typescript
setInputFiles(
  files: string | Array<string> | { name: string; mimeType: string; buffer: Buffer } | Array<{ name: string; mimeType: string; buffer: Buffer }>,
  options?: {
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Setzt Dateien fuer ein `<input type="file">`-Element.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `files` | `string \| string[] \| FilePayload \| FilePayload[]` | ja | — | Dateipfade oder Buffer-Objekte mit `name`, `mimeType`, `buffer` |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('Datei hochladen').setInputFiles('pfad/zu/datei.pdf');
```

---

## tap()

```typescript
tap(options?: {
  force?: boolean;
  modifiers?: Array<'Alt' | 'Control' | 'ControlOrMeta' | 'Meta' | 'Shift'>;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Fuehrt eine Touch-Tap-Geste auf dem Element aus.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.modifiers` | `Array<string>` | nein | `[]` | Modifier-Tasten |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Tap-Position |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByRole('button').tap();
```

---

## textContent()

```typescript
textContent(options?: { timeout?: number }): Promise<string | null>
```

Gibt den `textContent`-Wert des Elements zurueck (inklusive unsichtbarer Kinder).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<string | null>`

```typescript
const raw = await page.locator('script').textContent();
```

---

## uncheck()

```typescript
uncheck(options?: {
  force?: boolean;
  noWaitAfter?: boolean;
  position?: { x: number; y: number };
  timeout?: number;
  trial?: boolean;
}): Promise<void>
```

Stellt sicher, dass eine Checkbox oder ein Radio-Element nicht angehakt ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.force` | `boolean` | nein | `false` | Actionability uebergehen |
| `options.noWaitAfter` | `boolean` | nein | — | Veraltet, ohne Wirkung |
| `options.position` | `{ x: number; y: number }` | nein | Mittelpunkt | Klickposition |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |
| `options.trial` | `boolean` | nein | `false` | Nur Actionability pruefen |

**Rueckgabe:** `Promise<void>`

```typescript
await page.getByLabel('Alle auswaehlen').uncheck();
```

---

## waitFor()

```typescript
waitFor(options?: {
  state?: 'attached' | 'detached' | 'visible' | 'hidden';
  timeout?: number;
}): Promise<void>
```

Wartet, bis das Element den gewuenschten Zustand erreicht hat.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.state` | `'attached' \| 'detached' \| 'visible' \| 'hidden'` | nein | `'visible'` | Gewuenschter DOM-/Sichtbarkeits-Zustand |
| `options.timeout` | `number` | nein | global default | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await page.locator('.toast').waitFor({ state: 'visible' });
await page.locator('.spinner').waitFor({ state: 'hidden' });
```

---

## Methoden-Uebersicht (57 Methoden)

| Kategorie | Methoden |
|---|---|
| Iteration/Komposition | `all`, `and`, `or`, `filter`, `first`, `last`, `nth`, `count` |
| Fabrikmethoden (getBy*) | `getByAltText`, `getByLabel`, `getByPlaceholder`, `getByRole`, `getByTestId`, `getByText`, `getByTitle` |
| Untergeordnete Locatoren | `locator`, `frameLocator`, `contentFrame` |
| Lesen (keine Aktion) | `allInnerTexts`, `allTextContents`, `getAttribute`, `innerHTML`, `innerText`, `inputValue`, `textContent`, `boundingBox` |
| Zustands-Checks | `isChecked`, `isDisabled`, `isEditable`, `isEnabled`, `isHidden`, `isVisible` |
| Aktionen | `check`, `uncheck`, `setChecked`, `click`, `dblclick`, `tap`, `hover`, `fill`, `clear`, `press`, `pressSequentially`, `selectOption`, `selectText`, `setInputFiles`, `focus`, `blur`, `dragTo`, `drop`, `scrollIntoViewIfNeeded` |
| Screenshot/Snapshot | `screenshot`, `ariaSnapshot` |
| Eval | `evaluate`, `evaluateAll`, `evaluateHandle`, `dispatchEvent` |
| Warten | `waitFor` |
| Debugging | `describe`, `description`, `highlight`, `hideHighlight` |

---

Quelle: https://playwright.dev/docs/api/class-locator
