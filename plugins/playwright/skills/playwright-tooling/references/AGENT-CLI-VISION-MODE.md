# Playwright Agent CLI — Vision Mode

## Contents

- [Overview](#overview)
- [Vision commands](#vision-commands)
- [Use cases](#use-cases)
- [Workflow 1: Canvas app](#workflow-1-canvas-app)
- [Workflow 2: Clicking an icon without an accessible name](#workflow-2-clicking-an-icon-without-an-accessible-name)
- [Workflow 3: Right-click context menu](#workflow-3-right-click-context-menu)
- [Workflow 4: Scrolling](#workflow-4-scrolling)
- [Determining coordinates](#determining-coordinates)

## Overview

Vision Mode enables interaction with page elements via coordinates and screenshots —
for elements that are not visible in the accessibility tree.

**Basic rule:** For most web applications the standard snapshot approach is
more reliable and more token-efficient. Only use Vision Mode when the accessibility tree
does not cover the use case.

---

## Vision commands

| Command | Type | Description |
|--------|-----|-------------|
| `mousemove <x> <y>` | Required: x (number), y (number) | Move the mouse to pixel coordinates |
| `mousedown [button]` | Optional: `left` (default), `right`, `middle` | Press a mouse button |
| `mouseup [button]` | Optional: `left` (default), `right`, `middle` | Release a mouse button |
| `mousewheel <dx> <dy>` | Required: dx (number), dy (number) | Scroll (dx=horizontal, dy=vertical) |
| `screenshot` | — | Capture the viewport as a coordinate reference |

---

## Use cases

| Scenario | Recommended approach |
|----------|-------------------|
| Clicking buttons, links, form elements | `click`, `fill`, ref-based commands |
| Canvas/WebGL applications | Mouse commands with coordinates |
| Map interaction (pan/zoom) | Mouse commands with coordinates |
| Image editing tools | Mouse commands with coordinates |
| Chart/graph interaction | Mouse commands with coordinates |
| Custom widgets without ARIA | Mouse commands with coordinates |
| Pixel-precise drag interactions | Mouse commands with coordinates |

---

## Workflow 1: Canvas app

```bash
# Take a screenshot as a visual reference
playwright-cli screenshot

# Identify coordinates from the screenshot, then interact
playwright-cli mousemove 100 200
playwright-cli mousedown
playwright-cli mousemove 300 400
playwright-cli mouseup

# Check the result
playwright-cli screenshot --filename=after-draw.png
```

## Workflow 2: Clicking an icon without an accessible name

```bash
# Take a screenshot to identify coordinates
playwright-cli screenshot --filename=reference.png

# Click based on coordinates
playwright-cli mousemove 450 320
playwright-cli mousedown
playwright-cli mouseup

# Check the result
playwright-cli screenshot --filename=after-click.png
```

## Workflow 3: Right-click context menu

```bash
playwright-cli screenshot
playwright-cli mousemove 300 400
playwright-cli mousedown right
playwright-cli mouseup right
playwright-cli snapshot
```

## Workflow 4: Scrolling

```bash
# Scroll down (500 pixels)
playwright-cli mousewheel 0 500

# Scroll right (200 pixels)
playwright-cli mousewheel 200 0

# Scroll up
playwright-cli mousewheel 0 -300
```

---

## Determining coordinates

1. Run `playwright-cli screenshot --filename=ref.png`
2. Analyse the image (visually or with an image-analysis tool)
3. Determine the x/y coordinates of the target element
4. Run `playwright-cli mousemove <x> <y>`
5. Perform mouse down/up or further actions
6. Check the result with a screenshot

---

Source: https://playwright.dev/agent-cli/vision-mode
