# Shopware DAL — complete concept documentation

Source: `concepts/framework/data-abstraction-layer.md`

---

## Database access

Shopware uses **no ORM** (no Doctrine), but a Data Abstraction Layer (DAL) of its own.
Concepts such as Criteria are similar to Doctrine, but implemented for Shopware-specific requirements.

Reference ERD: https://developer.shopware.com/assets/shopware6-erd.pdf (for 6.6.5.0)

---

## CRUD operations

`EntityRepository` is the only recommended way to interact with the DAL.

### Providing it via dependency injection

```php
// Constructor injection
public function __construct(EntityRepository $productRepository)
{
    $this->productRepository = $productRepository;
}
```

```php
// Explicit DI configuration (services.php)
$services->set(DalExampleService::class)
    ->args([service('product.repository')]);
```

With service autowiring and the correct type + argument name, the repository is injected automatically.

---

## Translations (DAL level)

On read/search operations three language levels are searched:

1. **Current language** — the language shown to the user
2. **Parent language** — optional superordinate language for dialects (e.g. `de-DE` as parent of `de-AT`)
3. **System language** — the installation language; every entity has at least one translation here (final fallback)

Translations are stored in separate tables: `<entity-table>_translation` (suffix `_translation`).

---

## Versioning

- Enables multiple versions of an entity
- All associated data is duplicated for the new version
- Multiple entities/changes can be assigned to one version
- Use: previews, publishing, campaigns (prepare changes without going live)

**Restriction**: no "draft first, then live" — a live version must always exist
before a new version can be derived from it.

**Database structure**: versionable entities have a compound FK: `id` + `version_id`.
Foreign keys onto versioned records: `product_id` + `product_version_id`.

---

## Context (`core/Framework/Context.php`)

- Instantiated once per request
- Defines important shop configuration
- Influences the CRUD behaviour of the DAL (e.g. switch currency → all operations use the new currency)
- Contains: language, currency, price rules, permissions

---

## Inheritance

Implemented for the product/variant system:

- **Parent-child inheritance** — variants inherit records, properties and associations from the parent product
- Example: a variant without its own categories/images → inherits from the parent product
- Applies to fields and associations

---

## Indexing (entity indexer pattern)

Design principle: "the more time is invested in indexing, the faster reading becomes."

- Products are written rarely, but read very frequently
- On write: the corresponding **product indexer** is triggered
- The indexer pre-selects aggregations and writes them optimised for later reads
- Result: reads are minimally expensive (denormalised, indexed data)
