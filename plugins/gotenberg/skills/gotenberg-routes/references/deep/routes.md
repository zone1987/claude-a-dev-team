# Gotenberg — Vollstaendige Routen-Referenz

## Protokoll

Jede Route akzeptiert einen **`multipart/form-data` POST-Request** und gibt eine Datei zurueck.

## Gemeinsame Request-Header

| Header | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `Gotenberg-Output-Filename` | string | Random UUID | Dateiname der Ausgabedatei ohne Extension. Gotenberg haengt die korrekte Extension automatisch an. |
| `Gotenberg-Trace` | string | Random UUID | Eigene Request-ID zur Identifikation im Log. Ueberschreibt die Standard-UUID. Konfigurierbar via `--api-correlation-id-header`. |

## Standard Response-Header (Erfolg 200)

```
Content-Disposition: attachment; filename={output-filename.ext}
Content-Type: {content-type}
Content-Length: {content-length}
Gotenberg-Trace: {trace}
Body: {output-file}
```

## Authentifizierung

Basic Auth wird aktiviert per CLI-Flag:
```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8 \
  gotenberg --api-enable-basic-auth
```

Credentials werden ausschliesslich per Umgebungsvariable gesetzt:
- `GOTENBERG_API_BASIC_AUTH_USERNAME`
- `GOTENBERG_API_BASIC_AUTH_PASSWORD`

## Alle Routen

### Konvertierung zu PDF

| Aufgabe | Route | Engine |
|---------|-------|--------|
| URL zu PDF | `POST /forms/chromium/convert/url` | Chromium |
| HTML-Datei zu PDF | `POST /forms/chromium/convert/html` | Chromium |
| Markdown zu PDF | `POST /forms/chromium/convert/markdown` | Chromium |
| Office-Dokumente zu PDF | `POST /forms/libreoffice/convert` | LibreOffice |

### Screenshots

| Aufgabe | Route |
|---------|-------|
| URL screenshotten | `POST /forms/chromium/screenshot/url` |
| HTML screenshotten | `POST /forms/chromium/screenshot/html` |
| Markdown screenshotten | `POST /forms/chromium/screenshot/markdown` |

### PDF-Manipulation (PDF Engines)

| Aufgabe | Route |
|---------|-------|
| Merge | `POST /forms/pdfengines/merge` |
| Split | `POST /forms/pdfengines/split` |
| PDF/A oder PDF/UA | `POST /forms/pdfengines/convert` |
| Metadaten lesen | `POST /forms/pdfengines/metadata/read` |
| Metadaten schreiben | `POST /forms/pdfengines/metadata/write` |
| Lesezeichen lesen | `POST /forms/pdfengines/bookmarks/read` |
| Lesezeichen schreiben | `POST /forms/pdfengines/bookmarks/write` |
| Dateianhange einbetten | `POST /forms/pdfengines/embed` |
| Factur-X / ZUGFeRD | `POST /forms/pdfengines/factur-x` |
| Formularfelder glaetten | `POST /forms/pdfengines/flatten` |
| Wasserzeichen | `POST /forms/pdfengines/watermark` |
| Stempel | `POST /forms/pdfengines/stamp` |
| Drehen | `POST /forms/pdfengines/rotate` |
| Verschluesseln | `POST /forms/pdfengines/encrypt` |

### System & Betrieb

| Route | Beschreibung |
|-------|-------------|
| `GET /health` | Health-Check |
| `GET /version` | Versionsinfo |
| `GET /debug` | Konfigurationsdump (muss via `--api-enable-debug-route` aktiviert werden) |

### Asynchron & Remote

| Feature | Beschreibung |
|---------|-------------|
| Webhooks | Asynchrone Verarbeitung; Gotenberg laedt Ergebnis zu einer URL hoch |
| Download From | Input-Dateien koennen per Remote-URL angegeben werden |

## Hinweis zu Konvertierungsrouten

Konvertierungsrouten akzeptieren die meisten PDF-Engine-Funktionen
(Metadaten, Anhange, Wasserzeichen, Verschluesselung, ...) direkt im selben Request.
Kein separater zweiter API-Aufruf noetig.

## HTTP-Statuscodes

| Code | Bedeutung |
|------|-----------|
| 200 | Erfolg — Datei im Body |
| 400 | Ungueltige Felder oder kritischer Netzwerkfehler |
| 403 | URL verboten (Outbound-Filter) |
| 409 | HTTP-Statuscode-Fehler der Zielseite / Chromium-Console-Exception |
| 503 | Timeout — Request hat das Zeitlimit ueberschritten |

---
Quelle: https://gotenberg.dev/docs/getting-started/routes
