# Gotenberg — PDF Split (Vollreferenz)

## Route

```
POST /forms/pdfengines/split
```

**Content-Type des Requests:** `multipart/form-data`

---

## Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe; Erweiterung wird automatisch angehaengt |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID fuer Log-Identifizierung |

---

## Form-Felder (Kern)

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `files` | file[] | Ja | — | — | PDF-Dateien zum Aufteilen |
| `splitMode` | enum | Ja | — | `intervals`, `pages` | Aktiviert den Split-Engine und legt den Modus fest |
| `splitSpan` | string | Ja | — | — | Regel: Chunk-Groesse fuer `intervals` (z.B. `2`) oder Seitenbereiche fuer `pages` (z.B. `1-3`) |
| `splitUnify` | boolean | Nein | `false` | `true`, `false` | Nur `pages`-Modus: kombiniert extrahierte Seiten zu einer einzigen PDF |

### splitMode-Details

**`intervals`-Modus:**
- `splitSpan=1` → jede Seite wird einzelne PDF
- `splitSpan=2` → je 2 Seiten zusammen
- `splitSpan=3` → je 3 Seiten zusammen
- Ergebnis immer ZIP-Archiv

**`pages`-Modus:**
- `splitSpan=1-3` → Seiten 1-3 extrahieren
- `splitSpan=2,4,6` → einzelne Seiten extrahieren
- Mit `splitUnify=true` → eine einzelne PDF; ohne → ZIP mit einzelnen PDFs pro Bereich

---

## Form-Felder (Metadaten & Struktur)

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `metadata` | JSON-string | Nein | — | XMP-Metadaten fuer die Ausgabe-PDFs |
| `embeds` | file[] | Nein | — | Dateien, die als Anhaenge eingebettet werden |
| `embedsMetadata` | JSON-string | Nein | — | Pro-Anhang-Metadaten: `mimeType`, `relationship` |
| `facturxXml` | file | Nein | — | CII-Rechnungs-XML (als `factur-x.xml` eingebettet) |
| `facturxConformanceLevel` | enum | Bedingt | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` |
| `facturxDocumentType` | enum | Nein | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` |
| `facturxVersion` | string | Nein | `1.0` | Factur-X-Version |
| `flatten` | boolean | Nein | `false` | Formularfelder in Seiteninhalt umwandeln |

---

## Form-Felder (Wasserzeichen)

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `watermarkSource` | enum | Bedingt | — | `text`, `image`, `pdf` | Art des Wasserzeichens |
| `watermarkExpression` | string | Bedingt | — | — | Text-String oder hochgeladener Dateiname |
| `watermarkPages` | string | Nein | — (alle) | Seitenbereiche | Zielseiten |
| `watermarkOptions` | JSON-string | Nein | — | — | Engine-Optionen: `font`, `points`, `color`, `rotation`, `opacity`, `scale`, `offset` |
| `watermark` | file | Bedingt | — | — | Bild/PDF fuer source=image/pdf |

---

## Form-Felder (Stempel)

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `stampSource` | enum | Bedingt | — | `text`, `image`, `pdf` | Art des Stempels |
| `stampExpression` | string | Bedingt | — | — | Text-String oder hochgeladener Dateiname |
| `stampPages` | string | Nein | — (alle) | Seitenbereiche | Zielseiten |
| `stampOptions` | JSON-string | Nein | — | — | Engine-Optionen: `font`, `points`, `color`, `rotation`, `opacity`, `scale`, `offset` |
| `stamp` | file | Bedingt | — | — | Bild/PDF fuer source=image/pdf |

---

## Form-Felder (Rotation)

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `rotateAngle` | enum | Bedingt | — | `90`, `180`, `270` | Rotationswinkel |
| `rotatePages` | string | Nein | — (alle) | Seitenbereiche | Zu rotierende Seiten |

---

## Form-Felder (Konformitaet)

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `pdfa` | enum | Nein | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Archivstandard-Konvertierung |
| `pdfua` | boolean | Nein | `false` | — | PDF/UA-Barrierefreiheit aktivieren |

---

## Form-Felder (Verschluesselung)

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `userPassword` | string | Nein | — | Passwort zum Oeffnen |
| `ownerPassword` | string | Nein | = userPassword | Vollzugriff-Passwort |
| `allowPrinting` | boolean | Nein | `true` | Drucken erlauben |
| `allowCopying` | boolean | Nein | `true` | Kopieren erlauben |
| `allowModifying` | boolean | Nein | `true` | Bearbeiten erlauben |
| `allowAnnotating` | boolean | Nein | `true` | Annotieren erlauben |
| `allowFillingForms` | boolean | Nein | `true` | Formulare ausfuellen erlauben |
| `allowAssembling` | boolean | Nein | `true` | Seitenverwaltung erlauben |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/zip` oder `application/pdf` | ZIP bei mehreren Outputs; einzelne PDF wenn `pages`+`splitUnify=true` |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Maximale Bearbeitungsdauer ueberschritten |

---

## curl-Beispiele

### Jede Seite als eigene PDF (intervals=1)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/dokument.pdf \
  --form splitMode=intervals \
  --form splitSpan=1 \
  -o seiten.zip
```

### Je 3 Seiten zusammen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/dokument.pdf \
  --form splitMode=intervals \
  --form splitSpan=3 \
  -o chunks.zip
```

### Seiten 1-3 extrahieren (als einzelne PDF)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/dokument.pdf \
  --form splitMode=pages \
  --form splitSpan=1-3 \
  --form splitUnify=true \
  -o auszug.pdf
```

### Seiten 2, 5 und 7 extrahieren (separate PDFs im ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/dokument.pdf \
  --form splitMode=pages \
  --form 'splitSpan=2,5,7' \
  -o auswahl.zip
```

### Split mit Verschluesselung

```bash
curl --request POST http://localhost:3000/forms/pdfengines/split \
  --form files=@/path/to/dokument.pdf \
  --form splitMode=intervals \
  --form splitSpan=1 \
  --form userPassword=geheim \
  --form allowCopying=false \
  -o verschluesselt.zip
```

---

## Hinweise

- Engine-Syntax fuer `splitSpan` abhaengig von der konfigurierten PDF-Engine (pdfcpu, QPDF, PDFtk)
- PDF/A und Verschluesselung schliessen sich gegenseitig aus
- PDF/A-1b und PDF/A-2b unterstuetzen keine Dateianhaenge; fuer Anhaenge PDF/A-3b verwenden
- Wasserzeichen = hinter dem Inhalt; Stempel = ueber dem Inhalt
- `splitUnify=true` funktioniert nur im `pages`-Modus

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/split-pdfs
