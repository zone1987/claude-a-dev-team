---
name: gotenberg-libreoffice
description: >
  Gotenberg LibreOffice — Office-Dokumente zu PDF konvertieren. Alle unterstuetzten Formate,
  Form-Felder: landscape, singlePageSheets, skipEmptyPages, exportPlaceholders.
  Trigger: "Gotenberg LibreOffice", "Gotenberg Word zu PDF", "Gotenberg docx PDF",
  "Gotenberg xlsx PDF", "Gotenberg pptx PDF", "Gotenberg Office PDF",
  "Gotenberg libreoffice convert", "Gotenberg Office-Dokument konvertieren",
  "Gotenberg supported formats", "Gotenberg ODT PDF", "Gotenberg CSV PDF".
---

# Gotenberg — LibreOffice-Konvertierung

**Route:** `POST /forms/libreoffice/convert`

Konvertiert Office-Dokumente zu PDF via LibreOffice. Unterstuetzt Word, Excel, PowerPoint,
OpenDocument, Textdateien und viele weitere Formate.

## Pflichtfeld

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `files` | file[] | Mindestens eine Datei zum Konvertieren |

```bash
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  -o my.pdf
```

## Layout-Felder

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `landscape` | boolean | `false` | Querformat |
| `singlePageSheets` | boolean | `false` | Jedes Tabellenblatt auf genau eine Seite zwingen |
| `skipEmptyPages` | boolean | `false` | Automatisch eingefuegte Leerseiten unterdruecken (nur Writer) |
| `exportPlaceholders` | boolean | `false` | Platzhalterfelder als visuelle Markierungen exportieren |

Vollstaendige Formatenliste & Feldtabellen: `references/deep/libreoffice.md`
