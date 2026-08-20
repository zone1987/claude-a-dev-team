# Gotenberg — getting started & overview

Gotenberg is a **Docker-based, stateless HTTP API** for document conversion.
Send files via `multipart/form-data`, receive a PDF (or screenshot) back.
No Chromium/LibreOffice installation of your own is needed.

## Core features

- **Conversion to PDF**: HTML, URL, Markdown, Office documents
- **Screenshots**: HTML, URL, Markdown as PNG/JPEG/WebP
- **PDF manipulation**: merge, split, encrypt, watermark, metadata, Factur-X/ZUGFeRD

## Quickstart

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8

curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://example.com \
  -o output.pdf
```

Complete reference: `INTRODUCTION-DETAIL.md`
