# Gotenberg — HTML to PDF (full reference)

**Route:** `POST /forms/chromium/convert/html`
**Description:** Converts an `index.html` (with optional assets) to PDF via headless Chromium.

## Contents

- [Basic request structure](#basic-request-structure)
- [Mandatory files](#mandatory-files)
- [Optional assets](#optional-assets)
- [Request headers](#request-headers)
- [Page layout](#page-layout)
- [Background logic](#background-logic)
- [Print media](#print-media)
- [JavaScript & dynamic content](#javascript--dynamic-content)
- [Network & cookies](#network--cookies)
- [HTTP status codes & network errors](#http-status-codes--network-errors)
- [Header & footer](#header--footer)
- [Structure & metadata](#structure--metadata)
- [Page selection & split](#page-selection--split)
- [Watermark & stamp](#watermark--stamp)
- [PDF/A & PDF/UA](#pdfa--pdfua)
- [Encryption (PDF Engines)](#encryption-pdf-engines)
- [Response codes](#response-codes)
- [Total number of form fields: ~44](#total-number-of-form-fields-44)

## Basic request structure

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  -o my.pdf
```

## Mandatory files

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `files` (index.html) | file | Yes | HTML file. Must be named exactly `index.html`. |

## Optional assets

Images, fonts, stylesheets as further `files` parameters:
```bash
--form files=@/path/to/img.png \
--form files=@/path/to/style.css
```

**Important:** All files land in a **flat directory**. Reference assets by file name only
(e.g. `src="logo.png"`, not `src="/images/logo.png"`).

## Request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | File name of the output (without extension) |
| `Gotenberg-Trace` | string | Random UUID | Custom request ID for logs |

## Page layout

| Field | Type | Default | Unit | Description |
|------|-----|---------|---------|-------------|
| `paperWidth` | string | `8.5` | inches | Paper width. Units: in, pt, cm |
| `paperHeight` | string | `11` | inches | Paper height. Units: in, pt, cm |
| `marginTop` | string | `0.39` | inches | Top margin |
| `marginBottom` | string | `0.39` | inches | Bottom margin |
| `marginLeft` | string | `0.39` | inches | Left margin |
| `marginRight` | string | `0.39` | inches | Right margin |
| `landscape` | boolean | `false` | — | Enable landscape orientation |
| `scale` | number | `1.0` | — | Zoom factor |
| `singlePage` | boolean | `false` | — | Force all content onto one very long page. Overrides `paperHeight` and `nativePageRanges`. |
| `preferCssPageSize` | boolean | `false` | — | Use CSS `@page` sizes instead of the API parameters |

### Standard paper formats (inches, width x height)

| Format | Dimensions | US format | Dimensions |
|--------|-------|-----------|-------|
| A6 | 4.13 x 5.83 | Letter | 8.5 x 11 (default) |
| A5 | 5.83 x 8.27 | Legal | 8.5 x 14 |
| A4 | 8.27 x 11.7 | Tabloid | 11 x 17 |
| A3 | 11.7 x 16.54 | Ledger | 17 x 11 |
| A2 | 16.54 x 23.4 | | |
| A1 | 23.4 x 33.1 | | |
| A0 | 33.1 x 46.8 | | |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form paperWidth=8.27 \
  --form paperHeight=11.7 \
  --form marginTop=1 \
  --form marginBottom=1 \
  --form marginLeft=1 \
  --form marginRight=1 \
  --form landscape=true \
  --form scale=2.0 \
  -o my.pdf
```

## Background logic

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Include background graphics/colors from the HTML |
| `omitBackground` | boolean | `false` | Hide the default white background (allows transparency) |

| printBackground | omitBackground | HTML has BG | Result |
|----------------|----------------|-------------|---------|
| false | (any) | (any) | No background |
| true | (any) | Yes | CSS background |
| true | true | No | Transparent |
| true | false | No | White (default) |

## Print media

Chromium uses the `print` media type by default (no background, optimized for ink).

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | Emulate media type: `screen` or `print` |
| `emulatedMediaFeatures` | json | — | JSON array of CSS media feature overrides |

### emulatedMediaFeatures — common features

| Feature | Values | Description |
|---------|-------|-------------|
| `prefers-color-scheme` | `light`, `dark` | Emulate the OS color theme |
| `prefers-reduced-motion` | `no-preference`, `reduce` | Reduced animation |
| `color-gamut` | `srgb`, `p3`, `rec2020` | Emulate color space |
| `forced-colors` | `none`, `active` | High contrast |

```bash
--form 'emulatedMediaFeatures=[{"name": "prefers-color-scheme", "value": "dark"}]'
```

## JavaScript & dynamic content

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Fixed wait time before conversion (e.g. `5s`, `500ms`). Fallback method. |
| `waitForExpression` | string | — | JavaScript expression; conversion starts when it is `true` |
| `waitForSelector` | string | — | CSS selector; conversion starts when the element appears in the DOM |

```bash
# Wait for a JS signal
--form 'waitForExpression=window.status === '"'"'ready'"'"''

# Wait for a DOM element
--form 'waitForSelector=#app-ready'
```

## Network & cookies

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `cookies` | json | — | JSON array of cookie objects for auth/session |
| `extraHttpHeaders` | json | — | JSON object with additional HTTP headers for all browser requests |
| `userAgent` | string | — | Override the User-Agent header |

### Cookie fields

| Key | Required | Description |
|-----|---------|-------------|
| `name` | Yes | Cookie name |
| `value` | Yes | Cookie value |
| `domain` | Yes | Domain (e.g. `example.com`) |
| `path` | No | URL path |
| `secure` | No | Send over HTTPS only |
| `httpOnly` | No | Not accessible via JS |
| `sameSite` | No | `Strict`, `Lax` or `None` |

```bash
--form 'cookies=[{"name":"session","value":"abc123","domain":"example.com"}]'
```

### Header scoping

Headers can be restricted to specific URLs (`;scope=<regex>`):
```bash
--form-string 'extraHttpHeaders={"X-Token":"secret;scope=.*\\.internal\\.api"}'
```

## HTTP status codes & network errors

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 Conflict when the main URL returns this code. `X99` notation for ranges (e.g. `499` = 400-499). |
| `failOnResourceHttpStatusCodes` | json | — | 409 Conflict when an asset returns this code |
| `ignoreResourceHttpStatusDomains` | json | — | Exclude domains from `failOnResourceHttpStatusCodes` |
| `skipNetworkIdleEvent` | boolean | `true` | Do not wait for network idle (0 open connections for 500ms) |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Do not wait for almost-idle (max. 2 open connections for 500ms) |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 when assets fail to load because of a network error |
| `failOnConsoleExceptions` | boolean | `false` | 409 on JavaScript exceptions in the Chromium console |

## Header & footer

| File name | Required | Description |
|-----------|---------|-------------|
| `header.html` | No | Complete HTML document for the page header |
| `footer.html` | No | Complete HTML document for the page footer |

Header/footer are rendered in a separate Chromium context (no access to the main CSS,
no JavaScript, no external resources).

Automatically injected CSS classes:

| Class | Injected value |
|--------|-----------------|
| `date` | Formatted print date |
| `title` | Document title |
| `url` | Document URL |
| `pageNumber` | Current page number |
| `totalPages` | Total number of pages |

Timezone override: set the `TZ` env var.

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form files=@/path/to/header.html \
  --form files=@/path/to/footer.html \
  -o my.pdf
```

## Structure & metadata

### Document outline (Chromium-native)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | Generate PDF bookmarks from HTML headings (h1-h6) |

### Tagged PDF / accessibility (Chromium-native)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `generateTaggedPdf` | boolean | `false` | Embed logical structure tags for accessibility (during conversion) |

### Metadata (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `metadata` | json | — | XMP metadata as a JSON object (Author, Title, Copyright, Keywords, ...) |

```bash
--form 'metadata={"Author":"Max Mustermann","Title":"My document","Keywords":["pdf","api"]}'
```

### File attachments (PDF Engines)

| Field/file | Type | Default | Description |
|------------|-----|---------|-------------|
| `embeds` | file[] | — | Files that get embedded into the PDF |
| `embedsMetadata` | json | — | Per-attachment metadata: `mimeType` and `relationship` |

```bash
--form embeds=@factur-x.xml \
--form 'embedsMetadata={"factur-x.xml":{"mimeType":"text/xml","relationship":"Alternative"}}'
```

### Factur-X / ZUGFeRD (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `facturxXml` | file | — | CII invoice XML; embedded as `factur-x.xml` |
| `facturxConformanceLevel` | enum | — | Conformance level: `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | `INVOICE` | Document type: `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | `1.0` | Factur-X version for the XMP metadata |

### Flatten (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `flatten` | boolean | `false` | Convert interactive form fields into static content |

## Page selection & split

### Native page selection (Chromium)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Page ranges to print (e.g. `1-5, 8, 11-13`) |

### Split after conversion (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `splitMode` | enum | — | Enable split: `intervals` or `pages` |
| `splitSpan` | string | — | Split rule. With `intervals`: chunk size (e.g. `2`). With `pages`: page ranges. |
| `splitUnify` | boolean | `false` | Only with `pages`: put all extracted pages into one file |

Multiple files on split -> ZIP archive as the response (except with `splitUnify=true`).

## Watermark & stamp

### Native (HTML/CSS)
Set watermarks via CSS `::before`/`::after` directly in the HTML — no post-processing.

### Watermark (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `watermarkSource` | enum | Source: `text`, `image`, `pdf` |
| `watermarkExpression` | string | Content: text string or file name |
| `watermarkPages` | string | Page ranges (empty = all) |
| `watermarkOptions` | json | Engine-specific options (font, color, rotation, opacity, ...) |
| `watermark` (file) | file | Image/PDF as the watermark source |

### Stamp (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `stampSource` | enum | Source: `text`, `image`, `pdf` |
| `stampExpression` | string | Content: text string or file name |
| `stampPages` | string | Page ranges (empty = all) |
| `stampOptions` | json | Engine-specific options |
| `stamp` (file) | file | Image/PDF as the stamp source |

### Rotation (PDF Engines)

| Field | Type | Description |
|------|-----|-------------|
| `rotateAngle` | enum | Rotation angle: `90`, `180`, `270` |
| `rotatePages` | string | Page ranges (empty = all) |

## PDF/A & PDF/UA

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `pdfa` | enum | — | PDF/A standard: `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | Enable PDF/UA (Universal Accessibility) |
| `generateTaggedPdf` | boolean | `false` | Embed structure tags during the Chromium conversion |

Note: PDF/A and encryption are mutually exclusive.

## Encryption (PDF Engines)

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `userPassword` | string | — | Password to open the PDF |
| `ownerPassword` | string | — | Password for full access (lifts restrictions) |
| `allowPrinting` | boolean | `true` | Allow printing |
| `allowCopying` | boolean | `true` | Allow text/graphics extraction |
| `allowModifying` | boolean | `true` | Allow content editing |
| `allowAnnotating` | boolean | `true` | Allow annotations |
| `allowFillingForms` | boolean | `true` | Allow filling in form fields |
| `allowAssembling` | boolean | `true` | Allow inserting/deleting/rotating pages |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/html \
  --form files=@/path/to/index.html \
  --form userPassword=geheim \
  --form allowCopying=false \
  -o my.pdf
```

## Response codes

| Code | Meaning |
|------|-----------|
| 200 | Success — PDF in the body |
| 400 | Invalid fields or critical network error |
| 409 | HTTP status code error or Chromium exception |
| 503 | Timeout |

## Total number of form fields: ~44

Page layout (10) + background (2) + media (2) + JS/waiting (3) + network (7) +
header/footer files (2) + structure/metadata (8) + split (3) + watermark (5) +
stamp (5) + rotation (2) + PDF/A (3) + encryption (8) = ~44 fields + file inputs

---
Source: https://gotenberg.dev/docs/convert-with-chromium/convert-html-to-pdf
