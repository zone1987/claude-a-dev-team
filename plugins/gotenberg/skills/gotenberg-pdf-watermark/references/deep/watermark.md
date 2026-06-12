# Gotenberg — PDF Wasserzeichen (Vollreferenz)

## Route

```
POST /forms/pdfengines/watermark
```

**Content-Type des Requests:** `multipart/form-data`

Unterschied zum Stempel: Ein **Wasserzeichen** wird **hinter** dem Seiteninhalt gerendert (Hintergrund). Ein Stempel wird **ueber** dem Inhalt gerendert (Vordergrund).

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
| `files` | file[] | Ja | — | PDF-Dateien, die ein Wasserzeichen erhalten |
| `watermarkSource` | enum | Ja | `text`, `image`, `pdf` | Art des Wasserzeichens |
| `watermarkExpression` | string | Ja | — | Text-String (bei source=text) oder Dateiname der hochgeladenen Wasserzeichen-Datei |
| `watermark` | file | Bedingt | — | Bild- oder PDF-Datei als Wasserzeichen (erforderlich wenn source=image oder source=pdf) |
| `watermarkPages` | string | Nein | Seitenbereiche | Seiten, auf die das Wasserzeichen angewendet wird; leer = alle |
| `watermarkOptions` | JSON-string | Nein | — | Engine-spezifische Optionen |

---

## watermarkOptions-JSON

Die verfuegbaren Optionen haengen von der konfigurierten PDF-Engine ab. Standard-Engine: **pdfcpu**.

### pdfcpu (Standard)

Vollstaendige Dokumentation: https://pdfcpu.io/core/watermark

| Option | Typ | Beispiel | Beschreibung |
|--------|-----|---------|--------------|
| `font` | string | `"Helvetica"` | Schriftfamilie fuer Text-Wasserzeichen |
| `points` | integer | `48` | Schriftgroesse in Punkten |
| `color` | string | `"#808080"` | Hex-Farbe (Grau empfohlen fuer Wasserzeichen) |
| `rotation` | float | `45` | Drehwinkel in Grad |
| `opacity` | float 0-1 | `0.15` | Transparenz (typisch: 0.1-0.3 fuer Wasserzeichen) |
| `scale` | float | `0.5` | Groessenskalierung |
| `offset` | string | `"0 0"` | Versatz X Y in Punkten |
| `pos` | string | `"c"` | Position: `c`=Mitte, `tl`, `tr`, `bl`, `br` |
| `margin` | string | `"20 20"` | Randabstand |

### Beispiel watermarkOptions (klassisches Wasserzeichen)

```json
{
  "font": "Helvetica",
  "points": 48,
  "color": "#808080",
  "rotation": 45,
  "opacity": 0.15
}
```

---

## Antwort-Codes

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | variabel | PDF mit Wasserzeichen; mehrere Inputs → ZIP |
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

### Text-Wasserzeichen "VERTRAULICH" (klassisch diagonal)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=VERTRAULICH \
  --form 'watermarkOptions={"opacity":0.25,"rotation":45}' \
  -o mit-wasserzeichen.pdf
```

### Text-Wasserzeichen grau-transparent

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=ENTWURF \
  --form 'watermarkOptions={"font":"Helvetica","points":48,"color":"#808080","rotation":45,"opacity":0.15}' \
  -o entwurf.pdf
```

### Bild-Wasserzeichen (Logo als Hintergrund)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermark=@/path/to/logo.png \
  --form watermarkSource=image \
  --form watermarkExpression=logo.png \
  --form 'watermarkOptions={"opacity":0.1,"scale":0.5}' \
  -o mit-logo-wm.pdf
```

### PDF-Wasserzeichen (PDF als Overlay-Hintergrund)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermark=@/path/to/hintergrund.pdf \
  --form watermarkSource=pdf \
  --form watermarkExpression=hintergrund.pdf \
  -o mit-hintergrund.pdf
```

### Nur bestimmte Seiten mit Wasserzeichen

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=text \
  --form watermarkExpression=KOPIE \
  --form watermarkPages=1-3 \
  --form 'watermarkOptions={"opacity":0.2,"rotation":45}' \
  -o teilweise.pdf
```

---

## Vergleich Wasserzeichen vs. Stempel

| Eigenschaft | Wasserzeichen (watermark) | Stempel (stamp) |
|------------|--------------------------|-----------------|
| Position im PDF | Hinter dem Inhalt (Hintergrund) | Ueber dem Inhalt (Vordergrund) |
| Typische Opazitaet | 0.1 - 0.3 | 0.5 - 1.0 |
| Typischer Einsatz | VERTRAULICH-Hinweis, Entwurfsmarkierung | GENEHMIGT-Stempel, Logo |
| Route | `/forms/pdfengines/watermark` | `/forms/pdfengines/stamp` |

---

Quelle: https://gotenberg.dev/docs/manipulate-pdfs/watermark-pdfs
