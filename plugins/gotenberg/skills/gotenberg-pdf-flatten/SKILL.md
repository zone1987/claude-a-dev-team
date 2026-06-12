---
name: gotenberg-pdf-flatten
description: >
  Flatten PDF form fields with Gotenberg (POST /forms/pdfengines/flatten).
  Triggers: "flatten pdf", "pdf formular einbetten", "pdf formularfelder fixieren",
  "gotenberg flatten", "form fields to content", "interaktive felder entfernen",
  PDF-Formular-Flatten, non-editable pdf.
---

# Gotenberg — PDF Flatten

Wandelt interaktive Formularfelder in statischen Seiteninhalt um (nicht mehr bearbeitbar).
Referenz: `references/deep/flatten.md`

Route: `POST /forms/pdfengines/flatten`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
