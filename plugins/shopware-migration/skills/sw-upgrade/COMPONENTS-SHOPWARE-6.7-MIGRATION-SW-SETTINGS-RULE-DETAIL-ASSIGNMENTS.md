# sw-settings-rule-detail-assignments

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| conditions | `any` | `null` | no |  |
| detailPageLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `disableAdd` | |
| `getTooltipConfig` | |
| `allowDeletion` | |
| `prepareAssociationEntitiesList` | |
| `onOpenDeleteModal` | |
| `onCloseDeleteModal` | |
| `onOpenAddModal` | |
| `onCloseAddModal` | |
| `onEntitiesSaved` | |
| `onDeleteItems` | |
| `onDelete` | |
| `doDeleteItem` | |
| `refreshAssignmentData` | |
| `onFilterEntity` | |
| `loadNotAssignedDataTotals` | |
| `getRouterLink` | |
| `loadAssociationData` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `getRuleAssignmentConfiguration` | |
| `associationEntitiesConfig` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-settings-rule-detail-assignments
    rule="..."
>
    <!-- content -->
</sw-settings-rule-detail-assignments>
```
