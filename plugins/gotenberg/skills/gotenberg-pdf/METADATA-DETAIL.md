# Gotenberg — Reading & Writing PDF Metadata (Full Reference)

## Contents

- [Routes](#routes)
- [1. Reading Metadata](#1-reading-metadata)
- [2. Writing Metadata](#2-writing-metadata)
- [Notes](#notes)

## Routes

```
POST /forms/pdfengines/metadata/read
POST /forms/pdfengines/metadata/write
```

**Content-Type of the request:** `multipart/form-data`

---

## 1. Reading Metadata

### Route

```
POST /forms/pdfengines/metadata/read
```

### Request Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Form Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `files` | file[] | Yes | PDF files whose metadata is to be read (multiple allowed) |

### Response

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | `application/json; charset=UTF-8` | JSON object with the filename as key and the metadata as value |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response format (example)

```json
{
  "invoice.pdf": {
    "PDFVersion": 1.7,
    "Author": "Gotenberg",
    "Title": "Rechnung #001",
    "CreateDate": "2024:03:05 09:15:32Z",
    "ModifyDate": "2024:03:06 10:00:00Z",
    "PageCount": 2,
    "Producer": "Gotenberg",
    "Creator": "Chromium",
    "MIMEType": "application/pdf",
    "Keywords": "rechnung,2024"
  },
  "report.pdf": {
    "PDFVersion": 1.4,
    "Author": "Max Mustermann",
    "PageCount": 15
  }
}
```

The returned keys correspond to ExifTool tag names.
Reference: https://exiftool.org/TagNames/PDF.html

### curl example

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/read \
  --form files=@/path/to/invoice.pdf \
  --form files=@/path/to/report.pdf
```

---

## 2. Writing Metadata

### Route

```
POST /forms/pdfengines/metadata/write
```

### Request Headers

| Header | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | Filename of the output |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

### Form Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `metadata` | JSON string | Yes | XMP metadata as a JSON object |
| `files` | file[] | Yes | PDF files to be updated; multiple inputs → ZIP |

### Metadata JSON format

```json
{
  "Author": "Max Mustermann",
  "Title": "Jahresbericht 2024",
  "Subject": "Finanzbericht",
  "Producer": "MeinSystem",
  "Creator": "ReportGenerator",
  "Copyright": "2024 Mein Unternehmen",
  "Keywords": ["bericht", "finanzen", "2024"],
  "CreateDate": "2024:01:01 00:00:00Z"
}
```

Supported XMP tags: https://exiftool.org/TagNames/XMP.html#pdf

### Response

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | variable | Updated PDF; multiple inputs → ZIP archive |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### curl examples

#### Setting simple metadata

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/document.pdf \
  --form 'metadata={"Author":"Max Mustermann","Title":"Jahresbericht"}' \
  -o aktualisiert.pdf
```

#### Complete metadata with keywords (array)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/document.pdf \
  --form 'metadata={"Author":"Gotenberg","Producer":"Gotenberg","Keywords":["leitfaden","dokumentation"]}' \
  -o my.pdf
```

#### Updating several PDFs at once (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form 'metadata={"Author":"Muster GmbH","Copyright":"2024"}' \
  -o aktualisiert.zip
```

---

## Notes

- Writing metadata typically breaks PDF/A conformance
- The keys returned when reading correspond to ExifTool tag names (not always identical to the PDF-internal names)
- Uses ExifTool internally for both operations

---

Source:
- https://gotenberg.dev/docs/manipulate-pdfs/read-metadata
- https://gotenberg.dev/docs/manipulate-pdfs/write-metadata
