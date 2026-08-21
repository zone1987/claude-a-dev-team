# sw-bulk-edit-save-modal-confirm

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemTotal | `any` | — | yes |  |
| bulkEditData | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| title-set | — | |
| buttons-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isFlowTriggered` | |
| `triggeredFlows` | |

## Examples

### Basic Usage
```twig
<sw-bulk-edit-save-modal-confirm
    itemTotal="..."
>
    <!-- content -->
</sw-bulk-edit-save-modal-confirm>
```
