---
name: sw-entity-extension
description: Scaffold einer EntityExtension, um einer bestehenden Core-Entity (product, order, customer, ...) Felder/Associations hinzuzufügen — inkl. Migration und Registrierung.
argument-hint: <CoreEntity> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-entity-extension

Erweitere eine bestehende Entity ohne Core-Änderung. Skill: `sw-entity-extension` (+ `sw-field-types`, `sw-associations-*`, `sw-database-migration`).

## Ablauf
1. Ziel-Core-Entity (z.B. `product`) + zugehörige `*Definition`-Klasse bestimmen (ggf. Entity-Katalog `/sw-entity-map`).
2. Hinzuzufügende Felder/Associations erfragen (Association zu eigener Entity, Zusatzfeld, …).
3. Bei einfachen Zusatzdaten **CustomFields** vorschlagen (`/sw-custom-field`) — Extension für echte Associations/Spalten.
4. Erzeugen: `src/Extension/<CoreEntity>Extension.php` (`extends EntityExtension`, `getDefinitionClass`, `extendFields`),
   Registrierung in `services.xml` mit Tag `shopware.entity.extension`, bei eigenen Spalten eine Migration.

Felder mit `ApiAware()` versehen, wenn über API nötig; Lösch-Verhalten der Association bewusst (`CascadeDelete`/`SetNullOnDelete`).
