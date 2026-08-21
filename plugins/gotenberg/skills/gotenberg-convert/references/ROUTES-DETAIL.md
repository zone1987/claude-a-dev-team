# Gotenberg — Complete route reference

## Contents

- [Protocol](#protocol)
- [Common request headers](#common-request-headers)
- [Standard response headers (success 200)](#standard-response-headers-success-200)
- [Authentication](#authentication)
- [All routes](#all-routes)
- [Note on conversion routes](#note-on-conversion-routes)
- [HTTP status codes](#http-status-codes)

## Protocol

Every route accepts a **`multipart/form-data` POST request** and returns a file.

## Common request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Filename of the output file without extension. Gotenberg appends the correct extension automatically. |
| `Gotenberg-Trace` | string | Random UUID | Custom request ID for identification in the log. Overrides the default UUID. Configurable via `--api-correlation-id-header`. |

## Standard response headers (success 200)

```
Content-Disposition: attachment; filename={output-filename.ext}
Content-Type: {content-type}
Content-Length: {content-length}
Gotenberg-Trace: {trace}
Body: {output-file}
```

## Authentication

Enable Basic Auth via the CLI flag:
```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8 \
  gotenberg --api-enable-basic-auth
```

Set credentials exclusively via environment variable:
- `GOTENBERG_API_BASIC_AUTH_USERNAME`
- `GOTENBERG_API_BASIC_AUTH_PASSWORD`

## All routes

### Conversion to PDF

| Task | Route | Engine |
|---------|-------|--------|
| URL to PDF | `POST /forms/chromium/convert/url` | Chromium |
| HTML file to PDF | `POST /forms/chromium/convert/html` | Chromium |
| Markdown to PDF | `POST /forms/chromium/convert/markdown` | Chromium |
| Office documents to PDF | `POST /forms/libreoffice/convert` | LibreOffice |

### Screenshots

| Task | Route |
|---------|-------|
| Screenshot a URL | `POST /forms/chromium/screenshot/url` |
| Screenshot HTML | `POST /forms/chromium/screenshot/html` |
| Screenshot Markdown | `POST /forms/chromium/screenshot/markdown` |

### PDF manipulation (PDF Engines)

| Task | Route |
|---------|-------|
| Merge | `POST /forms/pdfengines/merge` |
| Split | `POST /forms/pdfengines/split` |
| PDF/A or PDF/UA | `POST /forms/pdfengines/convert` |
| Read metadata | `POST /forms/pdfengines/metadata/read` |
| Write metadata | `POST /forms/pdfengines/metadata/write` |
| Read bookmarks | `POST /forms/pdfengines/bookmarks/read` |
| Write bookmarks | `POST /forms/pdfengines/bookmarks/write` |
| Embed file attachments | `POST /forms/pdfengines/embed` |
| Factur-X / ZUGFeRD | `POST /forms/pdfengines/factur-x` |
| Flatten form fields | `POST /forms/pdfengines/flatten` |
| Watermark | `POST /forms/pdfengines/watermark` |
| Stamp | `POST /forms/pdfengines/stamp` |
| Rotate | `POST /forms/pdfengines/rotate` |
| Encrypt | `POST /forms/pdfengines/encrypt` |

### System & operations

| Route | Description |
|-------|-------------|
| `GET /health` | Health check |
| `GET /version` | Version info |
| `GET /debug` | Configuration dump (must be enabled via `--api-enable-debug-route`) |

### Asynchronous & remote

| Feature | Description |
|---------|-------------|
| Webhooks | Asynchronous processing; Gotenberg uploads the result to a URL |
| Download From | Input files can be supplied by remote URL |

## Note on conversion routes

Conversion routes accept most PDF engine features
(metadata, attachments, watermark, encryption, ...) directly in the same request.
No separate second API call needed.

## HTTP status codes

| Code | Meaning |
|------|-----------|
| 200 | Success — file in the body |
| 400 | Invalid fields or critical network error |
| 403 | URL forbidden (outbound filter) |
| 409 | HTTP status code error from the target page / Chromium console exception |
| 503 | Timeout — the request exceeded the time limit |

---
Source: https://gotenberg.dev/docs/getting-started/routes
