# Gotenberg — Screenshots (full reference)

## Contents

- [Routes](#routes)
- [Basic examples](#basic-examples)
- [Request headers](#request-headers)
- [Mandatory fields per route](#mandatory-fields-per-route)
- [Screenshot rendering fields](#screenshot-rendering-fields)
- [Viewport & layout notes](#viewport--layout-notes)
- [Fields shared with PDF conversion](#fields-shared-with-pdf-conversion)
- [Response codes](#response-codes)
- [Total number of form fields: ~22](#total-number-of-form-fields-22)

## Routes

| Route | Input type |
|-------|-----------|
| `POST /forms/chromium/screenshot/url` | URL (`url` field) |
| `POST /forms/chromium/screenshot/html` | `index.html` file |
| `POST /forms/chromium/screenshot/markdown` | `index.html` template + `.md` files |

## Basic examples

```bash
# URL screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/url \
  --form url=https://my.url \
  -o my.png

# HTML screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/html \
  --form files=@/path/to/index.html \
  -o my.png

# Markdown screenshot
curl \
  --request POST http://localhost:3000/forms/chromium/screenshot/markdown \
  --form files=@/path/to/index.html \
  --form files=@/path/to/file.md \
  -o my.png
```

## Request headers

| Header | Type | Default | Description |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Output file name (without extension) |
| `Gotenberg-Trace` | string | Random UUID | Request ID for logs |

## Mandatory fields per route

### /screenshot/url

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `url` | string | Yes | URL of the target page. `file://` URLs return 400. |

### /screenshot/html

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `files` (index.html) | file | Yes | HTML file (must be named `index.html`) |

### /screenshot/markdown

| Field | Type | Required | Description |
|------|-----|---------|-------------|
| `files` (index.html) | file | Yes | HTML template with `{{ toHTML "file.md" }}` |
| `files` (*.md) | file[] | Yes | At least one Markdown file |

## Screenshot rendering fields

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `width` | number | `800` | Viewport width in pixels |
| `height` | number | `600` | Viewport height in pixels |
| `clip` | boolean | `false` | Clip the screenshot to the viewport. Without clip: full page height. |
| `deviceScaleFactor` | number | `1` | Pixel density. `2` = Retina/HiDPI quality. |
| `format` | enum | `png` | Output format: `png`, `jpeg`, `webp` |
| `quality` | number | `100` | Compression quality 0-100 (only with `format=jpeg`) |
| `omitBackground` | boolean | `false` | Hide the default white background (transparency possible) |
| `optimizeForSpeed` | boolean | `false` | Optimize image encoding for speed instead of file size |

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

## Viewport & layout notes

- Without `clip=true` Chromium captures the full page height (the height of the content)
- With `clip=true` it clips exactly to `width` x `height`
- `deviceScaleFactor=2` doubles the resolution (good for Retina displays)
- Set the viewport dimensions accordingly with `width`/`height`

## Fields shared with PDF conversion

The following fields also work for screenshots:

### JavaScript & waiting

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `waitDelay` | duration | — | Fixed wait time before the screenshot |
| `waitForExpression` | string | — | Wait for a JS expression |
| `waitForSelector` | string | — | Wait for a CSS selector |

### Network

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `cookies` | json | — | Cookie array |
| `extraHttpHeaders` | json | — | Additional HTTP headers |
| `userAgent` | string | — | User agent |
| `failOnHttpStatusCodes` | json | `[499,599]` | Error on status codes |
| `failOnResourceHttpStatusCodes` | json | — | Error on asset status codes |
| `ignoreResourceHttpStatusDomains` | json | — | Exempt domains |
| `skipNetworkIdleEvent` | boolean | `true` | Do not wait for network idle |
| `skipNetworkAlmostIdleEvent` | boolean | `true` | Do not wait for almost-idle |
| `failOnResourceLoadingFailed` | boolean | `false` | Error on asset loading failure |
| `failOnConsoleExceptions` | boolean | `false` | Error on JS exceptions |

### Print media

| Field | Type | Default | Description |
|------|-----|---------|-------------|
| `emulatedMediaType` | enum | `screen` | `screen` or `print` (screenshots use `screen` as the default) |
| `emulatedMediaFeatures` | json | — | CSS media feature overrides |

## Response codes

| Code | Meaning |
|------|-----------|
| 200 | Success — image file in the body |
| 400 | Invalid fields / network error |
| 403 | URL forbidden (URL route only) |
| 409 | Status code error / console exception |
| 503 | Timeout |

## Total number of form fields: ~22

Screenshot-specific (8) + waiting (3) + network (10) + media (2) = ~23 fields

---
Sources:
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-url
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-html
- https://gotenberg.dev/docs/convert-with-chromium/screenshot-markdown
