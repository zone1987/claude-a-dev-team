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

Vollstaendige Formatenliste & Feldtabellen: `LIBREOFFICE-DETAIL.md`
