# Playwright Agent CLI — Snapshots & accessibility tree

## Contents

- [Overview](#overview)
- [Element refs](#element-refs)
- [On-demand snapshots](#on-demand-snapshots)
- [Using refs](#using-refs)
- [Selectors as an alternative](#selectors-as-an-alternative)
- [Raw output](#raw-output)
- [Best practices](#best-practices)

## Overview

After every command `playwright-cli` prints a snapshot of the current browser state —
an accessibility tree with element refs for interaction.

### Automatic output

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/#/
- Page Title: React - TodoMVC

### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

### Example accessibility tree

```yaml
- heading "todos" [level=1]
- textbox "What needs to be done?" [ref=e5]
- listitem:
  - checkbox "Toggle Todo" [ref=e10]
  - text: "Buy groceries"
- listitem:
  - checkbox "Toggle Todo" [ref=e14]
  - text: "Water flowers"
- contentinfo:
  - text: "2 items left"
  - link "All" [ref=e20]
  - link "Active" [ref=e21]
  - link "Completed" [ref=e22]
```

---

## Element refs

| Property | Detail |
|-------------|--------|
| Format | `e` followed by a number (e.g. `e1`, `e15`, `e203`) |
| Validity | Unique within a single snapshot |
| Lifetime | Valid until the next page change |
| Assignment | Only interactive elements receive refs (buttons, links, inputs etc.) |

Important: **Refs are stable within a snapshot, but become invalid when the page
changes — always take a new snapshot after navigation.**

---

## On-demand snapshots

```bash
playwright-cli snapshot                           # Whole page, timestamped filename
playwright-cli snapshot --filename=after.yaml     # Custom filename
playwright-cli snapshot "#main"                   # Scope to a CSS selector
playwright-cli snapshot e34                       # Scope to an element ref
playwright-cli snapshot --depth=4                 # Limit tree depth
```

### snapshot options

| Option | Type | Description |
|--------|-----|-------------|
| `--filename=<name>` | string | Filename for the snapshot |
| `--depth=<n>` | number | Maximum tree depth (reduces output on complex pages) |
| `--raw` | flag | Command output only, without page information |
| `<ref>` | string | Element ref or CSS selector as scope |

---

## Using refs

```bash
playwright-cli click e10           # Click the checkbox
playwright-cli fill e5 "Walk the dog"  # Enter text into the textbox
playwright-cli hover e20           # Hover over the "All" link
```

---

## Selectors as an alternative

### CSS selectors

```bash
playwright-cli click "#main > button.submit"
playwright-cli click "[data-testid='submit']"
```

### Playwright locators

```bash
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli click "getByTestId('submit-button')"
playwright-cli click "getByText('Login')"
```

---

## Raw output

Omit page information, command output only:

```bash
playwright-cli snapshot --raw | grep "button"
```

---

## Best practices

1. **Use refs instead of selectors** — refs from snapshots are more reliable than CSS selectors,
   because they point at the exact element the agent has just seen.
2. **Re-snapshot after navigation** — refs become invalid when the page changes.
3. **Limit the depth** — use `--depth` on complex pages to reduce the output size.
4. **Scope to elements** — snapshot a specific section instead of the whole page.
5. **Name snapshot files** — use `--filename` when the snapshot is part of a workflow result.
6. **Check for dialogs** — if a command reports that a dialog is open, handle it first
   before performing further actions.

---

Source: https://playwright.dev/agent-cli/snapshots
