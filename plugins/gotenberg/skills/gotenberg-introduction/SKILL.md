---
name: gotenberg-introduction
description: >
  Gotenberg Ueberblick — was ist Gotenberg, welche Faehigkeiten, wann einsetzen.
  Trigger: "was ist Gotenberg", "Gotenberg erklaeren", "PDF API Docker",
  "document conversion API", "what is Gotenberg", "Gotenberg overview",
  "PDF erstellen Docker", "HTML zu PDF API", "Office zu PDF Docker".
---

# Gotenberg — Einstieg & Ueberblick

Gotenberg ist eine **Docker-basierte, zustandslose HTTP-API** zur Dokumentenkonvertierung.
Dateien per `multipart/form-data` senden, PDF (oder Screenshot) zurueckerhalten.
Keine eigene Chromium/LibreOffice-Installation noetig.

## Kernfunktionen

- **Konvertierung zu PDF**: HTML, URL, Markdown, Office-Dokumente
- **Screenshots**: HTML, URL, Markdown als PNG/JPEG/WebP
- **PDF-Manipulation**: Merge, Split, Verschluesseln, Wasserzeichen, Metadaten, Factur-X/ZUGFeRD

## Quickstart

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8

curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://example.com \
  -o output.pdf
```

Vollstaendige Referenz: `references/deep/introduction.md`
