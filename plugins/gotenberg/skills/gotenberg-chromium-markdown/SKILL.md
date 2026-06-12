---
name: gotenberg-chromium-markdown
description: >
  Gotenberg Markdown zu PDF — index.html Template, .md Dateien, MathJax, Assets.
  Trigger: "Markdown zu PDF Gotenberg", "Markdown to PDF Gotenberg",
  "Gotenberg convert Markdown", "Gotenberg markdown template", "Gotenberg .md PDF",
  "Gotenberg toHTML template", "Gotenberg MathJax PDF", "Gotenberg markdown form fields".
---

# Gotenberg — Markdown zu PDF

**Route:** `POST /forms/chromium/convert/markdown`

Konvertiert Markdown (mit MathJax-Unterstuetzung) zu PDF via Headless Chromium.
Benoetigt eine `index.html`-Template-Datei mit Go-Template-Direktive
und mindestens eine `.md`-Datei.

## Template-Pflichtstruktur

```html
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="utf-8" /><title>My PDF</title></head>
  <body>
    {{ toHTML "file.md" }}
  </body>
</html>
```

## Pflicht-Files

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `files` (index.html) | file | HTML-Template mit `{{ toHTML "dateiname.md" }}` |
| `files` (*.md) | file[] | Mindestens eine Markdown-Datei |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.pdf
```

Alle weiteren Felder identisch mit HTML-Endpunkt.
Vollstaendige Referenz: `references/deep/chromium-markdown.md`
