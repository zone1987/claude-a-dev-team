# Gotenberg — HTML zu PDF

**Route:** `POST /forms/chromium/convert/html`

Konvertiert eine `index.html` (mit optionalen Assets) zu PDF via Headless Chromium.

## Pflichtfeld

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `files` (index.html) | file | HTML-Datei, muss `index.html` heissen |

## Gemeinsame Header

| Header | Beschreibung |
|--------|-------------|
| `Gotenberg-Output-Filename` | Dateiname (ohne Extension) |
| `Gotenberg-Trace` | Request-ID fuer Logs |

## Seitengroesse (ca. 10 Felder)

`paperWidth`, `paperHeight`, `marginTop`, `marginBottom`, `marginLeft`, `marginRight`,
`landscape`, `scale`, `singlePage`, `preferCssPageSize`

Vollstaendige Feldtabellen: `CHROMIUM-HTML-DETAIL.md`
