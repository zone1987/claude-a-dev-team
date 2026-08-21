# sw-condition-type-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| availableTypes | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| hasError | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| availableGroups | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `changeItem` | |
| `changeType` | |
| `getTooltipConfig` | |
| `groupAssignments` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `valueProperty` | |
| `ucTerm` | |
| `typeOptions` | |
| `typeSelectClasses` | |
| `arrowColor` | |

## Examples

### Basic Usage
```twig
<sw-condition-type-select
    availableTypes="..."
    condition="..."
>
    <!-- content -->
</sw-condition-type-select>
```
