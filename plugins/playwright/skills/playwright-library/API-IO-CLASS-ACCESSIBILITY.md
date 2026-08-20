# Playwright — class: Accessibility (deprecated / removed)

> **Manifest:** 1 method (deprecated), 0 properties, 0 events.
> This class has been removed from the current Playwright docs.
> The accessibility snapshot is now available via `page.ariaSnapshot()`.

---

## Contents

- [Status](#status)
- [Historical API: snapshot(options?)](#historical-api-snapshotoptions)
- [Current alternative: page.ariaSnapshot()](#current-alternative-pageariasnapshot)
- [Accessibility testing with @axe-core/playwright](#accessibility-testing-with-axe-coreplaywright)
- [ARIA role based locating](#aria-role-based-locating)
- [Manifest](#manifest)

## Status

The `Accessibility` class was reachable via `page.accessibility` up to
Playwright v1.x and offered a `snapshot()` command. It is no longer contained in the
current stable API documentation.

**Recommended alternatives:**
- `page.ariaSnapshot()` — returns an ARIA-based snapshot of the DOM tree
- `page.getByRole()` — locates elements by ARIA role and accessible name
- `@axe-core/playwright` — complete accessibility check with the axe engine

---

## Historical API: snapshot(options?)

The method was callable via `page.accessibility.snapshot()` and returned
a simplified accessibility tree of the page.

**Signature (historical):**
```typescript
page.accessibility.snapshot(options?: {
  interestingOnly?: boolean;
  root?: ElementHandle;
}): Promise<null | AccessibilityNode>
```

**Parameters (historical):**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `options.interestingOnly` | `boolean` | no | `true` | When `true`, only "interesting" nodes are returned (i.e. nodes with semantic meaning) |
| `options.root` | `ElementHandle` | no | — | Root element for the snapshot; by default the entire page |

**Returns (historical):**
`Promise<null | AccessibilityNode>` — an object with `role`, `name`, `value`,
`description`, `children` etc.

---

## Current alternative: page.ariaSnapshot()

```typescript
page.ariaSnapshot(options?: {
  ref?: Locator;
  timeout?: number;
}): Promise<string>
```

Returns an ARIA snapshot as a readable string:

```javascript
const snapshot = await page.ariaSnapshot();
console.log(snapshot);
// Output:
// - heading "Welcome" [level=1]
// - button "Sign in"
// - textbox "Email"
```

---

## Accessibility testing with @axe-core/playwright

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

## ARIA role based locating

```javascript
// Find a button by accessible name
await page.getByRole('button', { name: 'Submit' }).click();

// Navigation link
await page.getByRole('link', { name: 'Home' }).click();

// Form field by label
await page.getByRole('textbox', { name: 'Email address' }).fill('test@example.com');

// Check heading text
await expect(page.getByRole('heading', { level: 1 })).toHaveText('Welcome');
```

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 1 (historical, no longer available) |
| Properties | 0     |
| Events    | 0      |

**Conclusion:** The separate `Accessibility` class no longer exists in the current
Playwright API as a documentation page of its own. `page.ariaSnapshot()`
is the modern replacement for structural accessibility checks. For
comprehensive WCAG compliance tests, `@axe-core/playwright` is recommended.
`page.getByRole()` with `accessible name` is the recommended strategy for
accessibility-aware element targeting in tests.

---

*Note: the page https://playwright.dev/docs/api/class-accessibility
no longer exists in the current stable Playwright docs (as of 2024/2025).
Alternatives: https://playwright.dev/docs/api/class-page#page-aria-snapshot*
