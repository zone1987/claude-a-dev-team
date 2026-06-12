---
name: sw-theme-multiple
description: >
  Mehrere Themes in Shopware 6: configInheritance (Theme-Konfig vererben), je SalesChannel ein
  anderes Theme zuweisen, Basis-Theme + Channel-Theme-Muster, theme:change pro SalesChannel.
  Trigger: "mehrere Themes", "Theme je SalesChannel", "configInheritance", "Theme vererben Konfiguration",
  "Basis-Theme", "Theme SalesChannel zuweisen", "Holiday Theme", "corporate design theme". Shopware 6.7.
---

# Shopware 6 — Mehrere Themes & SalesChannel-Zuweisung

Vollständige Referenz: [references/deep/theme-multiple.md](references/deep/theme-multiple.md)

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
