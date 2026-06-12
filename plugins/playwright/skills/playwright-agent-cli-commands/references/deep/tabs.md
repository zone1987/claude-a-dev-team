# Playwright Agent CLI — Tabs

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `tab-list` | Alle offenen Tabs auflisten |
| `tab-new [url]` | Neuen Tab oeffnen |
| `tab-select <index>` | Zu Tab wechseln (per Index) |
| `tab-close [index]` | Tab schliessen |

---

## tab-list

```bash
playwright-cli tab-list
```

Ausgabe-Beispiel:

```
Tabs:
  [0] https://playwright.dev/ - Playwright
  [1] https://example.com/ - Example Domain [active]
  [2] https://github.com/ - GitHub
```

- Aktiver Tab wird mit `[active]` markiert
- Keine Argumente oder Optionen

---

## tab-new

```bash
playwright-cli tab-new                              # Leerer Tab
playwright-cli tab-new https://example.com          # Direkt navigieren
playwright-cli tab-new https://staging.example.com  # Staging-Umgebung
```

### tab-new-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `[url]` | string | Nein | URL zu der sofort navigiert wird (optional) |

---

## tab-select

```bash
playwright-cli tab-select 0   # Ersten Tab aktivieren
playwright-cli tab-select 1   # Zweiten Tab aktivieren
playwright-cli tab-select 2   # Dritten Tab aktivieren
```

### tab-select-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<index>` | number | Ja | Null-basierter Tab-Index (0 = erster Tab) |

Tab-Indizes sind null-basiert (0 = erster Tab).

---

## tab-close

```bash
playwright-cli tab-close       # Aktuellen Tab schliessen
playwright-cli tab-close 2     # Dritten Tab schliessen
playwright-cli tab-close 0     # Ersten Tab schliessen
```

### tab-close-Argumente

| Argument | Typ | Pflicht | Standard | Beschreibung |
|----------|-----|---------|---------|-------------|
| `[index]` | number | Nein | Aktueller Tab | Null-basierter Index des zu schliessenden Tabs |

---

## Workflow: Seiten vergleichen

```bash
# Zwei Umgebungen in separaten Tabs oeffnen
playwright-cli open https://staging.example.com
playwright-cli tab-new https://production.example.com

# Tabs pruefen
playwright-cli tab-list

# Staging inspizieren
playwright-cli tab-select 0
playwright-cli snapshot --filename=staging.yaml

# Produktion inspizieren
playwright-cli tab-select 1
playwright-cli snapshot --filename=production.yaml

# Zweiten Tab schliessen
playwright-cli tab-close 1
```

---

Quelle: https://playwright.dev/agent-cli/commands/tabs
