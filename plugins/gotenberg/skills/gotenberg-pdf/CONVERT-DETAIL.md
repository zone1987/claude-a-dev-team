# Gotenberg — PDF/A & PDF/UA Conversion (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [PDF/A Standard Overview](#pdfa-standard-overview)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/convert
```

**Content type of the request:** `multipart/form-data`

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | File name of the output; the extension is appended automatically |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields

| Field | Type | Required | Default | Allowed values | Description |
|------|-----|---------|----------|----------------|--------------|
| `files` | file[] | Yes | — | — | PDF files to be converted |
| `pdfa` | enum | Conditional* | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Target archival standard (*at least one of pdfa or pdfua is required) |
| `pdfua` | boolean | Conditional* | `false` | `true`, `false` | Enable PDF/UA (Universal Accessibility) |

---

## PDF/A Standard Overview

| Standard | Description | Attachments allowed |
|----------|-------------|-----------------|
| `PDF/A-1b` | ISO 19005-1 — preserves visual appearance | No |
| `PDF/A-2b` | ISO 19005-2 — improved compression | No |
| `PDF/A-3b` | ISO 19005-3 — arbitrary file attachments allowed | Yes |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | `application/pdf` | Converted PDF; multiple inputs → ZIP archive |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Maximum processing time exceeded |

All responses include: `Content-Disposition`, `Content-Type`, `Content-Length`, `Gotenberg-Trace`

---

## curl Examples

### Convert to PDF/A-1b

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-1b \
  -o archiv.pdf
```

### Convert to PDF/A-2b

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-2b \
  -o archiv.pdf
```

### Convert to PDF/A-3b (with attachment support)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-3b \
  -o archiv.pdf
```

### Enable PDF/UA accessibility

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfua=true \
  -o barrierefrei.pdf
```

### Combining PDF/A-3b + PDF/UA

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-3b \
  --form pdfua=true \
  -o archiv-barrierefrei.pdf
```

### Multiple files at once (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form pdfa=PDF/A-2b \
  -o konvertiert.zip
```

---

## Notes

- This operation requires LibreOffice to reprocess the documents — more compute-intensive than merge/split
- PDF/A and encryption are mutually exclusive (encryption breaks PDF/A conformance)
- Writing metadata typically breaks PDF/A conformance
- For e-invoices with an attachment, PDF/A-3b is required (ZUGFeRD/Factur-X)
- Conversion can take considerably longer for complex documents

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/pdfa-pdfua
