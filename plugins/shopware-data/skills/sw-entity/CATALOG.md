# Shopware 6 — Entity catalog (project introspection)

Unlike the reference skills ("how do I build X"), this skill answers: **"which entities/fields/associations
exist in THIS project?"** — from a cached catalog.

## Usage
1. The catalog lives at `.shopware-catalog/entities.md` in the project root.
2. **If it is missing or stale** → regenerate it with `/sw-entity-map` (agent `shopware-entity-mapper`, haiku).
3. Read the catalog to look up entity names (`product`, `order`, `ff_example`, `custom_entity_*`), fields, flags,
   associations, translations and custom fields — before writing code that accesses them.

## When to regenerate
- After `git pull` / plugin install or update, after creating or changing a `*Definition.php`, an `EntityExtension`,
  an `entities.xml`/`custom_entity.xml`, or a custom field set.

The catalog is the source of truth for the data structures that exist; to **build** new structures,
use the reference skills (`sw-entity-definition`, `sw-field-types`, `sw-associations-*`, `sw-translations`).
