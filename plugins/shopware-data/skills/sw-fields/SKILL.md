---
name: sw-fields
description: Shopware DAL fields: field types, flags, inheritance, serializers, custom fields, translations, all four association kinds. Use when the request names a Shopware field type or association.
---

# Shopware DAL fields and associations

What a definition is made of. Associations come in four shapes and each needs a specific field pair.

## Reference map

- **[ASSOCIATIONS.md](ASSOCIATIONS.md)**: Properties: - `$referenceClass`: FQCN of referenced EntityDefinition - `$referenceField`: Field on referenced…. [ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE](ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md), [ASSOCIATIONS-MANYTOMANY](ASSOCIATIONS-MANYTOMANY.md), [ASSOCIATIONS-MANYTOONE-ASSOCIATIONS](ASSOCIATIONS-MANYTOONE-ASSOCIATIONS.md), [ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE](ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md), [ASSOCIATIONS-MANYTOONE](ASSOCIATIONS-MANYTOONE.md), [ASSOCIATIONS-ONETOMANY-ASSOCIATIONS](ASSOCIATIONS-ONETOMANY-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOMANY](ASSOCIATIONS-ONETOMANY.md), [ASSOCIATIONS-ONETOONE-ASSOCIATIONS](ASSOCIATIONS-ONETOONE-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOONE](ASSOCIATIONS-ONETOONE.md).
- **[CUSTOM-FIELDS.md](CUSTOM-FIELDS.md)**: Configurable extra fields on existing entities — stored in the `custom_fields` JSON. [CUSTOM-FIELDS-DETAIL](CUSTOM-FIELDS-DETAIL.md).
- **[FIELD-FLAGS.md](FIELD-FLAGS.md)**: Flags control a field's behaviour and visibility: `->addFlags, new ApiAware)`. [FIELD-FLAGS-FLAGS](FIELD-FLAGS-FLAGS.md).
- **[FIELD-INHERITANCE.md](FIELD-INHERITANCE.md)**: Lets a child inherit field values from its parent when it has no value of its own.
- **[FIELD-SERIALIZER.md](FIELD-SERIALIZER.md)**: Every field type has a serializer that governs `encode`, `decode` and validation.
- **[FIELD-TYPES.md](FIELD-TYPES.md)**: Fields are declared in `defineFields`. [FIELD-TYPES-DETAIL](FIELD-TYPES-DETAIL.md), [FIELD-TYPES-MEDIA-EXAMPLE](FIELD-TYPES-MEDIA-EXAMPLE.md).
- **[PRICING.md](PRICING.md)**: Keyed by `currencyId` - each currency has exactly one price entry. [PRICING-FIELD](PRICING-FIELD.md).
- **[TRANSLATIONS.md](TRANSLATIONS.md)**: Translatable values live in a separate `*_translation` table. [TRANSLATIONS-EXAMPLE](TRANSLATIONS-EXAMPLE.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
