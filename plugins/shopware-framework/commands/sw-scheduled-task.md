---
name: sw-scheduled-task
description: Scaffold eines Shopware-6 ScheduledTask + Handler inkl. services.xml-Registrierung (Task-Tag + Message-Handler).
argument-hint: <task:name> [--plugin <PluginName>] [--interval 86400]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-scheduled-task

Erzeuge ScheduledTask + Handler. Skill: `sw-scheduled-task`.

## Ablauf
1. Task-Name (`vendor.domain.action`, z.B. `ff.cleanup`) + Ziel-Plugin + Intervall (Sekunden).
2. `src/ScheduledTask/<Name>Task.php` (extends `ScheduledTask`, `getTaskName`, `getDefaultInterval`).
3. `src/ScheduledTask/<Name>TaskHandler.php` (`#[AsMessageHandler(handles: ...)]` extends `ScheduledTaskHandler`, `run()`).
4. `services.xml`: Task mit Tag `shopware.scheduled.task`, Handler als Service (Autoconfigure oder `messenger.message_handler`).
5. Hinweis: `bin/console scheduled-task:run` + Worker/Cron.

Schwere Logik in eine eigene Message auslagern (MessageQueue). Bestehende Tasks nicht überschreiben.
