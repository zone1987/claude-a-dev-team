# Gotenberg — Factur-X / ZUGFeRD e-invoice

Creates standards-compliant Factur-X / ZUGFeRD e-invoices: embeds CII XML as
`factur-x.xml`, injects XMP metadata, converts to PDF/A-3.
Reference: `FACTURX-DETAIL.md`

Route: `POST /forms/pdfengines/factur-x`
Returns: PDF/A-3 (200) | ZIP (multiple inputs) | 400 | 503
