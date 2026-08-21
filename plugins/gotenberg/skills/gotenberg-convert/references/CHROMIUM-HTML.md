# Gotenberg — HTML to PDF

**Route:** `POST /forms/chromium/convert/html`

Converts an `index.html` (with optional assets) to PDF via headless Chromium.

## Required field

| Field | Type | Description |
|------|-----|-------------|
| `files` (index.html) | file | HTML file, must be named `index.html` |

## Common headers

| Header | Description |
|--------|-------------|
| `Gotenberg-Output-Filename` | Filename (without extension) |
| `Gotenberg-Trace` | Request ID for logs |

## Page size (approx. 10 fields)

`paperWidth`, `paperHeight`, `marginTop`, `marginBottom`, `marginLeft`, `marginRight`,
`landscape`, `scale`, `singlePage`, `preferCssPageSize`

Complete field tables: `CHROMIUM-HTML-DETAIL.md`
