---
name: contao-dca
description: Scaffolds a Contao DCA for a tl_* table: config, list, fields with eval and sql, palettes, optional callbacks and a model.
argument-hint: <tl_tablename> [--bundle <Bundle>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-dca

Create the DCA file `contao/dca/<tl_table>.php` for the table named in $ARGUMENTS.

Call the Skill tool with "contao-data" first: it carries the field types, every `eval` option and the
callback signatures.

## Steps (one question at a time, skip what the arguments settle)

1. **The table** (`tl_<name>`) and the target bundle.
2. **The fields**: for each one the name, `inputType`, the `eval` options, the `sql` definition, and
   whether it is mandatory.
3. **Write the DCA**:
   - `config`: `dataContainer: Table`, `ctable`/`ptable` where the table is nested, `sql.keys`.
   - `list`: `sorting` mode and fields, `label`, `global_operations`, `operations`.
   - `fields`: per field `label`, `exclude`, `inputType`, `eval`, `sql`.
   - `palettes`, plus `__selector__` and `subpalettes` where a field toggles others.
4. **Optional**: `callbacks` (`onload`, `onsubmit`, `save`) and a matching model under
   `contao/../Model/<Name>Model.php`.
5. **The migration** for the database table, which `contao-data` covers.

## Output

The file written, the fields it declares, and the migration still to run.

Extend an existing DCA rather than overwriting it. Take every field type and `eval` option from
`contao-data`. Invent nothing.
