---
name: sw-scheduled-task
description: Scaffolds a Shopware 6 ScheduledTask plus its handler, including the services.xml registration (task tag and message handler).
argument-hint: <Name> [--plugin <PluginName>] [--interval 86400]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-scheduled-task

Produce a scheduled task and its handler. Skill: `sw-messaging`.

## Steps
1. Settle the task name (`vendor.domain.action`, e.g. `ff.cleanup`), the target plugin and the
   interval in seconds.
2. `src/ScheduledTask/<Name>Task.php` (extends `ScheduledTask`, with `getTaskName` and
   `getDefaultInterval`).
3. `src/ScheduledTask/<Name>TaskHandler.php` (`#[AsMessageHandler(handles: …)]`, extends
   `ScheduledTaskHandler`, with `run()`).
4. `services.xml`: the task tagged `shopware.scheduled.task`, the handler as a service (through
   autoconfigure or `messenger.message_handler`).
5. Note the follow-up: `bin/console scheduled-task:run`, and the worker or cron that drives it.

Move heavy work into a message of its own (the message queue). Never overwrite an existing task.
