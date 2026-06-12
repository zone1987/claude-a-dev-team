---
name: gotenberg-pdf-watermark
description: >
  Add text, image or PDF watermarks behind PDF content with Gotenberg (POST /forms/pdfengines/watermark).
  Triggers: "pdf wasserzeichen", "watermark pdf", "pdf hintergrund text",
  "gotenberg watermark", "watermarkSource", "watermarkExpression", "watermarkOptions",
  CONFIDENTIAL wasserzeichen, Hintergrundstempel, transparent watermark.
---

# Gotenberg — PDF Wasserzeichen (Watermark)

Fuegt ein Text-, Bild- oder PDF-Wasserzeichen HINTER den Seiteninhalt.
Schriftart, Farbe, Rotation, Opazitaet via `watermarkOptions` (JSON, pdfcpu-Syntax).
Referenz: `references/deep/watermark.md`

Route: `POST /forms/pdfengines/watermark`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
