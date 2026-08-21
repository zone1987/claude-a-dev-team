# Gotenberg — Complete introduction

## What is Gotenberg?

Gotenberg is a Docker-based API for converting documents to PDF.
Files are sent via `multipart/form-data`; what comes back is a PDF (or image).
No need to manage Chromium, LibreOffice or fonts yourself.

Beyond plain conversion: merge, split, encrypt, watermarks, metadata,
Factur-X / ZUGFeRD e-invoicing.

## Quickstart

```bash
# 1. Start the container
docker run --rm -p "3000:3000" gotenberg/gotenberg:8

# 2. URL to PDF
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o invoice.pdf
```

## All routes at a glance

### Conversion to PDF

| Task | Route |
|---------|-------|
| URL to PDF | `POST /forms/chromium/convert/url` |
| HTML file to PDF | `POST /forms/chromium/convert/html` |
| Markdown to PDF | `POST /forms/chromium/convert/markdown` |
| Office documents to PDF | `POST /forms/libreoffice/convert` |

### Screenshots

| Task | Route |
|---------|-------|
| Screenshot a URL | `POST /forms/chromium/screenshot/url` |
| Screenshot HTML | `POST /forms/chromium/screenshot/html` |
| Screenshot Markdown | `POST /forms/chromium/screenshot/markdown` |

### PDF manipulation

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

### System

| Route | Description |
|-------|-------------|
| `GET /health` | Health check |
| `GET /version` | Version |
| `GET /debug` | Configuration dump (must be enabled) |

## Architectural characteristics

- **Stateless**: every request is self-contained
- **Two conversion engines**: headless Chromium + LibreOffice (via unoconv)
- **Five PDF engines**: ExifTool, PDFtk, pdfcpu, QPDF, UNO (LibreOffice-internal)
- **Conversion routes accept PDF engine functions in the same request** (no second API call)
- **Asynchronous processing** possible via webhooks
- **Remote input** via the "Download From" feature

## Resources

- GitHub: https://github.com/gotenberg/gotenberg
- PHP SDK: https://github.com/gotenberg/gotenberg-php
- Awesome Gotenberg (community clients): https://github.com/gotenberg/awesome-gotenberg
- Demo: https://demo.gotenberg.dev (2 req/s, 5 MB body limit)

---
Source: https://gotenberg.dev/docs/getting-started/introduction
