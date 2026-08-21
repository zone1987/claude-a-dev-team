# Shopware 6 — Mail data & sending

Template variables come from the triggering context (flow/event). Add extra data or attachments via a subscriber
on the mail events.

```php
public static function getSubscribedEvents(): array
{
    return [ MailBeforeValidateEvent::class => 'onBeforeValidate' ];
}
public function onBeforeValidate(MailBeforeValidateEvent $event): void
{
    $data = $event->getTemplateData();
    $data['ffExtra'] = $this->loadExtra($data['order'] ?? null);
    $event->setTemplateData($data);
    // $event->getContext(), attachments via the mail attachment mechanism
}
```

`MailBeforeValidateEvent` (data/validation) and `MailBeforeSentEvent` (just before sending). Sending itself goes through
the `AbstractMailService`. Templates/types: `sw-mail-template`. Sending as a flow action: `sw-flow-action`.
