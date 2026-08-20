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

→ Alle Template-Typen + auslösende Events: [MAIL-VARIABLES-MAIL-TEMPLATES.md](MAIL-VARIABLES-MAIL-TEMPLATES.md)
→ Vollständiger verschachtelter Variablen-Baum je Template: [MAIL-VARIABLES-VARIABLE-TREES.md](MAIL-VARIABLES-VARIABLE-TREES.md)
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
