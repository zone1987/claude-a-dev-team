# sw-entity-advanced-selection-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entityName | `any` | — | yes |  |
| entityDisplayText | `any` | — | yes |  |
| storeKey | `any` | — | yes |  |
| entityColumns | `any` | — | yes |  |
| entityFilters | `any` | — | yes |  |
| emptyImagePath | `any` | — | no |  |
| emptyIcon | `any` | `'solid-content'` | no |  |
| entityAssociations | `any` | — | no |  |
| isSingleSelect | `any` | `false` | no |  |
| isRecordSelectableCallback | `any` | — | no |  |
| criteriaFilters | `any` | — | no |  |
| criteriaAggregations | `any` | — | no |  |
| entityContext | `any` | — | no |  |
| initialSearchTerm | `any` | — | no |  |
| initialSelection | `any` | — | no |  |
| disablePreviews | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| `preview-${column.property}` | — | |
| `column-${column.property}` | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| selection-submit | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onSelectionChange` | |
| `onApply` | |
| `updateCriteria` | |
| `debouncedGetList` | |
| `clearFilters` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `entityRepository` | |
| `entityDefinition` | |
| `assignmentProperties` | |
| `allEntityAssociations` | |
| `entityCriteria` | |
| `activeFilterNumber` | |
| `defaultFilters` | |
| `listFilters` | |
| `previewColumns` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-entity-advanced-selection-modal
    entityName="..."
    entityDisplayText="..."
    storeKey="..."
>
    <!-- content -->
</sw-entity-advanced-selection-modal>
```
