# Gotenberg — PDF Wasserzeichen (Watermark)

Fuegt ein Text-, Bild- oder PDF-Wasserzeichen HINTER den Seiteninhalt.
Schriftart, Farbe, Rotation, Opazitaet via `watermarkOptions` (JSON, pdfcpu-Syntax).
Referenz: `WATERMARK-DETAIL.md`

Route: `POST /forms/pdfengines/watermark`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
