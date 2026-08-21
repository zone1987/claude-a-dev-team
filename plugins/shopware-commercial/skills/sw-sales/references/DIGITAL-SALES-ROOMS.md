# Digital Sales Rooms — overview

Digital Sales Rooms (DSR) is a licensed Shopware extension
(Shopware Beyond) that enables interactive live video shopping events directly
from the Shopware backend.

## Architecture

DSR is **not part of the standard Storefront**. It is a
stand-alone Nuxt 3 frontend app (`dsr-frontends`) that is hosted on a separate
domain and requires two external realtime services:

- **Daily.co** — realtime video/audio
- **Mercure** — server push updates

Full reference: [DIGITAL-SALES-ROOMS-OVERVIEW.md](DIGITAL-SALES-ROOMS-OVERVIEW.md)

## Related skills

| Topic | Skill |
|-------|-------|
| Installation (Plugin + Frontend) | `sw-digital-sales-rooms-installation` |
| Configuration (domain, CLI, plugin) | `sw-digital-sales-rooms-config` |
| Customization (branding, components, i18n) | `sw-digital-sales-rooms-customization` |
| 3rd-Party (Mercure, Daily.co) | `sw-digital-sales-rooms-3rdparty` |
| Deployment (AWS, Cloudflare, Ubuntu) | `sw-digital-sales-rooms-deployment` |
