# Gotenberg — PDF Watermark (Full Reference)

## Contents

- [Route](#route)
- [Request Headers](#request-headers)
- [Form Fields](#form-fields)
- [watermarkOptions JSON](#watermarkoptions-json)
- [Response Codes](#response-codes)
- [curl Examples](#curl-examples)
- [Watermark vs. Stamp Comparison](#watermark-vs-stamp-comparison)

## Route

```
POST /forms/pdfengines/watermark
```

**Content-Type of the request:** `multipart/form-data`

Difference from a stamp: a **watermark** is rendered **behind** the page content (background). A stamp is rendered **on top of** the content (foreground).

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
| `files` | file[] | Yes | — | PDF files that receive a watermark |
| `watermarkSource` | enum | Yes | `text`, `image`, `pdf` | Kind of watermark |
| `watermarkExpression` | string | Yes | — | Text string (with source=text) or filename of the uploaded watermark file |
| `watermark` | file | Conditional | — | Image or PDF file used as the watermark (required when source=image or source=pdf) |
| `watermarkPages` | string | No | Page ranges | Pages the watermark is applied to; empty = all |
| `watermarkOptions` | JSON string | No | — | Engine-specific options |

---

## watermarkOptions JSON

The available options depend on the configured PDF engine. Default engine: **pdfcpu**.

### pdfcpu (default)

Full documentation: https://pdfcpu.io/core/watermark

| Option | Type | Example | Description |
|--------|------|---------|-------------|
| `font` | string | `"Helvetica"` | Font family for text watermarks |
| `points` | integer | `48` | Font size in points |
| `color` | string | `"#808080"` | Hex color (gray recommended for watermarks) |
| `rotation` | float | `45` | Rotation angle in degrees |
| `opacity` | float 0-1 | `0.15` | Transparency (typical: 0.1-0.3 for watermarks) |
| `scale` | float | `0.5` | Size scaling |
| `offset` | string | `"0 0"` | Offset X Y in points |
| `pos` | string | `"c"` | Position: `c`=center, `tl`, `tr`, `bl`, `br` |
| `margin` | string | `"20 20"` | Margin |

### Example watermarkOptions (classic watermark)

```json
{
  "font": "Helvetica",
  "points": 48,
  "color": "#808080",
  "rotation": 45,
  "opacity": 0.15
}
```

---

## Response Codes

| Code | Content-Type | Description |
|------|-------------|-------------|
| `200` | variable | PDF with the watermark; multiple inputs → ZIP |
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

### Text watermark "VERTRAULICH" (classic diagonal)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=VERTRAULICH \
  --form 'watermarkOptions={"opacity":0.25,"rotation":45}' \
  -o mit-wasserzeichen.pdf
```

### Text watermark, gray and transparent

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=ENTWURF \
  --form 'watermarkOptions={"font":"Helvetica","points":48,"color":"#808080","rotation":45,"opacity":0.15}' \
  -o entwurf.pdf
```

### Image watermark (logo as background)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermark=@/path/to/logo.png \
  --form watermarkSource=image \
  --form watermarkExpression=logo.png \
  --form 'watermarkOptions={"opacity":0.1,"scale":0.5}' \
  -o mit-logo-wm.pdf
```

### PDF watermark (PDF as an overlay background)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermark=@/path/to/hintergrund.pdf \
  --form watermarkSource=pdf \
  --form watermarkExpression=hintergrund.pdf \
  -o mit-hintergrund.pdf
```

### Watermark on selected pages only

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=KOPIE \
  --form watermarkPages=1-3 \
  --form 'watermarkOptions={"opacity":0.2,"rotation":45}' \
  -o teilweise.pdf
```

---

## Watermark vs. Stamp Comparison

| Property | Watermark (watermark) | Stamp (stamp) |
|----------|----------------------|---------------|
| Position in the PDF | Behind the content (background) | On top of the content (foreground) |
| Typical opacity | 0.1 - 0.3 | 0.5 - 1.0 |
| Typical use | VERTRAULICH notice, draft marking | GENEHMIGT stamp, logo |
| Route | `/forms/pdfengines/watermark` | `/forms/pdfengines/stamp` |

---

Source: https://gotenberg.dev/docs/manipulate-pdfs/watermark-pdfs
