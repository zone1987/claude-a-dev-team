---
name: gotenberg-pdf-facturx
description: >
  Create Factur-X / ZUGFeRD e-invoices with Gotenberg (POST /forms/pdfengines/factur-x).
  Triggers: "factur-x", "zugferd", "e-rechnung", "e-invoice pdf", "cii xml invoice",
  "gotenberg facturx", conformanceLevel EN 16931, XRECHNUNG, MINIMUM, BASIC,
  elektronische Rechnung, ZUGFeRD-Konformitaet.
---

# Gotenberg — Factur-X / ZUGFeRD E-Rechnung

Erstellt normkonforme Factur-X / ZUGFeRD E-Rechnungen: bettet CII-XML als
`factur-x.xml` ein, injiziert XMP-Metadaten, konvertiert zu PDF/A-3.
Referenz: `references/deep/facturx.md`

Route: `POST /forms/pdfengines/factur-x`
Rueckgabe: PDF/A-3 (200) | ZIP (mehrere Inputs) | 400 | 503
