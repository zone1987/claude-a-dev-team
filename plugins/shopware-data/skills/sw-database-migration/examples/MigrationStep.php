<?php declare(strict_types=1);

namespace FfContentPlus\Migration;

use Doctrine\DBAL\Connection;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Migration\MigrationStep;

/**
 * @class Migration1700000000CreateItemTable
 * @package FfContentPlus\Migration
 */
#[Package('custom-plugins')]
class Migration1700000000CreateItemTable extends MigrationStep
{
    /**
     * @return int
     */
    public function getCreationTimestamp(): int
    {
        return 1700000000;
    }

    /**
     * @param Connection $connection
     * @return void
     */
    public function update(Connection $connection): void
    {
        $connection->executeStatement('
            CREATE TABLE IF NOT EXISTS `ff_content_plus_item` (
                `id`         BINARY(16)   NOT NULL,
                `active`     TINYINT(1)   NOT NULL DEFAULT 0,
                `name`       VARCHAR(255) NOT NULL,
                `created_at` DATETIME(3)  NOT NULL,
                `updated_at` DATETIME(3)  NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        ');
    }

    /**
     * @param Connection $connection
     * @return void
     */
    public function updateDestructive(Connection $connection): void
    {
    }
}
