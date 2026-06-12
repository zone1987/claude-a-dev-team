# Gotenberg — Vollstaendige Installationsanleitung

## Sicherheitshinweis

**Gotenberg NICHT im oeffentlichen Internet exponieren.** Wie eine Datenbank behandeln:
hinter der eigenen Firewall halten.

## Live Demo

Ohne Installation testen: https://demo.gotenberg.dev

```bash
curl \
  --request POST https://demo.gotenberg.dev/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o my.pdf
```

Demo-Beschraenkungen: 2 req/s pro IP, 5 MB Body-Limit, laeuft auf Render (512 MB RAM, 0.5 CPU).

## Docker

```bash
docker run --rm -p "3000:3000" gotenberg/gotenberg:8
```

API erreichbar unter http://localhost:3000.

Sicherer (nur localhost):
```bash
docker run --rm -p "127.0.0.1:3000:3000" gotenberg/gotenberg:8
```

## Image-Varianten

| Image | Groesse | Chromium | LibreOffice | PDF Engines |
|-------|---------|----------|-------------|-------------|
| `gotenberg/gotenberg:8` | Vollstaendig | Ja | Ja | Ja |
| `gotenberg/gotenberg:8-chromium` | ~30% kleiner | Ja | Nein | Ja |
| `gotenberg/gotenberg:8-libreoffice` | ~40% kleiner | Nein | Ja | Ja |

Alle Varianten enthalten PDF Engines (Merge, Split, Encrypt, Wasserzeichen, Metadaten, ...).

## Feature-Verfuegbarkeit nach Image

| Feature | Full | Chromium | LibreOffice |
|---------|------|----------|-------------|
| URL/HTML/Markdown zu PDF | Ja | Ja | Nein |
| Screenshots | Ja | Ja | Nein |
| Office-Dokumente (.docx, .xlsx, .pptx, ...) | Ja | Nein | Ja |
| Merge, Split, Rotate, Flatten | Ja | Ja | Ja |
| Encrypt, Wasserzeichen, Stempel | Ja | Ja | Ja |
| Metadaten & Lesezeichen | Ja | Ja | Ja |
| Dateianhange | Ja | Ja | Ja |
| Factur-X / ZUGFeRD E-Invoicing | Ja | Nein | Ja |
| PDF/A & PDF/UA Konvertierung | Ja | Nein | Ja |
| Webhooks & Async | Ja | Ja | Ja |
| Download From (Remote URLs) | Ja | Ja | Ja |

## Docker Compose

```yaml
# compose.yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "127.0.0.1:3000:3000"
```

Andere Services im selben Compose-Netzwerk erreichen Gotenberg unter `gotenberg:3000`.

Mit Port-Exposure auf dem Host:
```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "3000:3000"
      # Sicherer:
      # - "127.0.0.1:3000:3000"
```

## Kubernetes

Der Container laeuft als Non-Root-User `gotenberg` (UID/GID 1001).
Ab 8.21.0 werden auch beliebige User-IDs (OpenShift) unterstuetzt.

Pod-Deployment-Spec (Security Context):
```yaml
securityContext:
  readOnlyRootFilesystem: false
  allowPrivilegeEscalation: false
  privileged: false
  runAsUser: 1001  # weglassen bei beliebig zugewiesener User-ID
```

Mindest-Ressourcen: **512 Mi Memory**, **0.2 CPU**.

Community Helm Chart: https://artifacthub.io/packages/helm/maikumori/gotenberg

## Cloud Run

Image-Tags mit `-cloudrun`-Suffix:
```
gotenberg/gotenberg:8-cloudrun
gotenberg/gotenberg:8-chromium-cloudrun
gotenberg/gotenberg:8-libreoffice-cloudrun
```

Besonderheiten Cloud Run:
- Nutzt die `PORT`-Umgebungsvariable von Cloud Run
- Logs im Cloud-Run-kompatiblen Format
- Startet Chromium und LibreOffice automatisch beim Init (schnellere Bereitschaft)
- Synchroner Webhook-Modus (Cloud Run stoppt Container bei Inaktivitaet)

Mindest-Empfehlung: **1 Gi Memory**.
Tipp: HTTP/2 aktivieren, um das 32 MB Request-Limit zu umgehen.

## AWS Lambda (Beta)

Verfuegbar auf `linux/amd64` und `linux/arm64`:
```
gotenberg/gotenberg:8-aws-lambda
gotenberg/gotenberg:8-chromium-aws-lambda
gotenberg/gotenberg:8-libreoffice-aws-lambda
```

Konfiguration fuer AWS Lambda:
- `AWS_LWA_PORT` — Port der API (wird von Gotenberg ausgelesen)
- `AWS_LWA_READINESS_CHECK_PATH` — auf `/health` setzen
- `AWS_LWA_INVOKE_MODE` — auf `buffered` setzen
- Synchroner Webhook-Modus (AWS stoppt Container bei Inaktivitaet)

`buffered`-Modus unterstuetzt Responses bis **6 MB**.
Groessere Outputs: Webhook-Feature verwenden und Ergebnisse in S3 hochladen.

Mehr AWS-Optionen: https://github.com/awslabs/aws-lambda-web-adapter

---
Quelle: https://gotenberg.dev/docs/getting-started/installation
