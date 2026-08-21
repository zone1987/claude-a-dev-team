# sw-entity-many-to-many-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelProperty | `any` | `'name'` | no |  |
| resultLimit | `any` | `25` | no |  |
| valueLimit | `any` | `5` | no |  |
| localMode | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| entityCollection | `any` | — | yes |  |
| context | `any` | — | no |  |
| advancedSelectionComponent | `any` | `''` | no |  |
| advancedSelectionParameters | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| update:entityCollection | — | |
| item-add | — | |
| item-remove | — | |
| search-term-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `isSelected` | |
| `fetchDisplayItems` | |
| `displayAssigned` | |
| `displaySearch` | |
| `sendSearchRequest` | |
| `findAssignedEntities` | |
| `search` | |
| `paginateResult` | |
| `paginateDisplayList` | |
| `emitChanges` | |
| `addItem` | |
| `remove` | |
| `removeIdFromList` | |
| `resetSearchCriteria` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `onSearchTermChange` | |
| `resetActiveItem` | |
| `debouncedSearch` | |
| `resetResultCollection` | |
| `getKey` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `searchRepository` | |
| `selectedIds` | |
| `visibleValues` | |
| `invisibleValueCount` | |
| `isAdvancedSelectionActive` | |

## Examples

### Basic Usage
```twig
<sw-entity-many-to-many-select>
    <!-- content -->
</sw-entity-many-to-many-select>
```
