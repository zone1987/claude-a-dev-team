# Shopware 6 — Mehrere Themes & SalesChannel-Zuweisung

Vollständige Referenz: [MULTIPLE-DETAIL.md](MULTIPLE-DETAIL.md)

**Muster:** Ein Basis-Theme (Corporate Design), abgeleitete Themes für SalesChannels/Aktionen.

```json
// Abgeleitetes Theme: theme.json
{
  "name": "SwagHolidayTheme",
  "configInheritance": ["@Storefront", "@SwagBasicExampleTheme"],
  "config": {
    "fields": {
      "sw-color-brand-primary": { "type": "color", "value": "#cc0000" }
    }
  }
}
```

```bash
bin/console theme:change   # pro SalesChannel interaktiv auswählen
```

`configInheritance` erbt Felder + Snippets; Werte aus Parent werden übernommen, sofern nicht
explizit überschrieben. Relationship wird bei `plugin:install` gesetzt, Update via `theme:refresh`.
