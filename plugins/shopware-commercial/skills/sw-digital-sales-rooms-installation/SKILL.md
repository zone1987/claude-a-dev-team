---
name: sw-digital-sales-rooms-installation
description: >
  Installation von Digital Sales Rooms: Plugin via Composer/Download installieren
  und aktivieren, Frontend-App (dsr-frontends) einrichten und starten.
  Triggers: "DSR installieren", "install digital sales rooms", "dsr-frontends setup",
  "SwagDigitalSalesRooms install", "plugin:install SwagDigitalSalesRooms",
  "DSR frontend app", "dsr env setup", "pnpm dev dsr"
---

# Digital Sales Rooms — Installation

Vollständige Referenz: [references/deep/installation.md](references/deep/installation.md)

## Kurzanleitung

### 1. Plugin installieren (Admin-Seite)

```bash
bin/console plugin:refresh
bin/console plugin:install SwagDigitalSalesRooms --activate
bin/console cache:clear
```

### 2. Frontend-App starten

```bash
cd ./templates/dsr-frontends
cp .env.template .env
# .env befüllen (ORIGIN, SHOPWARE_STOREFRONT_URL, SHOPWARE_STORE_API, ...)
pnpm install
pnpm dev        # Entwicklung
pnpm build      # Produktion
```
