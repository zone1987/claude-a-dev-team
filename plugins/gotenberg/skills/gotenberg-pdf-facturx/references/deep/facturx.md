# Gotenberg — Factur-X / ZUGFeRD E-Rechnung (Vollreferenz)

## Route

```
POST /forms/pdfengines/factur-x
```

**Content-Type des Requests:** `multipart/form-data`

---

## Was ist Factur-X?

Factur-X (in Deutschland auch ZUGFeRD) ist ein Standard fuer elektronische Rechnungen (E-Invoicing), der ein PDF mit einer eingebetteten maschinenlesbaren XML-Datei verbindet. Der Standard basiert auf CII (Cross Industry Invoice) und ist nach EN 16931 genormt.

Gotenberg transformiert eine normale PDF in eine konforme E-Rechnung durch:
1. Einbetten der CII-XML als `factur-x.xml` mit `AFRelationship=Alternative`
2. Injizieren von XMP-Metadaten (Konformitaetsstufe, Dokumenttyp, Version)
3. Konvertierung in PDF/A-3 (Standard: PDF/A-3b)

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
| `files` | file[] | Ja | PDF-Rechnungsdokumente |
| `facturxXml` | file | Ja | CII-Rechnungs-XML; wird als `factur-x.xml` eingebettet (hochgeladener Dateiname wird ignoriert) |

### Factur-X-Konfiguration

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `facturxConformanceLevel` | enum | Ja | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` | Konformitaetsstufe in XMP-Metadaten |
| `facturxDocumentType` | enum | Nein | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` | Dokumenttyp in XMP-Metadaten |
| `facturxVersion` | string | Nein | `1.0` | beliebiger Versionsstring | Factur-X-Version in XMP-Metadaten |

### PDF/A-Konfiguration

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `pdfa` | enum | Nein | `PDF/A-3b` | `PDF/A-3a`, `PDF/A-3b`, `PDF/A-3u` | PDF/A-3-Variante (nur PDF/A-3 erlaubt Dateianhaenge) |
| `pdfua` | boolean | Nein | `false` | `true`, `false` | PDF/UA-Barrierefreiheit aktivieren |

---

## Konformitaetsstufen-Uebersicht

| Stufe | Beschreibung | Pflichtfelder |
|-------|-------------|---------------|
| `MINIMUM` | Nur Zahlungsinformationen | Sehr wenige |
| `BASIC WL` | Basis ohne Zeilenpositionen | Rechnungsheader |
| `BASIC` | Basiskonformitaet mit Positionen | Standard-Rechnungsfelder |
| `EN 16931` | Europaeischer Kernstandard (Core Invoice) | Vollstaendige Rechnungsdaten |
| `EXTENDED` | Erweiterte Konformitaet | + optionale Felder |
| `XRECHNUNG` | Deutsche B2G-E-Rechnung | XRechnung-Pflichtfelder |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/pdf` | PDF/A-3-konforme E-Rechnung; mehrere Inputs → ZIP |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Timeout |

### Antwort-Header bei Erfolg

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: application/pdf
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## curl-Beispiele

### Standard Factur-X EN 16931

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/cii-rechnung.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### XRechnung (deutsche B2G-Pflichtform)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/xrechnung.xml \
  --form facturxConformanceLevel=XRECHNUNG \
  -o xrechnung.pdf
```

### Minimale Konformitaet (Zahlungsinformationen)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/minimum.xml \
  --form facturxConformanceLevel=MINIMUM \
  -o e-rechnung-minimal.pdf
```

### Mit PDF/A-3a und PDF/UA

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/cii.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  --form pdfa=PDF/A-3a \
  --form pdfua=true \
  -o e-rechnung-barrierefrei.pdf
```

### Bestellung (ORDER-Dokumenttyp)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/factur-x \
  --form files=@/path/to/bestellung.pdf \
  --form facturxXml=@/path/to/bestellung.xml \
  --form facturxConformanceLevel=EXTENDED \
  --form facturxDocumentType=ORDER \
  -o e-bestellung.pdf
```

---

## Hinweise

- Nur PDF/A-3 unterstuetzt Dateianhaenge; PDF/A-1 und PDF/A-2 sind hier nicht verfuegbar
- Der Dateiname der `facturxXml`-Datei wird ignoriert; sie wird immer als `factur-x.xml` eingebettet
- Fuer einfaches Einbetten ohne automatische PDF/A-Konvertierung → `POST /forms/pdfengines/embed` verwenden
- Die XRechnung-Konformitaet ist fuer deutsche oeffentliche Auftraggeber (B2G) vorgeschrieben (ab 2020)
- ZUGFeRD und Factur-X sind interoperabel (gleicher technischer Standard, verschiedene Branding-Namen)

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/factur-x
