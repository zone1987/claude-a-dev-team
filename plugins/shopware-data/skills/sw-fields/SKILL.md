---
name: sw-fields
description: Shopware DAL fields: field types, flags, inheritance, serializers, custom fields, translations, all four association kinds. Use when the request names a Shopware field type or association.
---

# Shopware DAL fields and associations

What a definition is made of. Associations come in four shapes and each needs a specific field pair.

## Reference map

- **[ASSOCIATIONS.md](ASSOCIATIONS.md)**: Properties: - `$referenceClass`: FQCN of referenced EntityDefinition - `$referenceField`: Field on referenced…. [ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE](ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md), [ASSOCIATIONS-MANYTOMANY](ASSOCIATIONS-MANYTOMANY.md), [ASSOCIATIONS-MANYTOONE-ASSOCIATIONS](ASSOCIATIONS-MANYTOONE-ASSOCIATIONS.md), [ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE](ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md), [ASSOCIATIONS-MANYTOONE](ASSOCIATIONS-MANYTOONE.md), [ASSOCIATIONS-ONETOMANY-ASSOCIATIONS](ASSOCIATIONS-ONETOMANY-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOMANY](ASSOCIATIONS-ONETOMANY.md), [ASSOCIATIONS-ONETOONE-ASSOCIATIONS](ASSOCIATIONS-ONETOONE-ASSOCIATIONS.md), [ASSOCIATIONS-ONETOONE](ASSOCIATIONS-ONETOONE.md).
- **[CUSTOM-FIELDS.md](CUSTOM-FIELDS.md)**: Konfigurierbare Zusatzfelder an bestehenden Entities — landen im `custom_fields`-JSON. [CUSTOM-FIELDS-DETAIL](CUSTOM-FIELDS-DETAIL.md).
- **[FIELD-FLAGS.md](FIELD-FLAGS.md)**: Flags steuern Verhalten/Sichtbarkeit eines Feldes: `->addFlags, new ApiAware)`. [FIELD-FLAGS-FLAGS](FIELD-FLAGS-FLAGS.md).
- **[FIELD-INHERITANCE.md](FIELD-INHERITANCE.md)**: Erlaubt, dass ein Child Feldwerte vom Parent erbt, wenn es selbst keinen Wert hat.
- **[FIELD-SERIALIZER.md](FIELD-SERIALIZER.md)**: Jeder Field-Typ hat einen Serializer, der `encode` und `decode` sowie Validation regelt.
- **[FIELD-TYPES.md](FIELD-TYPES.md)**: Felder werden in `defineFields` deklariert. [FIELD-TYPES-DETAIL](FIELD-TYPES-DETAIL.md), [FIELD-TYPES-MEDIA-EXAMPLE](FIELD-TYPES-MEDIA-EXAMPLE.md).
- **[PRICING.md](PRICING.md)**: Keyed by `currencyId` - each currency has exactly one price entry. [PRICING-FIELD](PRICING-FIELD.md).
- **[TRANSLATIONS.md](TRANSLATIONS.md)**: Übersetzbare Werte liegen in einer separaten `*_translation`-Tabelle. [TRANSLATIONS-EXAMPLE](TRANSLATIONS-EXAMPLE.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
