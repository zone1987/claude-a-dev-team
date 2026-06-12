---
name: sw-digital-sales-rooms-deployment
description: >
  Deployment der Digital Sales Rooms Frontend-App: AWS Amplify, Cloudflare Pages
  (inkl. GitHub Actions Pipeline) und Ubuntu Server mit PM2.
  Triggers: "DSR deployment", "deploy digital sales rooms", "dsr aws amplify",
  "dsr cloudflare pages", "dsr ubuntu server pm2", "dsr github actions deploy",
  "nuxi build cloudflare_pages dsr", "dsr wrangler deploy", "dsr saas deployment"
---

# Digital Sales Rooms — Deployment

Vollständige Referenz: [references/deep/deployment.md](references/deep/deployment.md)

## Deployment-Optionen

| Option | Vorteile |
|--------|---------|
| **AWS Amplify** | Git-Push-Deployment, managed |
| **Cloudflare Pages** | Edge-Deployment, GitHub Actions |
| **Ubuntu Server + PM2** | Self-hosted, volle Kontrolle |

## SaaS (Beyond)

Im SaaS-Betrieb ist das Plugin bereits installiert. Nur noch tun:
1. Frontend-App deployen (eine der Optionen oben)
2. 3rd-Party-Dienste konfigurieren
3. Plugin konfigurieren
