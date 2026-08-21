---
name: sw-fields
description: Shopware DAL fields: field types, flags, inheritance, serializers, custom fields, translations, all four association kinds. Use when the request names a Shopware field type or association.
---

# Shopware DAL fields and associations

What a definition is made of. Associations come in four shapes and each needs a specific field pair.

## Reference map

- **[ASSOCIATIONS.md](references/ASSOCIATIONS.md)**: Properties: - `$referenceClass`: FQCN of referenced EntityDefinition - `$referenceField`: Field on referenced…. [ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE](references/ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md), [ASSOCIATIONS-MANYTOMANY](references/ASSOCIATIONS-MANYTOMANY.md), [ASSOCIATIONS-MANYTOONE-ASSOCIATIONS](references/ASSOCIATIONS-MANYTOONE-ASSOCIATIONS.md), [ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE](references/ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md), [ASSOCIATIONS-MANYTOONE](references/ASSOCIATIONS-MANYTOONE.md), [ASSOCIATIONS-ONETOMANY-ASSOCIATIONS](references/ASSOCIATIONS-ONETOMANY-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOMANY](references/ASSOCIATIONS-ONETOMANY.md), [ASSOCIATIONS-ONETOONE-ASSOCIATIONS](references/ASSOCIATIONS-ONETOONE-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOONE](references/ASSOCIATIONS-ONETOONE.md).
- **[CUSTOM-FIELDS.md](references/CUSTOM-FIELDS.md)**: Configurable extra fields on existing entities — stored in the `custom_fields` JSON.
- **[FIELD-FLAGS.md](references/FIELD-FLAGS.md)**: Flags control a field's behaviour and visibility: `->addFlags, new ApiAware)`. [FIELD-FLAGS-FLAGS](references/FIELD-FLAGS-FLAGS.md).
- **[FIELD-INHERITANCE.md](references/FIELD-INHERITANCE.md)**: Lets a child inherit field values from its parent when it has no value of its own.
- **[FIELD-SERIALIZER.md](references/FIELD-SERIALIZER.md)**: Every field type has a serializer that governs `encode`, `decode` and validation.
- **[FIELD-TYPES.md](references/FIELD-TYPES.md)**: Fields are declared in `defineFields`., [FIELD-TYPES-MEDIA-EXAMPLE](references/FIELD-TYPES-MEDIA-EXAMPLE.md).
- **[PRICING.md](references/PRICING.md)**: Keyed by `currencyId` - each currency has exactly one price entry. [PRICING-FIELD](references/PRICING-FIELD.md).
- **[TRANSLATIONS.md](references/TRANSLATIONS.md)**: Translatable values live in a separate `*_translation` table. [TRANSLATIONS-EXAMPLE](references/TRANSLATIONS-EXAMPLE.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
