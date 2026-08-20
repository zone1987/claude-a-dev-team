# Shopware 6 — Scheduled Task

Zwei Klassen: ein `ScheduledTask` (Name + Default-Intervall) und ein `ScheduledTaskHandler` (Logik).

```php
class FfCleanupTask extends ScheduledTask
{
    public static function getTaskName(): string { return 'ff.cleanup'; }
    public static function getDefaultInterval(): int { return 86400; } // Sekunden
}

#[AsMessageHandler(handles: FfCleanupTask::class)]
final class FfCleanupTaskHandler extends ScheduledTaskHandler
{
    public function run(): void { /* Aufräumen */ }
}
```

Registrierung: Task via `shopware.scheduled.task`-Tag, Handler als Message-Handler. Läuft über
`bin/console scheduled-task:run` (per System-Cron getriggert) bzw. den Worker. Schwere Last in MessageQueue
auslagern (`sw-message-queue`). Intervall im Admin (Einstellungen → System → Aufgaben) überschreibbar.

→ Details: [SCHEDULED-TASK-SCHEDULED-TASKS.md](SCHEDULED-TASK-SCHEDULED-TASKS.md) · Beispiele: [examples/ScheduledTask.php](examples/ScheduledTask.php), [examples/ScheduledTaskHandler.php](examples/ScheduledTaskHandler.php)
