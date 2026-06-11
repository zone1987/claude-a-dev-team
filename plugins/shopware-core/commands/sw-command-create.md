---
name: sw-command-create
description: Scaffold eines CLI-Commands (bin/console) in einem Shopware-6-Plugin inkl. services.xml-Registrierung.
argument-hint: <command:name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-command-create

Erzeuge einen Symfony-Command im Ziel-Plugin. Details siehe Skill `sw-cli-command`.

1. Command-Name `vendor:domain:action` (z.B. `ff:content:import`) aus `$ARGUMENTS`.
2. Ziel-Plugin bestimmen (aus `--plugin` oder erkanntem `custom/plugins/*`).
3. Datei `src/Command/<ClassName>.php` mit `#[AsCommand(name, description)]`, `execute()` mit `SymfonyStyle`,
   Rückgabe `Command::SUCCESS`.
4. Falls keine Attribut-Autoconfiguration: in `services.xml` mit Tag `console.command` registrieren.
5. Benötigte Repositories/Services als Constructor-Argumente ergänzen.

Klassenname = PascalCase aus dem Action-Teil + `Command`. Keine Geschäftslogik im Command bündeln, die in einen Service gehört.
