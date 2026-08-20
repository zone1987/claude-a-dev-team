# sw-flow-set-order-state-modal

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
| `getAllStates` | |
| `generateOptions` | |
| `buildTransitionOptions` | |
| `onClose` | |
| `onAddAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineState` | |

## Examples

### Basic Usage
```twig
<sw-flow-set-order-state-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-set-order-state-modal>
```
