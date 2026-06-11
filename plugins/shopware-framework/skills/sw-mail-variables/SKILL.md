---
name: sw-mail-variables
description: >
  Vollständiger Variablen-Baum für alle Shopware-6-Mail-Templates: welche Variablen im E-Mail-Template verfügbar
  sind, verschachtelter Variablenbaum per Template-Typ, Twig-Pfade (order.lineItems, order.orderCustomer.email
  usw.), auslösende Events, Aware-Interfaces. Trigger: "welche Variablen E-Mail-Template",
  "Mail Template Variablen", "Variablen Bestellbestätigung", "available mail variables", "mail variable tree",
  "Twig Variablen Shopware Mail", "E-Mail Template Variablen Shopware". Shopware 6.7.
---

# Shopware 6 — Mail-Template Variablen-Referenz

Pro Mail-Template-Typ steht ein vollständiger verschachtelter Variablen-Baum zur Verfügung.

## Wie Variables in Templates gelangen

```
Flow-Trigger (Event) → FlowStorer (je Aware-Interface) → flow->data()
→ SendMailAction::handleFlow() → templateData['order'] / ['customer'] / …
→ MailService::createMail() fügt 'salesChannel' hinzu
→ Twig-Rendering mit allen Schlüsseln als Top-Level-Variablen
```

Immer verfügbar (jedes Mail-Template): `eventName`, `salesChannelId`, `salesChannel`.

## Variablen-Baum abfragen

→ Alle Template-Typen + auslösende Events: [references/deep/mail-templates.md](references/deep/mail-templates.md)
→ Vollständiger verschachtelter Variablen-Baum je Template: [references/deep/variable-trees.md](references/deep/variable-trees.md)
→ Maschinenlesbarer JSON-Baum: [references/deep/variable-trees.json](references/deep/variable-trees.json)

## Eigene Variablen ergänzen

Via `MailBeforeValidateEvent` — Details: `sw-mail-data`.

```php
public function onBeforeValidate(MailBeforeValidateEvent $event): void
{
    $data = $event->getTemplateData();
    $data['myVar'] = 'value';
    $event->setTemplateData($data);
}
```
