# Gotenberg — PDF split

Splits PDFs by page intervals or page ranges.
Modes: `intervals` (even chunks) | `pages` (page selection, optional `splitUnify`).
Reference: `SPLIT-DETAIL.md`

Route: `POST /forms/pdfengines/split`
Returns: ZIP (default) | single PDF (pages+unify) | 400 | 503
