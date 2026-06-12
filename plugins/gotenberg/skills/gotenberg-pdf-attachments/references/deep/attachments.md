# Gotenberg — PDF Anhaenge / Attachments (Vollreferenz)

## Route

```
POST /forms/pdfengines/embed
```

**Content-Type des Requests:** `multipart/form-data`

---

## Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID fuer Log-Identifizierung |

---

## Form-Felder

### Datei-Upload

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `files` | file[] | Ja | PDF-Dateien, in die Inhalte eingebettet werden |
| `embeds` | file[] | Ja | Dateien, die als Anhaenge eingebettet werden sollen (XML, Bilder, etc.) |
| `facturxXml` | file | Bedingt | Factur-X CII-Rechnungs-XML; wird als `factur-x.xml` eingebettet (Dateiname wird ignoriert) |

### Metadaten

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `embedsMetadata` | JSON-string | Nein | — | Pro-Anhang-Metadaten, Schluessel = Dateiname des Anhangs |
| `facturxConformanceLevel` | enum | Bedingt* | — | Konformitaetsstufe fuer Factur-X XMP-Metadaten (*wenn facturxXml angegeben) |
| `facturxDocumentType` | enum | Nein | `INVOICE` | Dokumenttyp fuer Factur-X XMP-Metadaten |
| `facturxVersion` | string | Nein | `1.0` | Factur-X-Version fuer XMP-Metadaten |

---

## embedsMetadata-JSON-Format

```json
{
  "rechnung.xml": {
    "mimeType": "text/xml",
    "relationship": "Alternative"
  },
  "logo.png": {
    "mimeType": "image/png",
    "relationship": "Supplement"
  }
}
```

### AFRelationship-Werte

| Wert | Beschreibung |
|------|-------------|
| `Source` | Quelldokument (unveraenderte Quelle) |
| `Data` | Datendatei (ergaenzende Daten) |
| `Alternative` | Alternatives Format (z.B. XML-Version des PDF-Inhalts) |
| `Supplement` | Ergaenzende Information |
| `Unspecified` | Beziehung nicht definiert |

### facturxConformanceLevel-Werte

| Wert | Beschreibung |
|------|-------------|
| `MINIMUM` | Minimalkonformitaet |
| `BASIC WL` | Basis ohne Zeilenpositionen |
| `BASIC` | Basiskonformitaet |
| `EN 16931` | Europaeischer Standard (Core Invoice Usage Rules) |
| `EXTENDED` | Erweiterte Konformitaet |
| `XRECHNUNG` | Deutsche XRechnung (B2G) |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/pdf` oder `application/zip` | PDF mit eingebetteten Anhaengen; mehrere Inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Antwort-Header bei Erfolg

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl-Beispiele

### XML als Anhang einbetten

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form embeds=@/path/to/rechnung.xml \
  -o mit-anhang.pdf
```

### XML mit Metadaten einbetten

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form embeds=@/path/to/factur-x.xml \
  --form 'embedsMetadata={"factur-x.xml":{"mimeType":"text/xml","relationship":"Alternative"}}' \
  -o mit-anhang.pdf
```

### Factur-X XML (dediziertes Feld)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/rechnung.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### Mehrere Dateien einbetten

```bash
curl --request POST http://localhost:3000/forms/pdfengines/embed \
  --form files=@/path/to/dokument.pdf \
  --form embeds=@/path/to/daten.xml \
  --form embeds=@/path/to/logo.png \
  --form 'embedsMetadata={"daten.xml":{"mimeType":"text/xml","relationship":"Data"},"logo.png":{"mimeType":"image/png","relationship":"Supplement"}}' \
  -o dokument-mit-anhaengen.pdf
```

---

## Hinweise

- Erfordert QPDF als PDF-Engine fuer volle `embedsMetadata`-Unterstuetzung (Standard)
- `facturxXml` wird unabhaengig vom hochgeladenen Dateinamen immer als `factur-x.xml` eingebettet
- Fuer E-Rechnungen (ZUGFeRD/Factur-X) ist PDF/A-3b erforderlich — verwende `POST /forms/pdfengines/factur-x` fuer den vollstaendigen Workflow
- PDF/A-1b und PDF/A-2b unterstuetzen keine Dateianhaenge

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/attachments
