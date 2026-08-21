# Gotenberg — Screenshots

Three routes for screenshots via headless Chromium:

| Route | Input |
|-------|-------|
| `POST /forms/chromium/screenshot/url` | URL of the web page |
| `POST /forms/chromium/screenshot/html` | `index.html` file |
| `POST /forms/chromium/screenshot/markdown` | `index.html` + `.md` files |

## Screenshot-specific fields

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `width` | number | `800` | Viewport width in pixels |
| `height` | number | `600` | Viewport height in pixels |
| `clip` | boolean | `false` | Clip the screenshot to the viewport dimensions |
| `deviceScaleFactor` | number | `1` | Pixel density (2 = retina quality) |
| `format` | enum | `png` | Image format: `png`, `jpeg`, `webp` |
| `quality` | number | `100` | Compression quality 0-100 (only with `jpeg`) |
| `omitBackground` | boolean | `false` | Hide the white background |
| `optimizeForSpeed` | boolean | `false` | Optimize encoding for speed |

Complete reference: `CHROMIUM-SCREENSHOTS-DETAIL.md`
