<?php declare(strict_types=1);

namespace FfContentPlus\Core\Flow;

use Shopware\Core\Content\Flow\Dispatching\Action\FlowAction;
use Shopware\Core\Content\Flow\Dispatching\StorableFlow;
use Shopware\Core\Framework\Log\Package;

/**
 * @class FfContentPlusFlowAction
 * @package FfContentPlus\Core\Flow
 */
#[Package('custom-plugins')]
class FfContentPlusFlowAction extends FlowAction
{
    /**
     * @return string
     */
    public static function getName(): string
    {
        return 'action.ff_content_plus.do_something';
    }

    /**
     * @return array<string>
     */
    public function requirements(): array
    {
        return [];
    }

    /**
     * @param StorableFlow $flow
     * @return void
     */
    public function handleFlow(StorableFlow $flow): void
    {
        // Implement flow action logic
        // Access data: $flow->getData('orderId')
        // Access store: $flow->getStore('orderNumber')
    }
}
