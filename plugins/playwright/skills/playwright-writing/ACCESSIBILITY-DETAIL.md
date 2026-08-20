# Playwright Accessibility Testing - Complete Reference

---

## Contents

- [1. Overview and limits](#1-overview-and-limits)
- [2. ARIA snapshots](#2-aria-snapshots)
- [3. ARIA snapshot template syntax](#3-aria-snapshot-template-syntax)
- [4. Matching modes](#4-matching-modes)
- [5. Regex matching in templates](#5-regex-matching-in-templates)
- [6. Snapshot generation and updating](#6-snapshot-generation-and-updating)
- [7. Code generator for ARIA snapshots](#7-code-generator-for-aria-snapshots)
- [8. axe-core integration](#8-axe-core-integration)
- [9. Axe examples](#9-axe-examples)
- [10. AxeResults structure](#10-axeresults-structure)
- [11. Test fixtures for axe](#11-test-fixtures-for-axe)
- [12. Checking dynamic content](#12-checking-dynamic-content)
- [13. ARIA snapshot vs. axe](#13-aria-snapshot-vs-axe)

## 1. Overview and limits

Automated accessibility tests can detect structural problems
(missing alt texts, wrong ARIA roles, missing labels). Many
accessibility problems, however, require manual checking with tools such as
"Accessibility Insights for Web".

Playwright offers two approaches:
1. **ARIA snapshots** - Playwright-native, fast, no extra package
2. **axe-core integration** - WCAG-compliant rule set, more detailed reports

---

## 2. ARIA snapshots

### toMatchAriaSnapshot(template, options?)

Compares the accessibility tree against a YAML template.

```typescript
// Whole page
await expect(page).toMatchAriaSnapshot(`
  - heading "Playwright" [level=1]
  - link "Get Started"
  - link "API Reference"
`);

// Specific element
await expect(page.locator('nav')).toMatchAriaSnapshot(`
  - list
    - listitem
      - link "Home"
    - listitem
      - link "About"
`);
```

### page.ariaSnapshot() / locator.ariaSnapshot()

Programmatic generation of the ARIA snapshot as a YAML string.

```typescript
const snapshot = await page.ariaSnapshot();
console.log(snapshot);

const navSnapshot = await page.locator('nav').ariaSnapshot();
```

---

## 3. ARIA snapshot template syntax

### Basic structure

```yaml
- role "accessible name" [attribute=value]
  - child-role "child name"
```

Each line: `- <role> "<name>"` optionally followed by `[attr=value]`.

### Roles (selection)

| ARIA/HTML role | Example |
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

### Attributes

| Attribute | Type | Example |
|----------|-----|---------|
| `checked` | boolean | `[checked]` or `[checked=false]` |
| `disabled` | boolean | `[disabled]` |
| `expanded` | boolean | `[expanded=true]` |
| `level` | number | `[level=2]` |
| `pressed` | boolean/mixed | `[pressed=true]` |
| `selected` | boolean | `[selected]` |
| `url` | string | `[url="https://example.com"]` |

---

## 4. Matching modes

### Partial matching (default)

Only the specified children must be present, further ones may exist.
The order must match.

```typescript
await expect(page).toMatchAriaSnapshot(`
  - heading "Products" [level=1]
  - list
    - listitem: "Laptop"
`);
// Also okay if further listitem elements are present
```

### children: equal

Exactly these children, no further ones allowed.

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

Exact match including all nested children.

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

### Global configuration

```typescript
// playwright.config.ts
export default defineConfig({
  expect: {
    toMatchAriaSnapshot: {
      children: 'equal',  // Default for all toMatchAriaSnapshot calls
    },
  },
});
```

---

## 5. Regex matching in templates

For dynamic texts (numbers, timestamps, etc.):

```typescript
// Number in heading
await expect(page).toMatchAriaSnapshot(`
  - heading /Issues \d+/ [level=2]
`);

// URL pattern on a link
await expect(page.locator('footer')).toMatchAriaSnapshot(`
  - link "YouTube":
    - /url: /https:\/\/www\.youtube\.com\/.*/
`);

// Any text
await expect(page.locator('.timestamp')).toMatchAriaSnapshot(`
  - text /\d{2}\.\d{2}\.\d{4}/
`);
```

---

## 6. Snapshot generation and updating

### Empty template (auto-generate)

```typescript
// Snapshot is created on the first run
await expect(page.locator('#navigation')).toMatchAriaSnapshot('');
```

### CLI flags

```bash
# Update all snapshots
npx playwright test --update-snapshots

# Short form
npx playwright test -u

# Update method (patch = git-apply-able diff, default)
npx playwright test --update-snapshots --update-source-method=patch

# Merge conflicts for manual selection
npx playwright test --update-snapshots --update-source-method=3way

# Direct overwrite
npx playwright test --update-snapshots --update-source-method=overwrite
```

### Separate snapshot files

```typescript
// Snapshot in its own .aria.yml file
await expect(page.getByRole('main')).toMatchAriaSnapshot({
  name: 'main-content.aria.yml',
});
// Stored in: {testFile}-snapshots/main-content.aria.yml
```

### Path configuration

```typescript
// playwright.config.ts
expect: {
  toMatchAriaSnapshot: {
    pathTemplate: '__aria_snapshots__/{testFilePath}/{arg}{ext}',
  },
},
```

---

## 7. Code generator for ARIA snapshots

The Playwright Inspector can create snapshots interactively:

1. Start `npx playwright codegen https://example.com`
2. Select the "Assert snapshot" action
3. Click an element -> ARIA snapshot is generated
4. The "Aria snapshot" tab shows roles, attributes, names

---

## 8. axe-core integration

### Installation

```bash
npm install --save-dev @axe-core/playwright
```

### AxeBuilder - constructor

```typescript
import { AxeBuilder } from '@axe-core/playwright';

const axeBuilder = new AxeBuilder({ page });
```

### AxeBuilder - methods

| Method | Parameter | Description |
|---------|-----------|--------------|
| `analyze()` | - | Run the scan, returns Promise<AxeResults> |
| `include(selector)` | `string \| string[]` | Check only these areas |
| `exclude(selector)` | `string \| string[]` | Exclude these areas |
| `withTags(tags)` | `string[]` | Only rules with these WCAG tags |
| `disableRules(rules)` | `string[]` | Disable specific rules |
| `withRules(rules)` | `string[]` | Check only specific rules |
| `options(options)` | `RunOptions` | Complete axe options |

---

### WCAG tags

| Tag | Meaning |
|-----|-----------|
| `'wcag2a'` | WCAG 2.0 Level A |
| `'wcag2aa'` | WCAG 2.0 Level AA |
| `'wcag21a'` | WCAG 2.1 Level A |
| `'wcag21aa'` | WCAG 2.1 Level AA |
| `'wcag22aa'` | WCAG 2.2 Level AA |
| `'best-practice'` | Best Practices |
| `'section508'` | US Section 508 |

---

## 9. Axe examples

### Simple page scan

```typescript
import { test, expect } from '@playwright/test';
import { AxeBuilder } from '@axe-core/playwright';

test('page should have no accessibility violations', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page }).analyze();

  expect(results.violations).toEqual([]);
});
```

### WCAG-compliant scan

```typescript
test('WCAG 2.1 AA compliance', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Targeted scan of an area

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

### Excluding known issues

```typescript
test('page with known issues excluded', async ({ page }) => {
  await page.goto('/legacy-section');

  const results = await new AxeBuilder({ page })
    .exclude('#legacy-widget')           // Exclude element + children
    .disableRules(['color-contrast'])    // Disable rule for the whole scan
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Violations fingerprint (recommended over a full snapshot)

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

  // Store as an attachment (not in the snapshot comparison)
  await testInfo.attach('accessibility-scan', {
    body: JSON.stringify(results, null, 2),
    contentType: 'application/json',
  });

  // Compare only the fingerprint (stable)
  expect(violationFingerprints(results)).toMatchSnapshot();
});
```

---

## 10. AxeResults structure

```typescript
interface AxeResults {
  violations: Result[];      // Violations found
  passes: Result[];          // Rules passed
  incomplete: Result[];      // Incomplete check (manual needed)
  inapplicable: Result[];    // Non-applicable rules
  url: string;
  timestamp: string;
}

interface Result {
  id: string;                // Rule ID e.g. 'color-contrast', 'image-alt'
  impact: 'minor' | 'moderate' | 'serious' | 'critical';
  description: string;
  help: string;
  helpUrl: string;           // Link to the axe documentation
  tags: string[];            // WCAG tags
  nodes: NodeResult[];
}

interface NodeResult {
  target: string[];          // CSS selectors of the affected element
  html: string;              // HTML of the element
  impact: string;
  any: Check[];              // At least one must match
  all: Check[];              // All must match
  none: Check[];             // None may match
  failureSummary: string;
}
```

---

## 11. Test fixtures for axe

Reusable AxeBuilder configuration via custom fixtures:

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
      .disableRules(['duplicate-id']); // project-wide exception

    await use(makeAxeBuilder);
  },
});

export { expect };
```

### Using the fixture

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
    .include('#checkout-form')  // Additional narrowing
    .analyze();
  expect(results.violations).toEqual([]);
});
```

---

## 12. Checking dynamic content

```typescript
test('modal accessibility', async ({ page }) => {
  await page.goto('/products');

  // Wait until the modal is fully loaded
  await page.getByRole('button', { name: 'Quick View' }).click();
  const modal = page.getByRole('dialog');
  await modal.waitFor();

  // Check only the modal area
  const results = await new AxeBuilder({ page })
    .include('[role="dialog"]')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## 13. ARIA snapshot vs. axe

| Aspect | ARIA snapshot | axe-core |
|--------|---------------|----------|
| Package | No extra package | `@axe-core/playwright` |
| Speed | Very fast | Slower (detailed) |
| WCAG conformance | No | Yes (WCAG tags) |
| Structure check | Yes (complete) | Partially |
| False positives | Fewer | Possible |
| CI output | Diff-based | Attempts report |
| Recommendation | Structure regression | WCAG compliance |

---

Source: https://playwright.dev/docs/accessibility-testing | https://playwright.dev/docs/aria-snapshots
