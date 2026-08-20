# Sales Agent — Deployment

Vollständige Referenz: [AGENT-DEPLOYMENT-DEPLOYMENT.md](AGENT-DEPLOYMENT-DEPLOYMENT.md)

## Deployment-Optionen

| Option | Redis-Empfehlung |
|--------|-----------------|
| **AWS Amplify** | Amazon ElastiCache oder Upstash |
| **Cloudflare Pages** | Upstash (serverless Redis) |
| **Ubuntu Server + PM2** | Lokal oder Upstash/Redis Cloud |

> Im Gegensatz zu DSR benötigt Sales Agent **immer Redis** als Cache-Layer.
