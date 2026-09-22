# Scheduled Tasks

## Contents

- [Overview](#overview)
- [ScheduledTask Class](#scheduledtask-class)
- [ScheduledTaskHandler Class](#scheduledtaskhandler-class)
- [Service Registration](#service-registration)
- [Common Intervals](#common-intervals)
- [Task Management](#task-management)
- [Best Practices](#best-practices)

## Overview

Scheduled tasks are recurring background jobs managed by Shopware's task scheduler. Each task consists of two classes: the `ScheduledTask` (definition) and the `ScheduledTaskHandler` (execution logic).

## ScheduledTask Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\ScheduledTask;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\MessageQueue\ScheduledTask\ScheduledTask;

/**
 * @class CleanupTask
 * @package FfContentPlus\ScheduledTask
 */
#[Package('custom-plugins')]
class CleanupTask extends ScheduledTask
{
    /**
     * @return string
     */
    public static function getTaskName(): string
    {
        return 'ff_content_plus.cleanup';
    }

    /**
     * @return int
     */
    public static function getDefaultInterval(): int
    {
        return 86400; // 24 hours in seconds
    }
}
```

## ScheduledTaskHandler Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\ScheduledTask;

use Psr\Log\LoggerInterface;
use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\MessageQueue\ScheduledTask\ScheduledTaskHandler;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

/**
 * @class CleanupTaskHandler
 * @package FfContentPlus\ScheduledTask
 */
#[AsMessageHandler(handles: CleanupTask::class)]
#[Package('custom-plugins')]
class CleanupTaskHandler extends ScheduledTaskHandler
{
    /**
     * @param EntityRepository $scheduledTaskRepository
     * @param LoggerInterface $logger
     * @param MyCleanupService $cleanupService
     */
    public function __construct(
        EntityRepository $scheduledTaskRepository,
        LoggerInterface $logger,
        private readonly MyCleanupService $cleanupService,
    ) {
        parent::__construct($scheduledTaskRepository, $logger);
    }

    /**
     * @return void
     */
    public function run(): void
    {
        $this->cleanupService->cleanup();
    }
}
```

## Service Registration

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Resources\config\services;

use FfContentPlus\ScheduledTask\CleanupTask;
use FfContentPlus\ScheduledTask\CleanupTaskHandler;
use FfContentPlus\Service\MyCleanupService;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

return static function (ContainerConfigurator $containerConfigurator): void {
    $services = $containerConfigurator->services();

    $services->set(CleanupTask::class)
        // Without autoconfigure this tag is not inferred.
        ->tag('shopware.scheduled.task');

    $services->set(CleanupTaskHandler::class)
        ->args([
            service('scheduled_task.repository'),
            service('logger'),
            service(MyCleanupService::class),
        ])
        // Without autoconfigure this tag is not inferred from #[AsMessageHandler].
        ->tag('messenger.message_handler');
};
```

Both tags are silent when missing: an untagged task is never registered by
`scheduled-task:register`, and an untagged handler is never called when the task is due.

## Common Intervals

| Interval | Seconds | Constant |
|----------|---------|----------|
| 5 minutes | `300` | — |
| 15 minutes | `900` | — |
| 1 hour | `3600` | — |
| 6 hours | `21600` | — |
| 12 hours | `43200` | — |
| 24 hours | `86400` | — |
| 1 week | `604800` | — |

## Task Management

```bash
# List all scheduled tasks
ddev exec bin/console scheduled-task:list

# Run due tasks manually
ddev exec bin/console scheduled-task:run

# Run a specific task
ddev exec bin/console scheduled-task:run-single ff_content_plus.cleanup

# Register new tasks (after plugin install/update)
ddev exec bin/console scheduled-task:register
```

## Best Practices

1. **Task name** follows pattern: `{entity_prefix}_{plugin_snake}.{task_name}` (e.g., `ff_content_plus.cleanup`)
2. **Keep handlers lightweight** — dispatch messages to the message queue for heavy work
3. **Use the `#[AsMessageHandler]` attribute** on the handler to link it to the task class
4. **Log failures** — the handler has access to a logger via the parent constructor
5. **Default interval** should be reasonable — don't poll more frequently than needed
