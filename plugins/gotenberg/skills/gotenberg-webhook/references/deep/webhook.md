# Gotenberg — Webhook & Remote-Download (Vollreferenz)

## Konzept

Gotenberg unterstuetzt **asynchrone Verarbeitung**: Statt synchron auf das Ergebnis zu warten, gibt Gotenberg sofort `204 No Content` zurueck und sendet das Ergebnis (oder einen Fehler) nach der Verarbeitung an eine konfigurierte Callback-URL.

Webhook-Header koennen bei **jedem** Gotenberg-Endpunkt verwendet werden.

---

## Webhook-Header

| Header | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Webhook-Url` | string | Bedingt* | — | Callback-URL fuer erfolgreiche Ergebnisse (POST, ausser ueberschrieben) |
| `Gotenberg-Webhook-Method` | string | Nein | `POST` | HTTP-Methode fuer Erfolgs-Callback; erlaubt: `POST`, `PUT`, `PATCH` |
| `Gotenberg-Webhook-Error-Url` | string | Nein | — | **Deprecated** — stattdessen `Gotenberg-Webhook-Events-Url` verwenden |
| `Gotenberg-Webhook-Error-Method` | string | Nein | `POST` | HTTP-Methode fuer Fehler-Callback; erlaubt: `POST`, `PUT`, `PATCH` |
| `Gotenberg-Webhook-Extra-Http-Headers` | JSON-string | Nein | — | Zusaetzliche HTTP-Header als JSON-Objekt fuer Callback-Requests |
| `Gotenberg-Webhook-Events-Url` | string | Bedingt* | — | URL fuer strukturierte JSON-Events (Erfolg + Fehler) |

*Mindestens `Gotenberg-Webhook-Url` oder `Gotenberg-Webhook-Events-Url` muss angegeben sein, sonst → 400.

---

## Antwort-Codes beim initialen Request

| Code | Beschreibung |
|------|-------------|
| `204 No Content` | Anfrage valide, asynchrone Verarbeitung gestartet |
| `400 Bad Request` | Ungueltige oder fehlende Header/Felder |
| `403 Forbidden` | Webhook-URL durch Outbound-Filter geblockt |

---

## Callback-Payloads

### Erfolgs-Callback (an Gotenberg-Webhook-Url)

```
Content-Disposition: attachment; filename={dateiname.ext}
Content-Type: {content-type}
Content-Length: {laenge}
Gotenberg-Trace: {trace}
traceparent: {w3c-traceparent}
User-Agent: Gotenberg

[Datei-Inhalt als Binary]
```

### Fehler-Callback (an Gotenberg-Webhook-Error-Url, deprecated)

```json
{
  "status": 500,
  "message": "conversion failed"
}
```

---

## Events-URL Payloads (Gotenberg-Webhook-Events-Url)

### Erfolgs-Event

```json
{
  "event": "webhook.success",
  "correlationId": "unique-request-id",
  "timestamp": "2025-01-15T10:30:00.000000000Z"
}
```

### Fehler-Event

```json
{
  "event": "webhook.error",
  "correlationId": "unique-request-id",
  "timestamp": "2025-01-15T10:30:00.000000000Z",
  "error": {
    "status": 500,
    "message": "conversion failed"
  }
}
```

---

## downloadFrom — Remote-Dateien laden

Ermoeglicht das Laden von Quelldateien aus externen URLs, anstatt sie hochzuladen.

### Form-Feld

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `downloadFrom` | JSON-Array | Nein | Liste von Remote-Datei-Objekten |

### downloadFrom-Objekt-Struktur

| Feld | Typ | Pflicht | Standard | Beschreibung |
|------|-----|---------|----------|--------------|
| `url` | string | Ja | — | Remote-URL; der Server **muss** einen `Content-Disposition`-Header mit `filename`-Parameter zurueckgeben |
| `extraHttpHeaders` | JSON-Objekt | Nein | — | Zusaetzliche HTTP-Header fuer diesen Fetch |
| `embedded` | boolean | Nein | `false` | Legacy-Option fuer Anhaenge |
| `field` | string | Nein | `""` | Ziel-Feld: `""` (Hauptdatei), `"watermark"`, `"stamp"` |

---

## curl-Beispiele

### Asynchrone Konvertierung mit Webhook

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --header 'Gotenberg-Webhook-Url: https://meine-app.example.com/webhook/pdf' \
  --header 'Gotenberg-Webhook-Extra-Http-Headers: {"Authorization":"Bearer mein-token"}' \
  --form url=https://example.com
```

### Webhook mit Events-URL (empfohlen)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Webhook-Url: https://meine-app.example.com/webhook/ergebnis' \
  --header 'Gotenberg-Webhook-Events-Url: https://meine-app.example.com/webhook/events' \
  --header 'Gotenberg-Webhook-Extra-Http-Headers: {"X-Api-Key":"abc123"}' \
  --form files=@/path/to/1.pdf \
  --form files=@/path/to/2.pdf
```

### Webhook mit PUT-Methode

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Webhook-Url: https://storage.example.com/pdf/output' \
  --header 'Gotenberg-Webhook-Method: PUT' \
  --form files=@/path/to/1.pdf
```

### Remote-Datei laden (downloadFrom)

```bash
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form 'downloadFrom=[{"url":"https://example.com/dokument.docx","extraHttpHeaders":{"X-Header":"Wert"}}]' \
  -o konvertiert.pdf
```

### Remote-Datei als Wasserzeichen laden

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=image \
  --form 'downloadFrom=[{"url":"https://cdn.example.com/logo.png","field":"watermark"}]' \
  --form watermarkExpression=logo.png \
  -o mit-wasserzeichen.pdf
```

---

## Konfiguration (Env-Variablen)

| Variable | Beschreibung | Standard |
|----------|-------------|---------|
| `WEBHOOK_ALLOW_LIST` | Regex fuer erlaubte Webhook-URLs | — |
| `WEBHOOK_DENY_PRIVATE_IPS` | Private IPs fuer Webhooks sperren | `false` |
| `WEBHOOK_DENY_PUBLIC_IPS` | Oeffentliche IPs fuer Webhooks sperren | `false` |
| `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | Private IPs fuer downloadFrom sperren | `false` |
| `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | Oeffentliche IPs fuer downloadFrom sperren | `false` |

---

## Hinweise

- W3C `traceparent`-Header wird ab v8.34.0 im Callback-Request mitgesendet (Distributed Tracing)
- Webhook-Callbacks und `downloadFrom`-Fetches durchlaufen Gotenbergs Outbound-Filter-Pipeline
- `Gotenberg-Webhook-Error-Url` ist deprecated — `Gotenberg-Webhook-Events-Url` verwenden
- Der Remote-Server bei `downloadFrom` **muss** `Content-Disposition: attachment; filename=datei.ext` zurueckgeben

---

Quelle: https://gotenberg.dev/docs/webhook-download
