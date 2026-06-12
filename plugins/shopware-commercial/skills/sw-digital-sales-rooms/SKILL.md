---
name: sw-digital-sales-rooms
description: >
  Überblick über Digital Sales Rooms: Architektur, Voraussetzungen, Komponenten
  und Einstiegspunkt für alle DSR-Entwicklerthemen.
  Triggers: "Digital Sales Rooms", "DSR", "Live-Video-Shopping", "live shopping",
  "dsr-frontends", "SwagDigitalSalesRooms", "digital sales room overview"
---

# Digital Sales Rooms — Überblick

Digital Sales Rooms (DSR) ist eine lizenzpflichtige Shopware-Erweiterung
(Shopware Beyond), die interaktive Live-Video-Shopping-Events direkt aus dem
Shopware-Backend heraus ermöglicht.

## Architektur

DSR ist **kein Teil des Standard-Storefronts**. Es handelt sich um eine
eigenständige Nuxt-3-Frontend-App (`dsr-frontends`), die auf einer separaten
Domain gehostet wird und zwei externe Realtime-Dienste benötigt:

- **Daily.co** — Echtzeit-Video/Audio
- **Mercure** — Server-Push-Updates

Vollständige Referenz: [references/deep/overview.md](references/deep/overview.md)

## Verwandte Skills

| Thema | Skill |
|-------|-------|
| Installation (Plugin + Frontend) | `sw-digital-sales-rooms-installation` |
| Konfiguration (Domain, CLI, Plugin) | `sw-digital-sales-rooms-config` |
| Anpassung (Branding, Komponenten, i18n) | `sw-digital-sales-rooms-customization` |
| 3rd-Party (Mercure, Daily.co) | `sw-digital-sales-rooms-3rdparty` |
| Deployment (AWS, Cloudflare, Ubuntu) | `sw-digital-sales-rooms-deployment` |
