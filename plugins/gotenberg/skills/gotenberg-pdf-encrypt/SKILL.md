---
name: gotenberg-pdf-encrypt
description: >
  Encrypt PDFs with passwords and permissions with Gotenberg (POST /forms/pdfengines/encrypt).
  Triggers: "pdf verschluesseln", "pdf passwort", "encrypt pdf", "pdf permissions",
  "gotenberg encrypt", userPassword, ownerPassword, allowPrinting, allowCopying,
  PDF-Verschluesselung, PDF-Berechtigungen.
---

# Gotenberg — PDF Verschluesselung

Schuetzt PDFs mit Benutzer-/Eigentuemerpasswort und Berechtigungsrestriktionen
(Drucken, Kopieren, Bearbeiten, Annotieren, Formulare, Seitenverwaltung).
Referenz: `references/deep/encrypt.md`

Route: `POST /forms/pdfengines/encrypt`
Rueckgabe: PDF (200) | ZIP (mehrere Inputs) | 400 | 503
