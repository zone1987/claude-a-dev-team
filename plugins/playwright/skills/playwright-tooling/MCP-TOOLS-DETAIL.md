# Playwright MCP: Complete Tool Reference

All tools are organised by capability group. Core tools are always available;
further groups must be enabled explicitly (`--caps=...`).

---

## Contents

- [Core: Navigation](#core-navigation)
- [Core: Snapshot](#core-snapshot)
- [Core: Interaction](#core-interaction)
- [Core: Forms](#core-forms)
- [Core: Screenshots](#core-screenshots)
- [Core: Keyboard & Mouse](#core-keyboard-mouse)
- [Core: Tabs](#core-tabs)
- [Core: Dialogs](#core-dialogs)
- [Core: Wait conditions](#core-wait-conditions)
- [Core: Console](#core-console)
- [Core: File Upload](#core-file-upload)
- [Code execution](#code-execution)
- [Network](#network)
- [Storage](#storage)
- [Testing](#testing)
- [Devtools: Tracing](#devtools-tracing)
- [Devtools: Video](#devtools-video)
- [PDF](#pdf)
- [Complete tool overview](#complete-tool-overview)
- [Source](#source)

## Core: Navigation

Capability: `core` (always active)

### `browser_navigate`

Navigates to a URL in the current tab.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `url` | string | Yes | Complete URL including protocol |

```
browser_navigate { url: "https://demo.playwright.dev/todomvc" }
```

Returns an accessibility snapshot of the loaded page.

---

### `browser_navigate_back`

Goes back in the browser history.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| — | — | — | No parameters |

---

### `browser_navigate_forward`

Goes forward in the browser history.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| — | — | — | No parameters |

---

### `browser_reload`

Reloads the current page.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| — | — | — | No parameters |

---

### `browser_close`

Closes the current tab and the browser.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| — | — | — | No parameters |

---

## Core: Snapshot

### `browser_snapshot`

Takes an accessibility snapshot of the current page.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| — | — | — | No parameters |

Returns a structured ARIA tree with ref IDs. Most tools return a snapshot automatically after actions.

---

## Core: Interaction

Capability: `core` (always active)

### `browser_click`

Clicks an element on the page.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference from the snapshot (e.g. `e5`) |

```
browser_click { ref: "e10" }
```

---

### `browser_hover`

Hovers over an element (tooltips, dropdown hover states).

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference from the snapshot |

---

### `browser_drag`

Drag and drop between two elements.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `startRef` | string | Yes | Element to be dragged |
| `endRef` | string | Yes | Target element |

---

### `browser_select_option`

Selects one or more options in a `<select>` dropdown.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | The `<select>` element |
| `values` | string[] | Yes | Values or labels of the options |

```
browser_select_option { ref: "e15", values: ["germany"] }
```

---

### `browser_resize`

Changes the size of the browser window.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `width` | number | Yes | Width in pixels |
| `height` | number | Yes | Height in pixels |

---

## Core: Forms

Capability: `core` (always active)

### `browser_type`

Enter text into editable elements (input, textarea, contenteditable).

| Parameter | Type | Required | Default | Description |
|-----------|-----|----------|---------|--------------|
| `ref` | string | Yes | — | Element reference |
| `text` | string | Yes | — | Text to be entered |
| `submit` | boolean | No | false | Press Enter after typing |
| `slowly` | boolean | No | false | Type character by character (triggers key handlers) |

```
browser_type { ref: "e5", text: "Buy groceries", submit: true }
browser_type { ref: "e8", text: "search query", slowly: true }
```

---

### `browser_fill_form`

Fills several form fields at once (more efficient than individual type/click calls).

Supported elements: textboxes, checkboxes, radio buttons, comboboxes, sliders.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `fields` | array | Yes | Array of `{ ref, value }` objects |

```
browser_fill_form {
  fields: [
    { ref: "e5", value: "Alice" },
    { ref: "e8", value: "alice@example.com" },
    { ref: "e12", value: true }
  ]
}
```

---

### `browser_check`

Activates a checkbox or a radio button.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference |

---

### `browser_uncheck`

Deactivates a checkbox.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference |

---

## Core: Screenshots

Capability: `core` (always active)

### `browser_take_screenshot`

Takes a screenshot of the current page, of an element or of the entire scrollable page.

| Parameter | Type | Required | Default | Description |
|-----------|-----|----------|---------|--------------|
| `type` | string | No | `png` | Image format: `png` or `jpeg` |
| `ref` | string | No | — | Element reference for an element screenshot |
| `fullPage` | boolean | No | false | Capture the entire scrollable page |

```
# Viewport screenshot
browser_take_screenshot {}

# Element screenshot
browser_take_screenshot { ref: "e20" }

# Complete page
browser_take_screenshot { fullPage: true, type: "jpeg" }
```

---

## Core: Keyboard & Mouse

Capability: `core` (always active, without vision)

### `browser_press_key`

Presses a key or a key combination.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `key` | string | Yes | Key or combination |

Common keys: `Enter`, `Tab`, `Escape`, `Backspace`, `Delete`, `ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`, `Home`, `End`, `PageUp`, `PageDown`, `F5`

Combinations: `Control+a`, `Control+c`, `Control+v`, `Shift+Tab`, `Alt+F4`

```
browser_press_key { key: "Control+a" }
browser_press_key { key: "Enter" }
```

---

### Vision mode: mouse tools

Only available with `--caps=vision`. They work with pixel coordinates from screenshots.

#### `browser_mouse_move_xy`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `x` | number | Yes | Horizontal pixel position |
| `y` | number | Yes | Vertical pixel position |

#### `browser_mouse_click_xy`

| Parameter | Type | Required | Default | Description |
|-----------|-----|----------|---------|--------------|
| `x` | number | Yes | — | Horizontal coordinate |
| `y` | number | Yes | — | Vertical coordinate |
| `button` | string | No | `left` | `left`, `right`, `middle` |
| `clickCount` | number | No | 1 | Number of clicks (2 for a double click) |
| `delay` | number | No | 0 | Pause between mousedown/mouseup (ms) |

#### `browser_mouse_drag_xy`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `startX` | number | Yes | Start X coordinate |
| `startY` | number | Yes | Start Y coordinate |
| `endX` | number | Yes | Target X coordinate |
| `endY` | number | Yes | Target Y coordinate |

#### `browser_mouse_down` / `browser_mouse_up`

Press / release the mouse button at the current position. No parameters.

#### `browser_mouse_wheel`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `deltaX` | number | Yes | Horizontal scroll amount (pixels) |
| `deltaY` | number | Yes | Vertical scroll amount (positive = downwards) |

---

## Core: Tabs

Capability: `core` (always active)

### `browser_tabs`

Manages browser tabs (list, create, close, switch).

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `action` | string | Yes | `list`, `new`, `close`, `select` |
| `url` | string | No | URL for the `new` action |
| `index` | number | No | Tab index for `select` or `close` |

```
# List all tabs
browser_tabs { action: "list" }

# Open a new tab
browser_tabs { action: "new", url: "https://example.com" }

# Switch to tab 1
browser_tabs { action: "select", index: 1 }

# Close the current tab
browser_tabs { action: "close" }

# Close a specific tab
browser_tabs { action: "close", index: 2 }
```

---

## Core: Dialogs

Capability: `core` (always active)

### `browser_handle_dialog`

Handles browser dialogs (alert, confirm, prompt).

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `accept` | boolean | Yes | `true` = accept, `false` = dismiss |
| `promptText` | string | No | Text for prompt dialogs |

```
# Confirm an alert
browser_handle_dialog { accept: true }

# Dismiss a confirm
browser_handle_dialog { accept: false }

# Confirm a prompt with text
browser_handle_dialog { accept: true, promptText: "My input value" }
```

Dialog types: `alert` (message), `confirm` (yes/no), `prompt` (text input)
Note: the dialog must be handled before further operations are possible.

---

## Core: Wait conditions

Capability: `core` (always active)

### `browser_wait_for`

Waits for a condition before continuing.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `time` | number | No | Wait this many seconds |
| `text` | string | No | Wait for this text to appear |
| `textGone` | string | No | Wait for this text to disappear |

```
# Wait 2 seconds
browser_wait_for { time: 2 }

# Wait for text
browser_wait_for { text: "Successfully saved" }

# Wait for the loading indicator to disappear
browser_wait_for { textGone: "Loading..." }
```

For more complex conditions: `browser_run_code { code: "await page.waitForSelector('.data-loaded')" }`

---

## Core: Console

Capability: `core` (always active)

### `browser_console_messages`

Accesses browser console output.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `level` | string | No | Minimum level: `error`, `warning`, `info`, `debug` |

Each level includes the more severe levels (`debug` = all).

---

### `browser_console_clear`

Clears the console message buffer. No parameters.

---

## Core: File Upload

Capability: `core` (always active)

### `browser_file_upload`

Handles file selection dialogs.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `paths` | string[] | Yes | Absolute file paths; empty array = cancel |

```
# Single file
browser_file_upload { paths: ["/home/user/report.pdf"] }

# Several files
browser_file_upload {
  paths: [
    "/home/user/photo1.jpg",
    "/home/user/photo2.jpg"
  ]
}

# Cancel
browser_file_upload { paths: [] }
```

Security: by default only from the MCP workspace roots. `--allow-unrestricted-file-access` for arbitrary paths.

---

## Code execution

Capability: `core` (always active)

### `browser_run_code`

Executes Playwright code snippets with full API access via a `page` object.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `code` | string | Yes | Playwright code string |

```
browser_run_code { code: "return await page.title()" }

browser_run_code {
  code: "await page.context().grantPermissions(['geolocation'])"
}

browser_run_code {
  code: "await page.evaluate(() => navigator.geolocation)"
}
```

Use for: complex multi-step logic, geolocation/permissions, custom wait conditions, iFrame interactions, clipboard operations.

---

### `browser_evaluate`

Evaluates JavaScript directly on the page or on an element.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `expression` | string | Yes | JavaScript code to execute |
| `ref` | string | No | Element reference for element scope |

```
browser_evaluate { expression: "document.title" }
browser_evaluate { expression: "getAttribute('href')", ref: "e20" }
browser_evaluate { expression: "window.innerWidth + 'x' + window.innerHeight" }
```

---

## Network

Capability: `network` (with `--caps=network`)

### `browser_network_requests`

Lists the network requests captured since the page load.

| Parameter | Type | Required | Default | Description |
|-----------|-----|----------|---------|--------------|
| `filter` | string | No | — | RegExp pattern for filtering by URL |
| `includeStatic` | boolean | No | false | Include images, CSS, fonts |
| `includeBody` | boolean | No | false | Include the request body |
| `includeHeaders` | boolean | No | false | Include the request headers |

---

### `browser_route`

Intercepts a URL and returns a custom response.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `pattern` | string | Yes | URL pattern with glob support |
| `status` | number | No | HTTP status code |
| `body` | string | No | Response body |
| `contentType` | string | No | Content-Type header |
| `headers` | object | No | Additional response headers |
| `removeHeaders` | string[] | No | Request headers to be removed |

```
browser_route {
  pattern: "**/api/users",
  status: 200,
  body: '{"users":[{"id":1,"name":"Test"}]}',
  contentType: "application/json"
}
```

---

### `browser_route_list`

Shows the active route patterns, status codes and content types. No parameters.

---

### `browser_unroute`

Removes active routes.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `pattern` | string | No | Specific pattern; omit = remove all |

---

### `browser_network_state_set`

Simulates the online/offline state.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `state` | string | Yes | `"online"` or `"offline"` |

---

## Storage

Capability: `storage` (with `--caps=storage`)

### `browser_storage_state`

Saves the complete browser state (cookies + localStorage) as JSON. No parameters.

---

### `browser_set_storage_state`

Restores a saved browser state.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `path` | string | Yes | Path to the state JSON file |

---

### Cookie tools

#### `browser_cookie_list`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `domain` | string | No | Filter by domain |
| `path` | string | No | Filter by path |

Returns: name, value, domain, HttpOnly, Secure, Expires.

#### `browser_cookie_get`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `name` | string | Yes | Cookie name |

#### `browser_cookie_set`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `name` | string | Yes | Cookie name |
| `value` | string | Yes | Cookie value |
| `domain` | string | No | Domain |
| `path` | string | No | Path |
| `expires` | number | No | Unix timestamp |
| `httpOnly` | boolean | No | HttpOnly flag |
| `secure` | boolean | No | Secure flag |
| `sameSite` | string | No | `Strict`, `Lax`, or `None` |

#### `browser_cookie_delete`

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `name` | string | Yes | Cookie name |

#### `browser_cookie_clear`

Deletes all cookies. No parameters.

---

### localStorage tools

#### `browser_localstorage_list`
Lists all localStorage entries. No parameters.

#### `browser_localstorage_get`
| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `key` | string | Yes | Key |

#### `browser_localstorage_set`
| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `key` | string | Yes | Key |
| `value` | string | Yes | Value |

#### `browser_localstorage_delete`
| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `key` | string | Yes | Key |

#### `browser_localstorage_clear`
Deletes all localStorage entries. No parameters.

### sessionStorage tools

Identical interface to localStorage, but limited to the session:
- `browser_sessionstorage_list`
- `browser_sessionstorage_get` (`key`)
- `browser_sessionstorage_set` (`key`, `value`)
- `browser_sessionstorage_delete` (`key`)
- `browser_sessionstorage_clear`

---

## Testing

Capability: `testing` (with `--caps=testing`)

### `browser_verify_element_visible`

Verifies the visibility of an element via its ARIA role.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `role` | string | Yes | ARIA role (e.g. `button`, `heading`, `textbox`) |
| `name` | string | Yes | Accessible name of the element |

```
browser_verify_element_visible { role: "button", name: "Save" }
```

---

### `browser_verify_text_visible`

Checks whether a text is visible on the page.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `text` | string | Yes | Text to be checked |

---

### `browser_verify_list_visible`

Validates a list against expected entries.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `label` | string | Yes | List label / accessible name |
| `items` | string[] | Yes | Expected list items |

---

### `browser_verify_value`

Checks whether the value of an element matches the expected value.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference |
| `value` | string | Yes | Expected value |

---

### `browser_generate_locator`

Generates a Playwright locator for an element (for test code generation).

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `ref` | string | Yes | Element reference from the snapshot |

```
browser_generate_locator { ref: "e5" }
// Returns: page.getByRole('textbox', { name: 'New todo' })
```

---

## Devtools: Tracing

Capability: `devtools` (with `--caps=devtools`)

### `browser_start_tracing`

Starts recording an execution trace. No parameters.

Recorded are: DOM snapshots, screenshots, network requests, console messages, timing.

---

### `browser_stop_tracing`

Stops the recording and saves it as a `.zip` file. No parameters.

```bash
# View the trace
npx playwright show-trace /output/trace-2024-03-15.zip
```

Automatic recording: the `--save-session` flag.

---

## Devtools: Video

Capability: `devtools` (with `--caps=devtools`)

### `browser_start_video`

Starts video recording of the browser session.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `filename` | string | No | Custom file name |
| `width` | number | No | Video width in pixels |
| `height` | number | No | Video height in pixels |

---

### `browser_stop_video`

Stops the recording and saves it as a WebM file. No parameters.

---

### `browser_video_chapter`

Inserts chapter markers into the recording.

| Parameter | Type | Required | Description |
|-----------|-----|----------|--------------|
| `title` | string | Yes | Chapter title |
| `description` | string | No | Chapter description |
| `duration` | number | No | Display duration in milliseconds |

---

## PDF

Capability: `pdf` (with `--caps=pdf`)

### `browser_pdf_save`

Exports the current page as a PDF file. No parameters.

The file is saved in the output directory. Use cases: receipts, archives, reports, documentation.

---

## Complete tool overview

| Tool | Capability | Parameters |
|------|-----------|-----------|
| `browser_navigate` | core | url |
| `browser_navigate_back` | core | — |
| `browser_navigate_forward` | core | — |
| `browser_reload` | core | — |
| `browser_close` | core | — |
| `browser_snapshot` | core | — |
| `browser_click` | core | ref |
| `browser_hover` | core | ref |
| `browser_drag` | core | startRef, endRef |
| `browser_select_option` | core | ref, values[] |
| `browser_resize` | core | width, height |
| `browser_type` | core | ref, text, [submit, slowly] |
| `browser_fill_form` | core | fields[] |
| `browser_check` | core | ref |
| `browser_uncheck` | core | ref |
| `browser_take_screenshot` | core | [type, ref, fullPage] |
| `browser_press_key` | core | key |
| `browser_tabs` | core | action, [url, index] |
| `browser_handle_dialog` | core | accept, [promptText] |
| `browser_wait_for` | core | [time, text, textGone] |
| `browser_console_messages` | core | [level] |
| `browser_console_clear` | core | — |
| `browser_file_upload` | core | paths[] |
| `browser_run_code` | core | code |
| `browser_evaluate` | core | expression, [ref] |
| `browser_mouse_move_xy` | vision | x, y |
| `browser_mouse_click_xy` | vision | x, y, [button, clickCount, delay] |
| `browser_mouse_drag_xy` | vision | startX, startY, endX, endY |
| `browser_mouse_down` | vision | — |
| `browser_mouse_up` | vision | — |
| `browser_mouse_wheel` | vision | deltaX, deltaY |
| `browser_network_requests` | core | [filter, includeStatic, includeBody, includeHeaders] |
| `browser_route` | network | pattern, [status, body, contentType, headers, removeHeaders] |
| `browser_route_list` | network | — |
| `browser_unroute` | network | [pattern] |
| `browser_network_state_set` | network | state |
| `browser_storage_state` | storage | — |
| `browser_set_storage_state` | storage | path |
| `browser_cookie_list` | storage | [domain, path] |
| `browser_cookie_get` | storage | name |
| `browser_cookie_set` | storage | name, value, [domain, path, expires, httpOnly, secure, sameSite] |
| `browser_cookie_delete` | storage | name |
| `browser_cookie_clear` | storage | — |
| `browser_localstorage_list` | storage | — |
| `browser_localstorage_get` | storage | key |
| `browser_localstorage_set` | storage | key, value |
| `browser_localstorage_delete` | storage | key |
| `browser_localstorage_clear` | storage | — |
| `browser_sessionstorage_*` | storage | (as localStorage) |
| `browser_verify_element_visible` | testing | role, name |
| `browser_verify_text_visible` | testing | text |
| `browser_verify_list_visible` | testing | label, items[] |
| `browser_verify_value` | testing | ref, value |
| `browser_generate_locator` | testing | ref |
| `browser_start_tracing` | devtools | — |
| `browser_stop_tracing` | devtools | — |
| `browser_start_video` | devtools | [filename, width, height] |
| `browser_stop_video` | devtools | — |
| `browser_video_chapter` | devtools | title, [description, duration] |
| `browser_pdf_save` | pdf | — |

---

## Source

- https://playwright.dev/mcp/tools/navigation
- https://playwright.dev/mcp/tools/interaction
- https://playwright.dev/mcp/tools/forms
- https://playwright.dev/mcp/tools/screenshots
- https://playwright.dev/mcp/tools/keyboard-mouse
- https://playwright.dev/mcp/tools/tabs
- https://playwright.dev/mcp/tools/dialogs
- https://playwright.dev/mcp/tools/waiting
- https://playwright.dev/mcp/tools/console
- https://playwright.dev/mcp/tools/file-upload
- https://playwright.dev/mcp/tools/code-execution
- https://playwright.dev/mcp/tools/network-mocking
- https://playwright.dev/mcp/tools/storage
- https://playwright.dev/mcp/tools/assertions
- https://playwright.dev/mcp/tools/tracing
- https://playwright.dev/mcp/tools/video
- https://playwright.dev/mcp/tools/pdf
