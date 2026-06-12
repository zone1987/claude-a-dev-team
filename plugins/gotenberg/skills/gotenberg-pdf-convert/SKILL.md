---
name: gotenberg-pdf-convert
description: >
  Convert PDFs to PDF/A or PDF/UA with Gotenberg (POST /forms/pdfengines/convert).
  Triggers: "pdf/a", "pdf/ua", "pdf archivierung", "pdf archival", "pdf accessibility",
  "gotenberg convert", "PDF/A-1b", "PDF/A-2b", "PDF/A-3b", pdfua, Langzeitarchivierung.
---

# Gotenberg — PDF/A & PDF/UA Konvertierung

Wandelt PDFs in Langzeitarchivformate (PDF/A-1b, PDF/A-2b, PDF/A-3b) oder
barrierefreie PDFs (PDF/UA) um. Erfordert LibreOffice-Neuverarbeitung.
Referenz: `references/deep/convert.md`

Route: `POST /forms/pdfengines/convert`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
