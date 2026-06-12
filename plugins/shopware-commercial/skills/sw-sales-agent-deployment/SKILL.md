---
name: sw-sales-agent-deployment
description: >
  Deployment der Sales-Agent-App: AWS Amplify (mit ElastiCache/Upstash Redis),
  Cloudflare Pages (mit Upstash Redis), Ubuntu Server mit PM2 (lokales Redis).
  Triggers: "sales agent deployen", "deploy sales agent", "sales agent aws amplify",
  "sales agent cloudflare pages", "sales agent ubuntu pm2", "sales agent redis setup",
  "sales agent upstash", "sales agent elasticache", "sales agent github actions"
---

# Sales Agent — Deployment

Vollständige Referenz: [references/deep/deployment.md](references/deep/deployment.md)

## Deployment-Optionen

| Option | Redis-Empfehlung |
|--------|-----------------|
| **AWS Amplify** | Amazon ElastiCache oder Upstash |
| **Cloudflare Pages** | Upstash (serverless Redis) |
| **Ubuntu Server + PM2** | Lokal oder Upstash/Redis Cloud |

> Im Gegensatz zu DSR benötigt Sales Agent **immer Redis** als Cache-Layer.
