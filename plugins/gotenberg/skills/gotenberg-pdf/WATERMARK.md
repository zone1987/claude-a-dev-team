# Gotenberg — PDF watermark

Adds a text, image or PDF watermark BEHIND the page content.
Font, color, rotation, opacity via `watermarkOptions` (JSON, pdfcpu syntax).
Reference: `WATERMARK-DETAIL.md`

Route: `POST /forms/pdfengines/watermark`
Returns: PDF (200) | ZIP (multiple inputs) | 400 | 503
