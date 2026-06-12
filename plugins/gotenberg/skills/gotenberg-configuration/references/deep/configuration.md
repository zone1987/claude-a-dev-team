# Gotenberg — Vollstaendige Konfigurationsreferenz

Konfiguration via CLI-Flags oder Umgebungsvariablen. **Immer den Befehl ueberschreiben,
nicht den Entrypoint.**

```yaml
# Docker Compose Beispiel
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    command:
      - "gotenberg"
      - "--api-timeout=60s"
      - "--chromium-auto-start=true"

# Oder per Env-Var:
  gotenberg:
    image: gotenberg/gotenberg:8
    environment:
      API_TIMEOUT: "60s"
      CHROMIUM_AUTO_START: "true"
```

## API-Modul

HTTP/1 und HTTP/2 (H2C) Server.

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--api-port` | `API_PORT` | `3000` | Port der API |
| `--api-port-from-env` | `API_PORT_FROM_ENV` | — | Env-Variable die den Port enthaelt (ueberschreibt `--api-port`) |
| `--api-bind-ip` | `API_BIND_IP` | `0.0.0.0` | IP-Adresse fuer eingehende Verbindungen |
| `--api-tls-cert-file` | `API_TLS_CERT_FILE` | — | Pfad zum TLS/SSL-Zertifikat (HTTPS) |
| `--api-tls-key-file` | `API_TLS_KEY_FILE` | — | Pfad zum TLS/SSL-Schluessel (HTTPS) |
| `--api-start-timeout` | `API_START_TIMEOUT` | `30s` | Max. Startzeit der API |
| `--api-timeout` | `API_TIMEOUT` | `30s` | Max. Dauer pro Request |
| `--api-body-limit` | `API_BODY_LIMIT` | — | Body-Limit fuer multipart/form-data (z.B. `5MB`, `1GB`) |
| `--api-root-path` | `API_ROOT_PATH` | `/` | Root-Pfad der API (fuer Service-Discovery per URL-Pfad) |
| `--api-correlation-id-header` | `API_CORRELATION_ID_HEADER` | `Gotenberg-Trace` | Header-Name fuer Request-Identifikation |
| `--api-enable-basic-auth` | `API_ENABLE_BASIC_AUTH` | `false` | Basic Auth aktivieren. Credentials per `GOTENBERG_API_BASIC_AUTH_USERNAME` / `GOTENBERG_API_BASIC_AUTH_PASSWORD` |
| `--api-download-from-allow-list` | `API_DOWNLOAD_FROM_ALLOW_LIST` | Alle | Erlaubte URLs fuer "Download From" (Regex, kommagetrennt oder wiederholtes Flag). Match umgeht IP-Klassen-Checks. |
| `--api-download-from-deny-list` | `API_DOWNLOAD_FROM_DENY_LIST` | — | Verbotene URLs fuer "Download From" (Regex). Match lehnt immer ab. |
| `--api-download-from-deny-private-ips` | `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | `false` | "Download From"-URLs mit privater IP (Loopback, RFC1918, Link-Local, IPv6 ULA) ablehnen |
| `--api-download-from-deny-public-ips` | `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | `false` | "Download From"-URLs mit oeffentlicher IP ablehnen |
| `--api-download-from-max-retry` | `API_DOWNLOAD_FROM_MAX_RETRY` | `4` | Max. Wiederholungsversuche fuer "Download From" |
| `--api-disable-download-from` | `API_DISABLE_DOWNLOAD_FROM` | `false` | "Download From"-Funktion komplett deaktivieren |
| `--api-disable-health-check-route-telemetry` | `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | `true` | Telemetrie fuer `/health` deaktivieren |
| `--api-disable-root-route-telemetry` | `API_DISABLE_ROOT_ROUTE_TELEMETRY` | `true` | Telemetrie fuer Root-Route deaktivieren |
| `--api-disable-debug-route-telemetry` | `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | `true` | Telemetrie fuer `/debug` deaktivieren |
| `--api-disable-version-route-telemetry` | `API_DISABLE_VERSION_ROUTE_TELEMETRY` | `true` | Telemetrie fuer `/version` deaktivieren |
| `--api-enable-debug-route` | `API_ENABLE_DEBUG_ROUTE` | `false` | Debug-Route `/debug` aktivieren |

**Hinweis (8.29.0):** `--api-trace-header` ist veraltet; `--api-correlation-id-header` verwenden.
**Hinweis (8.32.0):** `--api-download-from-deny-list` Default-Regex aus 8.31.0 entfernt. Outbound-Filtering ist jetzt standardmaessig permissiv.

## Chromium-Modul

Ein einzelner Chromium-Browser verwaltet alle Konvertierungen (Stateful-Modus).
Chromium kann bis zu **6 parallele Operationen** ausfuehren.

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--chromium-restart-after` | `CHROMIUM_RESTART_AFTER` | `100` | Chromium nach N Konvertierungen neu starten. `0` = deaktiviert |
| `--chromium-max-queue-size` | `CHROMIUM_MAX_QUEUE_SIZE` | `0` | Max. Warteschlangen-Groesse. `0` = unbegrenzt |
| `--chromium-max-concurrency` | `CHROMIUM_MAX_CONCURRENCY` | `6` | Max. parallele Konvertierungen (max. 6) |
| `--chromium-auto-start` | `CHROMIUM_AUTO_START` | `false` | Chromium beim Start automatisch initialisieren |
| `--chromium-start-timeout` | `CHROMIUM_START_TIMEOUT` | `20s` | Max. Wartezeit beim Chromium-Start/-Neustart |
| `--chromium-idle-shutdown-timeout` | `CHROMIUM_IDLE_SHUTDOWN_TIMEOUT` | `0s` | Chromium nach Idle-Dauer beenden. `0` = deaktiviert |
| `--chromium-allow-file-access-from-files` | `CHROMIUM_ALLOW_FILE_ACCESS_FROM_FILES` | `false` | `file://`-URIs erlauben, andere `file://`-URIs zu lesen |
| `--chromium-allow-insecure-localhost` | `CHROMIUM_ALLOW_INSECURE_LOCALHOST` | `false` | TLS/SSL-Fehler auf localhost ignorieren |
| `--chromium-allow-list` | `CHROMIUM_ALLOW_LIST` | Alle | Erlaubte URLs fuer Chromium-Navigation (Regex). Match umgeht IP-Klassen-Checks. |
| `--chromium-deny-list` | `CHROMIUM_DENY_LIST` | `^file:(?!//\/tmp/).*` | Verbotene URLs fuer Chromium (Regex). Match lehnt immer ab. |
| `--chromium-deny-private-ips` | `CHROMIUM_DENY_PRIVATE_IPS` | `false` | Navigation zu privaten IPs ablehnen |
| `--chromium-deny-public-ips` | `CHROMIUM_DENY_PUBLIC_IPS` | `false` | Navigation zu oeffentlichen IPs ablehnen |
| `--chromium-ignore-certificate-errors` | `CHROMIUM_IGNORE_CERTIFICATE_ERRORS` | `false` | Zertifikatsfehler ignorieren |
| `--chromium-disable-web-security` | `CHROMIUM_DISABLE_WEB_SECURITY` | `false` | Same-Origin-Policy deaktivieren |
| `--chromium-incognito` | `CHROMIUM_INCOGNITO` | `false` | **Veraltet seit 8.29.0** — wird ignoriert |
| `--chromium-host-resolver-rules` | `CHROMIUM_HOST_RESOLVER_RULES` | — | Benutzerdefinierte Host-Resolver-Regeln. Umgeht DNS-Rebind-Proxy. |
| `--chromium-proxy-server` | `CHROMIUM_PROXY_SERVER` | — | Ausgehender Proxy-Server (nur HTTP/HTTPS). Umgeht DNS-Rebind-Proxy. |
| `--chromium-clear-cache` | `CHROMIUM_CLEAR_CACHE` | `false` | Chromium-Cache nach jeder Konvertierung leeren |
| `--chromium-clear-cookies` | `CHROMIUM_CLEAR_COOKIES` | `false` | Chromium-Cookies nach jeder Konvertierung leeren |
| `--chromium-disable-javascript` | `CHROMIUM_DISABLE_JAVASCRIPT` | `false` | JavaScript deaktivieren |
| `--chromium-disable-routes` | `CHROMIUM_DISABLE_ROUTES` | `false` | Alle Chromium-Routen deaktivieren |

**Hinweis (8.32.0):** Jeder Chromium HTTP/HTTPS-Request laeuft durch einen internen Pinning-Proxy
(DNS einmal aufloesen, validierte IP waehlen). `--chromium-proxy-server` oder `--chromium-host-resolver-rules`
umgehen diesen Proxy.

## LibreOffice-Modul

Eine einzelne LibreOffice-Instanz verwaltet alle Konvertierungen.
**Keine parallelen Operationen** moeglich (Lock-Mechanismus).

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--libreoffice-restart-after` | `LIBREOFFICE_RESTART_AFTER` | `10` | LibreOffice nach N Konvertierungen neu starten. `0` = deaktiviert |
| `--libreoffice-max-queue-size` | `LIBREOFFICE_MAX_QUEUE_SIZE` | `0` | Max. Warteschlangen-Groesse. `0` = unbegrenzt |
| `--libreoffice-auto-start` | `LIBREOFFICE_AUTO_START` | `false` | LibreOffice beim Start automatisch initialisieren |
| `--libreoffice-start-timeout` | `LIBREOFFICE_START_TIMEOUT` | `20s` | Max. Wartezeit beim Start/-Neustart |
| `--libreoffice-idle-shutdown-timeout` | `LIBREOFFICE_IDLE_SHUTDOWN_TIMEOUT` | `0s` | LibreOffice nach Idle-Dauer beenden. `0` = deaktiviert |
| `--libreoffice-allow-list` | `LIBREOFFICE_ALLOW_LIST` | Alle | Erlaubte URLs fuer LibreOffice-Outbound-Fetches (Regex) |
| `--libreoffice-deny-list` | `LIBREOFFICE_DENY_LIST` | — | Verbotene URLs fuer LibreOffice-Outbound-Fetches (Regex) |
| `--libreoffice-deny-private-ips` | `LIBREOFFICE_DENY_PRIVATE_IPS` | `false` | Outbound-Fetches zu privaten IPs ablehnen |
| `--libreoffice-deny-public-ips` | `LIBREOFFICE_DENY_PUBLIC_IPS` | `false` | Outbound-Fetches zu oeffentlichen IPs ablehnen |
| `--libreoffice-disable-routes` | `LIBREOFFICE_DISABLE_ROUTES` | `false` | Alle LibreOffice-Routen deaktivieren |

### LibreOffice-Sprache aendern

Standard: Englisch. Eigenes Docker-Image mit anderer Sprache bauen:

```dockerfile
# Ab Gotenberg 8.23.1 (Debian Trixie)
FROM gotenberg/gotenberg:8
USER root
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
      -t trixie-backports libreoffice-l10n-de && \
    sed -i '/de_DE.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8
USER gotenberg
```

## PDF-Engines-Modul

Gotenberg unterstuetzt folgende PDF Engines:

| Feature | ExifTool | PDFtk | pdfcpu | QPDF | UNO |
|---------|----------|-------|--------|------|-----|
| Merge | - | Ja | Ja | Ja | - |
| Split | - | Ja | Ja | Ja | - |
| Flatten | - | - | - | Ja | - |
| PDF/A & PDF/UA | - | - | - | - | Ja |
| Metadaten lesen | Ja | - | - | - | - |
| Metadaten schreiben | Ja | - | - | - | - |
| Encrypt | - | Ja | Ja | Ja | - |
| Dateien einbetten | - | - | Ja | - | - |
| Factur-X (XMP) | - | - | - | Ja | - |
| Wasserzeichen | - | Ja | Ja | - | - |
| Stempel | - | Ja | Ja | - | - |
| Lesezeichen lesen | - | - | Ja | - | - |
| Lesezeichen schreiben | - | - | Ja | - | - |
| Drehen | - | Ja | Ja | - | - |

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--pdfengines-merge-engines` | `PDFENGINES_MERGE_ENGINES` | `qpdf,pdfcpu,pdftk` | Engines und Reihenfolge fuer Merge |
| `--pdfengines-split-engines` | `PDFENGINES_SPLIT_ENGINES` | `pdfcpu,qpdf,pdftk` | Engines fuer Split |
| `--pdfengines-flatten-engines` | `PDFENGINES_FLATTEN_ENGINES` | `qpdf` | Engines fuer Flatten |
| `--pdfengines-convert-engines` | `PDFENGINES_CONVERT_ENGINES` | `libreoffice-pdfengine` | Engines fuer PDF/A-Konvertierung |
| `--pdfengines-read-metadata-engines` | `PDFENGINES_READ_METADATA_ENGINES` | `exiftool` | Engines zum Metadaten-Lesen |
| `--pdfengines-write-metadata-engines` | `PDFENGINES_WRITE_METADATA_ENGINES` | `exiftool` | Engines zum Metadaten-Schreiben |
| `--pdfengines-encrypt-engines` | `PDFENGINES_ENCRYPT_ENGINES` | `qpdf,pdftk,pdfcpu` | Engines fuer Verschluesselung |
| `--pdfengines-embed-engines` | `PDFENGINES_EMBED_ENGINES` | `pdfcpu` | Engines fuer Datei-Einbettung |
| `--pdfengines-embed-metadata-engines` | `PDFENGINES_EMBED_METADATA_ENGINES` | `qpdf` | Engines fuer Embed-Metadaten |
| `--pdfengines-watermark-engines` | `PDFENGINES_WATERMARK_ENGINES` | `pdfcpu,pdftk` | Engines fuer Wasserzeichen |
| `--pdfengines-stamp-engines` | `PDFENGINES_STAMP_ENGINES` | `pdfcpu,pdftk` | Engines fuer Stempel |
| `--pdfengines-write-bookmarks-engines` | `PDFENGINES_WRITE_BOOKMARKS_ENGINES` | `pdfcpu` | Engines fuer Lesezeichen-Schreiben |
| `--pdfengines-read-bookmarks-engines` | `PDFENGINES_READ_BOOKMARKS_ENGINES` | `pdfcpu` | Engines fuer Lesezeichen-Lesen |
| `--pdfengines-rotate-engines` | `PDFENGINES_ROTATE_ENGINES` | `pdfcpu,pdftk` | Engines fuer Drehen |
| `--pdfengines-factur-x-engines` | `PDFENGINES_FACTUR_X_ENGINES` | `qpdf` | Engines fuer Factur-X XMP |
| `--pdfengines-disable-routes` | `PDFENGINES_DISABLE_ROUTES` | `false` | Alle PDF-Engine-Routen deaktivieren |

## Webhook-Modul

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--webhook-enable-sync-mode` | `WEBHOOK_ENABLE_SYNC_MODE` | `false` | Synchronen Webhook-Modus aktivieren |
| `--webhook-allow-list` | `WEBHOOK_ALLOW_LIST` | Alle | Erlaubte Callback-URLs (Regex) |
| `--webhook-deny-list` | `WEBHOOK_DENY_LIST` | — | Verbotene Callback-URLs (Regex) |
| `--webhook-deny-private-ips` | `WEBHOOK_DENY_PRIVATE_IPS` | `false` | Callbacks zu privaten IPs ablehnen |
| `--webhook-deny-public-ips` | `WEBHOOK_DENY_PUBLIC_IPS` | `false` | Callbacks zu oeffentlichen IPs ablehnen |
| `--webhook-disable` | `WEBHOOK_DISABLE` | `false` | Webhook-Feature komplett deaktivieren |

---
Quelle: https://gotenberg.dev/docs/configuration
