---
name: sw-entity
description: Scaffold einer kompletten Shopware-6 DAL-Entity — Definition + Entity-Klasse + Collection + Migration + services.xml-Registrierung (optional Translations).
argument-hint: <EntityName> [--plugin <PluginName>] [--translatable] [--attribute]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-entity

Erzeuge eine vollständige DAL-Entity im Ziel-Plugin. Skills: `sw-entity-definition`, `sw-entity-class`,
`sw-entity-collection`, `sw-field-types`, `sw-field-flags`, `sw-database-migration` (bei `--translatable` zusätzlich `sw-translations`).

## Ablauf
1. EntityName (PascalCase) + Ziel-Plugin bestimmen; Entity-/Tabellenname = snake_case mit Owner-Präfix (z.B. `ff_example`).
2. Felder erfragen (Name, Typ, Flags, nullable). `id` (IdField/PrimaryKey/Required) immer.
3. `--attribute` → attributbasierte Variante (`sw-attribute-entities`); sonst klassisch (Definition+Entity+Collection).
4. Dateien erzeugen:
   - `src/Core/Content/<Entity>/<Entity>Definition.php`, `<Entity>Entity.php`, `<Entity>Collection.php`
   - bei `--translatable`: `<Entity>TranslationDefinition.php` + `TranslatedField`/`TranslationsAssociationField`
   - `src/Migration/Migration{ts}<Entity>.php` (BINARY(16) id, DATETIME(3) created_at/updated_at)
   - `services.xml`: Definition(en) mit Tag `shopware.entity.definition`
5. Hinweis: `bin/console database:migrate --all <PluginName>` und Entity-Katalog via `/sw-entity-map` aktualisieren.

PSR-4-Namespace des Plugins beibehalten, bestehende `services.xml`/Migrationen nicht überschreiben. Keine erfundenen Field-Typen.
