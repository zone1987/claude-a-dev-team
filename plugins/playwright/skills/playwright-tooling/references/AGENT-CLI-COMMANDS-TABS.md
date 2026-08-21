# Playwright Agent CLI — Tabs

## Contents

- [Command overview](#command-overview)
- [tab-list](#tab-list)
- [tab-new](#tab-new)
- [tab-select](#tab-select)
- [tab-close](#tab-close)
- [Workflow: comparing pages](#workflow-comparing-pages)

## Command overview

| Command | Description |
|--------|-------------|
| `tab-list` | List all open tabs |
| `tab-new [url]` | Open a new tab |
| `tab-select <index>` | Switch to a tab (by index) |
| `tab-close [index]` | Close a tab |

---

## tab-list

```bash
playwright-cli tab-list
```

Example output:

```
Tabs:
  [0] https://playwright.dev/ - Playwright
  [1] https://example.com/ - Example Domain [active]
  [2] https://github.com/ - GitHub
```

- The active tab is marked with `[active]`
- No arguments or options

---

## tab-new

```bash
playwright-cli tab-new                              # Empty tab
playwright-cli tab-new https://example.com          # Navigate directly
playwright-cli tab-new https://staging.example.com  # Staging environment
```

### tab-new arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `[url]` | string | No | URL to navigate to immediately (optional) |

---

## tab-select

```bash
playwright-cli tab-select 0   # Activate the first tab
playwright-cli tab-select 1   # Activate the second tab
playwright-cli tab-select 2   # Activate the third tab
```

### tab-select arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<index>` | number | Yes | Zero-based tab index (0 = first tab) |

Tab indices are zero-based (0 = first tab).

---

## tab-close

```bash
playwright-cli tab-close       # Close the current tab
playwright-cli tab-close 2     # Close the third tab
playwright-cli tab-close 0     # Close the first tab
```

### tab-close arguments

| Argument | Type | Required | Default | Description |
|----------|-----|---------|---------|-------------|
| `[index]` | number | No | Current tab | Zero-based index of the tab to close |

---

## Workflow: comparing pages

```bash
# Open two environments in separate tabs
playwright-cli open https://staging.example.com
playwright-cli tab-new https://production.example.com

# Check the tabs
playwright-cli tab-list

# Inspect staging
playwright-cli tab-select 0
playwright-cli snapshot --filename=staging.yaml

# Inspect production
playwright-cli tab-select 1
playwright-cli snapshot --filename=production.yaml

# Close the second tab
playwright-cli tab-close 1
```

---

Source: https://playwright.dev/agent-cli/commands/tabs
