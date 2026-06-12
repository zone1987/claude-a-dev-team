# Playwright Accessibility Testing - Vollstaendige Referenz

---

## 1. Uebersicht und Grenzen

Automatisierte Accessibility-Tests koennen strukturelle Probleme erkennen
(fehlende Alt-Texte, falsche ARIA-Rollen, fehlende Labels). Viele
Barrierefreiheitsprobleme erfordern jedoch manuelle Pruefung mit Tools wie
"Accessibility Insights for Web".

Playwright bietet zwei Ansaetze:
1. **ARIA-Snapshots** - Playwright-native, schnell, kein extra Package
2. **axe-core Integration** - WCAG-konformes Regelwerk, ausfuehrlichere Berichte

---

## 2. ARIA-Snapshots

### toMatchAriaSnapshot(template, options?)

Vergleicht den Accessibility-Tree gegen ein YAML-Template.

```typescript
// Ganze Seite
await expect(page).toMatchAriaSnapshot(`
  - heading "Playwright" [level=1]
  - link "Get Started"
  - link "API Reference"
`);

// Spezifisches Element
await expect(page.locator('nav')).toMatchAriaSnapshot(`
  - list
    - listitem
      - link "Home"
    - listitem
      - link "About"
`);
```

### page.ariaSnapshot() / locator.ariaSnapshot()

Programmatische Erzeugung des ARIA-Snapshots als YAML-String.

```typescript
const snapshot = await page.ariaSnapshot();
console.log(snapshot);

const navSnapshot = await page.locator('nav').ariaSnapshot();
```

---

## 3. ARIA-Snapshot-Template-Syntax

### Grundstruktur

```yaml
- role "accessible name" [attribute=value]
  - child-role "child name"
```

Jede Zeile: `- <role> "<name>"` optional gefolgt von `[attr=value]`.

### Rollen (Auswahl)

| ARIA/HTML-Rolle | Beispiel |
|-----------------|---------|
| `heading` | `- heading "Title" [level=1]` |
| `button` | `- button "Submit"` |
| `link` | `- link "Click here"` |
| `textbox` | `- textbox "Enter name"` |
| `checkbox` | `- checkbox "Accept terms" [checked]` |
| `radio` | `- radio "Option A" [checked]` |
| `combobox` | `- combobox "Country"` |
| `listbox` | `- listbox "Colors"` |
| `option` | `- option "Red" [selected]` |
| `list` | `- list` |
| `listitem` | `- listitem: Item text` |
| `table` | `- table` |
| `row` | `- row` |
| `cell` | `- cell: Content` |
| `columnheader` | `- columnheader "Name"` |
| `img` | `- img "Product photo"` |
| `paragraph` | `- paragraph: Text content` |
| `text` | `- text: Inline text` |
| `group` | `- group "Section name"` |
| `navigation` | `- navigation "Main nav"` |
| `main` | `- main` |
| `region` | `- region "Featured"` |
| `alert` | `- alert: Error message` |
| `dialog` | `- dialog "Confirm"` |

### Attribute

| Attribut | Typ | Beispiel |
|----------|-----|---------|
| `checked` | boolean | `[checked]` oder `[checked=false]` |
| `disabled` | boolean | `[disabled]` |
| `expanded` | boolean | `[expanded=true]` |
| `level` | number | `[level=2]` |
| `pressed` | boolean/mixed | `[pressed=true]` |
| `selected` | boolean | `[selected]` |
| `url` | string | `[url="https://example.com"]` |

---

## 4. Matching-Modi

### Partial Matching (Standard)

Nur angegebene Kinder muessen vorhanden sein, weitere duerfen existieren.
Reihenfolge muss stimmen.

```typescript
await expect(page).toMatchAriaSnapshot(`
  - heading "Products" [level=1]
  - list
    - listitem: "Laptop"
`);
// Auch okay wenn weitere listitem-Elemente vorhanden sind
```

### children: equal

Exakt diese Kinder, keine weiteren erlaubt.

```typescript
await expect(page.locator('ul.colors')).toMatchAriaSnapshot(`
  - list
    - /children: equal
    - listitem: Red
    - listitem: Green
    - listitem: Blue
`);
```

### children: deep-equal

Exakt-Match inkl. aller verschachtelten Kinder.

```typescript
await expect(page.locator('nav')).toMatchAriaSnapshot(`
  - navigation
    - /children: deep-equal
    - list
      - listitem
        - link "Home"
      - listitem
        - link "About"
`);
```

### Globale Konfiguration

```typescript
// playwright.config.ts
export default defineConfig({
  expect: {
    toMatchAriaSnapshot: {
      children: 'equal',  // Standard fuer alle toMatchAriaSnapshot-Aufrufe
    },
  },
});
```

---

## 5. Regex-Matching in Templates

Fuer dynamische Texte (Zahlen, Timestamps, etc.):

```typescript
// Zahl in Ueberschrift
await expect(page).toMatchAriaSnapshot(`
  - heading /Issues \d+/ [level=2]
`);

// URL-Pattern bei Link
await expect(page.locator('footer')).toMatchAriaSnapshot(`
  - link "YouTube":
    - /url: /https:\/\/www\.youtube\.com\/.*/
`);

// Beliebiger Text
await expect(page.locator('.timestamp')).toMatchAriaSnapshot(`
  - text /\d{2}\.\d{2}\.\d{4}/
`);
```

---

## 6. Snapshot-Generierung und Aktualisierung

### Leeres Template (auto-generieren)

```typescript
// Snapshot wird beim ersten Lauf erzeugt
await expect(page.locator('#navigation')).toMatchAriaSnapshot('');
```

### CLI-Flags

```bash
# Alle Snapshots aktualisieren
npx playwright test --update-snapshots

# Kurzform
npx playwright test -u

# Update-Methode (patch = git-apply-barer Diff, Standard)
npx playwright test --update-snapshots --update-source-method=patch

# Merge-Konflikte fuer manuelle Auswahl
npx playwright test --update-snapshots --update-source-method=3way

# Direkte Ueberschreibung
npx playwright test --update-snapshots --update-source-method=overwrite
```

### Separate Snapshot-Dateien

```typescript
// Snapshot in eigener .aria.yml-Datei
await expect(page.getByRole('main')).toMatchAriaSnapshot({
  name: 'main-content.aria.yml',
});
// Gespeichert in: {testFile}-snapshots/main-content.aria.yml
```

### Pfad-Konfiguration

```typescript
// playwright.config.ts
expect: {
  toMatchAriaSnapshot: {
    pathTemplate: '__aria_snapshots__/{testFilePath}/{arg}{ext}',
  },
},
```

---

## 7. Code-Generator fuer ARIA-Snapshots

Playwright Inspector kann Snapshots interaktiv erstellen:

1. `npx playwright codegen https://example.com` starten
2. "Assert snapshot"-Aktion auswaehlen
3. Element anklicken -> ARIA-Snapshot wird generiert
4. "Aria snapshot"-Tab zeigt Rollen, Attribute, Namen

---

## 8. axe-core Integration

### Installation

```bash
npm install --save-dev @axe-core/playwright
```

### AxeBuilder - Konstruktor

```typescript
import { AxeBuilder } from '@axe-core/playwright';

const axeBuilder = new AxeBuilder({ page });
```

### AxeBuilder - Methoden

| Methode | Parameter | Beschreibung |
|---------|-----------|--------------|
| `analyze()` | - | Scan ausfuehren, gibt Promise<AxeResults> zurueck |
| `include(selector)` | `string \| string[]` | Nur diese Bereiche pruefen |
| `exclude(selector)` | `string \| string[]` | Diese Bereiche ausnehmen |
| `withTags(tags)` | `string[]` | Nur Regeln mit diesen WCAG-Tags |
| `disableRules(rules)` | `string[]` | Bestimmte Regeln deaktivieren |
| `withRules(rules)` | `string[]` | Nur bestimmte Regeln pruefen |
| `options(options)` | `RunOptions` | Vollstaendige axe-Optionen |

---

### WCAG-Tags

| Tag | Bedeutung |
|-----|-----------|
| `'wcag2a'` | WCAG 2.0 Level A |
| `'wcag2aa'` | WCAG 2.0 Level AA |
| `'wcag21a'` | WCAG 2.1 Level A |
| `'wcag21aa'` | WCAG 2.1 Level AA |
| `'wcag22aa'` | WCAG 2.2 Level AA |
| `'best-practice'` | Best Practices |
| `'section508'` | US Section 508 |

---

## 9. Axe-Beispiele

### Einfacher Seitenscans

```typescript
import { test, expect } from '@playwright/test';
import { AxeBuilder } from '@axe-core/playwright';

test('page should have no accessibility violations', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page }).analyze();

  expect(results.violations).toEqual([]);
});
```

### WCAG-konformer Scan

```typescript
test('WCAG 2.1 AA compliance', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Gezielter Scan eines Bereichs

```typescript
test('navigation accessibility', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Open Menu' }).click();
  await page.locator('#menu-flyout').waitFor();

  const results = await new AxeBuilder({ page })
    .include('#menu-flyout')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Bekannte Probleme ausschliessen

```typescript
test('page with known issues excluded', async ({ page }) => {
  await page.goto('/legacy-section');

  const results = await new AxeBuilder({ page })
    .exclude('#legacy-widget')           // Element + Kinder ausschliessen
    .disableRules(['color-contrast'])    // Regel fuer ganzen Scan deaktivieren
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Violations-Fingerprint (empfohlen ueber vollstaendigen Snapshot)

```typescript
function violationFingerprints(results: AxeResults) {
  return results.violations.map(violation => ({
    rule: violation.id,
    targets: violation.nodes.map(node => node.target),
  }));
}

test('track known violations', async ({ page }, testInfo) => {
  await page.goto('/dashboard');

  const results = await new AxeBuilder({ page }).analyze();

  // Als Attachment speichern (nicht im Snapshot-Vergleich)
  await testInfo.attach('accessibility-scan', {
    body: JSON.stringify(results, null, 2),
    contentType: 'application/json',
  });

  // Nur Fingerprint vergleichen (stabil)
  expect(violationFingerprints(results)).toMatchSnapshot();
});
```

---

## 10. AxeResults-Struktur

```typescript
interface AxeResults {
  violations: Result[];      // Gefundene Verstoesse
  passes: Result[];          // Bestandene Regeln
  incomplete: Result[];      // Unvollstaendige Pruefung (manuell noetig)
  inapplicable: Result[];    // Nicht anwendbare Regeln
  url: string;
  timestamp: string;
}

interface Result {
  id: string;                // Regel-ID z.B. 'color-contrast', 'image-alt'
  impact: 'minor' | 'moderate' | 'serious' | 'critical';
  description: string;
  help: string;
  helpUrl: string;           // Link zur axe-Dokumentation
  tags: string[];            // WCAG-Tags
  nodes: NodeResult[];
}

interface NodeResult {
  target: string[];          // CSS-Selektoren des betroffenen Elements
  html: string;              // HTML des Elements
  impact: string;
  any: Check[];              // Mindestens einer muss passen
  all: Check[];              // Alle muessen passen
  none: Check[];             // Keiner darf passen
  failureSummary: string;
}
```

---

## 11. Test-Fixtures fuer axe

Wiederverwendbare AxeBuilder-Konfiguration ueber Custom Fixtures:

```typescript
// playwright/fixtures.ts
import { test as base, expect } from '@playwright/test';
import { AxeBuilder } from '@axe-core/playwright';

type AxeFixture = {
  makeAxeBuilder: () => AxeBuilder;
};

export const test = base.extend<AxeFixture>({
  makeAxeBuilder: async ({ page }, use) => {
    const makeAxeBuilder = () => new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .exclude('#known-issue')
      .disableRules(['duplicate-id']); // projektweite Ausnahme

    await use(makeAxeBuilder);
  },
});

export { expect };
```

### Verwendung des Fixtures

```typescript
import { test, expect } from '../playwright/fixtures';

test('home page accessibility', async ({ page, makeAxeBuilder }) => {
  await page.goto('/');
  const results = await makeAxeBuilder().analyze();
  expect(results.violations).toEqual([]);
});

test('checkout flow accessibility', async ({ page, makeAxeBuilder }) => {
  await page.goto('/checkout');
  const results = await makeAxeBuilder()
    .include('#checkout-form')  // Zusaetzliche Eingrenzung
    .analyze();
  expect(results.violations).toEqual([]);
});
```

---

## 12. Dynamische Inhalte pruefen

```typescript
test('modal accessibility', async ({ page }) => {
  await page.goto('/products');

  // Warten bis Modal vollstaendig geladen
  await page.getByRole('button', { name: 'Quick View' }).click();
  const modal = page.getByRole('dialog');
  await modal.waitFor();

  // Nur den Modal-Bereich pruefen
  const results = await new AxeBuilder({ page })
    .include('[role="dialog"]')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## 13. ARIA-Snapshot vs. axe

| Aspekt | ARIA-Snapshot | axe-core |
|--------|---------------|----------|
| Package | Kein extra Package | `@axe-core/playwright` |
| Geschwindigkeit | Sehr schnell | Langsamer (ausfuehrlich) |
| WCAG-Konformitaet | Nein | Ja (WCAG-Tags) |
| Strukturpruefung | Ja (vollstaendig) | Teilweise |
| Falsch-Positive | Weniger | Moeglich |
| CI-Ausgabe | Diff-basiert | Versuche-Bericht |
| Empfehlung | Struktur-Regression | WCAG-Compliance |

---

Quelle: https://playwright.dev/docs/accessibility-testing | https://playwright.dev/docs/aria-snapshots
