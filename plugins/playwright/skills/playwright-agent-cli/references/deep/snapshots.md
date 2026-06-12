# Playwright Agent CLI — Snapshots & Accessibility-Tree

## Uebersicht

Nach jedem Befehl gibt `playwright-cli` einen Snapshot des aktuellen Browser-Zustands aus —
einen Accessibility-Tree mit Element-Refs fuer die Interaktion.

### Automatische Ausgabe

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/#/
- Page Title: React - TodoMVC

### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

### Beispiel-Accessibility-Tree

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

## Element-Refs

| Eigenschaft | Detail |
|-------------|--------|
| Format | `e` gefolgt von einer Zahl (z. B. `e1`, `e15`, `e203`) |
| Gueltigkeit | Eindeutig innerhalb eines einzelnen Snapshots |
| Lebensdauer | Gueltig bis zur naechsten Seitenaenderung |
| Zuweisung | Nur interaktive Elemente erhalten Refs (Buttons, Links, Inputs usw.) |

Wichtig: **Refs sind stabil innerhalb eines Snapshots, werden aber ungueltig wenn die Seite
sich aendert — immer neu snapshotten nach Navigation.**

---

## On-Demand-Snapshots

```bash
playwright-cli snapshot                           # Ganze Seite, Zeitstempel-Dateiname
playwright-cli snapshot --filename=after.yaml     # Benutzerdefinierter Dateiname
playwright-cli snapshot "#main"                   # Scope auf CSS-Selektor
playwright-cli snapshot e34                       # Scope auf Element-Ref
playwright-cli snapshot --depth=4                 # Baum-Tiefe begrenzen
```

### snapshot-Optionen

| Option | Typ | Beschreibung |
|--------|-----|-------------|
| `--filename=<name>` | string | Dateiname fuer den Snapshot |
| `--depth=<n>` | number | Maximale Baum-Tiefe (reduziert Output bei komplexen Seiten) |
| `--raw` | flag | Nur Befehlsausgabe, ohne Seiteninformationen |
| `<ref>` | string | Element-Ref oder CSS-Selektor als Scope |

---

## Refs verwenden

```bash
playwright-cli click e10           # Checkbox anklicken
playwright-cli fill e5 "Walk the dog"  # Text in Textbox eingeben
playwright-cli hover e20           # Ueber "All"-Link hovern
```

---

## Selektoren als Alternative

### CSS-Selektoren

```bash
playwright-cli click "#main > button.submit"
playwright-cli click "[data-testid='submit']"
```

### Playwright-Locators

```bash
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli click "getByTestId('submit-button')"
playwright-cli click "getByText('Login')"
```

---

## Raw-Output

Seiteninformationen weglassen, nur Befehlsausgabe:

```bash
playwright-cli snapshot --raw | grep "button"
```

---

## Best Practices

1. **Refs statt Selektoren verwenden** — Refs aus Snapshots sind zuverlaessiger als CSS-Selektoren,
   weil sie auf das genaue Element zeigen, das der Agent gerade gesehen hat.
2. **Nach Navigation neu snapshotten** — Refs werden ungueltig wenn die Seite sich aendert.
3. **Tiefe begrenzen** — `--depth` auf komplexen Seiten nutzen, um die Ausgabegroesse zu reduzieren.
4. **Auf Elemente scopen** — Einen spezifischen Abschnitt statt der ganzen Seite snapshotten.
5. **Snapshot-Dateien benennen** — `--filename` nutzen wenn der Snapshot Teil eines Workflow-Ergebnisses ist.
6. **Auf Dialoge pruefen** — Wenn ein Befehl meldet, dass ein Dialog offen ist, diesen zuerst
   behandeln bevor weitere Aktionen ausgefuehrt werden.

---

Quelle: https://playwright.dev/agent-cli/snapshots
