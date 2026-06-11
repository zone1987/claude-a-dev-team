# Flags

Flags control field behavior for API visibility, validation, deletion cascading, write protection, inheritance, search, and more.

## Flag (abstract base)

All flags extend this class. Key method: `abstract parse(): \Generator` (yields key/value for serialization).

---

## ApiAware

**Constructor:** `(string ...$protectedSources)`

Controls which API endpoints can **read** this field.

- No args = exposed to both Admin API and Store API
- `new ApiAware(AdminApiSource::class)` = Admin API only (DEFAULT on every field)
- `new ApiAware(SalesChannelApiSource::class)` = Store API only

Method: `isSourceAllowed(string $source): bool` (SystemSource always allowed).

## ApiCriteriaAware

No parameters. Allows bypassing `ApiAware` restriction specifically for criteria usage (filtering/sorting/aggregation). Used for price fields where raw data is hidden but the accessor builder handles calculations in SQL.

## Required

No parameters. Field must be provided during write operations.

## PrimaryKey

No parameters. Marks a field as part of the entity's primary key.

## Inherited

**Constructor:** `(?string $foreignKey = null)`

Field data can be inherited from a parent record (used in parent-child structures like product variants). If child's value is NULL, parent's value is used. `$foreignKey` overrides expected FK name for multiple references to the same table.

## ReverseInherited

**Constructor:** `(string $propertyName)`

Counterpart to `Inherited`. Applied on the referenced entity side. Tells DAL which property name on the referenced definition corresponds to the inherited relationship.

## CascadeDelete

**Constructor:** `(bool $cloneRelevant = true)`

When parent is deleted, all associated records are also deleted (DAL-level cascade). `$cloneRelevant = false` means association is not duplicated during clone.

## RestrictDelete

No parameters. Prevents deletion if associated records exist.

## SetNullOnDelete

**Constructor:** `(bool $enforcedByConstraint = true)`

FK is set to NULL when referenced entity is deleted. `$enforcedByConstraint = false` for circular references (application-level handling).

## WriteProtected

**Constructor:** `(string ...$allowedScopes)`

Prevents writing unless context has an allowed scope (e.g., `Context::SYSTEM_SCOPE`, `Context::CRUD_API_SCOPE`).

## Runtime

**Constructor:** `(array $dependsOn = [])`

Field data is NOT stored in DB; loaded at runtime by event subscriber or service. `$dependsOn` declares which fields must be loaded first.

## Computed

No parameters. Value is computed by indexer and stored in DB, but CANNOT be written directly. Different from `Runtime`: value exists in DB but is read-only.

## Extension

No parameters. Field data stored in `Entity::$extensions` instead of direct properties. Used by plugins to extend entities without modifying entity classes.

## SearchRanking

**Constructor:** `(float $ranking, bool $tokenize = true)`

Search weight for full-text search.

Constants:
- `ASSOCIATION_SEARCH_RANKING = 0.25`
- `LOW_SEARCH_RANKING = 80`
- `MIDDLE_SEARCH_RANKING = 250`
- `HIGH_SEARCH_RANKING = 500`

`$tokenize = false` for fields matched as a whole (e.g., product numbers).

## AllowHtml

**Constructor:** `(bool $sanitized = true)`

Allows HTML content. `$sanitized = true` passes through XSS sanitizer. `$sanitized = false` stores raw HTML (dangerous).

## AllowEmptyString

No parameters. Prevents DAL from normalizing empty string to NULL.

## Immutable

No parameters. Write-once, then read-only. Cannot be updated after creation.

## NoConstraint

No parameters. Used on `FkField` to indicate no real FK constraint in DB. Affects write-order resolution. Needed for circular references (e.g., `product.coverId -> product_media.id`).

## Since

**Constructor:** `(string $since)` (version string like `'6.4.0.0'`)

Documents which Shopware version introduced this field.

## Deprecated

**Constructor:** `(string $deprecatedSince, string $willBeRemovedIn, ?string $replacedBy = null)`

Marks field as deprecated with migration path.

## AsArray

No parameters. Forces JSON field to be serialized/deserialized as array instead of object.

## RuleAreas

**Constructor:** `(string ...$areas)`

Tags a rule association with business areas: `PRODUCT_AREA`, `PAYMENT_AREA`, `SHIPPING_AREA`, `PROMOTION_AREA`, `FLOW_AREA`, `FLOW_CONDITION_AREA`.

## DoNotUseContext

No parameters. Prevents `FkFieldSerializer` from auto-filling FK values from WriteContext. FK must come from explicit payload only.

## IgnoreInOpenapiSchema

No parameters. Excludes field from auto-generated OpenAPI schema. Requires manual custom schema.
