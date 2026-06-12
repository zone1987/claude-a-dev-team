---
name: sw-theme-compile
description: >
  Shopware 6 Theme kompilieren: theme:compile, theme:refresh, Dev-Server/Watch (shopware-cli storefront-watch,
  composer run storefront:dev-server), JS-Build via shopware-cli/webpack, atomic compilation.
  Trigger: "Theme kompilieren", "theme:compile", "theme kompilieren CLI", "storefront-watch",
  "Theme bauen", "SCSS kompilieren Theme", "JS bauen Theme", "dev server storefront". Shopware 6.7.
---

# Shopware 6 — Theme kompilieren & Build

Vollständige Referenz: [references/deep/theme-compile.md](references/deep/theme-compile.md)

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
