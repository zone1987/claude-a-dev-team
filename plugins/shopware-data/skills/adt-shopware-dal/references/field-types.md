# Field Types

## Base Class: Field (abstract)

**Extends:** `Struct`
**Constructor:** `__construct(protected string $propertyName)`

Default behavior: Adds `ApiAware(AdminApiSource::class)` flag automatically.

Key methods:
- `compile(DefinitionInstanceRegistry $registry): void`
- `getPropertyName(): string`
- `getExtractPriority(): int` (default: 0)
- `setFlags(Flag ...$flags): self` / `addFlags(Flag ...$flags): self` / `removeFlag(string $class): self`
- `is(string $class): bool` / `getFlag(string $class): ?Flag`
- `getSerializer(): FieldSerializerInterface`
- `setDescription(string): self`

### StorageAware (interface)

Marks fields that map to a physical DB column. Method: `getStorageName(): string`.

---

## ID & Foreign Key Fields

### IdField

- **Implements:** `StorageAware`
- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `BINARY(16)` (UUID as binary)
- **Serializer:** `IdFieldSerializer`
- **Extract priority:** 75

### FkField

- **Implements:** `StorageAware`
- **Constructor:** `(string $storageName, string $propertyName, string $referenceClass, string $referenceField = 'id')`
- **DB type:** `BINARY(16)`
- **Serializer:** `FkFieldSerializer`
- **Extract priority:** 70
- Uses lazy compilation to resolve reference definitions

### ParentFkField

- **Extends:** `FkField`
- **Constructor:** `(string $referenceClass)`
- Hardcodes: `storageName = 'parent_id'`, `propertyName = 'parentId'`

---

## Scalar / Primitive Fields

### StringField

- **Constructor:** `(string $storageName, string $propertyName, int $maxLength = 255)`
- **DB type:** `VARCHAR(255)`
- **Serializer:** `StringFieldSerializer`

### LongTextField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `LONGTEXT`
- **Serializer:** `LongTextFieldSerializer`

### IntField

- **Constructor:** `(string $storageName, string $propertyName, ?int $minValue = null, ?int $maxValue = null)`
- **DB type:** `INT(11)`
- **Serializer:** `IntFieldSerializer`

### FloatField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `DOUBLE`
- **Serializer:** `FloatFieldSerializer`

### BoolField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `TINYINT(1)`
- **Serializer:** `BoolFieldSerializer`

---

## Date & Time Fields

### DateField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `DATE`

### DateTimeField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `DATETIME(3)` (millisecond precision)

### DateIntervalField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `VARCHAR(255)` (ISO 8601 duration, e.g. `P1Y2M3D`)

### CronIntervalField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `VARCHAR(255)` (cron expression)

---

## Specialized String Fields

### EmailField

- **Extends:** `StringField`
- **Serializer:** `EmailFieldSerializer` (adds email format validation)

### PasswordField

- **Constructor:** `(string $storageName, string $propertyName, ?string $algorithm = PASSWORD_DEFAULT, array $hashOptions = [], ?string $for = null)`
- **Constants:** `FOR_CUSTOMER = 'customer'`, `FOR_ADMIN = 'admin'`
- **DB type:** `VARCHAR(1024)`

### TimeZoneField

- **Extends:** `StringField`
- **Serializer:** `TimeZoneFieldSerializer` (validates IANA timezone identifier)

### RemoteAddressField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `VARCHAR(255)`
- **Serializer:** `RemoteAddressFieldSerializer` (may anonymize IP)

---

## JSON-Based Fields

### JsonField

- **Constructor:** `(string $storageName, string $propertyName, array $propertyMapping = [], ?array $default = null)`
- **DB type:** `JSON`
- `$propertyMapping`: `list<Field>` defining sub-field schema for validation
- **Accessor builder:** `JsonFieldAccessorBuilder` (enables JSON path queries)

### ListField

- **Extends:** `JsonField`
- **Constructor:** `(string $storageName, string $propertyName, ?string $fieldType = null)`
- `$fieldType`: optional class-string to enforce element types (e.g., `IntField::class`)

### ObjectField

- **Extends:** `JsonField`
- **Constructor:** `(string $storageName, string $propertyName)`
- Arbitrary JSON object (no sub-field schema)

### ConfigJsonField

- **Extends:** `JsonField`
- Uses a `_value` wrapper key for type-safe config storage
- **Accessor builder:** `ConfigJsonFieldAccessorBuilder`

### CustomFields

- **Extends:** `JsonField`
- **Constructor:** `(string $storageName = 'custom_fields', string $propertyName = 'customFields')`
- **Serializer:** `CustomFieldsSerializer`
- **Accessor builder:** `CustomFieldsAccessorBuilder`
- Property mapping is populated dynamically at runtime based on registered custom field sets
- Unique method: `setPropertyMapping(array $propertyMapping): void`

### BlobField

- **Constructor:** `(string $storageName, string $propertyName)`
- **DB type:** `LONGBLOB`

---

## Price & Commerce Fields

### PriceField

- **Extends:** `JsonField`
- **Constructor:** `(string $storageName, string $propertyName)`
- **Accessor builder:** `PriceFieldAccessorBuilder` (currency-aware filtering)
- Multi-currency price collection (net/gross per currency)

### PriceDefinitionField

- **Extends:** `JsonField`
- Stores price rule/definition objects (QuantityPriceDefinition, AbsolutePriceDefinition, etc.)

### CalculatedPriceField

- **Extends:** `JsonField`
- Hardcoded property mapping: `unitPrice` (float, Required), `totalPrice` (float, Required), `quantity` (int, Required), `calculatedTaxes` (JSON, Required), `taxRules` (JSON, Required), `referencePrice` (JSON), `listPrice` (JSON with price/discount/percentage), `regulationPrice` (JSON with price)

### CartPriceField

- **Extends:** `JsonField`
- Hardcoded: `netPrice`, `totalPrice`, `calculatedTaxes`, `taxRules`, `positionPrice`, `rawTotal`, `taxStatus` (all Required)

### CashRoundingConfigField

- **Extends:** `JsonField`
- Hardcoded: `decimals` (int, min 0, Required), `interval` (float, Required), `roundForNet` (bool, Required)

### TaxFreeConfigField

- **Extends:** `JsonField`
- Hardcoded: `enabled` (bool, Required), `currencyId` (string, Required), `amount` (float, Required)

### VariantListingConfigField

- **Extends:** `JsonField`
- Product variant listing display configuration

---

## Enum & Serialized Fields

### EnumField

- **Constructor:** `(string $storageName, string $propertyName, \BackedEnum $enum)`
- **DB type:** `VARCHAR(255)` for string-backed, `INT(11)` for int-backed
- Maps PHP `\BackedEnum` to DB column

### SerializedField

- **Constructor:** `(string $storageName, string $propertyName, string $serializer = JsonFieldSerializer::class)`
- Generic field allowing custom serializer injection
- Used internally by attribute-based entity definitions

---

## Auto-Increment & Special Fields

### AutoIncrementField

- **Extends:** `IntField`, no parameters
- Hardcodes: `storageName = 'auto_increment'`, `propertyName = 'autoIncrement'`
- Auto-adds `WriteProtected` flag

### LockedField

- **Extends:** `BoolField`, no parameters
- Hardcodes: `storageName = 'locked'`, `propertyName = 'locked'`
- Auto-adds `Computed` flag (read-only)

---

## Tree / Hierarchy Fields

### TreeBreadcrumbField

- **Extends:** `JsonField`
- **Constructor:** `(string $storageName = 'breadcrumb', string $propertyName = 'breadcrumb', string $nameField = 'name')`
- Auto-adds `WriteProtected(Context::SYSTEM_SCOPE)`
- Auto-computed breadcrumb for tree structures

### TreeLevelField

- **Extends:** `IntField`
- **Constructor:** `(string $storageName, string $propertyName)`
- Auto-adds `WriteProtected(Context::SYSTEM_SCOPE)`
- Stores depth/level in tree hierarchy

### TreePathField

- **Extends:** `LongTextField`
- **Constructor:** `(string $storageName, string $propertyName, string $pathField = 'id')`
- Auto-adds `WriteProtected(Context::SYSTEM_SCOPE)`
- Stores materialized path (e.g., `|uuid1|uuid2|uuid3|`)

### ChildCountField

- **Extends:** `IntField`, no parameters
- Hardcodes: `storageName = 'child_count'`, `propertyName = 'childCount'`
- Auto-adds `WriteProtected(Context::SYSTEM_SCOPE)`

### BreadcrumbField

- **Extends:** `JsonField`
- Used in translation entities for category breadcrumbs

---

## Timestamp Fields

### CreatedAtField

- **Extends:** `DateTimeField`, no parameters
- Hardcodes: `storageName = 'created_at'`, `propertyName = 'createdAt'`
- Auto-adds `Required` flag
- **Serializer:** `CreatedAtFieldSerializer` (auto-sets on create if not provided)

### UpdatedAtField

- **Extends:** `DateTimeField`, no parameters
- Hardcodes: `storageName = 'updated_at'`, `propertyName = 'updatedAt'`
- **Serializer:** `UpdatedAtFieldSerializer` (auto-sets on every write)

---

## Audit / Tracking Fields

### CreatedByField

- **Extends:** `FkField`
- **Constructor:** `(array $allowedWriteScopes = [Context::SYSTEM_SCOPE])`
- Hardcodes: FK to `UserDefinition`, storage `created_by_id`
- Auto-sets from context user

### UpdatedByField

- **Extends:** `FkField`
- **Constructor:** `(array $allowedWriteScopes = [Context::SYSTEM_SCOPE])`
- Hardcodes: FK to `UserDefinition`, storage `updated_by_id`
- Auto-sets from context user on update

---

## Versioning Fields

### VersionField

- **Extends:** `FkField`, no parameters
- Hardcodes: FK to `VersionDefinition`, storage `version_id`
- Auto-adds `PrimaryKey` and `Required` flags
- Part of composite PK for versionable entities

### ReferenceVersionField

- **Extends:** `FkField`
- **Constructor:** `(string $definition, ?string $storageName = null)`
- `$storageName` auto-generated as `{entity_name}_version_id` if null
- Stores the version ID of a referenced versionable entity

### VersionDataPayloadField

- **Extends:** `JsonField`
- @internal - stores full data payload of a version commit

---

## State Machine Field

### StateMachineStateField

- **Extends:** `FkField`
- **Constructor:** `(string $storageName, string $propertyName, string $stateMachineName, array $allowedWriteScopes = [Context::SYSTEM_SCOPE])`
- FK to `StateMachineStateDefinition`
- Direct writes restricted; state changes normally go through state machine transitions

---

## Non-Storage Fields

### TranslatedField

- **NOT StorageAware** (no DB column on main entity)
- **Constructor:** `(string $propertyName, bool $useForSorting = false)`
- **Extract priority:** 100 (highest)
- Resolves to the corresponding field on the entity's translation table

### ManyToManyIdField

- **Extends:** `ListField`
- **Constructor:** `(string $storageName, string $propertyName, string $associationName)`
- Auto-adds `WriteProtected` flag
- Denormalized cache of IDs from a many-to-many association (auto-computed by indexer)

---

## Extract Priority Order

| Priority | Field Type |
|----------|-----------|
| 100 | TranslatedField |
| 90 | TranslationsAssociationField |
| 80 | ManyToOneAssociationField, OneToOneAssociationField, ParentAssociationField |
| 75 | IdField |
| 70 | FkField (and descendants) |
| 0 | All other fields |
