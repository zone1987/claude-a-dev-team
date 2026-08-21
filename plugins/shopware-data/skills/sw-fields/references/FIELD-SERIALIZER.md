# Shopware 6 — FieldSerializer

Every field type has a serializer that governs `encode()` (entity→DB), `decode()` (DB→entity) and validation.
Only needed for **your own** field types or special persistence.

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

Register it with the `shopware.field_serializer` tag; your own `Field` references the serializer service.
In most cases the standard fields are enough (`sw-field-types`) — write a serializer only for genuinely special formats.
