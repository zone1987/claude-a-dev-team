# Gotenberg — Configuration

Configuration via CLI flags or environment variables.
Flag format: `--module-property=value` / Env: `MODULE_PROPERTY=value`

```bash
# CLI flag
docker run --rm -p "3000:3000" gotenberg/gotenberg:8 gotenberg --api-timeout=60s

# Environment variable
docker run --rm -p "3000:3000" -e API_TIMEOUT=60s gotenberg/gotenberg:8
```

## Most important parameters (excerpt)

| Flag | Env | Default | Description |
|------|-----|---------|-------------|
| `--api-port` | `API_PORT` | `3000` | Listening port of the API |
| `--api-timeout` | `API_TIMEOUT` | `30s` | Maximum request duration |
| `--api-enable-basic-auth` | `API_ENABLE_BASIC_AUTH` | `false` | Enable basic auth |
| `--chromium-max-concurrency` | `CHROMIUM_MAX_CONCURRENCY` | `6` | Max. parallel Chromium conversions |
| `--libreoffice-restart-after` | `LIBREOFFICE_RESTART_AFTER` | `10` | Restart LibreOffice after N conversions |

Complete parameter tables: `CONFIGURATION-DETAIL.md`
