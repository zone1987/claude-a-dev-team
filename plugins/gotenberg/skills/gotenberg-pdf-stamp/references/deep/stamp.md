# Gotenberg — PDF Stempel (Vollreferenz)

## Route

```
POST /forms/pdfengines/stamp
```

**Content-Type des Requests:** `multipart/form-data`

Unterschied zu Wasserzeichen: Ein **Stempel** wird **ueber** dem Seiteninhalt gerendert (Vordergrund). Ein Wasserzeichen wird **hinter** dem Inhalt gerendert (Hintergrund).

---

## Request-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Output-Filename` | string | Nein | zufaellige UUID | Dateiname der Ausgabe |
| `Gotenberg-Trace` | string | Nein | UUID | Eigene Request-ID fuer Log-Identifizierung |

---

## Form-Felder

### Kern

| Feld | Typ | Pflicht | Erlaubte Werte | Beschreibung |
|------|-----|---------|----------------|--------------|
| `files` | file[] | Ja | — | PDF-Dateien, die gestempelt werden sollen |
| `stampSource` | enum | Ja | `text`, `image`, `pdf` | Art des Stempels |
| `stampExpression` | string | Ja | — | Text-String (bei source=text) oder Dateiname der hochgeladenen Stempel-Datei |
| `stamp` | file | Bedingt | — | Bild- oder PDF-Datei als Stempel (erforderlich wenn source=image oder source=pdf) |
| `stampPages` | string | Nein | Seitenbereiche | Seiten, auf die der Stempel angewendet wird; leer = alle |
| `stampOptions` | JSON-string | Nein | — | Engine-spezifische Optionen |

---

## stampOptions-JSON

Die verfuegbaren Optionen haengen von der konfigurierten PDF-Engine ab. Standard-Engine: **pdfcpu**.

### pdfcpu (Standard)

Vollstaendige Dokumentation: https://pdfcpu.io/core/stamp

| Option | Typ | Beispiel | Beschreibung |
|--------|-----|---------|--------------|
| `font` | string | `"Helvetica"` | Schriftfamilie fuer Text-Stempel |
| `points` | integer | `48` | Schriftgroesse in Punkten |
| `color` | string | `"#008000"` | Hex-Farbe oder CSS-Farbname |
| `rotation` | float | `45` | Drehwinkel in Grad |
| `opacity` | float 0-1 | `0.5` | Transparenz (0=unsichtbar, 1=vollstaendig) |
| `scale` | float | `0.5` | Groessenskalierung |
| `offset` | string | `"10 20"` | Versatz X Y in Punkten |
| `pos` | string | `"c"` | Position: `c`=Mitte, `tl`=oben-links, `tr`=oben-rechts, `bl`=unten-links, `br`=unten-rechts |
| `margin` | string | `"20 20"` | Randabstand |
| `mode` | integer | `0` | Stempel-Modus (engine-spezifisch) |

### Beispiel stampOptions

```json
{
  "font": "Helvetica",
  "points": 36,
  "color": "#FF0000",
  "rotation": 0,
  "opacity": 0.8,
  "pos": "tr",
  "offset": "10 10"
}
```

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | PDF mit Stempel; mehrere Inputs → ZIP |
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

### Text-Stempel "GENEHMIGT" (oben rechts)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=GENEHMIGT \
  --form 'stampOptions={"color":"#008000","rotation":0,"opacity":0.8,"pos":"tr"}' \
  -o genehmigt.pdf
```

### Text-Stempel "VERTRAULICH" (diagonal, halbopak)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=VERTRAULICH \
  --form 'stampOptions={"font":"Helvetica","points":48,"color":"#FF0000","rotation":45,"opacity":0.5}' \
  -o vertraulich.pdf
```

### Bild-Stempel (z.B. Logo)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stamp=@/path/to/logo.png \
  --form stampSource=image \
  --form stampExpression=logo.png \
  --form 'stampOptions={"scale":0.3,"pos":"br","opacity":1}' \
  -o mit-logo.pdf
```

### PDF-Stempel

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stamp=@/path/to/stempel.pdf \
  --form stampSource=pdf \
  --form stampExpression=stempel.pdf \
  -o gestempelt.pdf
```

### Nur erste Seite stempeln

```bash
curl --request POST http://localhost:3000/forms/pdfengines/stamp \
  --form files=@/path/to/dokument.pdf \
  --form stampSource=text \
  --form stampExpression=ORIGINAL \
  --form stampPages=1 \
  -o gestempelt.pdf
```

---

## Hinweise

- Stempel rendert im **Vordergrund** (ueber dem Inhalt) — anders als Wasserzeichen
- Bei `stampSource=image` oder `stampSource=pdf` muss die Datei auch als `stamp`-Feld hochgeladen werden
- `stampExpression` muss beim image/pdf-Modus dem Dateinamen des `stamp`-Feldes entsprechen
- Engine-Optionen sind Engine-spezifisch; bei Wechsel der PDF-Engine (pdfcpu → PDFtk etc.) koennen Optionen abweichen

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/stamp-pdfs
