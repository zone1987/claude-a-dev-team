# sw-settings-state-machine-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| stateMachineId | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStateMachine` | |
| `onChangeLanguage` | |
| `onCancel` | |
| `onSave` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `stateMachineRepository` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `stateMachineNameError` | |

## Examples

### Basic Usage
```twig
<sw-settings-state-machine-detail
    stateMachineId="..."
>
    <!-- content -->
</sw-settings-state-machine-detail>
```
