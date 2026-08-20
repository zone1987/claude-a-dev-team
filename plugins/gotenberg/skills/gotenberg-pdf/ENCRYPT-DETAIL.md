# Gotenberg — PDF Encryption (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [Response Codes](#response-codes)
- [Engine-Specific Behavior](#engine-specific-behavior)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/encrypt
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

### File Upload

| Field | Type | Required | Description |
|------|-----|---------|--------------|
| `files` | file[] | Yes | PDF files to be encrypted |

### Passwords (at least one required)

| Field | Type | Required | Default | Description |
|------|-----|---------|----------|--------------|
| `userPassword` | string | Conditional* | — | Password required to open the PDF (*at least userPassword or ownerPassword) |
| `ownerPassword` | string | Conditional* | = userPassword | Password for full access; lifts all permission restrictions |

### Permissions (all default to `true`)

| Field | Type | Required | Default | Description |
|------|-----|---------|----------|--------------|
| `allowPrinting` | boolean | No | `true` | Allow printing the document |
| `allowCopying` | boolean | No | `true` | Allow extracting text and graphics |
| `allowModifying` | boolean | No | `true` | Allow modifying content |
| `allowAnnotating` | boolean | No | `true` | Allow adding/changing annotations |
| `allowFillingForms` | boolean | No | `true` | Allow filling in forms |
| `allowAssembling` | boolean | No | `true` | Allow inserting, deleting, rotating pages |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | `application/pdf` or `application/zip` | Encrypted PDF; multiple inputs → ZIP archive |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Maximum processing time exceeded |

### Response Headers on Success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## Engine-Specific Behavior

| Engine | Permission granularity | Particularities |
|--------|----------------------------|----------------|
| **QPDF** (default) | Complete — every permission individually controllable | Recommended for fine-grained control |
| **pdfcpu** | All or nothing — if one permission is denied, all are locked | Simplified model |
| **PDFtk** | No owner-only mode, no individual permissions | Limited support |

**As of v8.34.0:** Owner-only PDFs (ownerPassword only, no userPassword) open without a password but still apply permission restrictions.

---

## curl Examples

### User password only (to open)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/document.pdf \
  --form userPassword=geheimesPasswort \
  -o encrypted.pdf
```

### User and owner password

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/document.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  -o encrypted.pdf
```

### Allow reading only (block copying and editing)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/document.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  --form allowCopying=false \
  --form allowModifying=false \
  --form allowAnnotating=false \
  --form allowFillingForms=false \
  --form allowAssembling=false \
  -o nur-lesen.pdf
```

### Block printing only

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/document.pdf \
  --form userPassword=oeffnen \
  --form allowPrinting=false \
  -o kein-druck.pdf
```

### Owner-only (opens without a password, permissions restricted)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/document.pdf \
  --form ownerPassword=nurFuerAdmin \
  --form allowCopying=false \
  --form allowModifying=false \
  -o berechtigungen.pdf
```

---

## Notes

- Permission restrictions require at least `userPassword` or `ownerPassword`
- PDF/A and encryption are mutually exclusive
- QPDF is recommended when individual permissions are needed
- For a complete read lock, the following is recommended: Flatten → Encrypt

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/encrypt-pdfs
