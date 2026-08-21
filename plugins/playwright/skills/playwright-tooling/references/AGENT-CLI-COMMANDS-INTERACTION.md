# Playwright Agent CLI — Interaction

## Contents

- [Command overview](#command-overview)
- [Addressing elements](#addressing-elements)
- [click](#click)
- [dblclick](#dblclick)
- [fill](#fill)
- [type](#type)
- [select](#select)
- [check / uncheck](#check-uncheck)
- [hover](#hover)
- [drag](#drag)
- [upload](#upload)
- [resize](#resize)
- [Login workflow (example)](#login-workflow-example)

## Command overview

| Command | Description |
|--------|-------------|
| `click <ref> [button]` | Click an element (left, right or middle) |
| `dblclick <ref> [button]` | Double-click an element |
| `fill <ref> <text>` | Clear a text field and fill it |
| `fill <ref> <text> --submit` | Fill and press Enter |
| `type <text>` | Type text into the focused element |
| `select <ref> <value>` | Select a dropdown option |
| `check <ref>` | Click a checkbox or radio button (activate) |
| `uncheck <ref>` | Deactivate a checkbox |
| `hover <ref>` | Hover over an element |
| `drag <startRef> <endRef>` | Drag & drop |
| `upload <file>` | Upload a file |
| `resize <width> <height>` | Resize the browser window |

---

## Addressing elements

### Three supported methods

**Refs from snapshots (recommended):**

```bash
playwright-cli snapshot
playwright-cli click e15
playwright-cli fill e3 "hello"
```

**CSS selectors:**

```bash
playwright-cli click "#main > button.submit"
playwright-cli fill "#email" "test@example.com"
playwright-cli click "[data-testid='submit']"
```

**Playwright locators:**

```bash
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli fill "getByLabel('Email')" "test@example.com"
playwright-cli click "getByTestId('submit-button')"
playwright-cli click "getByText('Login')"
```

---

## click

```bash
playwright-cli click e15
playwright-cli click e15 right        # Right click
playwright-cli click e15 middle       # Middle click
playwright-cli click "#submit-btn"
playwright-cli click "getByRole('button', { name: 'Save' })"
```

### click arguments

| Argument | Type | Required | Default | Description |
|----------|-----|---------|---------|-------------|
| `<ref>` | string | Yes | — | Element ref, CSS selector or Playwright locator |
| `[button]` | string | No | `left` | Mouse button: `left`, `right`, `middle` |

---

## dblclick

```bash
playwright-cli dblclick e15
playwright-cli dblclick "#my-element"
```

### dblclick arguments

| Argument | Type | Required | Default | Description |
|----------|-----|---------|---------|-------------|
| `<ref>` | string | Yes | — | Element ref, CSS selector or Playwright locator |
| `[button]` | string | No | `left` | Mouse button: `left`, `right`, `middle` |

---

## fill

```bash
playwright-cli fill e3 "hello@example.com"
playwright-cli fill e3 "test input" --submit
playwright-cli fill "#search" "playwright"
playwright-cli fill "getByLabel('Email')" "user@example.com"
```

### fill arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `<ref>` | string | Yes | — | Element ref, CSS selector or Playwright locator |
| `<text>` | string | Yes | — | Text to enter (replaces existing content) |
| `--submit` | flag | No | false | Press Enter after filling |

---

## type

```bash
playwright-cli type "Buy groceries"
playwright-cli type "Water flowers"
```

### type arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<text>` | string | Yes | Text to type into the currently focused element |

Difference from `fill`: `type` simulates real keyboard input character by character,
`fill` sets the value directly and clears it beforehand.

---

## select

```bash
playwright-cli select e8 "Germany"
playwright-cli select "#country" "US"
playwright-cli select "getByLabel('Country')" "France"
```

### select arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<ref>` | string | Yes | Element ref, CSS selector or Playwright locator of the `<select>` element |
| `<value>` | string | Yes | Value (`value` attribute) or visible text of the option |

---

## check / uncheck

```bash
playwright-cli check e21
playwright-cli uncheck e21
playwright-cli check "[name='agree']"
```

### check/uncheck arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<ref>` | string | Yes | Element ref, CSS selector or Playwright locator of the checkbox/radio |

---

## hover

```bash
playwright-cli hover e20
playwright-cli hover "#menu-trigger"
playwright-cli hover "getByText('Hover me')"
```

### hover arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<ref>` | string | Yes | Element ref, CSS selector or Playwright locator |

---

## drag

```bash
playwright-cli drag e10 e20
playwright-cli drag "#draggable" "#droptarget"
```

### drag arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<startRef>` | string | Yes | Source element ref, CSS selector or Playwright locator |
| `<endRef>` | string | Yes | Target element ref, CSS selector or Playwright locator |

---

## upload

```bash
playwright-cli upload ./document.pdf
playwright-cli upload ./image.png
```

### upload arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<file>` | string (path) | Yes | Path to the file to upload |

The file input dialog must have been opened beforehand by a click.

---

## resize

```bash
playwright-cli resize 1280 720
playwright-cli resize 375 812          # iPhone size
playwright-cli resize 1920 1080        # Full HD desktop
```

### resize arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<width>` | number | Yes | Window width in pixels |
| `<height>` | number | Yes | Window height in pixels |

---

## Login workflow (example)

```bash
playwright-cli open https://app.example.com/login
playwright-cli snapshot
playwright-cli fill e3 "user@example.com"
playwright-cli fill e5 "password123" --submit
playwright-cli snapshot
playwright-cli screenshot --filename=after-login.png
```

---

Source: https://playwright.dev/agent-cli/commands/interaction
