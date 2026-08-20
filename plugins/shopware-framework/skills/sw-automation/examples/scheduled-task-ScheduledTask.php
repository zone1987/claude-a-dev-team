<?php declare(strict_types=1);

namespace FfContentPlus\ScheduledTask;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\MessageQueue\ScheduledTask\ScheduledTask;

/**
 * @class FfContentPlusCleanupTask
 * @package FfContentPlus\ScheduledTask
 */
#[Package('custom-plugins')]
class FfContentPlusCleanupTask extends ScheduledTask
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
        return 86400; // 24 hours
    }
}
