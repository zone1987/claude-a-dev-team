# Playwright Locators: Complete Reference

Locators represent a way to find elements on the page.
All locator methods are available on `page`, `Locator` and `FrameLocator`.
Shadow DOM is searched automatically (except XPath and closed shadow roots).

---

## Contents

- [1. getByRole()](#1-getbyrole)
- [2. getByText()](#2-getbytext)
- [3. getByLabel()](#3-getbylabel)
- [4. getByPlaceholder()](#4-getbyplaceholder)
- [5. getByAltText()](#5-getbyalttext)
- [6. getByTitle()](#6-getbytitle)
- [7. getByTestId()](#7-getbytestid)
- [8. locator() — CSS and XPath](#8-locator-css-and-xpath)
- [9. Filtering with filter()](#9-filtering-with-filter)
- [10. and() and or()](#10-and-and-or)
- [11. List operations](#11-list-operations)
- [12. Chaining](#12-chaining)
- [13. FrameLocator — iframes](#13-framelocator-iframes)
- [14. Finding the parent element](#14-finding-the-parent-element)
- [15. Legacy locators (deprecated, but documented)](#15-legacy-locators-deprecated-but-documented)
- [16. Locator strictness](#16-locator-strictness)
- [Recommended priority](#recommended-priority)

## 1. getByRole()

Preferred locator. Finds elements by their ARIA role and their accessible name.

```typescript
page.getByRole(role: AriaRole, options?)
```

### ARIA roles (commonly used)

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

### All options

| Option | Type | Default | Description |
|---|---|---|---|
| `name` | `string \| RegExp` | — | Accessible name; case-insensitive substring (default) or regex |
| `exact` | `boolean` | `false` | Exact matching for `name` and `description`: case-sensitive, full string |
| `checked` | `boolean` | — | `aria-checked` or native checkbox |
| `disabled` | `boolean` | — | `aria-disabled` or `disabled` attribute (inherited) |
| `expanded` | `boolean` | — | `aria-expanded` |
| `includeHidden` | `boolean` | `false` | Also include ARIA-hidden elements |
| `level` | `number` | — | `aria-level` (e.g. for heading h1-h6) |
| `pressed` | `boolean` | — | `aria-pressed` |
| `selected` | `boolean` | — | `aria-selected` |
| `description` | `string \| RegExp` | — | Accessible description (substring/case-insensitive) |

### Examples

```typescript
// Button with text
await page.getByRole('button', { name: 'Submit' }).click();
await page.getByRole('button', { name: /absenden/i }).click();
await page.getByRole('button', { name: 'Submit', exact: true }).click();

// Heading
await expect(page.getByRole('heading', { name: 'Registrieren', level: 2 })).toBeVisible();

// Checkbox
await page.getByRole('checkbox', { name: 'Newsletter' }).check();

// Link
await page.getByRole('link', { name: 'Mehr erfahren' }).click();

// Only enabled elements
await page.getByRole('option', { selected: false }).first().click();

// Expanded list box
await page.getByRole('combobox', { expanded: true }).locator('option').first().click();
```

---

## 2. getByText()

Finds elements by their visible text content.

```typescript
page.getByText(text: string | RegExp, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `exact` | `boolean` | `false` | `true` = exact match (case-sensitive, whole string); `false` = substring, case-insensitive |

Whitespace is normalized automatically.

```typescript
// Substring (default)
await expect(page.getByText('Welcome')).toBeVisible();

// Exact match
await expect(page.getByText('Welcome, Maria', { exact: true })).toBeVisible();

// Regex
await expect(page.getByText(/willkommen, [A-Za-z]+/i)).toBeVisible();
```

---

## 3. getByLabel()

Finds form elements by their associated label text.

```typescript
page.getByLabel(text: string | RegExp, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exact label text matching |

```typescript
await page.getByLabel('Username').fill('maria');
await page.getByLabel('Password', { exact: true }).fill('secret');
```

---

## 4. getByPlaceholder()

Finds inputs by their placeholder text.

```typescript
page.getByPlaceholder(text: string | RegExp, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exact placeholder text matching |

```typescript
await page.getByPlaceholder('name@beispiel.de').fill('user@test.de');
await page.getByPlaceholder(/suche/i).fill('Playwright');
```

---

## 5. getByAltText()

Finds images (`<img>`) and `<area>` elements by their alt text.

```typescript
page.getByAltText(text: string | RegExp, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exact alt text matching |

```typescript
await page.getByAltText('Playwright Logo').click();
await expect(page.getByAltText(/firmen.*logo/i)).toBeVisible();
```

---

## 6. getByTitle()

Finds elements by their `title` attribute.

```typescript
page.getByTitle(text: string | RegExp, options?)
```

| Option | Type | Default | Description |
|---|---|---|---|
| `exact` | `boolean` | `false` | Exact title matching |

```typescript
await expect(page.getByTitle('Anzahl der Issues')).toHaveText('25 Issues');
await page.getByTitle(/schliessen/i).click();
```

---

## 7. getByTestId()

Finds elements by the `data-testid` attribute (configurable).

```typescript
page.getByTestId(testId: string | RegExp)
```

```typescript
await page.getByTestId('route-button').click();
await expect(page.getByTestId(/submit/)).toBeVisible();
```

### Custom test ID attribute

```typescript
// playwright.config.ts
export default defineConfig({
  use: {
    testIdAttribute: 'data-pw',  // Default: 'data-testid'
  },
});
```

---

## 8. locator() — CSS and XPath

```typescript
page.locator(selector: string | Locator, options?)
```

### CSS selectors

```typescript
await page.locator('button').click();
await page.locator('css=button').click();                    // explicit
await page.locator('#submit-button').click();               // ID
await page.locator('.nav-link').first().click();            // class
await page.locator('input[type="email"]').fill('a@b.de');   // attribute
```

### CSS pseudo-classes (Playwright-specific)

| Pseudo-class | Description | Example |
|---|---|---|
| `:has-text("text")` | Contains text anywhere (case-insensitive, substring) | `article:has-text("News")` |
| `:text("text")` | Smallest element with text (case-insensitive, substring) | `#nav :text("Start")` |
| `:text-is("text")` | Exact text (case-sensitive, full string) | `:text-is("Log in")` |
| `:text-matches("regex", "flags")` | Regex text matching | `:text-matches("Log\s*in", "i")` |
| `:visible` | Only visible elements | `button:visible` |
| `:has(selector)` | Contains child element | `article:has(div.promo)` |
| `:is(sel1, sel2)` | Matches one of several | `:is(button, a):has-text("OK")` |
| `:nth-match(sel, n)` | N-th element (1-based) | `:nth-match(:text("Kaufen"), 2)` |

**Deprecated layout pseudo-classes** (can break on layout changes):
`:right-of()`, `:left-of()`, `:above()`, `:below()`, `:near()` (default: 50px)

### XPath selectors

```typescript
await page.locator('xpath=//button').click();
await page.locator('//button').click();    // // at the start = automatically XPath
await page.locator('..button').click();    // .. at the start = automatically XPath

// XPath union (multiple expressions)
await page.locator(
  '//span[contains(@class, "spinner")]|//div[@id="bestaetigung"]'
).waitFor();
```

Note: XPath does NOT pierce Shadow DOM.

### locator() options

| Option | Type | Description |
|---|---|---|
| `has` | `Locator` | Must contain this child locator |
| `hasNot` | `Locator` | Must NOT contain this child locator |
| `hasText` | `string \| RegExp` | Must contain this text |
| `hasNotText` | `string \| RegExp` | Must NOT contain this text |

```typescript
await page.locator('article', { hasText: 'Playwright' }).click();
await page.locator('li', { has: page.getByRole('checkbox') }).all();
```

---

## 9. Filtering with filter()

```typescript
locator.filter(options?)
```

| Option | Type | Description |
|---|---|---|
| `has` | `Locator` | Contains this child element |
| `hasNot` | `Locator` | Does NOT contain this child element |
| `hasText` | `string \| RegExp` | Contains this text |
| `hasNotText` | `string \| RegExp` | Does NOT contain this text |
| `visible` | `boolean` | Only visible / only invisible elements |

```typescript
// Filter by text
await page.getByRole('listitem')
  .filter({ hasText: 'Produkt 2' })
  .getByRole('button', { name: 'In den Warenkorb' })
  .click();

// Filter by child locator
await page.getByRole('listitem')
  .filter({ has: page.getByRole('heading', { name: 'Produkt 2' }) })
  .getByRole('button', { name: 'Kaufen' })
  .click();

// Negation: does NOT have this text
await expect(
  page.getByRole('listitem').filter({ hasNotText: 'Ausverkauft' })
).toHaveCount(5);

// Only visible buttons
await page.locator('button').filter({ visible: true }).first().click();

// Chained filtering
const rows = page.getByRole('row')
  .filter({ has: page.getByRole('checkbox', { checked: true }) })
  .filter({ hasNotText: 'archiviert' });
```

---

## 10. and() and or()

### and() — Both conditions must be satisfied

```typescript
const button = page.getByRole('button').and(page.getByTitle('Newsletter abonnieren'));
await button.click();
```

### or() — One of two conditions

Useful when two possible targets can appear:

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

## 11. List operations

### nth(index) — Element by index (0-based)

```typescript
const zweitesBanane = await page.getByRole('listitem').nth(1);
await page.getByRole('button').nth(0).click();   // first element
await page.getByRole('button').nth(-1).click();  // last element (via locator: nth=-1)
```

### first() and last()

```typescript
await page.getByRole('button').first().click();
await page.getByRole('listitem').last().click();
```

### all() — All elements as an array

```typescript
for (const row of await page.getByRole('listitem').all()) {
  console.log(await row.textContent());
}
```

### count() — Determine the number

```typescript
const anzahl = await page.getByRole('listitem').count();
await expect(page.getByRole('listitem')).toHaveCount(5);
```

### evaluateAll() — JavaScript on all elements

```typescript
const texte = await page.getByRole('listitem')
  .evaluateAll(list => list.map(el => el.textContent));
```

---

## 12. Chaining

```typescript
// Narrower search: within a container
const nav = page.getByRole('navigation');
await nav.getByRole('link', { name: 'Start' }).click();

// Multi-level
await page.getByRole('table')
  .getByRole('row').filter({ hasText: 'Bestellung 42' })
  .getByRole('button', { name: 'Details' })
  .click();
```

---

## 13. FrameLocator — iframes

```typescript
// Find elements inside an iframe
const frame = page.frameLocator('iframe.login-frame');
await frame.getByLabel('Username').fill('admin');
await frame.getByRole('button', { name: 'Einloggen' }).click();
```

### All FrameLocator methods

| Method | Signature | Description |
|---|---|---|
| `frameLocator` | `(selector: string) => FrameLocator` | Nested frame |
| `getByRole` | `(role, options?) => Locator` | All getByRole options |
| `getByText` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByLabel` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByPlaceholder` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByAltText` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByTitle` | `(text, options?) => Locator` | `exact?: boolean` |
| `getByTestId` | `(testId: string \| RegExp) => Locator` | — |
| `locator` | `(selector, options?) => Locator` | CSS/XPath with has/hasText etc. |
| `owner` | `() => Locator` | Locator for the iframe element itself |

### Frame by name or URL (legacy)

```typescript
// By frame name
const frame = page.frame('frame-login');
await frame.fill('#username', 'admin');

// By URL pattern
const frame = page.frame({ url: /login/ });
```

---

## 14. Finding the parent element

```typescript
// Recommended: filter() with has
const child = page.getByText('Inhalt');
const parent = page.getByRole('listitem').filter({ has: child });

// Alternative: XPath parent traversal
await page.locator('span').locator('xpath=..').click();
```

---

## 15. Legacy locators (deprecated, but documented)

### text= locator

```typescript
await page.locator('text=Einloggen').click();         // substring, case-insensitive
await page.locator('text="Einloggen"').click();       // exact
await page.locator('text=/ein.*gen/i').click();       // regex
```

### Attribute shorthand locators

```typescript
await page.locator('id=benutzername').fill('admin');
await page.locator('data-testid=submit').click();
await page.locator('data-test=submit').click();
await page.locator('data-test-id=submit').click();
```

Note: These do not support CSS pseudo-classes such as `:enabled`.

### nth= locator (legacy index)

```typescript
await page.locator('button').locator('nth=0').click();   // first element
await page.locator('button').locator('nth=-1').click();  // last element
```

### Selector chaining with >>

```typescript
await page.locator('css=article >> css=.preis >> css=span').click();
// * prefix: return the intermediate element
await page.locator('*css=article >> text=Welcome').screenshot();
```

---

## 16. Locator strictness

By default, operations on single-element locators fail with an error
when multiple elements match. Multi-element operations (`count()`, `all()`) work
with multiple matches.

`strictSelectors: true` in `newContext()` enforces strict checking for all selectors.

---

## Recommended priority

1. `getByRole()` — preferred (accessible, semantic)
2. `getByLabel()` — for forms
3. `getByPlaceholder()` — when no label is present
4. `getByText()` — for non-interactive elements
5. `getByTestId()` — for test-specific attributes
6. `getByAltText()` / `getByTitle()` — for images and titles
7. CSS / XPath — only when semantic locators are not possible

<!-- Sources:
https://playwright.dev/docs/locators
https://playwright.dev/docs/other-locators
https://playwright.dev/docs/frames
https://playwright.dev/docs/api/class-locator
https://playwright.dev/docs/api/class-framelocator
https://playwright.dev/docs/api/class-page#page-get-by-role
-->
