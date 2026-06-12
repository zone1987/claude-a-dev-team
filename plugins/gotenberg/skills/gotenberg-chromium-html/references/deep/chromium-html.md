# Gotenberg — HTML zu PDF (Vollreferenz)

**Route:** `POST /forms/chromium/convert/html`
**Beschreibung:** Konvertiert eine `index.html` (mit optionalen Assets) zu PDF via Headless Chromium.

## Request-Grundstruktur

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  -o my.pdf
```

## Pflicht-Files

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `files` (index.html) | file | Ja | HTML-Datei. Muss exakt `index.html` heissen. |

## Optionale Assets

Bilder, Schriften, Stylesheets als weitere `files`-Parameter:
```bash
--form files=@/path/to/img.png \
--form files=@/path/to/style.css
```

**Wichtig:** Alle Dateien landen in einem **flachen Verzeichnis**. Assets nur per Dateiname
referenzieren (z.B. `src="logo.png"`, nicht `src="/images/logo.png"`).

## Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Dateiname der Ausgabe (ohne Extension) |
| `Gotenberg-Trace` | string | Random UUID | Eigene Request-ID fuer Logs |

## Seitenlayout (Page Layout)

| Feld | Typ | Default | Einheit | Beschreibung |
|------|-----|---------|---------|-------------|
| `paperWidth` | string | `8.5` | Zoll | Papierbreite. Einheiten: in, pt, cm |
| `paperHeight` | string | `11` | Zoll | Papierhoehe. Einheiten: in, pt, cm |
| `marginTop` | string | `0.39` | Zoll | Oberer Rand |
| `marginBottom` | string | `0.39` | Zoll | Unterer Rand |
| `marginLeft` | string | `0.39` | Zoll | Linker Rand |
| `marginRight` | string | `0.39` | Zoll | Rechter Rand |
| `landscape` | boolean | `false` | — | Querformat aktivieren |
| `scale` | number | `1.0` | — | Zoom-Faktor |
| `singlePage` | boolean | `false` | — | Gesamten Inhalt auf eine sehr lange Seite zwingen. Ueberschreibt `paperHeight` und `nativePageRanges`. |
| `preferCssPageSize` | boolean | `false` | — | CSS `@page`-Groessen statt API-Parametern verwenden |

### Standardpapierformate (Zoll, Breite x Hoehe)

| Format | Masse | US-Format | Masse |
|--------|-------|-----------|-------|
| A6 | 4.13 x 5.83 | Letter | 8.5 x 11 (Default) |
| A5 | 5.83 x 8.27 | Legal | 8.5 x 14 |
| A4 | 8.27 x 11.7 | Tabloid | 11 x 17 |
| A3 | 11.7 x 16.54 | Ledger | 17 x 11 |
| A2 | 16.54 x 23.4 | | |
| A1 | 23.4 x 33.1 | | |
| A0 | 33.1 x 46.8 | | |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form paperWidth=8.27 \
  --form paperHeight=11.7 \
  --form marginTop=1 \
  --form marginBottom=1 \
  --form marginLeft=1 \
  --form marginRight=1 \
  --form landscape=true \
  --form scale=2.0 \
  -o my.pdf
```

## Hintergrund (Background Logic)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Hintergrundgrafiken/-farben aus HTML einschliessen |
| `omitBackground` | boolean | `false` | Standard-Weisshintergrund ausblenden (erlaubt Transparenz) |

| printBackground | omitBackground | HTML hat BG | Ergebnis |
|----------------|----------------|-------------|---------|
| false | (beliebig) | (beliebig) | Kein Hintergrund |
| true | (beliebig) | Ja | CSS-Hintergrund |
| true | true | Nein | Transparent |
| true | false | Nein | Weiss (Standard) |

## Druckmedien (Print Media)

Chromium verwendet standardmaessig `print`-Medientyp (kein Hintergrund, optimiert fuer Tinte).

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | Medientyp emulieren: `screen` oder `print` |
| `emulatedMediaFeatures` | json | — | JSON-Array mit CSS-Media-Feature-Overrides |

### emulatedMediaFeatures — Haeufige Features

| Feature | Werte | Beschreibung |
|---------|-------|-------------|
| `prefers-color-scheme` | `light`, `dark` | OS-Farbthema emulieren |
| `prefers-reduced-motion` | `no-preference`, `reduce` | Reduzierte Animation |
| `color-gamut` | `srgb`, `p3`, `rec2020` | Farbraum emulieren |
| `forced-colors` | `none`, `active` | Hoher Kontrast |

```bash
--form 'emulatedMediaFeatures=[{"name": "prefers-color-scheme", "value": "dark"}]'
```

## JavaScript & Dynamischer Inhalt

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Feste Wartezeit vor Konvertierung (z.B. `5s`, `500ms`). Fallback-Methode. |
| `waitForExpression` | string | — | JavaScript-Ausdruck; Konvertierung startet wenn `true` |
| `waitForSelector` | string | — | CSS-Selektor; Konvertierung startet wenn Element im DOM erscheint |

```bash
# Warten bis JS-Signal
--form 'waitForExpression=window.status === '"'"'ready'"'"''

# Warten auf DOM-Element
--form 'waitForSelector=#app-ready'
```

## Netzwerk & Cookies

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `cookies` | json | — | JSON-Array von Cookie-Objekten fuer Auth/Session |
| `extraHttpHeaders` | json | — | JSON-Objekt mit zusaetzlichen HTTP-Headern fuer alle Browser-Requests |
| `userAgent` | string | — | User-Agent-Header ueberschreiben |

### Cookie-Felder

| Key | Pflicht | Beschreibung |
|-----|---------|-------------|
| `name` | Ja | Cookie-Name |
| `value` | Ja | Cookie-Wert |
| `domain` | Ja | Domain (z.B. `example.com`) |
| `path` | Nein | URL-Pfad |
| `secure` | Nein | Nur HTTPS senden |
| `httpOnly` | Nein | Nicht per JS zugreifbar |
| `sameSite` | Nein | `Strict`, `Lax` oder `None` |

```bash
--form 'cookies=[{"name":"session","value":"abc123","domain":"example.com"}]'
```

### Header-Scoping

Header koennen auf bestimmte URLs beschraenkt werden (`;scope=<Regex>`):
```bash
--form-string 'extraHttpHeaders={"X-Token":"secret;scope=.*\\.internal\\.api"}'
```

## HTTP-Statuscodes & Netzwerkfehler

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 Conflict wenn Haupt-URL diesen Code zurueckgibt. `X99`-Notation fuer Bereiche (z.B. `499` = 400-499). |
| `failOnResourceHttpStatusCodes` | json | — | 409 Conflict wenn ein Asset diesen Code zurueckgibt |
| `ignoreResourceHttpStatusDomains` | json | — | Domains von `failOnResourceHttpStatusCodes` ausschliessen |
| `skipNetworkIdleEvent` | boolean | `true` | Nicht auf Netzwerk-Idle warten (0 offene Verbindungen fuer 500ms) |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Nicht auf Fast-Idle warten (max. 2 offene Verbindungen fuer 500ms) |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 wenn Assets wegen Netzwerkfehler nicht laden |
| `failOnConsoleExceptions` | boolean | `false` | 409 bei JavaScript-Exceptions in der Chromium-Console |

## Header & Footer

| Dateiname | Pflicht | Beschreibung |
|-----------|---------|-------------|
| `header.html` | Nein | Vollstaendiges HTML-Dokument fuer Seitenkopf |
| `footer.html` | Nein | Vollstaendiges HTML-Dokument fuer Seitenfuss |

Header/Footer werden in separatem Chromium-Kontext gerendert (kein Zugriff auf Haupt-CSS,
kein JavaScript, keine externen Ressourcen).

Automatisch injizierte CSS-Klassen:

| Klasse | Injizierter Wert |
|--------|-----------------|
| `date` | Formatiertes Druckdatum |
| `title` | Dokumenttitel |
| `url` | Dokument-URL |
| `pageNumber` | Aktuelle Seitennummer |
| `totalPages` | Gesamtanzahl Seiten |

Timezone-Override: Env-Var `TZ` setzen.

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form files=@/path/to/header.html \
  --form files=@/path/to/footer.html \
  -o my.pdf
```

## Struktur & Metadaten

### Dokument-Outline (Chromium-nativ)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | PDF-Lesezeichen aus HTML-Ueberschriften (h1-h6) generieren |

### Tagged PDF / Barrierefreiheit (Chromium-nativ)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `generateTaggedPdf` | boolean | `false` | Logische Strukturtags fuer Barrierefreiheit einbetten (waehrend Konvertierung) |

### Metadaten (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `metadata` | json | — | XMP-Metadaten als JSON-Objekt (Author, Title, Copyright, Keywords, ...) |

```bash
--form 'metadata={"Author":"Max Mustermann","Title":"Mein Dokument","Keywords":["pdf","api"]}'
```

### Dateianhange (PDF Engines)

| Feld/Datei | Typ | Default | Beschreibung |
|------------|-----|---------|-------------|
| `embeds` | file[] | — | Dateien die in das PDF eingebettet werden |
| `embedsMetadata` | json | — | Pro-Anhang-Metadaten: `mimeType` und `relationship` |

```bash
--form embeds=@factur-x.xml \
--form 'embedsMetadata={"factur-x.xml":{"mimeType":"text/xml","relationship":"Alternative"}}'
```

### Factur-X / ZUGFeRD (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `facturxXml` | file | — | CII-Rechnungs-XML; wird als `factur-x.xml` eingebettet |
| `facturxConformanceLevel` | enum | — | Konformitaetsstufe: `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | `INVOICE` | Dokumenttyp: `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | `1.0` | Factur-X-Version fuer XMP-Metadaten |

### Flatten (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `flatten` | boolean | `false` | Interaktive Formularfelder in statischen Inhalt umwandeln |

## Seitenauswahl & Split

### Native Seitenauswahl (Chromium)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Zu druckende Seitenbereiche (z.B. `1-5, 8, 11-13`) |

### Split nach Konvertierung (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `splitMode` | enum | — | Split aktivieren: `intervals` oder `pages` |
| `splitSpan` | string | — | Split-Regel. Bei `intervals`: Chunk-Groesse (z.B. `2`). Bei `pages`: Seitenbereiche. |
| `splitUnify` | boolean | `false` | Nur bei `pages`: alle extrahierten Seiten in eine Datei |

Mehrere Dateien bei Split -> ZIP-Archiv als Antwort (ausser `splitUnify=true`).

## Wasserzeichen & Stempel

### Native (HTML/CSS)
Wasserzeichen per CSS `::before`/`::after` direkt im HTML setzen — kein Post-Processing.

### Wasserzeichen (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `watermarkSource` | enum | Quelle: `text`, `image`, `pdf` |
| `watermarkExpression` | string | Inhalt: Text-String oder Dateiname |
| `watermarkPages` | string | Seitenbereiche (leer = alle) |
| `watermarkOptions` | json | Engine-spezifische Optionen (font, color, rotation, opacity, ...) |
| `watermark` (file) | file | Bild/PDF als Wasserzeichen-Quelle |

### Stempel (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `stampSource` | enum | Quelle: `text`, `image`, `pdf` |
| `stampExpression` | string | Inhalt: Text-String oder Dateiname |
| `stampPages` | string | Seitenbereiche (leer = alle) |
| `stampOptions` | json | Engine-spezifische Optionen |
| `stamp` (file) | file | Bild/PDF als Stempel-Quelle |

### Rotation (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `rotateAngle` | enum | Rotationswinkel: `90`, `180`, `270` |
| `rotatePages` | string | Seitenbereiche (leer = alle) |

## PDF/A & PDF/UA

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `pdfa` | enum | — | PDF/A-Standard: `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | PDF/UA (Universal Accessibility) aktivieren |
| `generateTaggedPdf` | boolean | `false` | Struktur-Tags waehrend Chromium-Konvertierung einbetten |

Hinweis: PDF/A und Verschluesselung schliessen sich gegenseitig aus.

## Verschluesselung (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `userPassword` | string | — | Passwort zum Oeffnen des PDF |
| `ownerPassword` | string | — | Passwort fuer vollen Zugriff (hebt Beschraenkungen auf) |
| `allowPrinting` | boolean | `true` | Drucken erlauben |
| `allowCopying` | boolean | `true` | Text/Grafik-Extraktion erlauben |
| `allowModifying` | boolean | `true` | Inhaltsbearbeitung erlauben |
| `allowAnnotating` | boolean | `true` | Annotationen erlauben |
| `allowFillingForms` | boolean | `true` | Formularfelder ausfullen erlauben |
| `allowAssembling` | boolean | `true` | Seiten einfuegen/loeschen/drehen erlauben |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form userPassword=geheim \
  --form allowCopying=false \
  -o my.pdf
```

## Response-Codes

| Code | Bedeutung |
|------|-----------|
| 200 | Erfolg — PDF im Body |
| 400 | Ungueltige Felder oder kritischer Netzwerkfehler |
| 409 | HTTP-Statuscode-Fehler oder Chromium-Exception |
| 503 | Timeout |

## Gesamtzahl Form-Felder: ~44

Seitenlayout (10) + Hintergrund (2) + Medien (2) + JS/Warten (3) + Netzwerk (7) +
Header/Footer-Files (2) + Struktur/Metadaten (8) + Split (3) + Wasserzeichen (5) +
Stempel (5) + Rotation (2) + PDF/A (3) + Verschluesselung (8) = ~44 Felder + Datei-Inputs

---
Quelle: https://gotenberg.dev/docs/convert-with-chromium/convert-html-to-pdf
