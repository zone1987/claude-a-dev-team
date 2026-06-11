---
name: sw-entity-catalog
description: >
  Den projektspezifischen Entity-Katalog von Shopware nutzen — welche Entities, Felder, Associations, Translations
  und CustomFields es im KONKRETEN Projekt (Core + custom/plugins) wirklich gibt. Trigger: "welche Entities gibt es",
  "Entity-Katalog", "welche Felder hat product/order/...", "Associations von Entity X", "welche custom entities",
  "Entitäten auflisten", "entity map". Shopware 6.7. Erzeuger: /sw-entity-map (Agent shopware-entity-mapper).
---

# Shopware 6 — Entity-Katalog (Projekt-Introspektion)

Anders als die Referenz-Skills („wie baut man X") beantwortet dieser Skill: **„welche Entities/Felder/Associations
existieren in DIESEM Projekt?"** — aus einem gecachten Katalog.

## Nutzung
1. Katalog liegt unter `.shopware-catalog/entities.md` im Projekt-Root.
2. **Fehlt er oder ist veraltet** → mit `/sw-entity-map` (Agent `shopware-entity-mapper`, haiku) neu erzeugen.
3. Den Katalog lesen, um Entity-Namen (`product`, `order`, `ff_example`, `custom_entity_*`), Felder, Flags,
   Associations, Translations und CustomFields nachzuschlagen — bevor man Code schreibt, der darauf zugreift.

## Wann neu erzeugen
- Nach `git pull` / Plugin-Install/-Update, nach Anlegen/Ändern einer `*Definition.php`, `EntityExtension`,
  `entities.xml`/`custom_entity.xml` oder eines CustomFieldSets.

Der Katalog ist die Quelle der Wahrheit über vorhandene Datenstrukturen; zum **Bauen** neuer Strukturen
die Referenz-Skills (`sw-entity-definition`, `sw-field-types`, `sw-associations-*`, `sw-translations`) nutzen.
