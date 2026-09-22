---
name: sw-scheduled-task
description: Scaffolds a Shopware 6 ScheduledTask plus its handler, including the PHP service registration (task tag and message handler).
argument-hint: <Name> [--plugin <PluginName>] [--interval 86400]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
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
4. `src/Resources/config/services/scheduled-tasks.php` — PHP, not XML (`XmlFileLoader` is
   `@deprecated tag:v6.8.0`), explicitly and without autowiring. Without `autoconfigure` neither tag is
   inferred, so set both yourself:

   ```php
   $services->set(MyCleanupTask::class)
       // Without autoconfigure this tag is not inferred.
       ->tag('shopware.scheduled.task');

   $services->set(MyCleanupTaskHandler::class)
       ->args([
           service('scheduled_task.repository'),
           service('logger'),
       ])
       // Without autoconfigure this tag is not inferred from #[AsMessageHandler].
       ->tag('messenger.message_handler');
   ```

   → `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`
5. Note the follow-up: `ddev exec bin/console scheduled-task:run`, and the worker or cron that drives it.

Move heavy work into a message of its own (the message queue). Never overwrite an existing task.

## Before it counts as done

`composer gate` green, unit tests for the handler's logic, and the task proved end-to-end:
registered, due, run, and its effect visible.
→ `shopware-testing` → `sw-testing-standard`
