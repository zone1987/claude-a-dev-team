---
name: sw-entity-map
description: Scans the current Shopware project (core + custom/plugins) and writes or updates the entity catalogue .shopware-catalog/entities.md (entities, fields, flags, associations, translations, CustomFields, custom entities).
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-entity-map

Create or update the project's entity catalogue. Delegate to the `shopware-entity-mapper` agent
(skill `sw-entity`).

## Steps
1. Determine the project root and the scan area: `vendor/shopware/**` (core) plus `custom/plugins/*`, `custom/static-plugins/*`.
   With `--custom-only`, scan custom code only.
2. Scan `*Definition.php` (defineFields), `EntityExtension`, attribute entities (`#[Entity]`),
   `entities.xml`/`custom_entity.xml`, CustomFieldSets, translation definitions.
3. Write `.shopware-catalog/entities.md` in the format described by `sw-entity` and `shopware-entity-mapper`
   (per entity: field table, associations, translations, CustomFields, extensions).
4. Add a header with the scan date, the scan area and the entity count. Print a short summary at the end.

Scan efficiently (targeted glob/grep, do not read whole files). Only structures that really exist — invent nothing.
