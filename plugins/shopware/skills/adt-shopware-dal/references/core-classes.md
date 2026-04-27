# Core Classes

## Entity

**Namespace:** `Shopware\Core\Framework\DataAbstractionLayer`
**Extends:** `Struct`

Base class for all DAL entities. Provides unique identifier management, versioning, translated fields, timestamps, field visibility control (for Twig rendering), and JSON serialization.

### Properties

| Visibility | Name | Type | Default |
|---|---|---|---|
| `protected` | `$_uniqueIdentifier` | `string` | - |
| `protected` | `$versionId` | `?string` | `null` |
| `protected` | `$translated` | `array<string, mixed>` | `[]` |
| `protected` | `$createdAt` | `?\DateTimeInterface` | `null` |
| `protected` | `$updatedAt` | `?\DateTimeInterface` | `null` |

### Key Methods

| Method | Returns | Description |
|---|---|---|
| `get(string $property)` | `mixed` | Gets property value, falls back to extensions, then foreignKeys extension |
| `has(string $property)` | `bool` | Checks property existence via `property_exists` |
| `getTranslated()` | `array` | Returns all translated field values |
| `getTranslation(string $field)` | `mixed\|null` | Returns single translated field value |
| `addTranslated(string $key, mixed $value)` | `void` | Adds/overwrites a single translated value |
| `jsonSerialize()` | `array` | Serializes entity, filters invisible fields, merges foreignKeys |
| `getApiAlias()` | `string` | Entity name or derived from class name (CamelCase to snake_case) |
| `internalSetEntityData(string $entityName, FieldVisibility $fieldVisibility)` | `self` | @internal - sets entity name and field visibility |

### Traits

**EntityIdTrait** - Provides the standard `id` property. When `setId()` is called, it also updates `_uniqueIdentifier`.

```php
trait EntityIdTrait {
    protected string $id;
    public function getId(): string;
    public function setId(string $id): void; // also sets _uniqueIdentifier
}
```

**EntityCustomFieldsTrait** - Provides custom fields support with merge behavior.

```php
trait EntityCustomFieldsTrait {
    #[CustomFields]
    protected ?array $customFields = null;
    
    public function getCustomFields(): ?array;
    public function getCustomFieldsValues(string ...$fields): array;
    public function getCustomFieldsValue(string $field): mixed;
    public function getTranslatedCustomFieldsValue(string $field): mixed;
    public function setCustomFields(?array $customFields): void;
    public function changeCustomFields(array $customFields): void; // merges via array_replace
}
```

---

## EntityCollection

**Extends:** `Collection<TElement of Entity>`

Typed collection of Entity objects, keyed by unique identifiers.

### Key Methods

| Method | Returns | Description |
|---|---|---|
| `add($entity)` | `void` | Adds entity keyed by unique identifier |
| `getIds()` | `array<string>` | All unique identifiers |
| `filterByProperty(string $property, mixed $value)` | `static` | Filter to matching entities |
| `filterAndReduceByProperty(string $property, mixed $value)` | `static` | Filter + remove from current collection |
| `merge(self $collection)` | `void` | Merge, skipping duplicates |
| `insert(int $position, Entity $entity)` | `void` | Insert at position |
| `getList(array $ids)` | `static` | Get subset by IDs |
| `sortByIdArray(array $ids)` | `void` | Reorder to match ID array order |
| `getCustomFieldsValues(string ...$fields)` | `array` | Custom fields across all entities |

---

## EntityDefinition (abstract)

The schema class that declares fields, associations, and entity capabilities.

### Abstract Methods

| Method | Returns | Description |
|---|---|---|
| `getEntityName()` | `string` | Entity name (e.g., `'product'`) |
| `defineFields()` | `FieldCollection` | Declares entity fields |

### Key Methods

| Method | Returns | Description |
|---|---|---|
| `getFields()` | `CompiledFieldCollection` | Compiles and returns all fields (cached) |
| `getField(string $propertyName)` | `?Field` | Single field by property name |
| `getPrimaryKeys()` | `CompiledFieldCollection` | Fields flagged with PrimaryKey |
| `getCollectionClass()` | `string` | Default: `EntityCollection::class` |
| `getEntityClass()` | `string` | Default: `ArrayEntity::class` |
| `getDefaults()` | `array` | Default values for new entities |
| `getChildDefaults()` | `array` | Default values for child entities |
| `isInheritanceAware()` | `bool` | Default: `false` |
| `isVersionAware()` | `bool` | True if entity has `versionId` field |
| `isLockAware()` | `bool` | True if entity has `LockedField` |
| `isSeoAware()` | `bool` | True if entity has `seoUrls` association |
| `isChildrenAware()` | `bool` | True if entity has `ChildrenAssociationField` |
| `isParentAware()` | `bool` | True if entity has `ParentAssociationField` |
| `getTranslationDefinition()` | `?EntityDefinition` | Translation entity if present |
| `getParentDefinition()` | `?EntityDefinition` | Parent definition if declared |
| `addExtension(EntityExtension $ext)` | `void` | Adds plugin extension |
| `getProtections()` | `EntityProtectionCollection` | Entity-level protections |
| `since()` | `?string` | Version this definition was introduced |

### Default Fields

Every `EntityDefinition` automatically includes `CreatedAtField` and `UpdatedAtField` via `defaultFields()`.

---

## EntityRepository

**Marked:** `@final`

Main entry point for all CRUD operations. Wraps reading, searching, aggregating, creating, updating, upserting, deleting, versioning, merging, and cloning.

### Methods

| Method | Signature | Returns |
|---|---|---|
| `search` | `(Criteria $criteria, Context $context)` | `EntitySearchResult` |
| `aggregate` | `(Criteria $criteria, Context $context)` | `AggregationResultCollection` |
| `searchIds` | `(Criteria $criteria, Context $context)` | `IdSearchResult` |
| `create` | `(array $data, Context $context)` | `EntityWrittenContainerEvent` |
| `update` | `(array $data, Context $context)` | `EntityWrittenContainerEvent` |
| `upsert` | `(array $data, Context $context)` | `EntityWrittenContainerEvent` |
| `delete` | `(array $ids, Context $context)` | `EntityWrittenContainerEvent` |
| `createVersion` | `(string $id, Context $context, ?string $name, ?string $versionId)` | `string` (version ID) |
| `merge` | `(string $versionId, Context $context)` | `void` |
| `clone` | `(string $id, Context $context, ?string $newId, ?CloneBehavior $behavior)` | `EntityWrittenContainerEvent` |

---

## EntityTranslationDefinition (abstract)

**Extends:** `EntityDefinition`

Base for translation table definitions. Automatically generates base fields:
- FkField for parent entity ID (PrimaryKey, Required)
- FkField for `language_id` (PrimaryKey, Required)
- ManyToOneAssociationField to parent entity
- ManyToOneAssociationField to language
- ReferenceVersionField if parent is version-aware (PrimaryKey, Required)

### Required Override

```php
protected function getParentDefinitionClass(): string
{
    return ParentDefinition::class; // MUST be implemented
}
```

---

## MappingEntityDefinition (abstract)

**Extends:** `EntityDefinition`

Base for many-to-many pivot/join table definitions. No entity class, no collection class, no default fields (createdAt/updatedAt).

Calling `getCollectionClass()` or `getEntityClass()` throws `MappingEntityClassesException`.

---

## EntityExtension (abstract)

Allows plugins to add fields, modify existing fields, and add protections to entity definitions without modifying the original class.

```php
abstract class EntityExtension {
    public function extendFields(FieldCollection $collection): void {}
    public function modifyFields(FieldCollection $collection): void {}
    public function extendProtections(EntityProtectionCollection $protections): void {}
    abstract public function getEntityName(): string;
}
```

Fields added via `extendFields()` automatically get the `Extension` flag. Their data goes to `$entity->getExtension('fieldName')` instead of direct properties.

---

## Supporting Classes

### TranslationEntity

**Extends:** `Entity`

Base entity for translation rows. Adds `languageId` (string) and `language` (?LanguageEntity) properties.

### PartialEntity

**Extends:** `ArrayEntity`

Used when only specific fields are requested in a Criteria. Behaves as a dynamic key-value bag.

### FieldCollection

Collection of Field objects. Can be compiled into `CompiledFieldCollection` via `compile(DefinitionInstanceRegistry)`.

### CompiledFieldCollection

**Extends:** `FieldCollection`

Optimized, compiled version with lookup indexes: by storage name, translated fields, extension fields, children association. Fields keyed by property name.

Key methods:
- `getByStorageName(string $storageName): ?Field`
- `filterByFlag(string $flagClass): self`
- `getBasicFields(): self` - non-association fields + autoloaded associations
- `getTranslatedFields(): array`
- `getExtensionFields(): array`

### FieldVisibility

Controls which fields are visible in Twig rendering contexts. When `$isInTwigRenderingContext` is true, internal (non-ApiAware) fields are hidden.

### DefinitionInstanceRegistry

Central registry mapping entity names to EntityDefinition instances and repository service IDs. Service locator for field serializers, resolvers, and accessor builders.

Key methods:
- `getRepository(string $entityName): EntityRepository`
- `getByEntityName(string $entityName): EntityDefinition`
- `get(string $class): EntityDefinition`
- `getSerializer(string $class): FieldSerializerInterface`
- `register(EntityDefinition $definition): void`
