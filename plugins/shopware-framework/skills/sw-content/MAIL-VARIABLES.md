# Shopware 6 — Mail template variable reference

Every mail template type has a complete nested variable tree available.

## How variables get into templates

```
Flow trigger (event) → FlowStorer (per aware interface) → flow->data()
→ SendMailAction::handleFlow() → templateData['order'] / ['customer'] / …
→ MailService::createMail() adds 'salesChannel'
→ Twig rendering with all keys as top-level variables
```

Always available (every mail template): `eventName`, `salesChannelId`, `salesChannel`.

## Querying the variable tree

→ All template types + triggering events: [MAIL-VARIABLES-MAIL-TEMPLATES.md](MAIL-VARIABLES-MAIL-TEMPLATES.md)
→ Complete nested variable tree per template: [MAIL-VARIABLES-VARIABLE-TREES.md](MAIL-VARIABLES-VARIABLE-TREES.md)
→ Machine-readable JSON tree: [references/deep/variable-trees.json](references/deep/variable-trees.json)

## Adding custom variables

Via `MailBeforeValidateEvent` — details: `sw-mail-data`.

```php
public function onBeforeValidate(MailBeforeValidateEvent $event): void
{
    $data = $event->getTemplateData();
    $data['myVar'] = 'value';
    $event->setTemplateData($data);
}
```
