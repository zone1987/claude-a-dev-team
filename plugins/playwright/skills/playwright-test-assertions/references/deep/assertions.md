# Playwright Assertions — Vollstaendige Referenz

## Grundprinzip

```typescript
import { test, expect } from '@playwright/test';

test('example', async ({ page }) => {
  await page.goto('/');

  // Auto-retrying: wartet bis Bedingung erfuellt oder Timeout
  await expect(page.getByRole('heading')).toBeVisible();

  // Generisch (nicht retrying): sofortige Auswertung
  expect(42).toBe(42);
});
```

**Default-Timeout fuer Assertions:** 5000 ms (konfigurierbar ueber `expect.timeout` in Config).

---

## Locator-Assertions (auto-retrying)

Alle Locator-Assertions wiederholen die Pruefung bis die Bedingung erfuellt ist oder der Timeout ablaeuft.

| Assertion | Parameter | Beschreibung |
|---|---|---|
| `toBeAttached(options?)` | `options?: { attached?: boolean, timeout?: number }` | Element ist an den DOM angehaengt |
| `toBeChecked(options?)` | `options?: { checked?: boolean, timeout?: number }` | Checkbox/Radio ist angekreuzt |
| `toBeDisabled(options?)` | `options?: { timeout?: number }` | Element ist deaktiviert |
| `toBeEditable(options?)` | `options?: { editable?: boolean, timeout?: number }` | Element ist editierbar |
| `toBeEmpty(options?)` | `options?: { timeout?: number }` | Container ist leer (kein Text/Kinder) |
| `toBeEnabled(options?)` | `options?: { timeout?: number }` | Element ist aktiviert |
| `toBeFocused(options?)` | `options?: { timeout?: number }` | Element hat den Fokus |
| `toBeHidden(options?)` | `options?: { timeout?: number }` | Element ist nicht sichtbar |
| `toBeInViewport(options?)` | `options?: { ratio?: number, timeout?: number }` | Element schneidet Viewport |
| `toBeVisible(options?)` | `options?: { visible?: boolean, timeout?: number }` | Element ist sichtbar |
| `toContainText(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { ignoreCase?, normalizeWhitespace?, useInnerText?, timeout? }` | Element enthaelt Text |
| `toContainClass(expected, options?)` | `expected: string \| string[]`, `options?: { timeout? }` | Element hat (mindestens) diese CSS-Klassen |
| `toHaveAccessibleDescription(description?, options?)` | `description?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | Zugehoeriger ARIA-Description-Wert |
| `toHaveAccessibleName(name?, options?)` | `name?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | Zugehoeriger ARIA-Name |
| `toHaveAttribute(name, value?, options?)` | `name: string`, `value?: string \| RegExp`, `options?: { ignoreCase?, timeout? }` | HTML-Attribut (und Wert) vorhanden |
| `toHaveClass(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { timeout? }` | CSS-class-Eigenschaft |
| `toHaveCount(count, options?)` | `count: number`, `options?: { timeout? }` | Locator-Liste hat genau N Eintraege |
| `toHaveCSS(name, value, options?)` | `name: string`, `value: string \| RegExp`, `options?: { timeout? }` | CSS-Eigenschaft hat Wert |
| `toHaveId(id, options?)` | `id: string \| RegExp`, `options?: { timeout? }` | Element hat ID |
| `toHaveJSProperty(name, value, options?)` | `name: string`, `value: any`, `options?: { timeout? }` | JS-Property hat Wert |
| `toHaveRole(role, options?)` | `role: AriaRole`, `options?: { timeout? }` | Element hat ARIA-Rolle |
| `toHaveScreenshot(name?, options?)` | Siehe Snapshot-Abschnitt | Screenshot-Vergleich |
| `toHaveText(expected, options?)` | `expected: string \| RegExp \| (string \| RegExp)[]`, `options?: { ignoreCase?, normalizeWhitespace?, useInnerText?, timeout? }` | Exakter Text-Match |
| `toHaveValue(value, options?)` | `value: string \| RegExp`, `options?: { timeout? }` | Input-Wert |
| `toHaveValues(values, options?)` | `values: (string \| RegExp)[]`, `options?: { timeout? }` | Select-Mehrfachauswahl |
| `toMatchAriaSnapshot(expected?, options?)` | `expected?: string`, `options?: { timeout? }` | ARIA-Snapshot-Vergleich |

### Beispiele

```typescript
// Text
await expect(page.getByRole('heading')).toHaveText('Welcome');
await expect(page.locator('.status')).toContainText(/error/i);

// Formular
await expect(page.getByRole('checkbox')).toBeChecked();
await expect(page.getByRole('textbox')).toHaveValue('John');
await expect(page.getByRole('combobox')).toHaveValues(['option1', 'option2']);

// Attribute
await expect(page.getByRole('img')).toHaveAttribute('alt', 'Logo');
await expect(page.getByRole('button')).toBeEnabled();

// Liste
await expect(page.getByRole('listitem')).toHaveCount(3);

// CSS
await expect(page.locator('.box')).toHaveCSS('color', 'rgb(0, 0, 0)');

// Sichtbarkeit
await expect(page.getByText('Error')).toBeHidden();
await expect(page.getByText('Success')).toBeVisible();
```

---

## Page-Assertions (auto-retrying)

| Assertion | Parameter | Beschreibung |
|---|---|---|
| `toHaveTitle(title, options?)` | `title: string \| RegExp`, `options?: { timeout? }` | Seiten-Titel |
| `toHaveURL(url, options?)` | `url: string \| RegExp`, `options?: { timeout? }` | Aktuelle URL |
| `toHaveScreenshot(name?, options?)` | Siehe Snapshot-Abschnitt | Seiten-Screenshot |
| `toMatchAriaSnapshot(expected?, options?)` | `expected?: string`, `options?: { timeout? }` | ARIA-Snapshot |

```typescript
await expect(page).toHaveTitle(/Playwright/);
await expect(page).toHaveURL('https://example.com/dashboard');
```

---

## APIResponse-Assertions (auto-retrying)

| Assertion | Parameter | Beschreibung |
|---|---|---|
| `toBeOK(options?)` | `options?: { timeout? }` | Status ist 2xx |

```typescript
const response = await page.request.get('/api/users');
await expect(response).toBeOK();
```

---

## Generische Assertions (NICHT auto-retrying)

Sofortige Auswertung — nicht fuer asynchrone Szenarien geeignet.

| Assertion | Parameter | Beschreibung |
|---|---|---|
| `toBe(value)` | `value: any` | Referenzgleichheit (`===`) |
| `toBeCloseTo(value, digits?)` | `value: number`, `digits?: number` | Genaeherte Gleichheit |
| `toBeDefined()` | — | Wert ist nicht `undefined` |
| `toBeFalsy()` | — | Falsy (false, 0, '', null, undefined, NaN) |
| `toBeGreaterThan(value)` | `value: number \| bigint` | Groesser als |
| `toBeGreaterThanOrEqual(value)` | `value: number \| bigint` | Groesser gleich |
| `toBeInstanceOf(cls)` | `cls: Function` | Instanz einer Klasse |
| `toBeLessThan(value)` | `value: number \| bigint` | Kleiner als |
| `toBeLessThanOrEqual(value)` | `value: number \| bigint` | Kleiner gleich |
| `toBeNaN()` | — | Wert ist NaN |
| `toBeNull()` | — | Wert ist null |
| `toBeTruthy()` | — | Truthy |
| `toBeUndefined()` | — | Wert ist undefined |
| `toContain(value)` | `value: string \| any` | String/Array/Set enthaelt Element |
| `toContainEqual(value)` | `value: any` | Array/Set enthaelt aehnliches Element |
| `toEqual(value)` | `value: any` | Tiefe Gleichheit |
| `toHaveLength(length)` | `length: number` | Array/String-Laenge |
| `toHaveProperty(path, value?)` | `path: string \| string[]`, `value?: any` | Objekt-Eigenschaft |
| `toMatch(regexp)` | `regexp: RegExp \| string` | String passt zu Regex |
| `toMatchObject(object)` | `object: object` | Objekt enthaelt Untermenge |
| `toStrictEqual(value)` | `value: any` | Strikte Gleichheit inkl. Typen |
| `toThrow(error?)` | `error?: string \| RegExp \| Error \| Function` | Funktion wirft Fehler |

```typescript
expect(result).toEqual({ id: 1, name: 'Alice' });
expect(items).toHaveLength(3);
expect(fn).toThrow(/invalid/);
expect(value).toBeGreaterThan(0);
```

---

## Snapshot-Assertions

### `toHaveScreenshot()`

```typescript
// Seite
await expect(page).toHaveScreenshot('landing.png');
await expect(page).toHaveScreenshot(['subdir', 'landing.png']);

// Element
await expect(page.getByRole('main')).toHaveScreenshot('main-content.png');
```

**Optionen:**

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `name` | `string \| string[]` | auto | Snapshot-Dateiname (Segment-Array = Unterverzeichnis) |
| `maxDiffPixels` | `number` | — | Max. abweichende Pixel |
| `maxDiffPixelRatio` | `number` | — | Max. Anteil abweichender Pixel (0-1) |
| `threshold` | `number` | `0.2` | Pixelmatch-Schwellenwert (0-1) |
| `animations` | `'disabled' \| 'allow'` | `'disabled'` | CSS-Animationen |
| `caret` | `'hide' \| 'initial'` | `'hide'` | Text-Cursor |
| `scale` | `'css' \| 'device'` | `'css'` | Skalierungsmodus |
| `stylePath` | `string \| string[]` | — | CSS zum Ueberlagern volatiler Elemente |
| `timeout` | `number` | (expect timeout) | Max. Wartezeit |
| `clip` | `{ x, y, width, height }` | — | Ausschnitt |
| `mask` | `Locator[]` | — | Bereiche maskieren |
| `maskColor` | `string` | `'#FF00FF'` | Farbe fuer Masken |
| `fullPage` | `boolean` | `false` | Vollseiten-Screenshot |
| `omitBackground` | `boolean` | `false` | Hintergrund transparent |

**Benennung:** `{testName}-{browser}-{platform}.png`
**Verzeichnis:** `{testfile}-snapshots/`

**Globale Konfiguration:**

```typescript
expect: {
  toHaveScreenshot: {
    maxDiffPixels: 100,
    stylePath: './screenshot.css',
  },
}
```

### `toMatchSnapshot()`

Fuer Text und Binaerdaten:

```typescript
expect(await page.textContent('.hero')).toMatchSnapshot('hero.txt');
expect(buffer).toMatchSnapshot('data.bin');
```

**Optionen:**

| Option | Typ | Beschreibung |
|---|---|---|
| `name` | `string \| string[]` | Snapshot-Dateiname |
| `maxDiffPixels` | `number` | Max. Pixel-Unterschiede (Bilder) |
| `maxDiffPixelRatio` | `number` | Max. Anteil (Bilder) |
| `threshold` | `number` | Schwellenwert (Bilder) |

**Snapshots aktualisieren:**

```bash
npx playwright test --update-snapshots
npx playwright test --update-snapshots=changed   # nur geaenderte
npx playwright test --update-snapshots=missing   # nur fehlende (Default)
```

---

## Negation

```typescript
await expect(page.getByText('Error')).not.toBeVisible();
expect(value).not.toEqual(0);
```

---

## Soft Assertions

Fehlgeschlagene Assertions brechen den Test NICHT ab; der Test wird am Ende als fehlerhaft markiert.

```typescript
// Einzeln
await expect.soft(page.getByTestId('status')).toHaveText('Success');
await expect.soft(page.getByTestId('count')).toHaveText('3');

// Mit benutzerdefinierter Meldung
expect.soft(value, 'should be positive').toBeGreaterThan(0);

// Fehler manuell pruefen
expect(test.info().errors).toHaveLength(0);
```

---

## Benutzerdefinierte Fehlermeldung

```typescript
await expect(
  page.getByRole('button'),
  'Submit-Button sollte sichtbar sein'
).toBeVisible();
```

---

## `expect.configure()`

Vorkonfigurierte expect-Instanz:

```typescript
const slowExpect = expect.configure({ timeout: 30_000 });
const softExpect = expect.configure({ soft: true });

await slowExpect(locator).toBeVisible();
await softExpect(locator).toHaveText('hello');
```

Parameter: `timeout: number`, `soft: boolean`

---

## `expect.poll()`

Synchrone expect-Funktion asynchron pollen:

```typescript
await expect.poll(async () => {
  const response = await page.request.get('/api/status');
  return response.status();
}, {
  message: 'API sollte 200 zurueckgeben',
  timeout: 10_000,
  intervals: [100, 250, 500, 1000],   // ms zwischen Versuchen
}).toBe(200);
```

Kombinierbar mit soft: `expect.configure({ soft: true }).poll(fn).toBe(x)`

---

## `expect.toPass()`

Codeblock wiederholen bis er erfolgreich ist:

```typescript
await expect(async () => {
  const response = await page.request.get('/api/data');
  expect(response.status()).toBe(200);
  expect(await response.json()).toHaveProperty('items');
}).toPass({
  intervals: [100, 250, 500, 1000],
  timeout: 10_000,                    // Default: 0 (kein Timeout)
});
```

---

## Asymmetrische Matcher

Innerhalb anderer Assertions fuer flexible Pruefungen:

| Matcher | Beschreibung |
|---|---|
| `expect.any(Class)` | Beliebige Instanz der Klasse/Primitiv |
| `expect.anything()` | Beliebiger Wert (nicht null/undefined) |
| `expect.arrayContaining([...])` | Array enthaelt alle aufgelisteten Elemente |
| `expect.arrayOf(type)` | Array aus Elementen des Typs |
| `expect.closeTo(num, digits?)` | Genaeherte Zahl |
| `expect.objectContaining({...})` | Objekt enthaelt bestimmte Eigenschaften |
| `expect.stringContaining(str)` | String enthaelt Teilstring |
| `expect.stringMatching(re)` | String passt zu Regex |

```typescript
expect(obj).toEqual({
  id: expect.any(Number),
  name: expect.stringMatching(/^Alice/),
  tags: expect.arrayContaining(['admin']),
});
```

---

## `expect.extend()` — Eigene Matcher

```typescript
import { expect as baseExpect } from '@playwright/test';
import type { Locator } from '@playwright/test';

export const expect = baseExpect.extend({
  async toHaveAmount(locator: Locator, expected: number, options?: { timeout?: number }) {
    const assertionName = 'toHaveAmount';
    let pass: boolean;
    let matcherResult: any;

    try {
      await baseExpect(locator).toHaveText(
        String(expected),
        { timeout: options?.timeout ?? 1000 }
      );
      pass = true;
    } catch (e: any) {
      matcherResult = e.matcherResult;
      pass = false;
    }

    const message = pass
      ? () => `${this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot })}\n\nExpected: not ${expected}`
      : () => `${this.utils.matcherHint(assertionName, undefined, undefined, { isNot: this.isNot })}\n\nExpected: ${expected}\nReceived: ${matcherResult?.actual}`;

    return { message, pass, name: assertionName, expected, actual: matcherResult?.actual };
  },
});
```

Mehrere Custom-Expect zusammenfuehren:

```typescript
import { mergeExpects } from '@playwright/test';
export const expect = mergeExpects(dbExpect, a11yExpect);
```

---

Source: https://playwright.dev/docs/test-assertions | https://playwright.dev/docs/test-snapshots
