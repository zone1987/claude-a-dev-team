# Gotenberg — Markdown zu PDF (Vollreferenz)

**Route:** `POST /forms/chromium/convert/markdown`
**Beschreibung:** Konvertiert Markdown (inkl. MathJax) zu PDF via Headless Chromium.
Gotenberg wandelt Markdown zu HTML um und injiziert es in das bereitgestellte Template.

## Besonderheit: Template-Mechanismus

Die `index.html` muss eine Go-Template-Direktive enthalten:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>My PDF</title>
  </head>
  <body>
    {{ toHTML "file.md" }}
  </body>
</html>
```

Mehrere Markdown-Dateien koennen referenziert werden:
```html
{{ toHTML "intro.md" }}
{{ toHTML "chapter1.md" }}
{{ toHTML "chapter2.md" }}
```

## Pflicht-Files

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `files` (index.html) | file | Ja | HTML-Template-Datei (muss `index.html` heissen) |
| `files` (*.md) | file[] | Ja | Mindestens eine Markdown-Datei |

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.pdf
```

## Optionale Assets

```bash
--form files=@/path/to/img.png \
--form files=@/path/to/style.css
```

Alle Dateien landen in einem **flachen Verzeichnis** — nur Dateinamen verwenden.

## Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Ausgabe-Dateiname |
| `Gotenberg-Trace` | string | Random UUID | Request-ID |

## Alle weiteren Form-Felder

Identisch mit `/forms/chromium/convert/html`. Hier die Uebersicht:

### Seitenlayout

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `paperWidth` | string | `8.5` | Papierbreite in Zoll |
| `paperHeight` | string | `11` | Papierhoehe in Zoll |
| `marginTop` | string | `0.39` | Oberer Rand |
| `marginBottom` | string | `0.39` | Unterer Rand |
| `marginLeft` | string | `0.39` | Linker Rand |
| `marginRight` | string | `0.39` | Rechter Rand |
| `landscape` | boolean | `false` | Querformat |
| `scale` | number | `1.0` | Zoom-Faktor |
| `singlePage` | boolean | `false` | Gesamten Inhalt auf eine Seite |
| `preferCssPageSize` | boolean | `false` | CSS `@page` bevorzugen |

### Hintergrund

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Hintergrundgrafiken/-farben einschliessen |
| `omitBackground` | boolean | `false` | Weisshintergrund ausblenden |

### Druckmedien

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | `screen` oder `print` |
| `emulatedMediaFeatures` | json | — | CSS-Media-Feature-Overrides |

### JavaScript & Warten

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Feste Wartezeit |
| `waitForExpression` | string | — | JS-Ausdruck |
| `waitForSelector` | string | — | CSS-Selektor |

### Netzwerk

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie-Array |
| `extraHttpHeaders` | json | — | Zusaetzliche HTTP-Header |
| `userAgent` | string | — | User-Agent |
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 bei Status-Codes |
| `failOnResourceHttpStatusCodes` | json | — | 409 bei Asset-Status-Codes |
| `ignoreResourceHttpStatusDomains` | json | — | Ausnahme-Domains |
| `skipNetworkIdleEvent` | boolean | `true` | Nicht auf Netzwerk-Idle warten |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Nicht auf Fast-Idle warten |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 bei Ladefehler |
| `failOnConsoleExceptions` | boolean | `false` | 409 bei JS-Exceptions |

### Header & Footer

| Datei | Beschreibung |
|-------|-------------|
| `header.html` | Seitenkopf-Template |
| `footer.html` | Seitenfuss-Template |

### Metadaten & Anhange

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | Lesezeichen aus Ueberschriften |
| `generateTaggedPdf` | boolean | `false` | Barrierefreiheits-Tags |
| `metadata` | json | — | XMP-Metadaten |
| `embeds` (files) | file[] | — | Einzubettende Dateien |
| `embedsMetadata` | json | — | Embed-Metadaten |
| `facturxXml` (file) | file | — | Factur-X XML |
| `facturxConformanceLevel` | enum | — | Konformitaetsstufe |
| `facturxDocumentType` | enum | `INVOICE` | Dokumenttyp |
| `facturxVersion` | string | `1.0` | Version |
| `flatten` | boolean | `false` | Formularfelder glaetten |

### Split & Seitenauswahl

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Seitenauswahl (z.B. `1-5`) |
| `splitMode` | enum | — | `intervals` oder `pages` |
| `splitSpan` | string | — | Split-Regel |
| `splitUnify` | boolean | `false` | In eine Datei zusammenfuehren |

### Wasserzeichen & Stempel

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Inhalt/Dateiname |
| `watermarkPages` | string | Seitenbereiche |
| `watermarkOptions` | json | Engine-Optionen |
| `watermark` (file) | file | Wasserzeichen-Datei |
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Inhalt/Dateiname |
| `stampPages` | string | Seitenbereiche |
| `stampOptions` | json | Engine-Optionen |
| `stamp` (file) | file | Stempel-Datei |
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Seitenbereiche |

### PDF/A, PDF/UA, Verschluesselung

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | PDF/UA aktivieren |
| `userPassword` | string | — | Oeffnungs-Passwort |
| `ownerPassword` | string | — | Voll-Zugriff-Passwort |
| `allowPrinting` | boolean | `true` | Drucken |
| `allowCopying` | boolean | `true` | Kopieren |
| `allowModifying` | boolean | `true` | Bearbeiten |
| `allowAnnotating` | boolean | `true` | Annotieren |
| `allowFillingForms` | boolean | `true` | Formulare ausfullen |
| `allowAssembling` | boolean | `true` | Seiten-Assembly |

## Vollbeispiel

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  --form files=@/path/to/header.html \
  --form files=@/path/to/footer.html \
  --form paperWidth=8.27 \
  --form paperHeight=11.7 \
  --form printBackground=true \
  --form pdfa=PDF/A-2b \
  -o my.pdf
```

## Gesamtzahl Form-Felder: ~46

Pflicht-Files (2+) + Seitenlayout (10) + Hintergrund (2) + Medien (2) + JS/Warten (3) +
Netzwerk (10) + Header/Footer-Files (2) + Metadaten/Anhange (10) + Split (4) +
Wasserzeichen (12) + PDF/A (2) + Verschluesselung (8) = ~46 Felder + Datei-Inputs

---
Quelle: https://gotenberg.dev/docs/convert-with-chromium/convert-markdown-to-pdf
