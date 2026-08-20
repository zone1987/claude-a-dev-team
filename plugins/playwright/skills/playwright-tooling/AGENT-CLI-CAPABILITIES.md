# Playwright Agent CLI — Capabilities

The CLI and MCP share the same underlying Playwright tools, organised into
capability groups. In the CLI all capabilities are always
available — no gating.

---

## Contents

- [Core (always available)](#core-always-available)
- [Network](#network)
- [Storage](#storage)
- [Vision](#vision)
- [DevTools](#devtools)
- [PDF](#pdf)
- [Testing](#testing)

## Core (always available)

Basic browser automation.

| Command | Purpose |
|--------|-------|
| `open`, `goto`, `close` | Open the browser, navigate, close |
| `go-back`, `go-forward`, `reload` | Navigation history |
| `click`, `dblclick`, `hover`, `drag` | Element interaction |
| `type`, `fill`, `select` | Text input and dropdowns |
| `check`, `uncheck` | Checkboxes and radio buttons |
| `press`, `keydown`, `keyup` | Keyboard input |
| `snapshot` | Capture the accessibility tree |
| `screenshot` | Take a screenshot |
| `upload` | Upload files |
| `dialog-accept`, `dialog-dismiss` | Handle dialogs |
| `resize` | Adjust the browser window |
| `eval`, `run-code` | Execute JavaScript/Playwright code |

---

## Network

Network inspection and mocking.

| Command | Purpose |
|--------|-------|
| `network` | List network requests since the page was loaded |
| `route` | Mock requests for a URL pattern |
| `route-list` | List active mock routes |
| `unroute` | Remove mock routes |
| `network-state-set` | Set the online/offline state |

---

## Storage

Cookie, localStorage and sessionStorage management as well as state persistence.

| Command | Purpose |
|--------|-------|
| `state-save`, `state-load` | Save/restore the complete browser state |
| `cookie-list/get/set/delete/clear` | Manage cookies |
| `localstorage-list/get/set/delete/clear` | Manage localStorage |
| `sessionstorage-list/get/set/delete/clear` | Manage sessionStorage |

---

## Vision

Coordinate-based mouse interaction with pixel positions taken from screenshots.
Useful for canvas apps, maps and custom widgets without
accessible elements.

| Command | Purpose |
|--------|-------|
| `mousemove <x> <y>` | Move the mouse to coordinates |
| `mousedown [button]` | Press a mouse button |
| `mouseup [button]` | Release a mouse button |
| `mousewheel <dx> <dy>` | Scroll with the mouse wheel |
| `screenshot` | Capture the viewport as a coordinate reference |

---

## DevTools

Tracing, video recording and test debugging.

| Command | Purpose |
|--------|-------|
| `console` | Show console messages |
| `tracing-start`, `tracing-stop` | Record execution traces |
| `video-start`, `video-stop`, `video-chapter` | Record session videos |
| `show` | Open the visual dashboard |
| `pause-at`, `resume`, `step-over` | Test debugging |

---

## PDF

PDF generation.

| Command | Purpose |
|--------|-------|
| `pdf` | Export the page as a PDF |

---

## Testing

Assertions and test-generation tools.

| Command | Purpose |
|--------|-------|
| `verify-element-visible` | Verify an element is visible by role and name |
| `verify-text-visible` | Verify text is visible |
| `verify-list-visible` | Verify a list with entries is visible |
| `verify-value` | Check a form field value |
| `generate-locator` | Generate a Playwright locator for test code |

---

Source: https://playwright.dev/agent-cli/capabilities
