# Playwright Locators: Vollstaendige Referenz

Locators repraesentieren eine Methode, Elemente auf der Seite zu finden.
Alle Locator-Methoden sind verfuegbar auf `page`, `Locator` und `FrameLocator`.
Shadow DOM wird automatisch durchsucht (ausser XPath und geschlossene Shadow Roots).

---

## 1. getByRole()

Bevorzugter Locator. Findet Elemente nach ihrer ARIA-Rolle und ihrem zugaenglichen Namen.

```typescript
page.getByRole(role: AriaRole, options?)
```

### ARIA-Rollen (haeufig verwendet)

`alert`, `alertdialog`, `application`, `article`, `banner`, `blockquote`, `button`,
`caption`, `cell`, `checkbox`, `code`, `columnheader`, `combobox`, `complementary`,
`contentinfo`, `definition`, `deletion`, `dialog`, `directory`, `document`, `emphasis`,
`feed`, `figure`, `form`, `generic`, `grid`, `gridcell`, `group`, `heading`, `img`,
`insertion`, `link`, `list`, `listbox`, `listitem`, `log`, `main`, `marquee`, `math`,
`menu`, `menubar`, `menuitem`, `menuitemcheckbox`, `menuitemradio`, `meter`, `navigation`,
`none`, `note`, `option`, `paragraph`, `presentation`, `progressbar`, `radio`,
`radiogroup`, `region`, `row`, `rowgroup`, `rowheader`, `scrollbar`, `search`,
`searchbox`, `separator`, `slider`, `spinbutton`, `status`, `strong`, `subscript`,
`superscript`, `switch`, `tab`, `table`, `tablist`, `tabpanel`, `term`, `textbox`,
`time`, `timer`, `toolbar`, `tooltip`, `tree`, `treegrid`, `treeitem`

### Alle Optionen

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `name` | `string \| RegExp` | — | Zugaenglicher Name; case-insensitiver Teilstring (Default) oder Regex |
| `exact` | `boolean` | `false` | Exaktes Matching fuer `name` und `description`: case-sensitiv, vollstaendiger String |
| `checked` | `boolean` | — | `aria-checked` oder native Checkbox |
| `disabled` | `boolean` | — | `aria-disabled` oder `disabled`-Attribut (vererbt) |
| `expanded` | `boolean` | — | `aria-expanded` |
| `includeHidden` | `boolean` | `false` | Auch ARIA-versteckte Elemente einschliessen |
| `level` | `number` | — | `aria-level` (z.B. fuer heading h1-h6) |
| `pressed` | `boolean` | — | `aria-pressed` |
| `selected` | `boolean` | — | `aria-selected` |
| `description` | `string \| RegExp` | — | Zugaengliche Beschreibung (Teilstring/case-insensitiv) |

### Beispiele

```typescript
// Button mit Text
await page.getByRole('button', { name: 'Absenden' }).click();
await page.getByRole('button', { name: /absenden/i }).click();
await page.getByRole('button', { name: 'Absenden', exact: true }).click();

// Ueberschrift
await expect(page.getByRole('heading', { name: 'Registrieren', level: 2 })).toBeVisible();

// Checkbox
await page.getByRole('checkbox', { name: 'Newsletter' }).check();

// Link
await page.getByRole('link', { name: 'Mehr erfahren' }).click();

// Nur aktivierte Elemente
await page.getByRole('option', { selected: false }).first().click();

// Erweiterte Listenbox
await page.getByRole('combobox', { expanded: true }).locator('option').first().click();
```

---

## 2. getByText()

Findet Elemente anhand ihres sichtbaren Textinhalts.

```typescript
page.getByText(text: string | RegExp, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `exact` | `boolean` | `false` | `true` = exakter Match (case-sensitiv, ganzer String); `false` = Teilstring, case-insensitiv |

Whitespace wird automatisch normalisiert.

```typescript
// Teilstring (Standard)
await expect(page.getByText('Willkommen')).toBeVisible();

// Exakter Match
await expect(page.getByText('Willkommen, Maria', { exact: true })).toBeVisible();

// Regex
await expect(page.getByText(/willkommen, [A-Za-z]+/i)).toBeVisible();
```

---

## 3. getByLabel()

Findet Formularelemente anhand des zugehoerigen Label-Texts.

```typescript
page.getByLabel(text: string | RegExp, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exaktes Label-Text-Matching |

```typescript
await page.getByLabel('Benutzername').fill('maria');
await page.getByLabel('Passwort', { exact: true }).fill('geheim');
```

---

## 4. getByPlaceholder()

Findet Inputs anhand ihres Placeholder-Texts.

```typescript
page.getByPlaceholder(text: string | RegExp, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exaktes Placeholder-Text-Matching |

```typescript
await page.getByPlaceholder('name@beispiel.de').fill('user@test.de');
await page.getByPlaceholder(/suche/i).fill('Playwright');
```

---

## 5. getByAltText()

Findet Bilder (`<img>`) und `<area>`-Elemente anhand ihres Alt-Texts.

```typescript
page.getByAltText(text: string | RegExp, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exaktes Alt-Text-Matching |

```typescript
await page.getByAltText('Playwright Logo').click();
await expect(page.getByAltText(/firmen.*logo/i)).toBeVisible();
```

---

## 6. getByTitle()

Findet Elemente anhand ihres `title`-Attributs.

```typescript
page.getByTitle(text: string | RegExp, options?)
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exaktes Title-Matching |

```typescript
await expect(page.getByTitle('Anzahl der Issues')).toHaveText('25 Issues');
await page.getByTitle(/schliessen/i).click();
```

---

## 7. getByTestId()

Findet Elemente anhand des `data-testid`-Attributs (konfigurierbar).

```typescript
page.getByTestId(testId: string | RegExp)
```

```typescript
await page.getByTestId('route-button').click();
await expect(page.getByTestId(/submit/)).toBeVisible();
```

### Benutzerdefiniertes TestId-Attribut

```typescript
// playwright.config.ts
export default defineConfig({
  use: {
    testIdAttribute: 'data-pw',  // Standard: 'data-testid'
  },
});
```

---

## 8. locator() — CSS und XPath

```typescript
page.locator(selector: string | Locator, options?)
```

### CSS-Selektoren

```typescript
await page.locator('button').click();
await page.locator('css=button').click();                    // explizit
await page.locator('#submit-button').click();               // ID
await page.locator('.nav-link').first().click();            // Klasse
await page.locator('input[type="email"]').fill('a@b.de');   // Attribut
```

### CSS-Pseudoklassen (Playwright-spezifisch)

| Pseudoklasse | Beschreibung | Beispiel |
|---|---|---|
| `:has-text("text")` | Enthaelt Text irgendwo (case-insensitiv, Teilstring) | `article:has-text("News")` |
| `:text("text")` | Kleinstes Element mit Text (case-insensitiv, Teilstring) | `#nav :text("Start")` |
| `:text-is("text")` | Exakter Text (case-sensitiv, voller String) | `:text-is("Log in")` |
| `:text-matches("regex", "flags")` | Regex-Text-Matching | `:text-matches("Log\s*in", "i")` |
| `:visible` | Nur sichtbare Elemente | `button:visible` |
| `:has(selector)` | Enthaelt Kind-Element | `article:has(div.promo)` |
| `:is(sel1, sel2)` | Matches einer von mehreren | `:is(button, a):has-text("OK")` |
| `:nth-match(sel, n)` | N-tes Element (1-basiert) | `:nth-match(:text("Kaufen"), 2)` |

**Veraltete Layout-Pseudoklassen** (koennen bei Layout-AEnderungen brechen):
`:right-of()`, `:left-of()`, `:above()`, `:below()`, `:near()` (Standard: 50px)

### XPath-Selektoren

```typescript
await page.locator('xpath=//button').click();
await page.locator('//button').click();    // // am Anfang = automatisch XPath
await page.locator('..button').click();    // .. am Anfang = automatisch XPath

// XPath-Union (mehrere Ausdruecke)
await page.locator(
  '//span[contains(@class, "spinner")]|//div[@id="bestaetigung"]'
).waitFor();
```

Hinweis: XPath durchdringt Shadow DOM NICHT.

### locator()-Optionen

| Option | Typ | Beschreibung |
|---|---|---|
| `has` | `Locator` | Muss diesen Kind-Locator enthalten |
| `hasNot` | `Locator` | Darf diesen Kind-Locator NICHT enthalten |
| `hasText` | `string \| RegExp` | Muss diesen Text enthalten |
| `hasNotText` | `string \| RegExp` | Darf diesen Text NICHT enthalten |

```typescript
await page.locator('article', { hasText: 'Playwright' }).click();
await page.locator('li', { has: page.getByRole('checkbox') }).all();
```

---

## 9. Filtern mit filter()

```typescript
locator.filter(options?)
```

| Option | Typ | Beschreibung |
|---|---|---|
| `has` | `Locator` | Enthaelt dieses Kind-Element |
| `hasNot` | `Locator` | Enthaelt dieses Kind-Element NICHT |
| `hasText` | `string \| RegExp` | Enthaelt diesen Text |
| `hasNotText` | `string \| RegExp` | Enthaelt diesen Text NICHT |
| `visible` | `boolean` | Nur sichtbare / nur unsichtbare Elemente |

```typescript
// Nach Text filtern
await page.getByRole('listitem')
  .filter({ hasText: 'Produkt 2' })
  .getByRole('button', { name: 'In den Warenkorb' })
  .click();

// Nach Kind-Locator filtern
await page.getByRole('listitem')
  .filter({ has: page.getByRole('heading', { name: 'Produkt 2' }) })
  .getByRole('button', { name: 'Kaufen' })
  .click();

// Negierung: hat diesen Text NICHT
await expect(
  page.getByRole('listitem').filter({ hasNotText: 'Ausverkauft' })
).toHaveCount(5);

// Nur sichtbare Buttons
await page.locator('button').filter({ visible: true }).first().click();

// Verkettetes Filtern
const rows = page.getByRole('row')
  .filter({ has: page.getByRole('checkbox', { checked: true }) })
  .filter({ hasNotText: 'archiviert' });
```

---

## 10. and() und or()

### and() — Beide Bedingungen muessen erfuellt sein

```typescript
const button = page.getByRole('button').and(page.getByTitle('Newsletter abonnieren'));
await button.click();
```

### or() — Eine von zwei Bedingungen

Nuetzlich wenn zwei moegliche Ziele erscheinen koennen:

```typescript
const neueEmail = page.getByRole('button', { name: 'Neu' });
const dialog = page.getByText('Sicherheitseinstellungen bestaetigen');
await expect(neueEmail.or(dialog).first()).toBeVisible();
if (await dialog.isVisible()) {
  await page.getByRole('button', { name: 'Bestaetigen' }).click();
}
await neueEmail.click();
```

---

## 11. Listenoperationen

### nth(index) — Element per Index (0-basiert)

```typescript
const zweitesBanane = await page.getByRole('listitem').nth(1);
await page.getByRole('button').nth(0).click();   // erstes Element
await page.getByRole('button').nth(-1).click();  // letztes Element (via locator: nth=-1)
```

### first() und last()

```typescript
await page.getByRole('button').first().click();
await page.getByRole('listitem').last().click();
```

### all() — Alle Elemente als Array

```typescript
for (const row of await page.getByRole('listitem').all()) {
  console.log(await row.textContent());
}
```

### count() — Anzahl bestimmen

```typescript
const anzahl = await page.getByRole('listitem').count();
await expect(page.getByRole('listitem')).toHaveCount(5);
```

### evaluateAll() — JavaScript auf allen Elementen

```typescript
const texte = await page.getByRole('listitem')
  .evaluateAll(list => list.map(el => el.textContent));
```

---

## 12. Chaining (Verketten)

```typescript
// Engere Suche: innerhalb eines Containers
const nav = page.getByRole('navigation');
await nav.getByRole('link', { name: 'Start' }).click();

// Mehrstufig
await page.getByRole('table')
  .getByRole('row').filter({ hasText: 'Bestellung 42' })
  .getByRole('button', { name: 'Details' })
  .click();
```

---

## 13. FrameLocator — iframes

```typescript
// Elemente innerhalb eines iframes finden
const frame = page.frameLocator('iframe.login-frame');
await frame.getByLabel('Benutzername').fill('admin');
await frame.getByRole('button', { name: 'Einloggen' }).click();
```

### Alle FrameLocator-Methoden

| Methode | Signatur | Beschreibung |
|---|---|---|
| `frameLocator` | `(selector: string) => FrameLocator` | Verschachtelter Frame |
| `getByRole` | `(role, options?) => Locator` | Alle getByRole-Optionen |
| `getByText` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByLabel` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByPlaceholder` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByAltText` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByTitle` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByTestId` | `(testId: string \| RegExp) => Locator` | — |
| `locator` | `(selector, options?) => Locator` | CSS/XPath mit has/hasText etc. |
| `owner` | `() => Locator` | Locator fuer das iframe-Element selbst |

### Frame ueber Name oder URL (legacy)

```typescript
// Ueber Frame-Name
const frame = page.frame('frame-login');
await frame.fill('#username', 'admin');

// Ueber URL-Muster
const frame = page.frame({ url: /login/ });
```

---

## 14. Elternelement finden

```typescript
// Empfohlen: filter() mit has
const child = page.getByText('Inhalt');
const parent = page.getByRole('listitem').filter({ has: child });

// Alternative: XPath-Parent-Traversal
await page.locator('span').locator('xpath=..').click();
```

---

## 15. Legacy-Locatoren (veraltet, aber dokumentiert)

### text= Locator

```typescript
await page.locator('text=Einloggen').click();         // Teilstring, case-insensitiv
await page.locator('text="Einloggen"').click();       // Exakt
await page.locator('text=/ein.*gen/i').click();       // Regex
```

### Attribut-Kurz-Locatoren

```typescript
await page.locator('id=benutzername').fill('admin');
await page.locator('data-testid=submit').click();
await page.locator('data-test=submit').click();
await page.locator('data-test-id=submit').click();
```

Hinweis: Diese unterstuetzen keine CSS-Pseudoklassen wie `:enabled`.

### nth= Locator (legacy Index)

```typescript
await page.locator('button').locator('nth=0').click();   // erstes Element
await page.locator('button').locator('nth=-1').click();  // letztes Element
```

### Selektor-Verkettung mit >>

```typescript
await page.locator('css=article >> css=.preis >> css=span').click();
// * prefix: Intermediate-Element zurueckgeben
await page.locator('*css=article >> text=Willkommen').screenshot();
```

---

## 16. Locator Striktheit

Standardmaessig schlagen Operationen auf Einzel-Locatoren mit einem Fehler fehl,
wenn mehrere Elemente passen. Multi-Element-Operationen (`count()`, `all()`) funktionieren
mit mehreren Matches.

`strictSelectors: true` in `newContext()` erzwingt strikte Pruefung fuer alle Selektoren.

---

## Empfohlene Prioritaet

1. `getByRole()` — bevorzugt (zugaenglich, semantisch)
2. `getByLabel()` — fuer Formulare
3. `getByPlaceholder()` — wenn kein Label vorhanden
4. `getByText()` — fuer nicht-interaktive Elemente
5. `getByTestId()` — bei Test-spezifischen Attributen
6. `getByAltText()` / `getByTitle()` — fuer Bilder und Titel
7. CSS / XPath — nur wenn semantische Locatoren nicht moeglich sind

<!-- Quellen:
https://playwright.dev/docs/locators
https://playwright.dev/docs/other-locators
https://playwright.dev/docs/frames
https://playwright.dev/docs/api/class-locator
https://playwright.dev/docs/api/class-framelocator
https://playwright.dev/docs/api/class-page#page-get-by-role
-->
