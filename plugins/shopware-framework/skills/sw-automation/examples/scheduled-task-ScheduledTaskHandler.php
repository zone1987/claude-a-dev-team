<?php declare(strict_types=1);

namespace FfContentPlus\ScheduledTask;

use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\MessageQueue\ScheduledTask\ScheduledTaskHandler;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

/**
 * @class FfContentPlusCleanupTaskHandler
 * @package FfContentPlus\ScheduledTask
 */
#[AsMessageHandler(handles: FfContentPlusCleanupTask::class)]
#[Package('custom-plugins')]
class FfContentPlusCleanupTaskHandler extends ScheduledTaskHandler
{
    /**
     * @param EntityRepository $scheduledTaskRepository
     */
    public function __construct(
        EntityRepository $scheduledTaskRepository,
    )
    {
        parent::__construct($scheduledTaskRepository);
    }

    /**
     * @return void
     */
    public function run(): void
    {
        // Perform cleanup logic
    }
}
