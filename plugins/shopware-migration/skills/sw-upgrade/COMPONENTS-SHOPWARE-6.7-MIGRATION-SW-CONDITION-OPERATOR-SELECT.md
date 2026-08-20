# sw-condition-operator-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| operators | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| plural | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `changeOperator` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `operator` | |
| `operatorClasses` | |
| `hasError` | |
| `translatedOperators` | |
| `conditionValueOperatorError` | |

## Examples

### Basic Usage
```twig
<sw-condition-operator-select
    operators="..."
    condition="..."
>
    <!-- content -->
</sw-condition-operator-select>
```
