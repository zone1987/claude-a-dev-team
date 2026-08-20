---
name: gotenberg-convert
description: Gotenberg conversion: HTML, URL and Markdown to PDF via Chromium, Office documents via LibreOffice, screenshots, the full route list. Use when converting a document or page to PDF with Gotenberg.
---

# Gotenberg conversion routes

Two engines: Chromium renders web content, LibreOffice handles Office formats. The route decides which.

## Reference map

- **[CHROMIUM-HTML.md](CHROMIUM-HTML.md)**: Converts an `index.html` to PDF via headless Chromium. [CHROMIUM-HTML-DETAIL](CHROMIUM-HTML-DETAIL.md).
- **[CHROMIUM-MARKDOWN.md](CHROMIUM-MARKDOWN.md)**: Converts Markdown to PDF via headless Chromium. [CHROMIUM-MARKDOWN-DETAIL](CHROMIUM-MARKDOWN-DETAIL.md).
- **[CHROMIUM-SCREENSHOTS.md](CHROMIUM-SCREENSHOTS.md)**: Three routes for screenshots via headless Chromium. [CHROMIUM-SCREENSHOTS-DETAIL](CHROMIUM-SCREENSHOTS-DETAIL.md).
- **[CHROMIUM-URL.md](CHROMIUM-URL.md)**: Converts a web page by URL to PDF via headless Chromium. [CHROMIUM-URL-DETAIL](CHROMIUM-URL-DETAIL.md).
- **[LIBREOFFICE.md](LIBREOFFICE.md)**: Converts Office documents to PDF via LibreOffice. [LIBREOFFICE-DETAIL](LIBREOFFICE-DETAIL.md).
- **[ROUTES.md](ROUTES.md)**: Every route accepts a `multipart/form-data` POST request and returns a file. [ROUTES-DETAIL](ROUTES-DETAIL.md).

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
