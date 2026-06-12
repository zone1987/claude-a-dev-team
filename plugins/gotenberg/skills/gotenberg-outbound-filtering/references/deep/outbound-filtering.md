# Gotenberg — Outbound URL Filtering (Vollreferenz)

## Konzept

Gotenberg sichert alle ausgehenden Verbindungen gegen SSRF (Server-Side Request Forgery) und ungewollten Netzwerkzugriff. Der Filter-Pipeline greift bei:

1. **Chromium-Navigationen und Sub-Ressourcen** (CSS, Bilder, iframes)
2. **Webhook-Callbacks** (Erfolgs- und Fehler-URLs)
3. **`downloadFrom`-Fetches** (Remote-Dateien)
4. **LibreOffice-Referenzen** (verlinkte Bilder, externe Inhalte)

---

## Immer aktive Schutzmechanismen

| Mechanismus | Beschreibung |
|-------------|-------------|
| **DNS-Rebind-Pinning-Proxy** | Alle ausgehenden HTTP/HTTPS-Requests laufen ueber einen In-Process-Proxy mit gepinnten IPs |
| **`file://`-URL-Blocking** | `file://`-URLs werden auf URL-Konvertierungs- und Screenshot-Routen immer abgelehnt → 400 |
| **Per-Request-Asset-Isolation** | Lokale HTML-Assets sind auf das per-Request-Arbeitsverzeichnis beschraenkt |
| **LibreOffice Linked Content Blocking** | Inhalte aus nicht vertrauenswuerdigen Quellen werden vor dem Fetch gesperrt (ab v8.34.0) |

---

## Umgebungsvariablen

### Chromium-Modul

| Variable | Typ | Standard | Beschreibung |
|----------|-----|---------|--------------|
| `CHROMIUM_DENY_PRIVATE_IPS` | boolean | `false` | Chromium-Navigationen und Sub-Ressourcen auf nicht-oeffentliche IPs ablehnen |
| `CHROMIUM_DENY_PUBLIC_IPS` | boolean | `false` | Chromium-Navigationen auf oeffentliche IPs ablehnen |
| `CHROMIUM_ALLOW_LIST` | Regex | — | URL-Regex, der IP-Klassen-Checks umgeht |
| `CHROMIUM_PROXY_SERVER` | string | — | Proxy-Server; deaktiviert DNS-Rebind-Pinning-Proxy wenn gesetzt |
| `CHROMIUM_HOST_RESOLVER_RULES` | string | — | Host-Resolver-Regeln; deaktiviert DNS-Rebind-Pinning-Proxy wenn gesetzt |

### Webhook-Modul

| Variable | Typ | Standard | Beschreibung |
|----------|-----|---------|--------------|
| `WEBHOOK_DENY_PRIVATE_IPS` | boolean | `false` | Webhook-URLs auf nicht-oeffentliche IPs ablehnen |
| `WEBHOOK_DENY_PUBLIC_IPS` | boolean | `false` | Webhook-URLs auf oeffentliche IPs ablehnen |
| `WEBHOOK_ALLOW_LIST` | Regex | — | URL-Regex, der IP-Klassen-Checks fuer Webhooks umgeht |

### API Download-Modul

| Variable | Typ | Standard | Beschreibung |
|----------|-----|---------|--------------|
| `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | boolean | `false` | `downloadFrom`-URLs auf nicht-oeffentliche IPs ablehnen |
| `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | boolean | `false` | `downloadFrom`-URLs auf oeffentliche IPs ablehnen |

### LibreOffice-Modul

| Variable | Typ | Standard | Beschreibung |
|----------|-----|---------|--------------|
| `LIBREOFFICE_DENY_PRIVATE_IPS` | boolean | `false` | LibreOffice ausgehende Fetches auf nicht-oeffentliche IPs ablehnen |
| `LIBREOFFICE_DENY_PUBLIC_IPS` | boolean | `false` | LibreOffice ausgehende Fetches auf oeffentliche IPs ablehnen |
| `LIBREOFFICE_ALLOW_LIST` | Regex | — | URL-Regex, der IP-Klassen-Checks fuer LibreOffice umgeht |
| `LIBREOFFICE_DENY_LIST` | Regex | — | URLs bedingungslos blockieren (unabhaengig von anderen Regeln) |

---

## Filter-Pipeline und Praezedenz

1. **Deny-List-Auswertung** → blockiert unabhaengig von anderen Regeln
2. **Allow-List-Abgleich** → umgeht IP-Klassen-Checks bei Treffer
3. **IP-Klassen-Variablen** → werden angewendet wenn kein Allow-List-Treffer

---

## Definition von "nicht-oeffentlichen IPs"

Folgende Adressbereiche gelten als nicht-oeffentlich:
- Loopback (127.0.0.0/8, ::1)
- RFC1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
- Link-Local (169.254.0.0/16, fe80::/10)
- IPv6 Unique-Local (fc00::/7)
- IPv6-Wrapper um nicht-oeffentliche IPv4: IPv4-mapped, IPv4-translated, 6to4, Teredo

---

## Antwort-Codes

| Code | Szenario |
|------|---------|
| `400 Bad Request` | `file://`-URLs bei URL-Konvertierung / Screenshots |
| `403 Forbidden` | URL durch Deny-List oder IP-Klassen-Variablen abgelehnt |

---

## Konfigurationsbeispiele

### Alle internen Zugriffe sperren (maximale Sicherheit)

```bash
docker run --rm \
  -e CHROMIUM_DENY_PRIVATE_IPS=true \
  -e WEBHOOK_DENY_PRIVATE_IPS=true \
  -e API_DOWNLOAD_FROM_DENY_PRIVATE_IPS=true \
  -e LIBREOFFICE_DENY_PRIVATE_IPS=true \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### Nur bestimmte interne URLs erlauben (Allow-List)

```bash
docker run --rm \
  -e CHROMIUM_DENY_PRIVATE_IPS=true \
  -e 'CHROMIUM_ALLOW_LIST=https://intern\.meinefirma\.de/.*' \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### LibreOffice bestimmte URLs blockieren

```bash
docker run --rm \
  -e 'LIBREOFFICE_DENY_LIST=https://gesperrte-domain\.com/.*' \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### Docker-Compose-Konfiguration

```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "3000:3000"
    environment:
      CHROMIUM_DENY_PRIVATE_IPS: "true"
      WEBHOOK_DENY_PRIVATE_IPS: "true"
      API_DOWNLOAD_FROM_DENY_PRIVATE_IPS: "true"
      CHROMIUM_ALLOW_LIST: "https://trusted\\.intern\\.example\\.com/.*"
```

---

## Hinweise

- Ab **v8.31.0** wurden private IP-Sperren fuer Chromium aktiviert (revertiert in v8.32.0 zurueck zu `false` als Standard)
- Wenn `CHROMIUM_PROXY_SERVER` oder `CHROMIUM_HOST_RESOLVER_RULES` gesetzt sind, wird der DNS-Rebind-Pinning-Proxy deaktiviert
- LibreOffice Linked Content Blocking (ab v8.34.0) kann **nicht deaktiviert** werden

---

Quelle: https://gotenberg.dev/docs/outbound-url-filtering
