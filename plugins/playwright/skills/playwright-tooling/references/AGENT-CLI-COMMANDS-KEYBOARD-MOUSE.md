# Playwright Agent CLI — Keyboard & Mouse

## Contents

- [Keyboard commands](#keyboard-commands)
- [press](#press)
- [keydown / keyup](#keydown-keyup)
- [Mouse commands](#mouse-commands)
- [mousemove](#mousemove)
- [mousedown / mouseup](#mousedown-mouseup)
- [mousewheel](#mousewheel)
- [When to use which approach](#when-to-use-which-approach)

## Keyboard commands

| Command | Description |
|--------|-------------|
| `press <key>` | Press and release a key |
| `keydown <key>` | Press a key down (keeps it held) |
| `keyup <key>` | Release a key |

---

## press

```bash
playwright-cli press Enter
playwright-cli press Tab
playwright-cli press Escape
playwright-cli press ArrowDown
playwright-cli press Control+a
playwright-cli press Control+c
playwright-cli press Control+v
playwright-cli press Shift+Tab
playwright-cli press Alt+Enter
```

### press arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<key>` | string | Yes | Key or key combination (e.g. `Enter`, `Control+a`) |

### Common keys

| Key | Description |
|-------|-------------|
| `Enter` | Confirm / submit form |
| `Tab` | Focus the next field |
| `Shift+Tab` | Focus the previous field |
| `Escape` | Cancel / close |
| `Backspace` | Delete character (backwards) |
| `Delete` | Delete character (forwards) |
| `Space` | Space / toggle checkbox |
| `ArrowUp` | Navigate up |
| `ArrowDown` | Navigate down |
| `ArrowLeft` | Navigate left |
| `ArrowRight` | Navigate right |
| `Home` | Jump to the beginning |
| `End` | Jump to the end |
| `PageUp` | Scroll one page up |
| `PageDown` | Scroll one page down |
| `Control+a` | Select all |
| `Control+c` | Copy |
| `Control+v` | Paste |
| `Control+x` | Cut |
| `Control+z` | Undo |
| `Control+y` | Redo |
| `F1` to `F12` | Function keys |

### Keyboard navigation (example)

```bash
playwright-cli press Tab                # Next field
playwright-cli press ArrowDown          # Dropdown navigation
playwright-cli press Enter              # Select option
playwright-cli press Shift+Tab          # Back
```

---

## keydown / keyup

For modified interactions (e.g. holding a key down while clicking):

```bash
playwright-cli keydown Shift
playwright-cli click e15               # Shift+click
playwright-cli keyup Shift
```

### keydown/keyup arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<key>` | string | Yes | Key to hold (e.g. `Shift`, `Control`, `Alt`) |

---

## Mouse commands

| Command | Description |
|--------|-------------|
| `mousemove <x> <y>` | Move the mouse to coordinates |
| `mousedown [button]` | Press a mouse button down |
| `mouseup [button]` | Release a mouse button |
| `mousewheel <dx> <dy>` | Scroll with the mouse wheel |

---

## mousemove

```bash
playwright-cli mousemove 100 200
playwright-cli mousemove 450 320
```

### mousemove arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<x>` | number | Yes | Horizontal coordinate in pixels |
| `<y>` | number | Yes | Vertical coordinate in pixels |

---

## mousedown / mouseup

```bash
# Left click at coordinates
playwright-cli mousemove 100 200
playwright-cli mousedown
playwright-cli mouseup

# Right click
playwright-cli mousemove 300 400
playwright-cli mousedown right
playwright-cli mouseup right

# Middle click
playwright-cli mousemove 500 300
playwright-cli mousedown middle
playwright-cli mouseup middle
```

### mousedown/mouseup arguments

| Argument | Type | Required | Default | Description |
|----------|-----|---------|---------|-------------|
| `[button]` | string | No | `left` | Button: `left`, `right`, `middle` |

---

## mousewheel

```bash
playwright-cli mousewheel 0 500        # Scroll 500px down
playwright-cli mousewheel 0 -300       # Scroll 300px up
playwright-cli mousewheel 200 0        # Scroll 200px right
playwright-cli mousewheel -100 0       # Scroll 100px left
playwright-cli mousewheel 0 1000       # Scroll quickly down
```

### mousewheel arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<dx>` | number | Yes | Horizontal scroll value in pixels (negative = left) |
| `<dy>` | number | Yes | Vertical scroll value in pixels (negative = up) |

---

## When to use which approach

| Scenario | Recommended approach |
|----------|-------------------|
| Clicking buttons, links, form fields | `click`, `fill`, ref-based commands |
| Canvas applications (drawing, maps) | Mouse commands with coordinates |
| Custom UI controls without accessibility | Mouse commands with coordinates |
| Drag interactions on pixel-precise targets | Mouse commands with coordinates |
| Keyboard shortcuts | `press` with modifier+key |
| Holding a modifier during a mouse click | `keydown` / `keyup` around `click` |

---

Source: https://playwright.dev/agent-cli/commands/keyboard-mouse
