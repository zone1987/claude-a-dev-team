# sw-settings-tag-list

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk-modal-merge-confirm-text | — | |
| bulk-modal-merge-confirm-name-input | — | |
| bulk-modal-merge-progress | — | |
| bulk-modal-merge-footer | — | |

## Methods

| Method | Description |
|--------|-------------|
| `setAggregations` | |
| `getList` | |
| `sortByIdsOrder` | |
| `getCounts` | |
| `getPropertyCounting` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `onDuplicate` | |
| `onCloseDuplicateModal` | |
| `onConfirmDuplicate` | |
| `onDetail` | |
| `onCloseDetailModal` | |
| `onCloseBulkMergeModal` | |
| `onMergeTags` | |
| `getBulkMergeMessageGlue` | |
| `onSaveFinish` | |
| `onFilter` | |
| `resetFilters` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `tagRepository` | |
| `tagDefinition` | |
| `assignmentProperties` | |
| `tagCriteria` | |
| `tagColumns` | |
| `assignmentFilterOptions` | |
| `hasAssignmentFilter` | |
| `filterCount` | |

## Examples

### Basic Usage
```twig
<sw-settings-tag-list>
    <!-- content -->
</sw-settings-tag-list>
```
