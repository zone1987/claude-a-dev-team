---
name: sw-config-create
description: Scaffold or extend a Shopware 6 plugin's configuration (config.xml) with cards and input fields.
argument-hint: [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-config-create

Create or extend `src/Resources/config/config.xml`. For the details, see the `sw-plugin` skill.

1. Determine the target plugin.
2. Ask which settings are needed (name, label DE/EN, type, default).
3. Create the `<card>` with a `<title>` and its `<input-field type="...">` entries
   (types: `text`, `bool`, `int`, `float`, `single-select`, `multi-select`, `password`, `colorpicker`, `datetime`).
4. Point out reading them through `SystemConfigService` with the key `{PluginName}.config.{fieldName}` (skill `sw-platform`).

Never overwrite an existing `config.xml` — keep the cards and fields that are there and only add to them.
