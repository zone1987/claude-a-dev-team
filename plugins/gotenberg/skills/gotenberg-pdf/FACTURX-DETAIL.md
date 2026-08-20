# Gotenberg — Factur-X / ZUGFeRD E-Invoice (Full Reference)

## Contents

- [Route](#route)
- [What is Factur-X?](#what-is-factur-x)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [Conformance Level Overview](#conformance-level-overview)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/factur-x
```

**Content type of the request:** `multipart/form-data`

---

## What is Factur-X?

Factur-X (also known as ZUGFeRD in Germany) is a standard for electronic invoices (e-invoicing) that combines a PDF with an embedded machine-readable XML file. The standard is based on CII (Cross Industry Invoice) and is standardized according to EN 16931.

Gotenberg transforms a regular PDF into a conformant e-invoice by:
1. Embedding the CII XML as `factur-x.xml` with `AFRelationship=Alternative`
2. Injecting XMP metadata (conformance level, document type, version)
3. Converting to PDF/A-3 (default: PDF/A-3b)

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
| `files` | file[] | Yes | PDF invoice documents |
| `facturxXml` | file | Yes | CII invoice XML; is embedded as `factur-x.xml` (the uploaded file name is ignored) |

### Factur-X Configuration

| Field | Type | Required | Default | Allowed values | Description |
|------|-----|---------|----------|----------------|--------------|
| `facturxConformanceLevel` | enum | Yes | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` | Conformance level in the XMP metadata |
| `facturxDocumentType` | enum | No | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` | Document type in the XMP metadata |
| `facturxVersion` | string | No | `1.0` | any version string | Factur-X version in the XMP metadata |

### PDF/A Configuration

| Field | Type | Required | Default | Allowed values | Description |
|------|-----|---------|----------|----------------|--------------|
| `pdfa` | enum | No | `PDF/A-3b` | `PDF/A-3a`, `PDF/A-3b`, `PDF/A-3u` | PDF/A-3 variant (only PDF/A-3 allows file attachments) |
| `pdfua` | boolean | No | `false` | `true`, `false` | Enable PDF/UA accessibility |

---

## Conformance Level Overview

| Level | Description | Mandatory fields |
|-------|-------------|---------------|
| `MINIMUM` | Payment information only | Very few |
| `BASIC WL` | Basic without line items | Invoice header |
| `BASIC` | Basic conformance with line items | Standard invoice fields |
| `EN 16931` | European core standard (Core Invoice) | Complete invoice data |
| `EXTENDED` | Extended conformance | + optional fields |
| `XRECHNUNG` | German B2G e-invoice | XRechnung mandatory fields |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | `application/pdf` | PDF/A-3 conformant e-invoice; multiple inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response Headers on Success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: application/pdf
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl Examples

### Standard Factur-X EN 16931

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/invoice.pdf \
  --form facturxXml=@/path/to/cii-invoice.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### XRechnung (mandatory German B2G format)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/invoice.pdf \
  --form facturxXml=@/path/to/xinvoice.xml \
  --form facturxConformanceLevel=XRECHNUNG \
  -o xrechnung.pdf
```

### Minimum conformance (payment information)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/invoice.pdf \
  --form facturxXml=@/path/to/minimum.xml \
  --form facturxConformanceLevel=MINIMUM \
  -o e-rechnung-minimum.pdf
```

### With PDF/A-3a and PDF/UA

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/invoice.pdf \
  --form facturxXml=@/path/to/cii.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  --form pdfa=PDF/A-3a \
  --form pdfua=true \
  -o e-rechnung-accessible.pdf
```

### Purchase order (ORDER document type)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/bestellung.pdf \
  --form facturxXml=@/path/to/bestellung.xml \
  --form facturxConformanceLevel=EXTENDED \
  --form facturxDocumentType=ORDER \
  -o e-bestellung.pdf
```

---

## Notes

- Only PDF/A-3 supports file attachments; PDF/A-1 and PDF/A-2 are not available here
- The file name of the `facturxXml` file is ignored; it is always embedded as `factur-x.xml`
- For simple embedding without automatic PDF/A conversion → use `POST /forms/pdfengines/embed`
- XRechnung conformance is mandatory for German public-sector contracting authorities (B2G) (since 2020)
- ZUGFeRD and Factur-X are interoperable (same technical standard, different branding names)

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/factur-x
