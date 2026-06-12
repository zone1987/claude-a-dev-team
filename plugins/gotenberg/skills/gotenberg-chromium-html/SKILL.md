---
name: gotenberg-chromium-html
description: >
  Gotenberg HTML zu PDF — alle Form-Felder, Header, Footer, Assets, Warte-Mechanismen,
  PDF/A, Wasserzeichen, Verschluesselung, Metadaten, Seitengroesse.
  Trigger: "HTML zu PDF Gotenberg", "HTML to PDF Gotenberg", "Gotenberg convert HTML",
  "Gotenberg paperWidth", "Gotenberg header footer", "Gotenberg marginTop",
  "Gotenberg printBackground", "Gotenberg waitDelay", "Gotenberg PDF/A HTML",
  "Gotenberg HTML form fields", "Gotenberg chromium HTML".
---

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

Vollstaendige Feldtabellen: `references/deep/chromium-html.md`
