# Gotenberg — URL zu PDF

**Route:** `POST /forms/chromium/convert/url`

Konvertiert eine Webseite per URL zu PDF via Headless Chromium.
Unterstuetzt JavaScript-Ausfuehrung, SPAs und dynamischen Inhalt.

## Pflichtfeld

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `url` | string | URL der zu konvertierenden Seite. `file://`-URLs geben 400 zurueck. |

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o my.pdf
```

Alle weiteren Form-Felder sind identisch mit dem HTML-Endpunkt:
Seitenlayout, Hintergrund, Medientyp, Warten, Cookies, Headers, Header/Footer,
Metadaten, Wasserzeichen, Split, PDF/A, Verschluesselung.

Vollstaendige Feldtabellen: `CHROMIUM-URL-DETAIL.md`
