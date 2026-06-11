# Association Fields

## AssociationField (abstract base)

**Extends:** `Field`

Properties:
- `$referenceClass`: FQCN of referenced EntityDefinition
- `$referenceField`: Field on referenced entity for joining (typically `'id'`)
- `$autoload`: If true, association loaded automatically without explicit Criteria inclusion

---

## ManyToOneAssociationField

**Constructor:**
```php
(
    string $propertyName,       // e.g., 'manufacturer'
    string $storageName,        // DB column for FK (e.g., 'product_manufacturer_id')
    string $referenceClass,     // Referenced EntityDefinition FQCN
    string $referenceField = 'id',
    bool $autoload = false
)
```

**DB:** FK column on THIS entity's table.
**Priority:** 80
**Relationship:** N:1 - Many records reference one record.

---

## OneToManyAssociationField

**Constructor:**
```php
(
    string $propertyName,       // e.g., 'products'
    string $referenceClass,     // Referenced EntityDefinition (the "many" side)
    string $referenceField,     // FK on referenced entity pointing back
    string $localField = 'id'
)
```

**DB:** FK on the REFERENCED entity's table.
**Relationship:** 1:N - One record has many related records.

---

## ManyToManyAssociationField

**Constructor:**
```php
(
    string $propertyName,            // e.g., 'categories'
    string $toManyDefinitionClass,   // TARGET entity FQCN
    string $mappingDefinition,       // PIVOT entity FQCN
    string $mappingLocalColumn,      // FK in mapping table -> THIS entity
    string $mappingReferenceColumn,  // FK in mapping table -> TARGET entity
    string $sourceColumn = 'id',
    string $referenceField = 'id'
)
```

**DB:** Pivot table with two FK columns.
**Key methods:**
- `getToManyReferenceDefinition()` - TARGET entity definition
- `getMappingDefinition()` - PIVOT entity definition

---

## OneToOneAssociationField

**Constructor:**
```php
(
    string $propertyName,
    string $storageName,        // FK column on THIS entity
    string $referenceField,     // Field on referenced entity
    string $referenceClass,
    bool $autoload = true       // NOTE: defaults to TRUE
)
```

**DB:** Same as ManyToOne (FK on this table). One-to-one enforced by logic/unique constraint.
**Priority:** 80
**Key difference from ManyToOne:** Autoload defaults to `true`, different parameter order.

---

## ParentAssociationField

**Extends:** `ManyToOneAssociationField`

**Constructor:** `(string $referenceClass, string $referenceField = 'id')`

Self-referencing ManyToOne for tree structures. Hardcodes `propertyName = 'parent'`, `storageName = 'parent_id'`.

---

## ChildrenAssociationField

**Extends:** `OneToManyAssociationField`

**Constructor:** `(string $referenceClass, string $propertyName = 'children')`

Inverse of ParentAssociationField. Loads all rows where `parent_id = this.id`.
**Auto-applies:** `CascadeDelete` flag.

---

## TranslationsAssociationField

**Extends:** `OneToManyAssociationField`

**Constructor:** `(string $referenceClass, string $referenceField, string $propertyName = 'translations', string $localField = 'id')`

Specialized OneToMany for the translation pattern.
**Priority:** 90
**Auto-applies:** `CascadeDelete` flag.
**Language field:** Hardcoded `'language_id'` column in translation table.

---

## Summary Tables

### Autoload Defaults

| Association | Autoload |
|---|---|
| ManyToOne | `false` |
| OneToMany | `false` |
| ManyToMany | `false` |
| OneToOne | **`true`** |
| Parent | `false` |
| Children | `false` |
| Translations | `false` |

### Auto-Applied Flags

| Association | Extra Flags |
|---|---|
| ChildrenAssociation | `CascadeDelete` |
| TranslationsAssociation | `CascadeDelete` |
| All others | None (only base `ApiAware(AdminApiSource)`) |

### Extract Priority

| Association | Priority |
|---|---|
| TranslationsAssociation | 90 |
| ManyToOne, OneToOne, Parent | 80 |
| OneToMany, ManyToMany, Children | 0 |
