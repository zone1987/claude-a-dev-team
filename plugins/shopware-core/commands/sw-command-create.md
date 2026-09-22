---
name: sw-command-create
description: Scaffold a CLI command (bin/console) in a Shopware 6 plugin, including its PHP service registration and console.command tag.
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
4. Register it in `src/Resources/config/services/commands.php` — PHP, not XML (`XmlFileLoader` is
   `@deprecated tag:v6.8.0`), explicitly and without autowiring. Without `autoconfigure` the
   `console.command` tag is not inferred from `#[AsCommand]`, so set it yourself:

   ```php
   $services->set(MyImportCommand::class)
       ->args([service('product.repository')])
       // Without autoconfigure this tag is not inferred.
       ->tag('console.command');
   ```

   → `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`
5. Add the repositories and services it needs as constructor arguments.

The class name is the action part in PascalCase plus `Command`. Keep out of the command any business logic that belongs in a service.
