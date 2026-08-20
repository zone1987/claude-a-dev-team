# Gotenberg — PDF Split

Teilt PDFs nach Seitenintervallen oder Seitenbereichen auf.
Modi: `intervals` (gleichmaessige Chunks) | `pages` (Seitenauswahl, optional `splitUnify`).
Referenz: `SPLIT-DETAIL.md`

Route: `POST /forms/pdfengines/split`
Rueckgabe: ZIP (Standard) | einzelne PDF (pages+unify) | 400 | 503
