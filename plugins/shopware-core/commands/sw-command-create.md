---
name: sw-command-create
description: Scaffold a CLI command (bin/console) in a Shopware 6 plugin, including its services.xml registration.
argument-hint: <command:name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-command-create

Create a Symfony command in the target plugin. For the details, see the `sw-services` skill.

1. Command name `vendor:domain:action` (e.g. `ff:content:import`) from `$ARGUMENTS`.
2. Determine the target plugin (from `--plugin` or the detected `custom/plugins/*`).
3. File `src/Command/<ClassName>.php` with `#[AsCommand(name, description)]`, an `execute()` using `SymfonyStyle`,
   returning `Command::SUCCESS`.
4. If attribute autoconfiguration is off, register it in `services.xml` with the `console.command` tag.
5. Add the repositories and services it needs as constructor arguments.

The class name is the action part in PascalCase plus `Command`. Keep out of the command any business logic that belongs in a service.
