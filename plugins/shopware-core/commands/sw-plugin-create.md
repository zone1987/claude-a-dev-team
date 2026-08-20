---
name: sw-plugin-create
description: Scaffold a new Shopware 6 plugin with correct naming and namespace conventions, composer.json, the plugin class and the base structure.
argument-hint: <PluginName> [--vendor <Prefix>] [--sw 6.7|6.8|6.9|7.0]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-plugin-create

Create a new Shopware 6 plugin. Use the `sw-plugin` skill for the detailed rules.

## Steps (one question at a time, skip what is already answered)
1. **Plugin name** (PascalCase, not a theme). From `$ARGUMENTS` if given.
2. **Vendor prefix** — the short prefix that identifies the author, prepended to the plugin name so it cannot
   collide with another vendor's. Take it from `--vendor`, otherwise ask for it.
3. **Purpose** ("what should the plugin do?") → the German and English `label` for composer.json.
4. **Licence** (MIT or proprietary).
5. **Target version** → the `conflict` range (6.7 → `<6.7 || >=6.8`, 6.8 → `<6.8 || >=6.9`, …).

## The structure it creates
```
<PluginName>/
├── composer.json          # type: shopware-platform-plugin, extra.shopware-plugin-class, extra.label (de/en),
│                          # autoload psr-4 "{PluginName}\\": "src/", the conflict range
├── src/
│   ├── <PluginName>.php    # extends Shopware\Core\Framework\Plugin
│   └── Resources/config/services.xml
├── README.md
└── CHANGELOG.md
```

Namespace = `{PluginName}\{PluginName}`, PSR-4 root `src/`. Keep the plugin class minimal — logic goes through DI.
Afterwards point out `bin/console plugin:refresh && plugin:install --activate <PluginName>`, and
`/sw-entity`, `/sw-controller`, `/sw-admin-module` for the next building blocks. No invented composer fields.
