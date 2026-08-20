---
name: sw-custom-field
description: Scaffold a CustomFieldSet including its CustomFields for a Shopware 6 entity (migration or lifecycle), with types and an entity relation.
argument-hint: <entityName> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-custom-field

Create a CustomFieldSet with fields. Skill: `sw-fields`.

## Steps
1. Determine the target entity (e.g. `product`, `order`, `customer`) and the target plugin.
2. Ask for the fields (name with an owner prefix e.g. `ff_*`, type, label DE/EN). Types: `text`, `bool`, `int`, `float`,
   `datetime`, `select`, `entity` (entity selection), `media`.
3. Create: a CustomFieldSet upsert in a migration (or the plugin's `install()`), with `relations: [{entityName: ...}]`
   and `customFields: [...]`.
4. Point out how to read it via `$entity->getCustomFields()['ff_...']` and how to access it in the storefront.

Give the set name an owner prefix (`ff_...`). Never overwrite existing sets or fields — only add to them.
