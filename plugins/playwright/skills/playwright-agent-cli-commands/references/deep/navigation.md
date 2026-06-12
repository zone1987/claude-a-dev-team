# Playwright Agent CLI — Navigation

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `open [url]` | Browser oeffnen, optional zu URL navigieren |
| `goto <url>` | Zu einer URL navigieren |
| `go-back` | Zur vorherigen Seite zurueck |
| `go-forward` | Zur naechsten Seite vor |
| `reload` | Aktuelle Seite neu laden |
| `close` | Browser schliessen |

---

## open

```bash
playwright-cli open
playwright-cli open https://example.com
playwright-cli open https://example.com --headed
playwright-cli open https://example.com --browser=firefox
playwright-cli open https://example.com --persistent
playwright-cli open https://example.com --profile=./my-profile
playwright-cli open https://example.com --config=config.json
```

### open-Optionen

| Option | Typ | Standard | Beschreibung |
|--------|-----|---------|-------------|
| `[url]` | string | — | Zu oeffnende URL (optional) |
| `--headed` | flag | false | Browser-Fenster anzeigen |
| `--browser=<name>` | string | `chrome` | Browser: `chrome`, `firefox`, `webkit`, `msedge` |
| `--persistent` | flag | false | Profil auf Disk speichern |
| `--profile=<pfad>` | string | — | Benutzerdefiniertes Profil-Verzeichnis |
| `--config=<datei>` | string | — | Pfad zur JSON-Konfigurationsdatei |

---

## goto

```bash
playwright-cli goto https://demo.playwright.dev/todomvc
```

### goto-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<url>` | string | Ja | Vollstaendige URL inklusive Protokoll |

Ausgabe: Seiteninformationen (URL, Titel) und Snapshot-Dateireferenz.

---

## go-back / go-forward

```bash
playwright-cli goto https://example.com/page1
playwright-cli goto https://example.com/page2
playwright-cli go-back
playwright-cli go-forward
```

Keine Argumente oder Optionen.

---

## reload

```bash
playwright-cli reload
```

Keine Argumente. Laedt die aktuelle Seite neu.

---

## close

```bash
playwright-cli close          # Aktuellen Browser schliessen
playwright-cli close-all      # Alle Sessions schliessen
```

---

## Vollstaendiger Navigations-Workflow

```bash
playwright-cli open https://example.com --headed --browser=firefox
playwright-cli goto https://example.com/products
playwright-cli goto https://example.com/products/123
playwright-cli go-back
playwright-cli goto https://example.com/products/456
playwright-cli reload
playwright-cli close
```

---

Quelle: https://playwright.dev/agent-cli/commands/navigation
