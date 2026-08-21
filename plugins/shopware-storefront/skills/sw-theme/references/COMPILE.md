# Shopware 6 — Compile a theme & build

Full reference: [COMPILE-DETAIL.md](COMPILE-DETAIL.md)

```bash
# compile SCSS (PHP SASS compiler)
bin/console theme:compile

# read in theme.json changes
bin/console theme:refresh

# build JS (webpack via shopware-cli)
shopware-cli project storefront-build

# dev server with live reload (port 9998)
shopware-cli project storefront-watch
# or (platform/contribution setup, from 6.7.11.0):
composer run storefront:dev-server
```

SCSS is compiled on the PHP side; JS requires Node/webpack (`shopware-cli`).
