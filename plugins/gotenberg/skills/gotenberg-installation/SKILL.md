---
name: gotenberg-installation
description: >
  Gotenberg installieren — Docker, Docker Compose, Kubernetes, Cloud Run, AWS Lambda.
  Trigger: "Gotenberg installieren", "Gotenberg Docker", "Gotenberg starten",
  "Gotenberg setup", "Gotenberg image tags", "Gotenberg Kubernetes", "Gotenberg Cloud Run",
  "how to install Gotenberg", "Gotenberg docker-compose", "Gotenberg deployment".
---

# Gotenberg — Installation

Gotenberg laeuft ausschliesslich als Docker-Container. Kein nativer Install.

## Docker (schnellster Start)

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8
# API erreichbar unter http://localhost:3000

# Sicherer: nur localhost binden
docker run --rm -p "127.0.0.1:3000:3000" gotenberg/gotenberg:8
```

## Image-Varianten

| Image | Groesse | Enthaelt |
|-------|---------|---------|
| `gotenberg/gotenberg:8` | Vollstaendig | Chromium + LibreOffice + PDF Engines |
| `gotenberg/gotenberg:8-chromium` | ~30% kleiner | Chromium + PDF Engines |
| `gotenberg/gotenberg:8-libreoffice` | ~40% kleiner | LibreOffice + PDF Engines |

Cloud Run / AWS Lambda: `-cloudrun` / `-aws-lambda` Suffix verwenden.

Vollstaendige Referenz: `references/deep/installation.md`
