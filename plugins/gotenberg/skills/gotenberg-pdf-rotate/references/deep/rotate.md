# Gotenberg — PDF Seiten drehen (Vollreferenz)

## Route

```
POST /forms/pdfengines/rotate
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

| Feld | Typ | Pflicht | Standard | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------|----------------|--------------|
| `files` | file[] | Ja | — | — | PDF-Dateien, die rotiert werden sollen |
| `rotateAngle` | enum | Ja | — | `90`, `180`, `270` | Rotationswinkel im Uhrzeigersinn (Grad) |
| `rotatePages` | string | Nein | — (alle Seiten) | Seitenbereiche z.B. `1-3`, `5`, `2,4,6` | Zu rotierende Seiten; leer = alle Seiten |

### rotatePages-Syntax

| Beispiel | Bedeutung |
|---------|-----------|
| leer / nicht angegeben | Alle Seiten rotieren |
| `1` | Nur Seite 1 |
| `1-3` | Seiten 1 bis 3 |
| `2,4,6` | Einzelne Seiten 2, 4 und 6 |
| `1-3,5,7-9` | Kombination aus Bereichen und Einzelseiten |

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | Rotierte PDF; mehrere Inputs → ZIP-Archiv |
| `400` | `text/plain; charset=UTF-8` | Ungueltige Form-Felder (z.B. ungueltige rotateAngle) |
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

### Alle Seiten um 90 Grad drehen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/dokument.pdf \
  --form rotateAngle=90 \
  -o rotiert.pdf
```

### Alle Seiten um 180 Grad drehen (umkehren)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/dokument.pdf \
  --form rotateAngle=180 \
  -o umgekehrt.pdf
```

### Nur erste Seite drehen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/dokument.pdf \
  --form rotateAngle=90 \
  --form rotatePages=1 \
  -o teilrotiert.pdf
```

### Seiten 2-4 um 270 Grad drehen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/dokument.pdf \
  --form rotateAngle=270 \
  --form rotatePages=2-4 \
  -o teilrotiert.pdf
```

### Querformat-Seiten korrigieren (Seiten 3, 5, 7)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/dokument.pdf \
  --form rotateAngle=90 \
  --form 'rotatePages=3,5,7' \
  -o korrigiert.pdf
```

### Mehrere PDFs rotieren (→ ZIP)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/rotate \
  --form files=@/path/to/doc1.pdf \
  --form files=@/path/to/doc2.pdf \
  --form rotateAngle=90 \
  -o rotiert.zip
```

---

## Hinweise

- Rotation erfolgt im Uhrzeigersinn
- 270 Grad im Uhrzeigersinn = 90 Grad gegen den Uhrzeigersinn
- Typischer Anwendungsfall: Scan-Korrekturen, Landscape-Seiten-Ausrichtung korrigieren

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/rotate-pdfs
