# Shopware 6 — Multiple themes & sales channel assignment

Full reference: [MULTIPLE-DETAIL.md](MULTIPLE-DETAIL.md)

**Pattern:** one base theme (corporate design), derived themes for sales channels/campaigns.

```json
// derived theme: theme.json
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
bin/console theme:change   # select interactively per sales channel
```

`configInheritance` inherits fields and snippets; values from the parent are adopted unless
explicitly overridden. The relationship is set during `plugin:install`, updated via `theme:refresh`.
