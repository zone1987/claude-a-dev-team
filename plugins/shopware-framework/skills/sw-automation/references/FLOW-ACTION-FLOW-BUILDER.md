# Flow Builder Actions

## Contents

- [Overview](#overview)
- [FlowAction Class](#flowaction-class)
- [Service Registration](#service-registration)
- [Flow Data Access](#flow-data-access)
- [Awareness Requirements](#awareness-requirements)
- [Naming Convention](#naming-convention)

## Overview

Flow actions are custom actions triggered by the Flow Builder in the Administration. They extend `FlowAction` and implement `handleFlow()`.

## FlowAction Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Flow;

use Shopware\Core\Content\Flow\Dispatching\Action\FlowAction;
use Shopware\Core\Content\Flow\Dispatching\StorableFlow;
use Shopware\Core\Framework\Log\Package;

/**
 * @class SendNotificationAction
 * @package FfContentPlus\Core\Flow
 */
#[Package('custom-plugins')]
class SendNotificationAction extends FlowAction
{
    /**
     * @return string
     */
    public static function getName(): string
    {
        return 'action.ff_content_plus.send_notification';
    }

    /**
     * @return array<string>
     */
    public function requirements(): array
    {
        // Return awareness interfaces required for this action
        return ['orderAware'];
    }

    /**
     * @param StorableFlow $flow
     * @return void
     */
    public function handleFlow(StorableFlow $flow): void
    {
        // Access flow data
        $orderId = $flow->getStore('orderId');
        $config = $flow->getConfig();

        // Action-specific config from Flow Builder UI
        $recipient = $config['recipient'] ?? '';
        $message = $config['message'] ?? '';

        // Execute action logic
        $this->notificationService->send($recipient, $message, $orderId);
    }
}
```

## Service Registration

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Resources\config\services;

use FfContentPlus\Core\Flow\SendNotificationAction;
use FfContentPlus\Service\NotificationService;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

return static function (ContainerConfigurator $containerConfigurator): void {
    $services = $containerConfigurator->services();

    $services->set(SendNotificationAction::class)
        ->args([service(NotificationService::class)])
        // Without autoconfigure this tag is not inferred.
        ->tag('flow.action');
};
```

Without the tag the action never appears in the Flow Builder, and nothing reports it.

## Flow Data Access

```php
public function handleFlow(StorableFlow $flow): void
{
    // Get stored data
    $orderId = $flow->getStore('orderId');
    $customerId = $flow->getStore('customerId');

    // Get full entity (lazy loaded)
    $order = $flow->getData('order');

    // Get action config (from Flow Builder UI)
    $config = $flow->getConfig();

    // Stop further actions in the flow
    $flow->stop();
}
```

## Awareness Requirements

| Requirement | Provides | Store Key |
|------------|----------|-----------|
| `orderAware` | Order data | `orderId` |
| `customerAware` | Customer data | `customerId` |
| `mailAware` | Mail recipients | `mailStruct` |
| `customerGroupAware` | Customer group | `customerGroupId` |

## Naming Convention

Action names: `action.{vendor_prefix}_{plugin_snake}.{action_description}`

Examples:
- `action.ff_content_plus.send_notification`
- `action.ff_content_plus.sync_external`
