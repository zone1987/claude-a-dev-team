---
name: sw-sales-agent
description: >
  Überblick über die Sales-Agent-App: Architektur (Nuxt/Nitro/Prisma/Redis),
  Lizenz, API-Dokumentation und Einstiegspunkt für alle SA-Entwicklerthemen.
  Triggers: "Sales Agent", "sales agent app", "swag sales agent", "swagsalesagent",
  "sales representative app shopware", "sales agent architektur",
  "sales agent overview", "shopware sales agent"
---

# Sales Agent — Überblick

Sales Agent ist eine lizenzpflichtige Shopware-App (Beyond oder Evolve),
die Vertriebsmitarbeitern eine optimierte Arbeitsumgebung bietet — ohne
den Overhead der Shopware-Administration.

![Sales Agent Overview](assets/sales-agent-overview.jpg)

## Architektur

| Schicht | Technologie |
|---------|------------|
| Frontend | Vue |
| Backend/Server | Nuxt 3 + Nitro |
| Datenbank | MySQL (via Prisma) |
| Cache | Redis (via Nitro Storage) |

![Architektur](assets/sales-agent-architecture.jpg)

Vollständige Referenz: [references/deep/overview.md](references/deep/overview.md)

## Verwandte Skills

| Thema | Skill |
|-------|-------|
| Installation & App-Server-Setup | `sw-sales-agent-setup` |
| Anpassung (Branding, Komponenten, i18n) | `sw-sales-agent-customization` |
| Deployment (AWS, Cloudflare, Ubuntu) | `sw-sales-agent-deployment` |
