# Gotenberg — URL to PDF (full reference)

**Route:** `POST /forms/chromium/convert/url`
**Description:** Converts a web page given by URL to PDF via headless Chromium.
Supports JavaScript, SPAs and dynamic content.

## Contents

- [Mandatory form field](#mandatory-form-field)
- [Request headers](#request-headers)
- [Page layout](#page-layout)
- [Background](#background)
- [Print media](#print-media)
- [JavaScript & waiting](#javascript--waiting)
- [Network](#network)
- [Header & footer](#header--footer)
- [Structure & metadata](#structure--metadata)
- [Split & pages](#split--pages)
- [Watermark & stamp](#watermark--stamp)
- [PDF/A & accessibility](#pdfa--accessibility)
- [Encryption](#encryption)
- [Response codes](#response-codes)
- [Total number of form fields: ~47](#total-number-of-form-fields-47)

## Mandatory form field

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `url` | string | Yes | URL of the page to convert. `file://` URLs are rejected with 400. Convert local HTML files via `/forms/chromium/convert/html`. |

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o my.pdf
```

## Request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | File name of the output (without extension) |
| `Gotenberg-Trace` | string | Random UUID | Custom request ID for logs |

## Page layout

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `paperWidth` | string | `8.5` | Paper width in inches (units: in, pt, cm) |
| `paperHeight` | string | `11` | Paper height in inches |
| `marginTop` | string | `0.39` | Top margin in inches |
| `marginBottom` | string | `0.39` | Bottom margin |
| `marginLeft` | string | `0.39` | Left margin |
| `marginRight` | string | `0.39` | Right margin |
| `landscape` | boolean | `false` | Landscape orientation |
| `scale` | number | `1.0` | Zoom factor |
| `singlePage` | boolean | `false` | All content on one page |
| `preferCssPageSize` | boolean | `false` | CSS `@page` instead of the API parameters |

## Background

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `printBackground` | boolean | `false` | Include background graphics/colors |
| `omitBackground` | boolean | `false` | Hide the white background |

## Print media

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `print` | `screen` or `print` |
| `emulatedMediaFeatures` | json | — | CSS media feature overrides (e.g. dark mode) |

## JavaScript & waiting

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Fixed wait time (e.g. `5s`, `500ms`) |
| `waitForExpression` | string | — | JS expression; conversion starts when it is `true` |
| `waitForSelector` | string | — | CSS selector; starts when the element is in the DOM |

## Network

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie array for auth/session |
| `extraHttpHeaders` | json | — | Additional HTTP headers for all browser requests |
| `userAgent` | string | — | Override the user agent |
| `failOnHttpStatusCodes` | json | `[499,599]` | 409 on these status codes from the main URL |
| `failOnResourceHttpStatusCodes` | json | — | 409 on these codes from an asset |
| `ignoreResourceHttpStatusDomains` | json | — | Exclude domains from the status code check |
| `skipNetworkIdleEvent` | boolean | `true` | Do not wait for network idle |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Do not wait for almost-idle |
| `failOnResourceLoadingFailed` | boolean | `false` | 400 on asset loading failures |
| `failOnConsoleExceptions` | boolean | `false` | 409 on JS exceptions |

## Header & footer

| File | Description |
|-------|-------------|
| `header.html` | Complete HTML for the page header |
| `footer.html` | Complete HTML for the page footer |

## Structure & metadata

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `generateDocumentOutline` | boolean | `false` | PDF bookmarks from headings |
| `generateTaggedPdf` | boolean | `false` | Accessibility tags |
| `metadata` | json | — | XMP metadata |
| `embeds` (files) | file[] | — | Files to embed |
| `embedsMetadata` | json | — | Per-attachment metadata |
| `facturxXml` (file) | file | — | Factur-X XML |
| `facturxConformanceLevel` | enum | — | Factur-X conformance level |
| `facturxDocumentType` | enum | `INVOICE` | Factur-X document type |
| `facturxVersion` | string | `1.0` | Factur-X version |
| `flatten` | boolean | `false` | Flatten form fields |

## Split & pages

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `nativePageRanges` | string | — | Native page selection (e.g. `1-5, 8`) |
| `splitMode` | enum | — | `intervals` or `pages` |
| `splitSpan` | string | — | Split rule |
| `splitUnify` | boolean | `false` | Pages mode: into one file |

## Watermark & stamp

| Field | Type | Description |
|------|-----|-------------|
| `watermarkSource` | enum | `text`, `image`, `pdf` |
| `watermarkExpression` | string | Content or file name |
| `watermarkPages` | string | Page ranges |
| `watermarkOptions` | json | Engine options |
| `watermark` (file) | file | Watermark file |
| `stampSource` | enum | `text`, `image`, `pdf` |
| `stampExpression` | string | Content or file name |
| `stampPages` | string | Page ranges |
| `stampOptions` | json | Engine options |
| `stamp` (file) | file | Stamp file |
| `rotateAngle` | enum | `90`, `180`, `270` |
| `rotatePages` | string | Page ranges |

## PDF/A & accessibility

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `pdfa` | enum | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` |
| `pdfua` | boolean | `false` | Enable PDF/UA |

## Encryption

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `userPassword` | string | — | Open password |
| `ownerPassword` | string | — | Full-access password |
| `allowPrinting` | boolean | `true` | Printing |
| `allowCopying` | boolean | `true` | Copying |
| `allowModifying` | boolean | `true` | Editing |
| `allowAnnotating` | boolean | `true` | Annotating |
| `allowFillingForms` | boolean | `true` | Filling in forms |
| `allowAssembling` | boolean | `true` | Page assembly |

## Response codes

| Code | Meaning |
|------|-----------|
| 200 | Success |
| 400 | Invalid fields / network error |
| 403 | URL forbidden (outbound filter) |
| 409 | Status code error / console exception |
| 503 | Timeout |

## Total number of form fields: ~47

Mandatory fields (1) + page layout (10) + background (2) + media (2) + JS/waiting (3) +
network (10) + header/footer files (2) + structure/metadata (10) + split (4) +
watermark (12) + PDF/A (2) + encryption (8) = ~47 fields

---
Source: https://gotenberg.dev/docs/convert-with-chromium/convert-url-to-pdf
