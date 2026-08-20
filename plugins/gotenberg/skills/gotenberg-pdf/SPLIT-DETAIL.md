# Gotenberg — PDF Split (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields (Core)](#form-fields-core)
- [Form Fields (Metadata & Structure)](#form-fields-metadata-structure)
- [Form Fields (Watermark)](#form-fields-watermark)
- [Form Fields (Stamp)](#form-fields-stamp)
- [Form Fields (Rotation)](#form-fields-rotation)
- [Form Fields (Conformance)](#form-fields-conformance)
- [Form Fields (Encryption)](#form-fields-encryption)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/split
```

**Content-Type of the request:** `multipart/form-data`

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | Filename of the output; the extension is appended automatically |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields (Core)

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `files` | file[] | Yes | — | — | PDF files to split |
| `splitMode` | enum | Yes | — | `intervals`, `pages` | Activates the split engine and determines the mode |
| `splitSpan` | string | Yes | — | — | Rule: chunk size for `intervals` (e.g. `2`) or page ranges for `pages` (e.g. `1-3`) |
| `splitUnify` | boolean | No | `false` | `true`, `false` | `pages` mode only: combines the extracted pages into a single PDF |

### splitMode details

**`intervals` mode:**
- `splitSpan=1` → every page becomes its own PDF
- `splitSpan=2` → 2 pages each together
- `splitSpan=3` → 3 pages each together
- Result is always a ZIP archive

**`pages` mode:**
- `splitSpan=1-3` → extract pages 1-3
- `splitSpan=2,4,6` → extract individual pages
- With `splitUnify=true` → a single PDF; without it → ZIP with one PDF per range

---

## Form Fields (Metadata & Structure)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `metadata` | JSON string | No | — | XMP metadata for the output PDFs |
| `embeds` | file[] | No | — | Files that are embedded as attachments |
| `embedsMetadata` | JSON string | No | — | Per-attachment metadata: `mimeType`, `relationship` |
| `facturxXml` | file | No | — | CII invoice XML (embedded as `factur-x.xml`) |
| `facturxConformanceLevel` | enum | Conditional | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | No | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | No | `1.0` | Factur-X version |
| `flatten` | boolean | No | `false` | Convert form fields into page content |

---

## Form Fields (Watermark)

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `watermarkSource` | enum | Conditional | — | `text`, `image`, `pdf` | Kind of watermark |
| `watermarkExpression` | string | Conditional | — | — | Text string or name of an uploaded file |
| `watermarkPages` | string | No | — (all) | Page ranges | Target pages |
| `watermarkOptions` | JSON string | No | — | — | Engine options: `font`, `points`, `color`, `rotation`, `opacity`, `scale`, `offset` |
| `watermark` | file | Conditional | — | — | Image/PDF for source=image/pdf |

---

## Form Fields (Stamp)

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `stampSource` | enum | Conditional | — | `text`, `image`, `pdf` | Kind of stamp |
| `stampExpression` | string | Conditional | — | — | Text string or name of an uploaded file |
| `stampPages` | string | No | — (all) | Page ranges | Target pages |
| `stampOptions` | JSON string | No | — | — | Engine options: `font`, `points`, `color`, `rotation`, `opacity`, `scale`, `offset` |
| `stamp` | file | Conditional | — | — | Image/PDF for source=image/pdf |

---

## Form Fields (Rotation)

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `rotateAngle` | enum | Conditional | — | `90`, `180`, `270` | Rotation angle |
| `rotatePages` | string | No | — (all) | Page ranges | Pages to rotate |

---

## Form Fields (Conformance)

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `pdfa` | enum | No | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Archival standard conversion |
| `pdfua` | boolean | No | `false` | — | Enable PDF/UA accessibility |

---

## Form Fields (Encryption)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `userPassword` | string | No | — | Password for opening |
| `ownerPassword` | string | No | = userPassword | Full-access password |
| `allowPrinting` | boolean | No | `true` | Allow printing |
| `allowCopying` | boolean | No | `true` | Allow copying |
| `allowModifying` | boolean | No | `true` | Allow editing |
| `allowAnnotating` | boolean | No | `true` | Allow annotating |
| `allowFillingForms` | boolean | No | `true` | Allow filling in forms |
| `allowAssembling` | boolean | No | `true` | Allow page management |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | `application/zip` or `application/pdf` | ZIP for multiple outputs; a single PDF when `pages`+`splitUnify=true` |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Maximum processing time exceeded |

---

## curl Examples

### Every page as its own PDF (intervals=1)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/document.pdf \
  --form splitMode=intervals \
  --form splitSpan=1 \
  -o pages.zip
```

### 3 pages each together

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/document.pdf \
  --form splitMode=intervals \
  --form splitSpan=3 \
  -o chunks.zip
```

### Extract pages 1-3 (as a single PDF)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/document.pdf \
  --form splitMode=pages \
  --form splitSpan=1-3 \
  --form splitUnify=true \
  -o auszug.pdf
```

### Extract pages 2, 5 and 7 (separate PDFs in a ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/document.pdf \
  --form splitMode=pages \
  --form 'splitSpan=2,5,7' \
  -o auswahl.zip
```

### Split with encryption

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/document.pdf \
  --form splitMode=intervals \
  --form splitSpan=1 \
  --form userPassword=geheim \
  --form allowCopying=false \
  -o encrypted.zip
```

---

## Notes

- The engine syntax for `splitSpan` depends on the configured PDF engine (pdfcpu, QPDF, PDFtk)
- PDF/A and encryption are mutually exclusive
- PDF/A-1b and PDF/A-2b do not support file attachments; use PDF/A-3b for attachments
- Watermark = behind the content; stamp = on top of the content
- `splitUnify=true` works only in `pages` mode

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/split-pdfs
