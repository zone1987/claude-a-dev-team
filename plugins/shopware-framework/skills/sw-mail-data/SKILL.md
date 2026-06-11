---
name: sw-mail-data
description: >
  Daten/Variablen für Shopware-6 E-Mails bereitstellen: MailBeforeValidateEvent/MailBeforeSentEvent, eigene Template-Daten
  injizieren, MailSender, Anhänge. Trigger: "Mail Daten", "MailBeforeValidateEvent", "Template-Variablen mail",
  "Mail Anhang", "eigene Daten in E-Mail", "MailBeforeSentEvent". Shopware 6.7.
---

# Shopware 6 — Mail-Daten & -Versand

Template-Variablen kommen aus dem auslösenden Kontext (Flow/Event). Zusätzliche Daten oder Anhänge via Subscriber
auf die Mail-Events ergänzen.

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
    // $event->getContext(), Anhänge über die Mail-Attachment-Mechanik
}
```

`MailBeforeValidateEvent` (Daten/Validierung) und `MailBeforeSentEvent` (kurz vor Versand). Versand selbst über den
`AbstractMailService`. Templates/Typen: `sw-mail-template`. Versand als Flow-Action: `sw-flow-action`.
