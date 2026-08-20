# Sales Agent — Vollständige Referenz

## Was ist Sales Agent?

Sales Agent ist eine lizenzpflichtige Shopware-Anwendung (nicht Open Source),
die Kommunikations- und Verkaufsprozesse zwischen Vertriebsmitarbeitern und
Kunden optimiert. Sie integriert Shopware in einer schlanken Umgebung ohne den
Overhead der vollständigen Administration.

![Sales Agent Overview](../../assets/sales-agent-overview.jpg)

> **Zugang:** Support-Ticket in [Shopware Account](https://account.shopware.com)
> eröffnen. Zugang wird nach kurzer Validierung oder beim Kauf einer
> Beyond/Evolve-Lizenz gewährt.

> **Architektur-Hinweis:** Sales Agent gehört **nicht** zum Shopware-Standard-
> Storefront. Es ist eine eigenständige Nuxt-3-App auf separater Domain.

## Mindestanforderungen

| Komponente | Version/Anforderung |
|-----------|---------------------|
| Node.js | >= 18 |
| pnpm | >= 8 |
| Shopware Frontends | Nuxt 3-basiert |
| Shopware 6 | >= 6.7.3 |
| Datenbank | MySQL |
| Lizenz | Beyond oder Evolve |

## Architektur-Detail

```
Browser ──── Sales Agent Frontend (Vue/Nuxt 3)    separater Hostname
                     │
                     ├── Nitro Server Engine
                     │     ├── Prisma → MySQL
                     │     └── Redis Cache (Nitro Storage Layer)
                     │
                     └── Shopware Backend
```

![Architektur](../../assets/sales-agent-architecture.jpg)

## API-Dokumentation

Detaillierte API-Informationen:
[shopware.stoplight.io/docs/swag-sales-agent/](https://shopware.stoplight.io/docs/swag-sales-agent/)

## Skill-Übersicht

- Setup/Installation → `sw-sales-agent-setup`
- Customization → `sw-sales-agent-customization`
- Deployment → `sw-sales-agent-deployment`
