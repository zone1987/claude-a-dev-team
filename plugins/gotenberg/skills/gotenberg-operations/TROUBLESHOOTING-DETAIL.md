# Gotenberg — Troubleshooting (Full Reference)

## Contents

- [API problems](#api-problems)
- [Chromium problems](#chromium-problems)
- [LibreOffice problems](#libreoffice-problems)
- [Webhook problems](#webhook-problems)
- [General debugging strategy](#general-debugging-strategy)
- [Version upgrade checklist](#version-upgrade-checklist)

## API problems

### 400 Bad Request

**Causes:**
- Required fields are missing
- Malformed JSON in form fields
- Unsupported file extensions
- Invalid field values

**Solution:** Match the `Gotenberg-Trace` header from the response against the logs for details about the missing/invalid field.

---

## Chromium problems

### Empty / missing content

| Cause | Solution |
|---------|---------|
| JavaScript rendering not finished yet | Use `waitDelay` or `waitForExpression` |
| Background elements missing | `printBackground=true` or CSS `-webkit-print-color-adjust: exact` |
| Content loads after the network idle event | Set `skipNetworkIdleEvent=false` |

### Empty charts / Google Maps (versions 8.29.0 - 8.31.0)

**Cause:** chromedp 0.15.0 blocked `requestAnimationFrame`, `ResizeObserver`, `IntersectionObserver` and CSS transitions/animations between page load and PDF generation — this prevented chart libraries from rendering.

**Solution:** Upgrade to **v8.32.0+** (reverted to chromedp v0.14.2).

Affected issues: #1531, #1534, #1535

### Sub-resources no longer load (after v8.31.0)

**Cause:** v8.31.0 blocked private-IP sub-resources by default, which blocked CSS/images/iframes on internal hostnames.

**Solution:** v8.32.0 restored the permissive defaults. For strict mode: set `CHROMIUM_DENY_PRIVATE_IPS=true`.

### Localhost / missing assets

| Problem | Solution |
|---------|---------|
| Container cannot find `localhost` | Use the host's real network IP or `host.docker.internal` (Docker) |
| CSS/fonts/images missing | Send the files as additional files in the multipart request OR embed them as Base64 data URIs OR make the assets publicly accessible |

### Large PDFs

| Cause | Solution |
|---------|---------|
| Web fonts | Configure your own fonts (fonts configuration, issue #521) |
| Duplicated images | Known Chromium bug (#1077) — currently no fix |

### Startup errors

- Increase the startup timeout in the Chromium module configuration
- macOS Docker Desktop: disable "Use Virtualization Framework" (issue #792)

### Liveness probe failures under load (before v8.33.0)

**Problem:** A single slow health probe under high load triggered an "unhealthy" status, causing Kubernetes to restart healthy pods.

**Fixed in v8.33.0:**
- Tolerates a transient failing probe
- Briefly caches successful probe results
- Prevents probe spam from overloading processes
- Dead processes are detected on the next check

Issue: #1561

### Print Error -32000

**Causes:**
1. Converting very large documents (known Chromium bug)
2. Unusually large headers/footers

**Solutions:**
- Increase container memory
- Reduce header/footer size
- Check the document size (issue #788)

### Truncated screenshots

**Problem:** Screenshots repeat themselves or appear truncated.

**Solution:** Set `skipNetworkIdleEvent=false` (issue #1065).

### Timeouts (503)

**Diagnosis:**
1. Is the Gotenberg instance overloaded?
2. Are the target page's resources responding slowly?
3. Is the target page reachable?

**Solutions:**
- Scale horizontally (more Gotenberg instances)
- Increase the API timeout in the API module configuration
- Define a maximum queue size (faster abort)

---

## LibreOffice problems

### Layout & font shifts

**Cause:** Missing system fonts force substitute fonts — this shifts page breaks and layout.

**Solutions:**
- Install the required fonts via your own Dockerfile
- Consult the fonts configuration

**Change as of v8.30.0:** Font stack reduced from 30+ to 8 packages. Microsoft Core Fonts (Arial, Times New Roman, Calibri) now use metric-compatible substitute fonts.

**After upgrading:** Install `ttf-mscorefonts-installer` or specific script fonts.

### Linked images missing (after v8.34.0)

**Change:** Content from untrusted sources is blocked; uploaded documents are considered untrusted.

**Behavior:** The conversion returns `200 OK`, but images/linked content are missing.

**Workaround:** Embed content directly in documents instead of linking it.

**Note:** No opt-out possible — this blocks security vulnerabilities (local file read and SSRF).

### Server error (500)

**Cause:** Document conversion is resource-intensive.

**Solution:** Increase memory and CPU allocation (issue #465).

### UUID in CSV page headers (before v8.34.0)

**Problem:** A random UUID appeared as a centered header in CSV conversions.

**Cause:** LibreOffice named the Calc sheet after the input file name; Gotenberg stored files with UUID-based names, which triggered the default page header.

**Fixed in v8.34.0:** The auto-generated header is suppressed for CSV inputs.

**Note:** XLSX/ODS with their own page styles are not affected (issue #1568).

### Startup errors

**Solutions:**
1. Increase the startup timeout (LibreOffice module configuration)
2. Debian users: make sure the distribution is up to date
3. Synology/Paperless-ngx: consult the specific configuration comment (issue #763)

Issue: #794

### First request times out, subsequent requests fail (before v8.32.0)

**Problem:** The supervisor cached the initial startup error and returned the identical error to all subsequent requests when `LIBREOFFICE_START_TIMEOUT` was shorter than the soffice cold-start duration.

**Fixed in v8.32.0:** Failed starts reset the state; the next request starts over.

**Temporary solution (older versions):** Increase `LIBREOFFICE_START_TIMEOUT` (default: 20s) beyond the soffice cold-start time (issue #1538).

### PDF/A-1a support

**Since LibreOffice 7.6:** PDF/A-1a is no longer supported. Previous behavior: generated PDF/A-1b files (sometimes misidentified by validators).

---

## Webhook problems

### HTTPS webhooks fail (Chromium variant before v8.34.0)

**Problem:** The `gotenberg/gotenberg:8-chromium` image did not include `ca-certificates` — TLS verification errors with HTTPS webhook endpoints.

**Note:** The conversions themselves are not affected (Chromium bundles its own certificates).

**Fixed in v8.34.0:** ca-certificates is now included.

**For older versions:** Install `ca-certificates` via your own Dockerfile.

**Other variants:** The full and LibreOffice variants were never affected.

---

## General debugging strategy

1. **Use the trace ID:** search the logs for the `Gotenberg-Trace` header to get detailed error messages
2. **Enable the debug route:** `API_ENABLE_DEBUG_ROUTE=true` → `GET /debug` for configuration info
3. **Check the version:** `GET /version` — many bugs are fixed in newer versions
4. **Health check:** `GET /health` for module status
5. **Check resources:** many timeouts and errors are memory/CPU problems

---

## Version upgrade checklist

| From → To | What to check |
|-----------|---------------|
| < 8.30.0 → 8.30.0+ | Check font packages (ttf-mscorefonts, script fonts) |
| < 8.32.0 → 8.32.0+ | Check the LibreOffice start timeout |
| < 8.33.0 → 8.33.0+ | Check the Kubernetes liveness probe configuration |
| < 8.34.0 → 8.34.0+ | Linked images in LibreOffice documents → embed them; check the webhook TLS configuration |

---

Source: https://gotenberg.dev/docs/troubleshooting
