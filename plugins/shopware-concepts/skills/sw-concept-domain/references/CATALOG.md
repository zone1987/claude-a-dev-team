# Shopware product catalogue — concept

Complete concept documentation: `CATALOG-DETAIL.md`

## Quick overview

### Products

- **Self-referencing entity** — parent product + child variants (inheritance)
- **Properties** — not variant-defining (origin, washing instructions)
- **Options** — variant-defining (size, colour)
- **Configurator** — Store API delivers all variant options for selection in the frontend

### Categories

- **Tree structure** — `parentId`, `path`, `level` for breadcrumbs and navigation
- **Types**: `page`, `folder`, `link`
- **CMS layout inheritance** — if `cmsPageId` is missing, it is taken from the parent
- **Dynamic Product Groups** — stream-based assignment instead of manual product assignment
- **SEO** — URL templates and per-sales-channel domain routing

### Sales Channels

- **One Shopware instance, multiple stores** — language, currency, payment methods per channel
- **Domains** — per domain: language + currency + snippet set (separate subdomains recommended)
- **Navigation Roots** — `navigation`, `footer`, `service` category entry points
- **Product Visibility** — products must be set visible per sales channel

Technical implementation: `shopware-core`, `shopware-data` (dev plugins)
