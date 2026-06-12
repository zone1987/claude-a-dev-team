---
name: gotenberg-pdf-stamp
description: >
  Stamp PDFs with text, image or PDF overlays with Gotenberg (POST /forms/pdfengines/stamp).
  Triggers: "pdf stempel", "stamp pdf", "pdf text overlay", "pdf bild stempel",
  "gotenberg stamp", "stampSource", "stampExpression", "stampOptions",
  Stempel aufbringen, APPROVED-Stempel, Wasserzeichen vordergrund.
---

# Gotenberg — PDF Stempel (Stamp)

Fuegt einen Text-, Bild- oder PDF-Stempel UEBER den Seiteninhalt.
Positionierung, Rotation, Opazitaet, Schriftart via `stampOptions` (JSON).
Referenz: `references/deep/stamp.md`

Route: `POST /forms/pdfengines/stamp`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
