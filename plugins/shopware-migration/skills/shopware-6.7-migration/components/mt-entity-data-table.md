# mt-entity-data-table

> Data table with integrated Shopware entity data source.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `keyof EntitySchema.Entities` | — | yes | |
| repository | `typeof Repository` | — | no | |
| forceRealModal | `boolean` | — | no | |
| columns | `ColumnDefinition[]` | — | yes | |
| columnChanges | `Record<string, ColumnChanges>` | — | no | |
| title | `string` | — | no | |
| subtitle | `string` | — | no | |
| layout | `"default" | "full"` | — | no | |
| allowBulkDelete | `boolean` | — | no | |
| allowBulkEdit | `boolean` | — | no | |
| allowRowSelection | `boolean` | — | no | |
| bulkEditMoreActions | `{` | — | no | |
| id | `string` | — | yes | |
| label | `string` | — | yes | |
| onClick | `() => void` | — | yes | |
| icon | `"default" | "critical" | "active" | string` | — | no | |
| type | `"default" | "active" | "critical"` | — | no | |
| metaCopy | `string` | — | no | |
| contextualDetail | `string` | — | no | |
| disableDelete | `boolean` | — | no | |
| disableEdit | `boolean` | — | no | |
| disableSearch | `boolean` | — | no | |
| disableSettingsTable | `boolean` | — | no | |
| additionalContextButtons | `{` | — | no | |
| key | `string` | — | yes | |
| caption | `string` | — | no | |
| paginationOptions | `number[]` | — | no | |
| availableFilters | `AvailableFilter[]` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| bulk-delete | rowIds: string[] | |
| bulk-edit | rowIds: string[] | |
| open-details | — | |

## Examples

### Basic Usage
```vue
<mt-entity-data-table
    entity="..."
    columns="..."
    id="..."
>
    <!-- content -->
</mt-entity-data-table>
```
