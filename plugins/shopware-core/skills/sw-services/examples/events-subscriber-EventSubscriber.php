<?php declare(strict_types=1);

namespace FfContentPlus\Subscriber;

use Shopware\Core\Framework\Log\Package;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

/**
 * @class ExampleSubscriber
 * @package FfContentPlus\Subscriber
 */
#[Package('custom-plugins')]
class ExampleSubscriber implements EventSubscriberInterface
{
    /**
     * @return array<string, string|array{0: string, 1: int}|list<array{0: string, 1?: int}>>
     */
    public static function getSubscribedEvents(): array
    {
        return [
            // ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
        ];
    }
}
