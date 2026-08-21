# sw-settings-rule-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| conditions | `any` | `null` | no |  |
| conditionRepository | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| ruleNameError | `any` | `null` | no |  |
| rulePriorityError | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| conditions-changed | — | |
| tree-finished-loading | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `hasProductStreamConditions` | |
| `hasConditionType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `availableModuleTypes` | |
| `moduleTypes` | |
| `showCustomFields` | |
| `productStreamIndexingEnabled` | |
| `showProductStreamIndexingWarning` | |
| `showProductStateConditionWarning` | |

## Examples

### Basic Usage
```twig
<sw-settings-rule-detail-base
    rule="..."
    conditionRepository="..."
>
    <!-- content -->
</sw-settings-rule-detail-base>
```
