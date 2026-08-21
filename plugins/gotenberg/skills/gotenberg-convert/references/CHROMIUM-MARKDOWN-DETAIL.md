# Gotenberg — Markdown to PDF (full reference)

**Route:** `POST /forms/chromium/convert/markdown`
**Description:** Converts Markdown (incl. MathJax) to PDF via headless Chromium.
Gotenberg converts the Markdown to HTML and injects it into the supplied template.

## Contents

- [Special feature: template mechanism](#special-feature-template-mechanism)
- [Mandatory files](#mandatory-files)
- [Optional assets](#optional-assets)
- [Request headers](#request-headers)
- [All further form fields](#all-further-form-fields)
- [Full example](#full-example)
- [Total number of form fields: ~46](#total-number-of-form-fields-46)

## Special feature: template mechanism

The `index.html` must contain a Go template directive:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>My PDF</title>
  </head>
  <body>
    {{ toHTML "file.md" }}
  </body>
</html>
```

Multiple Markdown files can be referenced:
```html
{{ toHTML "intro.md" }}
{{ toHTML "chapter1.md" }}
{{ toHTML "chapter2.md" }}
```

## Mandatory files

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `files` (index.html) | file | Yes | HTML template file (must be named `index.html`) |
| `files` (*.md) | file[] | Yes | At least one Markdown file |

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.pdf
```

## Optional assets

```bash
--form files=@/path/to/img.png \
--form files=@/path/to/style.css
```

All files land in a **flat directory** — use file names only.

## Request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Output file name |
| `Gotenberg-Trace` | string | Random UUID | Request ID |

## All further form fields

Identical to `/forms/chromium/convert/html`. Overview:

### Page layout

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `paperWidth` | string | `8.5` | Paper width in inches |
| `paperHeight` | string | `11` | Paper height in inches |
| `marginTop` | string | `0.39` | Top margin |
| `marginBottom` | string | `0.39` | Bottom margin |
| `marginLeft` | string | `0.39` | Left margin |
| `marginRight` | string | `0.39` | Right margin |
| `landscape` | boolean | `false` | Landscape orientation |
| `scale` | number | `1.0` | Zoom factor |
| `singlePage` | boolean | `false` | All content on one page |
| `preferCssPageSize` | boolean | `false` | Prefer CSS `@page` |

### Background

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Include background graphics/colors |
| `omitBackground` | boolean | `false` | Hide the white background |

### Print media

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | `screen` or `print` |
| `emulatedMediaFeatures` | json | — | CSS media feature overrides |

### JavaScript & waiting

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Fixed wait time |
| `waitForExpression` | string | — | JS expression |
| `waitForSelector` | string | — | CSS selector |

### Network

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie array |
| `extraHttpHeaders` | json | — | Additional HTTP headers |
| `userAgent` | string | — | User agent |
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 on status codes |
| `failOnResourceHttpStatusCodes` | json | — | 409 on asset status codes |
| `ignoreResourceHttpStatusDomains` | json | — | Exempt domains |
| `skipNetworkIdleEvent` | boolean | `true` | Do not wait for network idle |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Do not wait for almost-idle |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 on loading error |
| `failOnConsoleExceptions` | boolean | `false` | 409 on JS exceptions |

### Header & footer

| File | Description |
|-------|-------------|
| `header.html` | Page header template |
| `footer.html` | Page footer template |

### Metadata & attachments

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | Bookmarks from headings |
| `generateTaggedPdf` | boolean | `false` | Accessibility tags |
| `metadata` | json | — | XMP metadata |
| `embeds` (files) | file[] | — | Files to embed |
| `embedsMetadata` | json | — | Embed metadata |
| `facturxXml` (file) | file | — | Factur-X XML |
| `facturxConformanceLevel` | enum | — | Conformance level |
| `facturxDocumentType` | enum | `INVOICE` | Document type |
| `facturxVersion` | string | `1.0` | Version |
| `flatten` | boolean | `false` | Flatten form fields |

### Split & page selection

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Page selection (e.g. `1-5`) |
| `splitMode` | enum | — | `intervals` or `pages` |
| `splitSpan` | string | — | Split rule |
| `splitUnify` | boolean | `false` | Merge into one file |

### Watermark & stamp

| Field | Type | Description |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Content/file name |
| `watermarkPages` | string | Page ranges |
| `watermarkOptions` | json | Engine options |
| `watermark` (file) | file | Watermark file |
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Content/file name |
| `stampPages` | string | Page ranges |
| `stampOptions` | json | Engine options |
| `stamp` (file) | file | Stamp file |
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Page ranges |

### PDF/A, PDF/UA, encryption

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | Enable PDF/UA |
| `userPassword` | string | — | Open password |
| `ownerPassword` | string | — | Full-access password |
| `allowPrinting` | boolean | `true` | Printing |
| `allowCopying` | boolean | `true` | Copying |
| `allowModifying` | boolean | `true` | Editing |
| `allowAnnotating` | boolean | `true` | Annotating |
| `allowFillingForms` | boolean | `true` | Filling in forms |
| `allowAssembling` | boolean | `true` | Page assembly |

## Full example

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  --form files=@/path/to/header.html \
  --form files=@/path/to/footer.html \
  --form paperWidth=8.27 \
  --form paperHeight=11.7 \
  --form printBackground=true \
  --form pdfa=PDF/A-2b \
  -o my.pdf
```

## Total number of form fields: ~46

Mandatory files (2+) + page layout (10) + background (2) + media (2) + JS/waiting (3) +
network (10) + header/footer files (2) + metadata/attachments (10) + split (4) +
watermark (12) + PDF/A (2) + encryption (8) = ~46 fields + file inputs

---
Source: https://gotenberg.dev/docs/convert-with-chromium/convert-markdown-to-pdf
