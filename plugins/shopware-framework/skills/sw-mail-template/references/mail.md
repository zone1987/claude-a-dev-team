# Mail Templates

## Overview

Plugins can create custom mail templates and add data to existing mail events.

## Creating Mail Templates (Migration)

```php
use Shopware\Core\Content\MailTemplate\MailTemplateTypes;
use Shopware\Core\Framework\Uuid\Uuid;

public function update(Connection $connection): void
{
    $mailTemplateTypeId = Uuid::randomHex();

    // Create mail template type
    $connection->insert('mail_template_type', [
        'id' => Uuid::fromHexToBytes($mailTemplateTypeId),
        'technical_name' => 'ff_content_plus_notification',
        'available_entities' => json_encode([
            'order' => 'order',
            'salesChannel' => 'sales_channel',
        ]),
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);

    // Create type translation
    $connection->insert('mail_template_type_translation', [
        'mail_template_type_id' => Uuid::fromHexToBytes($mailTemplateTypeId),
        'language_id' => Uuid::fromHexToBytes('2fbb5fe2e29a4d70aa5854ce7ce3e20b'),
        'name' => 'Content Plus Notification',
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);

    $mailTemplateId = Uuid::randomHex();

    // Create mail template
    $connection->insert('mail_template', [
        'id' => Uuid::fromHexToBytes($mailTemplateId),
        'mail_template_type_id' => Uuid::fromHexToBytes($mailTemplateTypeId),
        'system_default' => 1,
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);

    // Create template translation
    $connection->insert('mail_template_translation', [
        'mail_template_id' => Uuid::fromHexToBytes($mailTemplateId),
        'language_id' => Uuid::fromHexToBytes('2fbb5fe2e29a4d70aa5854ce7ce3e20b'),
        'subject' => 'Content Plus: {{ subject }}',
        'content_html' => '<p>Hello {{ name }},</p><p>{{ message }}</p>',
        'content_plain' => 'Hello {{ name }}, {{ message }}',
        'sender_name' => '{{ salesChannel.name }}',
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);
}
```

## Sending Mails Programmatically

```php
use Shopware\Core\Content\Mail\Service\AbstractMailService;
use Shopware\Core\Framework\Validation\DataBag\DataBag;

class NotificationService
{
    public function __construct(
        private readonly AbstractMailService $mailService,
    )
    {
    }

    public function sendNotification(Context $context): void
    {
        $data = new DataBag([
            'recipients' => ['user@example.com' => 'User Name'],
            'senderName' => 'My Shop',
            'salesChannelId' => $salesChannelId,
            'contentHtml' => '<p>Hello World</p>',
            'contentPlain' => 'Hello World',
            'subject' => 'Notification',
        ]);

        $this->mailService->send($data->all(), $context);
    }
}
```

## Adding Data to Mail Events

Subscribe to `MailBeforeSentEvent` to add template variables:

```php
use Shopware\Core\Content\Mail\Events\MailBeforeSentEvent;

class MailDataSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            MailBeforeSentEvent::class => 'onMailBeforeSent',
        ];
    }

    public function onMailBeforeSent(MailBeforeSentEvent $event): void
    {
        $data = $event->getData();
        $data['customVariable'] = 'Custom Value';
        // Variables are available in the mail template as {{ customVariable }}
    }
}
```

## Flow Builder Integration

Mail templates can be triggered through the Flow Builder by creating a flow action that sends mails (see `references/flow-builder.md`).
