# Gotenberg — LibreOffice-Konvertierung (Vollreferenz)

**Route:** `POST /forms/libreoffice/convert`
**Beschreibung:** Konvertiert Dokumente zu PDF via LibreOffice (unoconv).
Akzeptiert Microsoft Office, OpenDocument, Plaintext und viele weitere Formate.

## Basisbeispiel

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  -o my.pdf
```

Mehrere Dateien: Antwort ist ein **ZIP-Archiv**.

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/doc1.docx \
  --form files=@/path/to/doc2.xlsx \
  -o archive.zip
```

## Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Ausgabe-Dateiname (ohne Extension) |
| `Gotenberg-Trace` | string | Random UUID | Request-ID fuer Logs |

## Pflichtfeld

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `files` | file[] | Ja | Eine oder mehrere Dateien. Mehrere Dateien -> ZIP-Archiv. |

## Layout-Felder (LibreOffice-Phase)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `landscape` | boolean | `false` | Querformat aktivieren |
| `singlePageSheets` | boolean | `false` | Jedes Tabellenblatt (auch versteckte) auf genau eine Seite. Ignoriert individuelle Blatt-Groessen und Druckbereiche. |
| `skipEmptyPages` | boolean | `false` | Automatisch eingefuegte Leerseiten unterdruecken (nur Writer-Dokumente) |
| `exportPlaceholders` | boolean | `false` | Platzhalterfelder als visuelle Markierungen exportieren (nicht funktional) |

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  --form landscape=true \
  -o my.pdf
```

## Unterstuetzte Dateiformate

### Word Processing (Textverarbeitung)

`.doc`, `.docx`, `.docm`, `.dot`, `.dotm`, `.dotx`, `.odt`, `.fodt`, `.ott`,
`.rtf`, `.txt`, `.wps`, `.wpd`, `.pages`, `.abw`, `.zabw`, `.lwp`, `.mw`, `.mcw`,
`.hwp`, `.sxw`, `.stw`, `.sgl`, `.vor`, `.602`, `.bib`, `.xml`, `.cwk`, `.psw`, `.uof`

### Tabellenkalkulation (Spreadsheets)

`.xls`, `.xlsx`, `.xlsm`, `.xlsb`, `.xlt`, `.xltm`, `.xltx`, `.xlw`, `.ods`, `.fods`,
`.ots`, `.csv`, `.numbers`, `.123`, `.wk1`, `.wks`, `.wb2`, `.dbf`, `.dif`, `.slk`,
`.sxc`, `.stc`, `.uos`, `.pxl`, `.sdc`

### Praesentationen

`.ppt`, `.pptx`, `.pptm`, `.pot`, `.potm`, `.potx`, `.pps`, `.odp`, `.fodp`, `.otp`,
`.key`, `.sxi`, `.sti`, `.uop`, `.sdd`, `.sdp`, `.fopd`

### Grafik & Zeichnung

`.odg`, `.fodg`, `.otg`, `.vsd`, `.vsdx`, `.vsdm`, `.vdx`, `.cdr`, `.svg`, `.svm`,
`.wmf`, `.emf`, `.cgm`, `.dxf`, `.std`, `.sxd`, `.pub`, `.wpg`, `.sda`, `.odd`,
`.met`, `.cmx`, `.eps`

### Bilder

`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tif`, `.tiff`, `.pbm`, `.pgm`, `.ppm`,
`.xbm`, `.xpm`, `.pcx`, `.pcd`, `.pct`, `.psd`, `.tga`, `.ras`, `.pwp`

### Web & Sonstiges

`.html`, `.htm`, `.xhtml`, `.epub`, `.pdf`, `.pdb`, `.ltx`, `.mml`, `.smf`, `.sxm`,
`.sxg`, `.oth`, `.odm`, `.swf`

## PDF-Engine-Felder (Post-Processing)

Identisch mit Chromium-Konvertierungsrouten. Alle unten genannten Felder koennen
im selben Request mit den LibreOffice-Feldern kombiniert werden.

### Metadaten (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `metadata` | json | — | XMP-Metadaten (Author, Title, Keywords, ...) |

### Dateianhange (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `embeds` (files) | file[] | — | Einzubettende Dateien |
| `embedsMetadata` | json | — | Pro-Anhang-Metadaten: `mimeType` und `relationship` |

### Factur-X / ZUGFeRD (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `facturxXml` (file) | file | — | Factur-X CII-XML |
| `facturxConformanceLevel` | enum | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | `1.0` | Factur-X-Version |

### Flatten (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `flatten` | boolean | `false` | Formularfelder in statischen Inhalt |

### Split (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `splitMode` | enum | — | `intervals` oder `pages` |
| `splitSpan` | string | — | Split-Regel |
| `splitUnify` | boolean | `false` | Alle extrahierten Seiten in eine Datei |

### Wasserzeichen (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Inhalt oder Dateiname |
| `watermarkPages` | string | Seitenbereiche |
| `watermarkOptions` | json | Engine-Optionen |
| `watermark` (file) | file | Wasserzeichen-Datei |

### Stempel (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Inhalt oder Dateiname |
| `stampPages` | string | Seitenbereiche |
| `stampOptions` | json | Engine-Optionen |
| `stamp` (file) | file | Stempel-Datei |

### Rotation (PDF Engines)

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Seitenbereiche |

### PDF/A & PDF/UA (PDF Engines)

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | PDF/UA aktivieren |

### Verschluesselung (PDF Engines)

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

## Hinweis: LibreOffice vs. Microsoft Office

LibreOffice ist kein 1:1-Klon von Microsoft Office. Dokumente mit komplexem Styling,
SmartArt oder sehr spezifischer Formatierung koennen leicht anders gerendert werden.

**Schriften**: Fehlende Schriften sind die haeufigste Ursache fuer Layout-Probleme.
Die im Docker-Image enthaltenen Schriften verwenden oder eigene Schriften einbinden.

## Sprache aendern

Standardmaessig verwendet LibreOffice Englisch. Eigenes Image bauen:

```dockerfile
FROM gotenberg/gotenberg:8
USER root
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
      -t trixie-backports libreoffice-l10n-de && \
    sed -i '/de_DE.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8
USER gotenberg
```

## Response-Codes

| Code | Bedeutung |
|------|-----------|
| 200 | Erfolg — PDF oder ZIP im Body |
| 400 | Ungueltige Felder |
| 503 | Timeout |

## Gesamtzahl Form-Felder: ~38

LibreOffice-spezifisch (4) + Metadaten (1) + Anhange (2) + Factur-X (4) +
Flatten (1) + Split (3) + Wasserzeichen (5) + Stempel (5) + Rotation (2) +
PDF/A (2) + Verschluesselung (8) = ~37 Felder + Datei-Inputs

---
Quelle: https://gotenberg.dev/docs/convert-with-libreoffice/convert-to-pdf
