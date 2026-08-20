# Shopware 6 — Theme erstellen (CLI)

Vollständige Schritt-für-Schritt-Anleitung: [CREATE-DETAIL.md](CREATE-DETAIL.md)

```bash
bin/console theme:create SwagBasicExampleTheme
bin/console plugin:refresh
bin/console plugin:install --activate SwagBasicExampleTheme
bin/console theme:change   # interaktiv: SalesChannel → Theme auswählen
```

Pflicht-Datei: `src/Resources/theme.json` + PHP-Klasse mit `implements ThemeInterface`.
Troubleshooting: `theme:compile`, `cache:clear`, Logs in `var/log/`.
