# Gotenberg — Factur-X / ZUGFeRD E-Rechnung

Erstellt normkonforme Factur-X / ZUGFeRD E-Rechnungen: bettet CII-XML als
`factur-x.xml` ein, injiziert XMP-Metadaten, konvertiert zu PDF/A-3.
Referenz: `FACTURX-DETAIL.md`

Route: `POST /forms/pdfengines/factur-x`
Rueckgabe: PDF/A-3 (200) | ZIP (mehrere Inputs) | 400 | 503
