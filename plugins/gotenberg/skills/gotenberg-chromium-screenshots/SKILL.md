---
name: gotenberg-chromium-screenshots
description: >
  Gotenberg Screenshots — HTML, URL und Markdown als PNG/JPEG/WebP erfassen.
  Alle Form-Felder: width, height, clip, format, quality, deviceScaleFactor, omitBackground, optimizeForSpeed.
  Trigger: "Gotenberg Screenshot", "Gotenberg screenshot HTML", "Gotenberg screenshot URL",
  "Gotenberg screenshot markdown", "Gotenberg PNG", "Gotenberg JPEG screenshot",
  "Gotenberg WebP", "Gotenberg capture image", "Gotenberg screenshot form fields".
---

# Gotenberg — Screenshots

Drei Routen fuer Screenshots via Headless Chromium:

| Route | Input |
|-------|-------|
| `POST /forms/chromium/screenshot/url` | URL der Webseite |
| `POST /forms/chromium/screenshot/html` | `index.html` Datei |
| `POST /forms/chromium/screenshot/markdown` | `index.html` + `.md` Dateien |

## Screenshot-spezifische Felder

| Feld | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `width` | number | `800` | Viewport-Breite in Pixel |
| `height` | number | `600` | Viewport-Hoehe in Pixel |
| `clip` | boolean | `false` | Screenshot auf Viewport-Abmessungen beschneiden |
| `deviceScaleFactor` | number | `1` | Pixel-Dichte (2 = Retina-Qualitaet) |
| `format` | enum | `png` | Bildformat: `png`, `jpeg`, `webp` |
| `quality` | number | `100` | Kompressionsqualitaet 0-100 (nur bei `jpeg`) |
| `omitBackground` | boolean | `false` | Weisshintergrund ausblenden |
| `optimizeForSpeed` | boolean | `false` | Encoding fuer Geschwindigkeit optimieren |

Vollstaendige Referenz: `references/deep/chromium-screenshots.md`
