# Gotenberg — LibreOffice conversion (full reference)

**Route:** `POST /forms/libreoffice/convert`
**Description:** Converts documents to PDF via LibreOffice (unoconv).
Accepts Microsoft Office, OpenDocument, plaintext and many further formats.

## Contents

- [Basic example](#basic-example)
- [Request headers](#request-headers)
- [Mandatory field](#mandatory-field)
- [Layout fields (LibreOffice phase)](#layout-fields-libreoffice-phase)
- [Supported file formats](#supported-file-formats)
- [PDF engine fields (post-processing)](#pdf-engine-fields-post-processing)
- [Note: LibreOffice vs. Microsoft Office](#note-libreoffice-vs-microsoft-office)
- [Changing the language](#changing-the-language)
- [Response codes](#response-codes)
- [Total number of form fields: ~38](#total-number-of-form-fields-38)

## Basic example

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  -o my.pdf
```

Multiple files: the response is a **ZIP archive**.

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/doc1.docx \
  --form files=@/path/to/doc2.xlsx \
  -o archive.zip
```

## Request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Output file name (without extension) |
| `Gotenberg-Trace` | string | Random UUID | Request ID for logs |

## Mandatory field

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `files` | file[] | Yes | One or more files. Multiple files -> ZIP archive. |

## Layout fields (LibreOffice phase)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `landscape` | boolean | `false` | Enable landscape orientation |
| `singlePageSheets` | boolean | `false` | Put every sheet (including hidden ones) on exactly one page. Ignores individual sheet sizes and print ranges. |
| `skipEmptyPages` | boolean | `false` | Suppress automatically inserted blank pages (Writer documents only) |
| `exportPlaceholders` | boolean | `false` | Export placeholder fields as visual markers (not functional) |

```bash
curl \
  --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  --form landscape=true \
  -o my.pdf
```

## Supported file formats

### Word processing

`.doc`, `.docx`, `.docm`, `.dot`, `.dotm`, `.dotx`, `.odt`, `.fodt`, `.ott`,
`.rtf`, `.txt`, `.wps`, `.wpd`, `.pages`, `.abw`, `.zabw`, `.lwp`, `.mw`, `.mcw`,
`.hwp`, `.sxw`, `.stw`, `.sgl`, `.vor`, `.602`, `.bib`, `.xml`, `.cwk`, `.psw`, `.uof`

### Spreadsheets

`.xls`, `.xlsx`, `.xlsm`, `.xlsb`, `.xlt`, `.xltm`, `.xltx`, `.xlw`, `.ods`, `.fods`,
`.ots`, `.csv`, `.numbers`, `.123`, `.wk1`, `.wks`, `.wb2`, `.dbf`, `.dif`, `.slk`,
`.sxc`, `.stc`, `.uos`, `.pxl`, `.sdc`

### Presentations

`.ppt`, `.pptx`, `.pptm`, `.pot`, `.potm`, `.potx`, `.pps`, `.odp`, `.fodp`, `.otp`,
`.key`, `.sxi`, `.sti`, `.uop`, `.sdd`, `.sdp`, `.fopd`

### Graphics & drawing

`.odg`, `.fodg`, `.otg`, `.vsd`, `.vsdx`, `.vsdm`, `.vdx`, `.cdr`, `.svg`, `.svm`,
`.wmf`, `.emf`, `.cgm`, `.dxf`, `.std`, `.sxd`, `.pub`, `.wpg`, `.sda`, `.odd`,
`.met`, `.cmx`, `.eps`

### Images

`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tif`, `.tiff`, `.pbm`, `.pgm`, `.ppm`,
`.xbm`, `.xpm`, `.pcx`, `.pcd`, `.pct`, `.psd`, `.tga`, `.ras`, `.pwp`

### Web & miscellaneous

`.html`, `.htm`, `.xhtml`, `.epub`, `.pdf`, `.pdb`, `.ltx`, `.mml`, `.smf`, `.sxm`,
`.sxg`, `.oth`, `.odm`, `.swf`

## PDF engine fields (post-processing)

Identical to the Chromium conversion routes. All fields listed below can be
combined with the LibreOffice fields in the same request.

### Metadata (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `metadata` | json | — | XMP metadata (Author, Title, Keywords, ...) |

### File attachments (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `embeds` (files) | file[] | — | Files to embed |
| `embedsMetadata` | json | — | Per-attachment metadata: `mimeType` and `relationship` |

### Factur-X / ZUGFeRD (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `facturxXml` (file) | file | — | Factur-X CII XML |
| `facturxConformanceLevel` | enum | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | `1.0` | Factur-X version |

### Flatten (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `flatten` | boolean | `false` | Form fields into static content |

### Split (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `splitMode` | enum | — | `intervals` or `pages` |
| `splitSpan` | string | — | Split rule |
| `splitUnify` | boolean | `false` | All extracted pages into one file |

### Watermark (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Content or file name |
| `watermarkPages` | string | Page ranges |
| `watermarkOptions` | json | Engine options |
| `watermark` (file) | file | Watermark file |

### Stamp (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Content or file name |
| `stampPages` | string | Page ranges |
| `stampOptions` | json | Engine options |
| `stamp` (file) | file | Stamp file |

### Rotation (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Page ranges |

### PDF/A & PDF/UA (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | Enable PDF/UA |

### Encryption (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `userPassword` | string | — | Open password |
| `ownerPassword` | string | — | Full-access password |
| `allowPrinting` | boolean | `true` | Printing |
| `allowCopying` | boolean | `true` | Copying |
| `allowModifying` | boolean | `true` | Editing |
| `allowAnnotating` | boolean | `true` | Annotating |
| `allowFillingForms` | boolean | `true` | Filling in forms |
| `allowAssembling` | boolean | `true` | Page assembly |

## Note: LibreOffice vs. Microsoft Office

LibreOffice is not a 1:1 clone of Microsoft Office. Documents with complex styling,
SmartArt or very specific formatting may render slightly differently.

**Fonts**: Missing fonts are the most common cause of layout problems.
Use the fonts included in the Docker image or bundle your own fonts.

## Changing the language

By default LibreOffice uses English. Build your own image:

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

## Response codes

| Code | Meaning |
|------|-----------|
| 200 | Success — PDF or ZIP in the body |
| 400 | Invalid fields |
| 503 | Timeout |

## Total number of form fields: ~38

LibreOffice-specific (4) + metadata (1) + attachments (2) + Factur-X (4) +
flatten (1) + split (3) + watermark (5) + stamp (5) + rotation (2) +
PDF/A (2) + encryption (8) = ~37 fields + file inputs

---
Source: https://gotenberg.dev/docs/convert-with-libreoffice/convert-to-pdf
