# Shopware 6 — Custom fields

Configurable extra fields on existing entities (without a new column) — stored in the `custom_fields` JSON.

```php
// via repository/migration: CustomFieldSet with relations + fields
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

Reading: `$entity->getCustomFields()['ff_extra_hint']`. Types include `text`, `bool`, `int`, `float`, `datetime`,
`select`, `entity` (entity selection), `media`. For real columns and associations of your own → `sw-entity-extension`.

→ Types, media/entity selection, storefront access: [CUSTOM-FIELDS-DETAIL.md](CUSTOM-FIELDS-DETAIL.md)
