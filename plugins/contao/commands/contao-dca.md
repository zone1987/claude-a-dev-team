---
name: contao-dca
description: Scaffold einer Contao-DCA-Konfiguration (Data Container Array) für eine Tabelle tl_* — config, list (sorting/label/operations), fields (mit eval + sql), palettes, optional callbacks + Model.
argument-hint: <tl_tablename> [--bundle <Bundle>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-dca

Erzeuge eine DCA-Datei `contao/dca/<tl_table>.php`. Skills: `contao-dca-reference`, `contao-dca-framework`, `contao-models`.

## Ablauf
1. Tabellenname (`tl_<name>`) + Ziel-Bundle bestimmen.
2. Felder erfragen (Name, inputType, eval-Optionen, sql-Definition, Pflicht). 
3. DCA erzeugen: `config` (dataContainer Table, ctable/ptable falls nötig, sql.keys), `list` (sorting mode/fields,
   label, global_operations, operations), `fields` (je Feld label/exclude/inputType/eval/sql), `palettes` (+ `__selector__`/subpalettes).
4. Optional: `callbacks` (z.B. onload/onsubmit/save) und ein zugehöriges **Model** (`contao/../Model/<Name>Model.php` bzw. via Annotation).
5. Hinweis: `contao/dca/<tl_table>.php` korrekt platzieren; Migration für die DB-Tabelle (`contao-migrations`).

Feld-Typen/eval-Optionen aus `contao-dca-reference`. Bestehende DCA nicht überschreiben — ergänzen.
