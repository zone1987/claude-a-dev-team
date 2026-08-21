# sw-flow-change-customer-group-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerGroupRepository` | |
| `customerGroupCriteria` | |
| `customerGroups` | |

## Examples

### Basic Usage
```twig
<sw-flow-change-customer-group-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-change-customer-group-modal>
```
