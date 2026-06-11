# JS SDK — Helpers (Criteria, Admin API, App-Actions, Media, Notification)

## Criteria

`import { Criteria, TotalCountMode } from "@shopware-ag/app-server-sdk/helper/criteria"`

Full-featured criteria builder mirroring Shopware's DAL. Chainable API.

```ts
constructor(ids: string[] = [])
```

### Instance methods (chainable unless noted)

| Method | Purpose |
|--------|---------|
| `setPage(n)` / `setLimit(n)` | Pagination |
| `setTerm(term)` | Full-text search |
| `addFilter(filter)` | Add filter |
| `addPostFilter(filter)` | Post-aggregation filter |
| `addSorting(sorting)` | Add sort |
| `addQuery(filter, score, scoreField?)` | Scored search |
| `addGrouping(field)` | GROUP BY field |
| `addFields(...fields)` | SELECT only specific fields |
| `addAggregation(aggregation)` | Add aggregation |
| `addAssociation<K>(field)` | Type-safe association (makes field non-nullable) |
| `getAssociation<K>(field)` | Get/create sub-criteria for association |
| `hasAssociation(prop)` | Check if association registered |
| `addIncludes(obj)` | Restrict returned fields per entity |
| `setTotalCountMode(mode)` | See `TotalCountMode` enum |
| `setIds(ids[])` | Load by IDs |
| `setTitle(title)` | For query debugging |
| `toPayload()` | Serialize to API request body |
| `resetSorting()` | Remove all sortings |

### TotalCountMode enum

```ts
enum TotalCountMode {
    NO_TOTAL_COUNT = 0,         // Default; fastest — no total calculated
    EXACT_TOTAL_COUNT = 1,      // Exact count (slow on large datasets)
    PAGINATION_TOTAL_COUNT = 2, // limit*5+1 (fast, "has next page" check)
}
```

### Static filter factories

```ts
Criteria.equals(field, value)                    // field = value
Criteria.equalsAny(field, values[])              // field IN (...)
Criteria.contains(field, value)                  // field LIKE %value%
Criteria.prefix(field, value)                    // field LIKE value%
Criteria.suffix(field, value)                    // field LIKE %value
Criteria.range(field, { lte?, lt?, gte?, gt? })  // range filter
Criteria.not(operator, queries[])                // NOT (q1 AND/OR q2...)
Criteria.multi(operator, queries[])              // q1 AND/OR q2...
```

### Static aggregation factories

```ts
Criteria.avg(name, field)
Criteria.count(name, field)
Criteria.max(name, field)
Criteria.min(name, field)
Criteria.stats(name, field)                      // sum/max/min/avg/count
Criteria.sum(name, field)
Criteria.terms(name, field, limit?, sort?, aggregation?)   // bucket
Criteria.entityAggregation(name, field, definition)
Criteria.filter(name, filters[], aggregation)
Criteria.histogram(name, field, interval?, format?, aggregation?, timeZone?)
```

### Static sorting factories

```ts
Criteria.sort(field, order?, naturalSorting?)
Criteria.naturalSorting(field, order?)
Criteria.countSorting(field, order?)
```

### Type-safe usage example

```ts
import { Criteria } from "@shopware-ag/app-server-sdk/helper/criteria";
import { EntityRepository } from "@shopware-ag/app-server-sdk/helper/admin-api";

type Product = { id: string; name: string; active: boolean; manufacturer?: { name: string } };
const repo = new EntityRepository<Product>(httpClient, "product");

const criteria = new Criteria<Product>()
    .setLimit(25)
    .addFilter(Criteria.equals("active", true))
    .addAssociation("manufacturer");  // TypeScript infers manufacturer as non-nullable

const result = await repo.search(criteria);
result.data[0].manufacturer.name; // no TypeScript error
```

## EntityRepository

`import { EntityRepository } from "@shopware-ag/app-server-sdk/helper/admin-api"`

Type-safe Admin API entity repository.

```ts
constructor(client: HttpClient, entityName: string)
// entityName: underscores → hyphens for URL routing (product_foo → /search/product-foo)
```

| Method | Description |
|--------|-------------|
| `search<T, Agg>(criteria, context?)` | POST `/search/{entity}` → `EntitySearchResult<T, Agg>` |
| `searchIds(criteria, context?)` | POST `/search-ids/{entity}` → `string[]` |
| `aggregate<Agg>(criteria, context?)` | Forces `limit: 1`, POST `/search/{entity}` |
| `upsert(payload[], context?)` | Delegates to `SyncService` with action `upsert` |
| `delete(payload[], context?)` | Delegates to `SyncService` with action `delete` |
| `deleteByFilters(filters[], context?)` | Delegates to `SyncService` with filter-based delete |

## ApiContext

Controls API headers per request.

```ts
constructor(
    languageId?: string | null,
    inheritance?: boolean | null,
    versionId?: string | null,
    skipTriggerFlows?: boolean | null,
    indexingSkip?: string | null,
    indexingBehaviour?: string | null
)
toHeaders(): Record<string, string>
```

Maps to headers: `sw-language-id`, `sw-inheritance`, `sw-version-id`, `sw-skip-trigger-flow`, `indexing-skip`, `indexing-behavior`. Null values omitted.

## EntitySearchResult

```ts
constructor(total: number, aggregations: Aggregations, data: Entity[])
first(): Entity | null  // returns data[0] or null
```

## SyncService

```ts
constructor(client: HttpClient)
sync(operations: SyncOperation[], context?: ApiContext): Promise<void>  // POST /_action/sync
```

## SyncOperation

```ts
constructor(
    key: string,                          // Operation identifier
    entity: string,                       // Entity name (underscores)
    action: "upsert" | "delete",
    payload: object[],
    criteria: SingleFilter[] | null = null  // For filter-based deletes
)
```

## Defaults

Shopware system UUIDs:

```ts
const Defaults = {
    systemLanguageId: "2fbb5fe2e29a4d70aa5854ce7ce3e20b",
    liveVersion: "0fa91ce3e96a4bc2be4bd9ce752c3425",
    systemCurrencyId: "b7d2554b0ce847cd82f3ac9bd1c0dfca",
    salesChannelTypeApi: "f183ee5650cf4bdb8a774337575067a6",
    salesChannelTypeSalesChannel: "8a243080f92e4c719546314b577cf82b",
    salesChannelTypeProductComparision: "ed535e5722134ac1aa6524f73e26881b",
}
```

## uuid()

```ts
import { uuid } from "@shopware-ag/app-server-sdk/helper/admin-api";
uuid()  // crypto.randomUUID().replaceAll("-", "")
```

## App Action Response Helpers

`import { createNotificationResponse, createNewTabResponse, createModalResponse } from "@shopware-ag/app-server-sdk/helper/app-actions"`

```ts
createNotificationResponse(
    status: "success" | "error" | "info" | "warning",
    message: string
): Response
// Body: { actionType: "notification", payload: { status, message } }

createNewTabResponse(redirectUrl: string): Response
// Body: { actionType: "openNewTab", payload: { redirectUrl } }

createModalResponse(
    iframeUrl: string,
    size?: "small" | "medium" | "large" | "fullscreen",  // default: "medium"
    expand?: boolean  // default: false
): Response
// Body: { actionType: "openModal", payload: { iframeUrl, size, expand } }
```

## Media Helpers

`import { uploadMediaFile, uploadMediaByUrl, ... } from "@shopware-ag/app-server-sdk/helper/media"`

```ts
uploadMediaFile(httpClient, options: {
    private?: boolean;
    mediaFolderId?: string | null;
    fileName: string;    // must include extension, e.g. "product.jpg"
    file: Blob | Promise<Blob>;
}): Promise<string>     // returns media entity UUID

uploadMediaByUrl(httpClient, options: {
    private?: boolean;
    mediaFolderId?: string | null;
    fileName: string;
    url: string;
}): Promise<string>     // returns media entity UUID

getMediaDefaultFolderByEntity(httpClient, entity: string): Promise<string | null>
// e.g. entity = "product" → finds default media folder for products

getMediaFolderByName(httpClient, name: string): Promise<string | null>

createMediaFolder(httpClient, name: string, options: { parentId?: string }): Promise<string>
```

On upload failure: both `uploadMediaFile` and `uploadMediaByUrl` delete the created media entity and rethrow.

## Notification Helper

`import { sendNotification } from "@shopware-ag/app-server-sdk/helper/notification"`

```ts
sendNotification(httpClient: HttpClient, notification: {
    status: "neutral" | "info" | "attention" | "critical" | "positive";
    message: string;
    adminOnly?: boolean;
    requiredPrivileges?: string[];
}): Promise<void>
// POST /notification
```
