# Gotenberg — PDF Flatten (Vollreferenz)

## Route

```
POST /forms/pdfengines/flatten
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

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `files` | file[] | Ja | — | PDF-Dateien, die geflattenet werden sollen |

---

## Funktion

Flatten wandelt alle interaktiven Formularfelder (Texteingaben, Checkboxen, Dropdowns, Radiobuttons, Signaturen etc.) in statischen Seiteninhalt um. Das Ergebnis ist eine nicht mehr bearbeitbare PDF, die visuell identisch mit dem ausgefuellten Formular ist.

**Typische Anwendungsfaelle:**
- Ausgefuellte Formulare archivieren
- Signierte PDFs fuer Weitergabe fixieren
- PDFs fuer PDF/A-Konvertierung vorbereiten
- Inhaltsschutz vor unerwuenschter Bearbeitung

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | Geflattente PDF; mehrere Inputs → ZIP-Archiv |
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

## curl-Beispiele

### Einzelne PDF flatten

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --form files=@/path/to/formular.pdf \
  -o geflattenet.pdf
```

### Mehrere PDFs auf einmal flatten (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --form files=@/path/to/formular1.pdf \
  --form files=@/path/to/formular2.pdf \
  -o geflattenet.zip
```

### Mit eigenem Ausgabenamen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/flatten \
  --header 'Gotenberg-Output-Filename: ausgefuelltes-formular' \
  --form files=@/path/to/formular.pdf \
  -o ausgefuelltes-formular.pdf
```

---

## Hinweis zum Unterschied Flatten vs. Encrypt

- **Flatten** macht Formularfelder zu statischem Inhalt — visuell gleich, nicht mehr bearbeitbar
- **Encrypt** schuetzt die gesamte PDF mit Passwort und Berechtigungen — Felder koennen aber noch sichtbar sein
- Fuer maximalen Schutz: zuerst Flatten, dann Encrypt

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/flatten-pdfs
