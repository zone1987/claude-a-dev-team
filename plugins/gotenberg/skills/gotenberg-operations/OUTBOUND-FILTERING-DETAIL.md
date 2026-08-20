# Gotenberg — Outbound URL Filtering (full reference)

## Contents

- [Concept](#concept)
- [Always-active protection mechanisms](#always-active-protection-mechanisms)
- [Environment variables](#environment-variables)
- [Filter pipeline and precedence](#filter-pipeline-and-precedence)
- [Definition of "non-public IPs"](#definition-of-non-public-ips)
- [Response codes](#response-codes)
- [Configuration examples](#configuration-examples)
- [Notes](#notes)

## Concept

Gotenberg secures all outbound connections against SSRF (server-side request forgery) and unwanted network access. The filter pipeline applies to:

1. **Chromium navigations and sub-resources** (CSS, images, iframes)
2. **Webhook callbacks** (success and error URLs)
3. **`downloadFrom` fetches** (remote files)
4. **LibreOffice references** (linked images, external content)

---

## Always-active protection mechanisms

| Mechanism | Description |
|-------------|-------------|
| **DNS rebind pinning proxy** | All outbound HTTP/HTTPS requests go through an in-process proxy with pinned IPs |
| **`file://` URL blocking** | `file://` URLs are always rejected on URL conversion and screenshot routes → 400 |
| **Per-request asset isolation** | Local HTML assets are restricted to the per-request working directory |
| **LibreOffice linked content blocking** | Content from untrusted sources is blocked before the fetch (from v8.34.0) |

---

## Environment variables

### Chromium module

| Variable | Type | Default | Description |
|----------|-----|---------|--------------|
| `CHROMIUM_DENY_PRIVATE_IPS` | boolean | `false` | Reject Chromium navigations and sub-resources to non-public IPs |
| `CHROMIUM_DENY_PUBLIC_IPS` | boolean | `false` | Reject Chromium navigations to public IPs |
| `CHROMIUM_ALLOW_LIST` | Regex | — | URL regex that bypasses IP class checks |
| `CHROMIUM_PROXY_SERVER` | string | — | Proxy server; disables the DNS rebind pinning proxy when set |
| `CHROMIUM_HOST_RESOLVER_RULES` | string | — | Host resolver rules; disables the DNS rebind pinning proxy when set |

### Webhook module

| Variable | Type | Default | Description |
|----------|-----|---------|--------------|
| `WEBHOOK_DENY_PRIVATE_IPS` | boolean | `false` | Reject webhook URLs to non-public IPs |
| `WEBHOOK_DENY_PUBLIC_IPS` | boolean | `false` | Reject webhook URLs to public IPs |
| `WEBHOOK_ALLOW_LIST` | Regex | — | URL regex that bypasses IP class checks for webhooks |

### API download module

| Variable | Type | Default | Description |
|----------|-----|---------|--------------|
| `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | boolean | `false` | Reject `downloadFrom` URLs to non-public IPs |
| `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | boolean | `false` | Reject `downloadFrom` URLs to public IPs |

### LibreOffice module

| Variable | Type | Default | Description |
|----------|-----|---------|--------------|
| `LIBREOFFICE_DENY_PRIVATE_IPS` | boolean | `false` | Reject LibreOffice outbound fetches to non-public IPs |
| `LIBREOFFICE_DENY_PUBLIC_IPS` | boolean | `false` | Reject LibreOffice outbound fetches to public IPs |
| `LIBREOFFICE_ALLOW_LIST` | Regex | — | URL regex that bypasses IP class checks for LibreOffice |
| `LIBREOFFICE_DENY_LIST` | Regex | — | Block URLs unconditionally (independent of other rules) |

---

## Filter pipeline and precedence

1. **Deny list evaluation** → blocks independently of other rules
2. **Allow list matching** → bypasses IP class checks on a match
3. **IP class variables** → applied when there is no allow list match

---

## Definition of "non-public IPs"

The following address ranges count as non-public:
- Loopback (127.0.0.0/8, ::1)
- RFC1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
- Link-local (169.254.0.0/16, fe80::/10)
- IPv6 unique-local (fc00::/7)
- IPv6 wrappers around non-public IPv4: IPv4-mapped, IPv4-translated, 6to4, Teredo

---

## Response codes

| Code | Scenario |
|------|---------|
| `400 Bad Request` | `file://` URLs on URL conversion / screenshots |
| `403 Forbidden` | URL rejected by the deny list or IP class variables |

---

## Configuration examples

### Block all internal access (maximum security)

```bash
docker run --rm \
  -e CHROMIUM_DENY_PRIVATE_IPS=true \
  -e WEBHOOK_DENY_PRIVATE_IPS=true \
  -e API_DOWNLOAD_FROM_DENY_PRIVATE_IPS=true \
  -e LIBREOFFICE_DENY_PRIVATE_IPS=true \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### Allow only specific internal URLs (allow list)

```bash
docker run --rm \
  -e CHROMIUM_DENY_PRIVATE_IPS=true \
  -e 'CHROMIUM_ALLOW_LIST=https://intern\.meinefirma\.de/.*' \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### Block specific URLs for LibreOffice

```bash
docker run --rm \
  -e 'LIBREOFFICE_DENY_LIST=https://gesperrte-domain\.com/.*' \
  -p 3000:3000 \
  gotenberg/gotenberg:8
```

### Docker Compose configuration

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

## Notes

- From **v8.31.0** private IP blocking was enabled for Chromium (reverted in v8.32.0 back to `false` as the default)
- When `CHROMIUM_PROXY_SERVER` or `CHROMIUM_HOST_RESOLVER_RULES` are set, the DNS rebind pinning proxy is disabled
- LibreOffice linked content blocking (from v8.34.0) **cannot be disabled**

---

Source: https://gotenberg.dev/docs/outbound-url-filtering
