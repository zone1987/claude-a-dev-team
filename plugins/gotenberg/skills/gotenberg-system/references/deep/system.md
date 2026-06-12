# Gotenberg — System-Endpunkte (Vollreferenz)

## Uebersicht aller System-Routen

| Methode | Route | Beschreibung |
|---------|-------|-------------|
| `GET` | `/health` | Gesundheitsstatus mit Detail-JSON |
| `HEAD` | `/health` | Gesundheitsstatus (nur Status-Code, kein Body) |
| `GET` | `/version` | Laufende Gotenberg-Version |
| `GET` | `/prometheus/metrics` | Prometheus-Metriken (deprecated ab v8.29.0) |
| `GET` | `/debug` | Runtime-Konfiguration + Module + Abhaengigkeiten (nur wenn aktiviert) |

---

## 1. GET /health — Gesundheitspruefung

### Route

```
GET /health
```

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Antwort-Codes

| Code | Beschreibung |
|------|-------------|
| `200` | Dienst ist gesund |
| `503` | Dienst ist nicht gesund |

### Antwort-Body (200 — gesund)

```json
{
  "status": "up",
  "details": {
    "chromium": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    },
    "libreoffice": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    }
  }
}
```

### Antwort-Body (503 — nicht gesund)

```json
{
  "status": "down",
  "details": {
    "chromium": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    },
    "libreoffice": {
      "status": "down",
      "timestamp": "2021-07-01T08:05:14.603364Z",
      "error": "LibreOffice ist nicht verfuegbar"
    }
  }
}
```

### Antwort-Struktur pro Modul

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `status` | `"up"` / `"down"` | Modulgesundheit |
| `timestamp` | ISO 8601 | Zeitstempel der Pruefung |
| `error` | string (optional) | Fehlermeldung wenn status=down |

### curl-Beispiel

```bash
curl --request GET http://localhost:3000/health
```

---

## 2. HEAD /health — Leichtgewichtige Gesundheitspruefung

### Route

```
HEAD /health
```

### Beschreibung

Identisch mit `GET /health`, aber ohne Response-Body. Ideal fuer haeufiges Polling (z.B. Kubernetes Liveness-Probe, Load-Balancer-Checks), da weniger Bandwidth verbraucht wird.

### Antwort-Codes

| Code | Beschreibung |
|------|-------------|
| `200` | Dienst ist gesund |
| `503` | Dienst ist nicht gesund |

### curl-Beispiel

```bash
curl --request HEAD http://localhost:3000/health
```

### Kubernetes Liveness-Probe (Beispiel)

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 3000
  initialDelaySeconds: 10
  periodSeconds: 30
  failureThreshold: 3
```

**Ab v8.33.0:** Toleriert eine transiente Fehler-Probe, cacht kurz erfolgreiche Ergebnisse — verhindert, dass Probe-Spam gesunde Instanzen zum Neustart zwingt.

---

## 3. GET /version — Versionsinformation

### Route

```
GET /version
```

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Antwort

| Code | Content-Type | Body |
|------|-------------|------|
| `200` | `text/plain; charset=UTF-8` | Versionsstring, z.B. `Gotenberg 8.0.0` |

### curl-Beispiel

```bash
curl --request GET http://localhost:3000/version
```

### Antwort-Beispiel

```
Gotenberg 8.0.0
```

Hinweis: Custom-Builds koennen nicht-standardmaessige Versionen anzeigen (z.B. `8.0.0-live-demo-snapshot`).

---

## 4. GET /prometheus/metrics — Prometheus-Metriken

### Route

```
GET /prometheus/metrics
```

**Deprecated ab v8.29.0** — Migration zu OpenTelemetry empfohlen (siehe `gotenberg-telemetry`).

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Antwort

| Code | Content-Type | Beschreibung |
|------|-------------|--------------|
| `200` | Prometheus-Textformat | Metriken im Prometheus-Exposition-Format |

### curl-Beispiel

```bash
curl --request GET http://localhost:3000/prometheus/metrics
```

### Konfiguration

Der Prometheus-Endpunkt wird durch das Prometheus-Modul aktiviert. Konfigurierbar ueber Gotenberg-Startflags.

Telemetrie-Route-Disable (Standard `true`):
- `PROMETHEUS_DISABLE_ROUTE_TELEMETRY=true` — Prometheus-Metriken-Route selbst erzeugt keine Telemetrie

---

## 5. GET /debug — Debug-Konfiguration

### Route

```
GET /debug
```

### Aktivierung

**Muss explizit aktiviert werden:**

```bash
# Als Startflag
--api-enable-debug-route

# Als Umgebungsvariable
API_ENABLE_DEBUG_ROUTE=true
```

### Beschreibung

Gibt zurueck:
- Runtime-Konfiguration (alle aktiven Flags und deren Werte)
- Aktive Module
- Abhaengigkeits-Versionen (Chromium, LibreOffice, ExifTool, etc.)

Nuetzlich fuer Deployment-Verifikation und Debugging von Konfigurationsproblemen.

### Request-Header

| Header | Typ | Pflicht | Beschreibung |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | Nein | Eigene Request-ID fuer Log-Identifizierung |

### Antwort

| Code | Beschreibung |
|------|-------------|
| `200` | Debug-Informationen (JSON-aehnliches Format) |

### curl-Beispiel

```bash
API_ENABLE_DEBUG_ROUTE=true
curl --request GET http://localhost:3000/debug
```

### Docker-Compose-Aktivierung

```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    environment:
      API_ENABLE_DEBUG_ROUTE: "true"
```

**Sicherheitshinweis:** Debug-Route in Produktion deaktiviert lassen! Sie kann interne Konfigurationsdetails, Versionen und Passwort-Hints preisgeben.

---

## Telemetrie-Steuerung fuer System-Routen

High-frequency-Routen erzeugen standardmaessig keine Telemetrie:

| Route | Env-Variable | Standard |
|-------|-------------|---------|
| Root `/` | `API_DISABLE_ROOT_ROUTE_TELEMETRY` | `true` |
| `/debug` | `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | `true` |
| `/version` | `API_DISABLE_VERSION_ROUTE_TELEMETRY` | `true` |
| `/health` | `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | `true` |
| `/prometheus/metrics` | `PROMETHEUS_DISABLE_ROUTE_TELEMETRY` | `true` |

---

Quellen:
- https://gotenberg.dev/docs/system/get-health-check
- https://gotenberg.dev/docs/system/head-health-check
- https://gotenberg.dev/docs/system/version
- https://gotenberg.dev/docs/system/prometheus-metrics
- https://gotenberg.dev/docs/system/debug
