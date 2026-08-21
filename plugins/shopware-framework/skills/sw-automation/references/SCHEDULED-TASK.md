# Shopware 6 — Scheduled task

Two classes: a `ScheduledTask` (name + default interval) and a `ScheduledTaskHandler` (logic).

```php
class FfCleanupTask extends ScheduledTask
{
    public static function getTaskName(): string { return 'ff.cleanup'; }
    public static function getDefaultInterval(): int { return 86400; } // seconds
}

#[AsMessageHandler(handles: FfCleanupTask::class)]
final class FfCleanupTaskHandler extends ScheduledTaskHandler
{
    public function run(): void { /* clean up */ }
}
```

Registration: the task via the `shopware.scheduled.task` tag, the handler as a message handler. Runs via
`bin/console scheduled-task:run` (triggered by the system cron) or the worker. Move heavy load into the message queue
(`sw-message-queue`). The interval can be overridden in the admin (Settings → System → Tasks).

→ Details: [SCHEDULED-TASK-SCHEDULED-TASKS.md](SCHEDULED-TASK-SCHEDULED-TASKS.md) · Examples: [examples/ScheduledTask.php](examples/ScheduledTask.php), [examples/ScheduledTaskHandler.php](examples/ScheduledTaskHandler.php)
