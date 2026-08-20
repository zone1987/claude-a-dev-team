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

→ Typen, Media-/Entity-Selection, Storefront-Zugriff: [CUSTOM-FIELDS-DETAIL.md](CUSTOM-FIELDS-DETAIL.md)
