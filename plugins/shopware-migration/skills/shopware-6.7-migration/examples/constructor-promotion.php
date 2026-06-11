<?php

declare(strict_types=1);

// Constructor Property Promotion (Shopware 6.7)
// Replaces property declarations + constructor assignments with promoted parameters.
// See: references/php-migration.md

namespace FfContentPlus\Service;

use Psr\Log\LoggerInterface;
use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SystemConfig\SystemConfigService;

/**
 * @class ContentService
 * @package FfContentPlus\Service
 */
#[Package('custom-plugins')]
class ContentService
{
    /**
     * @param EntityRepository $contentRepository
     * @param SystemConfigService $configService
     * @param LoggerInterface $logger
     */
    public function __construct(
        private readonly EntityRepository $contentRepository,
        private readonly SystemConfigService $configService,
        private readonly LoggerInterface $logger,
    ) {}

    /**
     * @param string $salesChannelId
     * @return bool
     */
    public function isEnabled(string $salesChannelId): bool
    {
        return (bool) $this->configService->get(
            'FfContentPlus.config.active',
            $salesChannelId
        );
    }
}
