# Playwright — class: Accessibility (Deprecated / Entfernt)

> **Manifest:** 1 Methode (deprecated), 0 Properties, 0 Events.
> Diese Klasse ist aus den aktuellen Playwright-Docs entfernt worden.
> Der Accessibility-Snapshot ist jetzt ueber `page.ariaSnapshot()` verfuegbar.

---

## Status

Die `Accessibility`-Klasse war bis Playwright v1.x ueber `page.accessibility`
erreichbar und bot einen `snapshot()`-Befehl. Sie ist nicht mehr in der
aktuellen stabilen API-Dokumentation enthalten.

**Empfohlene Alternativen:**
- `page.ariaSnapshot()` — gibt einen ARIA-basierten Snapshot des DOM-Baums zurueck
- `page.getByRole()` — lokalisiert Elemente nach ARIA-Rolle und accessible name
- `@axe-core/playwright` — vollstaendige Accessibility-Pruefung mit axe-Engine

---

## Historische API: snapshot(options?)

Die Methode war ueber `page.accessibility.snapshot()` aufrufbar und gab
einen vereinfachten Accessibility-Baum der Seite zurueck.

**Signatur (historisch):**
```typescript
page.accessibility.snapshot(options?: {
  interestingOnly?: boolean;
  root?: ElementHandle;
}): Promise<null | AccessibilityNode>
```

**Parameter (historisch):**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.interestingOnly` | `boolean` | nein | `true` | Wenn `true`, werden nur "interessante" Knoten zurueckgegeben (d.h. Knoten mit semantischer Bedeutung) |
| `options.root` | `ElementHandle` | nein | — | Wurzelelement fuer den Snapshot; standardmaessig gesamte Seite |

**Rueckgabe (historisch):**
`Promise<null | AccessibilityNode>` — ein Objekt mit `role`, `name`, `value`,
`description`, `children` etc.

---

## Aktuelle Alternative: page.ariaSnapshot()

```typescript
page.ariaSnapshot(options?: {
  ref?: Locator;
  timeout?: number;
}): Promise<string>
```

Gibt einen ARIA-Snapshot als lesbaren String zurueck:

```javascript
const snapshot = await page.ariaSnapshot();
console.log(snapshot);
// Ausgabe:
// - heading "Willkommen" [level=1]
// - button "Anmelden"
// - textbox "E-Mail"
```

---

## Accessibility-Testing mit @axe-core/playwright

```javascript
const { chromium } = require('playwright');
const { AxeBuilder } = require('@axe-core/playwright');

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');

const results = await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa'])
  .analyze();

console.log('Violations:', results.violations);
await browser.close();
```

---

## ARIA-Role-basierte Lokalisierung

```javascript
// Button nach accessible name finden
await page.getByRole('button', { name: 'Absenden' }).click();

// Navigationslink
await page.getByRole('link', { name: 'Startseite' }).click();

// Formularfeld nach Label
await page.getByRole('textbox', { name: 'E-Mail-Adresse' }).fill('test@example.com');

// Heading-Text pruefen
await expect(page.getByRole('heading', { level: 1 })).toHaveText('Willkommen');
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 1 (historisch, nicht mehr verfuegbar) |
| Properties | 0     |
| Events    | 0      |

**Fazit:** Die separate `Accessibility`-Klasse existiert in der aktuellen
Playwright-API nicht mehr als eigenstaendige Doku-Seite. `page.ariaSnapshot()`
ist der moderne Ersatz fuer strukturelle Accessibility-Pruefungen. Fuer
umfassende WCAG-Compliance-Tests wird `@axe-core/playwright` empfohlen.
`page.getByRole()` mit `accessible name` ist die empfohlene Strategie fuer
Accessibility-bewusstes Element-Targeting in Tests.

---

*Hinweis: Die Seite https://playwright.dev/docs/api/class-accessibility
existiert nicht mehr in den aktuellen stabilen Playwright-Docs (Stand 2024/2025).
Alternativen: https://playwright.dev/docs/api/class-page#page-aria-snapshot*
