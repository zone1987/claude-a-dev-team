---
name: sw-theme-create
description: >
  Shopware 6 Theme via CLI erstellen: theme:create, Verzeichnisstruktur, plugin:install --activate,
  theme:change (SalesChannel-Zuweisung), theme.json-Gerüst komplett. Trigger: "Theme erstellen CLI",
  "theme:create", "neues Theme anlegen", "Theme Verzeichnisstruktur", "Theme Schritte",
  "Theme installieren aktivieren", "create theme shopware". Shopware 6.7.
---

# Shopware 6 — Theme erstellen (CLI)

Vollständige Schritt-für-Schritt-Anleitung: [references/deep/theme-create.md](references/deep/theme-create.md)

```bash
bin/console theme:create SwagBasicExampleTheme
bin/console plugin:refresh
bin/console plugin:install --activate SwagBasicExampleTheme
bin/console theme:change   # interaktiv: SalesChannel → Theme auswählen
```

Pflicht-Datei: `src/Resources/theme.json` + PHP-Klasse mit `implements ThemeInterface`.
Troubleshooting: `theme:compile`, `cache:clear`, Logs in `var/log/`.
