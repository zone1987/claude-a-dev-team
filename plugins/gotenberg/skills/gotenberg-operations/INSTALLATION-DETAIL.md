# Gotenberg — Complete installation guide

## Contents

- [Security notice](#security-notice)
- [Live Demo](#live-demo)
- [Docker](#docker)
- [Image variants](#image-variants)
- [Feature availability by image](#feature-availability-by-image)
- [Docker Compose](#docker-compose)
- [Kubernetes](#kubernetes)
- [Cloud Run](#cloud-run)
- [AWS Lambda (Beta)](#aws-lambda-beta)

## Security notice

**Do NOT expose Gotenberg on the public internet.** Treat it like a database:
keep it behind your own firewall.

## Live Demo

Try it without installing: https://demo.gotenberg.dev

```bash
curl \
  --request POST https://demo.gotenberg.dev/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o my.pdf
```

Demo limitations: 2 req/s per IP, 5 MB body limit, runs on Render (512 MB RAM, 0.5 CPU).

## Docker

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8
```

API reachable at http://localhost:3000.

More secure (localhost only):
```bash
docker run --rm -p "127.0.0.1:3000:3000" gotenberg/gotenberg:8
```

## Image variants

| Image | Size | Chromium | LibreOffice | PDF Engines |
|-------|---------|----------|-------------|-------------|
| `gotenberg/gotenberg:8` | Complete | Yes | Yes | Yes |
| `gotenberg/gotenberg:8-chromium` | ~30% smaller | Yes | No | Yes |
| `gotenberg/gotenberg:8-libreoffice` | ~40% smaller | No | Yes | Yes |

All variants include PDF Engines (merge, split, encrypt, watermarks, metadata, ...).

## Feature availability by image

| Feature | Full | Chromium | LibreOffice |
|---------|------|----------|-------------|
| URL/HTML/Markdown to PDF | Yes | Yes | No |
| Screenshots | Yes | Yes | No |
| Office documents (.docx, .xlsx, .pptx, ...) | Yes | No | Yes |
| Merge, split, rotate, flatten | Yes | Yes | Yes |
| Encrypt, watermarks, stamps | Yes | Yes | Yes |
| Metadata & bookmarks | Yes | Yes | Yes |
| File attachments | Yes | Yes | Yes |
| Factur-X / ZUGFeRD e-invoicing | Yes | No | Yes |
| PDF/A & PDF/UA conversion | Yes | No | Yes |
| Webhooks & async | Yes | Yes | Yes |
| Download From (remote URLs) | Yes | Yes | Yes |

## Docker Compose

```yaml
# compose.yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "127.0.0.1:3000:3000"
```

Other services in the same Compose network reach Gotenberg at `gotenberg:3000`.

With port exposure on the host:
```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "3000:3000"
      # More secure:
      # - "127.0.0.1:3000:3000"
```

## Kubernetes

The container runs as the non-root user `gotenberg` (UID/GID 1001).
From 8.21.0 onwards, arbitrary user IDs (OpenShift) are supported as well.

Pod deployment spec (security context):
```yaml
securityContext:
  readOnlyRootFilesystem: false
  allowPrivilegeEscalation: false
  privileged: false
  runAsUser: 1001  # omit for an arbitrarily assigned user ID
```

Minimum resources: **512 Mi memory**, **0.2 CPU**.

Community Helm chart: https://artifacthub.io/packages/helm/maikumori/gotenberg

## Cloud Run

Image tags with the `-cloudrun` suffix:
```
gotenberg/gotenberg:8-cloudrun
gotenberg/gotenberg:8-chromium-cloudrun
gotenberg/gotenberg:8-libreoffice-cloudrun
```

Cloud Run specifics:
- Uses the `PORT` environment variable from Cloud Run
- Logs in a Cloud Run compatible format
- Starts Chromium and LibreOffice automatically at init (faster readiness)
- Synchronous webhook mode (Cloud Run stops containers when inactive)

Minimum recommendation: **1 Gi memory**.
Tip: enable HTTP/2 to work around the 32 MB request limit.

## AWS Lambda (Beta)

Available on `linux/amd64` and `linux/arm64`:
```
gotenberg/gotenberg:8-aws-lambda
gotenberg/gotenberg:8-chromium-aws-lambda
gotenberg/gotenberg:8-libreoffice-aws-lambda
```

Configuration for AWS Lambda:
- `AWS_LWA_PORT` — port of the API (read by Gotenberg)
- `AWS_LWA_READINESS_CHECK_PATH` — set to `/health`
- `AWS_LWA_INVOKE_MODE` — set to `buffered`
- Synchronous webhook mode (AWS stops containers when inactive)

The `buffered` mode supports responses up to **6 MB**.
Larger outputs: use the webhook feature and upload results to S3.

More AWS options: https://github.com/awslabs/aws-lambda-web-adapter

---
Source: https://gotenberg.dev/docs/getting-started/installation
