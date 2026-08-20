# Shopware 6 — Plugin Base

A plugin is a Symfony bundle extending `Shopware\Core\Framework\Plugin`.

## Naming/namespace convention
Plugin name in PascalCase with an owner prefix; namespace = `{PluginName}\{PluginName}`, PSR-4 root `src/`.

The prefix is the vendor's own short tag, chosen once and used for every plugin they publish, so
two vendors' plugins can never collide. Prefix, composer vendor and namespace all derive from it:

| Prefix | Composer vendor | Plugin name | Namespace |
|---|---|---|---|
| `Ff` | `ff/` | `FfContentPlus` | `FfContentPlus\FfContentPlus` |
| `Acme` | `acme/` | `AcmeProductExport` | `AcmeProductExport\AcmeProductExport` |

`composer.json` requires `"type": "shopware-platform-plugin"`, `extra.shopware-plugin-class`,
`extra.label` (DE/EN), `autoload.psr-4: { "{PluginName}\\": "src/" }` and a `conflict` range per target version
(6.7 → `<6.7 || >=6.8`).

## Plugin class
`src/{PluginName}.php` extends `Plugin`; put logic in `build()`/`boot()` only when necessary — wire services through DI (`sw-dependency-injection`).

→ Full skeleton: [examples/PluginClass.php](examples/PluginClass.php)
→ Lifecycle (install/activate/…): `sw-plugin-lifecycle` · Config: `sw-plugin-config` · Logging: `sw-logging`
