# Sales Agent — overview

Sales Agent is a licensed Shopware app (Beyond or Evolve) that gives
sales representatives an optimized working environment — without the
overhead of the Shopware administration.

![Sales Agent Overview](assets/sales-agent-overview.jpg)

## Architecture

| Layer | Technology |
|---------|------------|
| Frontend | Vue |
| Backend/Server | Nuxt 3 + Nitro |
| Database | MySQL (via Prisma) |
| Cache | Redis (via Nitro Storage) |

![Architecture](assets/sales-agent-architecture.jpg)

Full reference: [AGENT-OVERVIEW.md](AGENT-OVERVIEW.md)

## Related skills

| Topic | Skill |
|-------|-------|
| Installation & app server setup | `sw-sales-agent-setup` |
| Customization (branding, components, i18n) | `sw-sales-agent-customization` |
| Deployment (AWS, Cloudflare, Ubuntu) | `sw-sales-agent-deployment` |
