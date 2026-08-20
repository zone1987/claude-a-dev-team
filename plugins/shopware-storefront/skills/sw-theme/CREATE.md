# Shopware 6 — Create a theme (CLI)

Full step-by-step guide: [CREATE-DETAIL.md](CREATE-DETAIL.md)

```bash
bin/console theme:create SwagBasicExampleTheme
bin/console plugin:refresh
bin/console plugin:install --activate SwagBasicExampleTheme
bin/console theme:change   # interactive: select sales channel → theme
```

Required file: `src/Resources/theme.json` plus a PHP class with `implements ThemeInterface`.
Troubleshooting: `theme:compile`, `cache:clear`, logs in `var/log/`.
