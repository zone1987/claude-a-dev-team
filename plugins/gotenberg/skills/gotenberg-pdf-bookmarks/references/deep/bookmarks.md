# Gotenberg — PDF Lesezeichen Lesen & Schreiben (Vollreferenz)

## Routen

```
POST /forms/pdfengines/bookmarks/read
POST /forms/pdfengines/bookmarks/write
```

**Content-Type des Requests:** `multipart/form-data`

---

## 1. Lesezeichen Lesen

### Route

```
POST /forms/pdfengines/bookmarks/read
```

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Form-Felder

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `files` | file[] | Ja | PDF-Dateien, deren Lesezeichen gelesen werden sollen |

### Antwort

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/json; charset=UTF-8` | JSON-Objekt mit Dateiname als Schluessel |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Antwort-Format (Beispiel)

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

### Bookmark-Objekt-Struktur

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | string | Bezeichnung des Lesezeichens |
| `page` | integer | Seitennummer (1-basiert) |
| `children` | array | Untergeordnete Lesezeichen (rekursiv) |

### curl-Beispiel

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/read \
  --form files=@/path/to/dokument.pdf \
  --form files=@/path/to/bericht.pdf
```

---

## 2. Lesezeichen Schreiben

### Route

```
POST /forms/pdfengines/bookmarks/write
```

### Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID |

### Form-Felder

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `bookmarks` | JSON-string | Ja | Lesezeichen als Liste oder Dateiname-Map |
| `files` | file[] | Ja | PDF-Dateien, die aktualisiert werden sollen |

### Bookmarks-JSON-Format: Liste (fuer eine Datei)

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

### Bookmarks-JSON-Format: Map (fuer mehrere Dateien)

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

### Antwort

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | Aktualisierte PDF; mehrere Inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Antwort-Header bei Erfolg

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

### curl-Beispiele

#### Lesezeichen als Liste schreiben

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/write \
  --form files=@/path/to/dokument.pdf \
  --form 'bookmarks=[{"title":"Kapitel 1","page":1,"children":[]},{"title":"Kapitel 2","page":5,"children":[{"title":"Abschnitt 2.1","page":6,"children":[]}]}]' \
  -o mit-lesezeichen.pdf
```

#### Lesezeichen als Map fuer mehrere Dateien

```bash
curl --request POST http://localhost:3000/forms/pdfengines/bookmarks/write \
  --form files=@/path/to/datei1.pdf \
  --form files=@/path/to/datei2.pdf \
  --form 'bookmarks={"datei1.pdf":[{"title":"Einleitung","page":1,"children":[]}],"datei2.pdf":[{"title":"Kapitel 1","page":1,"children":[]}]}' \
  -o aktualisiert.zip
```

---

## Hinweise

- Lesezeichen representieren die Dokumentgliederung (Table of Contents) im PDF
- `children`-Array ist immer angegeben, auch wenn leer (`[]`)
- Seitennummern sind 1-basiert
- Beim Merge kann `autoIndexBookmarks=true` verwendet werden, um bestehende Lesezeichen automatisch zu indexieren

---

Quelle:
- https://gotenberg.dev/docs/manipulate-pdfs/read-bookmarks
- https://gotenberg.dev/docs/manipulate-pdfs/write-bookmarks
