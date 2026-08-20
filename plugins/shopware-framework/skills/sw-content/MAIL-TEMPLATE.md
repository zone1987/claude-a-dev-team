# Shopware 6 — Mail templates

Emails are based on `mail_template` (content) + `mail_template_type` (type/variable context). Create custom templates
via migration/repository.

```php
$this->mailTemplateTypeRepo->upsert([[
    'id' => $typeId, 'technicalName' => 'ff_custom_notice', 'name' => 'FF Notice',
    'availableEntities' => ['order' => 'order'],
]], $context);
$this->mailTemplateRepo->upsert([[
    'mailTemplateTypeId' => $typeId,
    'subject' => 'Info on {{ order.orderNumber }}',
    'contentHtml' => '<p>...</p>', 'contentPlain' => '...',
]], $context);
```

The content is Twig (HTML + plain). Sending via the `MailService` or a **flow action** "Send mail" (`sw-flow-action`).
Data/variables available in the template: `sw-mail-data`. Editable in the admin (Settings → Email templates).

→ Mail details: [MAIL.md](MAIL.md)
