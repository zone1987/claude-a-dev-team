# Gotenberg — Markdown to PDF

**Route:** `POST /forms/chromium/convert/markdown`

Converts Markdown (with MathJax support) to PDF via headless Chromium.
Requires an `index.html` template file with a Go template directive
and at least one `.md` file.

## Required template structure

```html
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="utf-8" /><title>My PDF</title></head>
  <body>
    {{ toHTML "file.md" }}
  </body>
</html>
```

## Required files

| Field | Type | Description |
|------|-----|-------------|
| `files` (index.html) | file | HTML template with `{{ toHTML "filename.md" }}` |
| `files` (*.md) | file[] | At least one Markdown file |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.pdf
```

All further fields are identical to the HTML endpoint.
Complete reference: `CHROMIUM-MARKDOWN-DETAIL.md`
