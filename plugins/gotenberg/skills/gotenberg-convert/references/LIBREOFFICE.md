# Gotenberg — LibreOffice conversion

**Route:** `POST /forms/libreoffice/convert`

Converts Office documents to PDF via LibreOffice. Supports Word, Excel, PowerPoint,
OpenDocument, text files and many more formats.

## Required field

| Field | Type | Description |
|------|-----|-------------|
| `files` | file[] | At least one file to convert |

```bash
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form files=@/path/to/document.docx \
  -o my.pdf
```

## Layout fields

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `landscape` | boolean | `false` | Landscape orientation |
| `singlePageSheets` | boolean | `false` | Force every spreadsheet sheet onto exactly one page |
| `skipEmptyPages` | boolean | `false` | Suppress automatically inserted blank pages (Writer only) |
| `exportPlaceholders` | boolean | `false` | Export placeholder fields as visual markers |

Complete format list & field tables: `LIBREOFFICE-DETAIL.md`
