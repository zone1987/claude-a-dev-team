# class-framelocator — Playwright API Reference

Ein `FrameLocator` repraesentiert eine Ansicht auf ein `iframe`-Element auf der Seite. Er ermoeglicht die Interaktion mit Elementen innerhalb des Frames. Alle `getBy*`- und `locator()`-Methoden verhalten sich identisch zu den Pendants in `Locator`, wirken aber im Kontext des adressierten Frames.

Methoden-Anzahl: 11 (davon 3 deprecated)

---

## frameLocator()

```typescript
frameLocator(selector: string): FrameLocator
```

Navigiert in ein verschachteltes iframe innerhalb dieses Frames.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selector` | `string` | ja | — | CSS-/Playwright-Selektor fuer das verschachtelte iframe |

**Rueckgabe:** `FrameLocator`

```typescript
const outer = page.frameLocator('#outer');
const inner = outer.frameLocator('#inner');
await inner.getByRole('button').click();
```

---

## getByAltText()

```typescript
getByAltText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente im Frame ueber ihren `alt`-Text.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Alt-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter (Gross-/Kleinschreibung + vollstaendiger String) Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#widget').getByAltText('Logo').click();
```

---

## getByLabel()

```typescript
getByLabel(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Formularelemente im Frame ueber ihr Label.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Label-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#editor').getByLabel('Titel').fill('Test');
```

---

## getByPlaceholder()

```typescript
getByPlaceholder(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet `<input>`-Elemente im Frame ueber ihren `placeholder`-Text.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Placeholder-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#form-frame').getByPlaceholder('E-Mail').fill('user@test.de');
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

Findet Elemente im Frame ueber ARIA-Rolle und optionale Attribute.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `role` | `AriaRole` | ja | — | ARIA-Rolle z.B. `'button'`, `'textbox'` |
| `options.checked` | `boolean` | nein | — | Filtert nach `aria-checked` |
| `options.description` | `string \| RegExp` | nein | — | Accessible description |
| `options.disabled` | `boolean` | nein | — | Filtert nach `aria-disabled` |
| `options.exact` | `boolean` | nein | `false` | Exakter name/description-Vergleich |
| `options.expanded` | `boolean` | nein | — | Filtert nach `aria-expanded` |
| `options.includeHidden` | `boolean` | nein | `false` | Versteckte Elemente einbeziehen |
| `options.level` | `number` | nein | — | Filtert nach `aria-level` |
| `options.name` | `string \| RegExp` | nein | — | Accessible name |
| `options.pressed` | `boolean` | nein | — | Filtert nach `aria-pressed` |
| `options.selected` | `boolean` | nein | — | Filtert nach `aria-selected` |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#checkout').getByRole('button', { name: 'Kaufen' }).click();
```

---

## getByTestId()

```typescript
getByTestId(testId: string | RegExp): Locator
```

Findet Elemente im Frame ueber ihr Test-ID-Attribut.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `testId` | `string \| RegExp` | ja | — | Wert des Test-ID-Attributs |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#app').getByTestId('confirm-btn').click();
```

---

## getByText()

```typescript
getByText(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente im Frame, die den angegebenen Text enthalten.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Gesuchter Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#preview').getByText('Bestaetigen').click();
```

---

## getByTitle()

```typescript
getByTitle(text: string | RegExp, options?: { exact?: boolean }): Locator
```

Findet Elemente im Frame ueber ihr `title`-Attribut.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `text` | `string \| RegExp` | ja | — | Title-Text |
| `options.exact` | `boolean` | nein | `false` | Exakter Vergleich |

**Rueckgabe:** `Locator`

```typescript
await page.frameLocator('#map').getByTitle('Vollbild').click();
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

Erstellt einen Locator innerhalb des Frames.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `selectorOrLocator` | `string \| Locator` | ja | — | Selektor oder Locator |
| `options.has` | `Locator` | nein | — | Enthaelt diesen Locator |
| `options.hasNot` | `Locator` | nein | — | Enthaelt diesen Locator nicht |
| `options.hasNotText` | `string \| RegExp` | nein | — | Enthaelt diesen Text nicht |
| `options.hasText` | `string \| RegExp` | nein | — | Enthaelt diesen Text |

**Rueckgabe:** `Locator`

```typescript
const frame = page.frameLocator('#app');
await frame.locator('.submit-btn').click();
```

---

## owner()

```typescript
owner(): Locator
```

Konvertiert den `FrameLocator` in einen `Locator`, der auf dasselbe iframe-Element zeigt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Locator`

```typescript
const frame = page.frameLocator('#app');
await expect(frame.owner()).toBeVisible();
```

---

## Deprecated Methoden

Diese Methoden sind deprecated. Stattdessen `locator().nth(n).contentFrame()` etc. verwenden.

### first() — DEPRECATED

```typescript
first(): FrameLocator
```

Gibt einen FrameLocator fuer das erste passende iframe zurueck.
**Ersatz:** `locator('iframe').first().contentFrame()`

### last() — DEPRECATED

```typescript
last(): FrameLocator
```

Gibt einen FrameLocator fuer das letzte passende iframe zurueck.
**Ersatz:** `locator('iframe').last().contentFrame()`

### nth() — DEPRECATED

```typescript
nth(index: number): FrameLocator
```

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `index` | `number` | ja | — | Nullbasierter Index |

Gibt einen FrameLocator fuer das n-te passende iframe zurueck.
**Ersatz:** `locator('iframe').nth(n).contentFrame()`

---

## Methoden-Uebersicht

| Kategorie | Methoden |
|---|---|
| Konversion | `owner()` |
| Verschachtelung | `frameLocator()` |
| Fabrikmethoden (getBy*) | `getByAltText`, `getByLabel`, `getByPlaceholder`, `getByRole`, `getByTestId`, `getByText`, `getByTitle` |
| Allgemeine Locatoren | `locator()` |
| Deprecated | `first()`, `last()`, `nth()` |

---

Quelle: https://playwright.dev/docs/api/class-framelocator
