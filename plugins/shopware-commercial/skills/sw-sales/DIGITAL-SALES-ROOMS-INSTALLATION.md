# Digital Sales Rooms — Installation

Full reference: [DIGITAL-SALES-ROOMS-INSTALLATION-INSTALLATION.md](DIGITAL-SALES-ROOMS-INSTALLATION-INSTALLATION.md)

## Quick guide

### 1. Install the plugin (admin side)

```bash
bin/console plugin:refresh
bin/console plugin:install SwagDigitalSalesRooms --activate
bin/console cache:clear
```

### 2. Start the frontend app

```bash
cd ./templates/dsr-frontends
cp .env.template .env
# fill in .env (ORIGIN, SHOPWARE_STOREFRONT_URL, SHOPWARE_STORE_API, ...)
pnpm install
pnpm dev        # development
pnpm build      # production
```
