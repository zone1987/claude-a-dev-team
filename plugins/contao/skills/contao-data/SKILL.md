---
name: contao-data
description: Contao 5 data layer: DCA definition and reference, Models, Collections, migrations, search indexing. Use when the request names a Contao DCA, tl_ table, Contao Model or migration.
---

# Contao data layer

The DCA array describes a table to Contao; a Model gives you typed access to it. Both are needed for any custom data.

## Reference map

- **[DCA-FRAMEWORK.md](DCA-FRAMEWORK.md)**: creating a DCA, registering callbacks, `PaletteManipulator`, and custom drivers.
- **[DCA-REFERENCE-DCA-CONFIG-LIST-FIELDS.md](DCA-REFERENCE-DCA-CONFIG-LIST-FIELDS.md)**: every key of `config`, `list` and `fields`, with types and defaults.
- **[DCA-REFERENCE-DCA-PALETTES-CALLBACKS.md](DCA-REFERENCE-DCA-PALETTES-CALLBACKS.md)**: every `palettes` and `subpalettes` form, and each callback with its signature.
- **[MODELS.md](MODELS.md)**: the model API: retrieving and modifying records, the options parameter, eager loading and relations.
- **[ADT-CONTAO-DAL.md](ADT-CONTAO-DAL.md)**: the same ground from the data-access side, kept as the older entry point.
- **[MIGRATIONS.md](MIGRATIONS.md)**: `MigrationInterface` and its three mandatory methods, `AbstractMigration`, and service registration.
- **[SEARCH-INDEXING.md](SEARCH-INDEXING.md)**: triggering indexing, writing a custom indexer, and excluding pages from the index.

## Source

Distilled from [docs.contao.org/5.x](https://docs.contao.org/5.x) : the developer documentation and the German end-user manual : plus the [contao/contao](https://github.com/contao/contao) source, retrieved 2026-08-20.
