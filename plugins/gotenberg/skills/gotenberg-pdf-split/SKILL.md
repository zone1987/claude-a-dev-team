---
name: gotenberg-pdf-split
description: >
  Split PDFs with Gotenberg (POST /forms/pdfengines/split).
  Triggers: "split pdf", "pdf aufteilen", "pdf teilen", "pdf pages extract",
  "gotenberg split", splitMode pages intervals, splitSpan, splitUnify, PDF-Trennung.
---

# Gotenberg — PDF Split

Teilt PDFs nach Seitenintervallen oder Seitenbereichen auf.
Modi: `intervals` (gleichmaessige Chunks) | `pages` (Seitenauswahl, optional `splitUnify`).
Referenz: `references/deep/split.md`

Route: `POST /forms/pdfengines/split`
Rueckgabe: ZIP (Standard) | einzelne PDF (pages+unify) | 400 | 503
