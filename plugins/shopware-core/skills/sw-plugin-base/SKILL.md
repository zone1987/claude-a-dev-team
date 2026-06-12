---
name: sw-plugin-base
description: >
  Eine Shopware-6-Plugin-Basis anlegen: Plugin-Bootstrap-Klasse, composer.json, PSR-4-Autoload,
  Owner-/Namens-Konventionen (A-Dev-Team Ff, A-Dev-Team Adt, Andreas Gerhardt Ag, Pfötchenbuddies Pb).
  Trigger: "neues Plugin", "Plugin erstellen/anlegen/scaffolden", "Plugin-Basisklasse", "composer.json plugin",
  "create shopware plugin", "FfXxx/AdtXxx/AgXxx/PbXxx". Shopware 6.7. Scaffolder: /sw-plugin-create.
---

# Shopware 6 — Plugin-Basis

Ein Plugin ist ein Symfony-Bundle, das `Shopware\Core\Framework\Plugin` erweitert.

## Namens-/Namespace-Konvention
Plugin-Name PascalCase mit Owner-Präfix; Namespace = `{PluginName}\{PluginName}`, PSR-4-Root `src/`.

| Owner | Präfix | Composer-Vendor | Beispiel |
|---|---|---|---|
| A-Dev-Team | `Ff` | `ff/` | `FfContentPlus` → `ff/content-plus` |
| A-Dev-Team | `Adt` | `adt/` | `AdtProductExport` → `adt/product-export` |
| Andreas Gerhardt | `Ag` | `ag/` | `AgNewsletterTools` → `ag/newsletter-tools` |
| Pfötchenbuddies | `Pb` | `pb/` | `PbHidePrices` → `pb/hide-prices` |

`composer.json` benötigt `"type": "shopware-platform-plugin"`, `extra.shopware-plugin-class`,
`extra.label` (DE/EN), `autoload.psr-4: { "{PluginName}\\": "src/" }` und einen `conflict`-Range je Ziel-Version
(6.7 → `<6.7 || >=6.8`).

## Plugin-Klasse
`src/{PluginName}.php` erweitert `Plugin`; Logik in `build()`/`boot()` nur wenn nötig — Services über DI (`sw-dependency-injection`).

→ Vollständiges Gerüst: [examples/PluginClass.php](examples/PluginClass.php)
→ Lifecycle (install/activate/…): `sw-plugin-lifecycle` · Config: `sw-plugin-config` · Logging: `sw-logging`
