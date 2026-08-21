# Gotenberg — installation

Gotenberg runs exclusively as a Docker container. There is no native install.

## Docker (fastest start)

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8
# API reachable at http://localhost:3000

# Safer: bind to localhost only
docker run --rm -p "127.0.0.1:3000:3000" gotenberg/gotenberg:8
```

## Image variants

| Image | Size | Contains |
|-------|---------|---------|
| `gotenberg/gotenberg:8` | Complete | Chromium + LibreOffice + PDF Engines |
| `gotenberg/gotenberg:8-chromium` | ~30% smaller | Chromium + PDF Engines |
| `gotenberg/gotenberg:8-libreoffice` | ~40% smaller | LibreOffice + PDF Engines |

Cloud Run / AWS Lambda: use the `-cloudrun` / `-aws-lambda` suffix.

Complete reference: `INSTALLATION-DETAIL.md`
