# Gotenberg — Rotating PDF Pages (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/rotate
```

**Content-Type of the request:** `multipart/form-data`

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | Filename of the output |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields

| Field | Type | Required | Default | Allowed values | Description |
|-------|------|----------|---------|----------------|-------------|
| `files` | file[] | Yes | — | — | PDF files to be rotated |
| `rotateAngle` | enum | Yes | — | `90`, `180`, `270` | Rotation angle clockwise (degrees) |
| `rotatePages` | string | No | — (all pages) | Page ranges, e.g. `1-3`, `5`, `2,4,6` | Pages to rotate; empty = all pages |

### rotatePages syntax

| Example | Meaning |
|---------|---------|
| empty / not provided | Rotate all pages |
| `1` | Page 1 only |
| `1-3` | Pages 1 through 3 |
| `2,4,6` | Individual pages 2, 4 and 6 |
| `1-3,5,7-9` | Combination of ranges and individual pages |

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | variable | Rotated PDF; multiple inputs → ZIP archive |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields (e.g. invalid rotateAngle) |
| `503` | `text/plain; charset=UTF-8` | Maximum processing time exceeded |

### Response headers on success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl Examples

### Rotate all pages by 90 degrees

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/document.pdf \
  --form rotateAngle=90 \
  -o rotiert.pdf
```

### Rotate all pages by 180 degrees (turn upside down)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/document.pdf \
  --form rotateAngle=180 \
  -o umgekehrt.pdf
```

### Rotate the first page only

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/document.pdf \
  --form rotateAngle=90 \
  --form rotatePages=1 \
  -o partly-rotated.pdf
```

### Rotate pages 2-4 by 270 degrees

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/document.pdf \
  --form rotateAngle=270 \
  --form rotatePages=2-4 \
  -o partly-rotated.pdf
```

### Fix landscape pages (pages 3, 5, 7)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/document.pdf \
  --form rotateAngle=90 \
  --form 'rotatePages=3,5,7' \
  -o korrigiert.pdf
```

### Rotate several PDFs (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form rotateAngle=90 \
  -o rotiert.zip
```

---

## Notes

- Rotation is performed clockwise
- 270 degrees clockwise = 90 degrees counter-clockwise
- Typical use case: scan corrections, fixing the orientation of landscape pages

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/rotate-pdfs
