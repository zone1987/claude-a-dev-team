# Sales Agent — Deployment

Full reference: [AGENT-DEPLOYMENT-DEPLOYMENT.md](AGENT-DEPLOYMENT-DEPLOYMENT.md)

## Deployment options

| Option | Redis recommendation |
|--------|-----------------|
| **AWS Amplify** | Amazon ElastiCache or Upstash |
| **Cloudflare Pages** | Upstash (serverless Redis) |
| **Ubuntu Server + PM2** | local or Upstash/Redis Cloud |

> Unlike DSR, Sales Agent **always requires Redis** as a cache layer.
