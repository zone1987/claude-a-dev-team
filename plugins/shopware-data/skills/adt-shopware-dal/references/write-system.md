# Write System and Events

## Write Pipeline Flow

1. Raw data enters via `EntityRepository->create/update/upsert/delete()`
2. `WriteInputValidator::validate()` ensures correct structure (list of assoc arrays)
3. `WriteCommandExtractor::normalize()` processes each field's serializer
4. `PrimaryKeyBag` collects PKs; `gateway->prefetchExistences()` batch-loads DB state
5. `WriteCommandExtractor::extract()` encodes values, creates Insert/Update commands
6. For deletes: restrict violations checked, Delete/Cascade/SetNull commands created
7. `WriteCommandQueue::getCommandsInOrder()` resolves FK dependencies
8. `PreWriteValidationEvent` dispatched (LockValidator, ParentRelationValidator)
9. `EntityWriteEvent` / `EntityDeleteEvent` dispatched (with success/error callbacks)
10. Gateway executes SQL, computes change sets where requested
11. `PostWriteValidationEvent` dispatched (can roll back transaction)
12. `EntityWriteResultFactory::build()` creates results, resolves parent/mapping impacts
13. `EntityWrittenContainerEvent` dispatched
14. Success/error callbacks executed

## Write Commands

| Command | Extends | Purpose | Privilege |
|---|---|---|---|
| `InsertCommand` | `WriteCommand` | Row insertion | `PRIVILEGE_CREATE` |
| `UpdateCommand` | `WriteCommand` | Row update, implements `ChangeSetAware` | `PRIVILEGE_UPDATE` |
| `DeleteCommand` | `WriteCommand` | Row deletion, implements `ChangeSetAware` | `PRIVILEGE_DELETE` |
| `CascadeDeleteCommand` | `DeleteCommand` | Cascade-delete of child entity | `null` (no ACL) |
| `SetNullOnDeleteCommand` | `UpdateCommand` | Sets FK to NULL on referenced entity delete | `null` (no ACL) |
| `JsonUpdateCommand` | `UpdateCommand` | Partial JSON column update | `PRIVILEGE_UPDATE` |

### WriteCommandQueue

Collects commands and resolves FK-dependency-aware execution order. `getCommandsInOrder()` iterates up to 50 times to resolve dependencies, throws `ImpossibleWriteOrderException` if circular.

### ChangeSet

Captures before/after state of a DB row. Methods:
- `getBefore(?string $property)` / `getAfter(?string $property)`
- `hasChanged(string $property): bool`

## Write Context

Tracks state for entire write operation: entity/property paths for cross-entity FK resolution, language mappings, exception collection.

Key methods:
- `set/get/has(entity, property, value)` - path-based value store
- `getLanguageId(string $identifier): ?string` - resolves UUID or locale code
- `scope(string $scope, callable $callback)` - temporary scope change

## Write Validation

### PreWriteValidationEvent

Dispatched BEFORE commands execute. Subscribers can inspect commands and add exceptions to block the write.

### PostWriteValidationEvent

Dispatched AFTER execution, before transaction commit. Adding exceptions rolls back everything.

### Built-in Validators

- **LockValidator:** Prevents modification of locked entities (`locked = 1`)
- **ParentRelationValidator:** Prevents self-referencing parent (`parent_id === id`)

## EntityWriteResult

Per-entity-row write result.

Constants: `OPERATION_INSERT`, `OPERATION_UPDATE`, `OPERATION_DELETE`

Properties: `$primaryKey`, `$payload`, `$entityName`, `$operation`, `$existence`, `$changeSet`

## Events

### Write Events

| Event | When | Name Pattern |
|---|---|---|
| `EntityWriteEvent` | Before any write | - |
| `EntityDeleteEvent` | Before delete | - |
| `EntityWrittenEvent` | After write (insert/update) | `{entity}.written` |
| `EntityDeletedEvent` | After delete | `{entity}.deleted` |
| `EntityWrittenContainerEvent` | After write (all entities) | - |

### Read Events

| Event | When | Name Pattern |
|---|---|---|
| `EntityLoadedEvent` | After entities loaded | `{entity}.loaded` |
| `PartialEntityLoadedEvent` | After partial entities loaded | `{entity}.partial_loaded` |
| `EntityLoadedContainerEvent` | Container for all loaded events | - |

### Search Events

| Event | When | Name Pattern |
|---|---|---|
| `EntitySearchedEvent` | When search performed | - |
| `EntitySearchResultLoadedEvent` | After search results | `{entity}.search.result.loaded` |
| `EntityIdSearchResultLoadedEvent` | After ID search | `{entity}.id.search.result.loaded` |
| `EntityAggregationResultLoadedEvent` | After aggregation | `{entity}.aggregation.result.loaded` |
| `BeforeEntityAggregationEvent` | Before aggregation query | - |

### Other Events

| Event | Purpose |
|---|---|
| `RefreshIndexEvent` | Trigger index refresh |
| `BeforeVersionMergeEvent` | Manipulate writes during version merge |

### EntityWrittenContainerEvent Key Methods

- `getEventByEntityName(string $entityName): ?EntityWrittenEvent`
- `getPrimaryKeys(string $entity): list`
- `getDeletedPrimaryKeys(string $entity): list`
- `getPrimaryKeysWithPropertyChange(string $entity, array $properties): list`
