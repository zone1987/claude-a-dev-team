# Gotenberg — Vollstaendige Einfuehrung

## Was ist Gotenberg?

Gotenberg ist eine Docker-basierte API fuer die Konvertierung von Dokumenten zu PDF.
Dateien werden per `multipart/form-data` gesendet; zurueck kommt ein PDF (oder Bild).
Keine eigene Verwaltung von Chromium, LibreOffice oder Schriftarten noetig.

Uber die reine Konvertierung hinaus: Merge, Split, Encrypt, Wasserzeichen, Metadaten,
Factur-X / ZUGFeRD E-Invoicing.

## Quickstart

```bash
# 1. Container starten
docker run --rm -p "3000:3000" gotenberg/gotenberg:8

# 2. URL zu PDF
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o invoice.pdf
```

## Alle Routen im Ueberblick

### Konvertierung zu PDF

| Aufgabe | Route |
|---------|-------|
| URL zu PDF | `POST /forms/chromium/convert/url` |
| HTML-Datei zu PDF | `POST /forms/chromium/convert/html` |
| Markdown zu PDF | `POST /forms/chromium/convert/markdown` |
| Office-Dokumente zu PDF | `POST /forms/libreoffice/convert` |

### Screenshots

| Aufgabe | Route |
|---------|-------|
| URL screenshotten | `POST /forms/chromium/screenshot/url` |
| HTML screenshotten | `POST /forms/chromium/screenshot/html` |
| Markdown screenshotten | `POST /forms/chromium/screenshot/markdown` |

### PDF-Manipulation

| Aufgabe | Route |
|---------|-------|
| Merge | `POST /forms/pdfengines/merge` |
| Split | `POST /forms/pdfengines/split` |
| PDF/A oder PDF/UA | `POST /forms/pdfengines/convert` |
| Metadaten lesen | `POST /forms/pdfengines/metadata/read` |
| Metadaten schreiben | `POST /forms/pdfengines/metadata/write` |
| Lesezeichen lesen | `POST /forms/pdfengines/bookmarks/read` |
| Lesezeichen schreiben | `POST /forms/pdfengines/bookmarks/write` |
| Dateianhange einbetten | `POST /forms/pdfengines/embed` |
| Factur-X / ZUGFeRD | `POST /forms/pdfengines/factur-x` |
| Formularfelder glaetten | `POST /forms/pdfengines/flatten` |
| Wasserzeichen | `POST /forms/pdfengines/watermark` |
| Stempel | `POST /forms/pdfengines/stamp` |
| Drehen | `POST /forms/pdfengines/rotate` |
| Verschluesseln | `POST /forms/pdfengines/encrypt` |

### System

| Route | Beschreibung |
|-------|-------------|
| `GET /health` | Health-Check |
| `GET /version` | Version |
| `GET /debug` | Konfigurationsdump (muss aktiviert werden) |

## Architektur-Merkmale

- **Stateless**: Jeder Request ist in sich abgeschlossen
- **Zwei Conversion-Engines**: Headless Chromium + LibreOffice (via unoconv)
- **Funf PDF-Engines**: ExifTool, PDFtk, pdfcpu, QPDF, UNO (LibreOffice-intern)
- **Konvertierungsrouten akzeptieren PDF-Engine-Funktionen im selben Request** (kein zweiter API-Call)
- **Asynchrone Verarbeitung** via Webhooks moeglich
- **Remote-Input** per "Download From"-Funktion

## Ressourcen

- GitHub: https://github.com/gotenberg/gotenberg
- PHP SDK: https://github.com/gotenberg/gotenberg-php
- Awesome Gotenberg (Community-Clients): https://github.com/gotenberg/awesome-gotenberg
- Demo: https://demo.gotenberg.dev (2 req/s, 5 MB Body-Limit)

---
Quelle: https://gotenberg.dev/docs/getting-started/introduction
