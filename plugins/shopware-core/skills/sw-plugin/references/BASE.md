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

`composer.json` requires `"type": "shopware-platform-plugin"`, `"license": "proprietary"`,
`extra.shopware-plugin-class`, `extra.label` (DE/EN), `autoload.psr-4: { "{PluginName}\\": "src/" }`,
`autoload-dev.psr-4: { "{PluginName}\\Tests\\": "tests/" }` as soon as there are tests, and a `conflict`
range per target version (6.7 → `<6.7 || >=6.8`), covering `shopware/core`, `shopware/storefront` and
`shopware/administration`.

→ Head, `require-dev`, `config.allow-plugins` and all 22 scripts: [PLUGIN-COMPOSER.md](PLUGIN-COMPOSER.md)

Plugins we develop ourselves live under `custom/static-plugins/{PluginName}/`; `custom/plugins/` holds
installed third-party extensions and is not touched.

→ Full directory tree and `.gitignore`: [PLUGIN-STRUCTURE.md](PLUGIN-STRUCTURE.md)

## Plugin class
`src/{PluginName}.php` extends `Plugin`; put logic in `build()`/`boot()` only when necessary — wire services through DI (`sw-dependency-injection`).

→ Full skeleton: [examples/PluginClass.php](examples/PluginClass.php)
→ Lifecycle (install/activate/…): `sw-plugin-lifecycle` · Config: `sw-plugin-config` · Logging: `sw-logging`

Every class carries the plugin's own `#[Package]` attribute, first in the attribute list —
not Shopware's `@internal` one: [PLUGIN-PACKAGE-ATTRIBUTE.md](PLUGIN-PACKAGE-ATTRIBUTE.md)

Setting a new plugin up: [PLUGIN-CHECKLIST.md](PLUGIN-CHECKLIST.md)
