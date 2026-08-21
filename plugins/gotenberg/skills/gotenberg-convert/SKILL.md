---
name: gotenberg-convert
description: Gotenberg conversion: HTML, URL and Markdown to PDF via Chromium, Office documents via LibreOffice, screenshots, the full route list. Use when converting a document or page to PDF with Gotenberg.
---

# Gotenberg conversion routes

Two engines: Chromium renders web content, LibreOffice handles Office formats. The route decides which.

## Reference map

- **[CHROMIUM-HTML.md](references/CHROMIUM-HTML.md)**: Converts an `index.html` to PDF via headless Chromium.
- **[CHROMIUM-MARKDOWN.md](references/CHROMIUM-MARKDOWN.md)**: Converts Markdown to PDF via headless Chromium.
- **[CHROMIUM-SCREENSHOTS.md](references/CHROMIUM-SCREENSHOTS.md)**: Three routes for screenshots via headless Chromium.
- **[CHROMIUM-URL.md](references/CHROMIUM-URL.md)**: Converts a web page by URL to PDF via headless Chromium.
- **[LIBREOFFICE.md](references/LIBREOFFICE.md)**: Converts Office documents to PDF via LibreOffice.
- **[ROUTES.md](references/ROUTES.md)**: Every route accepts a `multipart/form-data` POST request and returns a file.

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
