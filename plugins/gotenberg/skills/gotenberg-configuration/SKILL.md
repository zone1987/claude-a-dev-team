---
name: gotenberg-configuration
description: >
  Gotenberg Konfiguration — alle CLI-Flags und Env-Vars fuer API, Chromium, LibreOffice,
  PDF Engines, Webhook, Logging. Vollstaendige Parametertabellen mit Defaults.
  Trigger: "Gotenberg konfigurieren", "Gotenberg Flags", "Gotenberg Env Vars",
  "Gotenberg Timeout", "Gotenberg Port", "Gotenberg Basic Auth konfigurieren",
  "Gotenberg configure", "Gotenberg settings", "Gotenberg options", "Gotenberg flags".
---

# Gotenberg — Konfiguration

Konfiguration via CLI-Flags oder Umgebungsvariablen.
Flag-Format: `--modul-eigenschaft=wert` / Env: `MODUL_EIGENSCHAFT=wert`

```bash
# CLI-Flag
docker run --rm -p "3000:3000" gotenberg/gotenberg:8 gotenberg --api-timeout=60s

# Umgebungsvariable
docker run --rm -p "3000:3000" -e API_TIMEOUT=60s gotenberg/gotenberg:8
```

## Wichtigste Parameter (Auszug)

| Flag | Env | Default | Beschreibung |
|------|-----|---------|-------------|
| `--api-port` | `API_PORT` | `3000` | Lausch-Port der API |
| `--api-timeout` | `API_TIMEOUT` | `30s` | Maximale Request-Dauer |
| `--api-enable-basic-auth` | `API_ENABLE_BASIC_AUTH` | `false` | Basic Auth aktivieren |
| `--chromium-max-concurrency` | `CHROMIUM_MAX_CONCURRENCY` | `6` | Max. parallele Chromium-Konvertierungen |
| `--libreoffice-restart-after` | `LIBREOFFICE_RESTART_AFTER` | `10` | LibreOffice nach N Konvertierungen neu starten |

Vollstaendige Parametertabellen: `references/deep/configuration.md`
