---
name: gotenberg-pdf-bookmarks
description: >
  Read and write PDF bookmarks / document outline with Gotenberg.
  Triggers: "pdf bookmarks", "pdf lesezeichen", "pdf inhaltsverzeichnis",
  "gotenberg bookmarks", "pdf outline", "table of contents pdf",
  "pdf navigation", bookmarks lesen schreiben.
  Routes: POST /forms/pdfengines/bookmarks/read + /write
---

# Gotenberg — PDF Lesezeichen (Lesen & Schreiben)

Extrahiert die Dokumentgliederung (hierarchische Bookmarks) als JSON
oder schreibt neue Lesezeichen in PDFs.
Referenz: `references/deep/bookmarks.md`

Routen:
- `POST /forms/pdfengines/bookmarks/read` → JSON-Antwort
- `POST /forms/pdfengines/bookmarks/write` → PDF/ZIP
