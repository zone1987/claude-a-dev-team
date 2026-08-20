# sw-condition-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| conditionDataProviderService | `any` | — | yes |  |
| condition | `any` | `null` | no |  |
| scopes | `any` | — | no |  |
| allowedTypes | `any` | `null` | no |  |
| childAssociationField | `any` | `'children'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConditionsChanged` | |
| `deleteAndClose` | |
| `saveAndCloseModal` | |
| `deleteChildren` | |
| `closeModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `conditionRepository` | |
| `initialConditions` | |

## Examples

### Basic Usage
```twig
<sw-condition-modal
    conditionDataProviderService="..."
>
    <!-- content -->
</sw-condition-modal>
```
