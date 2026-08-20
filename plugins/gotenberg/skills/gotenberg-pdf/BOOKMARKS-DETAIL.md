# Gotenberg — Reading & Writing PDF Bookmarks (Full Reference)

## Contents

- [Routes](#routes)
- [1. Reading Bookmarks](#1-reading-bookmarks)
- [2. Writing Bookmarks](#2-writing-bookmarks)
- [Notes](#notes)

## Routes

```
POST /forms/pdfengines/bookmarks/read
POST /forms/pdfengines/bookmarks/write
```

**Content type of the request:** `multipart/form-data`

---

## 1. Reading Bookmarks

### Route

```
POST /forms/pdfengines/bookmarks/read
```

### Request Headers

| Header | Type | Required | Description |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Form Fields

| Field | Type | Required | Description |
|------|-----|---------|--------------|
| `files` | file[] | Yes | PDF files whose bookmarks are to be read |

### Response

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | `application/json; charset=UTF-8` | JSON object with the file name as key |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response Format (Example)

```json
{
  "dokument.pdf": [
    {
      "title": "Kapitel 1",
      "page": 1,
      "children": [
        {
          "title": "Abschnitt 1.1",
          "page": 2,
          "children": []
        },
        {
          "title": "Abschnitt 1.2",
          "page": 4,
          "children": []
        }
      ]
    },
    {
      "title": "Kapitel 2",
      "page": 7,
      "children": [
        {
          "title": "Abschnitt 2.1",
          "page": 8,
          "children": []
        }
      ]
    }
  ],
  "bericht.pdf": []
}
```

### Bookmark Object Structure

| Field | Type | Description |
|------|-----|--------------|
| `title` | string | Label of the bookmark |
| `page` | integer | Page number (1-based) |
| `children` | array | Nested bookmarks (recursive) |

### curl Example

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/read \
  --form files=@/path/to/dokument.pdf \
  --form files=@/path/to/bericht.pdf
```

---

## 2. Writing Bookmarks

### Route

```
POST /forms/pdfengines/bookmarks/write
```

### Request Headers

| Header | Type | Required | Default | Description |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | No | random UUID | File name of the output |
| `Gotenberg-Trace` | string | No | UUID | Custom request ID |

### Form Fields

| Field | Type | Required | Description |
|------|-----|---------|--------------|
| `bookmarks` | JSON string | Yes | Bookmarks as a list or as a file-name map |
| `files` | file[] | Yes | PDF files to be updated |

### Bookmarks JSON Format: List (for a single file)

```json
[
  {
    "title": "Kapitel 1",
    "page": 1,
    "children": []
  },
  {
    "title": "Kapitel 2",
    "page": 5,
    "children": [
      {
        "title": "Abschnitt 2.1",
        "page": 6,
        "children": []
      }
    ]
  }
]
```

### Bookmarks JSON Format: Map (for multiple files)

```json
{
  "datei1.pdf": [
    {"title": "Einleitung", "page": 1, "children": []}
  ],
  "datei2.pdf": [
    {"title": "Kapitel 1", "page": 1, "children": []},
    {"title": "Kapitel 2", "page": 10, "children": []}
  ]
}
```

### Response

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | variable | Updated PDF; multiple inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Invalid form fields |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Response Headers on Success

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

### curl Examples

#### Write bookmarks as a list

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/write \
  --form files=@/path/to/dokument.pdf \
  --form 'bookmarks=[{"title":"Kapitel 1","page":1,"children":[]},{"title":"Kapitel 2","page":5,"children":[{"title":"Abschnitt 2.1","page":6,"children":[]}]}]' \
  -o with-bookmarks.pdf
```

#### Bookmarks as a map for multiple files

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/write \
  --form files=@/path/to/datei1.pdf \
  --form files=@/path/to/datei2.pdf \
  --form 'bookmarks={"datei1.pdf":[{"title":"Einleitung","page":1,"children":[]}],"datei2.pdf":[{"title":"Kapitel 1","page":1,"children":[]}]}' \
  -o aktualisiert.zip
```

---

## Notes

- Bookmarks represent the document outline (table of contents) within the PDF
- The `children` array is always present, even when empty (`[]`)
- Page numbers are 1-based
- When merging, `autoIndexBookmarks=true` can be used to index existing bookmarks automatically

---

Source:
- https://gotenberg.dev/docs/manipulate-pdfs/read-bookmarks
- https://gotenberg.dev/docs/manipulate-pdfs/write-bookmarks
