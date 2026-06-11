---
name: sw-custom-field
description: Scaffold eines CustomFieldSet inkl. CustomFields für eine Shopware-6-Entity (Migration oder Lifecycle), mit Typen und Entity-Relation.
argument-hint: <entityName> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-custom-field

Lege ein CustomFieldSet mit Feldern an. Skill: `sw-custom-fields`.

## Ablauf
1. Ziel-Entity (z.B. `product`, `order`, `customer`) + Ziel-Plugin bestimmen.
2. Felder erfragen (Name mit Owner-Präfix z.B. `ff_*`, Typ, Label DE/EN). Typen: `text`, `bool`, `int`, `float`,
   `datetime`, `select`, `entity` (Entity-Selection), `media`.
3. Erzeugen: CustomFieldSet-Upsert in einer Migration (oder Plugin-`install()`), mit `relations: [{entityName: ...}]`
   und `customFields: [...]`.
4. Hinweis auf Auslesen via `$entity->getCustomFields()['ff_...']` und Storefront-Zugriff.

Set-Name mit Owner-Präfix (`ff_...`). Bestehende Sets/Felder nicht überschreiben — nur ergänzen.
