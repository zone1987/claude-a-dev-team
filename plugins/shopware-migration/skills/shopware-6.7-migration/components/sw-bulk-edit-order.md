# sw-bulk-edit-order

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setRouteMetaModule` | |
| `loadBulkEditData` | |
| `fetchStatusOptions` | |
| `fetchStateMachineStates` | |
| `fetchToStateMachineTransitions` | |
| `toStateMachineStatesCriteria` | |
| `onProcessData` | |
| `openModal` | |
| `closeModal` | |
| `onSave` | |
| `getLatestOrderStatus` | |
| `loadCustomFieldSets` | |
| `onCustomFieldsChange` | |
| `onChangeDocument` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `selectedIds` | |
| `stateMachineStateRepository` | |
| `orderRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `hasChanges` | |
| `restrictedFields` | |
| `statusFormFields` | |
| `documentsFormFields` | |
| `tagsFormFields` | |

## Examples

### Basic Usage
```twig
<sw-bulk-edit-order>
    <!-- content -->
</sw-bulk-edit-order>
```
