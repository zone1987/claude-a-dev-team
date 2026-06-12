# Gotenberg — Screenshots (Vollreferenz)

## Routen

| Route | Input-Typ |
|-------|-----------|
| `POST /forms/chromium/screenshot/url` | URL (`url`-Feld) |
| `POST /forms/chromium/screenshot/html` | `index.html`-Datei |
| `POST /forms/chromium/screenshot/markdown` | `index.html`-Template + `.md`-Dateien |

## Basisbeispiele

```bash
# URL-Screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/url \
  --form url=https://my.url \
  -o my.png

# HTML-Screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/html \
  --form files=@/path/to/index.html \
  -o my.png

# Markdown-Screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.png
```

## Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Ausgabe-Dateiname (ohne Extension) |
| `Gotenberg-Trace` | string | Random UUID | Request-ID fuer Logs |

## Pflichtfelder je Route

### /screenshot/url

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `url` | string | Ja | URL der Zielseite. `file://`-URLs geben 400 zurueck. |

### /screenshot/html

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `files` (index.html) | file | Ja | HTML-Datei (muss `index.html` heissen) |

### /screenshot/markdown

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|-------------|
| `files` (index.html) | file | Ja | HTML-Template mit `{{ toHTML "datei.md" }}` |
| `files` (*.md) | file[] | Ja | Mindestens eine Markdown-Datei |

## Screenshot-Rendering-Felder

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `width` | number | `800` | Viewport-Breite in Pixel |
| `height` | number | `600` | Viewport-Hoehe in Pixel |
| `clip` | boolean | `false` | Screenshot auf Viewport beschneiden. Ohne Clip: volle Seitenhoehe. |
| `deviceScaleFactor` | number | `1` | Pixel-Dichte. `2` = Retina/HiDPI-Qualitaet. |
| `format` | enum | `png` | Ausgabeformat: `png`, `jpeg`, `webp` |
| `quality` | number | `100` | Kompressionsqualitaet 0-100 (nur bei `format=jpeg`) |
| `omitBackground` | boolean | `false` | Standard-Weisshintergrund ausblenden (Transparenz moeglich) |
| `optimizeForSpeed` | boolean | `false` | Bild-Encoding fuer Geschwindigkeit statt Dateigroesse optimieren |

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/html \
  --form files=@/path/to/index.html \
  --form width=1280 \
  --form height=720 \
  --form clip=true \
  --form format=jpeg \
  --form quality=85 \
  --form deviceScaleFactor=2 \
  --form optimizeForSpeed=true \
  -o my.jpeg
```

## Viewport & Layout-Hinweise

- Ohne `clip=true` erfasst Chromium die volle Seitenhoehe (hoehe des Inhalts)
- Mit `clip=true` wird genau auf `width` x `height` beschnitten
- `deviceScaleFactor=2` verdoppelt die Aufloesung (gut fuer Retina-Displays)
- Viewport-Abmessungen mit `width`/`height` entsprechend setzen

## Gemeinsame Felder mit PDF-Konvertierung

Die folgenden Felder funktionieren auch bei Screenshots:

### JavaScript & Warten

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Feste Wartezeit vor Screenshot |
| `waitForExpression` | string | — | JS-Ausdruck abwarten |
| `waitForSelector` | string | — | CSS-Selektor abwarten |

### Netzwerk

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie-Array |
| `extraHttpHeaders` | json | — | Zusaetzliche HTTP-Header |
| `userAgent` | string | — | User-Agent |
| `failOnHttpStatusCodes` | json | `[499,599]` | Fehler bei Status-Codes |
| `failOnResourceHttpStatusCodes` | json | — | Fehler bei Asset-Status-Codes |
| `ignoreResourceHttpStatusDomains` | json | — | Ausnahme-Domains |
| `skipNetworkIdleEvent` | boolean | `true` | Nicht auf Netzwerk-Idle warten |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Nicht auf Fast-Idle warten |
| `failOnResourceLoadingFailed` | boolean | `false` | Fehler bei Asset-Ladefehler |
| `failOnConsoleExceptions` | boolean | `false` | Fehler bei JS-Exceptions |

### Druckmedien

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `screen` | `screen` oder `print` (Screenshots nutzen `screen` als Default) |
| `emulatedMediaFeatures` | json | — | CSS-Media-Feature-Overrides |

## Response-Codes

| Code | Bedeutung |
|------|-----------|
| 200 | Erfolg — Bilddatei im Body |
| 400 | Ungueltige Felder / Netzwerkfehler |
| 403 | URL verboten (nur URL-Route) |
| 409 | Status-Code-Fehler / Console-Exception |
| 503 | Timeout |

## Gesamtzahl Form-Felder: ~22

Screenshot-spezifisch (8) + Warten (3) + Netzwerk (10) + Medien (2) = ~23 Felder

---
Quellen:
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-url
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-html
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-markdown
