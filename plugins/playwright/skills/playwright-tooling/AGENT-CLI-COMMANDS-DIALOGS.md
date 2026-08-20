# Playwright Agent CLI — Dialogs

## Command overview

| Command | Description |
|--------|-------------|
| `dialog-accept [prompt]` | Accept a dialog, optionally with input text for prompt dialogs |
| `dialog-dismiss` | Dismiss a dialog (Cancel) |

---

## Background

Browser dialogs (alert, confirm, prompt) can block page interactions. When a dialog
appears, the following commands report it and cannot be executed until the dialog
has been handled.

---

## dialog-accept

```bash
playwright-cli dialog-accept
playwright-cli dialog-accept "Alice"           # Prompt with text
playwright-cli dialog-accept "Confirmed"       # Alert/confirm
```

### dialog-accept arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `[prompt]` | string | No | Text for prompt dialogs (ignored for alert/confirm) |

---

## dialog-dismiss

```bash
playwright-cli dialog-dismiss
```

No arguments. Equivalent to clicking "Cancel".

---

## Dialog types

### Alert dialog

```bash
playwright-cli click e5
# ⚠ Dialog appeared: [alert] "Item has been deleted."
playwright-cli dialog-accept
```

Alerts only have OK. `dialog-accept` and `dialog-dismiss` are equivalent.

### Confirm dialog

```bash
playwright-cli click e10
# ⚠ Dialog appeared: [confirm] "Are you sure you want to delete this?"
# Confirm (OK):
playwright-cli dialog-accept
# Cancel:
playwright-cli dialog-dismiss
```

### Prompt dialog

```bash
playwright-cli click e8
# ⚠ Dialog appeared: [prompt] "Enter your name:"
# Accept with text:
playwright-cli dialog-accept "Alice"
# Cancel:
playwright-cli dialog-dismiss
```

---

## Workflow pattern

When a dialog appears, other commands report it. Handle the dialog first:

```bash
playwright-cli click e15                         # Click the delete button
# ⚠ Dialog appeared: [confirm] "Delete all items?"
playwright-cli snapshot                           # Reports: Dialog is open
playwright-cli dialog-accept                      # Handle the dialog first
playwright-cli snapshot                           # Now the current state
```

---

Source: https://playwright.dev/agent-cli/commands/dialogs
