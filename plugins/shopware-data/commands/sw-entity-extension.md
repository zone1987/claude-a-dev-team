---
name: sw-entity-extension
description: Scaffold an EntityExtension to add fields or associations to an existing core entity (product, order, customer, ...) — including the migration and its registration.
argument-hint: <CoreEntity> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-entity-extension

Extend an existing entity without changing the core. Skill: `sw-entity` (plus `sw-fields`, `sw-write`).

## Steps
1. Determine the target core entity (e.g. `product`) and its `*Definition` class (use the entity catalogue `/sw-entity-map` if needed).
2. Ask which fields or associations to add (an association to your own entity, an extra field, …).
3. For simple extra data suggest **CustomFields** instead (`/sw-custom-field`) — an extension is for real associations and columns.
4. Create: `src/Extension/<CoreEntity>Extension.php` (`extends EntityExtension`, `getDefinitionClass`, `extendFields`),
   register it in `src/Resources/config/services/definitions.php` — PHP, not XML (`XmlFileLoader` is
   `@deprecated tag:v6.8.0`), explicitly and without autowiring — with the tag `shopware.entity.extension`,
   and add a migration for your own columns:

   ```php
   $services->set(ProductExtension::class)
       // Without autoconfigure this tag is not inferred.
       ->tag('shopware.entity.extension');
   ```

   → `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`

Mark fields `ApiAware()` when they must be reachable through the API; choose the association's delete behaviour deliberately (`CascadeDelete`/`SetNullOnDelete`).
