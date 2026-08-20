# Gotenberg — URL to PDF

**Route:** `POST /forms/chromium/convert/url`

Converts a web page by URL to PDF via headless Chromium.
Supports JavaScript execution, SPAs and dynamic content.

## Required field

| Field | Type | Description |
|------|-----|-------------|
| `url` | string | URL of the page to convert. `file://` URLs return 400. |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o my.pdf
```

All further form fields are identical to the HTML endpoint:
page layout, background, media type, waiting, cookies, headers, header/footer,
metadata, watermark, split, PDF/A, encryption.

Complete field tables: `CHROMIUM-URL-DETAIL.md`
