---
name: gotenberg-convert
description: Gotenberg conversion: HTML, URL and Markdown to PDF via Chromium, Office documents via LibreOffice, screenshots, the full route list. Use when converting a document or page to PDF with Gotenberg.
---

# Gotenberg conversion routes

Two engines: Chromium renders web content, LibreOffice handles Office formats. The route decides which.

## Reference map

- **[CHROMIUM-HTML.md](CHROMIUM-HTML.md)**: Konvertiert eine `index.html` zu PDF via Headless Chromium. [CHROMIUM-HTML-DETAIL](CHROMIUM-HTML-DETAIL.md).
- **[CHROMIUM-MARKDOWN.md](CHROMIUM-MARKDOWN.md)**: Konvertiert Markdown zu PDF via Headless Chromium. [CHROMIUM-MARKDOWN-DETAIL](CHROMIUM-MARKDOWN-DETAIL.md).
- **[CHROMIUM-SCREENSHOTS.md](CHROMIUM-SCREENSHOTS.md)**: Drei Routen fuer Screenshots via Headless Chromium:. [CHROMIUM-SCREENSHOTS-DETAIL](CHROMIUM-SCREENSHOTS-DETAIL.md).
- **[CHROMIUM-URL.md](CHROMIUM-URL.md)**: Konvertiert eine Webseite per URL zu PDF via Headless Chromium. [CHROMIUM-URL-DETAIL](CHROMIUM-URL-DETAIL.md).
- **[LIBREOFFICE.md](LIBREOFFICE.md)**: Konvertiert Office-Dokumente zu PDF via LibreOffice. [LIBREOFFICE-DETAIL](LIBREOFFICE-DETAIL.md).
- **[ROUTES.md](ROUTES.md)**: Jede Route akzeptiert einen `multipart/form-data` POST-Request und gibt eine Datei zurueck. [ROUTES-DETAIL](ROUTES-DETAIL.md).

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
