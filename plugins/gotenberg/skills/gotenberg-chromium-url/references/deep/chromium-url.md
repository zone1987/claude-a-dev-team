# Gotenberg — URL zu PDF (Vollreferenz)

**Route:** `POST /forms/chromium/convert/url`
**Beschreibung:** Konvertiert eine Webseite per URL zu PDF via Headless Chromium.
Unterstuetzt JavaScript, SPAs und dynamischen Inhalt.

## Pflicht-Formularfeld

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `url` | string | Ja | URL der zu konvertierenden Seite. `file://`-URLs werden mit 400 abgelehnt. Lokale HTML-Dateien ueber `/forms/chromium/convert/html` konvertieren. |

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o my.pdf
```

## Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Dateiname der Ausgabe (ohne Extension) |
| `Gotenberg-Trace` | string | Random UUID | Eigene Request-ID fuer Logs |

## Seitenlayout

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `paperWidth` | string | `8.5` | Papierbreite in Zoll (Einheiten: in, pt, cm) |
| `paperHeight` | string | `11` | Papierhoehe in Zoll |
| `marginTop` | string | `0.39` | Oberer Rand in Zoll |
| `marginBottom` | string | `0.39` | Unterer Rand |
| `marginLeft` | string | `0.39` | Linker Rand |
| `marginRight` | string | `0.39` | Rechter Rand |
| `landscape` | boolean | `false` | Querformat |
| `scale` | number | `1.0` | Zoom-Faktor |
| `singlePage` | boolean | `false` | Gesamter Inhalt auf eine Seite |
| `preferCssPageSize` | boolean | `false` | CSS `@page` statt API-Parametern |

## Hintergrund

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Hintergrundgrafiken/-farben einschliessen |
| `omitBackground` | boolean | `false` | Weisshintergrund ausblenden |

## Druckmedien

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | `screen` oder `print` |
| `emulatedMediaFeatures` | json | — | CSS-Media-Feature-Overrides (z.B. Dark Mode) |

## JavaScript & Warten

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Feste Wartezeit (z.B. `5s`, `500ms`) |
| `waitForExpression` | string | — | JS-Ausdruck; Konvertierung startet wenn `true` |
| `waitForSelector` | string | — | CSS-Selektor; Start wenn Element im DOM |

## Netzwerk

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie-Array fuer Auth/Session |
| `extraHttpHeaders` | json | — | Zusaetzliche HTTP-Header fuer alle Browser-Requests |
| `userAgent` | string | — | User-Agent ueberschreiben |
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 bei diesen Status-Codes der Haupt-URL |
| `failOnResourceHttpStatusCodes` | json | — | 409 bei diesen Codes eines Assets |
| `ignoreResourceHttpStatusDomains` | json | — | Domains von Status-Code-Pruefung ausschliessen |
| `skipNetworkIdleEvent` | boolean | `true` | Nicht auf Netzwerk-Idle warten |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Nicht auf Fast-Idle warten |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 bei Asset-Ladefehlern |
| `failOnConsoleExceptions` | boolean | `false` | 409 bei JS-Exceptions |

## Header & Footer

| Datei | Beschreibung |
|-------|-------------|
| `header.html` | Vollstaendiges HTML fuer Seitenkopf |
| `footer.html` | Vollstaendiges HTML fuer Seitenfuss |

## Struktur & Metadaten

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | PDF-Lesezeichen aus Ueberschriften |
| `generateTaggedPdf` | boolean | `false` | Barrierefreiheits-Tags |
| `metadata` | json | — | XMP-Metadaten |
| `embeds` (files) | file[] | — | Einzubettende Dateien |
| `embedsMetadata` | json | — | Pro-Anhang-Metadaten |
| `facturxXml` (file) | file | — | Factur-X XML |
| `facturxConformanceLevel` | enum | — | Factur-X-Konformitaetsstufe |
| `facturxDocumentType` | enum | `INVOICE` | Factur-X-Dokumenttyp |
| `facturxVersion` | string | `1.0` | Factur-X-Version |
| `flatten` | boolean | `false` | Formularfelder glaetten |

## Split & Seiten

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Native Seitenauswahl (z.B. `1-5, 8`) |
| `splitMode` | enum | — | `intervals` oder `pages` |
| `splitSpan` | string | — | Split-Regel |
| `splitUnify` | boolean | `false` | Pages-Modus: in eine Datei |

## Wasserzeichen & Stempel

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Inhalt oder Dateiname |
| `watermarkPages` | string | Seitenbereiche |
| `watermarkOptions` | json | Engine-Optionen |
| `watermark` (file) | file | Wasserzeichen-Datei |
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Inhalt oder Dateiname |
| `stampPages` | string | Seitenbereiche |
| `stampOptions` | json | Engine-Optionen |
| `stamp` (file) | file | Stempel-Datei |
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Seitenbereiche |

## PDF/A & Zugaenglichkeit

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | PDF/UA aktivieren |

## Verschluesselung

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `userPassword` | string | — | Oeffnungs-Passwort |
| `ownerPassword` | string | — | Voll-Zugriff-Passwort |
| `allowPrinting` | boolean | `true` | Drucken |
| `allowCopying` | boolean | `true` | Kopieren |
| `allowModifying` | boolean | `true` | Bearbeiten |
| `allowAnnotating` | boolean | `true` | Annotieren |
| `allowFillingForms` | boolean | `true` | Formulare ausfullen |
| `allowAssembling` | boolean | `true` | Seiten-Assembly |

## Response-Codes

| Code | Bedeutung |
|------|-----------|
| 200 | Erfolg |
| 400 | Ungueltige Felder / Netzwerkfehler |
| 403 | URL verboten (Outbound-Filter) |
| 409 | Status-Code-Fehler / Console-Exception |
| 503 | Timeout |

## Gesamtzahl Form-Felder: ~47

Pflichtfelder (1) + Seitenlayout (10) + Hintergrund (2) + Medien (2) + JS/Warten (3) +
Netzwerk (10) + Header/Footer-Files (2) + Struktur/Metadaten (10) + Split (4) +
Wasserzeichen (12) + PDF/A (2) + Verschluesselung (8) = ~47 Felder

---
Quelle: https://gotenberg.dev/docs/convert-with-chromium/convert-url-to-pdf
