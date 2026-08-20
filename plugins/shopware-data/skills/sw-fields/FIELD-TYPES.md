# Shopware 6 — Field types

Fields are declared in `defineFields()`. The most important ones (50+ in total):

| Field | Purpose |
|---|---|
| `IdField` / `FkField` / `ReferenceVersionField` | primary/foreign keys (binary UUID) |
| `StringField` / `LongTextField` | text |
| `IntField` / `FloatField` / `BoolField` | scalars |
| `JsonField` / `ListField` | structured data / arrays |
| `DateTimeField` / `DateField` | time |
| `PriceField` | prices (→ `sw-pricing-field`) |
| `TranslatedField` | translatable (→ `sw-translations`) |
| `EnumField` | backed by a PHP enum (6.6+) |
| `CustomFields` | custom fields container (→ `sw-custom-fields`) |
| `*AssociationField` | relations (→ `sw-associations-*`) |

Every field: `new XField('storageName', 'propertyName')`, optionally `->addFlags(...)` (`sw-field-flags`).
`storageName` = DB column (snake_case), `propertyName` = entity property (camelCase).

→ Complete field list with options: [FIELD-TYPES-DETAIL.md](FIELD-TYPES-DETAIL.md)
→ Media/file field example: [FIELD-TYPES-MEDIA-EXAMPLE.md](FIELD-TYPES-MEDIA-EXAMPLE.md)
