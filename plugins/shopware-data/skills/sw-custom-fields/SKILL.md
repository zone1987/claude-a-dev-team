---
name: sw-custom-fields
description: >
  Custom Fields in Shopware 6: CustomFieldSet + CustomField per Migration/Repository anlegen, Typen, Entity-Zuordnung,
  Auslesen via getCustomFields(), Media-/Entity-Selection-Typ. Trigger: "Custom Field", "CustomFieldSet",
  "Zusatzfeld", "custom_field anlegen", "getCustomFields", "Entity-Selection custom field", "Media custom field".
  Shopware 6.7. Scaffolder: /sw-custom-field.
---

# Shopware 6 — Custom Fields

Konfigurierbare Zusatzfelder an bestehenden Entities (ohne neue Spalte) — landen im `custom_fields`-JSON.

```php
// per Repository/Migration: CustomFieldSet mit relations + fields
$this->customFieldSetRepo->upsert([[
    'name' => 'ff_extra',
    'config' => ['label' => ['de-DE' => 'Extra']],
    'relations' => [['entityName' => 'product']],
    'customFields' => [[
        'name' => 'ff_extra_hint', 'type' => CustomFieldTypes::TEXT,
        'config' => ['label' => ['de-DE' => 'Hinweis']],
    ]],
]], $context);
```

Auslesen: `$entity->getCustomFields()['ff_extra_hint']`. Typen u.a. `text`, `bool`, `int`, `float`, `datetime`,
`select`, `entity` (Entity-Selection), `media`. Eigene echte Spalten/Associations → `sw-entity-extension`.

→ Typen, Media-/Entity-Selection, Storefront-Zugriff: [references/custom-fields.md](references/custom-fields.md)
