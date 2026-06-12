---
name: gotenberg-pdf-metadata
description: >
  Read and write PDF metadata (XMP/Exif) with Gotenberg.
  Triggers: "pdf metadata", "pdf metadaten", "pdf author", "pdf title",
  "gotenberg metadata", "exiftool pdf", "xmp metadata", "pdf metadaten lesen",
  "pdf metadaten schreiben", read metadata, write metadata.
  Routes: POST /forms/pdfengines/metadata/read + /write
---

# Gotenberg — PDF Metadaten (Lesen & Schreiben)

Liest XMP/Exif-Metadaten via ExifTool (JSON-Antwort) und schreibt neue XMP-Tags.
Referenz: `references/deep/metadata.md`

Routen:
- `POST /forms/pdfengines/metadata/read` → JSON-Antwort
- `POST /forms/pdfengines/metadata/write` → PDF/ZIP
