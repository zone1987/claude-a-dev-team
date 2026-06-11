---
name: sw-entity-map
description: Scannt das aktuelle Shopware-Projekt (Core + custom/plugins) und erzeugt/aktualisiert den Entity-Katalog .shopware-catalog/entities.md (Entities, Felder, Flags, Associations, Translations, CustomFields, CustomEntities).
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-entity-map

Erzeuge/aktualisiere den Entity-Katalog des Projekts. Delegiere an den Agent `shopware-entity-mapper`
(Skill `sw-entity-catalog`).

## Ablauf
1. Projekt-Root + Scan-Bereich bestimmen: `vendor/shopware/**` (Core) + `custom/plugins/*`, `custom/static-plugins/*`.
   Bei `--custom-only` nur Custom-Code scannen.
2. Scanne `*Definition.php` (defineFields), `EntityExtension`, Attribut-Entities (`#[Entity]`),
   `entities.xml`/`custom_entity.xml`, CustomFieldSets, Translation-Definitions.
3. Schreibe `.shopware-catalog/entities.md` im Format aus `sw-entity-catalog`/`shopware-entity-mapper`
   (pro Entity: Felder-Tabelle, Associations, Translations, CustomFields, Extensions).
4. Kopfzeile mit Scan-Datum, Scan-Bereich und Entity-Anzahl. Abschließend Kurzzusammenfassung ausgeben.

Effizient scannen (gezieltes glob/grep, nicht ganze Dateien lesen). Nur real vorhandene Strukturen — nichts erfinden.
