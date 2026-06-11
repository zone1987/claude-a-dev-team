---
name: sw-field-types
description: >
  Alle Shopware-6 DAL-Field-Typen: IdField, FkField, StringField, IntField, FloatField, BoolField, JsonField,
  DateTimeField, ListField, PriceField, TranslatedField, EnumField, Association-Felder u.v.m.
  Trigger: "Field type", "welches Field", "JsonField", "FkField", "DateTimeField", "ListField", "EnumField",
  "Feld in defineFields", "DAL field". Shopware 6.7.
---

# Shopware 6 — Field-Typen

Felder werden in `defineFields()` deklariert. Auswahl der wichtigsten (50+ insgesamt):

| Feld | Zweck |
|---|---|
| `IdField` / `FkField` / `ReferenceVersionField` | Primär-/Fremdschlüssel (Binary UUID) |
| `StringField` / `LongTextField` | Text |
| `IntField` / `FloatField` / `BoolField` | Skalare |
| `JsonField` / `ListField` | strukturierte Daten / Arrays |
| `DateTimeField` / `DateField` | Zeit |
| `PriceField` | Preise (→ `sw-pricing-field`) |
| `TranslatedField` | übersetzbar (→ `sw-translations`) |
| `EnumField` | PHP-Enum-Backed (6.6+) |
| `CustomFields` | Custom-Fields-Container (→ `sw-custom-fields`) |
| `*AssociationField` | Beziehungen (→ `sw-associations-*`) |

Jedes Feld: `new XField('storageName', 'propertyName')`, optional `->addFlags(...)` (`sw-field-flags`).
`storageName` = DB-Spalte (snake_case), `propertyName` = Entity-Property (camelCase).

→ Vollständige Field-Liste mit Optionen: [references/field-types.md](references/field-types.md)
→ Media-/File-Feld-Beispiel: [references/media-example.md](references/media-example.md)
