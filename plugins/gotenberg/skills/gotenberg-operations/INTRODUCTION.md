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

Vollstaendige Referenz: `INTRODUCTION-DETAIL.md`
