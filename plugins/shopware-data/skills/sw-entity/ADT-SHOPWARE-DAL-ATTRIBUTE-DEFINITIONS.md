# PHP Attribute-Based Definitions

Modern alternative to `defineFields()` using PHP 8 attributes. A compiler pass reads attributes and generates metadata consumed by `AttributeEntityDefinition`.

## #[Entity] (TARGET_CLASS)

```php
#[Entity(
    name: 'my_entity',
    parent: null,              // Parent entity class for aggregates
    since: null,               // Version introduced
    collectionClass: EntityCollection::class,
    hydratorClass: EntityHydrator::class
)]
```

## #[Field] (TARGET_PROPERTY)

Base attribute for all field types.

```php
#[Field(type: FieldType::STRING, translated: false, api: false, column: null)]
```

- `$type`: One of `FieldType` constants
- `$translated`: Whether field is translatable
- `$api`: `true`/`false` or `['admin-api' => bool, 'store-api' => bool]`
- `$column`: Custom column name override

## FieldType Constants

`UUID`, `STRING`, `TEXT`, `INT`, `FLOAT`, `BOOL`, `ENUM`, `JSON`, `DATETIME`, `DATE`, `DATE_INTERVAL`, `TIME_ZONE`

## Specialized Field Attributes

| Attribute | Type | Extra Parameters |
|---|---|---|
| `#[AutoIncrement]` | auto-increment | Always API-visible |
| `#[CustomFields]` | custom-fields | `translated`, `column` |
| `#[ForeignKey]` | fk | `entity`, `api`, `column` |
| `#[State]` | state | `machine`, `scopes`, `api`, `column` |
| `#[Serialized]` | serialized | `serializer` class |
| `#[Version]` | version | Makes entity version-aware |
| `#[ReferenceVersion]` | reference-version | `entity`, `column` |

## Association Attributes

### #[ManyToOne]
```php
#[ManyToOne(entity: 'manufacturer', onDelete: OnDelete::NO_ACTION, ref: 'id', api: false, column: null)]
```

### #[OneToOne]
```php
#[OneToOne(entity: 'order_customer', column: null, onDelete: OnDelete::NO_ACTION, ref: 'id', api: false)]
```

### #[OneToMany]
```php
#[OneToMany(entity: 'product_media', ref: 'product_id', onDelete: OnDelete::NO_ACTION, api: false)]
```

### #[ManyToMany]
```php
#[ManyToMany(entity: 'category', onDelete: OnDelete::NO_ACTION, api: false, mapping: null)]
```

### #[Translations]
No parameters. Always API-visible.

## OnDelete Enum

Values: `CASCADE`, `SET_NULL`, `RESTRICT`, `NO_ACTION`

## Marker Attributes

| Attribute | Parameters | Purpose |
|---|---|---|
| `#[PrimaryKey]` | none | Part of primary key |
| `#[Required]` | none | Required for writes |
| `#[AllowEmptyString]` | none | Preserve empty strings |
| `#[AllowHtml]` | `bool $sanitized = false` | Allow HTML content |
| `#[Inherited]` | `?string $foreignKey = null` | Inherited from parent |
| `#[ReverseInherited]` | `string $propertyName` | Reverse side of inheritance |
| `#[Protection]` | `array $write` | Write scope protection |

## AttributeEntityDefinition

Constructs itself from a `$meta` array. `defineFields()` iterates meta fields, creates TranslatedField for translated properties, instantiates field classes with args, applies flags.

## AttributeMappingDefinition

Extends `MappingEntityDefinition`. Adds `ReferenceVersionField` automatically when source/reference entities are version-aware.

## AttributeTranslationDefinition

Extends `EntityTranslationDefinition`. Entity name: `{meta.entity_name}_translation`. Only includes fields where `translated = true`.
