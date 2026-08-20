# Playwright Agent CLI — Screenshots & PDF

## Contents

- [Command overview](#command-overview)
- [screenshot](#screenshot)
- [pdf](#pdf)
- [snapshot (accessibility tree)](#snapshot-accessibility-tree)
- [When to use which tool](#when-to-use-which-tool)
- [Typical workflow](#typical-workflow)

## Command overview

| Command | Description |
|--------|-------------|
| `screenshot` | Screenshot of the visible viewport |
| `screenshot [ref]` | Screenshot of a specific element |
| `screenshot --filename=<name>` | Screenshot with a custom file name |
| `screenshot --full-page` | Screenshot of the entire scrollable page |
| `pdf` | Export the page as a PDF |
| `pdf --filename=<name>` | PDF with a custom file name |
| `snapshot` | Capture the accessibility tree (no visual image) |

---

## screenshot

```bash
playwright-cli screenshot
# Saved to: .playwright-cli/screenshot-2026-03-15.png

playwright-cli screenshot e15
# Screenshot of element e15

playwright-cli screenshot "#main"
# Screenshot of the element with ID 'main'

playwright-cli screenshot --filename=login-page.png
# Custom file name

playwright-cli screenshot --full-page --filename=full-page.png
# Entire scrollable page
```

### screenshot arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `[ref]` | string | No | — | Element ref or CSS selector for an element screenshot |
| `--filename=<name>` | string | No | Timestamp | File name for the screenshot |
| `--full-page` | flag | No | false | Capture the entire scrollable page |

Default location: `.playwright-cli/screenshot-<timestamp>.png`

---

## pdf

```bash
playwright-cli pdf
# Saved to: .playwright-cli/page-<timestamp>.pdf

playwright-cli pdf --filename=report.pdf
# Custom file name
```

### pdf options

| Option | Type | Required | Default | Description |
|--------|-----|---------|---------|-------------|
| `--filename=<name>` | string | No | Timestamp | File name for the PDF |

Default location: `.playwright-cli/page-<timestamp>.pdf`

---

## snapshot (accessibility tree)

In contrast to `screenshot` (visual), `snapshot` captures the accessibility tree.

```bash
playwright-cli snapshot                     # Whole page
playwright-cli snapshot --filename=f.yaml   # Custom file name
playwright-cli snapshot e34                 # Element scope by ref
playwright-cli snapshot "#main"             # Element scope by CSS selector
playwright-cli snapshot --depth=4           # Limit the tree depth
playwright-cli snapshot --raw               # Output only, without page information
```

---

## When to use which tool

| Use case | Recommended tool |
|----------------|-----------------|
| Check the visual layout | `screenshot` |
| Capture canvas/diagram content | `screenshot` |
| Document a bug | `screenshot` |
| Whole page as an image | `screenshot --full-page` |
| Export the page as a document | `pdf` |
| Find elements for interaction | `snapshot` (accessibility tree) |
| Understand the page structure | `snapshot` |
| Read text content | `snapshot` |
| Determine element refs for commands | `snapshot` |

---

## Typical workflow

```bash
# Load the page
playwright-cli open https://app.example.com --headed

# Take a structural snapshot
playwright-cli snapshot

# Interact
playwright-cli click e15
playwright-cli fill e3 "test@example.com"

# Take visual evidence
playwright-cli screenshot --filename=state-after-fill.png

# Bug documentation
playwright-cli screenshot --full-page --filename=full-bug-report.png
playwright-cli pdf --filename=bug-report.pdf
```

---

Source: https://playwright.dev/agent-cli/commands/screenshots-pdf
