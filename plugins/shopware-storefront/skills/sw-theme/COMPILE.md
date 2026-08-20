# Shopware 6 — Theme kompilieren & Build

Vollständige Referenz: [COMPILE-DETAIL.md](COMPILE-DETAIL.md)

```bash
# SCSS kompilieren (PHP SASS Compiler)
bin/console theme:compile

# theme.json-Änderungen einlesen
bin/console theme:refresh

# JS bauen (webpack via shopware-cli)
shopware-cli project storefront-build

# Dev-Server mit Live-Reload (Port 9998)
shopware-cli project storefront-watch
# oder (platform/contribution setup, ab 6.7.11.0):
composer run storefront:dev-server
```

SCSS wird PHP-seitig kompiliert; JS braucht Node/webpack (`shopware-cli`).
