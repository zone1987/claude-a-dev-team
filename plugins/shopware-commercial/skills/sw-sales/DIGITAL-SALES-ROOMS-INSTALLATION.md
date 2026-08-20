# Digital Sales Rooms — Installation

Vollständige Referenz: [DIGITAL-SALES-ROOMS-INSTALLATION-INSTALLATION.md](DIGITAL-SALES-ROOMS-INSTALLATION-INSTALLATION.md)

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
