# Gotenberg — Complete configuration reference

Configuration via CLI flags or environment variables. **Always override the command,
not the entrypoint.**

```yaml
# Docker Compose example
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    command:
      - "gotenberg"
      - "--api-timeout=60s"
      - "--chromium-auto-start=true"

# Or via env var:
  gotenberg:
    image: gotenberg/gotenberg:8
    environment:
      API_TIMEOUT: "60s"
      CHROMIUM_AUTO_START: "true"
```

## Contents

- [API module](#api-module)
- [Chromium module](#chromium-module)
- [LibreOffice module](#libreoffice-module)
- [PDF Engines module](#pdf-engines-module)
- [Webhook module](#webhook-module)

## API module

HTTP/1 and HTTP/2 (H2C) server.

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--api-port` | `API_PORT` | `3000` | Port of the API |
| `--api-port-from-env` | `API_PORT_FROM_ENV` | — | Env variable containing the port (overrides `--api-port`) |
| `--api-bind-ip` | `API_BIND_IP` | `0.0.0.0` | IP address for incoming connections |
| `--api-tls-cert-file` | `API_TLS_CERT_FILE` | — | Path to the TLS/SSL certificate (HTTPS) |
| `--api-tls-key-file` | `API_TLS_KEY_FILE` | — | Path to the TLS/SSL key (HTTPS) |
| `--api-start-timeout` | `API_START_TIMEOUT` | `30s` | Max. startup time of the API |
| `--api-timeout` | `API_TIMEOUT` | `30s` | Max. duration per request |
| `--api-body-limit` | `API_BODY_LIMIT` | — | Body limit for multipart/form-data (e.g. `5MB`, `1GB`) |
| `--api-root-path` | `API_ROOT_PATH` | `/` | Root path of the API (for service discovery via URL path) |
| `--api-correlation-id-header` | `API_CORRELATION_ID_HEADER` | `Gotenberg-Trace` | Header name for request identification |
| `--api-enable-basic-auth` | `API_ENABLE_BASIC_AUTH` | `false` | Enable basic auth. Credentials via `GOTENBERG_API_BASIC_AUTH_USERNAME` / `GOTENBERG_API_BASIC_AUTH_PASSWORD` |
| `--api-download-from-allow-list` | `API_DOWNLOAD_FROM_ALLOW_LIST` | All | Allowed URLs for "Download From" (regex, comma-separated or repeated flag). A match bypasses IP class checks. |
| `--api-download-from-deny-list` | `API_DOWNLOAD_FROM_DENY_LIST` | — | Forbidden URLs for "Download From" (regex). A match always rejects. |
| `--api-download-from-deny-private-ips` | `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | `false` | Reject "Download From" URLs with a private IP (loopback, RFC1918, link-local, IPv6 ULA) |
| `--api-download-from-deny-public-ips` | `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | `false` | Reject "Download From" URLs with a public IP |
| `--api-download-from-max-retry` | `API_DOWNLOAD_FROM_MAX_RETRY` | `4` | Max. retry attempts for "Download From" |
| `--api-disable-download-from` | `API_DISABLE_DOWNLOAD_FROM` | `false` | Disable the "Download From" feature entirely |
| `--api-disable-health-check-route-telemetry` | `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | `true` | Disable telemetry for `/health` |
| `--api-disable-root-route-telemetry` | `API_DISABLE_ROOT_ROUTE_TELEMETRY` | `true` | Disable telemetry for the root route |
| `--api-disable-debug-route-telemetry` | `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | `true` | Disable telemetry for `/debug` |
| `--api-disable-version-route-telemetry` | `API_DISABLE_VERSION_ROUTE_TELEMETRY` | `true` | Disable telemetry for `/version` |
| `--api-enable-debug-route` | `API_ENABLE_DEBUG_ROUTE` | `false` | Enable the debug route `/debug` |

**Note (8.29.0):** `--api-trace-header` is deprecated; use `--api-correlation-id-header`.
**Note (8.32.0):** the `--api-download-from-deny-list` default regex from 8.31.0 was removed. Outbound filtering is now permissive by default.

## Chromium module

A single Chromium browser handles all conversions (stateful mode).
Chromium can run up to **6 parallel operations**.

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--chromium-restart-after` | `CHROMIUM_RESTART_AFTER` | `100` | Restart Chromium after N conversions. `0` = disabled |
| `--chromium-max-queue-size` | `CHROMIUM_MAX_QUEUE_SIZE` | `0` | Max. queue size. `0` = unlimited |
| `--chromium-max-concurrency` | `CHROMIUM_MAX_CONCURRENCY` | `6` | Max. parallel conversions (max. 6) |
| `--chromium-auto-start` | `CHROMIUM_AUTO_START` | `false` | Initialize Chromium automatically at startup |
| `--chromium-start-timeout` | `CHROMIUM_START_TIMEOUT` | `20s` | Max. wait time for Chromium start/restart |
| `--chromium-idle-shutdown-timeout` | `CHROMIUM_IDLE_SHUTDOWN_TIMEOUT` | `0s` | Shut down Chromium after an idle period. `0` = disabled |
| `--chromium-allow-file-access-from-files` | `CHROMIUM_ALLOW_FILE_ACCESS_FROM_FILES` | `false` | Allow `file://` URIs to read other `file://` URIs |
| `--chromium-allow-insecure-localhost` | `CHROMIUM_ALLOW_INSECURE_LOCALHOST` | `false` | Ignore TLS/SSL errors on localhost |
| `--chromium-allow-list` | `CHROMIUM_ALLOW_LIST` | All | Allowed URLs for Chromium navigation (regex). A match bypasses IP class checks. |
| `--chromium-deny-list` | `CHROMIUM_DENY_LIST` | `^file:(?!//\/tmp/).*` | Forbidden URLs for Chromium (regex). A match always rejects. |
| `--chromium-deny-private-ips` | `CHROMIUM_DENY_PRIVATE_IPS` | `false` | Reject navigation to private IPs |
| `--chromium-deny-public-ips` | `CHROMIUM_DENY_PUBLIC_IPS` | `false` | Reject navigation to public IPs |
| `--chromium-ignore-certificate-errors` | `CHROMIUM_IGNORE_CERTIFICATE_ERRORS` | `false` | Ignore certificate errors |
| `--chromium-disable-web-security` | `CHROMIUM_DISABLE_WEB_SECURITY` | `false` | Disable the same-origin policy |
| `--chromium-incognito` | `CHROMIUM_INCOGNITO` | `false` | **Deprecated since 8.29.0** — is ignored |
| `--chromium-host-resolver-rules` | `CHROMIUM_HOST_RESOLVER_RULES` | — | Custom host resolver rules. Bypasses the DNS rebind proxy. |
| `--chromium-proxy-server` | `CHROMIUM_PROXY_SERVER` | — | Outbound proxy server (HTTP/HTTPS only). Bypasses the DNS rebind proxy. |
| `--chromium-clear-cache` | `CHROMIUM_CLEAR_CACHE` | `false` | Clear the Chromium cache after each conversion |
| `--chromium-clear-cookies` | `CHROMIUM_CLEAR_COOKIES` | `false` | Clear the Chromium cookies after each conversion |
| `--chromium-disable-javascript` | `CHROMIUM_DISABLE_JAVASCRIPT` | `false` | Disable JavaScript |
| `--chromium-disable-routes` | `CHROMIUM_DISABLE_ROUTES` | `false` | Disable all Chromium routes |

**Note (8.32.0):** every Chromium HTTP/HTTPS request goes through an internal pinning proxy
(resolve DNS once, pick the validated IP). `--chromium-proxy-server` or `--chromium-host-resolver-rules`
bypass this proxy.

## LibreOffice module

A single LibreOffice instance handles all conversions.
**No parallel operations** possible (lock mechanism).

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--libreoffice-restart-after` | `LIBREOFFICE_RESTART_AFTER` | `10` | Restart LibreOffice after N conversions. `0` = disabled |
| `--libreoffice-max-queue-size` | `LIBREOFFICE_MAX_QUEUE_SIZE` | `0` | Max. queue size. `0` = unlimited |
| `--libreoffice-auto-start` | `LIBREOFFICE_AUTO_START` | `false` | Initialize LibreOffice automatically at startup |
| `--libreoffice-start-timeout` | `LIBREOFFICE_START_TIMEOUT` | `20s` | Max. wait time for start/restart |
| `--libreoffice-idle-shutdown-timeout` | `LIBREOFFICE_IDLE_SHUTDOWN_TIMEOUT` | `0s` | Shut down LibreOffice after an idle period. `0` = disabled |
| `--libreoffice-allow-list` | `LIBREOFFICE_ALLOW_LIST` | All | Allowed URLs for LibreOffice outbound fetches (regex) |
| `--libreoffice-deny-list` | `LIBREOFFICE_DENY_LIST` | — | Forbidden URLs for LibreOffice outbound fetches (regex) |
| `--libreoffice-deny-private-ips` | `LIBREOFFICE_DENY_PRIVATE_IPS` | `false` | Reject outbound fetches to private IPs |
| `--libreoffice-deny-public-ips` | `LIBREOFFICE_DENY_PUBLIC_IPS` | `false` | Reject outbound fetches to public IPs |
| `--libreoffice-disable-routes` | `LIBREOFFICE_DISABLE_ROUTES` | `false` | Disable all LibreOffice routes |

### Changing the LibreOffice language

Default: English. Build your own Docker image with a different language:

```dockerfile
# From Gotenberg 8.23.1 onwards (Debian Trixie)
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

## PDF Engines module

Gotenberg supports the following PDF engines:

| Feature | ExifTool | PDFtk | pdfcpu | QPDF | UNO |
|---------|----------|-------|--------|------|-----|
| Merge | - | Yes | Yes | Yes | - |
| Split | - | Yes | Yes | Yes | - |
| Flatten | - | - | - | Yes | - |
| PDF/A & PDF/UA | - | - | - | - | Yes |
| Read metadata | Yes | - | - | - | - |
| Write metadata | Yes | - | - | - | - |
| Encrypt | - | Yes | Yes | Yes | - |
| Embed files | - | - | Yes | - | - |
| Factur-X (XMP) | - | - | - | Yes | - |
| Watermark | - | Yes | Yes | - | - |
| Stamp | - | Yes | Yes | - | - |
| Read bookmarks | - | - | Yes | - | - |
| Write bookmarks | - | - | Yes | - | - |
| Rotate | - | Yes | Yes | - | - |

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--pdfengines-merge-engines` | `PDFENGINES_MERGE_ENGINES` | `qpdf,pdfcpu,pdftk` | Engines and order for merge |
| `--pdfengines-split-engines` | `PDFENGINES_SPLIT_ENGINES` | `pdfcpu,qpdf,pdftk` | Engines for split |
| `--pdfengines-flatten-engines` | `PDFENGINES_FLATTEN_ENGINES` | `qpdf` | Engines for flatten |
| `--pdfengines-convert-engines` | `PDFENGINES_CONVERT_ENGINES` | `libreoffice-pdfengine` | Engines for PDF/A conversion |
| `--pdfengines-read-metadata-engines` | `PDFENGINES_READ_METADATA_ENGINES` | `exiftool` | Engines for reading metadata |
| `--pdfengines-write-metadata-engines` | `PDFENGINES_WRITE_METADATA_ENGINES` | `exiftool` | Engines for writing metadata |
| `--pdfengines-encrypt-engines` | `PDFENGINES_ENCRYPT_ENGINES` | `qpdf,pdftk,pdfcpu` | Engines for encryption |
| `--pdfengines-embed-engines` | `PDFENGINES_EMBED_ENGINES` | `pdfcpu` | Engines for file embedding |
| `--pdfengines-embed-metadata-engines` | `PDFENGINES_EMBED_METADATA_ENGINES` | `qpdf` | Engines for embedded metadata |
| `--pdfengines-watermark-engines` | `PDFENGINES_WATERMARK_ENGINES` | `pdfcpu,pdftk` | Engines for watermarks |
| `--pdfengines-stamp-engines` | `PDFENGINES_STAMP_ENGINES` | `pdfcpu,pdftk` | Engines for stamps |
| `--pdfengines-write-bookmarks-engines` | `PDFENGINES_WRITE_BOOKMARKS_ENGINES` | `pdfcpu` | Engines for writing bookmarks |
| `--pdfengines-read-bookmarks-engines` | `PDFENGINES_READ_BOOKMARKS_ENGINES` | `pdfcpu` | Engines for reading bookmarks |
| `--pdfengines-rotate-engines` | `PDFENGINES_ROTATE_ENGINES` | `pdfcpu,pdftk` | Engines for rotate |
| `--pdfengines-factur-x-engines` | `PDFENGINES_FACTUR_X_ENGINES` | `qpdf` | Engines for Factur-X XMP |
| `--pdfengines-disable-routes` | `PDFENGINES_DISABLE_ROUTES` | `false` | Disable all PDF engine routes |

## Webhook module

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--webhook-enable-sync-mode` | `WEBHOOK_ENABLE_SYNC_MODE` | `false` | Enable synchronous webhook mode |
| `--webhook-allow-list` | `WEBHOOK_ALLOW_LIST` | All | Allowed callback URLs (regex) |
| `--webhook-deny-list` | `WEBHOOK_DENY_LIST` | — | Forbidden callback URLs (regex) |
| `--webhook-deny-private-ips` | `WEBHOOK_DENY_PRIVATE_IPS` | `false` | Reject callbacks to private IPs |
| `--webhook-deny-public-ips` | `WEBHOOK_DENY_PUBLIC_IPS` | `false` | Reject callbacks to public IPs |
| `--webhook-disable` | `WEBHOOK_DISABLE` | `false` | Disable the webhook feature entirely |

---
Source: https://gotenberg.dev/docs/configuration
