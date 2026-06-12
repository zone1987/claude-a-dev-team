---
name: gotenberg-pdf-attachments
description: >
  Embed file attachments into PDFs with Gotenberg (POST /forms/pdfengines/embed).
  Triggers: "pdf attachment", "pdf anhang", "pdf einbetten", "embed file pdf",
  "gotenberg embed", "pdf dateianhang", embedsMetadata, mimeType, relationship,
  ZUGFeRD, e-rechnung xml anhang.
---

# Gotenberg — PDF Anhange (Attachments)

Bettet externe Dateien (XML, Bilder etc.) als Anhaenge in PDF-Container ein.
Beinhaltet Metadaten pro Anhang (mimeType, AFRelationship).
Referenz: `references/deep/attachments.md`

Route: `POST /forms/pdfengines/embed`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
