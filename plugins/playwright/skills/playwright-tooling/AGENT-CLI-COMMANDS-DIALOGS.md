# Playwright Agent CLI — Dialogs

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `dialog-accept [prompt]` | Dialog akzeptieren, optional mit Eingabetext fuer Prompt-Dialoge |
| `dialog-dismiss` | Dialog abbrechen (Cancel) |

---

## Hintergrund

Browser-Dialoge (alert, confirm, prompt) koennen Seiteninteraktionen blockieren. Wenn ein Dialog
erscheint, melden folgende Befehle dies und koennen nicht ausgefuehrt werden, bis der Dialog
behandelt wurde.

---

## dialog-accept

```bash
playwright-cli dialog-accept
playwright-cli dialog-accept "Alice"           # Prompt mit Text
playwright-cli dialog-accept "Bestaetigt"      # Alert/Confirm
```

### dialog-accept-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `[prompt]` | string | Nein | Text fuer Prompt-Dialoge (wird ignoriert bei alert/confirm) |

---

## dialog-dismiss

```bash
playwright-cli dialog-dismiss
```

Keine Argumente. Entspricht dem Klick auf "Cancel" / "Abbrechen".

---

## Dialog-Typen

### Alert-Dialog

```bash
playwright-cli click e5
# ⚠ Dialog appeared: [alert] "Item has been deleted."
playwright-cli dialog-accept
```

Alerts haben nur OK. `dialog-accept` und `dialog-dismiss` sind gleichwertig.

### Confirm-Dialog

```bash
playwright-cli click e10
# ⚠ Dialog appeared: [confirm] "Are you sure you want to delete this?"
# Bestaetigen (OK):
playwright-cli dialog-accept
# Abbrechen (Cancel):
playwright-cli dialog-dismiss
```

### Prompt-Dialog

```bash
playwright-cli click e8
# ⚠ Dialog appeared: [prompt] "Enter your name:"
# Mit Text akzeptieren:
playwright-cli dialog-accept "Alice"
# Abbrechen:
playwright-cli dialog-dismiss
```

---

## Workflow-Muster

Wenn ein Dialog erscheint, melden andere Befehle dies. Dialog zuerst behandeln:

```bash
playwright-cli click e15                         # Loeschen-Button klicken
# ⚠ Dialog appeared: [confirm] "Delete all items?"
playwright-cli snapshot                           # Meldet: Dialog is open
playwright-cli dialog-accept                      # Dialog zuerst behandeln
playwright-cli snapshot                           # Jetzt aktueller State
```

---

Quelle: https://playwright.dev/agent-cli/commands/dialogs
