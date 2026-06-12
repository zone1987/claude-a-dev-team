# Gotenberg — PDF Verschluesselung (Vollreferenz)

## Route

```
POST /forms/pdfengines/encrypt
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

### Datei-Upload

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `files` | file[] | Ja | PDF-Dateien, die verschluesselt werden sollen |

### Passwoerter (mindestens eines erforderlich)

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `userPassword` | string | Bedingt* | — | Passwort, das zum Oeffnen der PDF benoetigt wird (*mindestens userPassword oder ownerPassword) |
| `ownerPassword` | string | Bedingt* | = userPassword | Passwort fuer vollstaendigen Zugriff; hebt alle Berechtigungseinschraenkungen auf |

### Berechtigungen (alle Standard: `true`)

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `allowPrinting` | boolean | Nein | `true` | Drucken des Dokuments erlauben |
| `allowCopying` | boolean | Nein | `true` | Text und Grafiken extrahieren erlauben |
| `allowModifying` | boolean | Nein | `true` | Inhalte veraendern erlauben |
| `allowAnnotating` | boolean | Nein | `true` | Annotationen hinzufuegen/aendern erlauben |
| `allowFillingForms` | boolean | Nein | `true` | Formulare ausfuellen erlauben |
| `allowAssembling` | boolean | Nein | `true` | Seiten einfuegen, loeschen, rotieren erlauben |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | `application/pdf` oder `application/zip` | Verschluesselte PDF; mehrere Inputs → ZIP-Archiv |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder |
| `503` | `text/plain; charset=UTF-8` | Maximale Bearbeitungsdauer ueberschritten |

### Antwort-Header bei Erfolg

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
```

---

## Engine-spezifisches Verhalten

| Engine | Berechtigungs-Granularitaet | Besonderheiten |
|--------|----------------------------|----------------|
| **QPDF** (Standard) | Vollstaendig — jede Berechtigung einzeln steuerbar | Empfohlen fuer fine-grained control |
| **pdfcpu** | Alle oder keine — wenn eine Berechtigung verweigert, alle gesperrt | Vereinfachtes Modell |
| **PDFtk** | Kein Owner-Only-Modus, keine Einzel-Berechtigungen | Eingeschraenkte Unterstuetzung |

**Ab v8.34.0:** Owner-Only-PDFs (nur ownerPassword, kein userPassword) oeffnen sich passwortlos, wenden aber Berechtigungseinschraenkungen an.

---

## curl-Beispiele

### Nur Benutzerpasswort (zum Oeffnen)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/dokument.pdf \
  --form userPassword=geheimesPasswort \
  -o verschluesselt.pdf
```

### Benutzer- und Eigentuemer-Passwort

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/dokument.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  -o verschluesselt.pdf
```

### Nur Lesen erlauben (Kopieren und Bearbeiten sperren)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/dokument.pdf \
  --form userPassword=oeffnen \
  --form ownerPassword=verwalten \
  --form allowCopying=false \
  --form allowModifying=false \
  --form allowAnnotating=false \
  --form allowFillingForms=false \
  --form allowAssembling=false \
  -o nur-lesen.pdf
```

### Nur Drucken sperren

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/dokument.pdf \
  --form userPassword=oeffnen \
  --form allowPrinting=false \
  -o kein-druck.pdf
```

### Owner-Only (passwortlos oeffnen, Berechtigungen eingeschraenkt)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/encrypt \
  --form files=@/path/to/dokument.pdf \
  --form ownerPassword=nurFuerAdmin \
  --form allowCopying=false \
  --form allowModifying=false \
  -o berechtigungen.pdf
```

---

## Hinweise

- Berechtigungseinschraenkungen erfordern mindestens `userPassword` oder `ownerPassword`
- PDF/A und Verschluesselung schliessen sich gegenseitig aus
- QPDF wird empfohlen, wenn individuelle Berechtigungen benoetigt werden
- Fuer vollstaendige Lesesperre empfiehlt sich: Flatten → Encrypt

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/encrypt-pdfs
