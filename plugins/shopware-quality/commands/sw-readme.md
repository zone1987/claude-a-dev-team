---
name: sw-readme
description: Generiert/aktualisiert eine README für ein Shopware-6-Plugin nach dem etablierten README-Schema (Installation, Konfiguration, Features, Kompatibilität).
argument-hint: [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-readme

Erzeuge/aktualisiere die Plugin-README. Skill: `shopware-readme` (Schema/Struktur).

## Ablauf
1. Ziel-Plugin bestimmen; `composer.json` (Name, Label, Version, Ziel-SW-Version) + vorhandene Features aus dem Code lesen.
2. README nach Schema erstellen: Titel/Beschreibung, Installation (`plugin:install --activate`), Konfiguration,
   Features, Kompatibilität (SW-Version), ggf. Lizenz/Support.
3. Bestehende README respektieren — nur aktualisieren/ergänzen, nicht blind überschreiben.

Changelog separat: `/sw-changelog`.
