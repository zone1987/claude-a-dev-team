# Shopware 6 — Mail-Templates

E-Mails basieren auf `mail_template` (Inhalt) + `mail_template_type` (Typ/Variablen-Kontext). Eigene Templates per
Migration/Repository anlegen.

```php
$this->mailTemplateTypeRepo->upsert([[
    'id' => $typeId, 'technicalName' => 'ff_custom_notice', 'name' => 'FF Hinweis',
    'availableEntities' => ['order' => 'order'],
]], $context);
$this->mailTemplateRepo->upsert([[
    'mailTemplateTypeId' => $typeId,
    'subject' => 'Info zu {{ order.orderNumber }}',
    'contentHtml' => '<p>...</p>', 'contentPlain' => '...',
]], $context);
```

Inhalt ist Twig (HTML + Plain). Versand über den `MailService` bzw. eine **Flow-Action** „Mail senden" (`sw-flow-action`).
Daten/Variablen, die im Template verfügbar sind: `sw-mail-data`. Im Admin editierbar (Einstellungen → E-Mail-Templates).

→ Mail-Details: [MAIL.md](MAIL.md)
