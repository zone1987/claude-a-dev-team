# Gotenberg — PDF Merge (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/merge
```

**Content-Type of the request:** `multipart/form-data`

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | Filename of the output; the extension is appended automatically |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields

### Core

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `files` | file[] | Yes | — | PDF files to merge; they are merged in alphanumeric order of their filenames |

### Metadata

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `metadata` | JSON string | No | — | XMP metadata as a JSON object (e.g. `{"Author":"Max","Title":"Rechnung"}`) |

### Bookmarks

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `bookmarks` | JSON string | No | — | Bookmarks as a list or filename map |
| `autoIndexBookmarks` | boolean | No | `false` | Extracts existing bookmarks and shifts their page offsets automatically |

### Attachments (Embeds)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `embeds` | file[] | No | — | Files that are embedded as attachments in the PDF container |
| `embedsMetadata` | JSON string | No | — | Per-attachment metadata, key = filename; fields: `mimeType`, `relationship` (`Source`, `Data`, `Alternative`, `Supplement`, `Unspecified`) |

### Factur-X

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `facturxXml` | file | No | — | — | CII invoice XML; is embedded as `factur-x.xml` |
| `facturxConformanceLevel` | enum | Conditional* | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` | Conformance level in the XMP metadata (*if facturxXml is provided) |
| `facturxDocumentType` | enum | No | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` | Document type in the XMP metadata |
| `facturxVersion` | string | No | `1.0` | — | Factur-X version in the XMP metadata |

### Flatten

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `flatten` | boolean | No | `false` | Converts form fields into static page content |

### Watermark

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `watermarkSource` | enum | Conditional | — | `text`, `image`, `pdf` | Kind of watermark |
| `watermarkExpression` | string | Conditional | — | — | Text string or name of an uploaded file |
| `watermarkPages` | string | No | — (all) | Page ranges, e.g. `1-3,5` | Pages the watermark is applied to |
| `watermarkOptions` | JSON string | No | — | — | Engine options (font, color, rotation, opacity, scale, offset) |
| `watermark` | file | Conditional | — | — | Image/PDF file (for source=image or pdf) |

### Stamp

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `stampSource` | enum | Conditional | — | `text`, `image`, `pdf` | Kind of stamp |
| `stampExpression` | string | Conditional | — | — | Text string or name of an uploaded file |
| `stampPages` | string | No | — (all) | Page ranges, e.g. `1-3,5` | Pages the stamp is applied to |
| `stampOptions` | JSON string | No | — | — | Engine options (font, color, rotation, opacity, scale, offset) |
| `stamp` | file | Conditional | — | — | Image/PDF file (for source=image or pdf) |

### Rotation

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `rotateAngle` | enum | Conditional | — | `90`, `180`, `270` | Rotation angle in degrees |
| `rotatePages` | string | No | — (all) | Page ranges | Pages that are rotated |

### PDF/A & PDF/UA

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `pdfa` | enum | No | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Conversion to an archival standard |
| `pdfua` | boolean | No | `false` | — | Enable accessibility (Universal Accessibility) |

### Encryption

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `userPassword` | string | No | — | Password for opening the PDF |
| `ownerPassword` | string | No | = userPassword | Full-access password; lifts permission restrictions |
| `allowPrinting` | boolean | No | `true` | Allow printing |
| `allowCopying` | boolean | No | `true` | Allow text and graphics extraction |
| `allowModifying` | boolean | No | `true` | Allow content changes |
| `allowAnnotating` | boolean | No | `true` | Allow annotations |
| `allowFillingForms` | boolean | No | `true` | Allow form filling |
| `allowAssembling` | boolean | No | `true` | Allow inserting/deleting/rotating pages |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | `application/pdf` | Merged PDF; headers: `Content-Disposition`, `Content-Type`, `Content-Length`, `Gotenberg-Trace` |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields; detail in the body + `Gotenberg-Trace` |
| `503` | `text/plain; charset=UTF-8` | Maximum processing time exceeded |

---

## curl Examples

### Simple merge (alphanumeric order)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/01_deckblatt.pdf \
  --form files=@/path/to/02_inhalt.pdf \
  --form files=@/path/to/03_anhang.pdf \
  -o zusammengefuehrt.pdf
```

### With metadata

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form 'metadata={"Author":"Max Mustermann","Title":"Jahresbericht 2024","Keywords":["bericht","2024"]}' \
  -o mein.pdf
```

### With encryption

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  --form allowCopying=false \
  --form allowModifying=false \
  -o verschluesselt.pdf
```

### With a watermark (text)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=VERTRAULICH \
  --form 'watermarkOptions={"opacity":0.25,"rotation":45,"color":"#808080"}' \
  -o mit-wasserzeichen.pdf
```

### With Factur-X

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/rechnung.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### With PDF/A conversion + auto bookmarks

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form pdfa=PDF/A-3b \
  --form autoIndexBookmarks=true \
  -o archiv.pdf
```

### With a custom output filename and trace

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Output-Filename: jahresbericht-2024' \
  --header 'Gotenberg-Trace: mein-trace-123' \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  -o jahresbericht-2024.pdf
```

---

## Notes

- The files are merged in **alphanumeric order** of their filenames — name the files accordingly (01_, 02_, ...)
- `autoIndexBookmarks=true` extracts existing bookmarks and adjusts the page offsets
- PDF/A and encryption are mutually exclusive
- PDF/A-1b and PDF/A-2b do not support file attachments; use PDF/A-3b for attachments
- Watermark = behind the content; stamp = on top of the content

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/merge-pdfs
