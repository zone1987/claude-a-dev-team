# sw-flow-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-update-total | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createComponent` | |
| `getList` | |
| `isValidTrigger` | |
| `onDuplicateFlow` | |
| `onEditFlow` | |
| `onDeleteFlow` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `updateRecords` | |
| `getTranslatedEventName` | |
| `selectionChange` | |
| `deleteWarningMessage` | |
| `bulkDeleteWarningMessage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `flowRepository` | |
| `flowCriteria` | |
| `flowColumns` | |
| `detailPageLinkText` | |
| `assetFilter` | |
| `triggerEvents` | |

## Examples

### Basic Usage
```twig
<sw-flow-list>
    <!-- content -->
</sw-flow-list>
```
