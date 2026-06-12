# Gotenberg — PDF/A & PDF/UA Konvertierung (Vollreferenz)

## Route

```
POST /forms/pdfengines/convert
```

**Content-Type des Requests:** `multipart/form-data`

---

## Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe; Erweiterung wird automatisch angehaengt |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID fuer Log-Identifizierung |

---

## Form-Felder

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `files` | file[] | Ja | — | — | PDF-Dateien, die konvertiert werden sollen |
| `pdfa` | enum | Bedingt* | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Zielarchivstandard (*mindestens eines von pdfa oder pdfua erforderlich) |
| `pdfua` | boolean | Bedingt* | `false` | `true`, `false` | PDF/UA (Universal Accessibility) aktivieren |

---

## PDF/A-Standard-Uebersicht

| Standard | Beschreibung | Anhaenge erlaubt |
|----------|-------------|-----------------|
| `PDF/A-1b` | ISO 19005-1 — visuelle Darstellung erhalten | Nein |
| `PDF/A-2b` | ISO 19005-2 — verbesserte Kompression | Nein |
| `PDF/A-3b` | ISO 19005-3 — beliebige Dateianhaenge erlaubt | Ja |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/pdf` | Konvertierte PDF; mehrere Inputs → ZIP-Archiv |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Maximale Bearbeitungsdauer ueberschritten |

Alle Antworten enthalten: `Content-Disposition`, `Content-Type`, `Content-Length`, `Gotenberg-Trace`

---

## curl-Beispiele

### In PDF/A-1b konvertieren

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-1b \
  -o archiv.pdf
```

### In PDF/A-2b konvertieren

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-2b \
  -o archiv.pdf
```

### In PDF/A-3b konvertieren (mit Anhang-Unterstuetzung)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-3b \
  -o archiv.pdf
```

### PDF/UA-Barrierefreiheit aktivieren

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfua=true \
  -o barrierefrei.pdf
```

### Kombination PDF/A-3b + PDF/UA

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/dokument.pdf \
  --form pdfa=PDF/A-3b \
  --form pdfua=true \
  -o archiv-barrierefrei.pdf
```

### Mehrere Dateien auf einmal (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/convert \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form pdfa=PDF/A-2b \
  -o konvertiert.zip
```

---

## Hinweise

- Diese Operation erfordert LibreOffice-Neuverarbeitung der Dokumente — rechenintensiver als Merge/Split
- PDF/A und Verschluesselung schliessen sich gegenseitig aus (Verschluesselung bricht PDF/A-Konformitaet)
- Metadaten schreiben bricht typischerweise PDF/A-Konformitaet
- Fuer E-Rechnungen mit Anhang ist PDF/A-3b erforderlich (ZUGFeRD/Factur-X)
- Die Konvertierung kann bei komplexen Dokumenten erheblich laenger dauern

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/pdfa-pdfua
