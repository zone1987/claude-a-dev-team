# sw-flow-app-action-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChange` | |
| `isValid` | |
| `handleValid` | |
| `onSave` | |
| `buildConfig` | |
| `onClose` | |
| `getFields` | |
| `convertDefaultValue` | |
| `getConfig` | |
| `helpText` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `actionLabel` | |
| `appBadge` | |
| `currentLocale` | |
| `headline` | |
| `paragraph` | |

## Examples

### Basic Usage
```twig
<sw-flow-app-action-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-app-action-modal>
```
