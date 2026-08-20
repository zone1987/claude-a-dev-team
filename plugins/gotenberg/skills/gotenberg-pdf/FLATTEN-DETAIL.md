# Gotenberg — PDF Flatten (Full Reference)

## Route

```
POST /forms/pdfengines/flatten
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

| Field | Type | Required | Default | Description |
|------|-----|---------|----------|--------------|
| `files` | file[] | Yes | — | PDF files to be flattened |

---

## Function

Flatten converts all interactive form fields (text inputs, checkboxes, dropdowns, radio buttons, signatures, etc.) into static page content. The result is a no-longer-editable PDF that is visually identical to the filled-in form.

**Typical use cases:**
- Archiving filled-in forms
- Fixing signed PDFs for distribution
- Preparing PDFs for PDF/A conversion
- Protecting content against unwanted editing

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | variable | Flattened PDF; multiple inputs → ZIP archive |
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

## curl Examples

### Flatten a single PDF

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --form files=@/path/to/form.pdf \
  -o geflattenet.pdf
```

### Flatten multiple PDFs at once (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --form files=@/path/to/formular1.pdf \
  --form files=@/path/to/formular2.pdf \
  -o geflattenet.zip
```

### With a custom output name

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --header 'Gotenberg-Output-Filename: ausgefuelltes-formular' \
  --form files=@/path/to/form.pdf \
  -o filled-form.pdf
```

---

## Note on the Difference Between Flatten and Encrypt

- **Flatten** turns form fields into static content — visually the same, no longer editable
- **Encrypt** protects the entire PDF with a password and permissions — but fields may still be visible
- For maximum protection: Flatten first, then Encrypt

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/flatten-pdfs
