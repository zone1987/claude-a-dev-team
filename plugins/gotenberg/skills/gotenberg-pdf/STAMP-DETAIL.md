# Gotenberg — PDF Stamp (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [stampOptions JSON](#stampoptions-json)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Notes](#notes)

## Route

```
POST /forms/pdfengines/stamp
```

**Content-Type of the request:** `multipart/form-data`

Difference from a watermark: a **stamp** is rendered **on top of** the page content (foreground). A watermark is rendered **behind** the content (background).

---

## Request Headers

| Header | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | Filename of the output |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID for log identification |

---

## Form Fields

### Core

| Field | Type | Required | Allowed values | Description |
|-------|------|----------|----------------|-------------|
| `files` | file[] | Yes | — | PDF files to be stamped |
| `stampSource` | enum | Yes | `text`, `image`, `pdf` | Kind of stamp |
| `stampExpression` | string | Yes | — | Text string (with source=text) or filename of the uploaded stamp file |
| `stamp` | file | Conditional | — | Image or PDF file used as the stamp (required when source=image or source=pdf) |
| `stampPages` | string | No | Page ranges | Pages the stamp is applied to; empty = all |
| `stampOptions` | JSON string | No | — | Engine-specific options |

---

## stampOptions JSON

The available options depend on the configured PDF engine. Default engine: **pdfcpu**.

### pdfcpu (default)

Full documentation: https://pdfcpu.io/core/stamp

| Option | Type | Example | Description |
|--------|------|---------|-------------|
| `font` | string | `"Helvetica"` | Font family for text stamps |
| `points` | integer | `48` | Font size in points |
| `color` | string | `"#008000"` | Hex color or CSS color name |
| `rotation` | float | `45` | Rotation angle in degrees |
| `opacity` | float 0-1 | `0.5` | Transparency (0=invisible, 1=fully opaque) |
| `scale` | float | `0.5` | Size scaling |
| `offset` | string | `"10 20"` | Offset X Y in points |
| `pos` | string | `"c"` | Position: `c`=center, `tl`=top-left, `tr`=top-right, `bl`=bottom-left, `br`=bottom-right |
| `margin` | string | `"20 20"` | Margin |
| `mode` | integer | `0` | Stamp mode (engine-specific) |

### Example stampOptions

```json
{
  "font": "Helvetica",
  "points": 36,
  "color": "#FF0000",
  "rotation": 0,
  "opacity": 0.8,
  "pos": "tr",
  "offset": "10 10"
}
```

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | variable | PDF with the stamp; multiple inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response headers on success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl Examples

### Text stamp "GENEHMIGT" (top right)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=GENEHMIGT \
  --form 'stampOptions={"color":"#008000","rotation":0,"opacity":0.8,"pos":"tr"}' \
  -o genehmigt.pdf
```

### Text stamp "VERTRAULICH" (diagonal, semi-opaque)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=VERTRAULICH \
  --form 'stampOptions={"font":"Helvetica","points":48,"color":"#FF0000","rotation":45,"opacity":0.5}' \
  -o vertraulich.pdf
```

### Image stamp (e.g. a logo)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stamp=@/path/to/logo.png \
  --form stampSource=image \
  --form stampExpression=logo.png \
  --form 'stampOptions={"scale":0.3,"pos":"br","opacity":1}' \
  -o mit-logo.pdf
```

### PDF stamp

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stamp=@/path/to/stempel.pdf \
  --form stampSource=pdf \
  --form stampExpression=stempel.pdf \
  -o gestempelt.pdf
```

### Stamp the first page only

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=ORIGINAL \
  --form stampPages=1 \
  -o gestempelt.pdf
```

---

## Notes

- A stamp renders in the **foreground** (on top of the content) — unlike a watermark
- With `stampSource=image` or `stampSource=pdf` the file must also be uploaded in the `stamp` field
- In image/pdf mode, `stampExpression` must match the filename of the `stamp` field
- Engine options are engine-specific; when switching the PDF engine (pdfcpu → PDFtk etc.) the options may differ

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/stamp-pdfs
