---
name: sw-config-create
description: Scaffold/Erweiterung der Plugin-Konfiguration (config.xml) eines Shopware-6-Plugins mit Cards und Input-Feldern.
argument-hint: [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-config-create

Erzeuge oder erweitere `src/Resources/config/config.xml`. Details siehe Skill `sw-plugin-config`.

1. Ziel-Plugin bestimmen.
2. Fragen, welche Einstellungen gebraucht werden (Name, Label DE/EN, Typ, Default).
3. `<card>` mit `<title>` und `<input-field type="...">`-Einträgen erzeugen
   (Typen: `text`, `bool`, `int`, `float`, `single-select`, `multi-select`, `password`, `colorpicker`, `datetime`).
4. Hinweis auf Auslesen per `SystemConfigService` mit Key `{PluginName}.config.{feldName}` (Skill `sw-system-config`).

Bestehende `config.xml` nicht überschreiben — vorhandene Cards/Felder beibehalten und nur ergänzen.
