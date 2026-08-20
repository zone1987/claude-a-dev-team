# Shopware 6 — Plugin Base

A plugin is a Symfony bundle extending `Shopware\Core\Framework\Plugin`.

## Naming/namespace convention
Plugin name in PascalCase with an owner prefix; namespace = `{PluginName}\{PluginName}`, PSR-4 root `src/`.

| Owner | Prefix | Composer vendor | Example |
|---|---|---|---|
| A-Dev-Team | `Ff` | `ff/` | `FfContentPlus` → `ff/content-plus` |
| A-Dev-Team | `Adt` | `adt/` | `AdtProductExport` → `adt/product-export` |
| Andreas Gerhardt | `Ag` | `ag/` | `AgNewsletterTools` → `ag/newsletter-tools` |
| Pfötchenbuddies | `Pb` | `pb/` | `PbHidePrices` → `pb/hide-prices` |

`composer.json` requires `"type": "shopware-platform-plugin"`, `extra.shopware-plugin-class`,
`extra.label` (DE/EN), `autoload.psr-4: { "{PluginName}\\": "src/" }` and a `conflict` range per target version
(6.7 → `<6.7 || >=6.8`).

## Plugin class
`src/{PluginName}.php` extends `Plugin`; put logic in `build()`/`boot()` only when necessary — wire services through DI (`sw-dependency-injection`).

→ Full skeleton: [examples/PluginClass.php](examples/PluginClass.php)
→ Lifecycle (install/activate/…): `sw-plugin-lifecycle` · Config: `sw-plugin-config` · Logging: `sw-logging`
