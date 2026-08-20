---
name: sw-entity
description: Scaffold a complete Shopware 6 DAL entity — definition + entity class + collection + migration + services.xml registration (translations optional).
argument-hint: <EntityName> [--plugin <PluginName>] [--translatable] [--attribute]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-entity

Create a complete DAL entity in the target plugin. Skills: `sw-entity`, `sw-fields`,
`sw-write` (with `--translatable` also the translation section of `sw-fields`).

## Steps
1. Determine the entity name (PascalCase) and the target plugin; entity and table name = snake_case with an owner prefix (e.g. `ff_example`).
2. Ask for the fields (name, type, flags, nullable). `id` (IdField/PrimaryKey/Required) is always present.
3. `--attribute` → the attribute-based variant; otherwise the classic one (definition + entity + collection).
4. Create the files:
   - `src/Core/Content/<Entity>/<Entity>Definition.php`, `<Entity>Entity.php`, `<Entity>Collection.php`
   - with `--translatable`: `<Entity>TranslationDefinition.php` + `TranslatedField`/`TranslationsAssociationField`
   - `src/Migration/Migration{ts}<Entity>.php` (BINARY(16) id, DATETIME(3) created_at/updated_at)
   - `services.xml`: the definition(s) with the tag `shopware.entity.definition`
5. Point out `bin/console database:migrate --all <PluginName>` and updating the entity catalogue via `/sw-entity-map`.

Keep the plugin's PSR-4 namespace, never overwrite an existing `services.xml` or migration. No invented field types.
