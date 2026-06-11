---
name: sw-field-serializer
description: >
  Eigener FieldSerializer in Shopware 6 DAL: Schreib-/Leselogik eines (eigenen) Field-Typs, encode/decode,
  Validation-Constraints. Trigger: "FieldSerializer", "eigener Field-Typ", "encode decode field", "custom field type DAL",
  "AbstractFieldSerializer". Shopware 6.7.
---

# Shopware 6 — FieldSerializer

Jeder Field-Typ hat einen Serializer, der `encode()` (Entity→DB) und `decode()` (DB→Entity) sowie Validation regelt.
Nur nötig für **eigene** Field-Typen oder spezielle Persistenz.

```php
class FfMoneyFieldSerializer extends AbstractFieldSerializer
{
    public function encode(Field $field, EntityExistence $existence, KeyValuePair $data, WriteParameterBag $params): \Generator
    {
        yield $field->getStorageName() => $data->getValue() === null ? null : (int) round($data->getValue() * 100);
    }
    public function decode(Field $field, mixed $value): ?float
    {
        return $value === null ? null : ((int) $value) / 100;
    }
}
```

Registrierung via `shopware.field_serializer`-Tag, der eigene `Field` referenziert den Serializer-Service.
In den meisten Fällen reichen Standard-Felder (`sw-field-types`) — Serializer nur bei echten Sonderformaten.
