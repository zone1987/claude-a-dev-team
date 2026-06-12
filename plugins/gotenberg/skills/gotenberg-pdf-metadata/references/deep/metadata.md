# Gotenberg — PDF Metadaten Lesen & Schreiben (Vollreferenz)

## Routen

```
POST /forms/pdfengines/metadata/read
POST /forms/pdfengines/metadata/write
```

**Content-Type des Requests:** `multipart/form-data`

---

## 1. Metadaten Lesen

### Route

```
POST /forms/pdfengines/metadata/read
```

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Form-Felder

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `files` | file[] | Ja | PDF-Dateien, deren Metadaten gelesen werden sollen (mehrere erlaubt) |

### Antwort

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/json; charset=UTF-8` | JSON-Objekt mit Dateiname als Schluessel und Metadaten als Wert |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Antwort-Format (Beispiel)

```json
{
  "rechnung.pdf": {
    "PDFVersion": 1.7,
    "Author": "Gotenberg",
    "Title": "Rechnung #001",
    "CreateDate": "2024:03:05 09:15:32Z",
    "ModifyDate": "2024:03:06 10:00:00Z",
    "PageCount": 2,
    "Producer": "Gotenberg",
    "Creator": "Chromium",
    "MIMEType": "application/pdf",
    "Keywords": "rechnung,2024"
  },
  "bericht.pdf": {
    "PDFVersion": 1.4,
    "Author": "Max Mustermann",
    "PageCount": 15
  }
}
```

Rueckgegebene Schluessel entsprechen ExifTool-Tag-Namen.
Referenz: https://exiftool.org/TagNames/PDF.html

### curl-Beispiel

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/read \
  --form files=@/path/to/rechnung.pdf \
  --form files=@/path/to/bericht.pdf
```

---

## 2. Metadaten Schreiben

### Route

```
POST /forms/pdfengines/metadata/write
```

### Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID fuer Log-Identifizierung |

### Form-Felder

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `metadata` | JSON-string | Ja | XMP-Metadaten als JSON-Objekt |
| `files` | file[] | Ja | PDF-Dateien, die aktualisiert werden sollen; mehrere Inputs → ZIP |

### Metadata-JSON-Format

```json
{
  "Author": "Max Mustermann",
  "Title": "Jahresbericht 2024",
  "Subject": "Finanzbericht",
  "Producer": "MeinSystem",
  "Creator": "ReportGenerator",
  "Copyright": "2024 Mein Unternehmen",
  "Keywords": ["bericht", "finanzen", "2024"],
  "CreateDate": "2024:01:01 00:00:00Z"
}
```

Unterstuetzte XMP-Tags: https://exiftool.org/TagNames/XMP.html#pdf

### Antwort

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | Aktualisierte PDF; mehrere Inputs → ZIP-Archiv |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### curl-Beispiele

#### Einfache Metadaten setzen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/dokument.pdf \
  --form 'metadata={"Author":"Max Mustermann","Title":"Jahresbericht"}' \
  -o aktualisiert.pdf
```

#### Vollstaendige Metadaten mit Keywords (Array)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/dokument.pdf \
  --form 'metadata={"Author":"Gotenberg","Producer":"Gotenberg","Keywords":["leitfaden","dokumentation"]}' \
  -o mein.pdf
```

#### Mehrere PDFs gleichzeitig aktualisieren (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/metadata/write \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form 'metadata={"Author":"Muster GmbH","Copyright":"2024"}' \
  -o aktualisiert.zip
```

---

## Hinweise

- Metadaten schreiben bricht typischerweise PDF/A-Konformitaet
- Rueckgegebene Schluessel beim Lesen entsprechen ExifTool-Tag-Namen (nicht immer identisch mit PDF-internen Namen)
- Verwendet ExifTool intern fuer beide Operationen

---

Quelle:
- https://gotenberg.dev/docs/manipulate-pdfs/read-metadata
- https://gotenberg.dev/docs/manipulate-pdfs/write-metadata
