# Gotenberg — PDF Attachments (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [embedsMetadata JSON Format](#embedsmetadata-json-format)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/embed
```

**Content type of the request:** `multipart/form-data`

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | File name of the output |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields

### File Upload

| Field | Type | Required | Description |
|------|-----|---------|--------------|
| `files` | file[] | Yes | PDF files into which content is embedded |
| `embeds` | file[] | Yes | Files to be embedded as attachments (XML, images, etc.) |
| `facturxXml` | file | Conditional | Factur-X CII invoice XML; is embedded as `factur-x.xml` (the file name is ignored) |

### Metadata

| Field | Type | Required | Default | Description |
|------|-----|---------|----------|--------------|
| `embedsMetadata` | JSON string | No | — | Per-attachment metadata, key = file name of the attachment |
| `facturxConformanceLevel` | enum | Conditional* | — | Conformance level for Factur-X XMP metadata (*if facturxXml is provided) |
| `facturxDocumentType` | enum | No | `INVOICE` | Document type for Factur-X XMP metadata |
| `facturxVersion` | string | No | `1.0` | Factur-X version for XMP metadata |

---

## embedsMetadata JSON Format

```json
{
  "rechnung.xml": {
    "mimeType": "text/xml",
    "relationship": "Alternative"
  },
  "logo.png": {
    "mimeType": "image/png",
    "relationship": "Supplement"
  }
}
```

### AFRelationship Values

| Value | Description |
|------|-------------|
| `Source` | Source document (unmodified source) |
| `Data` | Data file (supplementary data) |
| `Alternative` | Alternative format (e.g. XML version of the PDF content) |
| `Supplement` | Supplementary information |
| `Unspecified` | Relationship not defined |

### facturxConformanceLevel Values

| Value | Description |
|------|-------------|
| `MINIMUM` | Minimum conformance |
| `BASIC WL` | Basic without line items |
| `BASIC` | Basic conformance |
| `EN 16931` | European standard (Core Invoice Usage Rules) |
| `EXTENDED` | Extended conformance |
| `XRECHNUNG` | German XRechnung (B2G) |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | `application/pdf` or `application/zip` | PDF with embedded attachments; multiple inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response Headers on Success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl Examples

### Embed XML as an attachment

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form embeds=@/path/to/rechnung.xml \
  -o mit-anhang.pdf
```

### Embed XML with metadata

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form embeds=@/path/to/factur-x.xml \
  --form 'embedsMetadata={"factur-x.xml":{"mimeType":"text/xml","relationship":"Alternative"}}' \
  -o mit-anhang.pdf
```

### Factur-X XML (dedicated field)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/rechnung.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### Embed multiple files

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/dokument.pdf \
  --form embeds=@/path/to/daten.xml \
  --form embeds=@/path/to/logo.png \
  --form 'embedsMetadata={"daten.xml":{"mimeType":"text/xml","relationship":"Data"},"logo.png":{"mimeType":"image/png","relationship":"Supplement"}}' \
  -o dokument-mit-anhaengen.pdf
```

---

## Notes

- Requires QPDF as the PDF engine for full `embedsMetadata` support (default)
- `facturxXml` is always embedded as `factur-x.xml`, regardless of the uploaded file name
- For e-invoices (ZUGFeRD/Factur-X), PDF/A-3b is required — use `POST /forms/pdfengines/factur-x` for the complete workflow
- PDF/A-1b and PDF/A-2b do not support file attachments

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/attachments
