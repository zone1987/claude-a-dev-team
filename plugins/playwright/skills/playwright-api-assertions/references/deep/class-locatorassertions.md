# class-locatorassertions — Playwright API Reference

`LocatorAssertions` ist die Assertion-Klasse fuer `Locator`-Objekte. Alle Matcher retrien automatisch bis der Test erfolgreich ist oder der Timeout erreicht wird. Standardtimeout: Wert aus `TestConfig.expect` (Standard 5000 ms).

Zugriff via `expect(locator).*`.

Matcher-Anzahl: 29 Matcher + Property `not`

---

## Uebersicht: Timeout-Muster

Jeder Matcher akzeptiert optional `{ timeout?: number }` als letztes options-Objekt. Der Timeout-Wert ueberschreibt `TestConfig.expect.timeout` fuer diesen einzelnen Aufruf.

```typescript
await expect(locator).toBeVisible({ timeout: 10_000 });
```

---

## not

```typescript
not: LocatorAssertions
```

Invertiert die Assertion — prueft das Gegenteil der nachfolgenden Assertion.

```typescript
await expect(page.locator('.error')).not.toBeVisible();
await expect(page.getByRole('button')).not.toBeDisabled();
```

---

## toBeAttached()

```typescript
toBeAttached(options?: {
  attached?: boolean;
  timeout?: number;
}): Promise<void>
```

Prueft, ob das Element mit dem DOM verbunden ist (an `Document` oder `ShadowRoot` angehaengt).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.attached` | `boolean` | nein | `true` | `true` = muss angehaengt sein; `false` = darf nicht angehaengt sein |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('#modal')).toBeAttached();
await expect(page.locator('#removed')).toBeAttached({ attached: false });
```

---

## toBeChecked()

```typescript
toBeChecked(options?: {
  checked?: boolean;
  indeterminate?: boolean;
  timeout?: number;
}): Promise<void>
```

Prueft den angehakten Zustand einer Checkbox, eines Radio-Buttons oder eines `aria-checked`-Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.checked` | `boolean` | nein | `true` | Erwarteter Zustand |
| `options.indeterminate` | `boolean` | nein | `false` | Prueft auf unbestimmten Zustand (`indeterminate`) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('AGB akzeptieren')).toBeChecked();
await expect(page.getByLabel('Option')).toBeChecked({ checked: false });
```

---

## toBeDisabled()

```typescript
toBeDisabled(options?: { timeout?: number }): Promise<void>
```

Prueft, ob das Element deaktiviert ist (ueber `disabled`-Attribut oder `aria-disabled`).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('button', { name: 'Senden' })).toBeDisabled();
```

---

## toBeEditable()

```typescript
toBeEditable(options?: {
  editable?: boolean;
  timeout?: number;
}): Promise<void>
```

Prueft, ob das Element editierbar ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.editable` | `boolean` | nein | `true` | Erwarteter Zustand |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('Kommentar')).toBeEditable();
await expect(page.getByLabel('Readonly')).toBeEditable({ editable: false });
```

---

## toBeEmpty()

```typescript
toBeEmpty(options?: { timeout?: number }): Promise<void>
```

Prueft, ob ein editierbares Element oder DOM-Knoten keinen Text enthaelt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('textbox')).toBeEmpty();
```

---

## toBeEnabled()

```typescript
toBeEnabled(options?: {
  enabled?: boolean;
  timeout?: number;
}): Promise<void>
```

Prueft, ob das Element aktiviert (nicht deaktiviert) ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.enabled` | `boolean` | nein | `true` | Erwarteter Zustand |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('button', { name: 'Absenden' })).toBeEnabled();
```

---

## toBeFocused()

```typescript
toBeFocused(options?: { timeout?: number }): Promise<void>
```

Prueft, ob das Element den Tastaturfokus hat.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('Suche')).toBeFocused();
```

---

## toBeHidden()

```typescript
toBeHidden(options?: { timeout?: number }): Promise<void>
```

Prueft, ob das Element verborgen oder nicht sichtbar ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.loading-spinner')).toBeHidden();
```

---

## toBeInViewport()

```typescript
toBeInViewport(options?: {
  ratio?: number;
  timeout?: number;
}): Promise<void>
```

Prueft, ob das Element den Viewport schneidet (Intersection Observer API).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.ratio` | `number` | nein | 0 | Mindestanteil des Elements im Viewport (0-1) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('#cta')).toBeInViewport();
await expect(page.locator('#hero')).toBeInViewport({ ratio: 0.5 });
```

---

## toBeVisible()

```typescript
toBeVisible(options?: {
  timeout?: number;
  visible?: boolean;
}): Promise<void>
```

Prueft, ob das Element im DOM angehaengt und sichtbar ist.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |
| `options.visible` | `boolean` | nein | `true` | `false` entspricht `.not.toBeVisible()` |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.toast')).toBeVisible();
await expect(page.locator('#overlay')).toBeVisible({ visible: false });
```

---

## toContainClass()

```typescript
toContainClass(
  expected: string | string[],
  options?: { timeout?: number }
): Promise<void>
```

Prueft, ob das Element die angegebenen CSS-Klassen enthaelt (nicht notwendigerweise alle).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| string[]` | ja | — | Erwartete Klasse(n); Leerzeichen-getrennt oder als Array |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.btn')).toContainClass('active');
await expect(page.locator('.item')).toContainClass(['selected', 'highlighted']);
```

---

## toContainText()

```typescript
toContainText(
  expected: string | RegExp | Array<string | RegExp>,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
    useInnerText?: boolean;
  }
): Promise<void>
```

Prueft, ob das Element den angegebenen Text enthaelt (Teilstring oder Regex-Match).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | ja | — | Erwarteter Text; bei Array werden Elemente sequenziell geprueft |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |
| `options.useInnerText` | `boolean` | nein | `false` | `innerText` statt `textContent` verwenden |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.message')).toContainText('Erfolg');
await expect(page.locator('.list')).toContainText(['Eintrag 1', 'Eintrag 2']);
```

---

## toHaveAccessibleDescription()

```typescript
toHaveAccessibleDescription(
  description: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Prueft die accessible description des Elements gemaess W3C-Spezifikation.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `description` | `string \| RegExp` | ja | — | Erwartete Beschreibung |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('img')).toHaveAccessibleDescription('Produktfoto');
```

---

## toHaveAccessibleErrorMessage()

```typescript
toHaveAccessibleErrorMessage(
  errorMessage: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Prueft den Wert des `aria-errormessage`-Attributs.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `errorMessage` | `string \| RegExp` | ja | — | Erwartete Fehlermeldung |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('E-Mail')).toHaveAccessibleErrorMessage('Ungueltige E-Mail');
```

---

## toHaveAccessibleName()

```typescript
toHaveAccessibleName(
  name: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Prueft den accessible name des Elements gemaess W3C-Spezifikation.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string \| RegExp` | ja | — | Erwarteter Name |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('button')).toHaveAccessibleName('Anmelden');
```

---

## toHaveAttribute() — mit Wert

```typescript
toHaveAttribute(
  name: string,
  value: string | RegExp,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Prueft, ob das Element ein bestimmtes Attribut mit einem bestimmten Wert hat.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | Attributname |
| `value` | `string \| RegExp` | ja | — | Erwarteter Attributwert |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('link')).toHaveAttribute('href', '/dashboard');
await expect(page.locator('img')).toHaveAttribute('src', /\.webp$/);
```

---

## toHaveAttribute() — nur Existenz

```typescript
toHaveAttribute(
  name: string,
  options?: { timeout?: number }
): Promise<void>
```

Prueft nur die Existenz des Attributs, unabhaengig vom Wert.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | Attributname |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('video')).toHaveAttribute('controls');
```

---

## toHaveClass()

```typescript
toHaveClass(
  expected: string | RegExp | Array<string | RegExp>,
  options?: { timeout?: number }
): Promise<void>
```

Prueft die vollstaendige `class`-Eigenschaft des Elements (exakter Match oder Regex).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | ja | — | Vollstaendige erwartete Klassen-Zeichenkette; bei Array: je Listenelement ein Element |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
// Einzelnes Element: exakter class-Attribut-Vergleich
await expect(page.locator('.btn')).toHaveClass('btn btn-primary');
// Liste von Elementen (Array-Form)
await expect(page.getByRole('listitem')).toHaveClass(['active', 'inactive', 'active']);
```

---

## toHaveCount()

```typescript
toHaveCount(
  count: number,
  options?: { timeout?: number }
): Promise<void>
```

Prueft, ob der Locator exakt die angegebene Anzahl DOM-Knoten aufloest.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `count` | `number` | ja | — | Erwartete Anzahl Elemente |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByRole('listitem')).toHaveCount(5);
```

---

## toHaveCSS()

```typescript
toHaveCSS(
  name: string,
  value: string | RegExp,
  options?: {
    pseudo?: 'before' | 'after';
    timeout?: number;
  }
): Promise<void>
```

Prueft einen berechneten (computed) CSS-Eigenschaftswert.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | CSS-Eigenschaftsname (z.B. `'display'`, `'color'`) |
| `value` | `string \| RegExp` | ja | — | Erwarteter Wert |
| `options.pseudo` | `'before' \| 'after'` | nein | — | Pseudo-Element pruefen |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.badge')).toHaveCSS('display', 'flex');
await expect(page.locator('.icon')).toHaveCSS('content', '"*"', { pseudo: 'before' });
```

---

## toHaveId()

```typescript
toHaveId(
  id: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Prueft die DOM-`id`-Eigenschaft des Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `id` | `string \| RegExp` | ja | — | Erwarteter ID-Wert |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('input').first()).toHaveId('username');
```

---

## toHaveJSProperty()

```typescript
toHaveJSProperty(
  name: string,
  value: unknown,
  options?: { timeout?: number }
): Promise<void>
```

Prueft eine JavaScript-Eigenschaft des DOM-Elements (nicht nur Attribute).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | Eigenschaftsname |
| `value` | `unknown` | ja | — | Erwarteter Wert (primitiv oder serialisierbares Objekt) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('input[type=checkbox]')).toHaveJSProperty('indeterminate', true);
```

---

## toHaveRole()

```typescript
toHaveRole(
  role: AriaRole,
  options?: { timeout?: number }
): Promise<void>
```

Prueft die ARIA-Rolle des Elements gemaess W3C-Spezifikation (exakter String-Vergleich).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `role` | `AriaRole` | ja | — | Erwartete ARIA-Rolle z.B. `'button'`, `'dialog'` |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.modal')).toHaveRole('dialog');
```

---

## toHaveScreenshot() — mit Name

```typescript
toHaveScreenshot(
  name: string | string[],
  options?: {
    animations?: 'disabled' | 'allow';
    caret?: 'hide' | 'initial';
    mask?: Locator[];
    maskColor?: string;
    maxDiffPixelRatio?: number;
    maxDiffPixels?: number;
    omitBackground?: boolean;
    scale?: 'css' | 'device';
    stylePath?: string | string[];
    threshold?: number;
    timeout?: number;
  }
): Promise<void>
```

Vergleicht einen Element-Screenshot mit einem gespeicherten Snapshot (benannter Modus). Nur im Test-Runner verfuegbar.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string \| string[]` | ja | — | Dateiname oder Pfad-Segmente fuer den Snapshot |
| `options.animations` | `'disabled' \| 'allow'` | nein | `'disabled'` | CSS-Animationen beim Screenshot behandeln |
| `options.caret` | `'hide' \| 'initial'` | nein | `'hide'` | Text-Cursor-Sichtbarkeit |
| `options.mask` | `Locator[]` | nein | `[]` | Zu maskierende Elemente (Magenta-Rechteck) |
| `options.maskColor` | `string` | nein | `'#FF00FF'` | Farbe der Maskierung |
| `options.maxDiffPixelRatio` | `number` | nein | aus Config | Maximaler Anteil unterschiedlicher Pixel (0-1) |
| `options.maxDiffPixels` | `number` | nein | aus Config | Maximale Anzahl unterschiedlicher Pixel |
| `options.omitBackground` | `boolean` | nein | `false` | Hintergrund transparent (nur PNG) |
| `options.scale` | `'css' \| 'device'` | nein | `'css'` | Pixel-Masseinheit |
| `options.stylePath` | `string \| string[]` | nein | — | Zusaetzliche CSS-Dateien fuer den Screenshot |
| `options.threshold` | `number` | nein | `0.2` | Farbdifferenz-Schwellenwert (YIQ, 0-1) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('.chart')).toHaveScreenshot('chart-baseline.png');
await expect(page.locator('.header')).toHaveScreenshot('header.png', {
  maxDiffPixelRatio: 0.01,
  mask: [page.locator('.dynamic-date')],
});
```

---

## toHaveScreenshot() — automatisch

```typescript
toHaveScreenshot(options?: {
  animations?: 'disabled' | 'allow';
  caret?: 'hide' | 'initial';
  mask?: Locator[];
  maskColor?: string;
  maxDiffPixelRatio?: number;
  maxDiffPixels?: number;
  omitBackground?: boolean;
  scale?: 'css' | 'device';
  stylePath?: string | string[];
  threshold?: number;
  timeout?: number;
}): Promise<void>
```

Wie oben, aber Name wird automatisch aus Testname + Zaehlnummer generiert.

```typescript
await expect(page.locator('.widget')).toHaveScreenshot();
```

---

## toHaveText()

```typescript
toHaveText(
  expected: string | RegExp | Array<string | RegExp>,
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
    useInnerText?: boolean;
  }
): Promise<void>
```

Prueft den vollstaendigen Text des Elements (whitespace-normalisiert fuer Strings).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Array<string \| RegExp>` | ja | — | Erwarteter Text; bei Array: je Listenelement ein Element |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |
| `options.useInnerText` | `boolean` | nein | `false` | `innerText` statt `textContent` verwenden |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('h1')).toHaveText('Willkommen');
await expect(page.getByRole('listitem')).toHaveText(['Eins', 'Zwei', 'Drei']);
```

---

## toHaveValue()

```typescript
toHaveValue(
  value: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Prueft den aktuellen Wert eines `<input>`, `<textarea>` oder `<select>`-Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `value` | `string \| RegExp` | ja | — | Erwarteter Wert |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('Name')).toHaveValue('Max Mustermann');
```

---

## toHaveValues()

```typescript
toHaveValues(
  values: Array<string | RegExp>,
  options?: { timeout?: number }
): Promise<void>
```

Prueft die ausgewaehlten Werte eines Multi-Select- oder Combobox-Elements.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `values` | `Array<string \| RegExp>` | ja | — | Erwartete ausgewaehlte Werte |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.getByLabel('Sprachen')).toHaveValues(['de', 'en']);
```

---

## toMatchAriaSnapshot() — inline

```typescript
toMatchAriaSnapshot(
  expected: string,
  options?: { timeout?: number }
): Promise<void>
```

Prueft, ob das Element einem inline-ARIA-Snapshot entspricht.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string` | ja | — | ARIA-Snapshot als YAML-String |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('nav')).toMatchAriaSnapshot(`
  - navigation:
    - link "Startseite"
    - link "Produkte"
`);
```

---

## toMatchAriaSnapshot() — gespeichert

```typescript
toMatchAriaSnapshot(options?: {
  name?: string;
  timeout?: number;
}): Promise<void>
```

Vergleicht mit einer gespeicherten `.aria.yml`-Snapshot-Datei.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.name` | `string` | nein | auto | Dateiname des gespeicherten Snapshots |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page.locator('main')).toMatchAriaSnapshot({ name: 'main-content.aria.yml' });
```

---

## Matcher-Uebersicht (29 Matcher)

| Kategorie | Matcher |
|---|---|
| Sichtbarkeit / DOM-Zustand | `toBeAttached`, `toBeHidden`, `toBeVisible`, `toBeInViewport` |
| Aktivierung / Interaktion | `toBeChecked`, `toBeDisabled`, `toBeEditable`, `toBeEmpty`, `toBeEnabled`, `toBeFocused` |
| Texte | `toContainText`, `toHaveText`, `toHaveValue`, `toHaveValues` |
| CSS / Layout | `toContainClass`, `toHaveClass`, `toHaveCSS` |
| Attribute / Eigenschaften | `toHaveAttribute`, `toHaveId`, `toHaveJSProperty`, `toHaveRole` |
| Accessibility | `toHaveAccessibleDescription`, `toHaveAccessibleErrorMessage`, `toHaveAccessibleName` |
| Anzahl | `toHaveCount` |
| Screenshots | `toHaveScreenshot` (2 Ueberladungen) |
| ARIA-Snapshots | `toMatchAriaSnapshot` (2 Ueberladungen) |

---

Quelle: https://playwright.dev/docs/api/class-locatorassertions
