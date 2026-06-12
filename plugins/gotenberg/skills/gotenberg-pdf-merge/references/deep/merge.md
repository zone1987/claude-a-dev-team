# Gotenberg — PDF Merge (Vollreferenz)

## Route

```
POST /forms/pdfengines/merge
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

### Kern

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `files` | file[] | Ja | — | PDF-Dateien zum Zusammenfuehren; werden in alphanumerischer Reihenfolge der Dateinamen zusammengefuegt |

### Metadaten

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `metadata` | JSON-string | Nein | — | XMP-Metadaten als JSON-Objekt (z.B. `{"Author":"Max","Title":"Rechnung"}`) |

### Lesezeichen

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `bookmarks` | JSON-string | Nein | — | Lesezeichen als Liste oder Dateiname-Map |
| `autoIndexBookmarks` | boolean | Nein | `false` | Extrahiert vorhandene Lesezeichen und verschiebt ihre Seiten-Offsets automatisch |

### Anhaenge (Embeds)

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `embeds` | file[] | Nein | — | Dateien, die als Anhaenge in den PDF-Container eingebettet werden |
| `embedsMetadata` | JSON-string | Nein | — | Pro-Anhang-Metadaten, Schluessel = Dateiname; Felder: `mimeType`, `relationship` (`Source`, `Data`, `Alternative`, `Supplement`, `Unspecified`) |

### Factur-X

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `facturxXml` | file | Nein | — | — | CII-Rechnungs-XML; wird als `factur-x.xml` eingebettet |
| `facturxConformanceLevel` | enum | Bedingt* | — | `MINIMUM`, `BASIC WL`, `BASIC`, `EN 16931`, `EXTENDED`, `XRECHNUNG` | Konformitaetsstufe in XMP-Metadaten (*wenn facturxXml angegeben) |
| `facturxDocumentType` | enum | Nein | `INVOICE` | `INVOICE`, `ORDER`, `ORDER_RESPONSE`, `ORDER_CHANGE` | Dokumenttyp in XMP-Metadaten |
| `facturxVersion` | string | Nein | `1.0` | — | Factur-X-Version in XMP-Metadaten |

### Flatten

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `flatten` | boolean | Nein | `false` | Wandelt Formularfelder in statischen Seiteninhalt um |

### Wasserzeichen

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `watermarkSource` | enum | Bedingt | — | `text`, `image`, `pdf` | Art des Wasserzeichens |
| `watermarkExpression` | string | Bedingt | — | — | Text-String oder hochgeladener Dateiname |
| `watermarkPages` | string | Nein | — (alle) | Seitenbereiche z.B. `1-3,5` | Seiten, auf die das Wasserzeichen angewendet wird |
| `watermarkOptions` | JSON-string | Nein | — | — | Engine-Optionen (font, color, rotation, opacity, scale, offset) |
| `watermark` | file | Bedingt | — | — | Bild/PDF-Datei (fuer source=image oder pdf) |

### Stempel

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `stampSource` | enum | Bedingt | — | `text`, `image`, `pdf` | Art des Stempels |
| `stampExpression` | string | Bedingt | — | — | Text-String oder hochgeladener Dateiname |
| `stampPages` | string | Nein | — (alle) | Seitenbereiche z.B. `1-3,5` | Seiten, auf die der Stempel angewendet wird |
| `stampOptions` | JSON-string | Nein | — | — | Engine-Optionen (font, color, rotation, opacity, scale, offset) |
| `stamp` | file | Bedingt | — | — | Bild/PDF-Datei (fuer source=image oder pdf) |

### Rotation

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `rotateAngle` | enum | Bedingt | — | `90`, `180`, `270` | Rotationswinkel in Grad |
| `rotatePages` | string | Nein | — (alle) | Seitenbereiche | Seiten, die rotiert werden |

### PDF/A & PDF/UA

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `pdfa` | enum | Nein | — | `PDF/A-1b`, `PDF/A-2b`, `PDF/A-3b` | Konvertierung in Archivstandard |
| `pdfua` | boolean | Nein | `false` | — | Barrierefreiheit (Universal Accessibility) aktivieren |

### Verschluesselung

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `userPassword` | string | Nein | — | Passwort zum Oeffnen der PDF |
| `ownerPassword` | string | Nein | = userPassword | Vollzugriff-Passwort; hebt Berechtigungseinschraenkungen auf |
| `allowPrinting` | boolean | Nein | `true` | Drucken erlauben |
| `allowCopying` | boolean | Nein | `true` | Text- und Grafikextraktion erlauben |
| `allowModifying` | boolean | Nein | `true` | Inhaltsaenderungen erlauben |
| `allowAnnotating` | boolean | Nein | `true` | Annotationen erlauben |
| `allowFillingForms` | boolean | Nein | `true` | Formularausfuellung erlauben |
| `allowAssembling` | boolean | Nein | `true` | Seiten einfuegen/loeschen/rotieren erlauben |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/pdf` | Zusammengefuehrte PDF; Headers: `Content-Disposition`, `Content-Type`, `Content-Length`, `Gotenberg-Trace` |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder; Detail im Body + `Gotenberg-Trace` |
| `503` | `text/plain; charset=UTF-8` | Maximale Bearbeitungsdauer ueberschritten |

---

## curl-Beispiele

### Einfaches Zusammenfuehren (alphanumerische Reihenfolge)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/01_deckblatt.pdf \
  --form files=@/path/to/02_inhalt.pdf \
  --form files=@/path/to/03_anhang.pdf \
  -o zusammengefuehrt.pdf
```

### Mit Metadaten

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form 'metadata={"Author":"Max Mustermann","Title":"Jahresbericht 2024","Keywords":["bericht","2024"]}' \
  -o mein.pdf
```

### Mit Verschluesselung

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  --form allowCopying=false \
  --form allowModifying=false \
  -o verschluesselt.pdf
```

### Mit Wasserzeichen (Text)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=VERTRAULICH \
  --form 'watermarkOptions={"opacity":0.25,"rotation":45,"color":"#808080"}' \
  -o mit-wasserzeichen.pdf
```

### Mit Factur-X

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/rechnung.pdf \
  --form facturxXml=@/path/to/rechnung.xml \
  --form 'facturxConformanceLevel=EN 16931' \
  -o e-rechnung.pdf
```

### Mit PDF/A-Konvertierung + auto-Lesezeichen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  --form pdfa=PDF/A-3b \
  --form autoIndexBookmarks=true \
  -o archiv.pdf
```

### Mit eigenem Output-Dateinamen und Trace

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Output-Filename: jahresbericht-2024' \
  --header 'Gotenberg-Trace: mein-trace-123' \
  --form files=@/path/to/1_pdf.pdf \
  --form files=@/path/to/2_pdf.pdf \
  -o jahresbericht-2024.pdf
```

---

## Hinweise

- Die Dateien werden in **alphanumerischer Reihenfolge** ihrer Dateinamen zusammengefuehrt — Dateinamen entsprechend benennen (01_, 02_, ...)
- `autoIndexBookmarks=true` extrahiert vorhandene Lesezeichen und passt die Seiten-Offsets an
- PDF/A und Verschluesselung schliessen sich gegenseitig aus
- PDF/A-1b und PDF/A-2b unterstuetzen keine Dateianhaenge; fuer Anhaenge PDF/A-3b verwenden
- Wasserzeichen = hinter dem Inhalt; Stempel = ueber dem Inhalt

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/merge-pdfs
