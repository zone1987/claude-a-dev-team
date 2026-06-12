---
name: gotenberg-pdf-rotate
description: >
  Rotate PDF pages with Gotenberg (POST /forms/pdfengines/rotate).
  Triggers: "pdf drehen", "rotate pdf", "pdf seiten drehen", "gotenberg rotate",
  "rotateAngle", "pdf 90 grad", "pdf 180 grad", "pdf 270 grad",
  Seitenrotation, Querformat korrigieren.
---

# Gotenberg — PDF Seiten drehen

Dreht alle oder ausgewaehlte Seiten eines PDFs um 90, 180 oder 270 Grad.
Referenz: `references/deep/rotate.md`

Route: `POST /forms/pdfengines/rotate`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
